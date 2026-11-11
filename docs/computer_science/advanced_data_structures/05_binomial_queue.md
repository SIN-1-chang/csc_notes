# Chapter 5: Binomial Queue（二项队列 / 二项堆）

!!! abstract
    Advanced Data Structures and Algorithm Analysis (ADS) | 第五章课堂、板书与讲义笔记
    
    参考：
    
    - Course Slides Lecture 5: *Binomial Queue*
    - 课堂手写板书 (`ADS26W4.pdf` Pages 6–11) & 课程讲义 Lecture 5:《二项堆》
    - M. A. Weiss, *Data Structures and Algorithm Analysis in C* (2nd Ed.), Ch. 6.8 & Ch. 11.2; *CLRS* (3rd Ed.), Ch. 19

## 1 二项队列的引入与结构性质 (Structure of Binomial Queues)

### 1.1 引入动机：突破插入操作的 $O(\log N)$ 瓶颈

在第四章中，左偏堆（Leftist Heap）和斜堆（Skew Heap）成功将两个优先队列的合并（`Merge`）加速到了 $O(\log N)$，其单次插入（`Insert`）作为合并的特例也是 $O(\log N)$。然而，普通二叉堆虽然不支持高效合并，却能在离线已知全部 $N$ 个元素时通过 `BuildHeap` 在 $O(N)$ 时间内建堆（平均每个元素 $O(1)$）。

这就引出了一个自然的问题：**当元素逐个在线（On-line）动态到来时，是否存在一种可合并堆，既能保持 $O(\log N)$ 的最坏合并与删除最小值时间，又能使单次插入的摊还时间降为常数 $O(1)$（即从空堆开始连续执行 $N$ 次 `Insert` 的最坏总时间仅为 $O(N)$）？**
**二项队列**（Binomial Queue，又称**二项堆** Binomial Heap）正是为了实现这一目标而设计的。

### 1.2 二项树 ($B_k$) 的递归定义与二项式性质

与普通二叉堆、左偏堆或斜堆不同，**二项队列不是一棵单一的堆序树，而是由若干棵堆序树组成的集合，即一片森林（Forest）**。森林中的每一棵树都具有严格规定的形态，称为**二项树**（Binomial Tree）：

**定义 1.1（二项树 Binomial Tree, $B_k$）**：
- 高度为 $0$ 的二项树 $B_0$ 是一棵单节点树（One-node tree）；
- 高度为 $k \ (k \ge 1)$ 的二项树 $B_k$，是通过将一棵高度为 $k - 1$ 的二项树 $B_{k-1}$ 直接挂接到另一棵高度为 $k - 1$ 的二项树 $B_{k-1}$ 的根节点下方（作为其新的最左子树）而构成的：

```text
  B0       B1          B2                 B3
  o        o           o                  o
           |          / \               / | \
           o         o   o             o  o  o
                         |                |  |\
                         o                o  o o
                                               |
                                               o
```

**定理 1.1（二项树 $B_k$ 的四大结构性质，Slide 2 Observation & 板书 `W4` Page 7）**：
对于任意整数 $k \ge 0$，高度为 $k$ 的二项树 $B_k$ 满足：

1. **根节点的子树分解**：$B_k$ 的根节点恰好有 **$k$ 个孩子**（即根节点的扇出度 Fanout $= k$），从左到右（或按高度递增）依次为 **$B_0, B_1, B_2, \dots, B_{k-1}$**；
2. **总节点数**：$B_k$ 恰好包含 **$2^k$ 个节点**；
3. **各层节点数的二项式系数分布**：在深度为 $d \ (0 \le d \le k)$ 的层上，恰好有 **$\dbinom{k}{d}$ 个节点**（这正是“二项树”名称的由来！）。

<details markdown="1">
<summary>点击展开：定理 1.1 的数学归纳法证明</summary>

**证明（对二项树的阶数 / 高度 $k$ 作数学归纳）**：

- **归纳基（$k = 0$）**：$B_0$ 只有一个根节点，孩子数为 $0$，总节点数为 $2^0 = 1$，深度 $d = 0$ 处有 $\binom{0}{0} = 1$ 个节点，命题成立。
- **归纳假设**：假设当阶数为 $k - 1$ 时命题成立，即 $B_{k-1}$ 的根有孩子 $B_0, \dots, B_{k-2}$，总节点数为 $2^{k-1}$，且深度 $d$ 处有 $\binom{k-1}{d}$ 个节点。
- **归纳步（考察 $B_k$）**：
  由定义，$B_k$ 是将一棵 $B_{k-1}$ 挂接到另一棵 $B_{k-1}$ 的根下构成的：
  1. 原根本来已有孩子 $B_0, \dots, B_{k-2}$，新挂入一棵 $B_{k-1}$ 后，其孩子恰好变为 $B_0, B_1, \dots, B_{k-1}$，共 $k$ 个孩子；
  2. 总节点数为 $2^{k-1} + 2^{k-1} = 2^k$；
  3. 考察 $B_k$ 中深度为 $d \ (1 \le d \le k-1)$ 的节点：它们一部分来自原本作为根的那棵 $B_{k-1}$ 的第 $d$ 层（共有 $\binom{k-1}{d}$ 个），另一部分来自被挂接下移一层的那棵 $B_{k-1}$ 的第 $d - 1$ 层（下移后深度变为 $d$，共有 $\binom{k-1}{d-1}$ 个）。由帕斯卡恒等式（Pascal's identity）：
     $$\text{\# nodes at depth } d = \binom{k-1}{d} + \binom{k-1}{d-1} = \binom{k}{d}$$
     对于边界层 $d = 0$ 和 $d = k$，节点数均为 $1 = \binom{k}{0} = \binom{k}{k}$，归纳完成。

</details>

### 1.3 二项队列的定义与二进制唯一表示定理

**定义 1.2（二项队列 Binomial Queue）**：
一个二项队列是由若干棵二项树组成的森林，且同时满足以下两条性质：

1. **堆序性（Heap Order）**：森林中的每一棵二项树 $B_k$ 内部均满足最小堆（或最大堆）的序性质，即每个节点的键值大于等于其父节点的键值；
2. **高度唯一性（Distinct Heights）**：森林中**每种高度 $k$ 的二项树至多只能有一棵**（即要么有 1 棵 $B_k$，要么没有 $B_k$）。

**核心结论：与二进制数的同构对应（Unique Binary Representation）**
由于一棵 $B_k$ 恰好有 $2^k$ 个节点，且每种高度 $k$ 至多出现一次，将节点总数 $N$ 写成二进制展开：

$$N = \sum_{k=0}^{\lfloor\log_2 N\rfloor} b_k 2^k, \qquad b_k \in \{0, 1\}$$

可以立即得出：**任意大小 $N$ 的优先队列都可以由二项树的集合唯一表示**！其中第 $k$ 位二进制位 $b_k = 1$ 当且仅当森林中存在二项树 $B_k$。

- **课堂实例（Slide 3 Example）**：用二项队列表示规模为 $N = 13$ 的优先队列。
  因为 $13 = 8 + 4 + 0 + 1 = 2^3 + 2^2 + 0\times 2^1 + 2^0 = 1101_2$，所以规模为 $13$ 的二项队列必定唯一地由 **一棵 $B_3$（8 节点）、一棵 $B_2$（4 节点）和一棵 $B_0$（1 节点）** 组成（没有 $B_1$）。
- **树的数量上界**：含有 $N$ 个节点的非空二项队列，至多包含 $\lfloor\log_2 N\rfloor + 1$（课件亦写作 $\lceil\log N\rceil$）棵二项树。

---

## 2 二项队列的基本操作原理 (Operations on Binomial Queues)

### 2.1 查找最小值 (`FindMin`)

由于每棵二项树均满足最小堆序，每棵树的最小元必定位于其根节点处，因此全局最小元素必定位于森林中某棵二项树的**根节点**上：

- **直接扫描法**：遍历森林中所有的根节点，由于至多只有 $\lfloor\log_2 N\rfloor + 1$ 棵树，耗时为 $T_p = O(\log N)$；
- **$O(1)$ 指针维护法（Slide 4 Note）**：在二项队列结构体中额外维护一个指向当前最小根节点的指针（或记录最小树下标），每次在 `Insert`、`Merge` 或 `DeleteMin` 改变根集合时顺带更新该指针，即可实现 **`FindMin` 的 $O(1)$ 最坏时间复杂度**。

### 2.2 合并操作 (`Merge`) 与插入操作 (`Insert`)

**1. 合并操作 `Merge(H1, H2)`：二进制加法器原理**

设二项队列 $H_1$ 有 $N_1$ 个节点，$H_2$ 有 $N_2$ 个节点（合并后共有 $N = N_1 + N_2$ 个节点）。前提条件是**森林中的二项树按高度 $k = 0, 1, 2, \dots$ 从小到大有序存放**。
两个二项队列的合并过程，与**两个二进制数从最低位（$k = 0$）向最高位逐位相加并处理进位（Carry）**的过程完全同构：

- **同阶二项树的合并（`CombineTrees`）**：两棵高度同为 $k$ 的二项树 $B_k$ 相加（$2^k + 2^k = 2^{k+1}$），只需比较两个根节点的键值大小，将键值较大的根直接挂接为键值较小的根的新孩子，即可在 **$O(1)$ 时间**内合成一棵高度为 $k + 1$ 的进位树 $B_{k+1}$！
- **逐阶全加器逻辑**：在第 $k$ 阶位置上，考察来自 $H_1$ 的 $B_k$、来自 $H_2$ 的 $B_k$ 以及从第 $k-1$ 阶传上来的进位树 `Carry`（共至多 3 棵 $B_k$）：
  - 若共有 **1 棵** $B_k$：直接保留在结果堆的第 $k$ 阶位置，进位为 `NULL`；
  - 若共有 **2 棵** $B_k$：将这两棵 $B_k$ 合并为一棵 $B_{k+1}$ 作为向第 $k+1$ 阶的进位 `Carry`，结果堆的第 $k$ 阶位置置空（`NULL`）；
  - 若共有 **3 棵** $B_k$：保留其中任意一棵（如 `Carry`）在结果堆的第 $k$ 阶位置，将另外两棵合并为一棵 $B_{k+1}$ 作为新的进位 `Carry` 传给第 $k+1$ 阶。
- **时间复杂度**：共有至多 $\lfloor\log_2 N\rfloor + 1$ 个阶位，每个阶位最多执行一次 $O(1)$ 的 `CombineTrees`，因此合并的最坏时间复杂度为 **$T_p = O(\log N)$**。

**课堂合并实例追踪（Slide 4 & 板书 `W4` Page 9）**：
- $H_1$（含 $6 = 110_2$ 个节点）：有 $B_1$（根 `16`）、$B_2$（根 `12`）；
- $H_2$（含 $7 = 111_2$ 个节点）：有 $B_0$（根 `13`）、$B_1$（根 `14`）、$B_2$（根 `23`）；
- 执行二进制加法 $110_2 + 111_2 = 1101_2 \ (6 + 7 = 13)$：
  1. **$k = 0$ 位（$0 + 1 = 1$）**：仅 $H_2$ 有 $B_0$（根 `13`），直接保留为结果的 $B_0$，无进位；
  2. **$k = 1$ 位（$1 + 1 = 10_2$）**：$H_1$ 的 $B_1$（根 `16`）与 $H_2$ 的 $B_1$（根 `14`）合并（因 $14 < 16$，`16` 挂在 `14` 下），形成进位树 `Carry` $= B_2$（根 `14`），结果的 $B_1$ 位置置空；
  3. **$k = 2$ 位（$1 + 1 + \text{Carry } 1 = 11_2$）**：共有三棵 $B_2$（$H_1$ 根 `12`、$H_2$ 根 `23`、进位根 `14`）。将进位树 $B_2$（根 `14`）留在结果的 $B_2$ 位置，将 $H_1$ 和 $H_2$ 的两棵 $B_2$（根 `12` 与 `23`）合并成进位树 $B_3$（根 `12`）；
  4. **$k = 3$ 位**：将进位树 $B_3$（根 `12`）放入结果的 $B_3$ 位置，合并结束！

**2. 插入操作 `Insert(X, H)`：二进制加一（短程进位传播）**

插入一个新元素 $X$，等价于将一棵仅含节点 $X$ 的单节点二项队列（$B_0$，大小 $1 = 1_2$）与原队列 $H$ 执行 `Merge`：

- **单次插入的精确耗时规律（Slide 5 Note）**：
  设在插入前，原队列 $H$ 中**最小的不存在的二项树是 $B_i$**（即原队列大小 $N$ 的二进制表示末尾恰好有 $i$ 个连续的 `1`：$b_0 = b_1 = \dots = b_{i-1} = 1, \ b_i = 0$）。
  那么插入新节点 $B_0$ 后，会从第 $0$ 位开始连续触发 $i$ 次同阶合并进位（$B_0 + B_0 \to B_1, \ B_1 + B_1 \to B_2, \ \dots, \ B_{i-1} + B_{i-1} \to B_i$），直到放入原本为空的第 $i$ 位才停止！因此本次插入的耗时为：
  $$T_p = \text{Const} \cdot (i + 1)$$
  在最坏情况下（当 $N = 2^k - 1$ 全为 `1` 时），单次插入耗时 $O(\log N)$；但正如二进制计数器连续加一，昂贵的进位极少发生，连续 $N$ 次插入的总耗时仅为 $O(N)$，平均（摊还）每次插入时间为 **$O(1)$**。

### 2.3 删除最小值 (`DeleteMin`)、降键 (`DecreaseKey`) 与任意删除

**1. 删除最小值 `DeleteMin(H)` 的四步流程（Slide 6 & 板书 `W4` Page 10）**

1. **Step 1**：在森林的所有根节点中查找最小元，设其位于二项树 $B_k$ 的根节点处 —— 耗时 $O(\log N)$（若有最小根指针则为 $O(1)$）；
2. **Step 2**：将这棵 $B_k$ 从原二项队列 $H$ 中移出，剩余的二项树森林记为新的二项队列 **$H'$** —— 耗时 $O(1)$；
3. **Step 3**：删去 $B_k$ 的根节点，将其下方的 $k$ 棵孩子子树 $B_0, B_1, \dots, B_{k-1}$ 拆开，按高度递增排成另一个合法的二项队列 **$H''$**（节点总数为 $2^k - 1$）—— 耗时 $O(k) = O(\log N)$；
4. **Step 4**：调用 **`Merge(H', H'')`** 将两个二项队列合并为最终结果 —— 耗时 $O(\log N)$。
因此，`DeleteMin` 的最坏时间复杂度为 **$T_p = O(\log N)$**。

**2. 降低键值 `DecreaseKey(x, k)` 与删除任意指定节点 `Delete(x)`**

- **`DecreaseKey`**：由于每棵二项树 $B_k$ 的高度不超过 $\log_2 N$，当把某节点 $x$ 的键值减小时，只需在该节点所属的那棵二项树内部，沿着父指针执行普通的**上滤（Percolate up，不断与父节点交换键值/卫星数据直至满足堆序）**即可，完全不会破坏二项树的形态！最坏耗时为树高 $O(\log N)$。
- **`Delete(x)`**：先调用 `DecreaseKey(x, -∞)` 将目标节点上滤到其所属二项树的根部，再调用一次 `DeleteMin(H)` 即可，最坏耗时 $O(\log N)$。

---

## 3 二项队列的底层实现与 C 语言源码 (Implementation Details)

### 3.1 为什么采用“左孩子-右兄弟”且按子树规模递减链接？

在实现二项队列时，我们需要解决两个核心工程问题（对应 PPT Slide 7 的 **Discussion 7 & Discussion 8**）：

1. **Discussion 7：一棵二项树 $B_k$ 的根节点有 $k$ 个孩子（变长多叉树），且 `DeleteMin` 需要快速找到所有子树，如何表示树节点？**
   **解决方案**：二项队列整体用**二项树根指针的数组** `TheTrees[MaxTrees]` 表示（下标 $i$ 存 $B_i$）；每棵二项树内部采用**左孩子-右兄弟表示法（Left-Child, Next-Sibling representation）**——每个节点只需维护两个指针：`LeftChild`（指向自己的第一个孩子）和 `NextSibling`（指向自己的下一个亲兄弟）。
2. **Discussion 8：同一个父节点下的各棵孩子子树，必须按什么顺序链接（In which order must we link the subtrees）？**
   **解决方案**：**必须按子树规模从大到小（即高度从高到低：$B_{k-1} \to B_{k-2} \to \dots \to B_1 \to B_0$）的逆序链接，`LeftChild` 直接指向最大的孩子 $B_{k-1}$**！
   - **核心原因 1（保证 `CombineTrees` 为 $O(1)$）**：当我们将两棵 $B_{k-1}$（根为 $T_1, T_2$，设 $T_1 < T_2$）合并为 $B_k$ 时，$T_1$ 原本已经挂着孩子链表 $B_{k-2} \to \dots \to B_0$。为了在 **$O(1)$ 时间**内把 $T_2$（一棵 $B_{k-1}$）加为 $T_1$ 的新孩子，我们绝不能顺着 `NextSibling` 链表遍历到末尾去尾插，而是必须采用**链表头插法**——直接令 `T2->NextSibling = T1->LeftChild; T1->LeftChild = T2;`！这样每次合并新挂入的最大子树自然排在孩子链表的最前端（`LeftChild`），孩子链表自动呈现 $B_{k-1} \to B_{k-2} \to \dots \to B_0$ 的降序排列！
   - **核心原因 2（配合 `DeleteMin` 拆分子树）**：在 `DeleteMin` 删去 $B_k$ 的根后，从 `LeftChild` 开始顺着 `NextSibling` 遍历，依次取出的正好是 $B_{k-1}, B_{k-2}, \dots, B_0$，只需用一个循环变量 `j` 从 `MinTree - 1` 递减到 `0`，就能直接对号入座填入 `DeletedQueue->TheTrees[j]`。

### 3.2 核心数据结构声明与三大函数标准源码

```c
typedef struct BinNode *Position;
typedef struct Collection *BinQueue;
typedef struct BinNode *BinTree;

struct BinNode {
    ElementType Element;
    Position    LeftChild;
    Position    NextSibling;
};

struct Collection {
    int     CurrentSize;          /* 堆中所有节点的当前总数 N */
    BinTree TheTrees[MaxTrees];   /* TheTrees[i] 指向高度为 i 的二项树 B_i */
};
```

**1. 合并两棵同阶二项树 `CombineTrees`（耗时 $T_p = O(1)$）**

```c
/* 合并两棵大小相同 (同为 B_k) 的二项树 T1 和 T2，返回合并后的 B_{k+1} 树根 */
BinTree CombineTrees(BinTree T1, BinTree T2) {
    if (T1->Element > T2->Element)
        /* 将根键值较大者挂接到较小者下方 */
        return CombineTrees(T2, T1);
    /* 头插法：将 T2 插入到 T1 的孩子链表的最前端 (LeftChild) */
    T2->NextSibling = T1->LeftChild;
    T1->LeftChild = T2;
    return T1;
}
```

**2. 合并两个二项队列 `Merge`（全加器 8 状态位掩码实现，耗时 $T_p = O(\log N)$）**

代码中使用 C 语言的双重逻辑非 `!!ptr` 将指针转化为二进制位（非空指针为 `1`，`NULL` 为 `0`），从而将 `(Carry, T2, T1)` 的存在状态编码为 $0 \sim 7$ 的三位二进制整数 `4*!!Carry + 2*!!T2 + !!T1`：

```c
BinQueue Merge(BinQueue H1, BinQueue H2) {
    BinTree T1, T2, Carry = NULL;
    int i, j;

    if (H1->CurrentSize + H2->CurrentSize > Capacity)
        ErrorMessage();
    H1->CurrentSize += H2->CurrentSize;

    for (i = 0, j = 1; j <= H1->CurrentSize; i++, j *= 2) {
        T1 = H1->TheTrees[i];
        T2 = H2->TheTrees[i]; /* 当前第 i 阶的三棵候选树: Carry, T2, T1 */

        switch (4 * !!Carry + 2 * !!T2 + !!T1) {
            case 0: /* 000: 无任何树 */
            case 1: /* 001: 仅有 T1，已在 H1 中，无需操作 */
                break;
            case 2: /* 010: 仅有 T2，移入 H1 并清空 H2 */
                H1->TheTrees[i] = T2;
                H2->TheTrees[i] = NULL;
                break;
            case 4: /* 100: 仅有进位树 Carry，放入 H1 并清空 Carry */
                H1->TheTrees[i] = Carry;
                Carry = NULL;
                break;
            case 3: /* 011: 有 T1 和 T2，合并为进位树 Carry */
                Carry = CombineTrees(T1, T2);
                H1->TheTrees[i] = H2->TheTrees[i] = NULL;
                break;
            case 5: /* 101: 有 T1 和 Carry，合并为新 Carry */
                Carry = CombineTrees(T1, Carry);
                H1->TheTrees[i] = NULL;
                break;
            case 6: /* 110: 有 T2 和 Carry，合并为新 Carry */
                Carry = CombineTrees(T2, Carry);
                H2->TheTrees[i] = NULL;
                break;
            case 7: /* 111: 三棵全有，保留 Carry 在当前阶，合并 T1 和 T2 进位 */
                H1->TheTrees[i] = Carry;
                Carry = CombineTrees(T1, T2);
                H2->TheTrees[i] = NULL;
                break;
        } /* end switch */
    } /* end for-loop */
    return H1;
}
```

**3. 删除最小元素 `DeleteMin`（耗时 $T_p = O(\log N)$）**

```c
ElementType DeleteMin(BinQueue H) {
    BinQueue DeletedQueue;
    Position DeletedTree, OldRoot;
    ElementType MinItem = Infinity; /* 待返回的最小元素值 */
    int i, j, MinTree;              /* MinTree 记录最小根所在的二项树阶数下标 */

    if (IsEmpty(H)) { PrintErrorMessage(); return -Infinity; }

    /* Step 1: 扫描所有二项树的根，找到最小元素所在的树下标 MinTree */
    /* 注：外层循环上限 MaxTrees 可替换为实际存在的根的最大阶数 */
    for (i = 0; i < MaxTrees; i++) {
        if (H->TheTrees[i] && H->TheTrees[i]->Element < MinItem) {
            MinItem = H->TheTrees[i]->Element;
            MinTree = i;
        }
    }

    /* Step 2: 将 B_{MinTree} 从 H 中移出，此时 H 变为 H' */
    DeletedTree = H->TheTrees[MinTree];
    H->TheTrees[MinTree] = NULL;

    /* Step 3.1: 删去 B_{MinTree} 的根节点，获取其孩子链表首指针 */
    OldRoot = DeletedTree;
    DeletedTree = DeletedTree->LeftChild;
    free(OldRoot);

    /* Step 3.2: 构造由被删根的各个孩子子树组成的二项队列 H'' (DeletedQueue) */
    DeletedQueue = Initialize();
    DeletedQueue->CurrentSize = (1 << MinTree) - 1; /* 2^{MinTree} - 1 个节点 */
    for (j = MinTree - 1; j >= 0; j--) {
        DeletedQueue->TheTrees[j] = DeletedTree;
        DeletedTree = DeletedTree->NextSibling;
        DeletedQueue->TheTrees[j]->NextSibling = NULL; /* 断开兄弟指针，恢复为独立树根 */
    }

    /* Step 4: 更新节点总数，并将 H' 与 H'' 合并 */
    H->CurrentSize -= DeletedQueue->CurrentSize + 1;
    H = Merge(H, DeletedQueue);
    return MinItem;
}
```

---

## 4 连续 $N$ 次插入耗时 $O(N)$ 的摊还分析证明 (Amortized Analysis)

**定理 4.1（二项队列线性建堆定理）**：从空二项队列开始，通过连续执行 $N$ 次 `Insert` 操作构建含 $N$ 个元素的二项队列，最坏总时间复杂度为 **$O(N)$**（即单次插入的摊还时间为 **$T_{\text{amortized}} = O(1)$**）。

课堂 PPT（Slides 12–13）与老师手写板书（`W4` Page 11）分别给出了**聚合分析**与**势能法**两种严格证明：

### 证明方法一：聚合分析 (Aggregate Analysis)

每次 `Insert` 包含两部分工作：① 新建单节点树 $B_0$ 并放入最低位（称为 $1$ 次基础 `step`，$N$ 次插入共执行 $N$ 次 `step`）；② 若低位已满，依次向上进位执行同阶树链接 `CombineTrees`（称为 `link`）。

考察从空堆开始连续插入 $N$ 个元素的过程（与二进制计数器从 $0$ 累加到 $N$ 完全相同）：
- 每隔 $2$ 次插入（即第 $2, 4, 6, \dots$ 次），最低位 $B_0$ 发生冲突，产生 $B_0 + B_0 \to B_1$ 的链接；
- 更进一步，按每次插入**恰好执行了多少次链接（`link`）**来分类统计：
  - 恰好产生 $1$ 次链接（止步于生成 $B_1$，即奇数位变偶数位 `...01 + 1 -> ...10`）的插入，占总次数的 $\dfrac{1}{4}$；
  - 恰好产生 $2$ 次链接（止步于生成 $B_2$，即 `...011 + 1 -> ...100`）的插入，占总次数的 $\dfrac{1}{8}$；
  - 恰好产生 $k$ 次链接（止步于生成 $B_k$）的插入，至多占总次数的 $\dfrac{1}{2^{k+1}}$。
- 因此，$N$ 次插入产生的总链接次数（Total links）至多为错位相减级数之和：
  $$
  \text{Total links} \le N\left(1 \times \frac{1}{4} + 2 \times \frac{1}{8} + 3 \times \frac{1}{16} + \cdots\right) = N \sum_{k=1}^{\infty} \frac{k}{2^{k+1}} = N \cdot 1 = O(N)
  $$
  加上 $N$ 次基础 `step`，总时间严格为 $O(N)$！

### 证明方法二：势能法 (Potential Method，必考核心推导)

观察插入操作的特征：**昂贵的插入操作（执行了多次 `link` 合并）会消灭森林中已有的多棵二项树，使树的总数大幅减少；而廉价的插入操作（不合并或少合并）则会增加森林中二项树的数量**（*"Expensive insertions remove trees, while cheap ones create trees"*）。

1. **定义势能函数 $\Phi_i$**：
   定义第 $i$ 次插入完成后的势能 $\Phi_i$ 为**当前二项队列森林中所含二项树的总棵数**（Number of trees in the forest，即二进制表示中 `1` 的个数）：
   $$
   \Phi_i = \text{number of binomial trees after the } i\text{-th insertion} \qquad (\text{初态空堆 } \Phi_0 = 0, \text{ 且恒有 } \Phi_i \ge 0)
   $$
2. **建立单步代价与势能变化的恒等式**：
   设第 $i$ 次插入的实际成本为 $C_i = c$ 个单位（其中 $1$ 个单位用于创建新树 $B_0$ 并放入空位，另外 $c - 1$ 个单位用于执行了 $c - 1$ 次 `CombineTrees` 合并链接）。
   - 创建新节点 $B_0$ 使树的数量 $+1$；
   - 每执行一次 `CombineTrees` 将两棵同阶树合二为一，使树的总数净减少 $1$（共执行了 $c - 1$ 次合并，故树的数量减少 $c - 1$）。
   因此，一次成本为 $c$ 的插入，必然导致森林中二项树的棵数净增加 $1 - (c - 1) = 2 - c$ 棵！即：
   $$
   \Delta\Phi_i = \Phi_i - \Phi_{i-1} = 2 - C_i \iff \hat{C}_i = C_i + (\Phi_i - \Phi_{i-1}) = 2 \qquad (\forall i = 1, 2, \dots, N)
   $$
3. **累加望远镜求和**：
   将上述 $N$ 个等式从 $i = 1$ 到 $N$ 全部相加：
   $$
   \sum_{i=1}^N C_i + \Phi_N - \Phi_0 = 2N
   $$
   代入 $\Phi_0 = 0$，由于终态至少有 $\Phi_N \ge 1$ 棵树（且精确有 $\Phi_N = \text{popcount}(N)$ 棵树），立得：
   $$
   \sum_{i=1}^N C_i = 2N - \Phi_N \le 2N = O(N) \implies T_{\text{amortized}} = 2 = O(1)
   $$
   （注：由此还可直接推出 $N$ 次插入中执行 `CombineTrees` 的**精确总次数**恒等于 $N - \Phi_N = N - \text{popcount}(N)$，见习题 5.1！）。

---

## 5 堆加速 Dijkstra 算法与斐波那契堆拓展 (Heaps in Dijkstra & Fibonacci Heaps)

### 5.1 优先队列在 Dijkstra 单源最短路算法中的复杂度分析 (Project 1)

在有向非负权图 $G = (V, E)$（顶点数 $n = |V|$，边数 $m = |E|$）上运行 Dijkstra 算法时，我们需要维护未确定最短距离的顶点集合，共需执行：
- **$1$ 次建堆（或 $n$ 次 `Insert`）**；
- **$n$ 次 `DeleteMin`**（每轮取出暂定距离 $d[u]$ 最小的顶点 $u$）；
- **至多 $m$ 次 `DecreaseKey`**（遍历每条边 $(u, v)$ 进行松弛 $d[v] \gets d[u] + w(u, v)$ 时更新堆中键值）。

因此，Dijkstra 算法的总时间复杂度由堆的操作复杂度直接决定：

$$
T_{\text{Dijkstra}} = O(n + m) + n \cdot T_{\text{DeleteMin}} + m \cdot T_{\text{DecreaseKey}}
$$

- 若使用**普通二叉堆 / 左偏堆 / 二项堆**：$T_{\text{DeleteMin}} = O(\log n)$ 且 $T_{\text{DecreaseKey}} = O(\log n)$，总时间为 **$O((n + m)\log n)$**（在连通稀疏图上即 $O(m \log n)$）；
- **问题**：在稠密图（$m = \Theta(n^2)$）上，$m$ 次 `DecreaseKey` 会使上述堆实现的耗时退化为 $O(n^2 \log n)$，甚至比不用堆的简单数组扫描版 $O(n^2 + m) = O(n^2)$ 还要慢！为了将总时间降到理论最优的 **$O(m + n\log n)$**，我们需要一种支持 **`DecreaseKey` 为 $O(1)$ 摊还时间**、同时 `DeleteMin` 仍为 $O(\log n)$ 摊还时间的数据结构——这就是**斐波那契堆（Fibonacci Heap，Fredman & Tarjan 1987）**。

### 5.2 斐波那契堆核心原理与五种堆的复杂度全表

<details markdown="1">
<summary>点击展开：斐波那契堆（Fibonacci Heap）核心机制与势能分析概要（讲义 §5.3 补充）</summary>

斐波那契堆在二项堆的基础上进一步贯彻了“**极致懒惰（Lazy evaluation）**”的思想：

1. **放宽结构约束**：允许根链表（循环双向链表）中同时存在多棵度数相同的树，也不要求每棵树必须是标准二项树，并用指针 `H.min` 直接指向最小根。
2. **`Insert` 与 `Merge` 均为 $O(1)$ 实际时间**：插入时直接将新节点扔进根链表而不做任何合并；合并两堆时直接将两条循环双向根链表首尾拼接，耗时均为 $O(1)$！
3. **`DeleteMin` 时才集中整理（`Consolidate`，摊还 $O(\log n)$）**：
   只有在执行 `DeleteMin` 摘除最小根并将其孩子全部放入根链表后，才借助辅助度数桶数组 `A[d]` 遍历根链表，将所有度数相同的根两两合并（同 `CombineTrees`），直到每个度数至多只剩一棵树。
4. **`DecreaseKey` 的切断与级联切断（Cut & Cascading Cut，摊还 $O(1)$）**：
   当降低节点 $x$ 的键值导致其小于父节点 $y$ 时，**不做上滤交换**，而是直接将 $x$ 连同其子树从父节点 $y$ 处**切断（Cut）**并扔进根链表！
   为了防止某个节点被无限次切走孩子而导致“度数为 $k$ 的树却只有极少节点”，为每个节点引入一个布尔标记 `mark`（记录该非根节点自从上次成为别人的孩子以来，是否已经失去过 1 个孩子）：
   - 当父节点 $y$ 第一次失去孩子时，将其标记置为 `y.mark = true`；
   - 当 $y$ **第二次失去孩子**时，立即将 $y$ 也从其父节点处切下扔进根链表（并清除 `y.mark`），并对其祖先递归检查——这称为**级联切断（Cascading Cut）**！
   - **度数上界定理**：级联切断保证了度数为 $k$ 的节点其子树至少包含 $F_{k+2} \ge \varphi^k$ 个节点，故任意节点的最大度数不超过 $D(n) \le \lfloor\log_\varphi n\rfloor \approx 1.44\log_2 n$！
5. **势能函数**：取 $\Phi(H) = t(H) + 2m(H)$，其中 $t(H)$ 为当前根链表中的树根个数，$m(H)$ 为带 `mark` 标记的节点个数（系数取 $2$ 是因为级联切断每切下一个带标记节点，标记数减 $1$ [$-2$] 而根数加 $1$ [$+1$]，净势能变化为 $-1$，正好支付切断该节点的 $1$ 单位实际开销！）。

</details>

**五种优先队列（堆）操作时间复杂度总结对比表**（记 $L = \log N$，带 `*` 号表示**摊还时间复杂度 Amortized**，其余为**最坏情况时间复杂度 Worst-case**）：

| 操作 \ 数据结构 | 二叉堆 (Binary Heap) | 左偏堆 (Leftist Heap) | 斜堆 (Skew Heap) | 二项堆 (Binomial Queue) | 斐波那契堆 (Fibonacci Heap) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`FindMin`** | $O(1)$ | $O(1)$ | $O(1)$ | $O(\log N)$ 或 $O(1)$ | $O(1)$ |
| **`Insert`** | $O(\log N)$ | $O(\log N)$ | $O(\log N)^*$ | **$O(1)^*$**（最坏 $O(\log N)$） | **$O(1)$** |
| **`Merge`** | $\Theta(N)$ | **$O(\log N)$** | **$O(\log N)^*$** | **$O(\log N)$** | **$O(1)$** |
| **`DeleteMin`** | $O(\log N)$ | $O(\log N)$ | $O(\log N)^*$ | $O(\log N)$ | $O(\log N)^*$ |
| **`DecreaseKey`** | $O(\log N)$ | $O(\log N)$ | $O(\log N)^*$ | $O(\log N)$ | **$O(1)^*$** |
| **`Delete` (指定节点)** | $O(\log N)$ | $O(\log N)$ | $O(\log N)^*$ | $O(\log N)$ | $O(\log N)^*$ |

---

## 6 Chapter 5 核心习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 5.1, 5.2 & 5.3: Exact Number of Combines, Even/Odd Depth Nodes & Merge Loop Pitfall（精确合并次数、奇偶深度节点差与通用 Merge 循环陷阱）</summary>

**Problem Statement:**
- **Ex 5.1**: 如果从空二项堆开始连续插入 $n$ 个元素，总共会执行多少次 `CombineTrees`？请给出关于 $n$ 的精确表达式。
- **Ex 5.2**: 约定根的深度为 $0$，记二项堆中深度为偶数、奇数的节点数分别为 $N_0$、$N_1$。证明 $N_0 - N_1$ 只能等于 $0$ 或 $1$，并说明这个差值由元素总数 $n$ 的奇偶性如何决定。当 $N_0 > N_1$ 时，元素总数是否可能为偶数？
- **Ex 5.3**: 解释为什么如果直接调用 §3.2 中完整的通用 `Merge(H1, H2)` 代码来实现从空堆开始的连续 $n$ 次插入，就不能保证每次插入 $O(1)$ 的常数摊还时间？应当如何小幅修改 `Merge` 的循环终止条件以恢复 $O(1)$ 摊还时间？

---

**解答与解析：**

**1. 连续插入 $n$ 个元素的精确 `CombineTrees` 次数（Exercise 5.1，高频填空/选择题）**：
- **不变量巧妙推导**：
  每次插入最初都会创建一个独立的单节点树 $B_0$，因此 $n$ 次插入一共诞生了 $n$ 棵初始树。
  而每执行一次 `CombineTrees(T1, T2)`，就会把两棵树合并为一棵树，使**森林中树的总棵数精确减少 $1$**！
  设最终含有 $n$ 个节点的二项堆森林中共有 $\text{popcount}(n)$ 棵二项树（其中 $\text{popcount}(n)$ 即 $n$ 的二进制表示中位值为 `1` 的个数）。由树的数量守恒：
  $$
  \text{初始树总数 } n - \text{合并次数 } (\#\text{CombineTrees}) = \text{最终树总数 } \text{popcount}(n)
  $$
  立即得到精确表达式：
  $$
  \#\text{CombineTrees} = n - \text{popcount}(n)
  $$
  （例如插入 $n = 13 = 1101_2$ 个元素，$\text{popcount}(13) = 3$，故期间一共精确执行了 $13 - 3 = 10$ 次 `CombineTrees`！）。

---

**2. 二项堆中偶数深度与奇数深度节点数之差（Exercise 5.2）**：
先考察单棵阶数为 $k$ 的二项树 $B_k$。由定理 1.1 知，$B_k$ 在深度 $d \ (0 \le d \le k)$ 处的节点数为 $\binom{k}{d}$。因此 $B_k$ 中偶数深度节点数与奇数深度节点数之差为交错二项式系数和：

$$
\Delta(B_k) = \sum_{d=0}^k (-1)^d \binom{k}{d} = \begin{cases}
(1 - 1)^k = 0, & k \ge 1, \\[4pt]
\binom{0}{0} = 1, & k = 0 \ (\text{即 } B_0).
\end{cases}
$$

这意味着：**对于任意阶数 $k \ge 1$ 的二项树 $B_k$，其内部的偶数深度节点数与奇数深度节点数永远严格相等（差值为 $0$）**！只有单节点树 $B_0$（仅含一个深度为 $0$ 的根）会贡献 $+1$ 的差值。
将二项堆森林中所有树的差值相加，总差值 $N_0 - N_1$ 完全取决于森林中**是否存在 $B_0$**（即总节点数 $n$ 的二进制最低位 $b_0$ 是 $1$ 还是 $0$）：
- 当元素总数 $n$ 为**偶数**时：二进制最低位为 $0$，堆中不含 $B_0$，故 **$N_0 - N_1 = 0$**（即 $N_0 = N_1$）；
- 当元素总数 $n$ 为**奇数**时：二进制最低位为 $1$，堆中恰有一棵 $B_0$，故 **$N_0 - N_1 = 1$**（即 $N_0 = N_1 + 1$）。
因此，当 $N_0 > N_1$ 时，元素总数 $n$ **必定为奇数，绝不可能为偶数**。

---

**3. 通用 `Merge` 循环在单点插入时的提前终止优化（Exercise 5.3）**：
- **原因剖析**：观察 §3.2 中 `Merge(H1, H2)` 的 `for` 循环条件：`for (i = 0, j = 1; j <= H1->CurrentSize; i++, j *= 2)`。
  该循环无条件地从第 $0$ 阶一直遍历到最高阶 $\lfloor\log_2 N\rfloor$（即使在低阶早已没有进位 `Carry == NULL` 且 `H2` 已经全部合并完毕，循环依然会空转执行 `case 0` 或 `case 1` 直到最高位）。如果每次 `Insert` 都调用这个不提前退出的 `Merge`，那么第 $k$ 次插入固定耗时 $\Theta(\log k)$，连续 $n$ 次插入的总耗时将变为 $\sum_{k=1}^n \Theta(\log k) = \Theta(n\log n)$，破坏了 $O(1)$ 的摊还上界！
- **修复方法**：在 `Merge`（或专门的 `Insert`）循环中增加**提前终止条件**：一旦某阶处理完毕后发现 **`H2` 中已无更高阶的树且当前进位 `Carry == NULL`**（对于单点插入，即遇到了第一个空位放下了进位树），立即 `break` 跳出循环！这样每次插入循环迭代的步数才真正等于“连续进位的次数 $+ 1$”，从而严格保证 $O(1)$ 的摊还插入时间。

</details>