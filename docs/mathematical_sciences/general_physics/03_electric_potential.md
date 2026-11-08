# Chapter 3: The Electrostatic Potential（静电势）

!!! abstract
    General Physics II (Electromagnetism) | 第三章课堂与讲义笔记
    
    参考：
    
    - Lecture 3: *The Electrostatic Potential* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 3: *Electrostatic Potential* & Halliday, Resnick & Krane, *Physics*, Chapter 28

## 1 电势能与静电场环路定理 (Electric Potential Energy and Conservative Field)

### 1.1 静电力的保守性与环路定理

点电荷间的库仑定律 $\vec{F}_{12} = \frac{1}{4\pi\epsilon_0}\frac{q_1 q_2}{r_{12}^2}\hat{r}_{12}$ 在数学形式上与质点间的万有引力定律 $\vec{F}_{12} = -G\frac{m_1 m_2}{r_{12}^2}\hat{r}_{12}$ 高度相似（引力恒为吸引，而库仑力可吸引可排斥）。正如万有引力是**保守力**（Conservative Force），静电力同样是保守力。

考察位于原点的点电荷 $Q$，当另一个点电荷 $q$ 从位置 $\vec{r}_1$ 移动到 $\vec{r}_2$ 时，利用球坐标下的微元关系 $\hat{r}\cdot d\vec{r} = dr$，静电力所做的功（Work done by the electrostatic force）为：

$$
W = \int_{\vec{r}_1}^{\vec{r}_2} \frac{1}{4\pi\epsilon_0} \frac{qQ}{r^2} \hat{r} \cdot d\vec{r} = \frac{qQ}{4\pi\epsilon_0} \int_{r_1}^{r_2} \frac{dr}{r^2} = \frac{1}{4\pi\epsilon_0} qQ \left(\frac{1}{r_1} - \frac{1}{r_2}\right)
$$

可以看到，功 $W$ **仅取决于初末位置 $r_1, r_2$，而与具体运动路径无关**（Path independent）。对于产生静电场 $\vec{E}(\vec{r})$ 的任意固定带电体 $O$，总可将其细分为无数个固定点电荷的叠加，因此静电场力做功恒与路径无关。写成沿任意闭合回路的线积分形式，即为**静电场环路定理**：

$$
\oint \vec{E} \cdot d\vec{l} = 0
$$

### 1.2 电势能差与机械能守恒定律

设正检验电荷 $q_0$ 在任意静电场 $\vec{E}(\vec{r})$ 中沿某路径从初位置 $i$ 移动到末位置 $f$，电场力对电荷所做的元功为 $\delta W = \vec{F}\cdot d\vec{s} = q_0\vec{E}\cdot d\vec{s}$，总功为线积分 $W = q_0\int_i^f \vec{E}\cdot d\vec{s}$。由此定义**电势能差**（Electric Potential Energy Difference）为静电力做功的负值（或外力克服静电力缓慢移动电荷所做的功 $W_{\text{ext}}$）：

$$
\Delta U \equiv U_f - U_i = -W = W_{\text{ext}} = -q_0 \int_i^f \vec{E} \cdot d\vec{s}
$$

若选定某个参考点 $O$（对于有限大小带电体系，通常取**无穷远处 Infinity**）作为电势能零点（$U_O = 0$），则检验电荷 $q_0$ 在位置 $\vec{r}$ 处的**电势能**（Electric Potential Energy）为：

$$
U(\vec{r}) = -q_0 \int_O^{\vec{r}} \vec{E}(\vec{r}') \cdot d\vec{r}' = q_0 \int_{\vec{r}}^O \vec{E}(\vec{r}') \cdot d\vec{r}'
$$

**能量守恒定律（Conservation of Mechanical Energy）**：若带电粒子在电场中运动且仅受电场力作用，由动能定理（Work-kinetic energy theorem）知动能变化量等于电场力做功 $\Delta K = K_f - K_i = W = -\Delta U$，移项即得机械能守恒方程：

$$
U_i + K_i = U_f + K_f
$$

---

## 2 电势与等势面 (Electric Potential and Equipotential Surfaces)

### 2.1 电势的定义与连续性

在电势能表达式中，$U(\vec{r})$ 与检验电荷 $q_0$ 成正比。消去 $q_0$ 后得到的比值仅由源电荷建立的静电场本身决定，称为**电势**（Electric Potential，即单位电荷所具有的电势能 Electric potential energy per unit charge）：

$$
V(\vec{r}) = \frac{U(\vec{r})}{q_0} = \int_{\vec{r}}^O \vec{E}(\vec{r}') \cdot d\vec{r}' = -\int_O^{\vec{r}} \vec{E}(\vec{r}') \cdot d\vec{r}'
$$

任意两点 $i$ 与 $f$ 之间的**电势差**（Potential Difference，即电压 Voltage）为：

$$
V_f - V_i = \frac{U_f - U_i}{q_0} = \frac{-W}{q_0} = -\int_i^f \vec{E} \cdot d\vec{s}
$$

电势 $V$ 的国际单位制（SI unit）为**伏特**（Volt，$\text{V} = \text{J/C}$），由此也导出了电场强度的常用工程单位 $\text{V/m}$（$1\text{ N/C} = 1\text{ V/m}$）。当电荷量为 $q$（含正负号）的粒子置于电势为 $V$ 的位置时，其电势能为 $U = qV$。

描述电荷相互作用与空间场效应的四个核心物理量对比如下表：

| 物理描述维度 | 矢量描述（Vector） | 标量描述（Scalar） | 相互转化关系 |
| :--- | :--- | :--- | :--- |
| **两个电荷之间的相互作用** | 静电力 $\vec{F}$（Force） | 电势能 $U$（Potential Energy） | $\Delta U = -\int \vec{F}\cdot d\vec{s}, \quad \vec{F} = -\nabla U$ |
| **源电荷在空间一点产生的场效应** | 电场强度 $\vec{E}$（Electric Field） | 电势 $V$（Electric Potential） | $\vec{E} = \dfrac{\vec{F}}{q_0}, \quad V = \dfrac{U}{q_0}, \quad U = qV$ |

!!! note "重要物理性质：电势的空间连续性（Continuity of Electric Potential）"
    由积分不等式 $|V(\vec{r}') - V(\vec{r})| = \left|-\int_{\vec{r}}^{\vec{r}'} \vec{E}\cdot d\vec{l}\right| \le \int_{\vec{r}}^{\vec{r}'} |\vec{E}|\,dl$ 可知，只要空间中的电场强度 $|\vec{E}|$ 保持有界（Bounded），当 $\vec{r}' \to \vec{r}$ 时必有 $V(\vec{r}') \to V(\vec{r})$。
    这意味着**即使在电场强度 $\vec{E}$ 发生跃变（Jump）的带电曲面上（如均匀带电球壳表面或无限大带电平板），电势 $V(\vec{r})$ 依然是连续跨过分界面的**，发生突变的仅仅是电势的空间梯度（即 $-\nabla V$）。

### 2.2 等势面 (Equipotential Surfaces)

空间中电势相等的相邻点构成的曲面 $V(\vec{r}) = V_0$ 称为**等势面**（Equipotential Surface / Isosurface of electric potential）。等势面具有以下三条核心几何与物理性质：

1. **沿等势面移动不做功**：当带电粒子在同一等势面上的任意两点间移动（或沿任意路径离开后又回到同一等势面）时，由于 $\Delta V = 0$，电场力所做的净功恒为零（$W = -q\Delta V = 0$）。
2. **电场方向指向电势降低的方向**：在匀强电场 $\vec{E}$ 中，沿电场线方向移动距离 $\Delta x$ 时有 $V_f - V_i = -\vec{E}\cdot\int_i^f d\vec{s} = -E\Delta x < 0$，故电场矢量 $\vec{E}$ 总是从高电势等势面指向低电势等势面（Points from higher potential toward lower potential）。
3. **电场线处处垂直于等势面（Orthogonality）**：
   *反证法*：假设电场 $\vec{E}$ 与等势面不垂直，则 $\vec{E}$ 必有一个平行于等势面的切向分量（Tangential component）。当检验电荷沿等势面移动时，该切向分量就会对电荷做非零功，这与“沿等势面移动不做功”的定义矛盾。因此，**电场线与电场矢量 $\vec{E}$ 在任何位置都必然垂直于该处的等势面**。

---

## 3 分立点电荷系的电势与静电能 (Discrete Charge Systems)

### 3.1 点电荷与点电荷系的电势

选取无穷远处为电势零点（$V(\infty) = 0$），将位于原点的单个点电荷电场 $\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}\hat{r}$ 代入定义式积分：

$$
V(r) = -\int_\infty^r \vec{E}(\vec{r}') \cdot d\vec{r}' = -\frac{q}{4\pi\epsilon_0} \int_\infty^r \frac{dr'}{r'^2} = \frac{1}{4\pi\epsilon_0} \frac{q}{r}
$$

其中 $r = |\vec{r}|$ 为场点到点电荷 $q$ 的距离（正电荷产生正电势，负电荷产生负电势）。

对于由 $n$ 个点电荷 $q_1, q_2, \dots, q_n$（分别位于 $\vec{r}_1, \vec{r}_2, \dots, \vec{r}_n$）组成的分立点电荷系，由叠加原理，空间位置 $\vec{r}$ 处的总电势等于各点电荷单独产生电势的**代数和**（Algebraic sum，标量直接相加，无需分解矢量）：

$$
V(\vec{r}) = \sum_{i=1}^n V_i(\vec{r}) = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^n \frac{q_i}{r_i} = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^n \frac{q_i}{|\vec{r} - \vec{r}_i|}
$$

### 3.2 电偶极子的电势 (Electric Potential of a Dipole)

设电偶极子由位于 $+\vec{d}/2$ 的 $+q$ 与位于 $-\vec{d}/2$ 的 $-q$ 组成，电偶极矩为 $\vec{p} = q\vec{d}$。计算远场位置 $\vec{r} \ (r \gg d)$ 处的电势共有两种等价方法（Example 3.1）：

**方法 1：利用点电荷系电势叠加与远场平行近似**

$$
V(\vec{r}) = V_{(+)} + V_{(-)} = \frac{1}{4\pi\epsilon_0}\left(\frac{q}{r_{(+)}} - \frac{q}{r_{(-)}}\right) = \frac{q}{4\pi\epsilon_0} \frac{r_{(-)} - r_{(+)}}{r_{(-)} r_{(+)}}
$$

其中 $r_{(\pm)} = \left|\vec{r} \mp \frac{\vec{d}}{2}\right|$。当 $r \gg d$ 时，两条连线近似平行，波程差与分母近似为（保留至领头阶）：

$$
r_{(-)} - r_{(+)} \approx d\cos\theta = \vec{d}\cdot\hat{r}, \qquad r_{(-)} r_{(+)} \approx r^2
$$

代入即得**电偶极子的远场电势公式**：

$$
V(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{p\cos\theta}{r^2} = \frac{1}{4\pi\epsilon_0} \frac{\vec{p} \cdot \hat{r}}{r^2} = \frac{1}{4\pi\epsilon_0} \frac{\vec{p} \cdot \vec{r}}{r^3}
$$

where $\theta$ 为位置矢量 $\vec{r}$ 与电偶极矩方向 $\vec{p}$ 之间的极角。

**方法 2：由电偶极子电场直接沿径向积分**

已知电偶极子电场通式为 $\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0 r^3}[3(\vec{p}\cdot\hat{r})\hat{r} - \vec{p}]$。固定极角 $\theta$ 沿径向从 $\infty$ 积分至 $r$（路径微元 $d\vec{l} = dr'\,\hat{r}$），径向分量 $\vec{E}\cdot\hat{r} = \frac{1}{4\pi\epsilon_0}\frac{2(\vec{p}\cdot\hat{r})}{r^3} = \frac{2p\cos\theta}{4\pi\epsilon_0 r^3}$，故：

$$
V(\vec{r}) = -\int_\infty^r \vec{E}\cdot d\vec{l} = -\frac{2p\cos\theta}{4\pi\epsilon_0} \int_\infty^r \frac{dr'}{r'^3} = \frac{1}{4\pi\epsilon_0} \frac{p\cos\theta}{r^2} = \frac{1}{4\pi\epsilon_0} \frac{\vec{p}\cdot\vec{r}}{r^3}
$$

### 3.3 点电荷系的相互作用势能 / 组装功 (Potential Energy of a System of Point Charges)

将原本相距无穷远（初态势能为零）的多个点电荷逐个缓慢移动到指定位置组装成点电荷系，外力所做的总功即为该系统的总静电势能 $U_{\text{tot}}$：

1. 将第 1 个电荷 $q_1$ 移至位置 $\vec{r}_1$：空间尚无其他电场，做功 $U_1 = 0$；
2. 将第 2 个电荷 $q_2$ 从无穷远移至 $\vec{r}_2$：在 $q_1$ 的电势中增加势能 $U_{12} = q_2 V_1(\vec{r}_2) = \frac{1}{4\pi\epsilon_0}\frac{q_1 q_2}{r_{12}}$；
3. 将第 3 个电荷 $q_3$ 从无穷远移至 $\vec{r}_3$：克服 $q_1, q_2$ 的电场做功，增加势能 $U_{13} + U_{23} = \frac{1}{4\pi\epsilon_0}\left(\frac{q_1 q_3}{r_{13}} + \frac{q_2 q_3}{r_{23}}\right)$；
4. **推广至 $N$ 个点电荷系统**：系统的总电势能等于**所有可能的电荷对（Every possible pair）相互作用势能之和**：
   $$
   U_{\text{tot}} = \sum_{i < j} U_{ij} = \frac{1}{4\pi\epsilon_0} \sum_{i < j} \frac{q_i q_j}{r_{ij}} = \frac{1}{2} \sum_{i=1}^N \sum_{j \neq i} \frac{1}{4\pi\epsilon_0} \frac{q_i q_j}{r_{ij}}
   $$

---

## 4 连续电荷分布的电势 (Potential Due to Continuous Charge Distributions)

### 4.1 微元积分公式与无穷远发散陷阱

对于**有限尺寸**（Finite-size）的连续带电体，将其分割为位于 $\vec{r}'$ 的无穷小电荷元 $dq(\vec{r}')$（如 $\lambda\,dl'$、$\sigma\,dS'$ 或 $\rho(\vec{r}')\,d^3r'$），以无穷远处为电势零点，位置 $\vec{r}$ 处的电势为：

$$
V = \frac{1}{4\pi\epsilon_0} \int \frac{dq}{r} \iff V(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int \frac{dq(\vec{r}')}{|\vec{r} - \vec{r}'|}
$$

!!! warning "物理陷阱：什么时候不能使用 $V = \frac{1}{4\pi\epsilon_0}\int \frac{dq}{r}$？"
    上述积分公式隐含了**选取无穷远处为电势零点（$V(\infty) = 0$）**的前提。
    如果连续电荷分布**延伸至无穷远**且电荷密度衰减得不够快（例如无限长均匀带电直导线或无限大均匀带电平板），由于无穷远处本身就存在源电荷，将单位电荷移至无穷远时电场力做功发散，导致积分 $\int \frac{dq}{r}$ **发散（Does not converge）**！
    在此类无限延伸系统中，**绝不能取无穷远为电势零点**，必须回到电势的原始线积分定义式 $V(\vec{r}) = -\int_{\vec{r}_0}^{\vec{r}} \vec{E}(\vec{r}')\cdot d\vec{r}'$，并人为指定一个**有限距离处的参考点 $\vec{r}_0$** 为电势零点。

### 4.2 两大经典连续带电体电势模型

**1. 有限长均匀带电细杆（Example 3.2: Charged Rod）**

设长度为 $L$ 的绝缘细杆沿 $y$ 轴（$[0, L]$，课件中记为 $x$ 轴）放置，均匀携带总电荷 $Q$（线电荷密度 $\lambda = \frac{Q}{L}$）。求过端点 $O$ 且垂直于细杆的直线上、距端点为 $x$（课件中记为 $d$）的点 $P$ 处的电势：

- **微元积分**：取位置 $y \to y+dy$ 处的微元 $dq = \lambda\,dy = \frac{Q}{L}dy$，到点 $P$ 的距离为 $r = \sqrt{x^2 + y^2}$。利用标准积分公式 $\int \frac{dy}{\sqrt{x^2+y^2}} = \ln\left(y + \sqrt{x^2+y^2}\right)$：
  $$
  V(x) = \frac{1}{4\pi\epsilon_0} \int_0^L \frac{\lambda\,dy}{\sqrt{x^2 + y^2}} = \frac{\lambda}{4\pi\epsilon_0} \left[\ln\left(y + \sqrt{x^2 + y^2}\right)\right]_0^L = \frac{Q}{4\pi\epsilon_0 L} \ln\left(\frac{L + \sqrt{L^2 + x^2}}{x}\right)
  $$
- **远场展开修正（$L \ll x$）**：令 $t = y/x$，利用 $(1 + t^2)^{-1/2} \approx 1 - \frac{1}{2}t^2$ 展开积分：
  $$
  \int_0^L \frac{dy}{\sqrt{x^2 + y^2}} = \int_0^{L/x} \left(1 - \frac{1}{2}t^2 + \cdots\right) dt = \frac{L}{x} - \frac{1}{6}\left(\frac{L}{x}\right)^3 + \cdots
  $$
  代入得远场近似（第一项为点电荷势，第二项为有限长度的领头阶修正）：
  $$
  V(x) \approx \frac{1}{4\pi\epsilon_0}\frac{Q}{x} - \frac{1}{24\pi\epsilon_0}\frac{QL^2}{x^3} \qquad (x \gg L)
  $$

**2. 均匀带电圆盘轴线上的电势（Example 3.3: Charged Disk）**

设半径为 $R$ 的薄圆盘均匀带电 $Q$，面电荷密度 $\sigma = \frac{Q}{\pi R^2}$。求中心轴线上距盘心为 $x > 0$（课件中记为 $z > 0$）的点 $P$ 处的电势：

- **同心细圆环分割**：取半径为 $s \to s+ds$（课件记为 $R' \to R'+dR'$）的细圆环，环上所有点到 $P$ 的距离均为 $r = \sqrt{s^2 + x^2}$，环上电荷量为 $dq = \sigma(2\pi s\,ds) = \frac{2Q}{R^2}s\,ds$。
- **一维积分求解**：
  $$
  V(x) = \frac{1}{4\pi\epsilon_0} \int_0^R \frac{\sigma(2\pi s\,ds)}{\sqrt{s^2 + x^2}} = \frac{\sigma}{4\epsilon_0} \int_0^{R^2} \frac{d(s^2)}{\sqrt{s^2 + x^2}} = \frac{\sigma}{2\epsilon_0}\left(\sqrt{R^2 + x^2} - x\right) = \frac{Q}{2\pi\epsilon_0 R^2}\left(\sqrt{R^2 + x^2} - x\right)
  $$
  当 $x \gg R$ 时，利用 $\sqrt{R^2 + x^2} - x = x\left(1 + \frac{R^2}{x^2}\right)^{1/2} - x \approx \frac{R^2}{2x}$，立即退化为点电荷电势 $V(x) \approx \frac{Q}{4\pi\epsilon_0 x}$。

---

## 5 由电势求电场与曲线积分 (From Electric Potential to Electric Field)

### 5.1 方向导数与负梯度关系 ($\vec{E} = -\nabla V$)

已知空间电势分布 $V(\vec{r})$，可以通过微分运算直接求出电场强度 $\vec{E}(\vec{r})$（这比先积分求矢量 $\vec{E}$ 往往简便得多）。

设正检验电荷 $q_0$ 在两个相邻等势面之间发生微小位移 $d\vec{s}$（长度为 $\delta s$，方向沿任意指定的 $s$ 轴，与 $\vec{E}$ 夹角为 $\theta$）。一方面，电场力做功为 $(q_0\vec{E})\cdot d\vec{s} = q_0 E\cos\theta\,\delta s$；另一方面，该功等于电势能减少量 $-q_0\,\delta V$。联立消去 $q_0$ 得：

$$
q_0 E\cos\theta\,\delta s = -q_0\,\delta V \implies E_s \equiv E\cos\theta = -\frac{\partial V}{\partial s}
$$

即：**电场矢量 $\vec{E}$ 沿任意方向 $s$ 的分量，等于电势 $V$ 沿该方向的变化率（方向导数）的负值**。

在直角坐标系 $(x, y, z)$ 中，分别取 $s$ 轴为 $x, y, z$ 轴，即可得到电场的三个直角坐标分量与矢量梯度公式：

$$
E_x = -\frac{\partial V}{\partial x}, \qquad E_y = -\frac{\partial V}{\partial y}, \qquad E_z = -\frac{\partial V}{\partial z} \iff \vec{E} = -\nabla V
$$

其中算符 $\nabla \equiv \hat{x}\dfrac{\partial}{\partial x} + \hat{y}\dfrac{\partial}{\partial y} + \hat{z}\dfrac{\partial}{\partial z}$ 称为**哈密顿算符 / 梯度算符**（Nabla / Del operator），$\nabla V$ 称为标量场 $V$ 的**梯度**（Gradient of $V$，指向 $V$ 增长最快的方向，故 $\vec{E} = -\nabla V$ 指向 $V$ 下降最快的方向且垂直于等势面）。

例如，对均匀带电圆盘轴线电势 $V(z) = \frac{\sigma}{2\epsilon_0}\left(\sqrt{z^2 + R^2} - z\right)$ 关于 $z$ 求负导数，立即复现第一章求得的轴线电场：

$$
E_z = -\frac{dV}{dz} = \frac{\sigma}{2\epsilon_0}\left[1 - \frac{z}{\sqrt{z^2 + R^2}}\right]
$$

<details markdown="1">
<summary>Appendix 3A: Line Integrals（空间有向曲线积分的参数化计算方法）</summary>

设三维空间中的有向曲线（Directed curve）$C$ 由参数方程给出：

$$
\vec{r}(t) = x(t)\hat{x} + y(t)\hat{y} + z(t)\hat{z}, \qquad t_i \le t \le t_f
$$

弧长微元为 $ds = \sqrt{\left|\frac{dx}{dt}\right|^2 + \left|\frac{dy}{dt}\right|^2 + \left|\frac{dz}{dt}\right|^2}\,dt = \left|\frac{d\vec{r}}{dt}\right|dt$，切向单位矢量为 $\hat{s} = \frac{d\vec{r}/dt}{|d\vec{r}/dt|}$。因此，矢量场 $\vec{f}(x, y, z) = f_x\hat{x} + f_y\hat{y} + f_z\hat{z}$ 沿曲线 $C$ 的线积分（Line integral）可通过以下两种等价形式计算：

$$
I = \int_C \vec{f}(x, y, z) \cdot d\vec{s} = \int_C \vec{f}\cdot\hat{s}\,ds = \int_{t_i}^{t_f} \vec{f}\big(x(t), y(t), z(t)\big) \cdot \frac{d\vec{r}}{dt}\,dt = \int_C \left(f_x\,dx + f_y\,dy + f_z\,dz\right)
$$

</details>

---

## 6 Chapter 3 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 3.1, 3.2 & 3.3: Point-Charge Work, Gradient Calculation & Charged Ring（点电荷移位做功、梯度求电场与圆环轴线偏导分析）</summary>

**Problem Statement:**
- **Ex 3.1**: Two point charges are at a distance of $2a$, and each carries a charge $q$. How much work is needed to bring them to a distance of $a$?
- **Ex 3.2**: Given the electric potential $V = V_0 \exp\left[-(x^2 + y^2 + az)/a^2\right]$, where $V_0 > 0$ is a constant potential and $a > 0$ a constant length, calculate the electric field $\vec{E}$ at $\vec{r} = (x, y, z)$.
- **Ex 3.3**: A thin ring of radius $R$, centered at the origin and lying in the $xy$ plane, carries a total charge $Q$ distributed uniformly. Take the electric potential to be zero at infinity. Compute the electric field $\vec{E}$ and the potential $V$ at the point $(0, 0, z)$ on the $z$ axis, and show that $E_z = -dV/dz$ there. Explain why $\partial V/\partial x$ and $\partial V/\partial y$ vanish on the axis, even though $V$ off the axis depends on $x$ and $y$.

---

**中文解析：**

**1. 移动两个同号点电荷所需的外力功（Exercise 3.1）**：
外力克服静电力所需的功等于系统电势能的增加量 $\Delta U = U_f - U_i$：

$$
W_{\text{ext}} = \Delta U = \frac{1}{4\pi\epsilon_0}\frac{q^2}{a} - \frac{1}{4\pi\epsilon_0}\frac{q^2}{2a} = \frac{q^2}{8\pi\epsilon_0 a}
$$

---

**2. 由给定电势函数求空间电场矢量（Exercise 3.2）**：
直接应用梯度公式 $\vec{E} = -\nabla V = -\left(\hat{x}\frac{\partial V}{\partial x} + \hat{y}\frac{\partial V}{\partial y} + \hat{z}\frac{\partial V}{\partial z}\right)$，对各坐标求偏导：

$$
\begin{aligned}
E_x &= -\frac{\partial V}{\partial x} = \frac{2x}{a^2} V_0 \exp\left(-\frac{x^2 + y^2 + az}{a^2}\right) \\
E_y &= -\frac{\partial V}{\partial y} = \frac{2y}{a^2} V_0 \exp\left(-\frac{x^2 + y^2 + az}{a^2}\right) \\
E_z &= -\frac{\partial V}{\partial z} = \frac{1}{a} V_0 \exp\left(-\frac{x^2 + y^2 + az}{a^2}\right)
\end{aligned}
$$

合并写成矢量形式为：

$$
\vec{E}(x, y, z) = \frac{V_0}{a^2}\left(2x\hat{x} + 2y\hat{y} + a\hat{z}\right)\exp\left(-\frac{x^2 + y^2 + az}{a^2}\right)
$$

---

**3. 均匀带电细圆环的轴线电势与偏导数对称性分析（Exercise 3.3）**：

- **计算轴线上的 $V(0, 0, z)$ 与 $\vec{E}(0, 0, z)$**：
  环上所有电荷微元 $dq$ 到轴线点 $(0, 0, z)$ 的距离均等于 $\sqrt{R^2 + z^2}$，故标量直接积分得：
  $$
  V(0, 0, z) = \frac{1}{4\pi\epsilon_0} \int \frac{dq}{\sqrt{R^2 + z^2}} = \frac{Q}{4\pi\epsilon_0\sqrt{R^2 + z^2}}
  $$
  由第二章结论知轴线电场为 $\vec{E}(0, 0, z) = \dfrac{Qz}{4\pi\epsilon_0(R^2 + z^2)^{3/2}}\hat{z}$。对 $V(0, 0, z)$ 关于 $z$ 求导：
  $$
  -\frac{dV}{dz} = -\frac{Q}{4\pi\epsilon_0}\left(-\frac{1}{2}\right)(R^2 + z^2)^{-3/2}(2z) = \frac{Qz}{4\pi\epsilon_0(R^2 + z^2)^{3/2}} = E_z
  $$
- **为什么轴线上 $\frac{\partial V}{\partial x} = \frac{\partial V}{\partial y} = 0$？**
  虽然偏离 $z$ 轴时电势 $V(x, y, z)$ 依赖于 $x$ 和 $y$，但由于圆环绕 $z$ 轴具有旋转对称性（以及关于 $xz, yz$ 平面的镜像偶对称性：$V(-x, y, z) = V(x, y, z)$），在固定 $z$ 的平面内，$V(x, y, z)$ 在轴线点 $(x, y) = (0, 0)$ 处取得极值（对 $\sqrt{x^2+y^2}$ 的偶函数展开不含一次项），因此在 $x=0, y=0$ 处一阶偏导数必为零：$\left.\frac{\partial V}{\partial x}\right|_{x=y=0} = \left.\frac{\partial V}{\partial y}\right|_{x=y=0} = 0$，物理上对应轴线上电场的横向分量 $E_x = E_y = 0$。

</details>

<details markdown="1">
<summary>Exercise 3.4 & 3.5: Thick Spherical Shell Potential & Apollonius Zero-Potential Sphere（均匀带电厚球壳电势与阿波罗尼奥斯零势球面）</summary>

**Problem Statement:**
- **Ex 3.4**: Consider a spherical shell with inner radius $R_1$ and outer radius $R_2$. The shell is uniformly charged with a volume charge density of $\rho$. Assume that the electric potential is zero at infinity. Calculate the electric potential at any distance $r$ from the origin.
- **Ex 3.5**: Consider two charged point particles, one with charge $-e$ at origin, another with charge $ne$ at $(0, 0, a)$, where $n > 1$. Assume that the electric potential is zero at infinity. Calculate: (a) The electric potential at any given point $\vec{r} = (x, y, z)$; (b) Show that the isosurface of zero electric potential is a sphere, and find the center of the sphere.

---

**中文解析：**

**1. 均匀带电厚球壳的全空间电势分布（Exercise 3.4，高频必考题）**：
首先利用高斯定理写出三个区域的径向电场强度 $E(r)$（其中厚球壳总电荷量为 $Q = \frac{4}{3}\pi(R_2^3 - R_1^3)\rho$）：

$$
E(r) = \begin{cases}
0, & r \le R_1, \\
\dfrac{\rho(r^3 - R_1^3)}{3\epsilon_0 r^2}, & R_1 < r < R_2, \\
\dfrac{\rho(R_2^3 - R_1^3)}{3\epsilon_0 r^2}, & r \ge R_2.
\end{cases}
$$

以无穷远处为电势零点，由外向内分段积分 $V(r) = \int_r^\infty E(r')\,dr'$（或利用薄球壳电势叠加）：

- **区域 I（外表面以外，$r \ge R_2$）**：
  $$
  V(r) = \int_r^\infty \frac{\rho(R_2^3 - R_1^3)}{3\epsilon_0 r'^2}\,dr' = \frac{\rho(R_2^3 - R_1^3)}{3\epsilon_0 r}
  $$
- **区域 II（球壳内部，$R_1 < r < R_2$）**：
  $$
  \begin{aligned}
  V(r) &= \int_r^{R_2} \frac{\rho}{3\epsilon_0}\left(r' - \frac{R_1^3}{r'^2}\right)dr' + V(R_2) \\
  &= \frac{\rho}{3\epsilon_0}\left[\frac{R_2^2 - r^2}{2} + R_1^3\left(\frac{1}{R_2} - \frac{1}{r}\right)\right] + \frac{\rho(R_2^3 - R_1^3)}{3\epsilon_0 R_2} = \frac{\rho}{6\epsilon_0}\left(3R_2^2 - r^2 - \frac{2R_1^3}{r}\right)
  \end{aligned}
  $$
- **区域 III（空腔内部，$r \le R_1$）**：
  因空腔内 $E = 0$，空腔为等势体，电势处处等于内表面 $r = R_1$ 处的电势：
  $$
  V(r) = V(R_1) = \frac{\rho}{6\epsilon_0}\left(3R_2^2 - 3R_1^2\right) = \frac{\rho}{2\epsilon_0}\left(R_2^2 - R_1^2\right)
  $$

---

**2. 异号不等量双点电荷的阿波罗尼奥斯零势球面（Exercise 3.5）**：

- **(a)** 任意点 $\vec{r} = (x, y, z)$ 到原点 $(-e)$ 的距离为 $r_1 = \sqrt{x^2 + y^2 + z^2}$，到 $(0, 0, a)$ 处 $(+ne)$ 的距离为 $r_2 = \sqrt{x^2 + y^2 + (z - a)^2}$。由叠加原理得电势：
  $$
  V(x, y, z) = \frac{e}{4\pi\epsilon_0}\left[ \frac{n}{\sqrt{x^2 + y^2 + (z - a)^2}} - \frac{1}{\sqrt{x^2 + y^2 + z^2}} \right]
  $$
- **(b)** 令 $V(x, y, z) = 0$，则有：
  $$
  \frac{n}{\sqrt{x^2 + y^2 + (z - a)^2}} = \frac{1}{\sqrt{x^2 + y^2 + z^2}} \implies n^2(x^2 + y^2 + z^2) = x^2 + y^2 + (z - a)^2
  $$
  移项整理并除以 $(n^2 - 1)$（因 $n > 1$，$n^2 - 1 > 0$）：
  $$
  x^2 + y^2 + z^2 + \frac{2a}{n^2 - 1}z = \frac{a^2}{n^2 - 1}
  $$
  对 $z$ 配方：
  $$
  x^2 + y^2 + \left(z + \frac{a}{n^2 - 1}\right)^2 = \frac{a^2}{n^2 - 1} + \frac{a^2}{(n^2 - 1)^2} = \left(\frac{na}{n^2 - 1}\right)^2
  $$
  这是一个标准的球面方程！其**球心坐标为 $\left(0, 0, -\dfrac{a}{n^2 - 1}\right)$**，球面半径为 $R = \dfrac{na}{n^2 - 1}$。

</details>

<details markdown="1">
<summary>Exercise 3.6 & 3.7: Two-Particle Energy/Momentum Conservation & Line Integral Path Independence（双粒子释放速度与电势路径无关性验证）</summary>

**Problem Statement:**
- **Ex 3.6**: Two small particles carry the same charge $q > 0$. Their masses are $m$ and $2m$. They are held at rest a distance $d$ apart, far from any other charge, and then released. (a) Find the speed of each particle when they are very far apart. (b) Suppose instead that the particle of mass $2m$ is held fixed, and only the other particle is released. Find its final speed. Why is it larger than in (a)?
- **Ex 3.7**: Take the electrostatic field to be $\vec{E}(x, y, z) = \frac{E_0}{a}(y\hat{x} + x\hat{y})$ everywhere ($E_0, a > 0$), and choose $V = 0$ at the origin. (a) Find $V$ at $P = (x, y, 0)$ by integrating along $(0,0,0) \to (x,0,0) \to (x,y,0)$, and again along $(0,0,0) \to (0,y,0) \to (x,y,0)$. Show that the two paths give the same result. (b) Find the equipotential curve in the $xy$ plane passing through $(a, a, 0)$ (keeping the branch containing this point), and show that $\vec{E}$ is perpendicular to this curve at every point on it.

---

**中文解析：**

**1. 斥力释放的双粒子终态速度（Exercise 3.6）**：

- **(a) 两粒子均自由释放**：系统不受外力，总动量守恒且机械能守恒。设无穷远时质量为 $m$ 和 $2m$ 的粒子速度大小分别为 $v_1$ 和 $v_2$（方向相反）：
  $$
  \begin{cases}
  mv_1 - (2m)v_2 = 0 \implies v_1 = 2v_2 \\
  \dfrac{1}{2}mv_1^2 + \dfrac{1}{2}(2m)v_2^2 = U_i = \dfrac{q^2}{4\pi\epsilon_0 d}
  \end{cases}
  $$
  将 $v_2 = v_1/2$ 代入能量方程得 $\frac{3}{4}mv_1^2 = \frac{q^2}{4\pi\epsilon_0 d}$，解得：
  $$
  v_1 = \sqrt{\frac{q^2}{3\pi\epsilon_0 m d}}, \qquad v_2 = \frac{1}{2}\sqrt{\frac{q^2}{3\pi\epsilon_0 m d}} = \sqrt{\frac{q^2}{12\pi\epsilon_0 m d}}
  $$
- **(b) 质量为 $2m$ 的粒子固定**：此时系统的全部初始静电势能都转化为轻粒子 $m$ 一者的动能：
  $$
  \frac{1}{2}mv_1'^2 = \frac{q^2}{4\pi\epsilon_0 d} \implies v_1' = \sqrt{\frac{q^2}{2\pi\epsilon_0 m d}}
  $$
  显然 $v_1' > v_1$，因为在 (a) 中有一部分初始势能（占比 $1/3$）被分配给了重粒子 $2m$ 作为动能，而在 (b) 中固定靶不获取任何动能，全部势能均由粒子 $m$ 独享。

---

**2. 二维四极场中的路径无关性验证与双曲线等势线（Exercise 3.7）**：

- **(a) 两条折线路径积分求 $V(x, y, 0)$**：
  由 $V(x, y, 0) = -\int_{(0,0,0)}^{(x,y,0)} (E_x\,dx' + E_y\,dy') = -\frac{E_0}{a}\int (y'\,dx' + x'\,dy')$：
  - **路径 1**：$(0,0,0) \xrightarrow{y'=0} (x,0,0) \xrightarrow{x'=x} (x,y,0)$：第一段 $y'=0 \implies E_x = 0$，积分为 $0$；第二段 $dx'=0, x'=x$，积分为 $-\frac{E_0}{a}\int_0^y x\,dy' = -\dfrac{E_0 xy}{a}$。
  - **路径 2**：$(0,0,0) \xrightarrow{x'=0} (0,y,0) \xrightarrow{y'=y} (x,y,0)$：第一段 $x'=0 \implies E_y = 0$，积分为 $0$；第二段 $dy'=0, y'=y$，积分为 $-\frac{E_0}{a}\int_0^x y\,dx' = -\dfrac{E_0 xy}{a}$。
  两条路径结果完全一致。
- **(b) 等势线方程与正交性证明**：
  将点 $(a, a, 0)$ 代入 $V(x, y, 0) = -\frac{E_0 xy}{a}$ 得常数 $V = -E_0 a$，故通过该点的等势线第一象限分支为双曲线：
  $$
  xy = a^2 \iff y = \frac{a^2}{x} \qquad (x > 0)
  $$
  在该曲线上任意一点 $(x, y)$ 处，曲线切线斜率为 $\frac{dy}{dx} = -\frac{a^2}{x^2} = -\frac{y}{x}$，故切向量为 $\vec{\tau} = \hat{x} - \frac{y}{x}\hat{y}$。将其与该点电场 $\vec{E} = \frac{E_0}{a}(y\hat{x} + x\hat{y})$ 作点乘：
  $$
  \vec{E} \cdot \vec{\tau} = \frac{E_0}{a}\left(y \cdot 1 + x \cdot \left(-\frac{y}{x}\right)\right) = 0
  $$
  点乘恒为零，证得 $\vec{E}$ 在等势线上每一点均与等势线垂直。

</details>

<details markdown="1">
<summary>Exercise 3.8, 3.9 & 3.10: Infinite Rod Potential Limit, Sphere Self-Energy & Yukawa Screened Potential（无限长杆电势差极限、实心球组装自能与汤川屏蔽势）</summary>

**Problem Statement:**
- **Ex 3.8**: A thin straight rod of length $2L$ carries a uniform linear charge density $\lambda > 0$. Point $P$ lies on the perpendicular bisector at distance $s$ from its midpoint. Take $V = 0$ at infinity. (a) Find $V$ at $P$, and show that for fixed $s$, $V \to \infty$ as $L \to \infty$. (b) Let $P_1, P_2$ be two points on the bisector at distances $s_1, s_2$. Show that $V(P_1) - V(P_2)$ approaches a finite limit as $L \to \infty$, find it, and check against Gauss's law.
- **Ex 3.9**: A ball of radius $R$ carries a total charge $Q$ spread uniformly through its volume. Imagine building it by bringing charge slowly in from infinity, one thin spherical layer at a time. (a) When the ball has radius $r$, find the work needed to bring in the next layer $dr$, and show that the total work is $U = \frac{3Q^2}{20\pi\epsilon_0 R}$. Why is $U$ smaller than $QV(R)$? (b) Suppose the electron were a uniformly charged ball whose rest energy $m_e c^2$ is all of this electrostatic energy. Estimate its radius ($e = 1.60\times 10^{-19}\text{ C}$, $m_e c^2 = 8.19\times 10^{-14}\text{ J}$, $\epsilon_0 = 8.85\times 10^{-12}\text{ F/m}$).
- **Ex 3.10**: A point charge $q > 0$ sits at the origin, surrounded by a spherically symmetric distribution of other charge. Together they produce the potential $V(r) = \frac{q\exp(-r/a)}{4\pi\epsilon_0 r} \ (r > 0)$. (a) Calculate the Cartesian components of $\vec{E} = -\nabla V$, and write the result in the form $\vec{E} = E(r)\hat{r}$. (b) Use Gauss's law to find the total charge $Q(r)$ inside a sphere of radius $r$. Find $Q(r)$ as $r \to 0$ and $r \to \infty$. What is the total charge of the surrounding distribution?

---

**中文解析：**

**1. 有限长带电细杆中垂线电势及 $L \to \infty$ 时的电势差极限（Exercise 3.8）**：

- **(a)** 以细杆中点为原点，细杆占据 $[-L, L]$，中垂线上距中点 $s$ 处的电势为：
  $$
  V(s) = \frac{\lambda}{4\pi\epsilon_0} \int_{-L}^L \frac{dx}{\sqrt{x^2 + s^2}} = \frac{\lambda}{4\pi\epsilon_0} \ln\left(\frac{\sqrt{L^2 + s^2} + L}{\sqrt{L^2 + s^2} - L}\right) = \frac{\lambda}{2\pi\epsilon_0} \ln\left(\frac{L + \sqrt{L^2 + s^2}}{s}\right)
  $$
  当 $s$ 固定而 $L \to \infty$ 时，$\ln\left(\frac{2L}{s}\right) \to +\infty$，即绝对电势发散。
- **(b)** 计算中垂线上两点 $s_1$ 与 $s_2$ 的电势差并取 $L \to \infty$ 极限：
  $$
  V(P_1) - V(P_2) = \frac{\lambda}{2\pi\epsilon_0} \ln\left(\frac{s_2}{s_1} \cdot \frac{L + \sqrt{L^2 + s_1^2}}{L + \sqrt{L^2 + s_2^2}}\right) \xrightarrow{L \to \infty} \frac{\lambda}{2\pi\epsilon_0} \ln\left(\frac{s_2}{s_1}\right)
  $$
  验证：由高斯定理知无限长直导线场强为 $E(s) = \frac{\lambda}{2\pi\epsilon_0 s}$，直接积分 $-\int_{s_2}^{s_1} E(s)\,ds = \frac{\lambda}{2\pi\epsilon_0}\ln\left(\frac{s_2}{s_1}\right)$，两者完全一致！

---

**2. 均匀带电实心球的逐层组装静电能（自能）与经典电子半径（Exercise 3.9，重点必考）**：

- **(a)** 实心球体电荷密度为 $\rho = \frac{Q}{\frac{4}{3}\pi R^3}$。当球体已经组装到半径为 $r$ 时，其已带电量为 $q(r) = \frac{4}{3}\pi r^3 \rho = Q\frac{r^3}{R^3}$，此时球体表面的电势为：
  $$
  V(r) = \frac{1}{4\pi\epsilon_0}\frac{q(r)}{r} = \frac{Qr^2}{4\pi\epsilon_0 R^3}
  $$
  从无穷远处再移来厚度为 $dr$ 的薄球壳层，该层所带电荷微元为 $dq = 4\pi r^2 \rho\,dr = \frac{3Q}{R^3}r^2\,dr$。所需做的微元功为：
  $$
  dU = V(r)\,dq = \left(\frac{Qr^2}{4\pi\epsilon_0 R^3}\right)\left(\frac{3Q}{R^3}r^2\,dr\right) = \frac{3Q^2}{4\pi\epsilon_0 R^6} r^4\,dr
  $$
  从 $r = 0$ 积分至 $r = R$，即得组装整个带电球所需的总静电能：
  $$
  U = \int_0^R dU = \frac{3Q^2}{4\pi\epsilon_0 R^6} \left[\frac{r^5}{5}\right]_0^R = \frac{3Q^2}{20\pi\epsilon_0 R} = \frac{3}{5} \frac{Q^2}{4\pi\epsilon_0 R}
  $$
  **为什么 $U = \frac{3}{5}QV(R) < QV(R)$？** 因为在组装过程中，球体所带电量是从 $0$ 逐渐增长到 $Q$ 的，绝大部分电荷在被移入时的瞬时表面电势 $V(r) \propto r^2$ 都远低于最终的表面电势 $V(R) = \frac{Q}{4\pi\epsilon_0 R}$。
- **(b) 经典电子半径估算**：
  令 $U = \frac{3e^2}{20\pi\epsilon_0 R} = m_e c^2$，解出半径 $R$：
  $$
  R = \frac{3e^2}{20\pi\epsilon_0 (m_e c^2)} = \frac{3 \times (1.60 \times 10^{-19})^2}{20\pi \times 8.85 \times 10^{-12} \times 8.19 \times 10^{-14}} \approx 1.69 \times 10^{-15}\text{ m}
  $$

---

**3. 汤川屏蔽势（Yukawa / Debye Screened Potential）的电场与包围电荷分析（Exercise 3.10）**：

- **(a)** 注意到 $\frac{\partial r}{\partial x} = \frac{x}{r}$，利用链式法则计算 $\vec{E} = -\nabla V$ 的 $x$ 分量：
  $$
  E_x = -\frac{\partial V}{\partial x} = -\frac{dV}{dr}\frac{\partial r}{\partial x} = -\frac{q}{4\pi\epsilon_0}\frac{d}{dr}\left(\frac{e^{-r/a}}{r}\right)\frac{x}{r} = \frac{q e^{-r/a}}{4\pi\epsilon_0 r^2}\left(1 + \frac{r}{a}\right)\frac{x}{r}
  $$
  同理可得 $E_y, E_z$（只需将 $x$ 换为 $y, z$）。由于 $\frac{x\hat{x} + y\hat{y} + z\hat{z}}{r} = \frac{\vec{r}}{r} = \hat{r}$，合并为径向形式：
  $$
  \vec{E}(\vec{r}) = \frac{q e^{-r/a}}{4\pi\epsilon_0 r^2}\left(1 + \frac{r}{a}\right)\hat{r}
  $$
- **(b)** 以原点为中心作半径为 $r$ 的球形高斯面，由高斯定理 $\epsilon_0 (4\pi r^2 E(r)) = Q(r)$ 得球内总电荷：
  $$
  Q(r) = q\left(1 + \frac{r}{a}\right)e^{-r/a}
  $$
  - 当 $r \to 0$ 时：$Q(r) \to q$（仅包围原点处的点电荷 $+q$）；
  - 当 $r \to \infty$ 时：因指数衰减快于多项式增长，$Q(r) \to 0$（完全屏蔽）。
  因此，包围在点电荷周围的球对称电荷云的总电荷量为 $Q_{\text{surr}} = Q(\infty) - Q(0) = 0 - q = -q$。

</details>