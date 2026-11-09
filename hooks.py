from pathlib import Path
import datetime
import re
import subprocess

# 文件夹路径与显示分类名称映射
CATEGORY_MAP = {
    "general_physics": "数理基础 · 普通物理",
    "probability_theory_and_statistics": "数理基础 · 概率统计",
    "numerical_analysis": "数理基础 · 数值分析",
    "mathematical_sciences": "数理基础",
    "computer_science": "计算机科学",
    "artificial_intelligence": "人工智能",
    "misc": "杂项与探索",
}

def get_md_title(file_path: Path) -> str:
    """提取 Markdown 文件的第一行一级标题，若无则返回文件名"""
    try:
        content = file_path.read_text(encoding="utf-8")
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return file_path.stem

def count_notes(docs_dir: Path, subpath: str) -> int:
    """统计指定板块下非 index.md 的笔记总数"""
    target = docs_dir / subpath
    if not target.exists():
        return 0
    return len([p for p in target.rglob("*.md") if p.name != "index.md"])

def get_recent_git_commits(limit: int = 4) -> str:
    """提取最近 N 条 git commit -m 的提交信息、短哈希与提交时间"""
    try:
        output = subprocess.check_output(
            [
                "git", "log", f"-n {limit}",
                "--pretty=format:%h|%ad|%s",
                "--date=format:%Y-%m-%d %H:%M"
            ],
            encoding="utf-8",
            stderr=subprocess.DEVNULL
        )
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        if not lines:
            return "- 暂无 Git 提交记录"

        md_items = []
        for line in lines:
            parts = line.split("|", 2)
            if len(parts) == 3:
                commit_hash, commit_date, commit_msg = parts
                md_items.append(
                    f"- **`[{commit_hash}]`** `{commit_date}` — **{commit_msg}**"
                )
        return "\n".join(md_items)
    except Exception:
        return "- 暂未检测到 Git 仓库或提交记录"

def on_serve(server, config, builder, **kwargs):
    """监听 Git 提交日志，执行 git commit 后自动触发网页热重载"""
    git_head_log = Path(".git/logs/HEAD")
    if git_head_log.exists():
        server.watch(str(git_head_log), builder)
    return server

def on_page_markdown(markdown: str, page, config, files, **kwargs) -> str:
    if page.file.src_uri != "index.md":
        return markdown

    docs_dir = Path(config["docs_dir"])

    # 1. 自动统计四大板块笔记数
    c_cs = count_notes(docs_dir, "computer_science")
    c_math = count_notes(docs_dir, "mathematical_sciences")
    c_ai = count_notes(docs_dir, "artificial_intelligence")
    c_misc = count_notes(docs_dir, "misc")

    all_notes = [
        p for p in docs_dir.rglob("*.md")
        if p.name not in ("index.md", "about.md")
    ]
    total_notes = len(all_notes)

    # 2. 自动生成最近更新的 6 个文件表格
    all_notes.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    recent_rows = [
        "| 所属板块 | 文件标题 | 最后修改时间 | 快速入口 |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for note in all_notes[:6]:
        rel_path = note.relative_to(docs_dir).as_posix()
        title = get_md_title(note)
        mtime = datetime.datetime.fromtimestamp(note.stat().st_mtime).strftime("%Y-%m-%d %H:%M")

        cat_name = "未分类"
        for folder_key, label in CATEGORY_MAP.items():
            if folder_key in rel_path:
                cat_name = label
                break

        recent_rows.append(
            f"| **{cat_name}** | {title} | `{mtime}` | [打开文件]({rel_path}) |"
        )

    recent_table_md = "\n".join(recent_rows)

    # 3. 自动获取最近 4 条 git commit -m 记录
    git_commits_md = get_recent_git_commits(4)

    # 4. 替换首页占位符
    replacements = {
        "{{ total_notes }}": str(total_notes),
        "{{ count_cs }}": str(c_cs),
        "{{ count_math }}": str(c_math),
        "{{ count_ai }}": str(c_ai),
        "{{ count_misc }}": str(c_misc),
        "{{ auto_recent_table }}": recent_table_md,
        "{{ auto_git_commits }}": git_commits_md,
    }

    for k, v in replacements.items():
        markdown = markdown.replace(k, v)

    return markdown
