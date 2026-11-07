# 多维随机变量及其分布

!!! abstract
    概率论与数理统计 | 第三章课堂笔记
    
    参考：
    
    - 《概率论与数理统计（第二版）》，高等教育出版社，2023 — Chapter 3: Multivariate Random Variables and Their Distributions
    - 浙江大学数学科学学院《概率论和数理统计》课程讲义（黄炜）

## 1 二维随机变量与离散型分布

### 1.1 二维随机变量的概念

在实际问题中（如同时考察学龄儿童的身高 $H$ 与体重 $W$，或同时考察市场供给模型中的多个指标），往往需要同时研究定义在同一样本空间上的多个随机变量及其相互关系。

设随机试验 $E$ 的样本空间为 $S$，$X = X(e)$ 与 $Y = Y(e)$ 是定义在 $S$ 上的两个随机变量，则称由它们构成的向量 $(X, Y)$ 为**二维（元）随机向量**或**二维（元）随机变量**（bivariate random variable/vector），其取值落入二维实平面 $\mathbb{R}^2$ 中。

### 1.2 二维离散型随机变量的联合分布律

若二维随机变量 $(X, Y)$ 的全部可能取值为有限对或可列无限对（即**至多可列对**），则称 $(X, Y)$ 为**二维离散型随机变量**。

设二维离散型随机变量 $(X, Y)$ 的所有可能取值为 $(x_i, y_j) \ (i, j = 1, 2, \dots)$，则称

$$
P(X = x_i, Y = y_j) = p_{ij}, \quad i, j = 1, 2, \dots
$$

为 $(X, Y)$ 的**联合概率分布律**（joint probability mass function），简称**联合分布律**。

联合分布律与边际分布律通常汇总表示为如下二维标准表格形式：

| $X \backslash Y$ | $y_1$ | $y_2$ | $\cdots$ | $y_j$ | $\cdots$ | $P(X = x_i)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$x_1$** | $p_{11}$ | $p_{12}$ | $\cdots$ | $p_{1j}$ | $\cdots$ | $p_{1\cdot}$ |
| **$x_2$** | $p_{21}$ | $p_{22}$ | $\cdots$ | $p_{2j}$ | $\cdots$ | $p_{2\cdot}$ |
| **$\vdots$** | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| **$x_i$** | $p_{i1}$ | $p_{i2}$ | $\cdots$ | $p_{ij}$ | $\cdots$ | $p_{i\cdot}$ |
| **$\vdots$** | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| **$P(Y = y_j)$** | $p_{\cdot 1}$ | $p_{\cdot 2}$ | $\cdots$ | $p_{\cdot j}$ | $\cdots$ | $1$ |

任何合法的联合概率分布律充要地满足以下两条基本性质：

| 性质名称 | 数学表达式 | 含义说明 |
| :--- | :--- | :--- |
| **1. 非负性** | $p_{ij} \ge 0, \quad i, j = 1, 2, \dots$ | 每个样本点对 $(x_i, y_j)$ 出现的概率非负 |
| **2. 规范性** | $\displaystyle\sum_{i=1}^\infty \sum_{j=1}^\infty p_{ij} = 1$ | 所有可能取值对的概率总和恒等于 $1$ |

### 1.3 离散型边际分布律与条件分布律

**1. 边际（边缘）分布律（Marginal p.m.f.）**

设 $(X, Y)$ 的联合分布律为 $P(X = x_i, Y = y_j) = p_{ij}$，将联合概率分别关于另一个变量的全部取值求和，即得到单个随机变量 $X$ 与 $Y$ 各自的**边际分布律**（对应联合分布表中的“行和”与“列和”）：

$$
P(X = x_i) = P\left(\bigcup_{j=1}^{+\infty} \{X = x_i, Y = y_j\}\right) = \sum_{j=1}^{+\infty} p_{ij} \xlongequal{\text{记为}} p_{i\cdot}, \quad i = 1, 2, \dots
$$

$$
P(Y = y_j) = P\left(\bigcup_{i=1}^{+\infty} \{X = x_i, Y = y_j\}\right) = \sum_{i=1}^{+\infty} p_{ij} \xlongequal{\text{记为}} p_{\cdot j}, \quad j = 1, 2, \dots
$$

**2. 条件分布律（Conditional p.m.f.）**

对于固定的 $y_j$（满足 $P(Y = y_j) = p_{\cdot j} > 0$），在给定 $\{Y = y_j\}$ 的条件下，随机变量 $X$ 的**条件分布律**定义为：

$$
P(X = x_i \mid Y = y_j) = \frac{P(X = x_i, Y = y_j)}{P(Y = y_j)} = \frac{p_{ij}}{p_{\cdot j}}, \quad i = 1, 2, \dots
$$

同理，对于固定的 $x_i$（满足 $P(X = x_i) = p_{i\cdot} > 0$），在给定 $\{X = x_i\}$ 的条件下，随机变量 $Y$ 的**条件分布律**定义为：

$$
P(Y = y_j \mid X = x_i) = \frac{P(X = x_i, Y = y_j)}{P(X = x_i)} = \frac{p_{ij}}{p_{i\cdot}}, \quad j = 1, 2, \dots
$$

条件分布律本质上也是合格的概率分布律，满足非负性 $\frac{p_{ij}}{p_{\cdot j}} \ge 0$ 与归一性 $\sum_{i=1}^\infty \frac{p_{ij}}{p_{\cdot j}} = 1$。

<details markdown="1">
<summary>典型例题：离散联合分布的构造、边际与条件分布求解（Example 2, 3, 5, 6, 7）</summary>

**1. 分阶段依赖取值的联合分布（Example 2）**

设 $X$ 在 $\{1, 2, 3, 4\}$ 中等可能取值，$Y$ 在 $1 \sim X$ 中等可能取整数值。由乘法公式，当 $1 \le j \le i \le 4$ 时：

$$
P(X = i, Y = j) = P(X = i)P(Y = j \mid X = i) = \frac{1}{4} \cdot \frac{1}{i}
$$

写成矩阵表格形式如下（当 $j > i$ 时概率均为 $0$）：

| $X \backslash Y$ | $1$ | $2$ | $3$ | $4$ |
| :---: | :---: | :---: | :---: | :---: |
| **$1$** | $1/4$ | $0$ | $0$ | $0$ |
| **$2$** | $1/8$ | $1/8$ | $0$ | $0$ |
| **$3$** | $1/12$ | $1/12$ | $1/12$ | $0$ |
| **$4$** | $1/16$ | $1/16$ | $1/16$ | $1/16$ |

---

**2. 泊松计数过程的增量联合分布（Example 3）**

足球队在长度为 $t$ 的时间段内得牌次数 $N(t) \sim P(\lambda t)$。记 $X_1, X_2$ 分别为比赛进行到 $t_1, t_2 \ (0 < t_1 < t_2)$ 分钟时的累计得牌数。利用不相交时间段增量的独立性，对 $0 \le i \le j$ 有：

$$
P(X_1 = i, X_2 = j) = P(N(t_1) = i) P(N(t_2 - t_1) = j - i) = \frac{e^{-\lambda t_1}(\lambda t_1)^i}{i!} \cdot \frac{e^{-\lambda(t_2 - t_1)}[\lambda(t_2 - t_1)]^{j - i}}{(j - i)!}
$$

---

**3. 由条件概率反求参数及复合事件条件分布（Example 5）**

设 $(X, Y)$ 的联合分布律如下表所示，且已知 $P(Y \le 0 \mid X < 2) = 0.5$：

| $X \backslash Y$ | $-1$ | $0$ | $1$ |
| :---: | :---: | :---: | :---: |
| **$1$** | $a$ | $0.2$ | $0.2$ |
| **$2$** | $0.1$ | $0.1$ | $b$ |

- **求参数 $a, b$**：由条件概率定义 $0.5 = \frac{P(X < 2, Y \le 0)}{P(X < 2)} = \frac{a + 0.2}{a + 0.4} \implies a = 0$；再由归一性 $a + b + 0.6 = 1 \implies b = 0.4$。
- **求 $\{X + Y = 2\}$ 下 $X$ 的条件分布律**：事件 $\{X + Y = 2\} = \{X=1, Y=1\} \cup \{X=2, Y=0\}$，概率为 $0.2 + 0.1 = 0.3$。故：
  $$
  P(X = 1 \mid X + Y = 2) = \frac{0.2}{0.3} = \frac{2}{3}, \qquad P(X = 2 \mid X + Y = 2) = \frac{0.1}{0.3} = \frac{1}{3}
  $$

---

**4. 不放回抽样 vs. 有放回抽样的联合分布对比（Example 6）**

盒中有 3 黑、2 红、1 白共 6 球，任取 2 球，$X$ 为黑球数，$Y$ 为红球数：

- **不放回抽样**：$P(X = i, Y = j) = \frac{C_3^i C_2^j C_1^{2 - i - j}}{C_6^2} \ (0 \le i + j \le 2)$；给定 $\{Y = 0\}$ 时，$X$ 只能在 $1, 2$ 上取值（因白球只有 1 个），$P(X = 1 \mid Y = 0) = P(X = 2 \mid Y = 0) = 1/2$。
- **有放回抽样**：每次取黑、红、白概率分别为 $3/6, 2/6, 1/6$；给定 $\{Y = 0\}$ 时，$X$ 在 $0, 1, 2$ 上的条件概率分别为 $1/16, \ 6/16, \ 9/16$。

---

**5. 首次击中次数与二次击中总次数的联合及条件分布（Example 7）**

独立射击命中率为 $p$，直至命中两次为止。记 $X$ 为首次命中的射击次数，$Y$ 为总射击次数。

- **联合分布律**：前 $n-1$ 次中仅第 $m$ 次命中，且第 $n$ 次必命中，故 $P(X = m, Y = n) = p^2(1 - p)^{n - 2} \ (m = 1, \dots, n - 1; \ n = 2, 3, \dots)$。
- **边际分布律**：对 $n$ 求和得 $P(X = m) = \sum_{n=m+1}^\infty p^2(1-p)^{n-2} = p(1-p)^{m-1} \implies X \sim Geom(p)$；对 $m$ 求和得 $P(Y = n) = (n - 1)p^2(1 - p)^{n - 2} \implies Y$ 服从参数 $(2, p)$ 的巴斯卡分布。
- **条件分布律与物理意义**：
  1. 给定总次数 $\{Y = n\}$：$P(X = m \mid Y = n) = \frac{1}{n - 1} \ (m = 1, \dots, n - 1)$，即首次命中位置在 $\{1, \dots, n - 1\}$ 上服从**离散均匀分布**；
  2. 给定首次命中 $\{X = m\}$：$P(Y = n \mid X = m) = p(1 - p)^{n - m - 1} \ (n \ge m + 1)$，表明剩余所需射击次数 $Y - m$ 仍服从几何分布（体现几何分布的**无记忆性**）。

</details>

---

## 2 二维随机变量的分布函数

### 2.1 联合分布函数的定义与性质

设 $(X, Y)$ 是二维随机变量，对任意实数 $x, y \in \mathbb{R}$，定义二元函数

$$
F(x, y) = P\{(X \le x) \cap (Y \le y)\} = P(X \le x, Y \le y) = P\{(X, Y) \in (-\infty, x] \times (-\infty, y]\}
$$

为二维随机变量 $(X, Y)$ 的**联合分布函数**（joint distribution function），几何上表示随机点 $(X, Y)$ 落在以 $(x, y)$ 为右上顶点的左下无穷矩形区域内的概率。

除满足有界性 $0 \le F(x, y) \le 1$ 外，任何联合分布函数 $F(x, y)$ 必满足以下四条基本性质：

| 性质名称 | 数学表达式 |
| :--- | :--- |
| **1. 单调不减性** | 关于 $x$ 和 $y$ 分别单调不减：$x_1 < x_2 \implies F(x_1, y) \le F(x_2, y)$；$y_1 < y_2 \implies F(x, y_1) \le F(x, y_2)$ |
| **2. 无穷处极限** | $F(+\infty, +\infty) = 1$；且对任意 $x, y$，有 $F(-\infty, y) = F(x, -\infty) = F(-\infty, -\infty) = 0$ |
| **3. 右连续性** | 关于 $x$ 和 $y$ 分别右连续：$\lim_{\epsilon \to 0^+} F(x + \epsilon, y) = F(x, y)$，$\lim_{\epsilon \to 0^+} F(x, y + \epsilon) = F(x, y)$ |
| **4. 矩形域非负性** | 对任意 $x_1 < x_2, \ y_1 < y_2$，有：<br>$P(x_1 < X \le x_2, y_1 < Y \le y_2) = F(x_2, y_2) - F(x_2, y_1) - F(x_1, y_2) + F(x_1, y_1) \ge 0$ |

对于二维离散型随机变量，联合分布律与联合分布函数的转换公式为：

$$
F(x, y) = \sum_{x_i \le x, \, y_j \le y} p_{ij}
$$

### 2.2 边际分布函数与条件分布函数

**1. 边际（边缘）分布函数（Marginal c.d.f.）**

二维随机变量 $(X, Y)$ 中各个分量的分布函数称为**边际分布函数**。由概率的连续性可知，一个分量的边际分布函数即为联合分布函数令另一个变量趋于 $+\infty$ 时的极限函数：

$$
F_X(x) = P(X \le x) = P(X \le x, Y < +\infty) = F(x, +\infty)
$$

$$
F_Y(y) = P(Y \le y) = P(X < +\infty, Y \le y) = F(+\infty, y)
$$

**2. 条件分布函数（Conditional c.d.f.）**

条件分布函数是关于目标变量的一元函数：

- **离散情形**：若 $P(Y = y) > 0$，则在 $\{Y = y\}$ 条件下 $X$ 的条件分布函数为：
  $$
  F_{X \mid Y}(x \mid y) = P(X \le x \mid Y = y) = \frac{P(X \le x, Y = y)}{P(Y = y)} = \sum_{x_k \le x} P(X = x_k \mid Y = y)
  $$
- **一般极限定义（含连续情形）**：若 $P(Y = y) = 0$，但对任意 $\epsilon > 0$ 有 $P(y < Y \le y + \epsilon) > 0$，则定义为右邻域极限：
  $$
  F_{X \mid Y}(x \mid y) = \lim_{\epsilon \to 0^+} P(X \le x \mid y < Y \le y + \epsilon) = \lim_{\epsilon \to 0^+} \frac{P(X \le x, y < Y \le y + \epsilon)}{P(y < Y \le y + \epsilon)}
  $$

<details markdown="1">
<summary>典型例题：二维离散分布律与分段分布函数的互推（Example 8 & 9）</summary>

**1. 由联合分布函数反推联合分布律（Example 9）**

设 $(X, Y)$ 的联合分布函数为：

$$
F(x, y) = \begin{cases}
0, & x < 0 \text{ 或 } y < 1, \\
0.1, & 0 \le x < 1 \text{ 且 } 1 \le y < 2, \\
0.3, & 0 \le x < 1 \text{ 且 } y \ge 2, \\
0.4, & x \ge 1 \text{ 且 } 1 \le y < 2, \\
1, & x \ge 1 \text{ 且 } y \ge 2.
\end{cases}
$$

**解**：观察分段边界可知，$X$ 的跳跃点为 $0, 1$，$Y$ 的跳跃点为 $1, 2$。利用二维矩形域增量公式计算各交点处的跳跃概率：

- $P(X = 0, Y = 1) = 0.1$
- $P(X = 0, Y = 2) = 0.3 - 0.1 = 0.2$
- $P(X = 1, Y = 1) = 0.4 - 0.1 = 0.3$
- $P(X = 1, Y = 2) = 1 - 0.3 - 0.4 + 0.1 = 0.4$

且令 $y \to +\infty$ 可直接读出 $X$ 的边际分布函数：$x < 0$ 时为 $0$，$0 \le x < 1$ 时为 $0.3$，$x \ge 1$ 时为 $1$。

</details>

---

## 3 二维连续型随机变量及其分布

### 3.1 联合概率密度函数的定义与性质

对于二维随机变量 $(X, Y)$ 的联合分布函数 $F(x, y)$，若存在非负可积函数 $f(x, y)$，使得对任意实数 $x, y \in \mathbb{R}$ 均有

$$
F(x, y) = \int_{-\infty}^x \int_{-\infty}^y f(u, v)\,du\,dv
$$

则称 $(X, Y)$ 为**二维连续型随机变量**，称 $f(x, y)$ 为 $(X, Y)$ 的**联合概率密度函数**（joint probability density function）。

联合概率密度函数 $f(x, y)$ 具有以下四条核心性质：

1. **非负性**：$f(x, y) \ge 0$。
2. **规范性（体积归一）**：曲面 $z = f(x, y)$ 与 $xOy$ 平面所夹空间区域的总体积恒为 $1$：
   $$
   \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x, y)\,dx\,dy = 1
   $$
3. **区域概率积分与零面积零概率**：点 $(X, Y)$ 落在平面区域 $G \subset \mathbb{R}^2$ 内的概率等于以 $G$ 为底、以 $z = f(x, y)$ 为顶的曲顶柱体体积：
   $$
   P((X, Y) \in G) = \iint_G f(x, y)\,dx\,dy
   $$
   由此可知，**二维连续型随机变量落在任意面积为零的平面区域（如单点或平面曲线 $Y = g(X)$）上的概率恒为零**。
4. **二阶混合偏导关系**：在 $f(x, y)$ 的**连续点** $(x, y)$ 处，有：
   $$
   \frac{\partial^2 F(x, y)}{\partial x \partial y} = f(x, y)
   $$

### 3.2 边际概率密度函数与条件概率密度函数

**1. 边际（边缘）概率密度函数（Marginal p.d.f.）**

设二维连续型随机变量 $(X, Y)$ 的联合概率密度为 $f(x, y)$，将其关于另一个变量在 $(-\infty, +\infty)$ 上积分，即得到 $X$ 与 $Y$ 各自的**边际概率密度函数**：

$$
f_X(x) = \int_{-\infty}^{+\infty} f(x, y)\,dy, \qquad f_Y(y) = \int_{-\infty}^{+\infty} f(x, y)\,dx
$$

**2. 条件概率密度函数（Conditional p.d.f.）**

对于固定的 $y$（满足 $f_Y(y) > 0$），在 $\{Y = y\}$ 条件下 $X$ 的**条件概率密度函数**定义为：

$$
f_{X \mid Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)}, \quad x \in \mathbb{R}
$$

同理，对于固定的 $x$（满足 $f_X(x) > 0$），在 $\{X = x\}$ 条件下 $Y$ 的**条件概率密度函数**定义为：

$$
f_{Y \mid X}(y \mid x) = \frac{f(x, y)}{f_X(x)}, \quad y \in \mathbb{R}
$$

联合分布、边际分布与条件分布三者之间的互推转化关系如下表所示：

| 转化方向 | 离散型随机变量公式 | 连续型随机变量公式 |
| :--- | :--- | :--- |
| **联合 $\to$ 边际**（对另一变量求和/积分） | $p_{i\cdot} = \displaystyle\sum_j p_{ij}, \quad p_{\cdot j} = \displaystyle\sum_i p_{ij}$ | $f_X(x) = \displaystyle\int_{-\infty}^{+\infty} f(x, y)\,dy, \quad f_Y(y) = \displaystyle\int_{-\infty}^{+\infty} f(x, y)\,dx$ |
| **联合 & 边际 $\to$ 条件**（作商） | $P(X = x_i \mid Y = y_j) = \dfrac{p_{ij}}{p_{\cdot j}}$ | $f_{X \mid Y}(x \mid y) = \dfrac{f(x, y)}{f_Y(y)}, \quad f_{Y \mid X}(y \mid x) = \dfrac{f(x, y)}{f_X(x)}$ |
| **边际 & 条件 $\to$ 联合**（乘法公式重构） | $p_{ij} = p_{i\cdot} P(Y = y_j \mid X = x_i)$ | $f(x, y) = f_X(x)f_{Y \mid X}(y \mid x) = f_Y(y)f_{X \mid Y}(x \mid y)$ |

!!! note "条件密度函数的核心性质与计算避坑指南"
    - **直观微元意义**：$f_{X \mid Y}(x \mid y)\Delta x \approx P(x < X \le x + \Delta x \mid y < Y \le y + \Delta y)$，它是关于自变量 $x$ 的一元密度函数，满足 $f_{X \mid Y}(x \mid y) \ge 0$ 且 $\int_{-\infty}^{+\infty} f_{X \mid Y}(x \mid y)\,dx = 1$。
    - **条件分布函数与条件区间概率**：
      $$
      F_{X \mid Y}(x \mid y) = \int_{-\infty}^x f_{X \mid Y}(u \mid y)\,du, \qquad P(a < X < b \mid Y = y) = \int_a^b f_{X \mid Y}(x \mid y)\,dx
      $$
    - **【高频易错警告】**：当条件为单点 $\{Y = y_0\}$ 时，由于连续型变量 $P(Y = y_0) = 0$，**严禁将 $P(X \le a \mid Y = y_0)$ 写成 $\frac{P(X \le a, Y = y_0)}{P(Y = y_0)}$**！必须先求出条件密度 $f_{X \mid Y}(x \mid y_0)$，再对 $x$ 积分求解。而当条件为正概率区间 $\{Y > y_0\}$ 时，才使用初等条件概率公式 $P(X \le a \mid Y > y_0) = \frac{P(X \le a, Y > y_0)}{P(Y > y_0)}$。

<details markdown="1">
<summary>典型例题：非矩形域边际积分上下限与条件密度重构（Example 11, 12, 14）</summary>

**1. 抛物线与直线围成区域的积分上下限确定（Example 11 & 12）**

设 $(X, Y)$ 的联合概率密度为 $f(x, y) = cy \ (0 < x < 1, \ x^2 < y < x)$，其余为 $0$。

- **求常数 $c$**：$\int_0^1 dx \int_{x^2}^x cy\,dy = \frac{c}{15} = 1 \implies c = 15$。
- **求边际概率密度 $f_X(x)$ 与 $f_Y(y)$**（核心是画图确定非零积分区间）：
  1. 当 $0 < x < 1$ 时，$y$ 从下界 $x^2$ 积分到上界 $x$：
     $$
     f_X(x) = \int_{x^2}^x 15y\,dy = \frac{15}{2}(x^2 - x^4), \quad 0 < x < 1
     $$
  2. 当 $0 < y < 1$ 时，反解不等式 $x^2 < y < x$ 得 $x$ 从左界 $y$ 积分到右界 $\sqrt{y}$：
     $$
     f_Y(y) = \int_y^{\sqrt{y}} 15y\,dx = 15\left(y^{\frac{3}{2}} - y^2\right), \quad 0 < y < 1
     $$

---

**2. 两人接力工作模型——由边际与条件反求另一方向条件密度（Example 14）**

甲乙接力完成工作，总限时 30 分钟。甲工作时间 $X \sim U(0, 30)$；给定 $\{X = x\} \ (0 < x < 30)$ 下，两人总用时 $Y$ 服从 $U(x, 30)$。

- **求联合密度与 $f_{X \mid Y}(x \mid y)$**：
  由 $f_X(x) = \frac{1}{30} \ (0 < x < 30)$ 及 $f_{Y \mid X}(y \mid x) = \frac{1}{30 - x} \ (x < y < 30)$，相乘得联合密度：
  $$
  f(x, y) = f_X(x)f_{Y \mid X}(y \mid x) = \frac{1}{30(30 - x)}, \quad 0 < x < y < 30
  $$
  先积分求 $Y$ 的边际密度（对固定的 $0 < y < 30$，$x$ 的积分范围为 $0 < x < y$）：
  $$
  f_Y(y) = \int_0^y \frac{1}{30(30 - x)}\,dx = \frac{1}{30}\ln\frac{30}{30 - y}, \quad 0 < y < 30
  $$
  从而在 $\{Y = y\} \ (0 < y < 30)$ 条件下，$X$ 的条件概率密度为：
  $$
  f_{X \mid Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)} = \frac{1}{(30 - x)\ln\frac{30}{30 - y}}, \quad 0 < x < y
  $$
- **已知两人共花 25 分钟，求甲工作不超过 10 分钟的概率**：
  $$
  P(X \le 10 \mid Y = 25) = \int_0^{10} f_{X \mid Y}(x \mid 25)\,dx = \int_0^{10} \frac{1}{(30 - x)\ln 6}\,dx = \frac{\ln 30 - \ln 20}{\ln 6} \approx 0.2263
  $$

</details>

### 3.3 两个重要的二维连续型分布

#### 3.3.1 二维均匀分布（Bivariate Uniform Distribution）

设二维随机变量 $(X, Y)$ 在平面有界区域 $D$ 上取值，若其联合概率密度函数为

$$
f(x, y) = \begin{cases}
\dfrac{1}{D \text{ 的面积}}, & (x, y) \in D, \\
0, & \text{其他},
\end{cases}
$$

则称 $(X, Y)$ 服从区域 $D$ 上的**二维均匀分布**。二维均匀分布具有平面**几何等可能性**：对任意子区域 $D_1 \subset D$，有 $P((X, Y) \in D_1) = \frac{D_1 \text{ 的面积}}{D \text{ 的面积}}$。

!!! note "二维均匀分布的边际分布 vs. 条件分布特征（Example 15）"
    - **边际分布不一定服从均匀分布**：若区域 $D$ 不是边平行于坐标轴的矩形（例如三角形区域 $D = \{(x, y) : |y| < x < 1\}$，面积为 $1$），其边际密度 $f_Y(y) = \int_{|y|}^1 1\,dx = 1 - |y| \ (-1 < y < 1)$ **不再是均匀分布**。
    - **条件分布仍然服从一维均匀分布**：在给定 $\{Y = y\}$ 截面上，$f_{X \mid Y}(x \mid y) = \frac{1}{1 - |y|} \ (|y|< x < 1)$，即条件分布恒为截面线段 $(|y|, 1)$ 上的**一维均匀分布** $U(|y|, 1)$！

#### 3.3.2 二维正态分布（Bivariate Normal Distribution）

设二维随机变量 $(X, Y)$ 的联合概率密度函数为

$$
f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} \exp\left\{-\frac{1}{2(1 - \rho^2)}\left[\frac{(x - \mu_1)^2}{\sigma_1^2} - 2\rho\frac{(x - \mu_1)(y - \mu_2)}{\sigma_1\sigma_2} + \frac{(y - \mu_2)^2}{\sigma_2^2}\right]\right\}, \quad x, y \in \mathbb{R}
$$

其中 $\mu_1, \mu_2 \in \mathbb{R}$，$\sigma_1, \sigma_2 > 0$，$-1 < \rho < 1$（定义中允许 $-1 \le \rho \le 1$），则称 $(X, Y)$ 服从参数为 $(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2; \rho)$ 的**二维（元）正态分布**，记作 $(X, Y) \sim N(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2; \rho)$。

二维正态分布的**边际分布与条件分布**全部保持正态性，具体参数汇总如下表（必背核心结论）：

| 分布类型 | 符号记法 | 服从的正态分布及参数 | 核心特征说明 |
| :--- | :--- | :--- | :--- |
| **$X$ 的边际分布** | $f_X(x)$ | $X \sim N(\mu_1, \sigma_1^2)$ | **与相关参数 $\rho$ 完全无关** |
| **$Y$ 的边际分布** | $f_Y(y)$ | $Y \sim N(\mu_2, \sigma_2^2)$ | **与相关参数 $\rho$ 完全无关** |
| **给定 $\{X = x\}$ 下 $Y$ 的条件分布** | $f_{Y \mid X}(y \mid x)$ | $N\left(\mu_2 + \rho\dfrac{\sigma_2}{\sigma_1}(x - \mu_1), \ (1 - \rho^2)\sigma_2^2\right)$ | 条件均值关于 $x$ 线性变化，条件方差缩减为 $(1-\rho^2)\sigma_2^2$ |
| **给定 $\{Y = y\}$ 下 $X$ 的条件分布** | $f_{X \mid Y}(x \mid y)$ | $N\left(\mu_1 + \rho\dfrac{\sigma_1}{\sigma_2}(y - \mu_2), \ (1 - \rho^2)\sigma_1^2\right)$ | 条件均值关于 $y$ 线性变化，条件方差缩减为 $(1-\rho^2)\sigma_1^2$ |

<details markdown="1">
<summary>点击展开：二维正态分布边际密度与条件密度的配方推导（Example 16）</summary>

将二维正态联合密度指数括号内的二次型关于变量 $y$ 进行配方：

$$
\frac{(x - \mu_1)^2}{\sigma_1^2} - 2\rho\frac{(x - \mu_1)(y - \mu_2)}{\sigma_1\sigma_2} + \frac{(y - \mu_2)^2}{\sigma_2^2} = (1 - \rho^2)\frac{(x - \mu_1)^2}{\sigma_1^2} + \left[\frac{y - \mu_2}{\sigma_2} - \rho\frac{x - \mu_1}{\sigma_1}\right]^2
$$

因此，联合密度函数可直接拆分为两项的乘积：

$$
f(x, y) = \underbrace{\frac{1}{\sqrt{2\pi}\sigma_1} e^{-\frac{(x - \mu_1)^2}{2\sigma_1^2}}}_{f_X(x)} \cdot \underbrace{\frac{1}{\sqrt{2\pi}\sigma_2\sqrt{1 - \rho^2}} \exp\left\{-\frac{\left\{y - \left[\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1)\right]\right\}^2}{2\sigma_2^2(1 - \rho^2)}\right\}}_{f_{Y \mid X}(y \mid x)}
$$

对 $y \in (-\infty, +\infty)$ 积分时，右侧第二项恰为正态分布 $N\left(\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1), \ (1 - \rho^2)\sigma_2^2\right)$ 的密度函数，其全积分为 $1$。从而立即同时证得 $f_X(x)$ 为 $N(\mu_1, \sigma_1^2)$ 的密度，且商值 $f_{Y \mid X}(y \mid x) = \frac{f(x, y)}{f_X(x)}$ 即为上述第二项。

</details>

---

## 4 随机变量的独立性与多维推广

### 4.1 二维随机变量的独立性及充要条件

设 $(X, Y)$ 的联合分布函数为 $F(x, y)$，边际分布函数为 $F_X(x)$ 与 $F_Y(y)$。若对**任意** $x, y \in \mathbb{R}$，均有

$$
P(X \le x, Y \le y) = P(X \le x)P(Y \le y) \iff F(x, y) = F_X(x)F_Y(y)
$$

则称随机变量 $X$ 与 $Y$ **相互独立**。

针对离散型与连续型随机变量，独立性具有如下等价判别准则：

| 随机变量类型 | 相互独立的充要条件 | 判别实战要点 |
| :--- | :--- | :--- |
| **二维离散型 $(X, Y)$** | $p_{ij} = p_{i\cdot} \cdot p_{\cdot j}$ 对**一切** $i, j$ 均成立 | 只要找到一对 $(i, j)$ 使得 $p_{ij} \neq p_{i\cdot}p_{\cdot j}$（例如某格概率为 $0$ 但行和、列和均非零），即可直接判定**不独立** |
| **二维连续型 $(X, Y)$** | $f(x, y) = f_X(x)f_Y(y)$ 几乎处处成立 | 除去面积为零的集合（如不连续边界点）外处处相等 |
| **连续型变量分离判据（定理 1）** | $f(x, y) = m(x) \cdot n(y), \quad \forall x, y \in \mathbb{R}$ | 需同时满足：① 非零支撑区域 $D$ 必须是**边平行于坐标轴的矩形区域**（$x, y$ 上下界互不牵制）；② 在 $D$ 内代数式可分离为纯 $x$ 函数与纯 $y$ 函数之积 |
| **二维正态分布（Example 21）** | **$\rho = 0$** | 对 $(X, Y) \sim N(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2; \rho)$，$X$ 与 $Y$ 独立 $\iff \rho = 0$ |

<details markdown="1">
<summary>点击展开：定理 1（变量分离判据）的四个思考题辨析与二维正态独立性证明</summary>

**1. 思考题：判断下列联合密度对应的 $X, Y$ 是否相互独立（Slide 76）**

1. $f(x, y) = e^{-2x} \ (x > 0, \ 0 < y < 2)$，其它为 $0$：**独立**（支撑为矩形 $(0, +\infty) \times (0, 2)$，且表达式 $e^{-2x} \cdot 1$ 可分离）。
2. $f(x, y) = xy/2 \ (0 < x < y < 2)$，其它为 $0$：**不独立**（虽然表达式 $xy/2$ 看似可分离，但支撑域 $0 < x < y < 2$ 为三角形区域，变量范围互相牵制，在全平面 $\mathbb{R}^2$ 上指示函数 $\mathbb{I}_{\{0<x<y<2\}}$ 无法拆为 $m(x)n(y)$）。
3. $f(x, y) = x + y \ (0 < x < 1, \ 0 < y < 1)$，其它为 $0$：**不独立**（支撑是矩形，但 $x + y$ 在矩形内无法拆为乘积 $m(x)n(y)$）。
4. $f(x, y) = xy \ (0 < x < 2, \ 0 < y < 1)$，其它为 $0$：**独立**（支撑为矩形 $(0, 2) \times (0, 1)$，且 $xy$ 可分离）。

---

**2. 二维正态分布 $X, Y$ 独立 $\iff \rho = 0$ 的证明（Example 21）**

- **充分性（$\Leftarrow$）**：若 $\rho = 0$，代入二维正态密度公式，交叉项消失且 $\sqrt{1-\rho^2} = 1$，对一切 $x, y \in \mathbb{R}$ 恒有 $f(x, y) = f_X(x)f_Y(y)$，故 $X, Y$ 独立。
- **必要性（$\Rightarrow$）**：若 $X, Y$ 独立，因 $f(x, y), f_X(x), f_Y(y)$ 均为全平面上的连续函数，故处处有 $f(x, y) = f_X(x)f_Y(y)$。特别地，取中心点 $(x, y) = (\mu_1, \mu_2)$ 代入得：
  $$
  f(\mu_1, \mu_2) = f_X(\mu_1)f_Y(\mu_2) \implies \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} = \frac{1}{2\pi\sigma_1\sigma_2} \implies \rho = 0
  $$

</details>

### 4.2 $n$ 维随机变量及其独立性重要定理

将二维概念推广至 $n$ 维随机向量 $(X_1, X_2, \dots, X_n)$，其联合分布函数为 $F(x_1, \dots, x_n) = P(X_1 \le x_1, \dots, X_n \le x_n)$。将不要的分量趋于 $+\infty$（或对不要的变量在 $(-\infty, +\infty)$ 上求多重积分/多重求和），即可得到任意 $k \ (1 \le k < n)$ 维边际分布。

若对任意 $x_1, \dots, x_n \in \mathbb{R}$ 均有 $F(x_1, \dots, x_n) = \prod_{i=1}^n F_{X_i}(x_i)$，则称 $X_1, \dots, X_n$ **相互独立**。若两个随机向量满足 $F(x_1, \dots, x_m, y_1, \dots, y_n) = F_1(x_1, \dots, x_m)F_2(y_1, \dots, y_n)$，则称随机向量 $(X_1, \dots, X_m)$ 与 $(Y_1, \dots, Y_n)$ **相互独立**。

!!! tip "关于随机变量独立性的三大高频定理（Theorems 2 & 3）"
    1. **子分量独立性（定理 2）**：若随机向量 $(X_1, \dots, X_m)$ 与 $(Y_1, \dots, Y_n)$ 相互独立，则其中任意分量 $X_i \ (1 \le i \le m)$ 与 $Y_j \ (1 \le j \le n)$ 必相互独立。
    2. **连续函数变换保持独立性（定理 3）**：若 $(X_1, \dots, X_m)$ 与 $(Y_1, \dots, Y_n)$ 相互独立，且 $h(x_1, \dots, x_m)$ 与 $g(y_1, \dots, y_n)$ 为连续函数，则重组后的随机变量 $h(X_1, \dots, X_m)$ 与 $g(Y_1, \dots, Y_n)$ 依然**相互独立**（特别地，若 $X, Y$ 独立，则 $f(X)$ 与 $g(Y)$ 必独立）。
    3. **常数与事件独立性**：任意常数 $C$ 与任意随机变量 $X$ 均相互独立；若 $X, Y$ 相互独立，则事件 $\{X \in A\}$ 与 $\{Y \in B\}$ 必相互独立。

---

## 5 多维随机变量函数的分布

### 5.1 离散型多维随机变量函数的分布

设二维离散型随机变量 $(X, Y)$ 的联合分布律为 $P(X = x_i, Y = y_j) = p_{ij}$。求一维函数 $Z = g(X, Y)$ 或二维函数 $U = u(X, Y), \ V = v(X, Y)$ 的分布律，只需先列出新变量的所有可能取值，再找出等价事件并将落入该等价域的所有 $p_{ij}$ 相加即可。

### 5.2 和的分布 $Z = X + Y$ 与卷积公式

**1. 离散型和的分布与可加性**

设二维离散型随机变量 $(X, Y)$ 的联合分布律为 $p_{ij}$，则 $Z = X + Y$ 的分布律为：

$$
P(Z = z_k) = \sum_{i=1}^{+\infty} P(X = x_i, Y = z_k - x_i) \xlongequal{\text{当 } X, Y \text{ 独立时}} \sum_{i=1}^{+\infty} P(X = x_i) P(Y = z_k - x_i)
$$

**2. 连续型和的分布与卷积公式（Convolution Formula）**

设二维连续型随机变量 $(X, Y)$ 的联合概率密度为 $f(x, y)$，通过分布函数法 $F_Z(z) = \iint_{x+y \le z} f(x, y)\,dx\,dy$ 作换元 $u = x + y$，可得 $Z = X + Y$ 的**一般概率密度公式**：

$$
f_Z(z) = \int_{-\infty}^{+\infty} f(x, z - x)\,dx = \int_{-\infty}^{+\infty} f(z - y, y)\,dy
$$

特别地，当 $X$ 与 $Y$ **相互独立**时，有 $f(x, y) = f_X(x)f_Y(y)$，上式化为著名的**卷积公式**（记作 $f_X * f_Y$）：

$$
f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{+\infty} f_X(x)f_Y(z - x)\,dx = \int_{-\infty}^{+\infty} f_X(z - y)f_Y(y)\,dy
$$

**3. 重要分布的可加性（再生性）汇总**

利用离散卷积与连续卷积公式，可导出独立随机变量求和的重要可加性结论：

| 分布名称 | 独立条件与参数设定 | 和的分布（可加性结论） | 线性组合推广 |
| :--- | :--- | :--- | :--- |
| **泊松分布** | $X \sim P(\lambda_1), \ Y \sim P(\lambda_2)$，且 $X, Y$ 独立 | $X + Y \sim P(\lambda_1 + \lambda_2)$ | $\sum_{i=1}^n X_i \sim P\left(\sum_{i=1}^n \lambda_i\right)$ |
| **二项分布** | $X \sim B(n_1, p), \ Y \sim B(n_2, p)$，且 $X, Y$ 独立（同参数 $p$） | $X + Y \sim B(n_1 + n_2, p)$ | 需保证成功概率 $p$ 相同 |
| **正态分布** | $X \sim N(\mu_1, \sigma_1^2), \ Y \sim N(\mu_2, \sigma_2^2)$，且 $X, Y$ 独立 | $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ | $aX + bY + c \sim N(a\mu_1 + b\mu_2 + c, \ a^2\sigma_1^2 + b^2\sigma_2^2)$ |

<details markdown="1">
<summary>点击展开：泊松可加性证明、正态卷积证明与三类和分布典型例题（Example 25 ~ 29）</summary>

**1. 泊松分布可加性证明（Example 25）**

设 $X \sim P(\lambda_1), \ Y \sim P(\lambda_2)$ 相互独立，对任意非负整数 $k = 0, 1, \dots$，利用二项式定理逆向合并：

$$
P(X + Y = k) = \sum_{i=0}^k P(X = i)P(Y = k - i) = e^{-(\lambda_1 + \lambda_2)} \sum_{i=0}^k \frac{\lambda_1^i \lambda_2^{k - i}}{i!(k - i)!} = \frac{e^{-(\lambda_1 + \lambda_2)}}{k!} \sum_{i=0}^k C_k^i \lambda_1^i \lambda_2^{k - i} = \frac{(\lambda_1 + \lambda_2)^k}{k!} e^{-(\lambda_1 + \lambda_2)}
$$

故 $Z = X + Y \sim P(\lambda_1 + \lambda_2)$。

---

**2. 独立标准正态变量卷积证明（Example 26）**

设 $X, Y \sim N(0, 1)$ 相互独立，由卷积公式并配完全平方（令 $t = x - z/2$，利用高斯积分 $\int_{-\infty}^{+\infty} e^{-t^2}\,dt = \sqrt{\pi}$）：

$$
f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-\frac{x^2}{2}} e^{-\frac{(z - x)^2}{2}}\,dx = \frac{1}{2\pi} e^{-\frac{z^2}{4}} \int_{-\infty}^{+\infty} e^{-\left(x - \frac{z}{2}\right)^2}\,dx = \frac{1}{2\pi} e^{-\frac{z^2}{4}} \cdot \sqrt{\pi} = \frac{1}{\sqrt{2\pi}(\sqrt{2})} e^{-\frac{z^2}{2(\sqrt{2})^2}}
$$

故 $Z = X + Y \sim N(0, 2)$。

---

**3. 独立均匀分布之和——三角分布分段积分限确定（Example 27）**

设 $X, Y$ 独立同分布于 $U[0, 1]$，求 $Z = X + Y$ 的密度函数。在卷积积分 $\int_{-\infty}^{+\infty} f_X(x)f_Y(z - x)\,dx$ 中，被积函数非零当且仅当：

$$
\begin{cases}
0 \le x \le 1 \\
0 \le z - x \le 1
\end{cases} \iff
\begin{cases}
0 \le x \le 1 \\
z - 1 \le x \le z
\end{cases} \iff \max(0, z - 1) \le x \le \min(1, z)
$$

故需对 $z$ 分段讨论积分上下限：

$$
f_Z(z) = \begin{cases}
\displaystyle\int_0^z 1\,dx = z, & 0 < z < 1, \\
\displaystyle\int_{z - 1}^1 1\,dx = 2 - z, & 1 \le z < 2, \\
0, & \text{其他}.
\end{cases}
$$

---

**4. 非独立二维连续型变量求和（Example 28）**

设 $(X, Y)$ 联合密度为 $f(x, y) = 3x \ (0 < y < x < 1)$，其余为 $0$，求 $Z = X + Y$ 的密度。
注意此处 **$X$ 与 $Y$ 不独立，严禁套用乘积卷积公式**，必须使用一般公式 $f_Z(z) = \int_{-\infty}^{+\infty} f(x, z - x)\,dx$。
将 $y = z - x$ 代入区域不等式 $0 < y < x < 1$，得：

$$
0 < z - x < x < 1 \iff \frac{z}{2} < x < \min(z, 1)
$$

分段积分可得：

$$
f_Z(z) = \begin{cases}
\displaystyle\int_{z/2}^z 3x\,dx = \frac{9}{8}z^2, & 0 < z < 1, \\
\displaystyle\int_{z/2}^1 3x\,dx = \frac{3}{2}\left(1 - \frac{z^2}{4}\right), & 1 \le z < 2, \\
0, & \text{其他}.
\end{cases}
$$

---

**5. 离散型随机变量与连续型随机变量独立求和（Example 29）**

一份工作酬金 $X$ 在 $\{10, 20, 30\}$ 上等可能取值（各为 $1/3$），另一份酬金 $Y \sim N(15, 4)$，且 $X, Y$ 独立，求总酬金 $Z = X + Y$ 的密度函数。

**解**：遇到“离散 + 连续”求和，标准通法是**对离散变量使用全概率公式展开分布函数 $F_Z(z)$**：

$$
F_Z(z) = P(X + Y \le z) = \sum_{i=1}^3 P(X = 10i) P(Y \le z - 10i \mid X = 10i) = \frac{1}{3}\left[F_Y(z - 10) + F_Y(z - 20) + F_Y(z - 30)\right]
$$

两边关于 $z$ 求导即得 $Z$ 的概率密度函数：

$$
f_Z(z) = F_Z'(z) = \frac{1}{3}\left[f_Y(z - 10) + f_Y(z - 20) + f_Y(z - 30)\right] = \frac{1}{6\sqrt{2\pi}}\left[e^{-\frac{(z - 25)^2}{8}} + e^{-\frac{(z - 35)^2}{8}} + e^{-\frac{(z - 45)^2}{8}}\right]
$$

</details>

### 5.3 极值分布（最大值与最小值）与混合分布

设 $X_1, X_2, \dots, X_n$ 是 $n$ 个**相互独立**的随机变量，其分布函数分别为 $F_{X_i}(x_i) \ (i = 1, \dots, n)$。记最大值 $M = \max_{1 \le i \le n} X_i$，最小值 $N = \min_{1 \le i \le n} X_i$。

求解极值分布的核心等价关系为：**“最大值 $\le z$”等价于“所有分量均 $\le z$”**；**“最小值 $> z$”等价于“所有分量均 $> z$”**（这两步等价转化本身无需独立性，展开为乘积时才用到独立性）：

| 极值统计量 | 核心等价事件转化 | 一般独立情形分布函数 | 独立同分布（i.i.d.，$F_{X_i} = F$）分布函数与密度 |
| :--- | :--- | :--- | :--- |
| **最大值 $M = \max X_i$** | $\{M \le z\} \iff \bigcap_{i=1}^n \{X_i \le z\}$ | $F_{\max}(z) = \displaystyle\prod_{i=1}^n F_{X_i}(z)$ | $F_{\max}(z) = [F(z)]^n$<br>$f_{\max}(z) = n[F(z)]^{n-1}f(z)$ |
| **最小值 $N = \min X_i$** | $\{N > z\} \iff \bigcap_{i=1}^n \{X_i > z\}$ | $F_{\min}(z) = 1 - \displaystyle\prod_{i=1}^n [1 - F_{X_i}(z)]$ | $F_{\min}(z) = 1 - [1 - F(z)]^n$<br>$f_{\min}(z) = n[1 - F(z)]^{n-1}f(z)$ |

<details markdown="1">
<summary>典型例题：串联/并联/备用系统寿命分布与随机选择混合分布（Example 31 & 32）</summary>

**1. 串联、并联与冷备用系统的寿命分布对比（Example 31）**

系统 $L$ 由两个独立子系统 $L_1, L_2$ 构成，寿命分别为 $X \sim E(\alpha)$ 与 $Y \sim E(\beta) \ (\alpha, \beta > 0, \ \alpha \neq \beta)$，写出三种联结方式下系统总寿命 $Z$ 的概率密度（当 $z > 0$ 时）：

1. **串联系统**（任一损坏即停机，$Z = \min(X, Y)$）：
   $$
   F_Z(z) = 1 - [1 - F_X(z)][1 - F_Y(z)] = 1 - e^{-(\alpha + \beta)z} \implies f_Z(z) = (\alpha + \beta)e^{-(\alpha + \beta)z} \quad (\text{即 } Z \sim E(\alpha + \beta))
   $$
2. **并联系统**（两者均损坏才停机，$Z = \max(X, Y)$）：
   $$
   F_Z(z) = F_X(z)F_Y(z) = (1 - e^{-\alpha z})(1 - e^{-\beta z}) \implies f_Z(z) = \alpha e^{-\alpha z} + \beta e^{-\beta z} - (\alpha + \beta)e^{-(\alpha + \beta)z}
   $$
3. **备用系统**（$L_1$ 损坏瞬间 $L_2$ 才启动，$Z = X + Y$，套用卷积公式）：
   $$
   f_Z(z) = \int_0^z \alpha e^{-\alpha(z - y)} \beta e^{-\beta y}\,dy = \frac{\alpha\beta}{\beta - \alpha}\left(e^{-\alpha z} - e^{-\beta z}\right)
   $$

---

**2. 伯努利切换开关构造的混合分布（Example 32）**

设 $Z = AX + (1 - A)Y$，其中 $A \sim B(1, p)$，且 $A, X, Y$ 相互独立。

- **求 $F_Z(z)$**：按 $A = 1$ 与 $A = 0$ 作全概率展开，并利用独立性：
  $$
  F_Z(z) = P(A = 1)P(X \le z \mid A = 1) + P(A = 0)P(Y \le z \mid A = 0) = p F_X(z) + (1 - p) F_Y(z)
  $$
- **类型判别**：当 $p = 1/2$、退化分布 $P(X = 2) = 1$、均匀分布 $Y \sim U(0, 1)$ 时：
  $$
  F_Z(z) = \frac{1}{2}F_X(z) + \frac{1}{2}F_Y(z) = \begin{cases}
  0, & z < 0, \\
  z/2, & 0 \le z < 1, \\
  1/2, & 1 \le z < 2, \\
  1, & z \ge 2.
  \end{cases}
  $$
  由于 $F_Z(z)$ 在 $[0, 1)$ 上连续递增，而在 $z = 2$ 处有高度为 $1/2$ 的跳跃，故 $Z$ **既不是离散型也不是连续型随机变量**（属于混合型随机变量）。

</details>