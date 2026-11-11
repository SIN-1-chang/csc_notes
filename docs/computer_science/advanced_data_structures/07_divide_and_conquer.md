# Chapter 7: Divide and Conquer（分治算法）

!!! abstract
    Advanced Data Structures and Algorithm Analysis (ADS) | 第七章课堂、板书与讲义笔记
    
    参考：
    
    - Course Slides Lecture 7: *Divide and Conquer*
    - 课堂手写板书 (`ADS26W8.pdf`) & 课程讲义 Lecture 7:《分治法》
    - *CLRS* (3rd Ed.), Ch. 4, Ch. 9.3 & Ch. 30; M. A. Weiss, *Data Structures and Algorithm Analysis in C* (2nd Ed.), Ch. 10.2

## 1 分治法基本框架与递推式求解方法 (Paradigm and Solving Recurrences)

### 1.1 分治法三步曲与通用递推方程

**分治法**（Divide and Conquer）将规模为 $N$ 的原问题递归地拆解求解，每层递归包含三个核心步骤：

1. **Divide（分解）**：将原问题划分为若干个规模较小的同类子问题；
2. **Conquer（解决）**：递归地求解各个子问题（当子问题规模足够小时，直接作为基准情形 Base case 在 $\Theta(1)$ 时间内求解）；
3. **Combine（合并）**：将各个子问题的解合并为原问题的最终解。

设原问题被分解为 $a$ 个子问题，每个子问题的规模是原问题的 $1/b$，且分解输入与合并子问题解所需的总附加时间为 $f(N)$，则分治算法的时间复杂度满足**通用递推关系**（General recurrence）：

$$T(N) = a T(N / b) + f(N)$$

（在渐近分析中，通常忽略 $N/b$ 的向上/向下取整细节 $\lfloor N/b \rfloor, \lceil N/b \rceil$，并默认小规模基准情形满足 $T(n) = \Theta(1)$）。
基础课程中接触过的典型分治案例包括：最大子序列和的 $O(N\log N)$ 分治解法（$a=b=2, \ f(N)=O(N)$）、树遍历 $O(N)$、归并排序（Mergesort）与快速排序（Quicksort）的 $O(N\log N)$ 解法。

### 1.2 方法一：代入法 (Substitution Method) 与归纳陷阱

**代入法**（Substitution Method）分为两步：① **先猜测（Guess）**解的渐近形式；② **再用数学归纳法（Mathematical Induction）**确定常数 $c$ 并证明猜测成立。

**1. 正确示例：证明 $T(N) = 2T(\lfloor N/2 \rfloor) + N = O(N\log N)$（Slide 8）**

- **猜测**：$T(N) \le c N \log_2 N$（对所有 $N \ge 2$ 及某个待定常数 $c > 0$）。
- **归纳证明**：假设对所有小于 $N$ 的正整数（特别是 $m = \lfloor N/2 \rfloor$）有 $T(\lfloor N/2 \rfloor) \le c \lfloor N/2 \rfloor \log_2 \lfloor N/2 \rfloor$。代入原递推式：
  $$\begin{aligned} T(N) &\le 2\Big(c \lfloor N/2 \rfloor \log_2 \lfloor N/2 \rfloor\Big) + N \\ &\le c N \log_2(N / 2) + N = c N (\log_2 N - \log_2 2) + N \\ &= c N \log_2 N - (c - 1)N \le c N \log_2 N \qquad (\text{只需取 } c \ge 1) \end{aligned}$$
  再检查边界基例 $T(2) = 4, \ T(3) = 5$，只需把常数 $c$ 取得足够大（如 $c \ge 2$）即可同时满足归纳基与归纳步。

**2. 经典归纳陷阱与“减去低阶项”强化归纳法（Slide 9 & 讲义例 7.3）**

!!! danger "核心考点：为什么在归纳步中绝不能寫出 $\le cN + N = O(N)$？"
    - **错误示范（Slide 9）**：对 $T(N) = 2T(\lfloor N/2 \rfloor) + N$，若错误猜测 $T(N) = O(N)$（即 $T(m) \le cm$），代入后会得到：
      $$T(N) \le 2c\lfloor N/2 \rfloor + N \le cN + N = (c + 1)N \stackrel{?}{=} O(N) \quad (\times \text{ 严格错误！})$$
      **错误原因**：数学归纳法要求在归纳步結束时必须**严格恢复与归纳假设完全一致的形式 $\le cN$（常数 $c$ 绝对不能变大）**！如果每递归一层常数从 $c$ 变成 $c+1$，递归 $\log N$ 层后常数就会膨胀为 $c + \log N$，不再是常数！
    - **正确技巧：当猜测本身是正确的（如 $T(N) = 2T(N/2) + 1 = O(N)$），但直接代入 $cN$ 会多出 $+1$（得到 $cN + 1$）时怎么办？**
      此时应采用**减去低阶项的强化归纳假设（Subtracting a lower-order term）**——设 $T(m) \le cm - d$（其中 $d > 0$ 为待定常数）。代入递推式：
      $$T(N) = 2T(N/2) + 1 \le 2\left(c\frac{N}{2} - d\right) + 1 = cN - 2d + 1 \le cN - d \qquad (\text{只需取 } d \ge 1)$$
      通过两个子问题各自贡献一个 $-d$，产生 $-2d$ 来抵消多出的 $+1$，完美保持了 $\le cN - d$ 的精确形式！

### 1.3 方法二：递归树法 (Recursion-Tree Method)

将递推式展开为一棵**递归树**（Recursion tree），根节点代表原问题的非递归开销 $f(N)$，第 $i$ 层代表规模为 $N/b^i$ 的 $a^i$ 个子问题的非递归开销，叶子代表规模为 $1$ 的基准开销 $\Theta(1)$。将树中所有层的开销累加即可求出总时间（既可直接求精确渐近阶，也可用于生成好的猜测再由代入法验证）。

1. **等分递归树与老师板书 $\dfrac{a}{b^c}$ 判据（板书 `W8` Pages 8–11）**：
   考察 $T(n) = aT(n/b) + n^c, \ T(1) = 1$。递归树深度为 $\log_b n$：
   - 第 $0$ 层开销：$n^c$；
   - 第 $1$ 层开销：$a \cdot \left(\frac{n}{b}\right)^c = n^c \left(\frac{a}{b^c}\right)$；
   - 第 $i$ 层开销：$a^i \cdot \left(\frac{n}{b^i}\right)^c = n^c \left(\frac{a}{b^c}\right)^i$。
   对所有层从 $i = 0$ 到 $\log_b n$ 求等比级数和，完全取决于公比 $r = \dfrac{a}{b^c}$ 与 $1$ 的大小关系：
   - **情形 A（$\dfrac{a}{b^c} < 1$，每层开销按等比级数递减，根主导）**：如 $T(N) = 3T(N/4) + cN^2$（公比 $\frac{3}{16} < 1$），总和收敛于首项的常数倍：$T(n) = O(n^c)$；
   - **情形 B（$\dfrac{a}{b^c} = 1$，每层开销全部相等）**：如 $T(n) = 2T(n/2) + n$（公比 $\frac{2}{2^1} = 1$），共 $\log_b n$ 层每层均为 $n^c$，故 $T(n) = \Theta(n^c \log_b n)$；
   - **情形 C（$\dfrac{a}{b^c} > 1$，每层开销按等比级数递增，叶子主导）**：如 $T(n) = 2T(n/2) + \sqrt{n}$（公比 $\frac{2}{\sqrt{2}} = \sqrt{2} > 1$），等比级数和由最后一层（$i = \log_b n$）主导。利用对数换底公式 $a^{\log_b n} = \left(b^{\log_b a}\right)^{\log_b n} = \left(b^{\log_b n}\right)^{\log_b a} = n^{\log_b a}$：
     $$T(n) = \Theta\left(n^c \left(\frac{a}{b^c}\right)^{\log_b n}\right) = \Theta\left(n^c \frac{a^{\log_b n}}{(b^{\log_b n})^c}\right) = \Theta\left(a^{\log_b n}\right) = \Theta\left(n^{\log_b a}\right)$$
2. **非均匀划分递归树：$T(N) = T(N/3) + T(2N/3) + cN$（Slide 11）**：
   每次将问题分为 $1/3$ 和 $2/3$ 两部分。在到达最早叶子之前，每一层所有子问题的规模之和恒为 $\left(\frac{1}{3} + \frac{2}{3}\right)^i N = N$，故每层开销恒为 $cN$！
   - 最短路径（一路走 $N/3$）深度为 $\log_3 N$ $\implies T(N) \ge cN\log_3 N = \Omega(N\log N)$；
   - 最长路径（一路走 $2N/3$）深度为 $\log_{3/2} N$（树并非满树，后面几层开销 $< cN$）$\implies T(N) \le cN\log_{3/2} N = O(N\log N)$。
   - 代入法严格验证：取 $T(N) \le d N \log_2 N$，代入得 $T(N) \le d N \log_2 N - dN\left(\log_2 3 - \frac{2}{3}\right) + cN \le d N \log_2 N$（只需取常数 $d \ge \frac{c}{\log_2 3 - 2/3}$），证得 $T(N) = \Theta(N\log N)$。

### 1.4 方法三：主定理的三种等价形式 (Master Theorem) 与 Akra-Bazzi 公式

课程组 PPT（Slides 12, 15, 16）给出了求解 $T(N) = aT(N/b) + f(N)$（其中常数 $a \ge 1, \ b > 1$）的**主定理（Master Theorem）的三种形式**，做题时可根据 $f(N)$ 的具体形态灵活选用：

| 主定理形式 | Case 1：叶子（递归分叉）主导 | Case 2：各层势均力敌 | Case 3：根（合并开销 $f(N)$）主导 |
| :--- | :--- | :--- | :--- |
| **形式一：标准 CLRS 形式**<br>（比较 $f(N)$ 与临界幂 $N^{\log_b a}$，需存在多项式间隙 $\epsilon > 0$） | 若 $f(N) = O\left(N^{\log_b a - \epsilon}\right)$（$\epsilon > 0$），则：<br>$$T(N) = \Theta\left(N^{\log_b a}\right)$$ | 若 $f(N) = \Theta\left(N^{\log_b a}\right)$，则：<br>$$T(N) = \Theta\left(N^{\log_b a}\log N\right)$$ | 若 $f(N) = \Omega\left(N^{\log_b a + \epsilon}\right)$（$\epsilon > 0$），且满足**正则条件（Regularity condition）**：存在 $c < 1$ 使 $af(N/b) \le cf(N)$，则：<br>$$T(N) = \Theta\big(f(N)\big)$$ |
| **形式二：相邻层比值形式**<br>（Slide 15：直接计算下一层总开销 $af(N/b)$ 与当前层 $f(N)$ 之比） | 若 $af(N/b) = K f(N)$，其中常数 **$K > 1$**，则：<br>$$T(N) = \Theta\left(N^{\log_b a}\right)$$ | 若 $af(N/b) = f(N)$（比值恒为 **$1$**），则：<br>$$T(N) = \Theta\big(f(N)\log_b N\big)$$ | 若 $af(N/b) = \kappa f(N)$，其中常数 **$\kappa < 1$**，则：<br>$$T(N) = \Theta\big(f(N)\big)$$ |
| **形式三：含对数幂扩展形式**<br>（Slide 16 & 讲义定理 7.8：$f(N) = \Theta(N^k \log^p N)$，比较 $a$ 与 $b^k$） | 若 **$a > b^k$**（即 $\log_b a > k$，对任意实数 $p$），则：<br>$$T(N) = \Theta\left(N^{\log_b a}\right)$$ | 若 **$a = b^k$**（即 $\log_b a = k$）：<br>• 当 $p > -1$：$\Theta\left(N^k \log^{p+1} N\right)$<br>• 当 $p = -1$：$\Theta\left(N^k \log\log N\right)$<br>• 当 $p < -1$：$\Theta\left(N^k\right)$ | 若 **$a < b^k$**（即 $\log_b a < k$，对任意实数 $p$），则：<br>$$T(N) = \Theta\left(N^k \log^p N\right)$$ |

**高频典型算例速查（Slides 12, 15, 16 & 讲义例 7.6）**：
- $T(N) = 2T(N/2) + N\log N$：此处 $a = b = 2 \implies N^{\log_b a} = N$。虽然 $N\log N$ 渐近大于 $N$，但 $\frac{N\log N}{N} = \log N = o(N^\epsilon)$（**不是多项式级大于，不满足标准形式 Case 3**！）。直接套用**形式三**（$a=b=2, \ k=1, \ p=1 \implies a = b^k$），立得 **$T(N) = \Theta(N\log^2 N)$**！
- $T(N) = 4T(N/2) + N\log N$：$a = 4, b = 2 \implies N^{\log_b a} = N^2$。因为 $N\log N = O(N^{2 - \epsilon})$（取 $\epsilon = 0.5$），满足标准形式 Case 1（或形式三 $a = 4 > 2^1 = b^k$），立得 **$T(N) = \Theta(N^2)$**（注意：此题不能直接套形式二，因为 $af(N/b) = 4(N/2)\log(N/2) = 2N\log N - 2N$ 与 $f(N)$ 的比值不是精确常数）。
- $T(N) = 2T(N/2) + \dfrac{N}{\log N}$：套用形式三（$a = b = 2, \ k = 1, \ p = -1$，处于调和级数临界点），立得 **$T(N) = \Theta(N\log\log N)$**。
- $T(N) = 2T(N/2) + \dfrac{N}{\log^2 N}$：套用形式三（$a = b = 2, \ k = 1, \ p = -2 < -1$，级数 $\sum \frac{1}{j^2} = \frac{\pi^2}{6}$ 收敛），立得 **$T(N) = \Theta(N)$**。

<details markdown="1">
<summary>点击展开：不均匀分治的终极武器——Akra-Bazzi 公式（讲义 §7.3.1 补充）</summary>

对于子问题缩放比例不相同的一般线性递推式：

$$T(x) = \sum_{i=1}^q a_i T(b_i x) + g(x) \qquad (a_i > 0, \ 0 < b_i < 1)$$

**Akra-Bazzi 定理**指出：先解特征方程求出唯一的实数幂指数 $s$：

$$\sum_{i=1}^q a_i b_i^s = 1$$

则递推式的渐近紧界直接由以下定积分给出：

$$T(x) = \Theta\left( x^s \left( 1 + \int_1^x \frac{g(u)}{u^{s+1}}\,du \right) \right)$$

- **应用示例**：对 $T(x) = T(x/3) + T(2x/3) + cx$，特征方程为 $\left(\frac{1}{3}\right)^s + \left(\frac{2}{3}\right)^s = 1 \implies s = 1$。代入积分得 $T(x) = \Theta\left(x\left(1 + \int_1^x \frac{cu}{u^2}\,du\right)\right) = \Theta(x\log x)$；若将 $cx$ 改为 $x^2$，则 $s=1$ 不变，积分变为 $\int_1^x \frac{u^2}{u^2}\,du = x - 1$，立得 $T(x) = \Theta(x^2)$！

</details>

---

## 2 计算几何中的分治：最近点对与二维凸包 (Closest Pair & Convex Hull)

### 2.1 平面最近点对问题 (Closest Points Problem)

**问题描述（PPT Slide 3 & 板书 `W8` Pages 4–6）**：
给定二维平面上的 $N$ 个点，找出欧氏距离最近的一对点（若有两个点坐标重合，则最近距离为 $0$）。

- **暴力枚举法（Exhaustive Search）**：检查全部 $\frac{N(N-1)}{2}$ 个点对，耗时 $T = O(N^2)$。
- **分治法（Divide and Conquer）设计思路**：
  1. **预处理排序（Pre-sorting）**：在进入递归前，先将所有点分别按 $x$ 坐标和 $y$ 坐标排序，得到两个有序数组 $P_x$ 和 $P_y$（耗时 $O(N\log N)$）。
  2. **Divide（划分）**：取 $P_x$ 的中位数位置画一条垂直分割线 $x = \bar{x}$，将点集均匀切分为左半集 $L$（$\lfloor N/2 \rfloor$ 个点）和右半集 $R$（$\lceil N/2 \rceil$ 个点），并通过一次线性扫描将 $P_y$ 拆分为保持 $y$ 坐标有序的 $L_y$ 和 $R_y$（耗时 $O(N)$）。
  3. **Conquer（递归求解左右半区）**：分别在左半区和右半区递归找出最近点对，记最小距离分别为 $\delta_L$ 和 $\delta_R$，令当前已知最小距离为：
     $$\delta = \min(\delta_L, \delta_R)$$
  4. **Combine（寻找跨越分割线的更近点对 `ClosestSplitPair`）**：
     这是决定整个算法复杂度的命门！因为 $a = b = 2$：
     - 如果在合并阶段使用暴力两两检查，耗时 $f(N) = cN^2$，则 $T(N) = 2T(N/2) + cN^2 = O(N^2)$，毫无改进（Slide 5）！
     - 如果在每层递归内部重新对条带内的点按 $y$ 排序，耗时 $f(N) = O(N\log N)$，则 $T(N) = 2T(N/2) + O(N\log N) = O(N\log^2 N)$；
     - **目标**：必须在**线性时间 $f(N) = O(N)$** 内完成跨界最近点对的查找，从而使 $T(N) = 2T(N/2) + O(N) = O(N\log N)$！

**如何在 $O(N)$ 时间内完成中心 $\delta$-条带（$\delta$-strip）扫描？（Slide 6 & 板书 `W8` Pages 5–6）**

1. **水平筛选 $\delta$-strip**：若一对跨界点 $(p_L, p_R)$ 的距离小于 $\delta$，则它们到分割线 $x = \bar{x}$ 的水平距离必定都小于 $\delta$。因此，我们只需遍历已按 $y$ 坐标排好序的数组 $P_y$，将满足 $\vert{}x - \bar{x}\vert{} < \delta$ 的点按顺序提取到数组 $S_y = (q_1, q_2, \dots, q_k)$ 中（此步耗时 $O(N)$，且 $S_y$ **天然按 $y$ 坐标递增有序**！注意在最坏情况下条带内的点数 `NumPointsInStrip` 仍可能等于 $N$）。
2. **竖直截断与八格抽屉原理（最多向后检查 7 个点！）**：
   对于条带中的每个点 $q_i$，我们只需向后检查满足纵坐标之差 **`Dist_y(q_i, q_j) < delta`** 的后续点 $q_j \ (j > i)$；一旦发现 $q_j.y - q_i.y \ge \delta$，立即 **`break` 跳出内层循环**！
   **为什么内层循环对每个 $q_i$ 最多只会检查后面的 $7$ 个点？（几何打包证明）**：
   考察以 $q_i$ 所在水平线为底边、跨越分割线左右各宽 $\delta$、向上高为 $\delta$ 的 **$2\delta \times \delta$ 矩形区域**（所有满足 $q_j.y \in [q_i.y, q_i.y + \delta)$ 的候选点 $q_j$ 都必须落在这个矩形内）。
   我们将这个 $2\delta \times \delta$ 的矩形平分为 **$8$ 个边长为 $\dfrac{\delta}{2} \times \dfrac{\delta}{2}$ 的小正方形**（左半区 4 个，右半区 4 个）：
   - 每个小正方形完全位于左半区 $L$ 或完全位于右半区 $R$；
   - 每个小正方形的最大内部距离为其对角线长度：
     $$d_{\text{diag}} = \sqrt{\left(\frac{\delta}{2}\right)^2 + \left(\frac{\delta}{2}\right)^2} = \frac{\delta}{\sqrt{2}} < \delta$$
   - 由于同属左半区（或同属右半区）的任意两点之间的距离已知**至少为 $\delta$**，根据抽屉原理，**每个 $\frac{\delta}{2} \times \frac{\delta}{2}$ 小正方形内至多只能包含 $1$ 个点**！（极端最坏情况如 Slide 6 左下角图所示：在分割线与左右边界的角点上恰好重合放置）。
   - 因此，整个 $2\delta \times \delta$ 矩形区域内总共**至多只能容纳 $8$ 个点**！扣除起点 $q_i$ 自身后，排在 $q_i$ 后面的候选点**至多只有 $7$ 个**！

```c
/* PPT Slide 6 & 板书 W8 Page 6: 线性时间检查 delta-strip 内的跨界点对 */
/* S_y (即 P[]) 包含所有在条带 |x - x_bar| < delta 内的点，且已按 y 坐标递增排好序 */
for (i = 0; i < NumPointsInStrip; i++) {
    /* 内层循环由于 if (Dist_y > delta) break，对每个 i 最多只会执行 7 次！ */
    for (j = i + 1; j < NumPointsInStrip; j++) {
        if (Dist_y(P[i], P[j]) >= delta)
            break; /* 纵坐标之差已达到或超过 delta，后续点更高，直接跳出内层循环！ */
        else if (Dist(P[i], P[j]) < delta)
            delta = Dist(P[i], P[j]);
    }
}
```

由此，内层循环只执行常数次（$\le 7$ 次），合并阶段耗时严格为 $f(N) = O(N)$，总时间复杂度为 **$T(N) = 2T(N/2) + O(N) = O(N\log N)$**！（注：讲义 §7.2.2 进一步证明了 Basic-2 优化：若将条带内的点按左右组分开存为 $Y_L$ 和 $Y_R$，每次只需将当前最低点与**对面组**的至多 **2 个点**比较距离即可）。

### 2.2 老师板书补充：二维凸包的分治算法 (2D Convex Hull)

在课堂手写板书（`ADS26W8.pdf` Pages 7–8）中，老师还讲解了计算几何的另一个经典分治问题——**二维凸包**（Convex Hull：给定平面上 $n$ 个点，找出能将所有点包围在内的最小凸多边形）：

1. **上下包络线分解**：凸包的边界可以分为**上包络线（Upper envelope / Upper hull）**和**下包络线（Lower envelope / Lower hull）**两部分分别求取。
2. **分治求解**：
   - 将点集按 $x$ 坐标排序并平分为左半点集 $L$ 和右半点集 $R$；
   - 递归求出左半凸包 $\text{CH}(L)$ 和右半凸包 $\text{CH}(R)$；
   - **线性时间合并（Finding Upper & Lower Tangents）**：利用双指针步进法（Rotating calipers / Two-finger walk）在 $O(n)$ 时间内找到同时切于左凸包和右凸包的**上公切线（Upper tangent）**与**下公切线（Lower tangent）**，删去两条公切线之间的内部折线即可合成全局凸包。
   - 递推式为 $T(n) = 2T(n/2) + O(n) = O(n\log n)$（板书同时提及了 Timothy Chan 在 1996 年提出的输出敏感型最优凸包算法 **Chan's Algorithm**，时间复杂度为 $O(n\log h)$，其中 $h$ 为最终凸包顶点个数）。

---

## 3 核心分治算法专题：逆序对、快速乘法与线性选择 (Core Algorithms)

### 3.1 逆序对计数 (Counting Inversions — 板书 `W8` Pages 2–4)

**问题描述**：给定长度为 $n$ 的数组 $A[1..n]$，若下标对 $(i, j)$ 满足 **$i < j$ 且 $A[i] > A[j]$**，则称 $(i, j)$ 为一个**逆序对**（Inversion）。数组的最大可能逆序对数为完全逆序时的 $\binom{n}{2} = \frac{n(n-1)}{2}$。

**分治策略（借力归并排序 `Sort-and-CountInv`）**：
将数组平分为左半部 $L$ 和右半部 $R$，所有的逆序对 $(i, j)$ 被划分为三类：
1. **左内部逆序对（Left inversions）**：$i, j \in L$，由左半递归计数返回；
2. **右内部逆序对（Right inversions）**：$i, j \in R$，由右半递归计数返回；
3. **跨越中点的分裂逆序对（Split inversions）**：$i \in L$ 且 $j \in R$，由合并过程 `Merge-and-CountSplit` 统计。

为了在 $O(n)$ 时间内数出所有的分裂逆序对，我们在递归计数后顺便返回**已排好序**的左半数组 $B$ 和右半数组 $C$（各自长度为 $n/2$）。用双指针 $i, j$ 归并 $B$ 和 $C$ 到输出数组 $D$：
- 若 **$B[i] \le C[j]$**：将 $B[i]$ 放入 $D[k]$，此时 $B[i]$ 小于等于 $C$ 中所有剩余元素，**不产生任何分裂逆序对**，$i \gets i + 1$；
- 若 **$B[i] > C[j]$**：将 $C[j]$ 放入 $D[k]$。由于左半数组 $B$ 是递增有序的，既然 $B[i] > C[j]$，那么**$B$ 中从下标 $i$ 到末尾 $\frac{n}{2}$ 的所有剩余元素全都严格大于 $C[j]$**！因此，这一个右侧元素 $C[j]$ 与 $B$ 中剩余元素恰好构成了 **$\left(\dfrac{n}{2} - i + 1\right)$ 个分裂逆序对**！直接累加 `splitInv += n/2 - i + 1`，然后 $j \gets j + 1$。

```c
/* 老师板书 W8 Pages 3-4: 归并排序并统计逆序对 O(n log n) */
(Array, int) Sort_and_CountInv(Array A, int n) {
    if (n <= 1) return (A, 0);
    Array L = left half of A;
    Array R = right half of A;
    (B, leftInv)  = Sort_and_CountInv(L, n / 2);
    (C, rightInv) = Sort_and_CountInv(R, n - n / 2);
    (D, splitInv) = Merge_and_CountSplit(B, C, n);
    return (D, leftInv + rightInv + splitInv);
}

(Array, int) Merge_and_CountSplit(Array B, Array C, int n) {
    int i = 1, j = 1, splitInv = 0;
    int lenB = n / 2, lenC = n - n / 2;
    Array D[1..n];
    for (int k = 1; k <= n; k++) {
        if (j > lenC || (i <= lenB && B[i] <= C[j])) {
            D[k] = B[i];
            i = i + 1;
        } else { /* B[i] > C[j]: C[j] 与 B[i ... lenB] 全部构成逆序对！ */
            D[k] = C[j];
            j = j + 1;
            splitInv = splitInv + (lenB - i + 1);
        }
    }
    return (D, splitInv);
}
```

递推式为 $T(n) = 2T(n/2) + O(n) \implies T(n) = O(n\log n)$。

### 3.2 Karatsuba 大整数乘法与 Strassen 矩阵乘法 (板书 `W8` Pages 1–2 & 讲义 §7.2.3)

**1. Karatsuba 大整数快速乘法（1960）**

设两个 $n$ 位大整数分别为 $A$ 和 $B$（传统小学竖式乘法需 $\Theta(n^2)$ 时间）。将每个数从中间拆分为高 $n/2$ 位和低 $n/2$ 位（以十进制或二进制基数 $10^{n/2}$ 为例）：

$$
A = A_H \cdot 10^{n/2} + A_L, \qquad B = B_H \cdot 10^{n/2} + B_L
$$

直接展开乘积：

$$
A \cdot B = (A_H B_H) \cdot 10^n + (A_H B_L + A_L B_H) \cdot 10^{n/2} + A_L B_L
$$

- **朴素分治的失败**：上式包含 $A_H B_H, \ A_H B_L, \ A_L B_H, \ A_L B_L$ 共 **$4$ 次**规模为 $n/2$ 的乘法，递推式为 $T(n) = 4T(n/2) + O(n)$。由主定理 Case 1 知 $T(n) = \Theta(n^{\log_2 4}) = \Theta(n^2)$，毫无加速！
- **Karatsuba 的神来之笔（代数消元将 4 次乘法降为 3 次乘法）**：
  注意到 $A_H B_H$ 和 $A_L B_L$ 本来就必须算，而中间的交叉项 $A_H B_L + A_L B_H$ 可以通过**1 次乘法加几次加减法**湊出来（板书形式与讲义形式等价）：
  $$
  \begin{aligned}
  A_H B_L + A_L B_H &= A_H B_H + A_L B_L - (A_H - A_L)(B_H - B_L) \qquad (\text{老师板书公式}) \\
  &= (A_H + A_L)(B_H + B_L) - A_H B_H - A_L B_L \qquad (\text{讲义公式})
  \end{aligned}
  $$
  这样，每层只需递归计算 **$3$ 个**规模为 $n/2$ 的乘法：$P_1 = A_H B_H$、$P_2 = A_L B_L$ 和 $P_3 = (A_H - A_L)(B_H - B_L)$！递推式降为：
  $$
  T(n) = 3T(n / 2) + O(n) \implies T(n) = \Theta\left(n^{\log_2 3}\right) \approx O\left(n^{1.585}\right) \ll O(n^2)
  $$

**2. Strassen 矩阵快速乘法（1969）**

将两个 $n \times n$ 方阵 $A, B$ 均分为四个 $\frac{n}{2} \times \frac{n}{2}$ 的子分块矩阵 $\begin{pmatrix} A_1 & A_2 \\ A_3 & A_4 \end{pmatrix}$ 与 $\begin{pmatrix} B_1 & B_2 \\ B_3 & B_4 \end{pmatrix}$。
朴素分块乘法需要计算 $8$ 次子矩阵乘法（$T(n) = 8T(n/2) + O(n^2) = \Theta(n^{\log_2 8}) = \Theta(n^3)$）。
Strassen 巧妙构造了 **$7$ 个辅助乘积矩阵** $M_1, \dots, M_7$（仅需 $7$ 次规模为 $n/2$ 的递归矩阵乘法和 $18$ 次 $O(n^2)$ 的矩阵加减法）：

$$
\begin{aligned}
M_1 &= (A_1 + A_4)(B_1 + B_4), \quad & M_2 &= (A_3 + A_4)B_1, \quad & M_3 &= A_1(B_2 - B_4), \quad & M_4 &= A_4(B_3 - B_1), \\
M_5 &= (A_1 + A_2)B_4, \quad & M_6 &= (A_3 - A_1)(B_1 + B_2), \quad & M_7 &= (A_2 - A_4)(B_3 + B_4),
\end{aligned}
$$

进而组合出结果分块 $C_1 = M_1 + M_4 - M_5 + M_7, \ C_2 = M_3 + M_5, \ C_3 = M_2 + M_4, \ C_4 = M_1 - M_2 + M_3 + M_6$。递推式降为：

$$
T(n) = 7T(n / 2) + O(n^2) \implies T(n) = \Theta\left(n^{\log_2 7}\right) \approx O\left(n^{2.807}\right)
$$

### 3.3 确定性线性时间选择 (Median-of-Medians) 与快速傅里叶变换 (FFT)

<details markdown="1">
<summary>点击展开：五元组中位数的中位数算法（BFPRT 最坏 O(n) 选择）与 FFT 原理（讲义 §7.2.4 & §7.3.2）</summary>

**1. 确定性线性时间选择算法（Selection in Worst-Case $O(n)$ Time）**

要在未排序的 $n$ 个元素中找出第 $k$ 小的元素，快速选择（Quickselect）在最坏情况下若每次选到极值作为主元（Pivot），会退化为 $T(n) = T(n-1) + O(n) = O(n^2)$。为了保证在**最坏情况下也能每次淘汰固定比例的元素**，BFPRT 算法按如下步骤确定好主元 $v$：
1. **五元分组**：将 $n$ 个元素每 $5$ 个分成一组（共 $g = \lceil n/5 \rceil$ 组），每组内部用 $O(1)$ 时间排序并取出各自的中位数；
2. **递归找中位数的中位数**：递归调用 `Select` 找出这 $\lceil n/5 \rceil$ 个组中位数的中位数，作为划分基准值 $v$（耗时 $T(\lceil n/5 \rceil)$）；
3. **三路划分与淘汰比例下界**：
   在 $\lceil n/5 \rceil$ 个组中，至少有一半（$\ge \lceil g/2 \rceil$ 个组）的组中位数 $\ge v$；而在每个这样的完整 $5$ 元组中，中位数及其上方的两个元素（共 $3$ 个元素）都 $\ge v$！除去可能不满 $5$ 人的最后一组和 $v$ 所在组，全数组中**至少有 $3\left(\lceil n/10 \rceil - 2\right) \ge \frac{3}{10}n - 6$ 个元素 $\ge v$**（同理也至少有 $\frac{3}{10}n - 6$ 个元素 $\le v$）。
   因此，下一轮递归进入的 $L$（严格小于 $v$）或 $G$（严格大于 $v$）的规模**至多为 $\frac{7}{10}n + 6$**！
4. **递推方程求解**：
   $$
   T(n) \le T(\lceil n / 5 \rceil) + T(\lfloor 7n / 10 + 6 \rfloor) + cn
   $$
   因为子问题规模比例之和为 $\frac{1}{5} + \frac{7}{10} = \frac{9}{10} < 1$（严格小于 $1$！），用代入法（当 $n > 140$ 时取 $d \ge 20c$）或 Akra-Bazzi 公式立证 **$T(n) = O(n)$**！

---

**2. 快速傅里叶变换（Fast Fourier Transform, FFT）求多项式乘法**

计算两个 $n-1$ 次多项式 $A(x) = \sum_{j=0}^{n-1} a_j x^j$ 与 $B(x)$ 的乘积 $C(x) = A(x)B(x)$（系数卷积）：
1. **系数表示 $\xrightarrow{\text{FFT } O(n\log n)}$ 点值表示**：选取 $n$（补零至 $2$ 的幂）个复平面上的 **$n$ 次本原单位根** $\omega_n^k = e^{i 2\pi k / n} = \cos\frac{2\pi k}{n} + i\sin\frac{2\pi k}{n} \ (k = 0, \dots, n-1)$。
   将 $A(x)$ 按偶次项和奇次项拆分为 $A(x) = E(x^2) + x O(x^2)$。利用单位根的折半性质 $\left(\omega_n^{j + n/2}\right)^2 = \left(-\omega_n^j\right)^2 = \omega_n^{2j} = \omega_{n/2}^j$，$n$ 个点的求值问题瞬间折半为两个规模为 $n/2$ 的子问题 $E(\omega_{n/2}^j)$ 和 $O(\omega_{n/2}^j)$，再通过**蝶形运算**（Butterfly operation）合并：
   $$
   A(\omega_n^j) = E(\omega_{n/2}^j) + \omega_n^j O(\omega_{n/2}^j), \qquad A(\omega_n^{j + n/2}) = E(\omega_{n/2}^j) - \omega_n^j O(\omega_{n/2}^j)
   $$
   递推式为 $T(n) = 2T(n/2) + O(n) = O(n\log n)$。
2. **逐点相乘 $O(n)$**：$C(\omega_n^j) = A(\omega_n^j) \cdot B(\omega_n^j)$。
3. **逆变换 IDFT $\xrightarrow{\text{IFFT } O(n\log n)}$ 恢复系数**：将单位根换为共轭逆元 $\omega_n^{-1}$ 再次调用同一个 FFT 算法，最后将结果除以 $n$，即可在 $O(n\log n)$ 时间内恢复乘积多项式的全部系数（在模素数 $p$ 整数环下可用原根替代复单位根，即**数论变换 NTT**，避免浮点舍入误差）。

</details>

---

## 4 Chapter 7 核心习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 7.1, 7.2 & 7.3: Recurrence True/False, Shifted Recurrence & Non-Constant Base Case（递推式辨析、含常数偏移换元与非1终止阈值）</summary>

**Problem Statement:**
- **Ex 7.1**: 判断下列结论是否正确并说明理由：
  (1) 若 $T(n) = T(n/5) + T(7n/10) + O(n)$，则 $T(n) = O(n)$。如果把两个比例改为 $1/6$ 和 $7/9$，结论是否仍成立？
  (2) 每次递归产生 $7$ 个规模为 $n/3$ 的子问题，且附加成本为 $O(n^2)$，则总成本一定为 $\Theta(n^2)$。
  (3) 若 $T(n) = 2T(n/2) + n / (\log n)^2$，则 $T(n) = \Theta(n)$。
- **Ex 7.2**: 设正整数函数 $T(n)$ 满足：当 $1 \le n \le 68$ 时 $T(n) = 1$；当 $n > 68$ 时 $T(n) = 2T(\lfloor n/2 \rfloor + 17) + n$。求 $T(n)$ 的渐近紧界。
- **Ex 7.3**: 设整数 $M \ge 1$，递推式为：当 $n^2 > M$ 时 $T(n) = 8T(n/2) + 1$；当 $n^2 \le M$ 时停止递归且耗时 $T(n) = M$。求 $T(n)$ 关于 $n$ 和 $M$ 的渐近紧界。

---

**解答与解析：**

**1. 基础递推式概念辨析（Exercise 7.1）**：

- **(1) 正确（且改为 $1/6$ 和 $7/9$ 依然成立）**：
  对于 $T(n) \le T(\alpha n) + T(\beta n) + cn$，只要两个缩放比例之和满足 **$\alpha + \beta < 1$**，递归树每向下一层，所有子问题的总规模就按公比 $r = \alpha + \beta < 1$ 严格指数衰减，所有层的开销之和为收敛等比级数 $\le \frac{cn}{1 - (\alpha + \beta)} = O(n)$！
  这里 $\frac{1}{5} + \frac{7}{10} = \frac{9}{10} < 1$；改为 $\frac{1}{6} + \frac{7}{9} = \frac{3 + 14}{18} = \frac{17}{18} < 1$，依然小于 $1$，故仍为 $O(n)$。
- **(2) 错误（大 $O$ 与 $\Theta$ 的经典陷阱！）**：
  题目说附加成本是 **$O(n^2)$（只给了上界，没给下界）**，而不是 $\Theta(n^2)$！
  例如，若附加成本实际上恒为常数 $f(n) = 1$（显然 $1 \in O(n^2)$），此时递推式为 $T(n) = 7T(n/3) + 1$，由主定理 Case 1 知其真实紧界为 $\Theta(n^{\log_3 7}) \approx \Theta(n^{1.77})$，根本达不到 $\Theta(n^2)$！只能说总成本为 $O(n^2)$，不能断定是 $\Theta(n^2)$。
- **(3) 正确**：
  直接套用主定理形式三（定理 7.8）：$a = b = 2 \implies k = \log_2 2 = 1$，而对数幂指数 $p = -2 < -1$。因为级数 $\sum_{j=1}^{\log_2 n} \frac{1}{j^2} < \frac{\pi^2}{6} = O(1)$ 收敛，故总时间由叶子层主导，为 $\Theta(n^k) = \Theta(n)$。

---

**2. 换元法消去子问题规模中的常数偏移 $+17$（Exercise 7.2）**：
为了消去 $\lfloor n/2 \rfloor + 17$ 中的常数 $+17$，令不动点满足 $x = \frac{x}{2} + 17 \implies x = 34$。
作变量代换：令 **$m = n - 34$**（即 $n = m + 34$），并定义新函数 $S(m) \equiv T(m + 34)$。
当 $n > 68$（即 $m > 34$）时，注意到 $\lfloor \frac{m + 34}{2} \rfloor + 17 = \lfloor \frac{m}{2} \rfloor + 17 + 17 = \lfloor \frac{m}{2} \rfloor + 34$，代入原递推式得：

$$
S(m) = T(m + 34) = 2 T\big(\lfloor m/2 \rfloor + 34\big) + (m + 34) = 2 S(\lfloor m/2 \rfloor) + m + 34
$$

当 $m > 34$ 时，$m < m + 34 < 2m$，即非递归附加项为 $\Theta(m)$。由标准主定理 Case 2 知 $S(m) = \Theta(m\log m)$。代回 $m = n - 34 = \Theta(n)$，即得 **$T(n) = \Theta(n\log n)$**。

---

**3. 终止阈值含参数 $M$ 的递归树求解（Exercise 7.3）**：
- 若初始就有 $n^2 \le M$（即 $n \le \sqrt{M}$），则无需递归直接返回，耗时 $T(n) = \Theta(M)$。
- 若 $n^2 > M$（即 $n > \sqrt{M}$），设经过 $d$ 层递归后子问题规模 $n / 2^d$ 首次满足终止条件 $(n / 2^d)^2 \le M \iff \frac{n}{2^d} \le \sqrt{M}$：
  $$
  2^d = \Theta\left(\frac{n}{\sqrt{M}}\right) \implies d = \left\lceil \log_2\left(\frac{n}{\sqrt{M}}\right) \right\rceil
  $$
  在深度为 $d$ 的终止层上，共有 $8^d$ 个叶子，**每个叶子的基准开销为 $M$**！而前面 $i = 0, \dots, d-1$ 层的非叶节点每个仅耗时 $1$。因此总耗时为：
  $$
  T(n) = M \cdot 8^d + \sum_{i=0}^{d-1} 8^i = M \cdot 8^d + \frac{8^d - 1}{7} = \Theta\left(M \cdot (2^d)^3\right) = \Theta\left(M \cdot \left(\frac{n}{\sqrt{M}}\right)^3\right) = \Theta\left(\frac{n^3}{\sqrt{M}}\right)
  $$

</details>

<details markdown="1">
<summary>Exercise 7.4, 7.5 & 7.6: Harmonic Loop Recurrence, Ternary Search & Selection Group Size（调和循环递推式、单谷三分搜索与线性选择分组大小分析）</summary>

**Problem Statement:**
- **Ex 7.4**: 在下面的分治程序 `Fun(l, r)` 中，单次 `Calc` 耗时 $\Theta(1)$，求 `Fun(1, N)` 的时间复杂度紧界：
  ```c
  void Fun(int l, int r) {
      int n = r - l + 1;
      if (n <= 1234) return;
      int m = (l + r) / 2, m1 = (l + m) / 2, m2 = (m + 1 + r) / 2;
      Fun(l, m); Fun(m1 + 1, m2);
      for (int k = 1; k <= n; k++)
          for (int i = 1; i <= n; i++)
              for (int j = l; j <= r; j += i) /* 步长为 i ! */
                  Calc(j, i);
      Fun(m + 1, r); Fun(m1 + 1, m2);
  }
  ```
- **Ex 7.5**: 设非空数组 $A[1..n]$ 先严格递减、后严格递增（单谷函数 Unimodal array），且最低点唯一。设计三分搜索（Ternary search）算法找出最低点，并分析时间复杂度。
- **Ex 7.6**: 在确定性线性时间选择（Median-of-Medians）算法中，如果将“每 5 个元素一组”改为“每 7 个元素一组”，证明算法仍有 $O(n)$ 时间上界；如果改为“每 3 个元素一组”，能得到什么时间上界？

---

**解答与解析：**

**1. 变步长调和循环与四分支递归分析（Exercise 7.4，期末必考代码阅读题型）**：

- **第一步：计算三层 `for` 循环的非递归开销 $f(n)$**：
  注意最内层 `j` 循环的步长是 **`j += i`**（而不是 `j++`）！
  因此对于固定的 $i$，内层循环执行的次数为 $\lceil n / i \rceil = \Theta\left(\frac{n}{i}\right)$。
  对中间层 $i = 1, 2, \dots, n$ 求和，得到调和级数：
  $$
  \sum_{i=1}^n \left\lceil \frac{n}{i} \right\rceil = \Theta\left(n \sum_{i=1}^n \frac{1}{i}\right) = \Theta(n \log n)
  $$
  再乘上最外层 $k = 1 \dots n$ 的 $n$ 次循环，得到本层的非递归附加开销为：
  $$
  f(n) = n \cdot \Theta(n\log n) = \Theta\left(n^2 \log n\right)
  $$
- **第二步：统计递归调用次数 $a$ 与缩放因子 $b$**：
  函数内部共调用了 **4 次** `Fun`：`Fun(l, m)`（长度 $n/2$）、两次 `Fun(m1+1, m2)`（区间从 $n/4$ 到 $3n/4$，长度也是 $n/2$！）以及 `Fun(m+1, r)`（长度 $n/2$）。
  因此 $a = 4, \ b = 2$，递推方程为：
  $$
  T(n) = 4T(n / 2) + \Theta\left(n^2 \log n\right)
  $$
- **第三步：套用扩展主定理（定理 7.8）求解**：
  此处 $\log_b a = \log_2 4 = 2 = k$，且对数幂 $p = 1 > -1$（处于 Case 2 的共振区，多乘一个 $\log n$ 因子），故总时间复杂度紧界为 **$\Theta\left(N^2 \log^2 N\right)$**！

---

**2. 单谷数组的三分搜索算法（Exercise 7.5）**：
在区间 $[l, r]$ 内取两个三等分点：$m_1 = l + \lfloor(r - l)/3\rfloor$，$m_2 = l + \lfloor 2(r - l)/3 \rfloor$（满足 $l \le m_1 < m_2 \le r$）。比较 $A[m_1]$ 与 $A[m_2]$：
- **若 $A[m_1] < A[m_2]$**：由于数组先严格递减后严格递增，最低点绝不可能位于 $m_2$ 的右侧（在 $m_2$ 右侧函数必然处于递增段，高于 $A[m_1]$），故直接舍弃右段的 $(m_2, r]$，保留区间 **$[l, m_2]$**；
- **若 $A[m_1] > A[m_2]$**：同理，最低点绝不可能位于 $m_1$ 的左侧，直接舍弃左段的 $[l, m_1)$，保留区间 **$[m_1, r]$**；
- **若 $A[m_1] == A[m_2]$**：最低点必严格夹在 $[m_1, m_2]$ 之间，保留 $[m_1, m_2]$；
- 当区间长度 $r - l + 1 \le 3$ 时，直接比较这至多 3 个元素返回最小值。
每次比较耗时 $O(1)$，且将搜索区间长度缩减为原来的至多 $2/3$，递推式为 $T(n) = T(2n / 3) + O(1) \implies T(n) = O(\log n)$。

---

**3. 线性时间选择算法改为 7 元分组 vs. 3 元分组（Exercise 7.6，经典理论必考题）**：

- **若改为每 $7$ 个元素一组（仍为线性 $O(n)$）**：
  共有 $\lceil n/7 \rceil$ 个组，找中位数的中位数 $v$ 耗时 $T(\lceil n/7 \rceil)$。
  在至少一半（$\frac{1}{2}\lceil n/7 \rceil$）的组中，每组有 **$4$ 个元素**（中位数及上方 3 个元素）$\ge v$。因此至少有 $\frac{4}{14}n - O(1) = \frac{2}{7}n - O(1)$ 个元素被淘汰，剩余进入下一轮递归的子问题规模至多为 $n - \frac{2}{7}n = \frac{5}{7}n + O(1)$。
  递推式为：
  $$
  T(n) \le T(n / 7 + O(1)) + T(5n / 7 + O(1)) + cn
  $$
  由于两个子问题规模比例之和为 **$\dfrac{1}{7} + \dfrac{5}{7} = \dfrac{6}{7} < 1$**，总时间依然收敛为线性 **$O(n)$**！
- **若改为每 $3$ 个元素一组（退化为 $O(n\log n)$，失去线性保证！）**：
  共有 $\lceil n/3 \rceil$ 个组，找中位数的中位数耗时 $T(\lceil n/3 \rceil)$。
  在至少一半（$\frac{1}{2}\lceil n/3 \rceil$）的组中，每组只有 **$2$ 个元素** $\ge v$，故至少淘汰 $\frac{2}{6}n - O(1) = \frac{1}{3}n - O(1)$ 个元素，剩余子问题规模至多为 $n - \frac{1}{3}n = \frac{2}{3}n + O(1)$。
  此时的递推式变为：
  $$
  T(n) = T(n / 3) + T(2n / 3) + cn
  $$
  由于两个子问题规模比例之和恰好等于 **$\dfrac{1}{3} + \dfrac{2}{3} = 1$**（递归树每一层的总工作量都不衰减，恒为 $cn$），由 §1.3 例 2 可知，时间复杂度将退化为 **$T(n) = \Theta(n\log n)$**！（这解释了为什么 BFPRT 算法最少必须以 **$5$** 个元素为一组）。

</details>