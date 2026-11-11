# Chapter 3: Inverted File Index（倒排文件索引）

!!! abstract
    Advanced Data Structures and Algorithm Analysis (ADS) | 第三章课堂与讲义笔记
    
    参考：
    
    - Course Slides Lecture 3: *Inverted File Index* (Student & Teacher Versions)
    - 课程讲义 Lecture 3:《倒排索引》
    - C. D. Manning, P. Raghavan, H. Schütze, *Introduction to Information Retrieval*

## 1 倒排索引的引入与基本结构 (Introduction and Basic Structure)

### 1.1 从顺序扫描、关联矩阵到倒排索引

在现代信息检索系统（如 Google 等Web搜索引擎）中，核心任务是从海量已抓取的网页或文档集合中，快速找出包含特定查询词（如 `"Computer Science"` 或 `"silver" AND "truck"`）的所有文档。我们对比三种演进方案：

**1. 方案一：逐篇顺序扫描（Naive String Scanning / `grep`）**
每次收到查询时，直接从头到尾扫描每一篇文档中的文本字符串。当文档规模达到十亿（Billion）乃至千亿级网页时，在线扫描的响应时间完全不可接受（*"Wait till your next life!"*）。

**2. 方案二：词项-文档关联矩阵（Term-Document Incidence Matrix）**
预先建立一个二元 0-1 矩阵，行代表全部互异词项（Terms，设共有 $V$ 个），列代表全部文档（Documents，设共有 $N$ 篇）。若词项 $t$ 出现在文档 $d$ 中，则矩阵元 $(t, d) = 1$，否则为 $0$。

例如，给定以下 4 篇短文档集合：

| Doc ID | Document Text |
| :---: | :--- |
| **Doc 1** | `Gold silver truck` |
| **Doc 2** | `Shipment of gold damaged in a fire` |
| **Doc 3** | `Delivery of silver arrived in a silver truck` |
| **Doc 4** | `Shipment of gold arrived in a truck` |

其对应的**词项-文档关联矩阵**为：

| Term \ Doc | Doc 1 | Doc 2 | Doc 3 | Doc 4 |
| :--- | :---: | :---: | :---: | :---: |
| `a` | 0 | 1 | 1 | 1 |
| `arrived` | 0 | 0 | 1 | 1 |
| `damaged` | 0 | 1 | 0 | 0 |
| `delivery` | 0 | 0 | 1 | 0 |
| `fire` | 0 | 1 | 0 | 0 |
| `gold` | 1 | 1 | 0 | 1 |
| `in` | 0 | 1 | 1 | 1 |
| `of` | 0 | 1 | 1 | 1 |
| `shipment` | 0 | 1 | 0 | 1 |
| `silver` | 1 | 0 | 1 | 0 |
| `truck` | 1 | 0 | 1 | 1 |

- **布尔查询处理**：若查询 `silver & truck`，只需直接取出 `silver` 的行向量 `1010` 与 `truck` 的行向量 `1011` 进行按位逻辑与（Bitwise `AND`），得到 `1010`，立即得知匹配文档为 **Doc 1** 和 **Doc 3**。
- **致命缺陷（空间爆炸）**：在真实搜索引擎中，若词表规模 $V \approx 10^6$、文档数 $N \approx 10^9$，则完整矩阵包含 $V \times N = 10^{15}$ 个比特，但**绝大多数位置全为 $0$（极度稀疏 Sparse）**，造成灾难性的空间浪费。

**3. 方案三：紧凑表示——倒排文件索引（Inverted File Index）**

既然关联矩阵极度稀疏，我们只需记录矩阵中取值为 `1` 的位置！

- **定义 3.1（索引 Index 与倒排文件 Inverted File）**：
  - **索引（Index）**：用于在文本中定位给定词项（Term）的一种机制。
  - **倒排文件 / 倒排索引（Inverted File / Inverted Index）**：之所以称为“倒排（Inverted）”，是因为它将正向的“文档 $\to$ 包含的单词列表”反转过来，变成以**词项（Term）**为主键，列出所有包含该词项的文档指针列表。
  - 倒排索引由两部分组成：**词典（Term Dictionary）** + **倒排表 / 倒排记录表（Posting Lists）**。

### 1.2 文档级倒排索引 vs. 位置倒排索引 (Positional Index)

根据倒排表（Posting List）中记录粒度的不同，倒排索引分为基础文档级倒排索引与带词位置的位置倒排索引：

| No. | Term（词典词项） | 版本 A：基础倒排表 `<Times; Documents>` | 版本 B：位置倒排表 `<Times; (Doc; Words...)>` |
| :-: | :--- | :--- | :--- |
| 1 | `a` | `<3; 2, 3, 4>` | `<3; (2; 6), (3; 6), (4; 6)>` |
| 2 | `arrived` | `<2; 3, 4>` | `<2; (3; 4), (4; 4)>` |
| 3 | `damaged` | `<1; 2>` | `<1; (2; 4)>` |
| 4 | `delivery` | `<1; 3>` | `<1; (3; 1)>` |
| 5 | `fire` | `<1; 2>` | `<1; (2; 7)>` |
| 6 | `gold` | `<3; 1, 2, 4>` | `<3; (1; 1), (2; 3), (4; 3)>` |
| 7 | `of` | `<3; 2, 3, 4>` | `<3; (2; 2), (3; 2), (4; 2)>` |
| 8 | `in` | `<3; 2, 3, 4>` | `<3; (2; 5), (3; 5), (4; 5)>` |
| 9 | `shipment` | `<2; 2, 4>` | `<2; (2; 1), (4; 1)>` |
| 10 | `silver` | `<2; 1, 3>` | `<2; (1; 2), (3; 3, 7)>` |
| 11 | `truck` | `<3; 1, 3, 4>` | `<3; (1; 3), (3; 8), (4; 7)>` |

- **文档频率（Document Frequency, $df(t)$ / `Times`）**：分号前的第一个数字，表示包含词项 $t$ 的不同文档总数（例如 `silver` 出现在 Doc 1 和 Doc 3 共 2 篇文档中，故 $df(\text{silver}) = 2$）。
- **词频（Term Frequency, $tf(t, d)$）**：词项 $t$ 在单篇文档 $d$ 内部出现的次数（例如在 Doc 3 中，`silver` 出现在第 3 和第 7 个单词位置，故 $tf(\text{silver}, D_3) = 2$）。

!!! question "课堂核心思考题（Slide 6 Q&A）：为什么要保存位置信息与 `Times`（文档频率 $df$）？"
    1. **Q1: 如何利用位置倒排表快速支持短语查询、打印包含检索词的句子并高亮（Highlight）关键词？**
       - **短语与邻近查询（Phrase & Proximity Queries）**：若用户查询精确短语 `"silver truck"`，仅靠文档级倒排表只能知道 Doc 1 和 Doc 3 同时含有这两个词，但无法判断它们是否紧挨着且顺序正确。有了位置列表后，在 Doc 1 中 `silver` 位于位置 `2`、`truck` 位于位置 `3`（$3 - 2 = 1$）；在 Doc 3 中 `silver` 位于 `3, 7`、`truck` 位于 `8`（$8 - 7 = 1$），立即判定两篇文档均包含连续短语 `"silver truck"`！
       - **上下文摘要提取与高亮（Snippet Extraction & Highlighting）**：返回搜索结果时，无需重新全文匹配，直接根据 `(DocID; WordPos)` 定位到原文档对应偏移量处，截取前后相邻单词生成摘要片段，并将对应位置直接高亮显示。
    2. **Q2: 为什么要在倒排表头部专门维护 `Times`（即文档频率 $df(t)$）？**
       - **优化多词布尔 `AND` 查询的求交顺序（核心考点）**：当执行多词交集查询 $t_1 \text{ AND } t_2 \text{ AND } \dots \text{ AND } t_k$ 时，**应当先将所有查询词按 `Times`（$df$）从小到大升序排列，优先合并最短的倒排表**！因为交集结果的长度绝不会超过参与求交的最短列表长度，先对最稀有的词求交能以最小代价迅速将中间候选集缩小，大幅减少后续长列表的比较次数。
       - **用于查询截断（Query Thresholding）与相关性权重计算（如 TF-IDF）**：在查询词截断时丢弃高频低区分度词，或在计算逆文档频率 $\text{IDF}(t) = \log(N / df(t))$ 时直接使用。

### 1.3 有序倒排表的布尔查询算法 (Intersection and Union of Posting Lists)

由于每个词项的倒排表中文档编号（DocID）严格递增排列，求两个倒排表 $A$ 和 $B$ 的交集（`AND`）或并集（`OR`）可采用经典的**双指针同步线性扫描算法**，时间复杂度仅为 $O(\vert{}A\vert{} + \vert{}B\vert{})$：

```c
/* 输入：按 DocID 严格递增的单链表 A, B；mode 为 AND (交集) 或 OR (并集) */
PostingList BooleanQuery(PostingList A, PostingList B, QueryMode mode) {
    Position p = A, q = B;
    PostingList C = CreateEmptyList();
    while (p != NULL && q != NULL) {
        if (p->id == q->id) {
            Append(C, p->id);
            p = p->next;
            q = q->next;
        } else if (p->id < q->id) {
            if (mode == OR) Append(C, p->id);
            p = p->next;
        } else {
            if (mode == OR) Append(C, q->id);
            q = q->next;
        }
    }
    if (mode == OR) {
        while (p != NULL) { Append(C, p->id); p = p->next; }
        while (q != NULL) { Append(C, q->id); q = q->next; }
    }
    return C;
}
```

---

## 2 索引构建流水线与文本预处理 (Index Construction & Text Preprocessing)

### 2.1 索引生成器 (Index Generator) 基本框架

构建倒排索引的基础流程是逐篇读取文档 $D$、逐个切分出词项 $T$，并在词典中查找和更新对应的倒排表：

```c
while ( read a document D ) {
    while ( read a term T in D ) {              /* 模块 1: Token Analyzer & Stop Filter */
        if ( Find( Dictionary, T ) == false )   /* 模块 2: Vocabulary Scanner */
            Insert( Dictionary, T );            /* 模块 3: Vocabulary Insertor */
        Get T's posting list;
        Insert a node to T's posting list;      /* 将当前文档号及位置追加到链表尾部 */
    }
}
Write the inverted index to disk;               /* 模块 4: Memory Management */
```

### 2.2 文本预处理：分词、词干提取与停用词过滤

在 `read a term T in D` 阶段（Token Analyzer & Stop Filter），原始文本需要经过以下标准化处理（注意：**查询时必须对用户输入的查询词执行完全相同的预处理规则**）：

1. **分词与归一化（Tokenization & Normalization）**：
   识别标点、连字符与空格边界，将英文文本切分为独立单词并统一转换为小写（Case-folding，如 `Truck` $\to$ `truck`）；对于中文等无空格分隔的语言，则需借助词典（如最大匹配法）或统计语言模型进行中文分词（Word Segmentation）。
2. **词干提取（Word Stemming）与词形还原（Lemmatization）**：
   剥离单词的词缀或曲折变化，只保留词根（Stem / Root form），使同一语义的不同语法形式归并到同一个词项下：
   - $\text{Process, processing, processes, processed} \implies \text{\textbf{process}}$
   - $\text{says, said, saying} \implies \text{\textbf{say}}$
   - **优缺点权衡**：能够显著缩减词典规模并提高召回率（Recall）；但基于简单规则的词干提取可能把本义不同的词错误归并（Over-stemming），降低查准率（Precision）。
3. **停用词消除（Stop Words Removal）**：
   像 `"a"`, `"the"`, `"it"`, `"of"`, `"in"` 这类词在几乎所有文档中都高频出现，其倒排表极长但对区分文档主题毫无帮助。这类词称为**停用词**（Stop words），通常在建索引前直接从原文档流中滤除。
   - *位置索引中的细节*：即使滤除了停用词，**其余正常词项仍应保留其在原文中的真实位置编号**（例如 `"silver a truck"` 中 `silver` 在 1、`truck` 在 3，不能重编号为 1 和 2，否则会被误判为连续短语 `"silver truck"`）；若系统需支持 `"to be or not to be"` 等完全由停用词构成的短语查询，则不能简单丢弃停用词。

### 2.3 词典的数据结构选型：搜索树 vs. 哈希表

在访问词典（Vocabulary Scanner & Insertor：执行 `Find(Dictionary, T)` 与 `Insert(Dictionary, T)`）时，主要有两类数据结构可选：

| 对比维度 | 方案 1：搜索树（Search Trees: B-树、B+ 树、Trie 字典树） | 方案 2：哈希表（Hashing / Hash Table） |
| :--- | :--- | :--- |
| **单词精确查找速度** | 较快：平衡树为 $O(\log V)$，Trie 树为 $O(\vert{}T\vert{})$ | **极快（优势）**：期望时间 $O(1)$（Faster for one word） |
| **有序性与范围查询** | **支持（核心优势）**：词项按字典序排列，天然支持按序遍历、**范围查询（Range searches）**及**前缀通配符查询**（如 `comp*`） | **不支持（致命缺陷）**：无法按字典序扫描，范围查询与前缀匹配代价极高（Sequential scanning / range searches are expensive） |
| **动态扩容开销** | 节点分裂局部完成，无全局停顿 | 负载因子过高时需触发全表 Rehash，且存在哈希冲突开销 |

---

## 3 大规模索引工程优化 (Large-Scale Indexing Optimizations)

### 3.1 内存受限下的外存分块归并构建 (Out-of-Core Indexing)

当文档集合极其庞大时，内存无法装下完整的倒排索引。此时需引入**基于分块的外部归并索引构建策略**（Memory Management，如 BSBI / SPIMI 算法）：

```c
BlockCnt = 0;
while ( read a document D ) {
    while ( read a term T in D ) {
        if ( out of memory ) { /* 内存空间耗尽时触发落盘 */
            Write the block index (sorted by term) to disk as Block[BlockCnt++];
            Clear in-memory dictionary and posting lists (free memory);
        }
        if ( Find( Dictionary, T ) == false )
            Insert( Dictionary, T );
        Get T's posting list;
        Insert a node to T's posting list;
    }
}
Write the final block index to disk;
Merge all sorted block indices on disk into the final inverted index; /* 多路外部归并 */
```

由于每个内存块在写入磁盘前已按词项字典序排好序，且块内每个倒排表都是按文档号递增生成的，最后的合并阶段只需对磁盘上的各个块执行一次线性顺序扫描的**多路归并（Multi-way Merge）**即可生成全局倒排索引。

### 3.2 分布式索引架构 (Distributed Indexing)

在 Web 级搜索引擎中，单台服务器无法存储或响应全局索引，必须将索引切分到多台机器组成的集群上。共有两种划分架构：

| 特性维度 | 方案 1：按词项划分（Term-Partitioned Index） | 方案 2：按文档划分（Document-Partitioned Index） |
| :--- | :--- | :--- |
| **切分方式** | 按词项字母范围（如 Node 1 存 `A~C`，Node 2 存 `D~F`，…，Node $K$ 存 `X~Z`）划分，每台机器存所辖词项的**全局完整倒排表** | 按文档 ID 范围（如 Node 1 存 `1~10000`，Node 2 存 `10001~20000`…）划分，每台机器只存**本地文档子集的独立倒排索引** |
| **单词查询处理** | 只需将请求路由给负责该词项的 **1 台机器** | 必须将查询广播给**所有机器**，再汇总结果 |
| **多词 `AND` 查询** | 需从多台机器拉取长倒排表在节点间传输求交，**网络通信开销极大** | 每台机器在**本地独立完成多词求交**，只将极少量的最终匹配文档 ID 发回主节点合并，网络通信极小 |
| **负载均衡与容错** | **差**：高频热门词所在节点会成为性能瓶颈（Hotspot）；单节点宕机导致整批词项彻底无法检索 | **极佳（主流搜索引擎实际采用方案）**：查询负载均匀分布在所有节点上；单机故障仅损失少量文档，不影响系统可用性 |

### 3.3 动态索引 (Dynamic Indexing)

真实世界中的网页不断新增、修改和删除。若每次文档更新都原地重构巨大的主索引（Main Index），I/O 代价过高。工程上采用**主索引 + 辅助索引 + 删除位图**的准实时架构：

1. **新增文档（New Docs）**：先在内存中维护一个较小的**辅助索引**（Auxiliary index），新文档直接写入辅助索引；
2. **检索查询（Search）**：每次查询**同时检索磁盘上的主索引和内存中的辅助索引**，将两者的结果集归并；
3. **删除与修改文档（Deletions & Updates）**：设置一个专门的**删除位向量 / 删除集合**（Invalidation bit-vector）。当某篇文档被删除时，仅在删除位图中将其 DocID 标记为已删除，在返回检索结果的最后一步过滤掉带有删除标记的文档；修改文档则直接视为“旧文档标记删除 + 新版本作为新文档插入辅助索引”；
4. **重索引（When to re-index）**：当内存中的辅助索引体积增长到超过设定阈值（或空闲时段）时，将辅助索引与磁盘主索引执行一次批量归并，并顺带物理清除所有已标记删除的倒排记录。

### 3.4 索引压缩技术 (Index Compression)

压缩索引不仅能节省磁盘空间，还能让更多索引常驻内存并加快磁盘向内存的 I/O 传输速度：

1. **词典压缩（单一长字符串表示 Dictionary-as-a-String）**：
   如果用定长字符数组存储每个词项（如每项分配 20 字节），短词会浪费大量空间，而超长词又装不下。改进方案是：先剔除停用词，再**将词典中的所有词项首尾相连拼接成一个无分隔符的连续长字符串**：
   ```text
   arrivedamagedeliverfiregoldshipmentsilvertruck...
   ^     ^     ^      ^   ^   ^       ^     ^
   ```
   词典表项中只需用定长整数指针指向每个词在该长字符串中的起始偏移位置（下一个词的起点即为当前词的终点）。
2. **倒排表压缩：差值编码 / 间距编码（Gap Encoding）**：
   倒排表中的文档编号是严格递增的正整数序列（如高频词 `computer` 的文档号序列可能跨度很大）。我们不直接存储原始的绝对文档号（如每个 ID 占 20 bits 或 32 bits），而是存储**相邻两个文档号之间的差值（Gaps）**：
   - **原始文档 ID 序列**：`2, 15, 47, ..., 58879, 58890, ...`
   - **差值（Gap）序列**：`2, 13, 32, ..., 11, ...`（其中 $13 = 15 - 2, \ 32 = 47 - 15, \ 11 = 58890 - 58879$）
   对于高频词，绝大多数相邻文档号的间距（Gap）都是极小的整数，配合**变长字节编码**（Variable-Byte encoding）或 $\gamma$ 编码，可以用远少于 20 bits 的位数表示每个间距；解码时只需从头累加差值即可还原全部文档 ID（为支持快速跳跃，可将倒排表分块并在块头记录绝对起始 ID）。

### 3.5 阈值截断优化 (Thresholding)

为了在海量候选集中进一步提升响应速度并控制返回规模，在文档端和查询端均可设置阈值（Thresholding）：

1. **文档端截断（Document Thresholding）**：
   根据相关性权重（Weight）对文档排序，**仅检索并返回得分最高的前 $x$ 篇文档（Top-$x$ retrieval）**。
   - *局限性*：① **不适用于布尔查询**（Not feasible for Boolean queries，因为布尔查询只有满足与不满足，无权重等级之分）；② 由于提前截断（Truncation），可能会漏掉排在 $x$ 名之后的部分相关文档。
2. **查询词端截断（Query Thresholding）**：
   当用户输入的查询包含较多词项（如长句查询 $T_1, T_2, \dots, T_{10}$）时，先将所有查询词按其**文档频率 $df$ 从小到大升序排列**（越靠前的词越稀有、信息量越大）。然后根据性能需求，**仅截取前 $p\%$（如前 $20\%, 40\%, 80\%$）最稀有的查询词进行检索**，忽略后面高频低区分度的词项。

---

## 4 搜索引擎性能评测与相关性指标 (Search Engine Evaluation Metrics)

### 4.1 数据检索 vs. 信息检索

评价一个搜索引擎的表现，除了考察底层的工程指标——**建索引速度**（Number of documents/hour）、**检索延迟**（Search latency as a function of index size）以及**查询语言的表达能力**（Expressiveness of query language）外，最核心的问题是：**如何衡量“用户满意度（User Happiness）”？**

这里必须严格区分两个概念：

- **数据检索（Data Retrieval）**：给定明确无误的布尔或正则条件，要求找出所有精确匹配的记录。在确保结果正确性的前提下，其性能完全由**响应时间（Response time）**和**索引空间开销（Index space）**决定。
- **信息检索（Information Retrieval, IR）**：用户通过自然语言查询寻求解决某个信息需求。因此除了时间与空间外，最核心的评价标准是：**返回的结果集与用户需求的“相关性（Relevance）”有多高？**

###