# Chapter 5: Conductors in Electrostatic Field（静电场中的导体）

!!! abstract
    General Physics II (Electromagnetism) | 第五章课堂与讲义笔记
    
    参考：
    
    - Lecture 5: *The Electrical Properties of Conductors* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 5: *Conductors in Electrostatic Field* & Halliday, Resnick & Krane, *Physics*, Chapter 29

## 1 导体的静电平衡性质 (Electrostatic Properties of Conductors)

### 1.1 导体的微观图像与静电平衡概念

金属导体（Metals）与绝缘体（Insulators）在电学性质上的巨大差异，类似于液体与固体在力学性质上的差异，二者皆取决于微观粒子的迁移率（Mobility）。在金属固体中，束缚的金属正离子（Bound metal cations）构成晶格骨架（Lattice），而部分外层电子脱离原子束缚形成可以在整个晶格间自由游走的**自由电子海**（Sea of conduction electrons），充当**载流子**（Charge carriers）。值得注意的是，导电性不仅取决于元素种类，还取决于原子的成键排列方式（例如同样由纯碳原子构成的石墨 Graphite 是良导体，而金刚石 Diamond 则是绝缘体）。

当将一个孤立导体（Isolated conductor）置于外静电场 $\vec{E}_0$ 中时，自由电子立即受到电场力作用并逆着电场线向高电势一侧移动，在原处留下净正电荷。经过极短的暂态过程后，导体表面重新分布的感应电荷（Induced charges）所产生的附加电场完全抵消了导体内部的外电场，导体内不再有宏观电荷的定向移动（无电流）。这种电荷分布稳定且不随时间变化的状态称为**静电平衡状态**（Electrostatic Equilibrium）。

### 1.2 静电平衡导体的四大基本性质

处于静电平衡状态下的任何导体，必然严格满足以下四条基本物理规律：

| 性质维度 | 数学表达式 | 物理证明与推论说明 |
| :--- | :--- | :--- |
| **1. 内部场强与电势** | $\vec{E}_{\text{inside}} = \vec{0}$<br>$V = \text{const}$ | 导体内部（金属实体内部）电场处处为零；否則自由电子将受力产生持续电流，违背静电平衡。由 $\vec{E} = -\nabla V = \vec{0}$ 知**整个导体（含表面与内部）是一个等势体（Equipotential body）**，导体表面是等势面 |
| **2. 内部与表面电荷** | $\rho_{\text{inside}} = 0$<br>$q_{\text{excess}} \subset \text{Surface}$ | 在导体内部任取高斯面（或由微分形式 $\rho = \epsilon_0\nabla\cdot\vec{E} = 0$），可知导体内部处处电中性（无净电荷），**所有净剩电荷（Excess charge）只能分布在导体的外表面或内腔表面上** |
| **3. 表面外侧场强方向** | $\vec{E}_{\text{surface}} \perp \text{Surface}$ | 紧贴导体表面外侧的电场矢量必须**处处垂直于导体表面**；否则切向电场分量会驱动表面电荷移动形成表面电流 |
| **4. 表面外侧场强大小** | $\vec{E}_{\text{just outside}} = \dfrac{\sigma}{\epsilon_0}\hat{n}$ | 跨接导体表面作微小圆柱形高斯药盒（Pillbox，底面积 $A$，内底面在金属内 $\vec{E}=\vec{0}$，外底面在金属外，侧面无通量）：由高斯定理 $\epsilon_0 EA = \sigma A$ 得 $E_\perp = \dfrac{\sigma}{\epsilon_0}$（$\hat{n}$ 为表面外法向单位矢量） |

!!! warning "核心辨析：导体表面场强 $\frac{\sigma}{\epsilon_0}$ vs. 绝缘薄板场强 $\frac{\sigma}{2\epsilon_0}$"
    - **无限大均匀带电绝缘薄板（Nonconducting sheet）**：两侧均有电场穿出，圆柱药盒两个底面平分通量 $\epsilon_0(2EA) = \sigma A \implies E = \frac{\sigma}{2\epsilon_0}$。
    - **孤立带电导体平板（Conducting plate）**：在无外场时，净电荷均匀分布在左右**两个表面**上，每个表面的面电荷密度为 $\sigma_1$。在导体外侧，两个表面各自产生 $\frac{\sigma_1}{2\epsilon_0}$ 的同向电场，叠加后恰为 $E = \frac{\sigma_1}{2\epsilon_0} + \frac{\sigma_1}{2\epsilon_0} = \frac{\sigma_1}{\epsilon_0}$；而在导体内部，两表面产生的电场等大反向，叠加为 $E = 0$！当把两块带等量异号电荷的平行金属板靠近时，异号电荷相互吸引，全部净电荷迁移至相对的**内表面**（面密度变为 $2\sigma_1$），外表面电荷为零，两板之间场强为 $E = \frac{2\sigma_1}{\epsilon_0}$，两板外侧场强均为 $0$。

**表面电荷分布与曲率的关系（尖端效应）**：
对于远离其他电荷的孤立导体球，由球对称性知净电荷均匀分布（球外电场等效于球心点电荷，即壳层定理 Shell theorem）。但对于非球形的一般导体，面电荷密度 $\sigma$ 随表面位置变化：在向外凸出的**尖端与棱角处**（Sharp outward points and edges，曲率半径小），面电荷密度 $|\sigma|$ 及紧贴表面外侧的场强 $|\vec{E}|$ **极大**；而在平坦处较小，向内凹陷的拐角处（Inward corners）极小。

---

## 2 空腔导体与静电屏蔽 (Conductors with Cavities and Electrostatic Shielding)

### 2.1 空腔内无电荷的情形 (Empty Cavity)

考察内部含有一个空腔（Empty cavity）的孤立带电导体（Example 5.1）：

1. **内表面总净电荷为零**：在金属实体内部紧贴空腔内壁作一个完全包围空腔的高斯面 $\Sigma$。由于金属内部处处 $\vec{E} = \vec{0}$，穿过 $\Sigma$ 的电通量 $\oint_\Sigma \vec{E}\cdot d\vec{A} = 0$，由高斯定理知 $Q_{\text{enc}} = 0$，故空腔内壁上的总净电荷必为零。
2. **内表面处处无电荷（$\sigma_{\text{inner}} = 0$）且空腔内处处无电场（$\vec{E}_{\text{cavity}} = \vec{0}$）**：
   空腔内部无体积电荷（$\rho = 0$），电势满足拉普拉斯方程 $\nabla^2 V = 0$；同时空腔内壁属于同一个等势体导体，电势恒为常数 $V = V_0$。根据**唯一性定理**（Uniqueness Theorem），空腔内部唯一满足边界条件的解就是常函数 $V(\vec{r}) \equiv V_0$。因此空腔内部处处 $\vec{E} = -\nabla V = \vec{0}$，进而跨接内壁作微小高斯药盒可知内壁每一点的面电荷密度均为 $\sigma = 0$！所有净电荷完全分布在导体的**最外表面**上。
   *思维实验（Lecture 5 Slide 7）*：若将空腔不断扩大直至吞噬整个金属壳（仅保留原本外表面上的电荷分布），空间各处的电场丝毫不变，这说明内部零电场是由外表面电荷自身精妙排布抵消的结果。

**对外部电场的屏蔽（法拉第笼 Faraday Cage）**：上述结论表明，无论导体外部存在多么强的静电场（如雷暴天气 Thunderstorm），空腔内部（只要内部无源电荷）的电场恒严格为零（因此雷雨天待在全金属车身的轿车内是安全的，但不适用于敞篷车或塑料/乐高车）。

### 2.2 空腔内有电荷与接地屏蔽 (Cavity with Charge & Grounding)

设孤立导体原本带有总净电荷 $Q_c$（若原本中性则 $Q_c = 0$），现将一个电荷量为 $+Q$ 的点电荷放入其空腔内部（Example 5.2）：

1. **内外表面感应电荷定量关系**：
   仍取完全位于金属实体内部、包围空腔的高斯面 $\Sigma$。因金属内 $\vec{E} = \vec{0}$，必有 $Q_{\text{enc}} = Q + q_{\text{inner}} = 0$，因此**空腔内壁必然感应出总量为 $q_{\text{inner}} = -Q$ 的异号电荷**！
   再由导体整体电荷守恒（$q_{\text{inner}} + q_{\text{outer}} = Q_c$），**导体外表面必然带有总量为 $q_{\text{outer}} = Q_c + Q$ 的电荷**（若导体原本电中性，则内壁为 $-Q$，外壁为 $+Q$）。
2. **偏心放置时的对称性解耦（Lecture 5 Slides 17–19 重点辨析）**：
   若球形金属壳空腔内的点电荷偏离球心（Off-center，例如位于距球心 $R/2$ 处），则：
   - **空腔内壁（Inner wall）**：感应电荷虽然总量恒为 $-Q$，但因点电荷偏心吸引，**分布是不均匀的**（靠近点电荷一侧更密集）；内壁感应电荷的作用是与腔内点电荷共同在金属壳实体及外部空间产生完全相消的零电场。
   - **导体外壁（Outer wall）**：由于金属实体内部 $\vec{E} = \vec{0}$ 彻底阻断了空腔内部与外部的电力联系，在外部无其他电荷时，外壁上的电荷 $Q_c + Q$ 完全不受腔内点电荷位置的影响，依然保持**球对称均匀分布**！
3. **接地屏蔽（Grounding）**：
   将导体与大地相连称为**接地**（Grounding）。地球是一个巨大的导体库，其电势固定为无穷远参考零电势 $V = 0$。当包裹着腔内电荷 $+Q$ 的导体壳接地且外部无其他电荷时，导体壳电势变为 $V = 0$（与无穷远处相同），故壳外空间处处 $V = 0, \ \vec{E} = \vec{0}$，外表面上的电荷 $+Q$ 全部流入大地（$q_{\text{outer}} = 0$），从而将空腔内部电荷的电场完全屏蔽在空腔之内。

| 空腔导体状态（设导体原本中性，腔内偏心放置 $+q$） | 空腔内壁电荷 $q_{\text{inner}}$ | 球壳外壁电荷 $q_{\text{outer}}$ | 球壳外部空间电场 $\vec{E}(r > b)$ |
| :--- | :--- | :--- | :--- |
| **孤立不接地（Isolated, ungrounded）** | $-q$（**非均匀分布**） | $+q$（**均匀分布**） | $\vec{E} = \dfrac{q}{4\pi\epsilon_0 r^2}\hat{r}$（等效于球心点电荷） |
| **外壳接地（Grounded，$V_{\text{shell}} = 0$）** | $-q$（**非均匀分布，腔内场不变**） | $0$（流入大地） | $\vec{E} = \vec{0}$（对腔内电荷实现向外屏蔽） |

---

## 3 唯一性定理与镜像法 (Uniqueness Theorem and Method of Image Charges)

### 3.1 理论基础与镜像法三条基本准则

在导体外部的无电荷空间区域内，电势满足拉普拉斯方程 $\nabla^2 V = 0$。该方程具有两个核心数学性质：

1. **唯一性（Uniqueness Theorem）**：在给定电荷分布的区域内，如果某个电势函数满足拉普拉斯/泊松方程，并且满足全部**边界条件**（Boundary conditions：给定各边界面及无穷远处的电势值，或给定各孤立导体的等势条件及所围总电荷量），则该电势就是空间**唯一真实**的物理电势。
2. **线性叠加性（Linearity）**：多个解的线性组合依然满足方程，因此可以通过逐个边界添加虚拟电荷来叠加构造解。

**镜像法（Method of Image Charges）**正是利用唯一性定理，在所求解区域**外部**（通常在导体内部）放置一个或几个虚拟的**镜像电荷**（Image charges），用以替代导体表面未知的感应电荷分布。使用镜像法必须严格遵守以下**三条基本准则**（Rules of Image Charges）：

1. **准则 1（禁入研究区域）**：镜像电荷**绝不能放置在待求解场分布的物理区域内部**（否则会改变该区域内的源电荷密度 $\rho$，使泊松方程本身发生改变）。
2. **准则 2（复现边界条件）**：镜像系统与原物理系统在待求解区域的所有边界上必须具有完全相同的边界条件（例如使接地导体表面所在位置满足等势条件 $V = 0$；若导体孤立且给定总电荷，则需使该表面为等势面，且闭合面内包围的镜像电荷与真实电荷之和等于原系统的总电荷）。
3. **准则 3（多镜像叠加）**：当存在多个导电边界或孤立带电导体时，可利用线性叠加原理同时引入多个镜像电荷。

### 3.2 模型一：无限大接地导体平面上方的点电荷 (Point Charge Above a Grounded Plane)

设无限大接地导体平面位于 $z = 0$（边界条件 $V(x, y, 0) = 0$，且下半空间 $z < 0$ 在导体内恒有 $\vec{E} = \vec{0}$），点电荷 $+q$ 位于上方 $(0, 0, d)$ 处（Example 5.3）：

1. **镜像系统构造与上半空间电势**：
   去掉导体平面，在下半空间对称位置 $(0, 0, -d)$ 放置一个镜像电荷 **$-q$**。该辅助系统在上半空间 $(z > 0)$ 的电荷分布与原系统完全相同，且在 $z = 0$ 平面及无穷远处均满足 $V = 0$。由唯一性定理，上半空间的电势与电场唯一确定为：
   $$
   V(x, y, z > 0) = \frac{q}{4\pi\epsilon_0}\left[ \frac{1}{\sqrt{x^2 + y^2 + (z - d)^2}} - \frac{1}{\sqrt{x^2 + y^2 + (z + d)^2}} \right]
   $$
2. **导体表面外侧电场与感应面电荷密度 $\sigma(x, y)$**：
   在紧贴导体平面上方 $z = 0^+$ 处，电场垂直于平面（只有 $z$ 分量）：
   $$
   \vec{E}(x, y, z = 0^+) = -\hat{z}\left.\frac{\partial V}{\partial z}\right|_{z=0} = -\hat{z}\frac{qd}{2\pi\epsilon_0(x^2 + y^2 + d^2)^{3/2}}
   $$
   由导体表面边界关系 $\sigma = \epsilon_0 \hat{n}\cdot\vec{E}(z=0^+) = \epsilon_0 E_z(x, y, 0^+)$，立即得到导体平面上的**感应面电荷密度**：
   $$
   \sigma(x, y) = -\frac{qd}{2\pi(x^2 + y^2 + d^2)^{3/2}}
   $$
   在极坐标 $(r, \phi)$ 下对整个平面积分：$\int_0^\infty \sigma(r) 2\pi r\,dr = -qd\int_0^\infty (r^2+d^2)^{-3/2}r\,dr = -q$，即导体平面上感应出的总电荷恰好等于镜像电荷 $-q$。
3. **相互作用力与静电能减半机制（Lecture 5 Slide 25 & Exercise 5.9）**：
   - 点电荷 $+q$ 受到导体平面的吸引力等于位于 $(0, 0, -d)$ 处的镜像电荷 $-q$ 对它的库仑引力（间距为 $2d$）：
     $$
     \vec{F} = -\frac{1}{4\pi\epsilon_0}\frac{q^2}{(2d)^2}\hat{z} = -\frac{q^2}{16\pi\epsilon_0 d^2}\hat{z}
     $$
   - 将 $+q$ 从无穷远移至 $z = d$ 处，系统的静电势能为：
     $$
     U = -\int_\infty^d F_z(z')\,dz' = \int_\infty^d \frac{q^2}{16\pi\epsilon_0 z'^2}\,dz' = -\frac{1}{4\pi\epsilon_0}\frac{q^2}{4d} = \frac{1}{2}\left(-\frac{1}{4\pi\epsilon_0}\frac{q^2}{2d}\right)
     $$
     该能量**恰好是没有导体时将 $+q$ 与 $-q$ 移至相距 $2d$ 所需能量的一半**！物理原因在于：双点电荷系统中上下整个全空间都存在电场；而在接地导体板系统中，电场仅存在于上半空间（$z > 0$），下半空间（$z < 0$）内部 $\vec{E} = \vec{0}$ 不储存任何电场能（从做功角度看，只移动了真实电荷 $+q$，而导体上的感应电荷是在 $V = 0$ 的等势面上移动的，不做功）。

### 3.3 模型二：接地导体球壳外的点电荷 (Point Charge Outside a Grounded Sphere)

设半径为 $R$ 的接地导体球壳中心位于原点（球面边界条件 $V(r = R) = 0$），点电荷 $+Q$ 位于球外 $(d, 0, 0)$ 处，其中 $d > R$（Example 5.4）：

1. **镜像电荷参数推导**：
   在球壳内部 $x$ 轴上 $(d', 0, 0) \ (d' < R)$ 放置一个镜像电荷 $-q$。令球面 $x^2 + y^2 + z^2 = R^2$ 上处处满足 $V = 0$：
   $$
   \frac{Q}{\sqrt{(x - d)^2 + y^2 + z^2}} - \frac{q}{\sqrt{(x - d')^2 + y^2 + z^2}} = 0
   $$
   两边平方移项并展开：
   $$
   (Q^2 - q^2)(x^2 + y^2 + z^2) + 2(q^2 d - Q^2 d')x = q^2 d^2 - Q^2 d'^2
   $$
   要使该方程与球面方程 $x^2 + y^2 + z^2 = R^2$（不含 $x$ 一次项）完全重合，必须令 $x$ 的系数为零且常数项之比等于 $R^2$：
   $$
   \begin{cases}
   q^2 d - Q^2 d' = 0 \implies d' = \dfrac{q^2}{Q^2}d \\
   R^2(Q^2 - q^2) = q^2 d^2 - Q^2 d'^2
   \end{cases}
   $$
   消去 $d'$ 并排除平凡解 $q=Q, d'=d$（违背准则 1），解得**球面镜像电荷的唯一参数**：
   $$
   q = \frac{R}{d}Q \quad (\text{即镜像电荷为 } q' = -\frac{R}{d}Q), \qquad d' = \frac{R^2}{d} < R
   $$
2. **推广：孤立不接地且带总电荷 $Q_0$ 的导体球（Exercise 5.3）**：
   若导体球不接地，而是孤立且携带总电荷 $Q_0$，则由叠加原理（准则 2 与准则 3），需在球内放置**两个镜像电荷**：
   - 第一个镜像电荷 $q_1' = -\frac{R}{d}Q$ 位于 $(d', 0, 0) = \left(\frac{R^2}{d}, 0, 0\right)$，使球面保持为 $V = 0$ 的等势面；
   - 第二个镜像电荷 $q_2' = Q_0 - q_1' = Q_0 + \frac{R}{d}Q$ 放置在**球心 $(0, 0, 0)$** 处：由于它到球面各点距离均为 $R$，它在球面上产生常电势（不破坏球面的等势性），且使高斯球面内包围的总镜像电荷 $q_1' + q_2' = Q_0$ 恰好等于原导体球的总电荷！

---

## 4 Chapter 5 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 5.1 & 5.2: Concentric Conducting Shells & Two Parallel Metal Plates（同心导体球壳与双平行金属板四表面电荷分配）</summary>

**Problem Statement:**
- **Ex 5.1**: A conducting spherical ball of radius $R_1$ is placed concentrically inside a conducting spherical shell with inner radius $R_2$ and outer radius $R_3 \ (R_1 < R_2 < R_3)$. The inner ball carries charge $Q_1$ and the outer shell carries total charge $Q_2$. Find the electric field in all regions ($r < R_1$, $R_1 < r < R_2$, $R_2 < r < R_3$, $r > R_3$) and the surface charge density on each surface.
- **Ex 5.2**: Two isolated parallel metal plates of the same area $A$ carry charges $Q_1$ and $Q_2$. There are no other charges and no external field. Assume that the plates are large enough that edge effects can be neglected. (a) Prove that the charge surface densities on the two facing surfaces are equal in magnitude but opposite in sign, and the charge surface densities on the two outward-facing surfaces are equal in magnitude and same in sign. (b) Calculate the total charge of each surface.

---

**中文解析：**

**1. 同心导体球与导体球壳的电荷及场强分布（Exercise 5.1）**：
由静电平衡条件与球对称性：
- 内球 $r = R_1$ 表面带有电荷 $q_1 = Q_1$；
- 在外球壳实体内部 $R_2 < r < R_3$ 取同心球形高斯面，因导体内 $\vec{E} = \vec{0}$，故外球壳内表面 $r = R_2$ 必感应出 $q_2 = -Q_1$；
- 由外球壳电荷守恒，外球壳外表面 $r = R_3$ 带有电荷 $q_3 = Q_1 + Q_2$。

因此三个表面的面电荷密度分别为：

$$
\sigma_1 = \frac{Q_1}{4\pi R_1^2}, \qquad \sigma_2 = -\frac{Q_1}{4\pi R_2^2}, \qquad \sigma_3 = \frac{Q_1 + Q_2}{4\pi R_3^2}
$$

四个区域内的径向电场强度 $\vec{E}(r)$ 分别为：

$$
\vec{E}(\vec{r}) = \begin{cases}
\vec{0}, & r < R_1 \text{ 或 } R_2 < r < R_3, \\
\dfrac{Q_1}{4\pi\epsilon_0 r^2}\hat{r}, & R_1 < r < R_2, \\
\dfrac{Q_1 + Q_2}{4\pi\epsilon_0 r^2}\hat{r}, & r > R_3.
\end{cases}
$$

---

**2. 两块孤立平行带电金属板的四表面电荷分配定律（Exercise 5.2，高频必考模型）**：
设左板（带电 $Q_1$）的左、右表面面电荷密度分别为 $\sigma_L, \sigma_1$，右板（带电 $Q_2$）的左、右表面面电荷密度分别为 $\sigma_2, \sigma_R$（即 $\sigma_1, \sigma_2$ 为相对的内表面，$\sigma_L, \sigma_R$ 为朝外的外表面）。

- **(a) 证明内表面等大异号、外表面等大同号**：
  1. 作一个圆柱形高斯药盒，使其左右两个底面分别位于左金属板实体内部和右金属板实体内部（包围两个相对的内表面 $\sigma_1$ 与 $\sigma_2$）。由于两金属板内部均有 $\vec{E} = \vec{0}$，穿过该高斯面的总通量为零，故高斯面内净电荷为零：
     $$
     (\sigma_1 + \sigma_2)A = 0 \implies \sigma_2 = -\sigma_1
     $$
     即两个相对内表面的面电荷密度必等大异号！
  2. 考察左金属板内部任意一点的合电场（由四个无限大均匀带电平面共同叠加产生，每个平面在两侧产生 $\frac{\sigma_i}{2\epsilon_0}$ 的场）。以向右为正方向，左板内部点位于 $\sigma_L$ 右侧、$\sigma_1, \sigma_2, \sigma_R$ 左侧，故合场强为：
     $$
     E_{\text{in, 1}} = \frac{\sigma_L}{2\epsilon_0} - \frac{\sigma_1}{2\epsilon_0} - \frac{\sigma_2}{2\epsilon_0} - \frac{\sigma_R}{2\epsilon_0} = 0
     $$
     将 $\sigma_2 = -\sigma_1$ 代入上式，中间两项抵消，立即得到：
     $$
     \sigma_L - \sigma_R = 0 \implies \sigma_L = \sigma_R
     $$
     即两个朝外的外表面的面电荷密度必等大同号！
- **(b) 计算四个表面的具体电荷量**：
  由两板各自的电荷守恒：$q_L + q_1 = Q_1$，$q_2 + q_R = Q_2$。结合 $q_1 + q_2 = 0$ 与 $q_L = q_R$，将两式相加得 $2q_L = Q_1 + Q_2$，故四个表面的总电荷分别为：
  $$
  q_L = q_R = \frac{Q_1 + Q_2}{2}, \qquad q_1 = -q_2 = \frac{Q_1 - Q_2}{2}
  $$

</details>

<details markdown="1">
<summary>Exercise 5.3 & 5.4: Isolated Sphere Image Method & 90-Degree Corner Wall Images（孤立带电球双镜像法与直角导体墙三镜像法）</summary>

**Problem Statement:**
- **Ex 5.3**: Consider again the example of a point charge $Q$ located outside a thin spherical conducting shell of radius $R$ at distance $d$ from the center. This time, the spherical shell is not grounded, and instead it has a total charge of $Q_0$. Calculate the force exerted on the point charge by the shell.
- **Ex 5.4**: A point charge $Q$ is located at $(a, a, 0)$, where $a > 0$. A grounded conductor fills the whole region where $x < 0$ or $y < 0$ (or both), so that the charge lies in the empty region $x > 0, y > 0$. Calculate the force exerted on the point charge by the conductor.

---

**中文解析：**

**1. 孤立带电导体球壳对外部点电荷的作用力（Exercise 5.3）**：
如 §3.3 所述，为同时满足球面 $r = R$ 为等势面且球壳总电荷为 $Q_0$ 的边界条件，需在球内设置两个镜像电荷：
1. 在 $(d', 0, 0) = \left(\frac{R^2}{d}, 0, 0\right)$ 处放置 $q_1' = -\frac{R}{d}Q$（该电荷与真实电荷 $Q$ 共同使 $r = R$ 球面电势处处为 $0$）；
2. 在球心 $(0, 0, 0)$ 处放置 $q_2' = Q_0 - q_1' = Q_0 + \frac{R}{d}Q$（使球面电势整体抬升至常数 $V_0 = \frac{Q_0 + RQ/d}{4\pi\epsilon_0 R}$，且保证高斯球面内总电荷为 $Q_0$）。

根据库仑定律，球壳对位于 $(d, 0, 0)$ 处的点电荷 $Q$ 施加的静电力等于两个镜像电荷对 $Q$ 作用力的叠加（沿径向 $\hat{r}$ 向外为正）：

$$
\vec{F} = \frac{Q}{4\pi\epsilon_0}\left[ \frac{q_2'}{d^2} + \frac{q_1'}{(d - d')^2} \right]\hat{r} = \frac{Q}{4\pi\epsilon_0}\left[ \frac{Q_0 + \frac{R}{d}Q}{d^2} - \frac{\frac{R}{d}Q}{\left(d - \frac{R^2}{d}\right)^2} \right]\hat{r} = \frac{Q}{4\pi\epsilon_0 d^2}\left[ Q_0 - \frac{QdR^3(2d^2 - R^2)}{(d^2 - R^2)^2} \right]\hat{r}
$$

---

**2. 直角相交接地导体墙（第一象限角域）的三镜像电荷法（Exercise 5.4）**：
真实电荷 $+Q$ 位于 $(a, a, 0)$。为了使半平面 $x = 0 \ (y \ge 0)$ 和 $y = 0 \ (x \ge 0)$ 上同时满足 $V = 0$，仅靠两个镜像电荷是不够的（因为针对 $x=0$ 的镜像会破坏 $y=0$ 的零电势），必须按棋盘格对称放置在其余三个象限中设置**三个镜像电荷**：
- 在第二象限 $(-a, a, 0)$ 放置 **$-Q$**（距离为 $2a$，方向沿 $-\hat{x}$）；
- 在第四象限 $(a, -a, 0)$ 放置 **$-Q$**（距离为 $2a$，方向沿 $-\hat{y}$）；
- 在第三象限 $(-a, -a, 0)$ 放置 **$+Q$**（对角距离为 $2\sqrt{2}a$，斥力方向沿 $\frac{\hat{x} + \hat{y}}{\sqrt{2}}$）。

对位于 $(a, a, 0)$ 的 $+Q$ 进行矢量力合成：
- 两个 $-Q$ 的吸引力合力为：$\vec{F}_{12} = -\frac{Q^2}{4\pi\epsilon_0 (2a)^2}(\hat{x} + \hat{y}) = -\frac{Q^2}{16\pi\epsilon_0 a^2}(\hat{x} + \hat{y})$；
- 对角 $+Q$ 的排斥力为：$\vec{F}_3 = +\frac{Q^2}{4\pi\epsilon_0 (2\sqrt{2}a)^2}\left(\frac{\hat{x} + \hat{y}}{\sqrt{2}}\right) = +\frac{Q^2}{32\sqrt{2}\pi\epsilon_0 a^2}(\hat{x} + \hat{y})$。

相加即得导体对点电荷 $Q$ 的总静电力：

$$
\vec{F} = -\frac{(4 - \sqrt{2})Q^2}{64\pi\epsilon_0 a^2}(\hat{x} + \hat{y})
$$

</details>

<details markdown="1">
<summary>Exercise 5.5 & 5.6: Off-Center Cavity Charge & Grounded Sphere Inside Charged Shell（偏心空腔电荷与带电绝缘球壳内的接地导体球）</summary>

**Problem Statement:**
- **Ex 5.5**: A neutral conducting spherical shell, centered at the origin, has inner radius $a$ and outer radius $b$ ($0 < a < b$). A point charge $q > 0$ is fixed inside the cavity at a distance $s$ from the center ($0 < s < a$). (a) Find the total charge on the inner surface and on the outer surface of the shell. Is either of these charges spread uniformly over its surface? Find $\vec{E}$ for $r > b$. (b) The shell is now connected to the ground. Find the charge on the outer surface and $\vec{E}$ for $r > b$. Does the electric field inside the cavity change?
- **Ex 5.6**: A conducting ball of radius $a$ is centered at the origin and connected to the ground ($V = 0$). It is surrounded by a thin nonconducting spherical shell of radius $b > a$, also centered at the origin, which carries a fixed total charge $Q > 0$ spread uniformly over its surface. (a) Find the total charge $q_g$ that flows onto the ball from the ground, and the surface charge density $\sigma_g$ on the ball. (b) Find the electric field $\vec{E}$ in the three regions $r < a$, $a < r < b$ and $r > b$.

---

**中文解析：**

**1. 偏心空腔点电荷在球壳接地前后的对比（Exercise 5.5）**：

- **(a) 球壳孤立中性时**：
  内表面总电荷为 $q_{\text{inner}} = -q$（因点电荷偏离球心 $s > 0$，内表面电荷分布**不均匀**）；
  外表面总电荷为 $q_{\text{outer}} = +q$（因金属壳内部 $\vec{E} = \vec{0}$ 屏蔽了内部非对称性，外表面电荷呈**球对称均匀分布**）。
  故在球壳外部 $r > b$ 处，电场等效于中心点电荷：$\vec{E}(\vec{r}) = \dfrac{q}{4\pi\epsilon_0 r^2}\hat{r}$。
- **(b) 球壳接地后**：
  外表面电势变为 $V = 0$，外表面电荷全部流入大地，故 $q_{\text{outer}} = 0$，且球壳外部 $r > b$ 处电场变为 $\vec{E} = \vec{0}$。
  **空腔内部的电场完全不会改变**！因为无论球壳是否接地，空腔内壁始终是同一个等势面（电势常数值的平移不影响 $-\nabla V$），内壁感应电荷分布保持原样。

---

**2. 均匀带电绝缘球壳内部包裹接地导体球（Exercise 5.6，经典等势叠加法）**：

- **(a) 求从大地流入导体球的电荷 $q_g$**：
  由球对称性，流入导体球的电荷 $q_g$ 均匀分布在半径为 $a$ 的球面上。利用球壳电势叠加公式（以无穷远为电势零点），中心导体球（半径 $a$）的电势等于其自身电荷 $q_g$ 产生的表面电势 $\frac{q_g}{4\pi\epsilon_0 a}$ 与外部半径为 $b$ 的带电球壳 $Q$ 在其内部产生的常电势 $\frac{Q}{4\pi\epsilon_0 b}$ 之和。由于导体球接地（$V(a) = 0$），必有：
  $$
  V(a) = \frac{1}{4\pi\epsilon_0}\left(\frac{q_g}{a} + \frac{Q}{b}\right) = 0 \implies q_g = -\frac{a}{b}Q
  $$
  导体球表面的面电荷密度为 $\sigma_g = \dfrac{q_g}{4\pi a^2} = -\dfrac{Q}{4\pi a b}$。
- **(b) 三个区域的电场分布 $\vec{E}$**：
  由同心球形高斯面及高斯定理，直接写出各区域场强：
  $$
  \vec{E}(\vec{r}) = \begin{cases}
  \vec{0}, & r < a \quad (\text{导体球内部}), \\
  -\dfrac{aQ}{4\pi\epsilon_0 b r^2}\hat{r}, & a < r < b \quad (\text{仅包围 } q_g = -\frac{a}{b}Q), \\
  \dfrac{Q(1 - a/b)}{4\pi\epsilon_0 r^2}\hat{r}, & r > b \quad (\text{包围总电荷 } Q + q_g).
  \end{cases}
  $$

</details>

<details markdown="1">
<summary>Exercise 5.7, 5.8 & 5.9: Electrostatic Pressure, Connected Spheres & Grounded Plane Energy（静电压强、双球相连尖端效应与接地平面能量分析）</summary>

**Problem Statement:**
- **Ex 5.7**: Just outside a conductor in equilibrium the electric field is $(\sigma/\epsilon_0)\hat{n}$; inside it is zero. (a) Treat a small patch of the surface, of area $\Delta A$, as a flat, uniformly charged sheet. Find the field that all the *other* charges produce at the patch, and show that the electric force on the patch's charge is $\sigma^2\Delta A/(2\epsilon_0)\hat{n}$ whatever the sign of $\sigma$. (b) An isolated conducting sphere of radius $R$ carries total charge $Q$. Find the electric force on the charge of its upper half ($z > 0$).
- **Ex 5.8**: Two conducting spheres of radii $R_1 > R_2$, far apart, are joined by a long thin conducting wire and carry total charge $Q > 0$. (a) Find the charges $Q_1$ and $Q_2$ on the two spheres. (b) Find the ratios $\sigma_1/\sigma_2$ and $E_1/E_2$. On which sphere is the field stronger? What does this suggest about the field near a sharp point?
- **Ex 5.9**: A point charge $q > 0$ is held at $(0, 0, d)$ above an infinite grounded conducting plane $z = 0$. (a) Find $\sigma(x, y)$, show the total induced charge is $-q$, and find the radius $r_0$ of the circle $x^2 + y^2 = r_0^2$ that contains half of it. (b) Find the work an external agent must do to move the charge slowly from $z = d$ to infinity, compare with separating $q$ and $-q$ from $2d$ to infinity, and explain why they differ.

---

**中文解析：**

**1. 导体表面的静电压强（Electrostatic Pressure）与半球张力（Exercise 5.7，必考重点）**：

- **(a) 为什么要扣除面元自身的电场？**
  面元 $\Delta A$ 上的电荷不能对自己施力，作用于面元电荷 $\Delta q = \sigma\Delta A$ 上的电场只是**除该面元以外的其余所有电荷**产生的电场 $\vec{E}_{\text{other}}$。
  将无穷小面元视为无限大均匀带电薄板，它自身在紧贴外侧产生 $+\frac{\sigma}{2\epsilon_0}\hat{n}$ 的场，在紧贴内侧产生 $-\frac{\sigma}{2\epsilon_0}\hat{n}$ 的场。由叠加原理：
  $$
  \begin{cases}
  \vec{E}_{\text{out}} = \vec{E}_{\text{other}} + \dfrac{\sigma}{2\epsilon_0}\hat{n} = \dfrac{\sigma}{\epsilon_0}\hat{n} \\
  \vec{E}_{\text{in}} = \vec{E}_{\text{other}} - \dfrac{\sigma}{2\epsilon_0}\hat{n} = \vec{0}
  \end{cases} \implies \vec{E}_{\text{other}} = \frac{\sigma}{2\epsilon_0}\hat{n}
  $$
  因此，面元所受的向外静电力（及单位面积所受的**静电压强** $P = \Delta F/\Delta A$）为：
  $$
  \Delta\vec{F} = (\sigma\Delta A)\vec{E}_{\text{other}} = \frac{\sigma^2}{2\epsilon_0}\Delta A\,\hat{n} \implies P = \frac{\sigma^2}{2\epsilon_0} = \frac{1}{2}\epsilon_0 E^2
  $$
  由于 $\sigma^2 > 0$，无论表面带正电还是带负电，导体表面所受静电力**永远沿外法线 $\hat{n}$ 向外拉伸表面**！
- **(b) 带电导体球下半球对上半球的排斥力**：
  球面面电荷密度为 $\sigma = \frac{Q}{4\pi R^2}$。由轴对称性，上半球（$0 \le \theta \le \pi/2$）所受合力沿 $+z$ 方向。利用 $\hat{n}\cdot\hat{z} = \cos\theta$ 及球面面元 $dA = 2\pi R^2\sin\theta\,d\theta$ 积分：
  $$
  F_z = \int_{\text{upper}} \frac{\sigma^2}{2\epsilon_0}\cos\theta\,dA = \frac{\sigma^2}{2\epsilon_0}(2\pi R^2) \int_0^{\pi/2} \sin\theta\cos\theta\,d\theta = \frac{\pi R^2 \sigma^2}{2\epsilon_0} = \frac{Q^2}{32\pi\epsilon_0 R^2}
  $$
  因为上半球电荷内部之间的相互作用力内力之和为零，这一净力完全是由下半球的电荷对上半球施加的排斥力。

---

**2. 细导线连接的两个远距导体球与尖端效应模型（Exercise 5.8）**：

- **(a)** 两球通过导线相连构成同一个等势体，且相距极远互不影响，故两球表面电势相等：
  $$
  V_1 = V_2 \implies \frac{Q_1}{4\pi\epsilon_0 R_1} = \frac{Q_2}{4\pi\epsilon_0 R_2} \implies \frac{Q_1}{Q_2} = \frac{R_1}{R_2}
  $$
  结合总电荷守恒 $Q_1 + Q_2 = Q$，解得：
  $$
  Q_1 = \frac{R_1}{R_1 + R_2}Q, \qquad Q_2 = \frac{R_2}{R_1 + R_2}Q
  $$
- **(b)** 计算面电荷密度之比与表面电场强度之比：
  $$
  \frac{\sigma_1}{\sigma_2} = \frac{Q_1 / (4\pi R_1^2)}{Q_2 / (4\pi R_2^2)} = \frac{R_1}{R_2} \cdot \frac{R_2^2}{R_1^2} = \frac{R_2}{R_1}, \qquad \frac{E_1}{E_2} = \frac{\sigma_1 / \epsilon_0}{\sigma_2 / \epsilon_0} = \frac{R_2}{R_1}
  $$
  由于 $R_1 > R_2$，故 **$\sigma_2 > \sigma_1$ 且 $E_2 > E_1$**，即**半径较小的小球表面电场更强**！将不规则导体的尖端视为曲率半径 $R_2$ 极小的球面，这直观解释了为什么导体尖端处的面电荷密度和局部电场强度会变得极高（尖端放电原理）。

---

**3. 接地平面感应电荷半径与移走点电荷的外力功（Exercise 5.9）**：

- **(a)** 由 §3.2 知 $\sigma(r) = -\frac{qd}{2\pi(r^2 + d^2)^{3/2}}$（其中 $r = \sqrt{x^2 + y^2}$）。在半径为 $r_0$ 的圆盘内包含的感应电荷量为：
  $$
  q(r_0) = \int_0^{r_0} \sigma(r) 2\pi r\,dr = -qd \int_0^{r_0} \frac{r\,dr}{(r^2 + d^2)^{3/2}} = -qd\left[-\frac{1}{\sqrt{r^2 + d^2}}\right]_0^{r_0} = -q\left(1 - \frac{d}{\sqrt{r_0^2 + d^2}}\right)
  $$
  当 $r_0 \to \infty$ 时，$q(\infty) = -q$。令 $q(r_0) = -\frac{1}{2}q$，解得包含一半感应电荷的圆半径为：
  $$
  1 - \frac{d}{\sqrt{r_0^2 + d^2}} = \frac{1}{2} \implies \sqrt{r_0^2 + d^2} = 2d \implies r_0 = \sqrt{3}\,d
  $$
- **(b)** 当真实电荷位于 $(0, 0, z)$ 时，其镜像电荷位于 $(0, 0, -z)$，两者间距为 $2z$（随 $z$ 动态同步变化），真实电荷所受向下的吸引力为 $F_{\text{elec}} = -\frac{q^2}{4\pi\epsilon_0(2z)^2} = -\frac{q^2}{16\pi\epsilon_0 z^2}$。因此外力将其从 $z = d$ 缓慢移至 $\infty$ 所需做的功为：
  $$
  W_{\text{ext}} = \int_d^\infty \frac{q^2}{16\pi\epsilon_0 z^2}\,dz = \frac{q^2}{16\pi\epsilon_0 d} = \frac{1}{4\pi\epsilon_0}\frac{q^2}{4d}
  $$
  而在无导体情况下将相距 $2d$ 的 $+q$ 与 $-q$ 拉开至无穷远所需的外力功为 $W_{\text{two charges}} = \frac{1}{4\pi\epsilon_0}\frac{q^2}{2d} = 2W_{\text{ext}}$。两者相差一倍的原因在于：在双点电荷问题中，需要将 $+q$（向上移 $d \to \infty$）和 $-q$（向下移 $-d \to -\infty$）两个真实电荷都拉开做功（或者说全空间上下两半均储有电场能）；而在接地导体板问题中，只有上半空间 $z > 0$ 存在真实电荷与电场，外力只需对上方的 $+q$ 做功，下方导体内的镜像电荷只是数学虚构。

</details>