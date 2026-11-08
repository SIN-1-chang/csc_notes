# Chapter 11: Faraday's Law of Induction（法拉第电磁感应定律）

!!! abstract
    General Physics II (Electromagnetism) | 第十一章课堂与讲义笔记
    
    参考：
    
    - Lecture 11: *Faraday's Law of Induction* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 11: *Faraday's Law of Induction*
    - Halliday, Resnick & Krane, *Physics*, Chapter 34

## 1 电磁感应现象与法拉第定律 (Electromagnetic Induction and Faraday's Law)

### 1.1 从静场到动场：法拉第的两个经典实验

在静电学与静磁学中，电场与磁场彼此独立，遵循各自的散度与旋度方程：

$$
\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}, \quad \nabla \times \vec{E} = \vec{0}; \qquad \nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{B} = \mu_0 \vec{j}
$$

既然电流可以产生磁场，那么磁场能否反过来产生电场并驱动电流？1831 年，迈克尔·法拉第（Michael Faraday）通过两个奠基性实验发现了**电磁感应**（Electromagnetic Induction）现象，建立了从变化的磁场 $\vec{B}$ 到电场 $\vec{E}$ 的桥梁（结合后续麦克斯韦的位移电流，最终实现了电与磁的统一）：

1. **实验一（磁铁与导电线圈的相对运动）**：
   将导电闭合回路 $L$ 连接到灵敏电流计上。当把条形磁铁移向或移离线圈时，回路中立即出现电流；当磁铁停止运动时，电流立即消失；运动越快，产生的电流越大；将磁铁运动方向反转或将 N 极换为 S 极，电流方向随之反转。
2. **实验二（邻近线圈通断电流）**：
   将接有电池和开关的第二个线圈 $L'$ 放置在静止线圈 $L$ 旁边（两者不接触）。仅在合上开关（接通电流）或断开开关（切断电流）的**短暂瞬间**，线圈 $L$ 中才会出现方向相反的瞬时电流；而当 $L'$ 中的电流保持恒定时（无论恒定电流有多大），线圈 $L$ 中均无电流。

由此产生的电流称为**感应电流**（Induced current），推动单位电荷绕回路运动所做的功称为**感应电动势**（Induced emf, $\mathcal{E}$）。

### 1.2 磁通量与法拉第电磁感应定律

法拉第意识到，上述两个实验的共同本质是**穿过闭合回路的磁感线条数发生了改变**。为此，定量定义穿过以回路为边界的曲面 $S$（或面积 $A$）的**磁通量**（Magnetic Flux，记作 $\Phi_B$）为：

$$
\Phi_B = \int_S \vec{B} \cdot d\vec{S} = \int_A \vec{B} \cdot d\vec{A}
$$

磁通量 $\Phi_B$ 是标量，其国际单位制（SI）单位为**韦伯**（Weber，简记为 $\text{Wb}$）：

$$
1\text{ Wb} = 1\text{ T}\cdot\text{m}^2 = 1\text{ V}\cdot\text{s}
$$

**法拉第电磁感应定律（Faraday's Law of Induction）**：闭合导电回路中感应电动势 $\mathcal{E}$ 的大小等于穿过该回路的磁通量 $\Phi_B$ 随时间的变化率：

$$
\mathcal{E} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\int_S \vec{B} \cdot d\vec{S}
$$

若紧密绕制的线圈共有 $N$ 匝（Turns），且每匝穿过相同的磁通量 $\Phi_B$，则总感应电动势为：

$$
\mathcal{E} = -N\frac{d\Phi_B}{dt}
$$

**核心要点说明**：
- **右手螺旋符号约定**：公式中的正负号将感应电动势 $\mathcal{E}$ 的正绕行方向与曲面法向微元 $d\vec{S}$ 的方向通过**右手定则**绑定——弯曲右手四指顺着选定的回路正绕行方向，大拇指所指方向即为法向量 $d\vec{S}$ 的正方向。
- **改变磁通量 $\Phi_B$ 的三种途径**：① 改变磁感应强度 $\vec{B}$ 的大小（如 $\vec{B}(t)$ 随时间变化）；② 改变回路处于磁场中的有效面积 $A$（如拉伸线圈或将线框拉出磁场）；③ 改变磁场 $\vec{B}$ 与回路法向 $\hat{n}$ 之间的夹角 $\theta$（如在线圈中旋转发电）。

---

## 2 楞次定律与能量转换 (Lenz's Law and Energy Transfers)

### 2.1 楞次定律的两种等价表述

法拉第定律公式中的负号代表了由海因里希·楞次（Heinrich Lenz）总结出的方向判据——**楞次定律**（Lenz's Law）：**感应电流的方向总是使其自身所产生的感应磁场 $\vec{B}_{\text{ind}}$ 阻碍（Oppose）引起感应电流的原磁通量 $\Phi_B$ 的变化**（感应电动势的方向与感应电流方向一致）。

在实际解题中，可通过以下两个互补视角应用楞次定律：

| 判别视角 | 核心物理法则 | 典型实例（磁铁 N 极从右侧移向线圈 vs. 移离线圈） |
| :--- | :--- | :--- |
| **1. 阻碍磁通量变化**<br>（Opposition to Flux Change） | 原磁通量 **增加**（$\Delta\Phi_B > 0$）时，$\vec{B}_{\text{ind}}$ 与原磁场 $\vec{B}$ **反向**；<br>原磁通量 **减少**（$\Delta\Phi_B < 0$）时，$\vec{B}_{\text{ind}}$ 与原磁场 $\vec{B}$ **同向** | N 极靠近时，向左的 $\Phi_B$ 增加 $\implies \vec{B}_{\text{ind}}$ 向右 $\implies$ 由右手定则知电流顺时针（从左往右看）；<br>**注意：$\vec{B}_{\text{ind}}$ 并非总是与 $\vec{B}$ 反向**（当 $\vec{B}$ 减弱时二者同向，口诀：“增反减同”） |
| **2. 阻碍磁极相对运动**<br>（Opposition to Pole Movement） | 感应电流使线圈等效为一个磁偶极子 $\vec{\mu}$，其磁极取向总是**反抗磁铁的相对运动**（“来拒去留”） | N 极靠近时，线圈右侧等效为 N 极（$\vec{\mu}$ 向右）以排斥磁铁靠近；<br>N 极远离时，线圈右侧等效为 S 极（$\vec{\mu}$ 向左）以吸引磁铁挽留 |

### 2.2 电磁感应中的机械能与焦耳热守恒

楞次定律本质上是**能量守恒定律**在电磁感应中的必然要求。考察两个经典模型（Examples 11.1 & 11.2）：

**模型 1：时变磁场中的静止圆环（Example 11.1）**
半径为 $R$ 的圆形导线环置于 $xy$ 平面，空间存在沿 $z$ 轴的余弦交变磁场 $\vec{B}(t) = \hat{z} B_0\cos(\omega t)$。取 $d\vec{S}$ 沿 $+\hat{z}$ 方向，则磁通量为 $\Phi_B(t) = B_0\pi R^2\cos(\omega t)$，感应电动势为：

$$
\mathcal{E} = -\frac{d\Phi_B}{dt} = \omega B_0 \pi R^2 \sin(\omega t)
$$

**模型 2：平行导轨上的滑动导体棒 / 拉出矩形线框的能量守恒（Example 11.2 & Lecture 11 Slides 18–20）**
设宽度为 $L$、总电阻为 $R$ 的矩形线框（或在间距为 $L$ 的平行导轨上滑动的导体棒）处于垂直纸面的匀强磁场 $B$ 中。以恒定速度 $v$ 将线框向右拉出磁场（或使滑杆向右滑动）：

1. **动生电动势与感应电流**：设回路在磁场内的长度为 $x$，则磁通量大小为 $\Phi_B = BLx$，感应电动势大小与感应电流分别为：
   $$
   |\mathcal{E}| = \left|\frac{d\Phi_B}{dt}\right| = BL\left|\frac{dx}{dt}\right| = BLv, \qquad i = \frac{|\mathcal{E}|}{R} = \frac{BLv}{R}
   $$
2. **安培阻力与外力平衡**：根据楞次定律，磁场对载流边框施加的安培力（上下两条水平边的安培力 $\vec{F}_2 = -\vec{F}_3$ 相互抵消，仅剩左侧垂直边受向左的安培力 $\vec{F}_1$）必然阻碍线框被拉出。为了维持恒定速度 $v$，外加拉力 $F$ 必须与安培力平衡：
   $$
   F = F_1 = iLB = \left(\frac{BLv}{R}\right)LB = \frac{B^2 L^2 v}{R}
   $$
3. **机械功率等于热耗散功率**：外力拉动线框做功的机械功率 $P_{\text{mech}}$ 与回路电阻产生的焦耳热功率 $P_{\text{thermal}}$ 精确相等（忽略电磁辐射损耗）：
   $$
   P_{\text{mech}} = Fv = \frac{B^2 L^2 v^2}{R} \equiv i^2 R = \left(\frac{BLv}{R}\right)^2 R = P_{\text{thermal}}
   $$

---

## 3 感生电场与法拉第定律的微分形式 (Induced Electric Fields & Differential Form)

### 3.1 动生电动势 vs. 感生电场

当穿过闭合回路的磁通量发生变化并产生感应电动势时，究竟是什么力在驱动回路中的电荷运动？讲义（Section 11.3）深入对比了三种物理情形：

| 物理情形 | 磁场 $\vec{B}$ 是否随时间变化 | 闭合回路是否运动 | 驱动电荷运动的物理本质 | 空间是否存在感生电场 $\vec{E}_{\text{ind}}$ |
| :--- | :---: | :---: | :--- | :---: |
| **情形 1：静磁场中导轨滑杆**<br>（Motional Emf, Example 11.2） | 否（$\dfrac{\partial\vec{B}}{\partial t} = \vec{0}$） | 是（速度 $\vec{v}$） | 随杆运动的载流子受到磁洛伦兹力 $\vec{F}_B = q\vec{v}\times\vec{B}$，沿杆产生 $\mathcal{E} = -vBL$ | **无**（$\vec{E} = \vec{0}$，电势概念依然有效） |
| **情形 2：磁铁移向静止线圈**<br>（Moving Magnet） | 是（在静止线圈系中 $\dfrac{\partial\vec{B}}{\partial t} \neq \vec{0}$） | 否（$\vec{v} = \vec{0}$） | 线圈内载流子初速为零，不受洛伦兹力，必受**感生电场力** $q\vec{E}$ 驱动 | **有**（由变化的磁场激发） |
| **情形 3：交变磁场中的静止线圈**<br>（Time-Varying $\vec{B}$, Example 11.1） | 是（$\dfrac{\partial\vec{B}}{\partial t} \neq \vec{0}$） | 否（$\vec{v} = \vec{0}$） | 变化的磁场在空间激发闭合涡旋状**感生电场** $\vec{E}$ | **有**（即使移走铜环，真空中 $\vec{E}$ 依然存在） |

由此得出电动力学中最核心的结论之一：**变化的磁场会在周围空间（包括真空）激发电场（A changing magnetic field produces an electric field）**！这种由时变磁场产生的电场称为**感生电场**（Induced Electric Field），它对检验电荷的作用力 $q_0\vec{E}$ 与静电荷产生的库仑电场没有任何局域区别。

对于空间任意**静止闭合路径 $C$**（无论是否有实体导体存在），感应电动势定义为感生电场沿闭合路径的环流，法拉第电磁感应定律改写为完整场积分形式：

$$
\mathcal{E} = \oint_C \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\int_S \vec{B} \cdot d\vec{S}
$$

*（注：若闭合回路 $C$ 自身还在以速度 $\vec{v}$ 运动，则普遍情形下的感应电动势为单位电荷所受总洛伦兹力的环流 $\mathcal{E} = \oint_C (\vec{E} + \vec{v}\times\vec{B})\cdot d\vec{l} = -\frac{d\Phi_B}{dt}$，其中 $-\frac{d}{dt}\int_S \vec{B}\cdot d\vec{S}$ 同时包含了场随时间变化 $\frac{\partial\vec{B}}{\partial t}$ 的感生贡献和边界移动切割磁感线 $\vec{v}\times\vec{B}$ 的动生贡献）。*

### 3.2 法拉第定律的微分形式与电势概念的失效

对于空间静止的闭合回路 $C$ 及其张成的任意静止曲面 $S$，应用斯托克斯定理（Stokes' theorem）将左侧环流化为旋度的面积分，并将右侧时间全导数移入积分号内化为偏导数：

$$
\oint_C \vec{E} \cdot d\vec{l} = \int_S (\nabla \times \vec{E}) \cdot d\vec{S} = -\int_S \frac{\partial\vec{B}}{\partial t} \cdot d\vec{S} \implies \int_S \left(\nabla \times \vec{E} + \frac{\partial\vec{B}}{\partial t}\right) \cdot d\vec{S} = 0
$$

由于曲面 $S$ 是任意选取的，被积函数必须处处为零，从而得到**法拉第电磁感应定律的微分形式**（麦克斯韦四大方程之一）：

$$
\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}
$$

!!! danger "核心概念转折：感生电场的非保守性与电势 $V$ 的失效（Loss of Electric Potential）"
    - **静电学回顾**：在静电场中，$\frac{\partial\vec{B}}{\partial t} = \vec{0} \implies \nabla\times\vec{E} = \vec{0} \iff \oint \vec{E}\cdot d\vec{l} = 0$。静电场是无旋保守场，两点间的线积分 $\int_i^f \vec{E}\cdot d\vec{l}$ 与路径无关，因此可以定义单值标量电势 $V$（满足 $\vec{E} = -\nabla V$）。
    - **电动力学新特征**：当空间存在随时间变化的磁场（$\frac{\partial\vec{B}}{\partial t} \neq \vec{0}$）时，**$\nabla\times\vec{E} \neq \vec{0}$ 且 $\oint \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt} \neq 0$**！感生电场线本身是无头无尾的闭合涡旋线（如 Figure 11.5）。此时**感生电场是非保守场（Non-conservative field）**，两点之间的线积分 $\int_P^Q \vec{E}\cdot d\vec{l}$ **强烈依赖于所选取的具体积分路径**（见 Exercise 11.9）。因此，在磁场随时间变化的区域内，**不存在满足 $\vec{E} = -\nabla V$ 的单值标量电势 $V$，针对感生电场谈论“电势”或“电势差”是毫无物理意义的**！
    - **唯一例外（动生电动势）**：在静磁场（$\frac{\partial\vec{B}}{\partial t} = \vec{0}$）中由导体切割磁感线产生的动生电动势中，空间静电场依然满足 $\nabla\times\vec{E} = \vec{0}$（保守场），因此各点电势 $V$ 依然有明确定义（见 Exercise 11.2）。

---

## 4 狭义相对论与电磁场的参考系变换 (Relativity of $\vec{E}$ and $\vec{B}$, Appendices 11A–11C)

为什么洛伦兹力 $\vec{F} = q\vec{E} + q\vec{v}\times\vec{B}$ 中的磁场力部分依赖于粒子的运动速度 $\vec{v}$，而不同惯性系（Inertial frames of reference）中的观察者测得的 $\vec{v}$ 并不相同？爱因斯坦正是从“磁铁与线圈相对运动只取决于相对速度”这一电磁感应不对称性出发，创立了狭义相对论。

### 4.1 电荷的洛伦兹不变性与电场的相对论变换

1. **电荷的相对论不变性（Relativistic Invariance of Charge，Appendix 11A）**：
   实验表明，任何带电体所带的电荷量 $q$ 是严格的洛伦兹标量不变量，不随参考系的运动而改变。因此高斯定理通量 $\int_S \vec{E}\cdot d\vec{a} = \int_{S'} \vec{E}'\cdot d\vec{a}' = q_{\text{enc}}/\epsilon_0$ 在一切惯性系中均成立。
2. **相对运动引起的电场变换（Appendix 11B）**：
   考察在惯性系 $F$ 中静止的两块平行带电平板（边长为 $b$，面电荷密度为 $\pm\sigma$）。板间静电场为 $E = \frac{\sigma}{\epsilon_0}$。现从以速度 $\vec{v} = v\hat{x}$ 相对于 $F$ 运动的惯性系 $F'$ 中观察（记洛伦兹因子 $\gamma = \frac{1}{s} = \frac{1}{\sqrt{1 - v^2/c^2}}$）：
   - **当极板平行于 $xy$ 平面（电场沿 $z$ 轴，垂直于运动方向 $\vec{v}$）**：在 $F'$ 系中，沿运动方向 $x$ 的极板边长发生**洛伦兹尺缩**（由 $b$ 收缩为 $sb = b/\gamma$），而垂直方向的 $y$ 边长 $b$ 不变，且总电荷量不变。因此 $F'$ 系测得的面电荷密度增大为 $\sigma' = \frac{\sigma}{s} = \gamma\sigma$，由高斯定理知垂直于速度方向的电场增强为 $\gamma$ 倍：
     $$
     E_z' = \frac{\sigma'}{\epsilon_0} = \gamma E_z
     $$
   - **当极板垂直于 $x$ 轴（电场沿 $x$ 轴，平行于运动方向 $\vec{v}$）**：极板的横截面积位于 $yz$ 平面内，不发生尺缩，故 $\sigma' = \sigma$，平行于速度方向的电场保持不变：
     $$
     E_x' = \frac{\sigma'}{\epsilon_0} = E_x
     $$
   综上所述，在静电荷源参考系 $F$ 变换到运动参考系 $F'$ 时，电场分量的变换法则为：
   $$
   E_\parallel' = E_\parallel, \qquad E_\perp' = \gamma E_\perp
   $$

### 4.2 相对运动中感生电场与磁场的相互转化

1. **动生电动势 vs. 感生电场的参考系调和（Appendix 11B Slides 34–35）**：
   在线框以速度 $\vec{v}$ 离开磁铁的实验中：
   - 与磁铁相对静止的观察者 $S$ 认为空间只有静磁场 $\vec{B}$，线框受磁洛伦兹力产生动生电动势 $\mathcal{E} = BLv = \oint (\vec{v}\times\vec{B})\cdot d\vec{s}$；
   - 与线框相对静止的观察者 $S'$ 看到线框静止（无磁力），必然认为运动的磁铁在空间激发了横向**感生电场** $\vec{E}'$。计入相对论横向场变换因子 $\gamma$，在 $S'$ 系中测得的电场为：
     $$
     \vec{E}' = \gamma(\vec{v} \times \vec{B}) \xrightarrow{v \ll c} \vec{E}' \approx \vec{v} \times \vec{B}
     $$
2. **纯电场通过相对运动产生磁场（Appendix 11C & Section 11.4）**：
   回到在 $F$ 系中静止、平行于 $xy$ 平面的两块带电板（板间只有纯电场 $\vec{E} = E\hat{z}, \ E = \sigma/\epsilon_0$，无磁场 $\vec{B} = \vec{0}$）。
   在沿 $+x$ 方向以速度 $v$ 运动的 $F'$ 系看来，两块带电板正以速度 $-v\hat{x}$ 向左运动，构成两层反向流动的无限大**面电流**，面电流密度大小为 $J_s' = \sigma' v = \gamma\sigma v$！
   由第九章面电流磁场公式，两层反向面电流在板间产生的磁场同向叠加为 $B' = 2 \times \left(\frac{1}{2}\mu_0 J_s'\right) = \mu_0 J_s'$。代入 $\sigma = \epsilon_0 E$ 以及著名的电磁常数与光速关系 **$\mu_0\epsilon_0 = \dfrac{1}{c^2}$**：
   $$
   B' = \mu_0 \gamma \sigma v = \mu_0 \epsilon_0 \gamma v E = \frac{\gamma v E}{c^2} \iff \vec{B}' = -\frac{\gamma \vec{v} \times \vec{E}}{c^2}
   $$
   **物理结论**：在一个惯性系中纯粹的静电场 $\vec{E}$，在另一个惯性系中会同时表现为电场 $\vec{E}'$ 和磁场 $\vec{B}'$！电与磁并非独立的实体，而是同一个四维**二阶反对称电磁场张量**（Antisymmetric second-rank tensor，共 6 个独立分量：$E_x, E_y, E_z, B_x, B_y, B_z$）在不同惯性参考系下的不同表象。

---

## 5 Chapter 11 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 11.1, 11.2 & 11.3: Moving Loop Near Wire, Rotating Triangle Potentials & AC Solenoid（离开长直导线的矩形框、旋转正三角形顶点电势差与交流螺线管）</summary>

**Problem Statement:**
- **Ex 11.1**: An infinitely long conducting wire carries a current $I$, and a rectangular loop lies in the same plane as the wire and moves away from it perpendicular to the wire at constant speed $v$ (`Figure 11.6`). The loop has side $a$ parallel to the wire, width $b$, and its near side is a distance $c$ from the wire. Calculate the induced emf in the rectangle.
- **Ex 11.2**: An equilateral triangular loop of side $a$ and resistance $R$ ($R/3$ per side) is rotating about its edge 1-2 with constant angular velocity $\omega$ (`Figure 11.7`). A uniform magnetic field $\vec{B}$ points into the page. At $t = 0$ the triangular plane is perpendicular to $\vec{B}$. Across a side with motional emf $e$ and current $I$, $V_a - V_b = e - IR/3$. Calculate the electric potential difference between each pair of vertices at any time $t$.
- **Ex 11.3**: A long solenoid with radius $r_1 = 5\text{ cm}$ and $n = 1000\text{ turns/m}$ has its axis along $z$ and carries $I(t) = I_0\sin(\omega t)$ ($I_0 = 2\text{ A}$, $\omega = 100\pi\text{ rad/s}$, positive counterclockwise from $+z$). A circular loop of radius $r_2 = 3\text{ cm}$ and resistance $R = 0.5\ \Omega$ is placed inside perpendicular to the axis. (a) Find $B(t)$ inside. (b) Calculate the induced emf $\mathcal{E}(t)$ in the loop. (c) Calculate the maximum induced current $I_{\max}$. (d) Describe the phase relationship over one period.

---

**中文解析：**

**1. 垂直远离长直载流导线的矩形线框感应电动势（Exercise 11.1）**：

- **方法 1（磁通量求导法）**：
  设某时刻矩形近端距导线的距离为 $x$（初态或瞬时值 $x = c$，且 $\frac{dx}{dt} = v$）。在距导线 $r$ 处，长直导线的磁场垂直纸面向里，大小为 $B(r) = \frac{\mu_0 I}{2\pi r}$。穿过矩形框的磁通量为：
  $$
  \Phi_B(x) = \int_x^{x+b} \frac{\mu_0 I}{2\pi r} a\,dr = \frac{\mu_0 I a}{2\pi}\ln\left(\frac{x + b}{x}\right)
  $$
  由法拉第定律求时间导数，并代入 $x = c, \ \frac{dx}{dt} = v$：
  $$
  |\mathcal{E}| = \left|-\frac{d\Phi_B}{dt}\right| = \frac{\mu_0 I a}{2\pi}\left|\frac{1}{x + b} - \frac{1}{x}\right|\frac{dx}{dt} = \frac{\mu_0 I a b v}{2\pi c(c + b)}
  $$
  （由楞次定律，因向里的磁通量减小，感应电流方向为**顺时针**）。
- **方法 2（左右两边切割磁感线动生电动势相减）**：
  近端边（$x = c$）与远端边（$x = c+b$）均以速度 $v$ 切割磁感线，各自产生向上的动生电动势 $B(c)av$ 与 $B(c+b)av$，回路总电动势为两者之差：
  $$
  |\mathcal{E}| = \left[\frac{\mu_0 I}{2\pi c} - \frac{\mu_0 I}{2\pi(c + b)}\right]av = \frac{\mu_0 I a b v}{2\pi c(c + b)}
  $$

---

**2. 静磁场中旋转正三角形线框各顶点间的电势差（Exercise 11.2，核心概念辨析题）**：
由于匀强磁场 $\vec{B}$ 是**不随时间变化的静磁场**（$\frac{\partial\vec{B}}{\partial t} = \vec{0}$），空间无感生电场（$\nabla\times\vec{E} = \vec{0}$），因此尽管回路运动产生动生电动势，**各顶点的静电势 $V_1, V_2, V_3$ 依然是单值且严格良定义的**！

1. **求回路总动生电动势与感应电流 $I(t)$**：
   正三角形面积为 $A = \frac{\sqrt{3}}{4}a^2$。在 $t = 0$ 时线框平面垂直于 $\vec{B}$，取法向与 $\vec{B}$（向里）同向，则时刻 $t$ 转角为 $\theta = \omega t$，磁通量为 $\Phi_B(t) = BA\cos(\omega t) = \frac{\sqrt{3}}{4}Ba^2\cos(\omega t)$。
   因此回路总感应电动势与总感应电流（沿 $1 \to 2 \to 3 \to 1$ 顺时针方向为正）分别为：
   $$
   \mathcal{E}_{\text{tot}}(t) = -\frac{d\Phi_B}{dt} = \frac{\sqrt{3}}{4}B\omega a^2\sin(\omega t), \qquad I(t) = \frac{\mathcal{E}_{\text{tot}}(t)}{R} = \frac{\sqrt{3}B\omega a^2}{4R}\sin(\omega t)
   $$
2. **分析三段边各自的分段动生电动势 $e_{ij}$**：
   - **边 1–2**：恰位于旋转轴上，速度处处为零（$\vec{v} = \vec{0}$），不切割磁感线，故该边动生电动势为 **$e_{12} = 0$**；
   - **边 2–3 与边 3–1**：由关于过顶点 3 且垂直于边 1–2 的中垂线的对称性，边 2–3（从轴到顶点 3）与边 3–1（从顶点 3 回到轴）切割磁感线的情况完全对称，平分总动生电动势：
     $$
     e_{23} = e_{31} = \frac{1}{2}\mathcal{E}_{\text{tot}}(t) = \frac{\sqrt{3}}{8}B\omega a^2\sin(\omega t)
     $$
3. **计算各顶点间的电势差（应用含源欧姆定律 $V_{\text{end}} - V_{\text{start}} = e - I R_{\text{side}}$）**：
   每条边的电阻均为 $R_{\text{side}} = \frac{R}{3}$，感应电流引起的每边欧姆压降为 $I\frac{R}{3} = \frac{1}{3}\mathcal{E}_{\text{tot}}(t)$：
   - **顶点 1 与 2 之间**（沿 $1 \to 2$，$e_{12} = 0$）：
     $$
     V_2 - V_1 = e_{12} - I\frac{R}{3} = 0 - \frac{1}{3}\mathcal{E}_{\text{tot}}(t) = -\frac{\sqrt{3}}{12}B\omega a^2\sin(\omega t) \iff V_1 - V_2 = +\frac{\sqrt{3}}{12}B\omega a^2\sin(\omega t)
     $$
   - **顶点 2 与 3 之间**（沿 $2 \to 3$，$e_{23} = \frac{1}{2}\mathcal{E}_{\text{tot}}$）：
     $$
     V_3 - V_2 = e_{23} - I\frac{R}{3} = \left(\frac{1}{2} - \frac{1}{3}\right)\mathcal{E}_{\text{tot}}(t) = +\frac{\sqrt{3}}{24}B\omega a^2\sin(\omega t)
     $$
   - **顶点 3 与 1 之间**（沿 $3 \to 1$，$e_{31} = \frac{1}{2}\mathcal{E}_{\text{tot}}$）：
     $$
     V_1 - V_3 = e_{31} - I\frac{R}{3} = \left(\frac{1}{2} - \frac{1}{3}\right)\mathcal{E}_{\text{tot}}(t) = +\frac{\sqrt{3}}{24}B\omega a^2\sin(\omega t)
     $$
   （验证：$(V_2 - V_1) + (V_3 - V_2) + (V_1 - V_3) = 0$，静电势绕闭合回路一周增量为零，完全自洽！）。

---

**3. 交流长直螺线管内部小线圈的电磁感应（Exercise 11.3）**：

- **(a) 螺线管内部磁场 $B(t)$**：
  由右手定则，逆时针为正方向对应轴向磁场沿 $+\hat{z}$ 方向。代入 $n = 1000\text{ m}^{-1}, \ I_0 = 2\text{ A}$：
  $$
  B(t) = \mu_0 n I(t) = \mu_0 n I_0 \sin(\omega t) = (4\pi \times 10^{-7}) \times 1000 \times 2 \sin(100\pi t) = 8\pi \times 10^{-4}\sin(100\pi t)\text{ T} \approx 2.51 \times 10^{-3}\sin(100\pi t)\text{ T}
  $$
- **(b) 小圆环（半径 $r_2 = 0.03\text{ m} < r_1$）中的感应电动势 $\mathcal{E}(t)$**：
  穿过小圆环的磁通量为 $\Phi_B(t) = \pi r_2^2 B(t) = \mu_0 n I_0 \pi r_2^2 \sin(\omega t)$。求负时间导数：
  $$
  \mathcal{E}(t) = -\frac{d\Phi_B}{dt} = -\mu_0 n I_0 \pi r_2^2 \omega \cos(\omega t) = -(8\pi \times 10^{-4}) \times \pi(0.03)^2 \times (100\pi)\cos(100\pi t) \approx -2.23 \times 10^{-3}\cos(100\pi t)\text{ V}
  $$
- **(c) 小圆环中的最大感应电流 $I_{\text{ind, max}}$**：
  $$
  I_{\text{ind, max}} = \frac{|\mathcal{E}|_{\max}}{R} = \frac{\mu_0 n I_0 \pi r_2^2 \omega}{R} = \frac{2.23 \times 10^{-3}\text{ V}}{0.5\ \Omega} \approx 4.45 \times 10^{-3}\text{ A} = 4.45\text{ mA}
  $$
- **(d) 波形与相位关系**：螺线管电流 $I(t) = 2\sin(100\pi t)\text{ A}$ 为正弦波（周期 $T = 2\pi/\omega = 0.02\text{ s}$），而小圆环中的感应电流 $I_{\text{ind}}(t) = -4.45\cos(100\pi t)\text{ mA}$ 为负余弦波（相位比螺线管电流滞后 $90^\circ$ 或超前 $270^\circ$：在 $I(t)$ 过零点变化最快时感应电流达到极值，在 $I(t)$ 达到波峰/波谷变化率为零时感应电流为零）。

</details>

<details markdown="1">
<summary>Exercise 11.4, 11.5 & 11.6: Cylindrical Induced E-Field, Dual Solenoids Flux & Decelerating Rail Rod（圆柱形感生电场与粒子加速、双螺线管反号磁通与导轨滑杆减速）</summary>

**Problem Statement:**
- **Ex 11.4**: A uniform magnetic field is confined to a long cylindrical region of radius $R$, pointing out of the page and varying as $B(t) = B_0 e^{-t/\tau}$ ($B_0, \tau > 0$). (a) Find the magnitude of the induced electric field $E(r, t)$ for both $r < R$ and $r > R$. (b) Sketch $E(r)$ at fixed $t$; at what radius is $E$ maximized? (c) A charged particle ($q, m$) is released from rest at $t = 0$ inside a frictionless circular tube of radius $r_0$. Find the speed of the particle as $t \to \infty$ and its sense of circulation (for both $r_0 < R$ and $r_0 > R$).
- **Ex 11.5**: A thin stationary loop of resistance $R$ in the $xy$-plane encloses two non-overlapping long solenoids of radii $a_1, a_2$ ($a_1^2 < 2a_2^2$). For $0 \le t \le T$, $\vec{B}_1 = B_0\frac{t}{T}\hat{z}$ and $\vec{B}_2 = -B_0\left(\frac{t}{T}\right)^2\hat{z}$ ($B_0, T > 0$). Take $d\vec{S}$ along $+\hat{z}$. (a) Find $\mathcal{E}(t)$ and $I(t)$. (b) Find the time $t_*$ at which the current reverses, and explain with Lenz's law. (c) Find the net charge $Q = \int_0^T I\,dt$.
- **Ex 11.6**: Two parallel horizontal rails a distance $L$ apart are joined at one end by a resistor $R$ in a vertical uniform field $B$. A rod of mass $m$ slides without friction with initial speed $v_0$ away from $R$. (a) Find the current $i(v)$ and its sense from above. (b) Find $v(t)$ and the total distance traveled. (c) Find the total energy dissipated in $R$ and compare with $\frac{1}{2}mv_0^2$.

---

**中文解析：**

**1. 圆柱形指数衰减磁场的感生电场与圆管约束粒子的加速终态（Exercise 11.4，必考经典模型）**：

- **(a) 求区域内部（$r < R$）与外部（$r > R$）的感生电场大小 $E(r, t)$**：
  由轴对称性，感生电场线为同心圆。取半径为 $r$ 的同心圆作为积分回路（由于指向纸面外的磁场正在衰减，由楞次定律知感生电场 $\vec{E}$ 沿**逆时针方向**以维持向外磁通）。应用 $\oint \vec{E}\cdot d\vec{l} = 2\pi r E(r, t) = \left|-\frac{d\Phi_B}{dt}\right|$：
  - **当 $r < R$（磁场区内部）**：回路包围面积为 $\pi r^2$，$\Phi_B(r, t) = \pi r^2 B(t)$，故：
    $$
    2\pi r E(r, t) = \pi r^2 \left|\frac{dB}{dt}\right| = \frac{\pi r^2 B_0}{\tau}e^{-t/\tau} \implies E(r, t) = \frac{B_0 r}{2\tau}e^{-t/\tau} \qquad (r < R)
    $$
  - **当 $r > R$（磁场区外部）**：磁场仅存在于半径 $R$ 以内，回路包围的有效有场面积恒为 $\pi R^2$，$\Phi_B(r, t) = \pi R^2 B(t)$，故：
    $$
    2\pi r E(r, t) = \pi R^2 \left|\frac{dB}{dt}\right| = \frac{\pi R^2 B_0}{\tau}e^{-t/\tau} \implies E(r, t) = \frac{B_0 R^2}{2\tau r}e^{-t/\tau} \qquad (r \ge R)
    $$
- **(b) 空间分布特征与最大值半径**：
  在固定时刻 $t$，感生电场在圆柱内部随 $r$ **线性增长**（$E \propto r$），在圆柱外部随 $r$ **按反比衰减**（$E \propto 1/r$）。因此在圆柱边界 **$r = R$ 处感生电场达到最大值**，最大值为 $E_{\max}(t) = \dfrac{B_0 R}{2\tau}e^{-t/\tau}$。
- **(c) 圆形绝缘光滑管道内带电粒子在 $t \to \infty$ 时的终态速率与绕行方向**：
  光滑圆管提供径向约束力（平衡径向洛伦兹力与向心力），粒子切向运动仅受切向感生电场力 $F_\phi = q E(r_0, t) = m\frac{dv_\phi}{dt}$。对时间从 $t = 0$ 积分至 $\infty$（利用 $\int_0^\infty \frac{1}{\tau}e^{-t/\tau}\,dt = 1$）：
  $$
  v_\phi(\infty) = \frac{q}{m}\int_0^\infty E(r_0, t)\,dt = \begin{cases}
  \dfrac{|q| B_0 r_0}{2m}, & r_0 < R, \\[8pt]
  \dfrac{|q| B_0 R^2}{2m r_0}, & r_0 \ge R.
  \end{cases}
  $$
  **绕行方向**：由于感生电场 $\vec{E}$ 沿逆时针方向，若 **$q > 0$（正电荷）**则粒子沿**逆时针**方向旋转；若 **$q < 0$（负电荷）**则粒子沿**顺时针**方向旋转。

---

**2. 包围两个反向时变螺线管的静止回路与感应电量定理（Exercise 11.5）**：

- **(a)** 回路包围的总磁通量为两个螺线管各自磁通量的代数和：
  $$
  \Phi_B(t) = \pi a_1^2 B_1(t) + \pi a_2^2 B_2(t) = \pi B_0\left[ a_1^2 \frac{t}{T} - a_2^2 \left(\frac{t}{T}\right)^2 \right]
  $$
  由法拉第定律求得感应电动势与感应电流（逆时针为正）：
  $$
  \mathcal{E}(t) = -\frac{d\Phi_B}{dt} = \frac{\pi B_0}{T}\left( \frac{2a_2^2}{T}t - a_1^2 \right), \qquad I(t) = \frac{\mathcal{E}(t)}{R} = \frac{\pi B_0}{RT}\left( \frac{2a_2^2}{T}t - a_1^2 \right)
  $$
- **(b) 电流反向时刻 $t_*$ 及楞次定律解释**：
  令 $I(t_*) = 0$，解得：
  $$
  t_* = \frac{a_1^2}{2a_2^2}T \qquad (\text{因 } a_1^2 < 2a_2^2, \text{ 故 } 0 < t_* < T)
  $$
  - 在 $0 \le t < t_*$ 阶段：线性增长的正向磁通量 $\Phi_1$ 变化率大于二次增长的反向磁通量 $|\Phi_2|$ 变化率，总向外磁通量 $\Phi_B$ 正在增加（$\frac{d\Phi_B}{dt} > 0$），由楞次定律知感应电流必产生向里的磁场以阻碍增加，故电流为**顺时针**（$I < 0$）；
  - 在 $t_* < t \le T$ 阶段：二次项 $|\Phi_2|$ 的增长率超过 $\Phi_1$，总向外磁通量 $\Phi_B$ 转为减小（或向里磁通增加，$\frac{d\Phi_B}{dt} < 0$），感应电流产生向外的磁场，故翻转为**逆时针**（$I > 0$）。
- **(c) 流过回路某截面的总净感应电荷量 $Q$**：
  直接积分（或利用普适感应电量公式 $Q = \int_0^T I\,dt = -\frac{\Phi_B(T) - \Phi_B(0)}{R}$）：
  $$
  Q = \int_0^T \frac{\pi B_0}{RT}\left( \frac{2a_2^2}{T}t - a_1^2 \right)dt = \frac{\pi B_0}{R}\left(a_2^2 - a_1^2\right)
  $$

---

**3. 水平导轨滑杆在磁阻尼下的指数减速、滑行总距离与能量守恒（Exercise 11.6）**：

- **(a)** 当滑杆以速度 $v$ 远离电阻运动时，回路面积增大，向上的磁通量 $\Phi_B = BLx$ 增加。由法拉第定律与楞次定律，从上往下看（Seen from above），感应电流沿**顺时针方向**（产生向下的感应磁场），电流大小为：
  $$
  i(v) = \frac{BLv}{R}
  $$
- **(b) 速度演化 $v(t)$ 与滑行总距离 $x_{\max}$**：
  滑杆受到指向电阻方向的安培制动力 $F_B = -iLB = -\frac{B^2 L^2}{R}v$。由牛顿第二定律：
  $$
  m\frac{dv}{dt} = -\frac{B^2 L^2}{R}v \implies v(t) = v_0 \exp\left(-\frac{B^2 L^2}{mR}t\right)
  $$
  对速度从 $t = 0$ 积分至 $\infty$，得滑杆停止前滑行的总距离：
  $$
  x_{\max} = \int_0^\infty v(t)\,dt = v_0 \int_0^\infty \exp\left(-\frac{B^2 L^2}{mR}t\right)dt = \frac{m R v_0}{B^2 L^2}
  $$
  *（巧解：也可由动量定理 $-B L \int i\,dt = -BL q_{\text{tot}} = -BL\frac{BL x_{\max}}{R} = 0 - mv_0$ 一步秒解 $x_{\max} = \frac{mRv_0}{B^2 L^2}$！）*
- **(c) 电阻上耗散的总焦耳热**：
  $$
  H = \int_0^\infty i^2(t)R\,dt = \frac{B^2 L^2 v_0^2}{R}\int_0^\infty \exp\left(-\frac{2B^2 L^2}{mR}t\right)dt = \frac{B^2 L^2 v_0^2}{R}\cdot\frac{mR}{2B^2 L^2} = \frac{1}{2}mv_0^2
  $$
  总耗散焦耳热精确等于滑杆的初始动能 $\frac{1}{2}mv_0^2$。

</details>

<details markdown="1">
<summary>Exercise 11.7, 11.8 & 11.9: Faraday Disk Generator, Exterior Solenoid Loops & Path-Dependent Integrals（法拉第圆盘发电机、螺线管外扇形回路与感生电场路径依赖性）</summary>

**Problem Statement:**
- **Ex 11.7 (Faraday Disk Dynamo)**: A thin conducting disk of radius $a$ turns with constant angular speed $\omega$ about the $z$ axis (counterclockwise from $+z$) in a uniform field $\vec{B} = B\hat{z}$ ($B > 0$). Sliding contacts at the center and the rim are joined through a resistor $R$.
  (a) Using the magnetic force on a positive charge carried round with the disk, find the emf between the center and the rim, and say which is at higher potential.
  (b) Find the current, the magnetic torque on the disk, and the applied torque needed to keep $\omega$ constant. Show that mechanical power supplied equals power dissipated in $R$.
  (c) Consider the closed path made of the external circuit, a radius drawn on the disk at $t = 0$ that turns with the disk, and the arc of the rim swept since then. Find the rate at which flux through this path changes, and compare with (a).
- **Ex 11.8**: A long solenoid of radius $a$ ($n$ turns/m, axis along $z$) carries $i(t) = kt$ ($k > 0$, counterclockwise from $+z$), giving $\vec{B} = \mu_0 nkt\hat{z}$ inside and $\vec{0}$ outside. The induced electric field has magnitude $E = \mu_0 nkr/2$ ($r < a$) and $E = \mu_0 nka^2/(2r)$ ($r > a$).
  (a) Write $\vec{E}$ in Cartesian components (including sense), and verify $\nabla\times\vec{E} = -\partial\vec{B}/\partial t$ inside and outside.
  (b) A circular wire loop of radius $b > a$ and resistance $R$ is centered on the axis. Find the current in it and its sense from $+z$.
  (c) Another loop outside the solenoid is made of two circular arcs of radii $b_1 < b_2$ ($a < b_1 < b_2$, angle $\alpha$) joined by two radial segments. Find its emf by integrating $\vec{E}$ around it, and compare with Faraday's law. Is $\vec{E}$ zero on this loop?
- **Ex 11.9**: A long solenoid of radius $b$ along $z$ produces $\vec{B} = \beta t\hat{z}$ ($\beta > 0$) inside and zero outside. In the plane $z = 0$, let $P = (a, 0)$ and $Q = (-a, 0)$ with $0 < a < b$.
  (a) Find the induced electric field on the circle $r = a$.
  (b) Find $\int_P^Q \vec{E}\cdot d\vec{l}$ along the upper semicircle ($y > 0$), along the lower semicircle ($y < 0$), and along the straight diameter, each from $P$ to $Q$.
  (c) Can a potential $V$ with $\vec{E} = -\nabla V$ be defined inside? Relate the difference between the two semicircle integrals to Faraday's law.

---

**中文解析：**

**1. 法拉第同极圆盘发电机（Faraday Homopolar Generator，Exercise 11.7，经典必考名题）**：

- **(a)** 在圆盘上距中心为 $r$ 处，随盘逆时针旋转的正电荷 $q$ 具有切向速度 $\vec{v} = \omega r\,\hat{\phi}$。在磁场 $\vec{B} = B\hat{z}$ 中，它受到的磁洛伦兹力为：
  $$
  \vec{F}_B = q(\omega r\,\hat{\phi}) \times (B\hat{z}) = +q\omega B r\,\hat{r} \qquad (\text{沿径向指向圆盘边缘 Rim})
  $$
  因此单位正电荷从盘心移动到边缘所受非静电力做的功（即动生电动势）为：
  $$
  \mathcal{E} = \int_0^a (\vec{v}\times\vec{B})\cdot d\vec{r} = \int_0^a \omega B r\,dr = \frac{1}{2}B\omega a^2
  $$
  由于磁力将正电荷推向圆盘边缘，**圆盘边缘（Rim）处于高电势**，盘心（Center）处于低电势。
- **(b)** 闭合回路中的稳恒电流为 $I = \frac{\mathcal{E}}{R} = \dfrac{B\omega a^2}{2R}$（在圆盘内部沿径向从中心流向边缘）。
  径向微元段 $dr$ 所受安培力为 $d\vec{F}_{\text{Amp}} = I\,dr\,\hat{r} \times (B\hat{z}) = -IB\,dr\,\hat{\phi}$（顺时针方向，阻碍圆盘逆时针旋转），对转轴产生的微元制动磁力矩为 $d\tau_B = -r\,dF_{\text{Amp}} = -IB r\,dr$。从 $0$ 到 $a$ 积分得总磁力矩：
  $$
  \tau_B = -\int_0^a IB r\,dr = -\frac{1}{2}IB a^2 = -\frac{B^2 \omega a^4}{4R} \quad (\text{顺时针制动})
  $$
  因此，外力维持恒定角速度 $\omega$ 所需施加的驱动力矩大小为 $\tau_{\text{app}} = +\frac{1}{2}IB a^2 = \dfrac{B^2 \omega a^4}{4R}$（逆时针）。
  验证功率守恒：外力输入的机械功率为 $P_{\text{mech}} = \tau_{\text{app}}\omega = \frac{B^2 \omega^2 a^4}{4R}$，而电阻 $R$ 上的热耗散功率为 $P_{\text{diss}} = I^2 R = \left(\frac{B\omega a^2}{2R}\right)^2 R = \frac{B^2 \omega^2 a^4}{4R}$，两者完全相等！
- **(c) 扇形扫过面积的磁通变化率**：
  在时间 $t$ 内，印在圆盘上的那条导电半径转过了角度 $\theta(t) = \omega t$，与滑动触头之间的扇形面积为 $A(t) = \frac{1}{2}a^2\theta(t) = \frac{1}{2}\omega a^2 t$，穿过该闭合回路的磁通量为 $\Phi_B(t) = B A(t) = \frac{1}{2}B\omega a^2 t$。其变化率为：
  $$
  \frac{d\Phi_B}{dt} = \frac{1}{2}B\omega a^2 = \mathcal{E}
  $$
  与 (a) 中由洛伦兹力积分算出的动生电动势完全一致！

---

**2. 螺线管内外的旋度验证与管外闭合环路分析（Exercise 11.8）**：

- **(a)** 由于管内沿 $+\hat{z}$ 的磁场随时间线性增加（$\frac{\partial\vec{B}}{\partial t} = \mu_0 nk\hat{z}$），由楞次定律知感生电场从 $+z$ 看沿**顺时针方向**（$-\hat{\phi}$）。在直角坐标系中，顺时针切向单位矢量为 $-\hat{\phi} = \frac{y\hat{x} - x\hat{y}}{r}$（其中 $r = \sqrt{x^2 + y^2}$）。代入 $E(r)$ 的表达式：
  - **管内（$r < a$）**：
    $$
    \vec{E}_{\text{in}}(x, y) = \frac{\mu_0 nk}{2}(y\hat{x} - x\hat{y}) \implies \nabla\times\vec{E}_{\text{in}} = \hat{z}\left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right) = \hat{z}\frac{\mu_0 nk}{2}(-1 - 1) = -\mu_0 nk\,\hat{z} = -\frac{\partial\vec{B}}{\partial t}
    $$
  - **管外（$r > a$）**：
    $$
    \vec{E}_{\text{out}}(x, y) = \frac{\mu_0 nk a^2}{2}\left(\frac{y}{x^2 + y^2}\hat{x} - \frac{x}{x^2 + y^2}\hat{y}\right)
    $$
    求旋度：$\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} = \frac{\mu_0 nka^2}{2}\left[ -\frac{(x^2+y^2) - 2x^2}{(x^2+y^2)^2} - \frac{(x^2+y^2) - 2y^2}{(x^2+y^2)^2} \right] = 0 \implies \nabla\times\vec{E}_{\text{out}} = \vec{0} = -\frac{\partial\vec{B}_{\text{out}}}{\partial t}$。
- **(b) 包围螺线管的同心大圆环（$b > a$）中的感应电流**：
  尽管大圆环导线所在位置（$r = b > a$）处的磁场处处为零（$B = 0$），但那里存在非零的感生电场 $E(b) = \frac{\mu_0 nka^2}{2b}$（或从全局看，圆环内部包围了螺线管横截面内的变化磁通量 $\Phi_B = \pi a^2 \mu_0 nkt$）：
  $$
  |\mathcal{E}| = 2\pi b E(b) = \pi a^2 \mu_0 nk \implies I = \frac{\pi a^2 \mu_0 nk}{R} \quad (\text{从 }+z\text{ 看沿顺时针方向})
  $$
- **(c) 完全位于螺线管外部的扇形闭合回路（$a < b_1 < b_2$）**：
  沿扇形回路积分 $\oint \vec{E}\cdot d\vec{l}$：
  - 两条径向直边：因 $\vec{E}$ 沿切向 $\hat{\phi}$ 与径向 $d\vec{r}$ 处处垂直，线积分为 $0$；
  - 内圆弧（半径 $b_1$，弧长 $b_1\alpha$）与外圆弧（半径 $b_2$，弧长 $b_2\alpha$）：绕行方向相反，一正一负：
    $$
    \mathcal{E} = \oint \vec{E}\cdot d\vec{l} = E(b_1)(b_1\alpha) - E(b_2)(b_2\alpha) = \frac{\mu_0 nka^2}{2b_1}(b_1\alpha) - \frac{\mu_0 nka^2}{2b_2}(b_2\alpha) = 0
    $$
  这与法拉第定律完全吻合，因为该扇形回路完全位于管外无磁场区，其所包围的磁通量恒为零（$\Phi_B \equiv 0 \implies \mathcal{E} = 0$）。注意：**虽然回路上的总感应电动势 $\mathcal{E} = 0$，但回路上每一点处的感生电场 $\vec{E}$ 均不为零**！

---

**3. 螺线管内部非保守感生电场沿不同路径的线积分对比（Exercise 11.9，必考重点）**：

- **(a)** 在半径 $r = a < b$ 的圆周上，由 $2\pi a E(a) = \pi a^2 \frac{dB}{dt} = \pi a^2 \beta$，解得感生电场大小为：
  $$
  E(a) = \frac{1}{2}\beta a \qquad (\text{方向沿顺时针切向 } -\hat{\phi})
  $$
  在任意半径 $r < b$ 处，矢量表达式为 $\vec{E}(x, y) = \frac{1}{2}\beta(y\hat{x} - x\hat{y})$。
- **(b) 从点 $P(a, 0)$ 到点 $Q(-a, 0)$ 沿三条不同路径的线积分 $\int_P^Q \vec{E}\cdot d\vec{l}$**：
  1. **沿上半圆弧（$y > 0$，从 $P$ 逆时针走到 $Q$，弧长 $\pi a$）**：
     路径方向（逆时针）与感生电场方向（顺时针）处处**相反**，故：
     $$
     \int_{P \to Q, \text{ upper}} \vec{E}\cdot d\vec{l} = -E(a)\cdot (\pi a) = -\frac{1}{2}\pi\beta a^2
     $$
  2. **沿下半圆弧（$y < 0$，从 $P$ 顺时针走到 $Q$，弧长 $\pi a$）**：
     路径方向（顺时针）与感生电场方向（顺时针）处处**相同**，故：
     $$
     \int_{P \to Q, \text{ lower}} \vec{E}\cdot d\vec{l} = +E(a)\cdot (\pi a) = +\frac{1}{2}\pi\beta a^2
     $$
  3. **沿水平直径直线段（$y = 0$，从 $x = a$ 走到 $x = -a$，$d\vec{l} = dx\,\hat{x}$）**：
     在直径 $y = 0$ 上，感生电场为 $\vec{E}(x, 0) = -\frac{1}{2}\beta x\,\hat{y}$，与水平路径微元 $dx\,\hat{x}$ 处处**垂直**（$\vec{E} \perp d\vec{l}$），故：
     $$
     \int_{P \to Q, \text{ diameter}} \vec{E}\cdot d\vec{l} = 0
     $$
- **(c) 电势不存在性与法拉第定律关联**：
  由于从同一起点 $P$ 到同一终点 $Q$ 沿三条不同路径的线积分给出了三个截然不同的数值（$-\frac{1}{2}\pi\beta a^2, \ +\frac{1}{2}\pi\beta a^2, \ 0$），线积分严重依赖于路径，因此**在螺线管内部绝不可能定义满足 $\vec{E} = -\nabla V$ 的标量电势 $V$**。
  若取“从 $P$ 沿上半圆弧逆时针到 $Q$，再从 $Q$ 沿下半圆弧逆时针回到 $P$”构成一个完整的逆时针闭合圆周（面积 $\pi a^2$），其闭合环流恰等于上半圆积分减去下半圆积分：
  $$
  \oint_{\text{CCW}} \vec{E}\cdot d\vec{l} = \int_{\text{upper}} \vec{E}\cdot d\vec{l} - \int_{\text{lower}} \vec{E}\cdot d\vec{l} = -\frac{1}{2}\pi\beta a^2 - \frac{1}{2}\pi\beta a^2 = -\pi a^2 \beta = -\frac{d\Phi_B}{dt}
  $$
  这正是法拉第电磁感应定律！

</details>