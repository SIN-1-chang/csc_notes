# 随机变量及其分布

!!! abstract
    概率论与数理统计 | 第二章课堂笔记
    
    参考：
    
    - 《概率论与数理统计（第二版）》，高等教育出版社，2023 — Chapter 2: Random Variables and Distributions
    - 浙江大学数学科学学院《概率论和数理统计》课程讲义（黄炜）

## 1 随机变量

设随机试验样本空间为 $S$，定义在 $S$ 上的**实值单值函数** $X = X(e)$ 称为**随机变量**（r.v.）。随机事件可表示为实数区间 $A = \{e : X(e) \in I\} = \{X \in I\}$。由单值性可知，不同取值对应的事件必互斥：

$$\forall i \neq j, \quad \{X = i\} \cap \{X = j\} = \emptyset$$

---

## 2 离散型随机变量及其分布

### 2.1 概率分布律

取值至多可列（有限或可列无穷）的随机变量称为**离散型随机变量**。设其可能取值为 $x_1, x_2, \dots$，则称

$$P(X = x_k) = p_k, \quad k = 1, 2, \dots$$

为 $X$ 的**概率分布律**（p.m.f.）。集合 $\{x : P(X = x) > 0\}$ 称为 $X$ 的**支撑**（support）。分布律充要地满足两条基本性质：

```text
1. 非负性    p_k >= 0,  k = 1, 2, ...
2. 规范性    sum_{k=1}^{infty} p_k = 1
```

### 2.2 六大常见离散型分布


| 分布名称与记号 | 试验物理模型 | 概率分布律 $P(X=k)$ | 取值范围 $k$ |
| --- | --- | --- | --- |
| 0-1 分布 $B(1,p)$ | 单次 Bernoulli 试验 | $p^k(1-p)^{1-k}$ | $k=0,\ 1$ |
| 二项分布 $B(n,p)$ | $n$ 重独立试验成功次数 | $C_n^k p^k(1-p)^{n-k}$ | $k=0,\ 1,\ \dots,\ n$ |
| 泊松分布 $P(\lambda)$ | 单位时间稀有事件计数 | $\dfrac{\lambda^k}{k!}\,e^{-\lambda}$ | $k=0,\ 1,\ 2,\ \dots$ |
| 几何分布 $\mathrm{Geom}(p)$ | 首次成功时的试验次数 | $(1-p)^{k-1}p$ | $k=1,\ 2,\ \dots$ |
| 帕斯卡分布（负二项）$NB(r,p)$ | 第 $r$ 次成功时试验次数 | $C_{k-1}^{r-1}p^{r}(1-p)^{k-r}$ | $k=r,\ r+1,\ \dots$ |
| 超几何分布$H(n,a,N)$ | $N$ 中不放回取 $n$ 个成功数 | $\dfrac{C_a^k C_b^{n-k}}{C_N^n}$ | $\max(0,\,n-b)\le k\le \min(a,\,n)$ |



**二项分布的泊松近似**：当 $X \sim B(n, p)$ 满足 $n > 10, \ p < 0.1$ 时，取 $\lambda = np$，有：

$$C_n^k p^k (1 - p)^{n - k} \approx \frac{e^{-\lambda}\lambda^k}{k!}$$

<details markdown="1">
<summary>点击展开：泊松近似证明与典型例题（Example 6, 9 & 五种摸球对比）</summary>

**1. 泊松近似证明**

令 $\lambda = np$，当 $n \to \infty$ 时，由 $\frac{n(n-1)\cdots(n-k+1)}{n^k} \to 1$、$(1 - \frac{\lambda}{n})^{-k} \to 1$ 及 $(1 - \frac{\lambda}{n})^n \to e^{-\lambda}$，直接化简 $C_n^k (\frac{\lambda}{n})^k (1 - \frac{\lambda}{n})^{n-k}$ 即得 $\frac{e^{-\lambda}\lambda^k}{k!}$。

---

**2. 二次抽样验收方案（Example 6）**

次品率为 $p$。首检取 $X \sim B(10, p)$：若 $X = 0$ 接收，$X > 2$ 拒收；若 $1 \le X \le 2$ 则复检取 $Y \sim B(5, p)$（$X, Y$ 独立），仅当 $Y = 0$ 时接收。接收概率为：

$$P(A) = P(X = 0) + P(1 \le X \le 2)P(Y = 0) = (1-p)^{10} + \left[10p(1-p)^9 + 45p^2(1-p)^8\right](1-p)^5$$

---

**3. 泊松分布嵌套二项分布（Example 9）**

单位时间候车人数 $X \sim P(4.8)$。单次观察至少 3 人的概率 $p = P(X \ge 3) = 1 - \sum_{k=0}^2 \frac{4.8^k}{k!}e^{-4.8} \approx 0.8580$。独立观察 5 个单位时间，恰有 4 个满足条件的概率为 $Y \sim B(5, p) \implies P(Y = 4) = C_5^4 p^4(1-p) \approx 0.7696$。

---

**4. 盒中 2 红 4 白（$p = 1/3$）的五种抽样分布对比**

- 任取 1 球，红球数 $X \sim B(1, 1/3)$
- 不放回取 3 球，红球数 $Y$ 服从超几何分布：$P(Y = k) = \frac{C_2^k C_4^{3-k}}{C_6^3} \ (k = 0, 1, 2)$
- 有放回取 3 球，红球数 $Z \sim B(3, 1/3)$
- 有放回取至出红球，次数 $U \sim Geom(1/3)$：$P(U = k) = \frac{2^{k-1}}{3^k} \ (k \ge 1)$
- 有放回取至出 3 次红球，次数 $V$ 服从帕斯卡分布：$P(V = k) = C_{k-1}^2 \frac{2^{k-3}}{3^k} \ (k \ge 3)$

</details>

---

## 3 概率分布函数

对任意随机变量 $X$，定义其**分布函数**（c.d.f.）为：

$$F(x) = P(X \le x), \quad \forall x \in \mathbb{R}$$

任何分布函数充要地满足以下**三条基本性质**：

```markdown
1. 单调不减性      若 x_1 < x_2，则 F(x_1) <= F(x_2)
2. 无穷处极限      F(-infty) = lim_{x -> -infty} F(x) = 0，F(+infty) = lim_{x -> +infty} F(x) = 1
3. 右连续性        在任意点 x in R 处恒有 F(x + 0) = F(x)
```

利用 $F(x)$ 及其左极限 $F(x - 0) = P(X < x)$ 计算单点与区间概率：

$$P(X = x_0) = F(x_0) - F(x_0 - 0)$$

$$\begin{aligned} P(a < X \le b) &= F(b) - F(a), & P(a < X < b) &= F(b - 0) - F(a) \\ P(a \le X \le b) &= F(b) - F(a - 0), & P(a \le X < b) &= F(b - 0) - F(a - 0) \end{aligned}$$

离散型随机变量的分布函数为**阶梯函数** $F(x) = \sum_{x_k \le x} p_k$，在取值点 $x_k$ 处的跳跃度即为 $p_k = P(X = x_k)$。

---

## 4 连续型随机变量及其分布

### 4.1 概率密度函数的定义与性质

若存在非负函数 $f(x)$ 使得对任意 $x \in \mathbb{R}$ 均有

$$F(x) = \int_{-\infty}^x f(t)\,dt$$

则称 $X$ 为**连续型随机变量**，$f(x)$ 为其**概率密度函数**（p.d.f.）。密度函数核心性质如下：

1. **充要性质**：$f(x) \ge 0$ 且 $\int_{-\infty}^{+\infty} f(x)\,dx = 1$（注：$f(x)$ 的值可大于 $1$）。
2. **单点零概率与区间积分**：$\forall a \in \mathbb{R}, \ P(X = a) = 0$；端点开闭不影响区间概率 $P(X \in I) = \int_I f(x)\,dx$。
3. **导数与微元意义**：在 $f(x)$ 的连续点处有 $F'(x) = f(x)$，且当 $\Delta x \to 0^+$ 时 $P(x < X \le x + \Delta x) \approx f(x)\Delta x$。

### 4.2 三个重要的连续型分布

#### 4.2.1 均匀分布 $X \sim U(a, b)$

$$f(x) = \begin{cases} \dfrac{1}{b - a}, & a < x < b, \\ 0, & \text{其他}, \end{cases} \qquad F(x) = \begin{cases} 0, & x < a, \\ \dfrac{x - a}{b - a}, & a \le x < b, \\ 1, & x \ge b. \end{cases}$$

具有区间**等可能性**：落入子区间 $(c, c+s) \subset (a, b)$ 的概率 $P(c < X < c+s) = \frac{s}{b-a}$ 仅与长度 $s$ 有关。

#### 4.2.2 指数分布 $X \sim E(\lambda)$（或 $Exp(\lambda), \ \lambda > 0$）

$$f(x) = \begin{cases} \lambda e^{-\lambda x}, & x > 0, \\ 0, & x \le 0, \end{cases} \qquad F(x) = \begin{cases} 1 - e^{-\lambda x}, & x > 0, \\ 0, & x \le 0. \end{cases}$$

- **无记忆性**：$\forall t, t_0 > 0$，恒有 $P(X > t_0 + t \mid X > t_0) = \frac{e^{-\lambda(t_0+t)}}{e^{-\lambda t_0}} = e^{-\lambda t} = P(X > t)$。
- **与泊松过程的关系（Example 20）**：若长度为 $t$ 的时间段内故障次数 $N(t) \sim P(\lambda t)$，则首次故障前的无故障时间 $T$ 满足 $\{T > t\} \iff \{N(t) = 0\}$，故 $F_T(t) = 1 - P(N(t) = 0) = 1 - e^{-\lambda t} \ (t \ge 0)$，即 $T \sim E(\lambda)$。

#### 4.2.3 正态分布 $X \sim N(\mu, \sigma^2)$（$\sigma > 0$）

$$f(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}, \quad -\infty < x < +\infty$$

```text
几何性质    关于位置参数 x = mu 对称；峰值 f(mu) = 1/(sqrt(2*pi)*sigma)；拐点 x = mu +- sigma
参数影响    mu 决定左右平移；尺度参数 sigma 越小曲线越高瘦（集中），sigma 越大越矮胖（分散）
```

当 $\mu = 0, \ \sigma = 1$ 时称为**标准正态分布** $Z \sim N(0, 1)$，密度与分布函数记为 $\varphi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$ 与 $\Phi(z)$，满足：

$$
\Phi(-z_0) = 1 - \Phi(z_0), \qquad Z = \frac{X - \mu}{\sigma} \sim N(0, 1) \implies F_X(a) = \Phi\left(\frac{a - \mu}{\sigma}\right)
$$

**$3\sigma$ 准则**：$P(|X - \mu| < k\sigma) = 2\Phi(k) - 1$，当 $k = 1, 2, 3$ 时分别为 $0.6826, \ 0.9544, \ 0.9974$。

<details markdown="1">
<summary>点击展开：正态归一化证明与混合型分布例题（Example 25）</summary>

**1. 正态密度归一化证明**

令 $t = \frac{x-\mu}{\sigma}$，归结为证 $I = \int_{-\infty}^{+\infty} e^{-t^2/2}\,dt = \sqrt{2\pi}$。利用极坐标变换计算二重积分：

$$
I^2 = \iint_{\mathbb{R}^2} e^{-\frac{x^2+y^2}{2}}\,dx\,dy = \int_0^{2\pi} d\theta \int_0^{+\infty} r e^{-\frac{r^2}{2}}\,dr = 2\pi \implies I = \sqrt{2\pi}
$$

---

**2. 截断等待时间——非连非离型变量（Example 25）**

设服务等待时间 $X \sim E(1/10)$，超过 15 分钟即离开，实际等待时间 $Y = \min\{X, 15\}$。
由全概率公式或等价事件（当 $0 \le y < 15$ 时 $\{\min\{X, 15\} \le y\} \iff \{X \le y\}$）得：

$$
F_Y(y) = \begin{cases}
0, & y < 0, \\
1 - e^{-y/10}, & 0 \le y < 15, \\
1, & y \ge 15.
\end{cases}
$$

因 $Y$ 取值充满 $[0, 15]$ 且在 $y = 15$ 处有非零跳跃度 $P(Y = 15) = e^{-1.5} \neq 0$，故 $Y$ 为**非连非离型随机变量**。

</details>

---

## 5 随机变量函数的分布

已知 $X$ 的分布求 $Y = g(X)$ 的分布，核心是**寻找等价事件**。离散型直接合并等价事件概率 $P(Y = y_j) = P(X \in I_j)$；连续型分为**分布函数法**与**单调变换公式法**。

### 5.1 分布函数法与常用非单调变换

对一般连续型变换 $Y = g(X)$，先写出 $F_Y(y) = P(g(X) \le y) = P(X \in I(y))$，再利用复合求导 $\frac{d}{dy}F_X(h(y)) = f_X(h(y))h'(y)$ 得密度函数 $f_Y(y)$。由此导出两个核心二级公式：

1. **绝对值变换 $Y = |X|$**：

$$
f_Y(y) = \begin{cases}
f_X(y) + f_X(-y), & y \ge 0, \\
0, & y < 0.
\end{cases}
$$

2. **平方变换 $Z = X^2$**：

$$
f_Z(z) = \begin{cases}
\dfrac{1}{2\sqrt{z}}\left[f_X(\sqrt{z}) + f_X(-\sqrt{z})\right], & z > 0, \\
0, & z \le 0.
\end{cases}
$$

特别地，若 $X \sim N(0, 1)$，则 $Z = X^2$ 服从自由度为 $1$ 的**卡方分布** $\chi^2(1)$，其密度为 $f_Z(z) = \frac{1}{\sqrt{2\pi}} z^{-1/2} e^{-z/2} \ (z > 0)$。

### 5.2 单调函数公式法与理论推论

**定理 1（单调变换公式）**：设 $X$ 支撑为 $(a, b)$，若 $y = g(x)$ 在 $(a, b)$ 内具有连续导函数且恒有 $g'(x) > 0$（或恒有 $g'(x) < 0$），记反函数为 $x = h(y)$，值域端点为 $\alpha = \min(g(a), g(b)), \ \beta = \max(g(a), g(b))$，则：

$$
f_Y(y) = \begin{cases}
f_X[h(y)] \cdot |h'(y)|, & \alpha < y < \beta, \\
0, & \text{其他}.
\end{cases}
$$

**推论 1（正态分布的线性不变性）**：若 $X \sim N(\mu, \sigma^2)$，则对 $a \neq 0$，有 $Y = aX + b \sim N(a\mu + b, a^2\sigma^2)$。

**定理 2（概率积分变换，Probability Integral Transformation）**：设 $X$ 具有连续的分布函数 $F_X(x)$，则随机变量 $Y = F_X(X)$ 必服从 $(0, 1)$ 上的均匀分布 $U(0, 1)$。

<details markdown="1">
<summary>典型例题：不对称区间分段叠加与单调/非单调正弦变换对比（Example 30, 34, 35）</summary>

**1. 不对称支撑下的 $Y = |X|$ 分段叠加（Example 30）**

设 $X \sim U(-1, 2)$（在 $[-1, 2]$ 上 $f_X(x) = 1/3$），求 $Y = |X|$ 的密度函数。需按 $f_X(-y)$ 是否为零分段：

$$
f_Y(y) = f_X(y) + f_X(-y) = \begin{cases}
1/3 + 1/3 = 2/3, & 0 \le y < 1, \\
1/3 + 0 = 1/3, & 1 \le y \le 2, \\
0, & \text{其他}.
\end{cases}
$$

---

**2. 单调区间 vs. 非单调区间上的 $Y = \sin X$（Example 34 vs. 35）**

- **单调区间 $X \sim U(-\pi/2, \pi/2)$**：$g(x) = \sin x$ 在该区间内 $g'(x) = \cos x > 0$，直接套用单调公式（$h(y) = \arcsin y$）：
  $$
  f_Y(y) = \frac{1}{\pi\sqrt{1 - y^2}}, \quad -1 < y < 1
  $$
- **非单调区间 $X \sim U(0, \pi)$**：$g(x) = \sin x$ 在 $(0, \pi)$ 上不单调，**不可套用公式**。用分布函数法：对 $0 \le y < 1$，有 $F_Y(y) = P(X \in [0, \arcsin y] \cup [\pi - \arcsin y, \pi]) = \frac{2\arcsin y}{\pi}$，求导得：
  $$
  f_Y(y) = \frac{2}{\pi\sqrt{1 - y^2}}, \quad 0 \le y < 1
  $$

</details>