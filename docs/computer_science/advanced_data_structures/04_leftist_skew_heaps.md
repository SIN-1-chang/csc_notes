# Chapter 4: Leftist Heaps and Skew Heaps（左式堆与斜堆）

!!! abstract
    Advanced Data Structures and Algorithm Analysis (ADS) | 第四章课堂、板书与讲义笔记
    
    参考：
    
    - Course Slides Lecture 4: *Leftist Heaps and Skew Heaps*
    - 课堂手写板书 (`ADS26W4.pdf`, Pages 1–6) & 课程讲义 Lecture 4:《左式堆与斜堆》
    - M. A. Weiss, *Data Structures and Algorithm Analysis in C* (2nd Ed.), Ch. 6.6–6.7 & Ch. 11.3

## 1 左式堆 / 左偏堆 (Leftist Heaps)

### 1.1 可合并堆的引入与二叉堆的局限

在基础数据结构中，标准的**二叉堆**（Binary Heap，以下默认讨论**最小堆 Min-Heap**）由两条性质唯一规定：

1. **结构性质（Structure Property）**：是一棵**完全二叉树**（Complete binary tree），树高严格满足 $h = \lfloor\log_2 N\rfloor = O(\log N)$，且可直接用紧凑的一维数组实现（无需显式存储左右孩子指针）；
2. **堆序性质（Order Property）**：任意节点的键值大于等于其父节点的键值（$\forall v \neq \text{root}, \ \text{key}(v) \ge \text{key}(\text{parent}(v))$），因此全局最小元恒位于根节点。

虽然二叉堆能以 $O(1)$ 时间完成 `FindMin`、以 $O(\log N)$ 时间完成 `Insert`（尾插 + 上滤 Percolate up）、`DeleteMin`（尾元替根 + 下滤 Percolate down）、`DecreaseKey` 和 `Delete`，并以 $O(N)$ 时间完成线性建堆 `BuildHeap`，但它在处理**两个堆的合并（`Merge`）**时效率极低：

!!! question "Discussion 5: 如果直接使用标准二叉堆结构，合并两个堆最快需要多少时间？"
    由于数组实现的完全二叉树要求所有元素在内存中连续紧凑排列，合并两个规模分别为 $n_1$ 和 $n_2$（记 $N = n_1 + n_2$）的二叉堆时：
    
    - **方法 1**：将较小堆的元素逐个 `Insert` 到较大堆中，耗时 $O(\min(n_1, n_2)\log N)$（当 $n_1 \approx n_2 \approx N/2$ 时退化为 $O(N\log N)$）；
    - **方法 2**：直接将两个数组拼接在一起，然后调用自底向上的线性建堆算法 `BuildHeap`，最坏与平均时间复杂度均为 **$\Theta(n_1 + n_2) = \Theta(N)$**。
    
    **设计目标（Target）**：为了在支持高效合并的场景中将 `Merge` 从 $O(N)$ 加速至 **$O(\log N)$**，我们必须放弃数组与完全二叉树的结构限制，改用**基于指针的二叉树（Pointer-based binary tree）**，这就是**左式堆（Leftist Heap）**与**斜堆（Skew Heap）**的由来。

**核心直觉辨析：为什么搜索树要求越平衡越好，而左式堆却故意设计成极度不平衡（向左倾斜）？**
因为堆**不需要支持任意键值的查找 `Find(x)`**！左式堆的核心思想是：**将左子树做得非常深、把绝大多数节点都堆积在左侧（Biased to get deep toward the left），从而保证右侧路径（Right path）极其短（$O(\log N)$）**。在执行 `Merge`、`Insert` 和 `DeleteMin` 时，左边庞大的子树完全不需要被访问，所有实质性工作全部集中在短短的**右路径**上完成！

### 1.2 零路径长 (Null Path Length, NPL) 与左式堆定义

为了严格量化“二叉树向左倾斜”的程度，引入**零路径长**（Null Path Length, 简记为 `Npl`）的概念：

**定义 1.1（零路径长 Null Path Length, `Npl(X)`）**：
任意节点 $X$ 的零路径长 $\text{Npl}(X)$ 定义为从 $X$ 出发到达一个**不满节点（即没有两个孩子的节点：度为 $0$ 的叶节点或度为 $1$ 的单孩子节点）**的最短路径长度（按边数计）。特别规定空节点的零路径长为：

$$\text{Npl}(\text{NULL}) = -1$$

由此可得 `Npl(X)` 的局部递推计算公式（从叶节点向上递推）：

$$\text{Npl}(X) = \min\big\{\text{Npl}(X.\text{left}), \ \text{Npl}(X.\text{right})\big\} + 1$$

- 具有 $0$ 个或 $1$ 个孩子的节点（至少有一个 `NULL` 孩子），其 $\text{Npl} = \min\{\dots, -1\} + 1 = 0$。

!!! warning "符号约定对比：课程组 PPT / 教材约定 vs. 老师手写板书约定"
    - **课程组 PPT 与 Weiss 教材标准约定（考试做题默认采用）**：定义 $\text{Npl}(\text{NULL}) = -1$，因此叶节点与单孩子节点的 $\text{Npl} = 0$（代表从 $X$ 到不满节点的**边数**）。
    - **