# Chapter 8: Dynamic Programming（动态规划）

!!! abstract
    Advanced Data Structures and Algorithm Analysis (ADS) | 第八章课堂与讲义笔记
    
    参考：
    
    - Course Slides Lecture 8: *Dynamic Programming*
    - 课程讲义 Lecture 8:《动态规划》
    - *CLRS* (3rd Ed.), Ch. 15; M. A. Weiss, *Data Structures and Algorithm Analysis in C* (2nd Ed.), Ch. 10.3; J. Kleinberg & É. Tardos, *Algorithm Design*, Ch. 6

## 1 动态规划的核心思想与设计范式 (Core Philosophy and Design Paradigm)

### 1.1 从递归冗余爆炸到填表法：以斐波那契数列为例

**动态规划（Dynamic Programming, DP，由 Richard Bellman 于 1950 年代在兰德公司提出）**的核心格言是：

> **Solve sub-problems just once and save answers in a table — Use a table instead of recursion!**
> （每个子问题只求解一次并将答案保存在表中——用查表/迭代填表代替朴素递归！）

考察最基础的**斐波那契数列**（或每次可跨 $1$ 阶或 $2$ 阶的**爬楼梯计数问题**）：$F(0) = F(1) = 1, \ F(N) = F(N - 1) + F(N - 2) \ (N \ge 2)$。

- **朴素递归的灾难（Trouble-maker: Explosive redundant calculations）**：
  若直接将递推式写为递归函数 `return Fib(N - 1) + Fib(N - 2);`，在计算 `Fib(N - 1)` 的过程中已经完整算出了 `Fib(N - 2)`，但返回后又会为右侧分支重新递归计算一遍 `Fib(N - 2)`（例如算 $F_6$ 时，$F_2$ 被重复计算了 $5$ 次）。
  设调用次数为 $T(N)$，则 $T(N) \ge T(N - 1) + T(N - 2) \implies T(N) \ge F(N) \approx \frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^N$，时间复杂度呈**指数级爆炸**！
- **动态规划解法（自底向上迭代填表与滚动变量优化）**：
  从小到大依次计算 $F(2), F(3), \dots, F(N)$，由于每次计算只需用到最近算出的前两项 `Last`（$F(i-1)$）和 `NextToLast`（$F(i-2)$），只需维护两个变量即可在 **$T(N) = O(N)$ 时间、$O(1)$ 空间**内完成计算：

```c
int Fibonacci(int N) {
    int i, Last, NextToLast, Answer;
    if (N <= 1) return 1;
    Last = NextToLast = 1;                  /* F(0) = F(1) = 1 */
    for (i = 2; i <= N; i++) {
        Answer = Last + NextToLast;         /* F(i) = F(i-1) + F(i-2) */
        NextToLast = Last;
        Last = Answer;                      /* 滚动更新 F(i-1) 与 F(i-2) */
    }
    return Answer;
}
```

### 1.2 动态规划的四步设计范式与装配线调度问题

设计一个动态规划算法通常遵循以下**标准四步法（4-Step Design Paradigm，PPT Slide 12）**：

1. **Characterize an optimal solution（刻画最优解的结构特征）**：分析最优解由哪些选择和哪些子问题构成；
2. **Recursively define the optimal values（递归定义最优值）**：写出原问题最优值与子问题最优值之间的状态转移方程（Bellman 方程）及边界初值；
3. **Compute the values in some order（按某种自底向上的拓扑顺序计算最优值）**：确保计算某个状态时，其依赖的所有更小子问题状态均已算出并保存在表中；
4. **Reconstruct the solving strategy（重构最优解方案）**：利用填表过程中记录的决策信息（或逆向回溯状态表），还原出达到最优值的具体决策序列（若只需最优数值，可省略第 4 步）。

**课堂经典实例：双装配线产品调度问题（Product Assembly，PPT Slides 13–16 & 习题 8.5）**

- **问题描述**：同一辆汽车可以在两条平行的装配线（Line `0` 和 Line `1`）上生产，每条装配线各有 $n$ 个加工阶段（Stage $1 \dots n$）。不同装配线在每个阶段采用的工艺耗时不同（第 `line` 号线在第 `stage` 阶段的加工耗时为 `t_process[line][stage-1]`）；在相邻两个阶段之间，产品既可以留在原装配线继续加工（无转移耗时），也可以花费转移时间 `t_transit[1-line][stage-1]` 切换到另一条装配线。求完成全部 $n$ 个阶段的最少总时间及具体的装配线选择方案。
- **暴力搜索代价**：每个阶段都有 2 种选择，共有 $2^n$ 条可能路径，穷举搜索需 $O(2^n)$ 时间。
- **四步法设计 DP（$O(n)$ 时间 + $O(n)$ 空间）**：
  1. **刻画最优子结构**：若到达第 `stage` 阶段（位于装配线 `line`）的路径是最快的，那么它前半段到达第 `stage - 1` 阶段（位于 `line` 或 `1 - line`）的子路径也必定是到达该前置状态的最快路径！（*An optimal solution contains an optimal solution of a sub-problem*，可通过剪切-粘贴 Cut-and-paste 反证法证明：若前置子路径不是最快，替换为更快的前置子路径会使全路径更快，矛盾）。
  2. **定义状态与递推方程**：设 `f[line][stage]` 表示完成第 `stage` 阶段且当前位于第 `line`（$\in \{0, 1\}$）条装配线时的最少总耗时；用 `L[line][stage]` 记录该状态的前一步来自哪条装配线：
     $$f[\text{line}][\text{stage}] = \min\begin{cases} f[\text{line}][\text{stage}-1] + t_{\text{process}}[\text{line}][\text{stage}-1] & (\text{留在原线 }\text{stay}) \\ f[1-\text{line}][\text{stage}-1] + t_{\text{transit}}[1-\text{line}][\text{stage}-1] & (\text{从另一线转来 }\text{move}) \end{cases}$$
  3. **按 `stage = 1 .. n` 顺序填表并重构最优路径（Slide 16 完整代码）**：

```c
/* Step 3: 自底向上按 stage 递增顺序填表，同时在 L[][] 中记录决策前驱 */
f[0][0] = 0; f[1][0] = 0;
L[0][0] = 0; L[1][0] = 0;

for (stage = 1; stage <= n; stage++) {
    for (line = 0; line <= 1; line++) {
        f_stay = f[line][stage - 1]   + t_process[line][stage - 1];
        f_move = f[1 - line][stage - 1] + t_transit[1 - line][stage - 1];
        if (f_stay < f_move) {
            f[line][stage] = f_stay;
            L[line][stage] = line;      /* 记录前一步留在同一条线 */
        } else {
            f[line][stage] = f_move;
            L[line][stage] = 1 - line;  /* 记录前一步从另一条线切换过来 */
        }
    }
}
Solution = min(f[0][n], f[1][n]);

/* Step 4: 从最后一个阶段逆向回溯重构最优装配路线 plan[1..n] */
line = (f[0][n] < f[1][n]) ? 0 : 1;
for (stage = n; stage > 0; stage--) {
    plan[stage] = line;
    line = L[line][stage];
}
```

### 1.3 动态规划的适用条件与失效边界 (Elements & Limitations of DP)

一个问题能够有效应用动态规划，必须同时具备以下**两个核心要素（Elements of DP，PPT Slide 17）**：

1. **最优子结构（Optimal Substructure）**：一个问题的全局最优解包含其子问题的最优解。
2. **重叠子问题（Overlapping Sub-problems）**：递归求解过程中，相同的子问题被反复多次用到（*If sub-problems do not overlap, DP becomes sort of pointless*——如果子问题完全不重叠，如归并排序每次切分出的左右区间互不相交，则直接用普通**分治法 Divide and Conquer** 即可，无需建表记忆化）。

!!! warning "思考题（Discussion 11）：什么时候不能直接应用动态规划（When CAN'T we apply DP）？"
    **当子问题之间存在“历史依赖性（History-dependency）”从而破坏无后效性/最优子结构时！**
    - **典型反例 1（带历史路径约束的装配线，Slide 17 & 习题 8.5(2)）**：如果在装配线问题中增加一条全局历史规则：“凡是在第 1 阶段走了 `0` 号线的产品，由于某种物理损耗，在最后一个阶段享有特权（或被禁止从 `0` 号线换到 `1` 号线）”。此时，子问题不仅取决于当前到达了哪个节点 `(line, stage)`，还依赖于**过去是如何走到这里的（历史轨迹）**！单纯的状态 `f[line][stage]` 不再满足最优子结构（消除较浅层的历史依赖需要将历史信息扩充进状态维度，如改为三维状态 `f[line][stage][first_line]`）。
    - **典型反例 2（图中的无权最长简单路径问题 Longest Simple Path）**：虽然“最短路径”满足最优子结构，但“**最长简单路径**（要求不能重复经过顶点）”完全不满足最优子结构！因为两段局部最长简单路径拼在一起极大可能会共享内部顶点从而形成环（违背“简单路径”约束），子问题之间高度历史耦合（实际上最长简单路径是 **NP-Complete** 问题）。

---

## 2 经典区间动态规划：矩阵链乘法与最优二叉搜索树 (Interval DP)

当问题涉及一个线性序列，且每次决策是将序列在某处切分开（或选定一个根将序列分为左右两段）时，子问题自然由序列的**左右端点区间 $[i, j]$** 界定，这类 DP 统称为**区间动态规划**（特征：**必须按区间长度 $k = j - i$ 从小到大递增的顺序填表**）。

### 2.1 矩阵链乘法的最佳加括号顺序 (Ordering Matrix Multiplications)

**1. 问题背景与卡特兰数（Catalan Number）枚举爆炸（PPT Slides 4–5）**

矩阵乘法满足结合律，但不同的加括号计算顺序会导致标量乘法次数相差悬殊（设矩阵 $P_{p \times q}$ 与 $Q_{q \times r}$ 相乘需执行 $p \cdot q \cdot r$ 次标量乘法）。
- **课堂算例**：给定四个矩阵：$M_{1\,[10\times 20]}, \ M_{2\,[20\times 50]}, \ M_{3\,[50\times 1]}, \ M_{4\,[1\times 100]}$：
  - 若按 $M_1 * (M_2 * (M_3 * M_4))$ 顺序计算：总乘法次数为 $50\times 1\times 100 + 20\times 50\times 100 + 10\times 20\times 100 = \mathbf{125,000}$ 次；
  - 若按 $(M_1 * (M_2 * M_3)) * M_4$ 顺序计算：总乘法次数仅为 $20\times 50\times 1 + 10\times 20\times 1 + 10\times 1\times 100 = \mathbf{2,200}$ 次！（相差超過 $56$ 倍）。
- **为什么不能暴力枚举所有加括号方式？**
  设对 $n$ 个矩阵的乘积 $M_1 \cdot M_2 \cdots M_n$ 共有 $b_n$ 种不同的完全加括号方式（其中 $b_1 = 1, \ b_2 = 1, \ b_3 = 2, \ b_4 = 5$）。若最后一次乘法发生在第 $i$ 个矩阵之后（即 $(M_1\cdots M_i) \cdot (M_{i+1}\cdots M_n)$），则左半部分有 $b_i$ 种加括号法，右半部分有 $b_{n-i}$ 种加括号法。因此 $b_n$ 满足**卡特兰数（Catalan Number）递推关系**：
  $$b_n = \sum_{i=1}^{n-1} b_i b_{n-i} = \frac{1}{n}\binom{2n-2}{n-1} = O\left(\frac{4^n}{n\sqrt{n}}\right)$$
  方案数随 $n$ 呈指数级增长，暴力穷举完全不可行。

**2. 状态转移方程与 $O(N^3)$ 填表算法（PPT Slides 5–6）**

设要计算 $n$ 个矩阵的乘积 $M_1 * M_2 * \dots * M_n$，其中矩阵 $M_i$ 的维度为 **$r_{i-1} \times r_i$**（故子链乘积矩阵 $M_{ij} = M_i \cdots M_j$ 的维度为 $r_{i-1} \times r_j$）。
定义状态 **$m_{ij}$** 为计算子链 $M_i * \dots * M_j \ (1 \le i \le j \le n)$ 所需的**最少标量乘法次数**。枚举这步区间最后一次乘法发生的位置 $l \ (i \le l < j)$，将子链切分为 $M_{i\dots l}$ 和 $M_{l+1\dots j}$ 两部分：

$$m_{ij} = \begin{cases} 0, & \text{if } i = j, \\ \displaystyle\min_{i \le l < j} \big\{ m_{il} + m_{l+1, j} + r_{i-1} r_l r_j \big\}, & \text{if } j > i. \end{cases}$$

**关键填表顺序**：由于计算 $m_{ij}$（区间差 $j - i = k$）时，所依赖的 $m_{il}$ 和 $m_{l+1, j}$ 的区间差 $y - x < k$ 均严格小于 $k$，因此**最外层循环必须按区间跨度 `k = j - i` 从 `1` 到 `N - 1` 递增（即沿着矩阵主对角线向右上角逐条斜对角线推进）**！

```c
/* r[0..N] 存放矩阵维度：矩阵 i 的维度为 r[i-1] x r[i] */
/* 最少乘法次数最终保存在 M[1][N] 中；时间复杂度 T(N) = O(N^3)，空间 O(N^2) */
void OptMatrix(const long r[], int N, TwoDimArray M, TwoDimArray LastChange) {
    int i, j, k, L;
    long ThisM;
    for (i = 1; i <= N; i++)
        M[i][i] = 0;                        /* 长度为 1 的单矩阵无需乘法 */
    
    for (k = 1; k < N; k++)                 /* k = j - i 为区间跨度，从 1 递增到 N-1 */
        for (i = 1; i <= N - k; i++) {      /* i 为区间左端点 */
            j = i + k;                      /* j 为区间右端点 */
            M[i][j] = Infinity;
            for (L = i; L < j; L++) {       /* 枚举最后一次乘法的分裂点 L */
                ThisM = M[i][L] + M[L + 1][j] + r[i - 1] * r[L] * r[j];
                if (ThisM < M[i][j]) {      /* 更新最小值并记录最优分裂点 L */
                    M[i][j] = ThisM;
                    LastChange[i][j] = L;
                }
            }
        }
}
```

### 2.2 最优二叉搜索树 (Optimal Binary Search Tree, OBST)

**1. 问题描述与期望访问代价公式（PPT Slides 7–8）**

在静态查找场景（词典一旦建好后不再频繁插入或删除，如编译器保留字表）中，给定 $N$ 个已按字典序排好序的单词 $w_1 < w_2 < \dots < w_N$，且已知每个单词 $w_i$ 被查找的概率为 $p_i$。
如果将这 $N$ 个单词组织成一棵二叉搜索树 $T$，其中单词 $w_i$ 在树中的深度为 $d_i$（约定根节点深度 $d_{\text{root}} = 0$，故查找到 $w_i$ 需要进行 $1 + d_i$ 次比较），则整棵树的**期望总访问时间（Expected total access cost）**为：

$$T(N) = \sum_{i=1}^N p_i \cdot (1 + d_i)$$

我们的目标是构造一棵**最优二叉搜索树（OBST）**，使期望总比较次数最小。

**2. 最优子结构与状态转移方程推导**

考察由连续单词子集 $w_i, \dots, w_j \ (i \le j)$ 构成的局部最优二叉搜索树 $T_{ij}$，定义三个核心量（约定当 $j < i$ 空树时，$c_{ij} = 0$）：
- $w_{ij} = \sum_{k=i}^j p_k$：子区间 $[i, j]$ 内所有单词的概率权重之和（Weight of $T_{ij}$）；
- $r_{ij}$：最优子树 $T_{ij}$ 选定的根节点下标（Root of $T_{ij}$）；
- $c_{ij}$：最优子树 $T_{ij}$ 的最小期望代价（Cost of $T_{ij}$）。

若选定单词 $w_k \ (i \le k \le j)$ 作为 $T_{ij}$ 的根，则其左子树 $L$ 包含 $w_i \dots w_{k-1}$，右子树 $R$ 包含 $w_{k+1} \dots w_j$。由于左、右子树挂在根 $w_k$ 下方后，**左、右子树中每一个节点的深度都比在原独立子树中增加了 $1$**，因此左、右子树中所有节点各自多贡献了一次比较（合计多出 $\text{weight}(L) + \text{weight}(R) = w_{i, k-1} + w_{k+1, j}$），再加上根节点 $w_k$ 自身的概率 $p_k$：

$$\begin{aligned} c_{ij} &= p_k + \text{cost}(L) + \text{cost}(R) + \text{weight}(L) + \text{weight}(R) \\ &= \underbrace{\big(p_k + w_{i, k-1} + w_{k+1, j}\big)}_{=\,w_{ij}} + c_{i, k-1} + c_{k+1, j} = w_{ij} + c_{i, k-1} + c_{k+1, j} \end{aligned}$$

枚举所有可能的根 $l \in [i, j]$ 取最小值，即得 **OBST 的核心状态转移方程**：

$$c_{ij} = \min_{i \le l \le j} \big\{ w_{ij} + c_{i, l-1} + c_{l+1, j} \big\} = w_{ij} + \min_{i \le l \le j} \big\{ c_{i, l-1} + c_{l+1, j} \big\} \qquad (i \le j)$$

**3. 课堂 7 保留字实例对比与完整 DP 表（PPT Slides 7 & 9）**

给定 C 语言 7 个保留字及其查找概率：

| 下标 $i$ | 1: `break` | 2: `case` | 3: `char` | 4: `do` | 5: `return` | 6: `switch` | 7: `void` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **概率 $p_i$** | $0.22$ | $0.18$ | $0.20$ | $0.05$ | $0.25$ | $0.02$ | $0.08$ |

- **三种建树策略对比（Discussion 10）**：
  1. **贪心法（Greedy Method，每次选当前区间概率最大者为根）**：根选 `return (0.25)`，左子树根选 `break (0.22)`，右子树根选 `void (0.08)`……最终期望代价为 **$2.43$**；
  2. **AVL 平衡树法（每次选正中间下标的词为根）**：根选 `do`，左根 `case`，右根 `switch`……高度最矮，但把概率极小的 `do (0.05)` 和 `switch (0.02)` 放在了高层，最终期望代价高达 **$2.70$**；
  3. **动态规划 OBST 法**：按区间长度从 $1$ 到 $7$ 自底向上填表（见下表），最终在 `break..void` 格得出最小期望代价为 **$2.15$**（最优根为 `char`，左孩子 `break` 右挂 `case`，右孩子 `return` 左挂 `do`、右挂 `void` 左挂 `switch`）：

| 区间长度 | `break..` ($i=1$) | `case..` ($i=2$) | `char..` ($i=3$) | `do..` ($i=4$) | `return..` ($i=5$) | `switch..` ($i=6$) | `void..` ($i=7$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Len = 1** | `..break`<br>$0.22$ (`break`) | `..case`<br>$0.18$ (`case`) | `..char`<br>$0.20$ (`char`) | `..do`<br>$0.05$ (`do`) | `..return`<br>$0.25$ (`return`) | `..switch`<br>$0.02$ (`switch`) | `..void`<br>$0.08$ (`void`) |
| **Len = 2** | `..case`<br>$0.58$ (`break`) | `..char`<br>$0.56$ (`char`) | `..do`<br>$0.30$ (`char`) | `..return`<br>$0.35$ (`return`) | `..switch`<br>$0.29$ (`return`) | `..void`<br>$0.12$ (`void`) | — |
| **Len = 3** | `..char`<br>$1.02$ (`case`) | `..do`<br>$0.66$ (`char`) | `..return`<br>$0.80$ (`return`) | `..switch`<br>$0.39$ (`return`) | `..void`<br>$0.47$ (`return`) | — | — |
| **Len = 4** | `..do`<br>$1.17$ (`case`) | `..return`<br>$1.21$ (`char`) | `..switch`<br>$0.84$ (`return`) | `..void`<br>$0.57$ (`return`) | — | — | — |
| **Len = 5** | `..return`<br>$1.83$ (`char`) | `..switch`<br>$1.27$ (`char`) | `..void`<br>$1.02$ (`return`) | — | — | — | — |
| **Len = 6** | `..switch`<br>$1.89$ (`char`) | `..void`<br>$1.53$ (`char`) | — | — | — | — | — |
| **Len = 7** | `..void`<br>**$2.15$ (`char`)** | — | — | — | — | — | — |

<details markdown="1">
<summary>点击展开：Knuth 的 O(N²) 最优二叉搜索树加速算法（四边形不等式与最优根单调性，讲义 §8.5.3）</summary>

标准 OBST 填表与矩阵链乘法一样包含三层循环，时间复杂度为 $O(N^3)$。但 PPT Slide 9 特别指出：存在一个 **$O(N^2)$ 的改进算法（Knuth, 1971）**！

1. **四边形不等式与最优根单调性定理（Monotonicity of Optimal Roots）**：
   由于区间权重和 $w_{ij} = \sum_{t=i}^j p_t$ 满足**区间包含单调性**（当 $[b, c] \subseteq [a, d]$ 时 $w_{bc} \le w_{ad}$）和**四边形不等式**（Quadrangle Inequality：对 $a \le b \le c \le d$，有 $w_{ac} + w_{bd} \le w_{ad} + w_{bc}$，此处实际上取等号），可以归纳证明最优代价表 $c_{ij}$ 也满足四边形不等式，进而推出子区间的最优根下标 $r_{ij}$ 具有**决策单调性**：
   **当区间向右扩展一个单词（$j \to j+1$）或从左端删去一个单词（$i \to i+1$）时，最优根的位置绝不会向左倒退**！即恒有：
   $$r_{i, j-1} \le r_{i, j} \le r_{i+1, j}$$
2. **收缩枚举范围实现 $O(N^2)$ 复杂度**：
   在计算区间 $[i, j]$（设长度 $j - i = k$）的最优根时，我们不再需要盲目枚举 $l \in [i, j]$ 的全部 $k+1$ 个位置，而是**只需在上一层已算出的两个子区间最优根之间枚举：令 $l$ 从 $r_{i, j-1}$ 遍历到 $r_{i+1, j}$ 即可**！
   对同一长度 $k$ 的所有区间求和，内层循环的枚举次数构成**望远镜相消和（Telescoping sum）**：
   $$\sum_{i=1}^{N-k} \big(r_{i+1, i+k} - r_{i, i+k-1} + 1\big) = r_{N-k+1, N} - r_{1, k} + (N - k) \le 2N = O(N)$$
   每条对角线所有格子的内层循环加起来总共才执行 $O(N)$ 次，共有 $N$ 条对角线，因此总时间复杂度从 $O(N^3)$ 直接降至 **$O(N^2)$**！

</details>

---

## 3 图论与计数动态规划：全源最短路与红黑树计数 (Graph & Counting DP)

### 3.1 全源最短路径：Floyd-Warshall 算法 (All-Pairs Shortest Path)

**问题描述（PPT Slides 10–11 & 讲义 §8.6.2）**：
给定含 $N = |V|$ 个顶点的有向带权图 $G = (V, E)$（顶点编号为 $0, 1, \dots, N-1$），求出**任意一对顶点 $v_i$ 与 $v_j \ (i \neq j)$ 之间的最短路径长度**。

- **Method 1（对每个顶点运行一次单源最短路算法）**：
  若边权非负，运行 $|V|$ 次线性扫描版 Dijkstra 耗时 $O(|V|^3)$（用二叉堆优化为 $O(|V||E|\log|V|)$，用斐波那契堆为 $O(|V|^2\log|V| + |V||E|)$，在**稀疏图 Sparse graph** 上很快）；若有负权边，运行 $|V|$ 次 Bellman-Ford 耗时 $O(|V|^2|E|)$，在稠密图上高达 $O(|V|^4)$。
- **Method 2：Floyd-Warshall 动态规划算法（在稠密图 Dense graph 上极快，且支持负权边）**：
  **核心状态定义**：定义 **$D^k[i][j]$** 为从顶点 $i$ 到顶点 $j$、且**路径上所有中间内部顶点（Intermediate vertices，不含起点 $i$ 和终点 $j$）的编号均不超过 $k$（即内部顶点 $\in \{0, 1, \dots, k\}$）**的所有路径中的最短长度。
  - **初值（$k = -1$）**：不允许经过任何中间顶点，$D^{-1}[i][j] = \text{Cost}[i][j]$（即邻接矩阵 $A[i][j]$：有直接边则为边权，$i=j$ 时为 $0$，无边则为 $+\infty$）；
  - **状态转移（从 $D^{k-1}$ 递推 $D^k$，$k = 0, 1, \dots, N-1$）**：
    当新允许使用编号为 $k$ 的顶点作为中转点时，从 $i$ 到 $j$（中间顶点 $\le k$）的最短路径只有两种可能：
    ① **不经过顶点 $k$**：最短长度仍为 $D^{k-1}[i][j]$；
    ② **经过顶点 $k$**（在无负环图中简单路径至多经过 $k$ 一次）：路径在 $k$ 处拆分为 $i \to k$ 和 $k \to j$ 两段，每段内部顶点均 $\le k-1$，长度为 $D^{k-1}[i][k] + D^{k-1}[k][j]$。
    因此递推方程为：
    $$
    D^k[i][j] = \min\Big\{ D^{k-1}[i][j], \ \ D^{k-1}[i][k] + D^{k-1}[k][j] \Big\}, \qquad k = 0, 1, \dots, N-1
    $$
    最终 $D^{N-1}[i][j]$ 即为允许经过任意顶点的全局最短路径长度！

```c
/* A[][] 为邻接矩阵 (A[i][i] = 0); D[][] 保存最终全源最短路径长度; Path[][] 记录中转点用于重构路径 */
/* 时间复杂度 T(N) = O(N^3)，空间复杂度 O(N^2) */
void AllPairs(TwoDimArray A, TwoDimArray D, TwoDimArray Path, int N) {
    int i, j, k;
    for (i = 0; i < N; i++)                 /* Step 1: Initialize D and Path */
        for (j = 0; j < N; j++) {
            D[i][j] = A[i][j];
            Path[i][j] = NotAVertex;        /* -1 */
        }

    /* Step 2: 动态规划三层循环 —— 注意最外层循环变量必须是中转点 k ！ */
    for (k = 0; k < N; k++)                 /* 依次解锁中间顶点 k = 0 .. N-1 */
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                if (D[i][k] + D[k][j] < D[i][j]) { /* Update shortest path */
                    D[i][j] = D[i][k] + D[k][j];
                    Path[i][j] = k;
                }
}
```

!!! note "Floyd-Warshall 算法的三大核心考点（Slide 11 & 习题 8.13）"
    1. **负权边与负权环（Negative-cost cycles）检测**：
       Floyd-Warshall 算法在图中存在**负权边（Negative edge costs）但不存在负权环**时完全正确。如果图中存在负权环，如何检测？只需在算法运行中或结束后检查主对角线元素：**图中存在负权环当且仅当存在某个顶点 $i$ 使得 `D[i][i] < 0`**（从 $i$ 出发绕一圈回到 $i$ 总代价为负）！
    2. **为什么可以直接用单个二维数组 `D[i][j]` 原地覆盖更新（省去上标 $k$）？**
       因为在计算第 $k$ 轮时，`D[i][k]` 和 `D[k][j]` 在第 $k$ 轮中自身不会被修改（因为 $D[i][k] = \min(D[i][k], D[i][k] + D[k][k])$，只要无负环即 $D[k][k] \ge 0$，它就不会变），所以原地覆盖绝不会污染本轮所需的旧值。
    3. **三层循环的顺序 `k -> i -> j` 能否交换为 `i -> j -> k`？**
       **绝对不能**！$k$ 是动态规划的“阶段（Stage）”变量，必须放在最外层。若把 $k$ 放在最内层，在计算 `D[i][j]` 时所依赖的 `D[i][k]` 和 `D[k][j]` 尚未解锁更高编号的中转点（见习题 8.13 反例）。

### 3.2 讲义补充：Bellman-Ford 算法与红黑树计数 DP

<details markdown="1">
<summary>点击展开：Bellman-Ford 单源最短路算法与给定键值红黑树计数 DP（讲义 §8.6.1 & §8.7）</summary>

**1. Bellman-Ford 单源含负权边最短路算法（讲义 §8.6.1）**

给定有向图 $G = (V, E)$（$n = |V|, \ m = |E|$）与源点 $s$：
- **状态定义**：设 $D_k[v]$ 为从源点 $s$ 出发、**至多经过 $k$ 条边**到达顶点 $v$ 的最短路径长度（初值 $D_0[s] = 0$，其余 $D_0[v] = +\infty$）。
- **状态转移**：
  $$
  D_k[v] = \min\left\{ D_{k-1}[v], \ \ \min_{(u, v) \in E}\big\{ D_{k-1}[u] + w(u, v) \big\} \right\}, \qquad k = 1, 2, \dots, n
  $$
- **负环判定定理**：若图中不含从 $s$ 可达的负环，则任意最短简单路径至多包含 $n - 1$ 条边，故算到 $D_{n-1}$ 即已收敛。**图中不存在从 $s$ 可达的负环，当且仅当第 $n$ 轮没有任何距离被更新（即对所有 $v \in V$ 均有 $D_n[v] = D_{n-1}[v]$）**！时间复杂度为 $O(nm)$。

---

**2. 给定 $N$ 个互异键值的合法红黑树计数（Counting Red-Black Trees，讲义 §8.7，经典树形计数 DP）**

**问题**：给定 $N$ 个互异键值（中序遍历唯一确定，故只需枚举树形与染色），一共能构造出多少棵合法的红黑树？
**状态设计**：为了在拼接左右子树时验证红黑树的性质 4（红节点无红孩子）和性质 5（各路径黑节点数相同），子问题的状态必须同时记录三个维度：
- $n$：子树的内部节点总数（$0 \le n \le N$）；
- $h$：从子树根到 `NIL` 路径上的**黑色内部节点个数**（含子树根自身，不含 `NIL`；由红黑树高度引理知 $h \le H = \lfloor\log_2(N+1)\rfloor$）；
- 根的颜色：用 **$B[n, h]$** 表示根为**黑色**的合法子树方案数，用 **$R[n, h]$** 表示根为**红色**的合法子树方案数。

**初值与状态转移方程**：
空树（$n=0$）对应单个黑色 `NIL`，含 $0$ 个黑色内部节点，故初值为 $B[0, 0] = 1$，其余 $B[0, h] = R[0, h] = 0$。
对于 $n \ge 1$，根节点占去 $1$ 个节点，枚举左子树分配 $a \ (0 \le a \le n-1)$ 个节点，则右子树分配 $b = n - 1 - a$ 个节点：
1. **若当前根染黑色（计算 $B[n, h]$）**：根自身贡献了 $1$ 个黑节点，故左、右子树内部需各有 $h - 1$ 个黑节点，且**左右子树的根既可以是黑色也可以是红色**，由乘法原理：
   $$
   B[n, h] = \sum_{a=0}^{n-1} \big(B[a, h-1] + R[a, h-1]\big)\big(B[n-1-a, h-1] + R[n-1-a, h-1]\big)
   $$
2. **若当前根染红色（计算 $R[n, h]$）**：根不贡献黑节点，且由性质 4 知**左右子树的根必须都是黑色**，各含 $h$ 个黑节点：
   $$
   R[n, h] = \sum_{a=0}^{n-1} B[a, h] \cdot B[n-1-a, h]
   $$

整棵红黑树要求根必须为黑色，故最终答案为 $\sum_{h=0}^{\lfloor\log_2(N+1)\rfloor} B[N, h]$。共有 $O(N\log N)$ 个状态，每个状态枚举 $N$ 个分点，总时间复杂度为 **$O(N^2 \log N)$**。

</details>

---

## 4 线性、背包与序列动态规划专题 (Knapsack & Sequence DP)

讲义（§8.2, §8.3, §8.9）系统梳理了算法竞赛与考试中最常考的几类经典 DP 模型，核心递推式与空间优化对比汇总如下：

### 4.1 三类背包问题 (0-1, Unbounded, and Bounded Knapsack)

设背包总容量为正整数 $C$，共有 $n$ 种物品，第 $i$ 种物品的重量为 $s_i$、价值为 $v_i$：

| 背包类型 | 物品数量限制 | 二维状态转移方程（$V[i, c]$） | 一维空间优化 $A[0..C]$ 的内层循环方向与复杂度 |
| :--- | :--- | :--- | :--- |
| **1. 0-1 背包**<br>（0-1 Knapsack） | 每件物品至多选 **$1$ 次** | $V[i, c] = \max\big\{V[i-1, c], \ V[i-1, c - s_i] + v_i\big\}$ | **逆序循环 `for c = C downto s_i`**<br>（防止 $A[c-s_i]$ 在本轮被提前覆盖而重复选入同一物品）<br>时间 $O(nC)$（**伪多项式时间**），空间 $O(C)$ |
| **2. 完全背包**<br>（Unbounded） | 每种物品可选**无限次** | $U[i, c] = \max\big\{U[i-1, c], \ U[i, c - s_i] + v_i\big\}$ | **正序循环 `for c = s_i to C`**<br>（恰需利用本轮已更新的 $U[i, c-s_i]$ 实现继续选同种物品）<br>时间 $O(nC)$，空间 $O(C)$ |
| **3. 有界/多重背包**<br>（Bounded） | 第 $i$ 种物品至多选 **$b_i$ 次** | 朴素枚举件数 $k \in [0, \min(b_i, \lfloor c/s_i \rfloor)]$：<br>$O\left(C \sum_{i=1}^n b_i\right)$ | **二进制分组拆分法（Binary Grouping）**：<br>将 $b_i$ 件拆分为系数 $1, 2, 4, \dots, 2^{t-1}, r$（其中 $r = b_i - (2^t - 1)$）共 $\lfloor\log_2 b_i\rfloor + 1$ 组新 0-1 物品，转化为 0-1 背包，时间降为 **$O\left(C \sum_{i=1}^n \log b_i\right)$** |

!!! warning "重要理论概念：为什么 0-1 背包的 $O(nC)$ 是伪多项式时间（Pseudo-polynomial Time）？"
    在计算复杂性理论中，衡量算法是否属于多项式时间，其基准是**输入编码的比特长度（Input size in bits）**，而非输入数值本身的大小！
    整数容量 $C$ 在输入中只需用 $k = \lfloor\log_2 C\rfloor + 1$ 个二进制比特表示，而 $O(nC) = O(n \cdot 2^k)$ 关于输入比特数 $k$ 实际上是**指数级增长**的，因此称为**伪多项式时间算法**（0-1 背包问题是 NP-Hard 问题）。

### 4.2 序列 DP 与 Hirschberg 线性空间 LCS 重构算法

**1. 路径图最大加权独立集（House Robber）、最大子序列和、LCS 与序列对齐**

| 经典问题 | 状态定义 | 状态转移方程与时间复杂度 |
| :--- | :--- | :--- |
| **路径图最大加权独立集**<br>（相邻顶点不能同时选） | $W[i]$：前 $i$ 个顶点的最大独立集权和 | $W[i] = \max\big\{W[i-1], \ W[i-2] + w_i\big\} \quad (W[0]=0, W[1]=w_1)$<br>时间 $O(n)$，空间 $O(n)$（只求值可降为 $O(1)$） |
| **最大连续子序列和**<br>（Kadane 算法） | $E[i]$：**以 $a_i$ 结尾**的最大非空连续子序列和 | $E[i] = \max\big\{a_i, \ E[i-1] + a_i\big\}, \quad \text{Ans} = \max_{1\le i\le n} E[i]$<br>时间 $O(n)$，空间 $O(1)$ |
| **最长公共子序列（LCS）**<br>（子序列不要求连续） | $L[i, j]$：$X[1..i]$ 与 $Y[1..j]$ 的 LCS 长度 | $L[i, j] = \begin{cases} L[i-1, j-1] + 1, & x_i = y_j \\ \max\{L[i-1, j], L[i, j-1]\}, & x_i \neq y_j \end{cases}$<br>时间 $O(mn)$，标准重构空间 $O(mn)$ |
| **序列对齐 / 编辑距离**<br>（空位罚分 $g$，错配 $\alpha(x_i, y_j)$） | $P[i, j]$：$X[1..i]$ 与 $Y[1..j]$ 的最小对齐总代价 | $P[i, j] = \min\begin{cases} P[i-1, j-1] + \alpha(x_i, y_j) \\ P[i-1, j] + g, \ \ P[i, j-1] + g \end{cases}$<br>初值 $P[i, 0] = ig, \ P[0, j] = jg$；时间 $O(mn)$ |

**2. Hirschberg 算法：在 $O(mn)$ 时间、$O(m + n)$ 线性空间内重构完整 LCS（讲义 §8.9）**

在 LCS 问题中，如果只求长度，只需保留两行滚动数组，空间为 $O(\min(m, n))$；但如果还要重构输出具体的 LCS 字符串，由于两行滚动数组丢掉了历史行，无法回溯路径。
1975 年，Daniel Hirschberg 提出了将**动态规划滚动数组与分治法完美结合**的算法，仅用 **$O(m + n)$ 线性空间**即可恢复完整 LCS（且时间仍保持为 $O(mn)$）：

1. **取半切分 $X$**：令 $r = \lfloor m / 2 \rfloor$，将字符串 $X$ 对半切分为前半段 $X[1..r]$ 和后半段 $X[r+1..m]$。
2. **正反两次滚动数组 DP 寻找最佳切分点 $j^*$**：
   - 用两行滚动数组正向计算 $X[1..r]$ 与 $Y[1..n]$ 的最后一行 LCS 长度，记为 $L[j] = \text{LCSLen}(X[1..r], Y[1..j]) \ (0 \le j \le n)$；
   - 将后半段 $X[r+1..m]$ 与 $Y[1..n]$ 反转（Reverse），用两行滚动数组反向计算 $X[r+1..m]$ 与后缀 $Y[j+1..n]$ 的 LCS 长度，记为 $R[j] = \text{LCSLen}(X[r+1..m], Y[j+1..n])$；
   - 遍历 $j \in [0, n]$，找到使前后两段 LCS 长度之和最大的分界点 $j^*$：
     $$
     j^* = \arg\max_{0 \le j \le n} \big\{ L[j] + R[j] \big\}
     $$
     这表明全局最优 LCS 必然在 $(r, j^*)$ 处穿过中线！
3. **分治递归求解**：释放临时数组 $L, R$，分别递归调用 `Hirschberg(X[1..r], Y[1..j*])` 和 `Hirschberg(X[r+1..m], Y[j*+1..n])`（当子串行数 $m = 1$ 时直接扫描匹配输出）。
4. **为什么时间复杂度依然是 $O(mn)$ 而没有多乘 $\log m$？**
   - 第 $0$ 层（根）扫描网格面积为 $m \times n$；
   - 第 $1$ 层两个子问题的网格面积分别为 $\frac{m}{2} \times j^*$ 和 $\frac{m}{2} \times (n - j^*)$，**面积之和恒等于 $\frac{m}{2}(j^* + n - j^*) = \frac{1}{2}mn$**！
   - 每向下一层，总计算面积严格减半！由等比级数求和：
     $$
     T(m, n) = O\left(mn + \frac{1}{2}mn + \frac{1}{4}mn + \cdots\right) = O(2mn) = O(mn)
     $$
   空间复杂度仅为两行滚动数组 $O(n)$ 加上递归栈深度 $O(\log m)$ 及输入输出 $O(m+n)$，总空间严格为 **$O(m + n)$**！

---

## 5 Chapter 8 核心习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 8.1, 8.2, 8.3 & 8.4: Tree Independent Set, Coin Change, Decode Ways & Max Product（树的最大权独立集、零钱兑换、数字串解码与最大乘积子数组）</summary>

**Problem Statement:**
- **Ex 8.1**: 对任意无向图 $G = (V, E)$ 及顶点 $v \in V$（权 $w_v \ge 0$），令 $H = G - v$，且 $K = G - N[v]$（删去 $v$ 及其所有邻点）。递推式 $W_G = \max\{W_H, W_K + w_v\}$ 是否对任意图都正确？为什么它能对**树（Tree）**产生 $O(n)$ 时间的 DP 算法，却不能对一般图产生线性时间算法？
- **Ex 8.2 (Coin Change)**: 给定正整数硬币面额数组 `coins[1..q]`（每种无限枚）和目标金额 `A`，求凑出金额 `A` 所需的最少硬币枚数。
- **Ex 8.3 (Decode Ways)**: 字母 `A..Z` 编码为十进制串 `'0'..'25'`（两位编码不能有前导零，如 `07` 只能拆为 `0 | 7`）。给定长度为 $n$ 的数字串，设计 $O(n)$ DP 算法计算解码方式总数。
- **Ex 8.4 (Maximum Subsequence Product)**: 给定含正数、负数、$0$ 及小数的实数数组 $a[1..n]$，设计 $O(n)$ 算法求非空连续子序列的最大乘积。

---

**解答与解析：**

**1. 一般图与树上的最大加权独立集（Exercise 8.1）**：

- **递推式的普适性**：公式 $W_G = \max\{W_H, W_K + w_v\}$ **对任意无向图都是完全正确的**（因为最优独立集要么不含 $v$ [此时等价于在 $G - v$ 中找最大独立集]，要么包含 $v$ [此时 $v$ 的所有邻点均不能选，等价于在 $G - N[v]$ 中找最大独立集再加上 $w_v$]）。
- **为什么在一般图上不是线性时间，而在树上是 $O(n)$ 时间？**
  在一般无向图中，反复删去不同顶点及邻域会产生多达 $O(2^n)$ 个互不同构的导出子图状态（子问题数量呈指数级爆炸）。
  而在**树（Tree）**上，固定任意根节点后，删去父节点或子节点只会留下标准的**以各节点 $u$ 为根的子树 $T_u$**（全树总共只有 $n$ 棵子树）！对每个树节点 $u$ 仅需维护两个状态：$I[u]$（选 $u$ 时子树 $T_u$ 的最大独立集权和）与 $O[u]$（不选 $u$ 时子树 $T_u$ 的最大独立集权和），按后序遍历自底向上递推：
  $$
  I[u] = w_u + \sum_{v \in \text{children}(u)} O[v], \qquad O[u] = \sum_{v \in \text{children}(u)} \max\big\{I[v], \ O[v]\big\}
  $$
  每个节点和每条树边仅被访问一次，总时间复杂度严格为 **$O(n)$**！

---

**2. 零钱兑换问题（Coin Change，Exercise 8.2）**：
令 $D[x]$ 表示凑出金额 $x \ (0 \le x \le A)$ 所需的最少硬币数（初值 $D[0] = 0$，其余初始化为 $+\infty$）。枚举最后一枚硬币的面额 $c \in \text{coins}$：

$$
D[x] = 1 + \min_{c \in \text{coins},\, c \le x} D[x - c], \qquad x = 1, 2, \dots, A
$$

时间复杂度为 $O(Aq)$，空间复杂度为 $O(A)$。

---

**3. 数字串解码方式计数（Decode Ways，Exercise 8.3）**：
设数字串为 $s[1..n]$，令 $D[i]$ 表示前缀 $s[1..i]$ 的合法解码方式总数（初值 $D[0] = 1, \ D[1] = 1$）：
- 最后一个数字 $s[i]$ 总是可以单独解码为一个字母（`'0'..'9'` $\to$ `A..J`），贡献 $D[i-1]$ 种方式；
- 若倒数两个数字构成的十进制两位数满足 $s[i-1] \neq \text{'0'}$ 且 $10 \le \text{val}(s[i-1..i]) \le 25$，则最后两位可以合并解码为一个字母（`'10'..'25'` $\to$ `K..Z`），额外贡献 $D[i-2]$ 种方式：
  $$
  D[i] = D[i-1] + \mathbb{I}\big(10 \le \text{val}(s[i-1..i]) \le 25\big) \cdot D[i-2]
  $$
  时间复杂度为 $O(n)$。

---

**4. 最大连续子序列乘积（Maximum Subsequence Product，Exercise 8.4，必考状态设计题）**：
**为什么不能像最大子序列和那样只记一个最大值 $E[i]$？**
因为乘法具有**负负得正**的性质！如果当前元素 $a_i < 0$ 是负数，它乘以前面一个**最小的负乘积**反而会瞬间变成最大的正乘积！
因此，对每个位置 $i$，必须**同时维护两个状态**：
- $H[i]$：以 $a_i$ 结尾的连续子序列的**最大乘积**；
- $L[i]$：以 $a_i$ 结尾的连续子序列的**最小乘积**（最负值）。
初值 $H[1] = L[1] = a_1$。对 $i = 2 \dots n$，状态转移方程为：

$$
\begin{aligned}
H[i] &= \max\big\{ a_i, \ \ H[i-1] \cdot a_i, \ \ L[i-1] \cdot a_i \big\}, \\
L[i] &= \min\big\{ a_i, \ \ H[i-1] \cdot a_i, \ \ L[i-1] \cdot a_i \big\},
\end{aligned}
$$

全局最大乘积为 $\max_{1 \le i \le n} H[i]$，时间复杂度为 $O(n)$。

</details>

<details markdown="1">
<summary>Exercise 8.5, 8.6, 8.7, 8.8 & 8.9: Assembly History, Bread-Cream Pairing, Palindromes, LIS & Rod Cutting（历史依赖扩维、面包奶油配对、回文分割、LIS 与钢条切割）</summary>

**Problem Statement:**
- **Ex 8.5**: 在 §1.2 的双生产线问题中，若增加历史约束：“第一阶段在生产线 `0` 加工的产品，最后一步（第 $n$ 阶段）不能从生产线 `0` 换到生产线 `1`”，应如何修改状态设计以在 $O(n)$ 时间内求解？
- **Ex 8.6 (Hand-made Cream)**: 给定 $n$ 片面包评分 $a[1..n]$ 和 $m$ 份奶油评分 $b[1..m]$（评分可正可负）。按原相对顺序挑选相同数量的面包和奶油一一配对，每对得分为 $a_i \cdot b_j$（允许一对都不选得 $0$ 分），求最大总得分。
- **Ex 8.7 (Palindromes)**: 给定长度为 $n$ 的字符串 $s[1..n]$，设计 $O(n^2)$ DP 算法解决：(1) 求最长回文子串；(2) 将整个字符串切割为若干回文子串，求最少切割次数。
- **Ex 8.8 (Longest Increasing Subsequence, LIS)**: 给定数组 $a[1..n]$，设计 $O(n^2)$ DP 算法求最长严格递增子序列的长度并恢复方案。
- **Ex 8.9 (Rod Cutting)**: 给定长度为 $n$ 英寸的钢条和长度 $1 \dots n$ 的价格表 $p_1, \dots, p_n$，求使销售总收益最大的切割方案。

---

**解答与解析：**

**1. 消除历史依赖的维度扩充技巧（Exercise 8.5）**：
由于第 $n$ 步的转移合法性依赖于“第 1 阶段在哪条生产线上”，我们在状态中增加一个二元维度 $z \in \{0, 1\}$ 来记住起点！
定义三维状态 **$F[l, j, z]$** 表示：**第 1 阶段固定在生产线 $z$ 加工**，且完成第 $j$ 阶段时位于生产线 $l$ 的最少总用时：
- **初值（$j = 1$）**：对 $z \in \{0, 1\}$，$F[z, 1, z] = \min\{a_{z, 1}, b_{1-z, 1}\}$，$F[1-z, 1, z] = +\infty$；
- **状态转移（$2 \le j \le n$）**：中间阶段 $2 \le j < n$ 照常转移；仅在最后一步 **$j = n$ 且 $z = 0, \ l = 1$** 时，禁止从 $(0, n-1)$ 转移过来，只允许留在 $1$ 号线：$F[1, n, 0] = F[1, n-1, 0] + a_{1, n}$。
最终全局最优解为 $\min_{l, z \in \{0,1\}} F[l, n, z]$，状态数仅扩大 2 倍，时间复杂度仍为 **$O(n)$**！

---

**2. 面包与奶油顺序配对（Hand-made Cream，Exercise 8.6）**：
类比 LCS：令 $F[i, j]$ 表示从前 $i$ 片面包和前 $j$ 份奶油中按序配对能获得的最大总得分（初值 $F[i, 0] = F[0, j] = 0$）。考察末尾的 $a_i$ 与 $b_j$：要么放弃 $a_i$，要么放弃 $b_j$，要么将 $a_i$ 与 $b_j$ 配成最后一对：

$$
F[i, j] = \max\Big\{ F[i-1, j], \ \ F[i, j-1], \ \ F[i-1, j-1] + a_i \cdot b_j \Big\}
$$

时间复杂度为 $O(nm)$。

---

**3. 最长回文子串与最少回文分割（Exercise 8.7）**：

- **(1) 最长回文子串**：
  定义布尔区间状态 $H[i, j]$ 表示子串 $s[i..j]$ 是否为回文串。按子串长度 $len = j - i + 1$ 从 $1$ 到 $n$ 递增填表：
  $$
  H[i, j] = \big(s[i] == s[j]\big) \land \big(j - i \le 1 \ \lor \ H[i+1, j-1]\big)
  $$
  所有满足 $H[i, j] = \text{true}$ 中长度 $j - i + 1$ 最大者即为最长回文子串，耗时 $O(n^2)$。
- **(2) 最少回文切割次数**：
  先用 (1) 预处理出全表 $H[i, j]$。再令 $F[j]$ 表示前缀 $s[1..j]$ 最少能被分成多少段回文子串（初值 $F[0] = 0$，最少切割刀数为 $F[n] - 1$）。枚举最后一段回文子串的起点 $i \ (1 \le i \le j)$：
  $$
  F[j] = \min_{1 \le i \le j,\, H[i, j] = \text{true}} \big\{ F[i - 1] + 1 \big\}
  $$
  总时间复杂度为 $O(n^2)$。

---

**4. 最长严格递增子序列（LIS，Exercise 8.8）与钢条切割（Rod Cutting，Exercise 8.9）**：

- **LIS（Exercise 8.8）**：令 $E[i]$ 表示**以 $a_i$ 结尾**的最长严格递增子序列长度。枚举倒数第二项的位置 $j < i$（需满足 $a_j < a_i$）：
  $$
  E[i] = 1 + \max\Big( \big\{ E[j] : 1 \le j < i \text{ and } a_j < a_i \big\} \cup \{0\} \Big)
  $$
  全局 LIS 长度为 $\max_{1 \le i \le n} E[i]$，同步用 `prev[i]` 记录取到最大值的 $j$ 即可逆向恢复序列，时间 $O(n^2)$。
- **钢条切割（Exercise 8.9）**：令 $R[j]$ 表示长度为 $j$ 的钢条的最大销售收益（$R[0] = 0$）。枚举切下的第一段长度 $i \ (1 \le i \le j)$：
  $$
  R[j] = \max_{1 \le i \le j} \big\{ p_i + R[j - i] \big\} \qquad (\text{时间复杂度 } O(n^2))
  $$

</details>

<details markdown="1">
<summary>Exercise 8.10, 8.11, 8.12 & 8.13: Batch Task Scheduling, Perfect Squares, RNA Pairing & Shortest Path Pitfalls（任务分批费用提前计算、完全平方数、RNA二级结构配对与最短路辨析）</summary>

**Problem Statement:**
- **Ex 8.10 (Manager of Tasks)**: 机器从时刻 $0$ 开始按顺序将任务 $1 \dots n$ 分成若干连续批次处理。每批启动需耗时 $S$，批内任务执行时间依次为 $T_k$，同批任务在整批全部做完的同一时刻 $d$ 才一起算作完成，任务 $k$ 的成本为 $d \cdot C_k$。设计 $O(n^2)$ DP 算法求最小总成本。
- **Ex 8.11**: 将正整数 $n$ 写成若干个正整数平方之和（如 $13 = 4 + 9$ 需 2 项），求最少项数及复杂度。
- **Ex 8.12 (RNA Secondary Structure Pairing)**: 给定由 `A, C, G, U` 组成的长度为 $n$ 的 RNA 序列 $s[1..n]$。配对规则：① 只允许 `A-U`、`C-G` 互补配对，每个位置至多配对一次；② 严禁急转弯：配对的 $(i, j)$ 必须满足 **$j - i \ge 5$**；③ 严禁假结（弧线不能交叉）：不能同时选 $i < k < j < l$。设计 DP 算法求最大配对数。
- **Ex 8.13**: 判断正误并解释：(1) 用一维数组 `d[v]` 原地实现的 Bellman-Ford 算法，在第 $k$ 轮循环结束后恰好得到至多 $k$ 条边的最短距离 $D_k[v]$；(2) Floyd-Warshall 算法的三层循环 `k, i, j` 可以任意交换顺序。

---

**解答与解析：**

**1. 任务分批调度的“费用提前计算 / 后缀成本累加”技巧（Exercise 8.10，经典高阶 DP 题）**：
如果我们从前往后定义状态，由于当前批次花费的时间 $S + \sum_{k=i}^j T_k$ 会把后面所有尚未分批的任务完成时刻整体往后推迟，如果不记录当前累计时刻，就无法算代价。
**巧妙解法（从后往前定义后缀状态 / 费用提前计算）**：
定义 **$F[i]$** 为将后缀任务 $i, i+1, \dots, n$ 从时刻 $0$ 开始分批处理所能取得的最小总成本（边界 $F[n + 1] = 0$）。
假设当前第一批包含了任务 $i, \dots, j \ (i \le j \le n)$：
- 这一批任务本身的耗时为 $d = S + \sum_{k=i}^j T_k$；
- 这一批任务不仅让本批内的任务 $i \dots j$ 在时刻 $d$ 完成（产生成本 $d \sum_{k=i}^j C_k$），而且**使后面所有的剩余任务 $j+1 \dots n$ 的完成时刻全都统一往后推迟了 $d$**（额外增加成本 $d \sum_{k=j+1}^n C_k$）！
将这两部分合并，当前批次耗时 $d$ 对后续所有任务 $i \dots n$ 造成的总成本贡献恰好是 **$d \cdot \sum_{k=i}^n C_k$**！因此状态转移方程为：

$$
F[i] = \min_{i \le j \le n} \left\{ F[j + 1] + \left(S + \sum_{k=i}^j T_k\right) \sum_{k=i}^n C_k \right\}, \qquad i = n, n-1, \dots, 1
$$

预处理 $T$ 和 $C$ 的前缀和后，每次转移 $O(1)$，总时间复杂度为 **$O(n^2)$**！

---

**2. 完全平方数最少项数（Exercise 8.11）**：
视为硬币面额为 $1^2, 2^2, \dots, \lfloor\sqrt{n}\rfloor^2$ 的零钱兑换问题：$Q[0] = 0$，对 $x = 1 \dots n$ 有：

$$
Q[x] = 1 + \min_{1 \le t \le \lfloor\sqrt{x}\rfloor} Q[x - t^2]
$$

每个 $x$ 尝试 $\lfloor\sqrt{x}\rfloor \le \sqrt{n}$ 种平方数，总时间复杂度为 **$O(n\sqrt{n})$**。

---

**3. RNA 二级结构最大不交叉碱基配对（Exercise 8.12，Kleinberg & Tardos 经典区间 DP）**：
定义区间状态 **$R[i, j]$** 为子序列 $s[i..j]$ 内部能形成的最大合法配对数（当 $j - i < 5$ 时 $R[i, j] = 0$）。
考察区间右端点 $j$ 的碱基 $s[j]$：
1. **若 $s[j]$ 不参与任何配对**：最大配对数为 $R[i, j - 1]$；
2. **若 $s[j]$ 与区间内某个位置 $k \ (i \le k \le j - 5$，且 $s[k]$ 与 $s[j]$ 满足 `A-U` 或 `C-G` 互补) 配对**：
   由于弧线不能交叉，弧线 $(k, j)$ 将剩余位置严格隔离为**弧线左侧外部 $[i, k - 1]$** 和**弧线内部 $[k + 1, j - 1]$** 两个互不干扰的独立子区间！
   因此状态转移方程为：
   $$
   R[i, j] = \max\left\{ R[i, j - 1], \ \ \max_{\substack{i \le k \le j - 5 \\ s[k]\text{ pairs with }s[j]}} \big\{ 1 + R[i, k - 1] + R[k + 1, j - 1] \big\} \right\}
   $$
   按区间长度 $len = j - i$ 从 $5$ 到 $n-1$ 递增填表，共有 $O(n^2)$ 个区间，每个区间枚举 $O(n)$ 个配对点 $k$，总时间复杂度为 **$O(n^3)$**。

---

**4. Bellman-Ford 一维原地数组与 Floyd 循环顺序辨析（Exercise 8.13）**：

- **(1) 错误**：在一维数组 `d[v]` 原地更新的 Bellman-Ford 中，如果在第 $1$ 轮按顺序依次扫描边 $(s, u)$ 和 $(u, v)$，那么扫描 $(s, u)$ 时已经将 `d[u]` 更新为 $w(s, u)$，紧接着在同一轮扫描 $(u, v)$ 时就会立刻用刚更新的 `d[u]` 把 `d[v]` 更新为 $w(s, u) + w(u, v)$（一条含 2 条边的路径）！因此一维原地实现在第 $k$ 轮结束时满足 $d[v] \le D_k[v]$，可能已经提前算出了超过 $k$ 条边的更短路径（但这不影响最终收敛性与负环判定的正确性）。
- **(2) 错误**：反例：设图含 4 个顶点和三条有向边 $1 \to 3 \to 4 \to 2$（边权均为 $1$）。若将循环顺序改为 `for i -> for j -> for k`（把 $k$ 放在最内层），当外层算到 `(i=1, j=2)` 时，它枚举 $k=3$ 需要用到 `D[3][2]`，枚举 $k=4$ 需要用到 `D[1][4]`；但此时外层循环才刚走到 $i=1, j=2$，`D[1][4]`（需等 $j=4$ 时才算）和 `D[3][2]`（需等 $i=3$ 时才算）都还是初始的 $+\infty$！导致 `D[1][2]` 算完后依然是 $+\infty$，且此后再也不会回到 `(1, 2)`，彻底漏掉了 $1 \to 3 \to 4 \to 2$ 这条最短路径！

</details>