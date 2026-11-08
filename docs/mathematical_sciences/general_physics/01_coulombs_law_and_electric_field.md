# Chapter 1: Coulomb's Law and the Electric Field（库仑定律与电场）

!!! abstract
    General Physics II (Electromagnetism) | 第一章课堂与讲义笔记
    
    参考：
    
    - Lecture 1: *Coulomb's Law and the Electric Field* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 1 & Halliday, Resnick & Krane, *Physics*, Chapters 25 & 26

## 1 电荷与材料分类 (Electric Charge and Materials)

### 1.1 绝缘体与导体 (Insulators and Conductors)

所有物质均由原子（Atoms）构成，每个原子由带正电的原子核（Nucleus，含质子 Protons）和周围带负电的电子（Electrons）组成。根据电荷在材料内部能否自由移动，可将材料分为四类：

| 材料类型（中英对照） | 物理特征说明 | 典型代表材料 |
| :--- | :--- | :--- |
| **绝缘体（Insulators）** | 电荷无法在其中自由移动 | 橡胶、塑料、玻璃、化学纯水（Chemically pure water） |
| **导体（Conductors）** | 电荷可以在其中相当自由地移动 | 金属（$\text{Cu}, \text{Al}$ 等）、人体、自来水（Tap water） |
| **半导体（Semiconductors）** | 导电性能介于导体与绝缘体之间 | 硅（$\text{Si}$）、砷化镓（$\text{GaAs}$） |
| **超导体（Superconductors）** | 理想导体（Perfect conductors），电荷移动不受任何阻碍 | 低温超导材料 |

**导体导电的微观机制**：当铜等金属原子结合形成固体时，部分外层电子脱离原子核束缚，可以在固体内部自由游走，称为**传导电子**（Conduction Electrons），而留在原处的原子则成为带正电的**正离子**（Positive Ions）。

### 1.2 电荷的三大基本性质 (Fundamental Properties of Electric Charge)

自然界只存在两种电荷，由本杰明·富兰克林（Benjamin Franklin）命名为**正电荷**（Positive Charge）和**负电荷**（Negative Charge）。同号电荷相互排斥（Repel），异号电荷相互吸引（Attract）。物体内部所有正负电荷的代数和称为**净电荷**（Net Charge）；若净电荷为零，则称该物体是**电中性的**（Charge Neutral / Electrically Neutral）。

电荷具有以下三个至关重要的基本物理性质：

1. **电荷量子化（Quantization of Electric Charge）**：
   电荷只能取分立的离散值，任何正负电荷量 $q$ 都必然是某个基本常数的整数倍：
   $$q = ne \qquad (n \in \mathbb{Z})$$
   其中 $e = 1.602 \times 10^{-19}\text{ C}$ 称为**元电荷**（Elementary Charge）。一个质子携带 $+e$ 电荷，一个电子携带 $-e$ 电荷（注：夸克 Quarks 携带 $\pm e/3$ 和 $\pm 2e/3$ 分数电荷，但从不单独自由存在）。
2. **电荷守恒定律（Conservation of Charge）**：
   电荷可以从一个物体转移到另一个物体，也可以被产生（Created）或湮灭（Annihilated），但正负电荷必须**等量同时产生或同时湮灭**，孤立系统的净电荷总量保持不变（例如电子-正电子对 $\text{e}^-\text{e}^+$ 湮灭为两个不带电的 $\gamma$ 射线光子）。
3. **洛伦兹不变性（Lorentz Invariance）**：
   物体的电荷量不随物体运动速度或参考系的改变而变化（这与狭义相对论中随速度变化的相对论质量 Relativistic Mass 形成鲜明对比）。

<details markdown="1">
<summary>拓展阅读：密立根油滴实验（Millikan's Oil-Drop Experiment）与费曼“草包族科学”</summary>

- **实验原理**：1897 年 J. J. Thomson 发现了电子并测出了电子的**荷质比**（Charge-to-mass ratio）。随后 R. A. Millikan 与其学生 H. Fletcher 通过著名的**油滴实验**（Oil-drop experiment，获 1923 年诺贝尔物理学奖）首次精确测定了元电荷 $e$。实验中，带不同电荷量 $q$ 的微小油滴进入平行板匀强电场区域，同时受到重力（Gravitational force）、空气浮力（Buoyancy force）、空气粘滞阻力（Drag force）与电场力（Electric force）的作用，通过显微镜观测其平衡或匀速运动速度即可反推 $q$。
- **科学史启示（Cargo Cult Science）**：费曼（R. Feynman）在加州理工学院毕业演讲中指出，密立根当年测得的 $e = 1.592 \times 10^{-19}\text{ C}$ 略低于真实值（$1.602 \times 10^{-19}\text{ C}$），原因是他使用了错误的空气粘滞系数（Viscosity of air）。有趣的是，此后数十年间后人测得的数值随年份缓慢爬升而非一步到位，因为实验者一旦测出比密立根大得多的数值就会怀疑自己出错并寻找借口剔除数据。费曼借此告诫科学研究者：*“第一原则是你绝不能欺骗自己，而你自己正是最容易被欺骗的人。”*

</details>

---

## 2 库仑定律与叠加原理 (Coulomb's Law and Principle of Superposition)

### 2.1 库仑定律的矢量形式

对于两个静止的**点电荷**（Point Charges，即物理尺寸远小于考察距离的理想化带电体），电荷 $1$ 对电荷 $2$ 施加的**静电力 / 库仑力**（Electrostatic Force / Coulomb Force）的完整矢量形式为：

$$\vec{F}_{12} = k \frac{q_1 q_2}{r_{12}^2} \hat{r}_{12} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r_{12}^2} \hat{r}_{12}$$

公式中各物理量的严格定义如下：

- $\vec{F}_{12}$：施力者为颗粒 $1$、受力者为颗粒 $2$ 的库仑力矢量；
- $r_{12} = \vert{}\vec{r}_2 - \vec{r}_1\vert{}$：颗粒 $1$ 与颗粒 $2$ 之间的距离；
- $\hat{r}_{12} = \dfrac{\vec{r}_{12}}{r_{12}} = \dfrac{\vec{r}_2 - \vec{r}_1}{\vert{}\vec{r}_2 - \vec{r}_1\vert{}}$：**由颗粒 $1$ 指向颗粒 $2$ 的单位矢量**（Unit Vector）；
- $k = \dfrac{1}{4\pi\epsilon_0} \approx 8.99 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$：**静电力常量**（Electrostatic Constant）；
- $\epsilon_0 \approx 8.85 \times 10^{-12}\text{ C}^2/(\text{N}\cdot\text{m}^2)$：**真空介电常数**（Permittivity Constant，引入 $4\pi\epsilon_0$ 是为了简化后续的麦克斯韦方程组）。

### 2.2 叠加原理 (Principle of Superposition)

当空间存在 $N$ 个静止点电荷时，任意两电荷间的相互作用力不受其他电荷存在的影响。因此，第 $i$ 个点电荷 $q_i$ 所受的总静电力 $\vec{F}_i$ 等于其余所有点电荷对它单独作用的库仑力的**矢量和**（Vector Sum）：

$$\vec{F}_i = \sum_{j \neq i} \vec{F}_{ji} = \frac{1}{4\pi\epsilon_0} \sum_{j \neq i} \frac{q_j q_i}{r_{ji}^2} \hat{r}_{ji}$$

---

## 3 电场与电场线 (The Electric Field and Electric Field Lines)

### 3.1 场的物理概念与电场定义

为了克服经典的**超距作用**（Action at a Distance）困难，法拉第与麦克斯韦引入了**场**（Field）的概念：场是空间位置与时间的函数，用于描述某种物理量的空间分布（如温度场、压强场等**标量场 Scalar Fields**，以及流速场、力场等**矢量场 Vector Fields**）。电荷 $1$ 在周围时空中建立起**电场**（Electric Field），当电荷 $2$ 置于某点时，便受到该点电场的局域作用力（且电场的变化在空间传播需要时间）。

**电场的数学定义**：将一微小的正**检验电荷**（Test Charge）$q_0$ 置于空间位置 $\vec{r}$ 处，若它受到的静电力为 $\vec{F}$，则该点的电场强度 $\vec{E}(\vec{r})$ 定义为：

$$\vec{E}(\vec{r}) = \frac{\vec{F}}{q_0}$$

!!! note "思考题解析：为什么要求检验电荷 $q_0$ 足够“小”（Small）？"
    这里的“小”包含两层物理含义：
    
    1. **空间尺寸足够小（Small physical size）**：使其可以被视为理想点电荷，从而精确探测空间某单一几何点 $\vec{r}$ 处的局域场强；
    2. **所带电荷量足够小（Small amount of charge）**：防止检验电荷自身的电场对原本的源电荷（Source charges）分布产生反作用（极化或位移），确保测得的是未受扰动的原电场。

由库仑定律与叠加原理，位于原点的单个点电荷 $q$ 以及位于 $\vec{r}_1, \dots, \vec{r}_N$ 的点电荷系在位置 $\vec{r}$ 处产生的电场分别为：

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{r}, \qquad \vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^N \frac{q_i}{\vert{}\vec{r} - \vec{r}_i\vert{}^3} (\vec{r} - \vec{r}_i)$$

当一个带电粒子 $q$（含正负号）置于外电场（External Field）$\vec{E}$ 中时，所受静电力为 $\vec{F} = q\vec{E}$（正电荷受力与 $\vec{E}$ 同向，负电荷受力与 $\vec{E}$ 反向）。

### 3.2 电场线 (Electric Field Lines)

法拉第引入**电场线**（Electric Field Lines）来直观可视化电场，其性质类似于理想不可压缩流体中的**流线**（Streamlines，满足连续性方程 Equation of Continuity）。绘制与理解电场线需遵循三条基本规则：

| 规则编号 | 核心物理准则 | 推论与几何意义 |
| :--- | :--- | :--- |
| **规则 1（起止点）** | 电场线总是从**正电荷**（或无穷远处）出发（Originate），终止（Terminate）于**负电荷**（或无穷远处） | 正电荷相当于流体的“源”（Source），负电荷相当于“汇”（Drain） |
| **规则 2（切线方向）** | 空间任意一点处电场线的**切线方向**（Tangent direction）即为该点电场矢量 $\vec{E}$ 的方向 | 在无电荷的单点处电场方向唯一，因此**两条电场线绝不会相交（Never cross）** |
| **规则 3（疏密程度）** | 在垂直于电场线的截面上，电场线的**相对数密度**（Density of lines）正比于该处电场强度的大小 $\vert{}\vec{E}\vert{}$ | 电场线越密集处场强越大，越稀疏处场强越小 |

---

## 4 电偶极子 (Electric Dipole)

### 4.1 电偶极矩与轴线/一般位置电场推导

**电偶极子**（Electric Dipole）是由两个电量相等（均为 $q>0$）、符号相反（$\pm q$）、相距微小距离 $d$ 的点电荷组成的特殊系统。定义位移矢量 $\vec{d}$ 的方向为**从负电荷 $-q$ 指向正电荷 $+q$**，则系统的**电偶极矩**（Electric Dipole Moment）定义为：

$$\vec{p} = q\vec{d}$$

理想的电偶极子（Ideal Dipole）是指在保持电偶极矩 $\vec{p} = q\vec{d}$ 不变的条件下，令间距 $d \to 0$ 的极限系统。

**1. 偶极子轴线上的远场（On-Axis Field，$z \gg d$）**

设偶极子中心位于原点，沿 $z$ 轴放置，在距离中心为 $z \ (z \gg d)$ 的轴线点 $P$ 处，利用泰勒展开 $(1 \mp \frac{d}{2z})^{-2} \approx 1 \pm \frac{d}{z}$ 可得：

$$E_z = \frac{q}{4\pi\epsilon_0\left(z - \frac{1}{2}d\right)^2} - \frac{q}{4\pi\epsilon_0\left(z + \frac{1}{2}d\right)^2} = \frac{q}{4\pi\epsilon_0 z^2}\left[\left(1 - \frac{d}{2z}\right)^{-2} - \left(1 + \frac{d}{2z}\right)^{-2}\right] \approx \frac{1}{2\pi\epsilon_0} \frac{p}{z^3}$$

**2. 空间任意点的一般矢量公式（General Vector Formula，$r \gg d$）**

设 $+q$ 位于 $+\vec{d}/2$，$-q$ 位于 $-\vec{d}/2$，空间观测点位于 $\vec{r} \ (r \gg d)$。由叠加原理：

$$\vec{E}(\vec{r}) = \frac{q}{4\pi\epsilon_0} \left( \frac{\vec{r} - \frac{\vec{d}}{2}}{\left\vert{}\vec{r} - \frac{\vec{d}}{2}\right\vert{}^3} - \frac{\vec{r} + \frac{\vec{d}}{2}}{\left\vert{}\vec{r} + \frac{\vec{d}}{2}\right\vert{}^3} \right)$$

当 $d \ll r$ 时，忽略 $d^2/4$ 二阶小量并利用广义二项式展开 $(1 + x)^{-3/2} \approx 1 - \frac{3}{2}x$：

$$\left\vert{}\vec{r} \mp \frac{\vec{d}}{2}\right\vert{}^{-3} = \left(r^2 \mp \vec{r}\cdot\vec{d} + \frac{d^2}{4}\right)^{-3/2} = r^{-3}\left(1 \mp \frac{\vec{r}\cdot\vec{d}}{r^2}\right)^{-3/2} \approx r^{-3}\left(1 \pm \frac{3}{2}\frac{\vec{r}\cdot\vec{d}}{r^2}\right)$$

代入原式并保留关于 $\vec{d}$ 的一阶主项（注意到 $q\vec{d} = \vec{p}$ 且 $\hat{r} = \vec{r}/r$），即得**电偶极子在空间任意远点处的电场矢量通式**：

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{1}{r^3} \left[ 3(\vec{p}\cdot\hat{r})\hat{r} - \vec{p} \right]$$

!!! tip "物理图像：为什么电偶极子的电场按 $1/r^3$ 衰减？"
    单个点电荷的电场按 $1/r^2$ 衰减；但从远处（$r \gg d$）观察电偶极子时，正负电荷 $+q$ 与 $-q$ 几乎重合，它们产生的 $1/r^2$ 领头阶（Leading order）电场相互抵消，剩余的净电场由间距 $d$ 引起的一阶修正项主导，因此随距离按 $1/r^3$ 快速衰减。

### 4.2 外电场中的电偶极子 (Dipole in an External Electric Field)

将电偶极子 $\vec{p} = q\vec{d}$ 置于**匀强外电场**（Uniform Electric Field）$\vec{E}$ 中：

1. **净平动力为零**：正负电荷所受电场力分别为 $\vec{F}_+ = +q\vec{E}$ 与 $\vec{F}_- = -q\vec{E}$，合力 $\vec{F}_{\text{net}} = 0$，因此偶极子的质心（Center of mass）不会发生平动。
2. **合力矩（Net Torque）**：设 $\vec{p}$ 与 $\vec{E}$ 夹角为 $\theta$，一对等大反向的力对质心产生恢复力矩 $\tau = -Fd\sin\theta = -pE\sin\theta$，写成矢量叉乘形式为：
   $$\vec{\tau} = \vec{p} \times \vec{E}$$
   该力矩总是试图将电偶极矩 $\vec{p}$ 旋转到与外电场 $\vec{E}$ 一致的方向（即减小夹角 $\theta$）。若置于非匀强电场中，偶极子除受力矩外还会受到净平动力 $\vec{F} = (\vec{p}\cdot\nabla)\vec{E}$。

---

## 5 连续电荷分布与积分计算 (Continuous Charge Distribution)

在宏观尺度下，包含海量元电荷的带电体可视为**连续电荷分布**（Continuous Charge Distribution）。采用微元法（Slicing into infinitesimal charge elements $dq$），点电荷 $q_0$ 所受库仑力与空间位置 $\vec{r}$ 处的电场强度转化为积分形式：

$$\vec{F}_0 = \frac{1}{4\pi\epsilon_0} \int_q \frac{q_0\,dq}{r_q^2} \hat{r}_q, \qquad \vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_q \frac{dq}{r_q^2} \hat{r}_q$$

其中 $r_q$ 为电荷微元 $dq$ 到场点 $\vec{r}$ 的距离，$\hat{r}_q$ 为从 $dq$ 指向场点的单位矢量。根据带电体的维度，电荷微元 $dq$ 可分别表示为线电荷密度 $\lambda\,dl$、面电荷密度 $\sigma\,dS$ 或体电荷密度 $\rho\,dV$。

**经典模型（Example 1.1）：均匀带电圆盘轴线上的电场（Uniformly Charged Disk）**

设半径为 $R$ 的圆盘均匀携带总电荷 $Q>0$，面电荷密度（Surface charge density）为 $\sigma = \frac{Q}{\pi R^2}$。求圆盘中心轴线上距盘心为 $z \ (z > 0)$ 的点 $P$ 处的电场：

1. **取微元**：在极坐标 $(r, \phi)$ 下，取半径 $r \to r+dr$、方位角 $\phi \to \phi+d\phi$ 的面元 $dS = r\,dr\,d\phi$，电荷微元为 $dq = \sigma r\,dr\,d\phi$，到点 $P$ 的距离为 $r_q = \sqrt{z^2 + r^2}$。
2. **对称性简化**：由轴对称性（Axial symmetry），垂直于 $z$ 轴的径向分量两两抵消，只需积分沿 $z$ 轴的分量 $dE_z = \frac{1}{4\pi\epsilon_0}\frac{dq}{r_q^2}\cos\theta = \frac{1}{4\pi\epsilon_0}\frac{\sigma z r\,dr\,d\phi}{(z^2+r^2)^{3/2}}$。
3. **二重积分求解**：
   $$E_z = \frac{\sigma z}{4\pi\epsilon_0} \int_0^R dr \int_0^{2\pi} d\phi \frac{r}{(z^2 + r^2)^{3/2}} = \frac{\sigma z}{2\epsilon_0} \int_0^R \frac{r\,dr}{(z^2 + r^2)^{3/2}} = \frac{\sigma}{2\epsilon_0}\left(1 - \frac{z}{\sqrt{z^2 + R^2}}\right)$$
   （当 $R \to \infty$ 时，$E_z \to \frac{\sigma}{2\epsilon_0}$，即退化为无限大均匀带电平板的匀强电场）。

<details markdown="1">
<summary>数学附录：物理学中的泰勒多项式展开与矢量代数（Appendix 1B & 1C）</summary>

**1. 常用麦克劳林级数展开（Maclaurin Series，适用于 $\vert{}x\vert{} \ll 1$）**

| 函数形式 | 多项式近似展开式（保留至领头修正项） | 远场大参数展开示例（当 $z \gg a$ 时，提取 $1/z$） |
| :--- | :--- | :--- |
| $(1 + x)^n$ | $1 + nx + \dfrac{n(n-1)}{2}x^2 + \cdots$ | $\dfrac{1}{(z+a)^2} = \dfrac{1}{z^2(1 + a/z)^2} \approx \dfrac{1}{z^2}\left(1 - \dfrac{2a}{z}\right) = \dfrac{1}{z^2} - \dfrac{2a}{z^3}$ |
| $\dfrac{1}{1 + x}$ 及 $\sqrt{1 + x}$ | $1 - x + x^2 - \cdots$ 及 $1 + \dfrac{x}{2} - \dfrac{x^2}{8} + \cdots$ | $\dfrac{1}{\sqrt{z^2 + a^2}} = \dfrac{1}{z}\left(1 + \dfrac{a^2}{z^2}\right)^{-1/2} \approx \dfrac{1}{z}\left(1 - \dfrac{a^2}{2z^2}\right)$ |
| $e^x$ 及 $\ln(1+x)$ | $1 + x + \dfrac{x^2}{2} + \cdots$ 及 $x - \dfrac{x^2}{2} + \cdots$ | $\sin x = x - \dfrac{x^3}{6} + \cdots, \quad \cos x = 1 - \dfrac{x^2}{2} + \cdots$ |

**2. 矢量点乘与叉乘（Dot Product & Cross Product）**

- **点乘（标量积）**：$\vec{A}\cdot\vec{B} \equiv AB\cos\theta$。满足交换律 $\vec{A}\cdot\vec{B} = \vec{B}\cdot\vec{A}$ 与分配律；若 $\vec{A} \perp \vec{B}$，则 $\vec{A}\cdot\vec{B} = 0$；特别地 $\vec{A}\cdot\vec{A} = A^2$。
- **叉乘（矢量积）**：$\vec{A}\times\vec{B} \equiv AB\sin\theta\,\hat{n}$（方向由右手定则 Right-hand rule 确定）。满足**反交换律**（Anti-commutative）$\vec{A}\times\vec{B} = -\vec{B}\times\vec{A}$；模长 $\vert{}\vec{A}\times\vec{B}\vert{}$ 等于以 $\vec{A}, \vec{B}$ 为邻边的平行四边形面积；特别地 $\vec{A}\times\vec{A} = \vec{0}$。

</details>

---

## 6 Chapter 1 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 1.1: Electric Quadrupole（电四极子的远场展开）</summary>

**Problem Statement:**
An electric quadrupole can be viewed as 4 point charges at 4 corners of a square of side $a$, a pair of $+q$ located at one of the diagonals, and a pair of $-q$ located at the other. Suppose $a$ is small but $\Omega = qa^2$ is finite. Use $\Omega$ to express the electric field generated by this quadrupole at $P$:
(a) $P$ is located along the diagonal of $-q$'s, and at distance $x$ away from the center of the square.
(b) $P$ is located along the axis perpendicular to one of the edges and through the center, and at distance $x$ away from the center of the square.

---

**中文解析：**

**(a) 点 $P$ 位于两个 $-q$ 所在的对角线延长线上（距中心 $x \gg a$）**：
以正方形中心为原点，令两个 $-q$ 所在的对角线为 $x$ 轴，另一个对角线（两个 $+q$）为 $y$ 轴。记半对角线长为 $d = \frac{a}{\sqrt{2}}$，则 $d^2 = \frac{a^2}{2}$，且四极矩参数满足 $\Omega = qa^2 = 2qd^2$。
四个电荷的坐标分别为：$-q$ 位于 $(\pm d, 0)$，$+q$ 位于 $(0, \pm d)$。由对称性，点 $P(x, 0)$ 处的电场只有 $x$ 分量：

$$
E_x = \frac{q}{4\pi\epsilon_0} \left[ -\frac{1}{(x - d)^2} - \frac{1}{(x + d)^2} + \frac{2x}{(x^2 + d^2)^{3/2}} \right]
$$

当 $x \gg d$ 时，将每一项对小量 $\frac{d}{x}$ 展开至二阶项 $(d/x)^2$：

$$
(x - d)^{-2} + (x + d)^{-2} = x^{-2}\left[\left(1 - \frac{d}{x}\right)^{-2} + \left(1 + \frac{d}{x}\right)^{-2}\right] \approx x^{-2}\left[2 + 6\frac{d^2}{x^2}\right]
$$

$$
2x(x^2 + d^2)^{-3/2} = 2x^{-2}\left(1 + \frac{d^2}{x^2}\right)^{-3/2} \approx x^{-2}\left[2 - 3\frac{d^2}{x^2}\right]
$$

代入相减，常数项 $2$ 完全抵消，得到：

$$
E_x \approx \frac{q}{4\pi\epsilon_0 x^2}\left(-9\frac{d^2}{x^2}\right) = -\frac{9qd^2}{4\pi\epsilon_0 x^4} = -\frac{9\Omega}{8\pi\epsilon_0 x^4}
$$

方向沿对角线指向正方形中心，大小为 $E = \dfrac{9\Omega}{8\pi\epsilon_0 x^4}$。

**(b) 点 $P$ 位于过中心且垂直于正方形某条边的轴线上（距中心 $x \gg a$）**：
重新建立坐标系，使正方形四边平行于 $x, y$ 轴，点 $P$ 位于 $(x, 0)$。此时右半边 $x' = +a/2$ 处有一对异号电荷：$(a/2, a/2)$ 处为 $+q$，$(a/2, -a/2)$ 处为 $-q$，构成一个电偶极矩为 $\vec{p}_1 = qa\hat{y}$ 的竖直电偶极子；左半边 $x' = -a/2$ 处则相反，构成一个电偶极矩为 $\vec{p}_2 = -qa\hat{y}$ 的反向竖直电偶极子。
由对称性，点 $P(x, 0)$ 处的 $x$ 方向场强完全抵消（$E_x = 0$），只有沿 $y$ 方向的分量：

$$E_y = \frac{q}{4\pi\epsilon_0} \left[ -\frac{2(a/2)}{\left[(x - a/2)^2 + (a/2)^2\right]^{3/2}} + \frac{2(a/2)}{\left[(x + a/2)^2 + (a/2)^2\right]^{3/2}} \right]$$

利用 $\left[(x \mp a/2)^2 + a^2/4\right]^{-3/2} = x^{-3}\left(1 \mp \frac{a}{x} + \frac{a^2}{2x^2}\right)^{-3/2} \approx x^{-3}\left(1 \pm \frac{3a}{2x}\right)$ 代入化简，得：

$$E_y \approx \frac{qa}{4\pi\epsilon_0 x^3}\left(-\frac{3a}{x}\right) = -\frac{3qa^2}{4\pi\epsilon_0 x^4} = -\frac{3\Omega}{4\pi\epsilon_0 x^4}$$

电场方向平行于被穿过的那条边（垂直于轴线），大小为 $E = \dfrac{3\Omega}{4\pi\epsilon_0 x^4}$。可以看到电四极子的远场均按 $1/x^4$ 衰减。

</details>

<details markdown="1">
<summary>Exercise 1.2 & 1.4: Spherical Shell and Solid Sphere by Direct Integration（直接积分求球壳与实心球电场）</summary>

**Problem Statement:**
- **Ex 1.2**: Explicitly use $\vec{E} = \frac{1}{4\pi\epsilon_0} \int_q \frac{dq}{r_q^2}\hat{r}_q$ to calculate the electric field generated by a uniformly charged spherical shell of radius $R$ carrying total charge $Q$, both inside ($r < R$) and outside ($r > R$). The thickness of the shell can be ignored.
- **Ex 1.4**: Explicitly use $\vec{E} = \frac{1}{4\pi\epsilon_0} \int_q \frac{dq}{r_q^2}\hat{r}_q$ to calculate the electric field generated by a uniformly charged solid sphere of radius $R$ carrying total charge $Q$, both inside ($r < R$) and outside ($r > R$).

---

**中文解析：**

**1. 均匀带电薄球壳的直接积分（Exercise 1.2）**：
设球壳半径为 $R$，面电荷密度 $\sigma = \frac{Q}{4\pi R^2}$，场点 $P$ 位于 $z$ 轴上 $(0, 0, r)$。
将球壳按极角 $\theta \in [0, \pi]$ 切分为细圆环，环半径为 $R\sin\theta$，环宽为 $R\,d\theta$，环上电荷微元为 $dq = \sigma (2\pi R\sin\theta)(R\,d\theta) = \frac{Q}{2}\sin\theta\,d\theta$。
环上各点到 $P$ 的距离为 $s = \sqrt{r^2 + R^2 - 2rR\cos\theta}$，且夹角余弦为 $\cos\alpha = \frac{r - R\cos\theta}{s}$。因此：

$$
E_z(r) = \frac{1}{4\pi\epsilon_0} \int_0^\pi \frac{Q\sin\theta\,d\theta}{2s^2} \frac{r - R\cos\theta}{s} = \frac{Q}{8\pi\epsilon_0} \int_0^\pi \frac{(r - R\cos\theta)\sin\theta}{(r^2 + R^2 - 2rR\cos\theta)^{3/2}}\,d\theta
$$

作换元 $s = \sqrt{r^2 + R^2 - 2rR\cos\theta}$，两边微分得 $s\,ds = rR\sin\theta\,d\theta \implies \sin\theta\,d\theta = \frac{s\,ds}{rR}$，且 $r - R\cos\theta = \frac{s^2 + r^2 - R^2}{2r}$。积分上下限变为 $s_{\min} = |r - R|$ 到 $s_{\max} = r + R$：

$$
E_z(r) = \frac{Q}{16\pi\epsilon_0 r^2 R} \int_{|r - R|}^{r + R} \left(1 + \frac{r^2 - R^2}{s^2}\right) ds = \frac{Q}{16\pi\epsilon_0 r^2 R} \left[ s - \frac{r^2 - R^2}{s} \right]_{|r - R|}^{r + R}
$$

- **当 $r > R$（球壳外部）**：$|r - R| = r - R$，方括号计算结果为 $[(r+R) - (r-R)] - [(r-R) - (r+R)] = 4R$，故：
  $$
  \vec{E}(\vec{r}) = \frac{Q}{4\pi\epsilon_0 r^2}\hat{r} \quad (r > R)
  $$
- **当 $r < R$（球壳内部）**：$|r - R| = R - r$，方括号计算结果为 $[(r+R) - (r-R)] - [(R-r) - (R+r)] = 2r - 2r = 0$，故：
  $$
  \vec{E}(\vec{r}) = \vec{0} \quad (r < R)
  $$

---

**2. 均匀带电实心球的直接积分（Exercise 1.4）**：
将半径为 $R$、体电荷密度为 $\rho = \frac{Q}{\frac{4}{3}\pi R^3}$ 的实心球视为无数层半径为 $r' \in [0, R]$、厚度为 $dr'$ 的同心薄球壳的叠加，每层球壳带电量为 $dq(r') = 4\pi r'^2 \rho\,dr' = \frac{3Q}{R^3}r'^2\,dr'$：

- **当 $r > R$（球外）**：场点位于所有薄球壳外部，每层球壳均等效于中心点电荷，积分得：
  $$
  \vec{E}(\vec{r}) = \frac{\hat{r}}{4\pi\epsilon_0 r^2} \int_0^R dq(r') = \frac{Q}{4\pi\epsilon_0 r^2}\hat{r}
  $$
- **当 $r < R$（球内）**：半径 $r' > r$ 的外层球壳对场点贡献为零，仅有 $0 \le r' \le r$ 的内层球壳产生贡献：
  $$
  \vec{E}(\vec{r}) = \frac{\hat{r}}{4\pi\epsilon_0 r^2} \int_0^r \frac{3Q}{R^3}r'^2\,dr' = \frac{Qr}{4\pi\epsilon_0 R^3}\hat{r}
  $$

</details>

<details markdown="1">
<summary>Exercise 1.3 & 1.9: Dipole-Dipole Force & Rigid Dipole Dynamics（偶极子间作用力与偶极子简谐振动）</summary>

**Problem Statement:**
- **Ex 1.3**: An electric dipole $\vec{p}_2$ is located at position $\vec{r}$ relative to a second dipole $\vec{p}_1$, with $r$ much larger than the size of either dipole. Find the force exerted on $\vec{p}_2$ by $\vec{p}_1$, expressed in terms of $\vec{p}_1$, $\vec{p}_2$ and $\vec{r}$.
- **Ex 1.9**: A rigid electric dipole is made of two point charges $+q$ and $-q$, each of mass $m$, fixed at the two ends of a massless rod of length $d$, so that its dipole moment has magnitude $p = qd$.
  (a) The dipole is placed in a uniform electric field $\vec{E}$ and released from rest at a small angle $\theta_0$ from the direction of $\vec{E}$. Show that it rotates about its center and oscillates harmonically about the direction of $\vec{E}$, and find the angular frequency of the oscillation.
  (b) The uniform field is now replaced by the field of a point charge $Q > 0$ fixed at the origin. The dipole sits on the $z$ axis at $z = r \gg d$, with $\vec{p} = p\hat{z}$, that is, pointing away from $Q$. Find the net force on the dipole to leading order in $d/r$, and verify that it is equal and opposite to the force that the dipole exerts on $Q$.

---

**中文解析：**

**1. 两个电偶极子之间的相互作用力（Exercise 1.3）**：
将 $\vec{p}_2 = q_2 \vec{d}_2$ 写为位于 $\vec{r} + \vec{d}_2/2$ 的 $+q_2$ 与位于 $\vec{r} - \vec{d}_2/2$ 的 $-q_2$。置于 $\vec{p}_1$ 产生的电场 $\vec{E}_1(\vec{r}) = \frac{1}{4\pi\epsilon_0 r^3}[3(\vec{p}_1\cdot\hat{r})\hat{r} - \vec{p}_1]$ 中，对 $\vec{d}_2$ 展开至一阶：

$$
\vec{F}_{12} = q_2\left[\vec{E}_1\left(\vec{r} + \frac{\vec{d}_2}{2}\right) - \vec{E}_1\left(\vec{r} - \frac{\vec{d}_2}{2}\right)\right] \approx q_2(\vec{d}_2 \cdot \nabla)\vec{E}_1(\vec{r}) = (\vec{p}_2 \cdot \nabla)\vec{E}_1(\vec{r})
$$

利用矢量梯度恒等式 $(\vec{p}_2\cdot\nabla)\vec{r} = \vec{p}_2$ 以及 $(\vec{p}_2\cdot\nabla)r^{-n} = -n r^{-(n+2)}(\vec{p}_2\cdot\vec{r})$ 对 $\vec{E}_1(\vec{r}) = \frac{1}{4\pi\epsilon_0}\left[\frac{3(\vec{p}_1\cdot\vec{r})\vec{r}}{r^5} - \frac{\vec{p}_1}{r^3}\right]$ 求方向导数，整理得：

$$
\vec{F}_{12} = \frac{3}{4\pi\epsilon_0 r^4}\left[ (\vec{p}_1\cdot\hat{r})\vec{p}_2 + (\vec{p}_2\cdot\hat{r})\vec{p}_1 + (\vec{p}_1\cdot\vec{p}_2)\hat{r} - 5(\vec{p}_1\cdot\hat{r})(\vec{p}_2\cdot\hat{r})\hat{r} \right]
$$

---

**2. 刚性电偶极子在匀强场中的微幅简谐振动与点电荷场中的受力（Exercise 1.9）**：

- **(a) 转动与简谐振动角频率**：
  匀强电场中合力为零，故质心静止，偶极子绕中心旋转。两个质量为 $m$ 的粒子距中心均为 $d/2$，系统的转动惯量（Moment of inertia）为：
  $$
  I = 2 \times m\left(\frac{d}{2}\right)^2 = \frac{1}{2}md^2
  $$
  在小角度近似 $\sin\theta \approx \theta$ 下，转动定律 $I\ddot{\theta} = \tau = -pE\sin\theta$ 化为标准简谐振动方程：
  $$
  \frac{1}{2}md^2 \frac{d^2\theta}{dt^2} + pE\theta = 0 \implies \frac{d^2\theta}{dt^2} + \frac{2pE}{md^2}\theta = 0
  $$
  因此偶极子作简谐振动，其角频率为 $\omega = \sqrt{\dfrac{2pE}{md^2}} = \sqrt{\dfrac{2qE}{md}}$。

- **(b) 点电荷场中的净力与牛顿第三定律验证**：
  原点处点电荷 $Q$ 在 $z$ 轴上产生的电场为 $E_z(z) = \frac{Q}{4\pi\epsilon_0 z^2}$。偶极子所受净力为：
  $$
  F_z = q E_z\left(r + \frac{d}{2}\right) - q E_z\left(r - \frac{d}{2}\right) \approx qd \left.\frac{dE_z}{dz}\right|_{z=r} = p \left(-\frac{2Q}{4\pi\epsilon_0 r^3}\right) = -\frac{Qp}{2\pi\epsilon_0 r^3}
  $$
  即偶极子受到的净力为 $\vec{F}_{\text{on dipole}} = -\dfrac{Qp}{2\pi\epsilon_0 r^3}\hat{z}$（指向原点 $Q$）。
  反之，位于 $z=r$ 处的偶极子 $\vec{p} = p\hat{z}$ 在原点（处于其轴线上距离 $r$ 处）产生的电场为 $\vec{E}_{\text{dipole}}(0) = +\frac{p}{2\pi\epsilon_0 r^3}\hat{z}$，故偶极子对点电荷 $Q$ 施加的力为 $\vec{F}_{\text{on } Q} = Q\vec{E}_{\text{dipole}}(0) = +\dfrac{Qp}{2\pi\epsilon_0 r^3}\hat{z}$，两者严格等大反向，满足牛顿第三定律。

</details>

<details markdown="1">
<summary>Exercise 1.6, 1.7 & 1.8: Square Equilibrium, Semi-Infinite Rod & Charged Rings（正方形平衡、半无限长杆与带电圆弧/圆环）</summary>

**Problem Statement:**
- **Ex 1.6**: Four identical point charges $q > 0$ are held at the four corners of a square of side $a$. (a) Find the magnitude and direction of the net electrostatic force on any one of them. (b) A fifth point charge $Q$ is placed at the center. Find $Q$ for which all five charges are in equilibrium.
- **Ex 1.7**: A thin rod occupies the half-line $z \ge 0$ with uniform linear charge density $\lambda > 0$. Point $P$ lies in the plane $z = 0$ at perpendicular distance $d$ from the end. (a) Calculate $E_\perp$ and $E_\parallel$ at $P$, and show $\vec{E}$ makes a $45^\circ$ angle with the rod regardless of $d$. (b) Without new integration, obtain $\vec{E}$ for an infinitely long rod.
- **Ex 1.8**: Calculate $\vec{E}$ at the center of curvature for: (a) A thin circular arc of radius $R$, total charge $Q > 0$, subtending angle $2\alpha$. (b) A full circular ring of radius $R$ in the $xy$ plane with $\lambda(\phi) = \lambda_0\cos\phi$.

---

**中文解析：**

**1. 正方形四角电荷受力与五电荷平衡（Exercise 1.6）**：

- **(a)** 考察位于右上角 $(a, a)$ 的电荷 $q$。两个相邻顶点 $(a, 0)$ 和 $(0, a)$ 距离为 $a$，合力沿对角线向外，大小为 $\sqrt{2}\frac{q^2}{4\pi\epsilon_0 a^2}$；对角顶点 $(0, 0)$ 距离为 $\sqrt{2}a$，斥力沿对角线向外，大小为 $\frac{q^2}{4\pi\epsilon_0 (2a^2)}$。故总静电力方向**沿对角线背离中心向外**，大小为：
  $$
  F = \frac{q^2}{4\pi\epsilon_0 a^2}\left(\sqrt{2} + \frac{1}{2}\right) = \frac{(2\sqrt{2} + 1)q^2}{8\pi\epsilon_0 a^2}
  $$
- **(b)** 中心电荷 $Q$ 由对称性自动处于受力平衡。要使四角电荷也平衡，$Q$ 对角上电荷的引力（距离 $r = a/\sqrt{2}$）必须抵消 $F$：
  $$
  \frac{-Qq}{4\pi\epsilon_0 (a/\sqrt{2})^2} = \frac{(2\sqrt{2} + 1)q^2}{8\pi\epsilon_0 a^2} \implies Q = -\frac{2\sqrt{2} + 1}{4}q
  $$

---

**2. 半无限长细杆的 $45^\circ$ 恒定倾角与无限长直导线（Exercise 1.7）**：

- **(a)** 设细杆沿 $z \ge 0$ 放置，点 $P$ 距端点距离为 $d$。取微元 $dq = \lambda\,dz$，距离 $r_q = \sqrt{z^2 + d^2}$：
  $$
  E_\perp = \frac{\lambda}{4\pi\epsilon_0} \int_0^\infty \frac{d\,dz}{(z^2 + d^2)^{3/2}} = \frac{\lambda d}{4\pi\epsilon_0} \left[\frac{z}{d^2\sqrt{z^2 + d^2}}\right]_0^\infty = \frac{\lambda}{4\pi\epsilon_0 d}
  $$
  $$
  E_\parallel = E_z = -\frac{\lambda}{4\pi\epsilon_0} \int_0^\infty \frac{z\,dz}{(z^2 + d^2)^{3/2}} = -\frac{\lambda}{4\pi\epsilon_0} \left[-\frac{1}{\sqrt{z^2 + d^2}}\right]_0^\infty = -\frac{\lambda}{4\pi\epsilon_0 d}
  $$
  由于 $|E_\perp| = |E_\parallel| = \frac{\lambda}{4\pi\epsilon_0 d}$，合场强必与细杆轴线成 $45^\circ$ 夹角（指向斜下方 $-\hat{z}$ 与远离细杆的合成方向），且该角度与距离 $d$ 完全无关。
- **(b)** 无限长带电细杆可视为 $z \ge 0$ 与 $z \le 0$ 两根半无限长细杆的拼接：两者的平行分量 $E_\parallel$ 等大反向相互抵消，垂直分量 $E_\perp$ 同向叠加翻倍，立即得到无限长直导线场强：
  $$
  E = 2 E_\perp = \frac{\lambda}{2\pi\epsilon_0 d}
  $$

---

**3. 均匀带电圆弧与非均匀余弦带电圆环（Exercise 1.8）**：

- **(a) 张角为 $2\alpha$ 的均匀带电圆弧**：线电荷密度 $\lambda = \frac{Q}{2\alpha R}$。以圆弧对称轴为 $x$ 轴（$\theta \in [-\alpha, \alpha]$），圆心处 $y$ 分量抵消，沿对称轴背离圆弧方向的场强为：
  $$
  E = \int_{-\alpha}^\alpha \frac{\lambda R\,d\theta}{4\pi\epsilon_0 R^2}\cos\theta = \frac{Q}{8\pi\epsilon_0 \alpha R^2} \cdot 2\sin\alpha = \frac{Q}{4\pi\epsilon_0 R^2}\frac{\sin\alpha}{\alpha}
  $$
  极限检验：当 $\alpha \to 0$ 时，$\frac{\sin\alpha}{\alpha} \to 1$，$E \to \frac{Q}{4\pi\epsilon_0 R^2}$（退化为点电荷）；当 $\alpha = \pi$（闭合整圆环）时，$\sin\pi = 0 \implies E = 0$。
- **(b) 余弦分布圆环 $\lambda(\phi) = \lambda_0\cos\phi$**：
  总电荷量 $Q_{\text{tot}} = \int_0^{2\pi} \lambda_0\cos\phi \, R\,d\phi = 0$。
  在圆心处，微元 $dq = \lambda_0\cos\phi R\,d\phi$ 产生的场强指向 $-\hat{r} = -(\cos\phi\hat{x} + \sin\phi\hat{y})$。由于 $\int_0^{2\pi} \cos\phi\sin\phi\,d\phi = 0$，$y$ 分量抵消，仅剩 $x$ 分量：
  $$
  \vec{E} = -\hat{x} \int_0^{2\pi} \frac{\lambda_0\cos\phi R\,d\phi}{4\pi\epsilon_0 R^2}\cos\phi = -\frac{\lambda_0}{4\pi\epsilon_0 R}\left(\int_0^{2\pi} \cos^2\phi\,d\phi\right)\hat{x} = -\frac{\lambda_0}{4\epsilon_0 R}\hat{x}
  $$

</details>