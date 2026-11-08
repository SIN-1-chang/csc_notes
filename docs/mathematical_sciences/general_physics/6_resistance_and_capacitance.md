# Chapter 6: Resistance and Capacitance（电阻与电容）

!!! abstract
    General Physics II (Electromagnetism) | 第六章课堂与讲义笔记
    
    参考：
    
    - Lecture 6: *Resistance and Capacitance* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 6: *Resistance and Capacitance*
    - Halliday, Resnick & Krane, *Physics*, Chapters 29 & 30

## 1 稳恒电流与电流密度 (Steady Current and Current Density)

### 1.1 电流与稳恒条件

当对导体施加外电场时，导体内的传导电子（Conduction electrons）在静电力驱动下产生宏观定向运动，形成**电流**（Electric Current）。设无穷小时间间隔 $dt$ 内穿过某假想截面的净电荷量为 $dq$，则电流 $I$（课件亦记为 $i$）定义为：

$$
I = \frac{dq}{dt} \iff q = \int_{t_1}^{t_2} I\,dt
$$

由于电荷 $q$ 与时间 $t$ 均为标量，**电流 $I$ 是标量（Scalar）**，其国际单位制（SI base unit）为**安培**（Ampere，$\text{A} = \text{C/s}$）。在电路图中标注的电流箭头仅代表正载流子（Positive charge carriers）等效流动的方向（与实际带负电的电子定向移动方向相反）。

本章重点研究**稳恒电流**（Steady Current），即电流的宏观性质不随时间变化（$\frac{\partial\rho}{\partial t} = 0$）。在稳恒条件下，由局域电荷守恒可知，无论导体截面形状如何变化或截面如何倾斜，**穿过导体任意完整横截面的电流 $I$ 处处相等**；在电路分支节点处则满足**节点定律**（Junction Rule）：流入节点的电流之和等于流出节点的电流之和（$i_0 = i_1 + i_2$）。

### 1.2 电流密度矢量与漂移速度

对于非均匀或变截面导体，虽然总电流 $I$ 处处相同，但电流在横截面上的空间分布可能不同。为此定义空间点 $\vec{r}$ 处的**电流密度**（Current Density，矢量 $\vec{j}$ 或 $\vec{J}$，单位 $\text{A/m}^2$）：其方向为正电荷载流子的局部运动方向（即令单位面积电流 $\lim_{|\delta\vec{S}|\to 0}\frac{\delta I}{|\delta\vec{S}|}$ 取得最大值的面积微元法向 $\hat{n}$），其大小为垂直穿过单位面积的电流。由此，穿过任意曲面 $S$ 的总电流为矢量点乘的曲面积分：

$$
I = \int_S \vec{j} \cdot d\vec{S} \qquad (\text{对比电通量公式：} \Phi = \int_S \vec{E} \cdot d\vec{S})
$$

**微观漂移速度（Drift Velocity, $\vec{v}_d$）与热运动速率（Thermal Speed, $v_{\text{th}}$）**：

1. **无外场时的随机热运动**：当导体未通电时，传导电子作剧烈的无规则热运动，净位移为零。若按经典理想气体能量均分定理 $\frac{1}{2}mv_{\text{th}}^2 = \frac{3}{2}k_B T$ 估算，室温（$T = 300\text{ K}$）下电子的热运动速率高达 $v_{\text{th}} = \sqrt{3k_B T/m} \approx 1.17 \times 10^5\text{ m/s}$（若计入量子力学泡利不相容原理，金属费米面电子的实际速率还要大十倍以上，约 $10^6\text{ m/s}$）。
2. **有外场时的定向漂移**：施加电场 $\vec{E}$ 后，电子在高速热运动背景上叠加了一个逆着电场方向的微小平均速度，称为**漂移速度** $\vec{v}_d$（典型值仅约 $10^{-4}\text{ m/s}$，比热运动慢约 $9$ 个数量级）。
3. **电流密度的微观表达式**：设导体内载流子数密度（Number density）为 $n$，截面积为 $S$。在 $\Delta t$ 时间内穿过截面的电子数为 $N = n S v_d \Delta t$，故电流大小为 $I = \frac{Ne}{\Delta t} = neSv_d$。写成矢量形式即为：
   $$
   \vec{j} = n q \vec{v}_d = -n e \vec{v}_d \qquad (\text{对带电 }-e\text{ 的电子，}\vec{j}\text{ 与 }\vec{v}_d\text{ 反向})
   $$

---

## 2 电阻、欧姆定律与连续性方程 (Resistance, Ohm's Law and Continuity Equation)

### 2.1 电阻、电阻率与欧姆定律

宏观上，当导体两端施加电势差 $V$ 并产生电流 $I$ 时，定义导体的**电阻**（Resistance，SI 单位为欧姆 Ohm，$\Omega = \text{V/A}$）为：

$$
R = \frac{V}{I}
$$

为了剥离几何尺寸的影响以表征材料本身的导电能力，引入材料的**电导率**（Conductivity, $\sigma$，单位 $\text{S/m} = (\Omega\cdot\text{m})^{-1}$）与**电阻率**（Resistivity, $\rho_e$，课件亦记为 $\rho$，单位 $\Omega\cdot\text{m}$），二者互为倒数（$\rho_e = \sigma^{-1}$），并满足局域**欧姆定律的微分形式**：

$$
\vec{j} = \sigma \vec{E} \iff \vec{E} = \rho_e \vec{j}
$$

对于长度为 $L$、横截面积为 $S$（或 $A$）的均匀柱体导体，由 $V = EL$ 与 $I = jS = \sigma E S$，即可导出宏观电阻与材料电阻率的关系：

$$
R = \frac{V}{I} = \frac{EL}{\sigma E S} = \frac{L}{\sigma S} = \rho_e \frac{L}{S}
$$

*注：电阻 $R$ 是特定几何形状**物体（Object）**的属性，而电阻率 $\rho_e$ 是**材料（Material）**的本征属性。若材料的 $\rho_e$ 不随外加电场或电压变化，则称该器件遵循**欧姆定律**（Ohm's Law，如正常条件下的金属）；而半导体 $p\text{-}n$ 结二极管（Diode）的 $I\text{-}V$ 曲线呈指数非线性，不遵循欧姆定律。*

### 2.2 自由电子模型（Drude Model）对欧姆定律的微观解释

在金属自由电子模型中，传导电子不断与金属晶格正离子发生碰撞（注：电子与电子之间的碰撞满足总动量守恒，本身不会改变宏观总电流；真正产生电阻的是**电子与金属离子的碰撞**）。

1. **碰撞失忆假设与平均自由时间 $\tau$**：由于碰撞极其频繁且散射方向随机，可认为每次碰撞后电子都“失去了对先前漂移速度的全部记忆”（Loses memory），以随机方向重新出发。设两次连续碰撞之间的平均时间间隔为**平均自由时间**（Mean free time, $\tau$）。
2. **漂移速度与电导率推导**：在电场 $\vec{E}$ 中，电子（质量 $m$，电荷 $-e$）获得的加速度为 $\vec{a} = -\frac{e\vec{E}}{m}$。在任意时刻，电子自上一次碰撞以来平均经历了时间 $\tau$，因此对所有电子求平均后获得的漂移速度为：
   $$
   \vec{v}_d = \vec{a}\tau = -\frac{e\vec{E}}{m}\tau
   $$
   将其代入 $\vec{j} = -ne\vec{v}_d$，立即得到**德鲁德电导率与电阻率公式**：
   $$
   \vec{j} = -ne\left(-\frac{e\vec{E}}{m}\tau\right) = \frac{ne^2\tau}{m}\vec{E} \implies \sigma = \frac{ne^2\tau}{m}, \qquad \rho_e = \frac{1}{\sigma} = \frac{m}{ne^2\tau}
   $$
   在常温常压下，金属中的载流子浓度 $n$ 与平均自由时间 $\tau$ 均与外电场 $E$ 无关，因此 $\sigma$ 和 $\rho_e$ 为常数，这从微观上解释了金属为何遵循欧姆定律。

!!! warning "经典图像的局限：电阻率的温度依赖关系（Classical vs. Quantum）"
    设电子两次碰撞间走过的平均距离——**平均自由程**（Mean free path）为 $\lambda = v_{\text{th}}\tau$。若按经典图像假设 $\lambda$ 与温度 $T$ 无关，且电子速率为经典热运动速率 $v_{\text{th}} = \sqrt{3k_B T/m} \propto \sqrt{T}$，则会推出 $\tau = \frac{\lambda}{v_{\text{th}}} \propto T^{-1/2}$，进而预言金属电阻率 $\rho_e = \frac{m}{ne^2\tau} \propto \sqrt{T}$（随温度的平方根增长）。
    然而实验测得**真实金属在室温附近的电阻率随温度近似呈线性增长（$\rho_e \propto T$）**！这一矛盾表明经典气体模型失效，必须引入量子力学（费米面电子速率 $v_F$ 与温度无关，而晶格热振动声子散射截面正比于 $T$）才能正确解释。

### 2.3 电荷守恒与连续性方程 (Equation of Continuity)

电荷在任何物理过程中均严格守恒。考察空间中任意固定的闭合曲面 $S$（包围体积 $V$）：在单位时间内，穿过闭合面 $S$ 向外流出的总电流 $\oint_S \vec{j}\cdot d\vec{S}$，必然等于体积 $V$ 内部总电荷量 $\int_V \rho\,dV$ 的减少率：

$$
\frac{d}{dt}\int_V \rho(\vec{r}, t)\,dV + \oint_S \vec{j}(\vec{r}, t) \cdot d\vec{S} = 0
$$

利用第四章的散度定理（Divergence theorem）将面积分转化为体积分 $\oint_S \vec{j}\cdot d\vec{S} = \int_V (\nabla\cdot\vec{j})\,dV$，并将时间导数移入积分号内：

$$
\int_V \left(\frac{\partial\rho}{\partial t} + \nabla \cdot \vec{j}\right) dV = 0
$$

由于体积 $V$ 是任意选取的，被积函数必须处处为零，从而得到电磁学中极其重要的**连续性方程（微分形式）**：

$$
\frac{\partial\rho}{\partial t} + \nabla \cdot \vec{j} = 0 \iff \nabla \cdot \vec{j} = -\frac{\partial\rho}{\partial t}
$$

特别地，对于**稳恒电流**（Steady current），空间各点电荷密度不随时间变化（$\frac{\partial\rho}{\partial t} = 0$），故恒有 $\nabla\cdot\vec{j} = 0$。

---

## 3 电容器与电容计算 (Capacitors and Capacitance)

### 3.1 电容的定义与几何决定性

由两个相互孤立的导体（称为极板 Plates）组成的系统称为**电容器**（Capacitor，广泛用于调谐电路、电源滤波及 DRAM/闪光灯储能）。当两导体分别携带等量异号电荷 $+q$ 和 $-q$ 时，每个导体各自成为等势体，两导体之间存在电势差 $V > 0$（注意：电容器的带电量 $q$ 指的是**其中一个极板所带电荷量的绝对值**，$V$ 指两极板间电势差的绝对值）。

实验与理论均表明，$q$ 与 $V$ 恒成正比，比例系数 $C$ 称为电容器的**电容**（Capacitance，SI 单位为**法拉** Farad，$1\text{ F} = 1\text{ C/V}$；常用微法 $1\ \mu\text{F} = 10^{-6}\text{ F}$ 与皮法 $1\text{ pF} = 10^{-12}\text{ F}$）：

$$
q = CV \iff C = \frac{q}{V}
$$

**为什么电容 $C$ 与带电量 $q$ 及电压 $V$ 无关？**
根据第五章拉普拉斯方程的线性叠加性与唯一性定理，当固定形状和相对位置的两导体间为真空（或线性电介质）时，若将两极板上的电荷量翻倍（$\pm q \to \pm 2q$），则空间各处的电场强度 $\vec{E}$ 精确翻倍，从而两极板间的线积分电势差 $V$ 也精确翻倍。因此比值 $C = q/V$ 完全独立于 $q$ 和 $V$，**仅由导体的几何尺寸（形状、大小、相对位置）以及极板间的电介质材料决定**，通用量纲形式可写为 $C = \epsilon_0 L_{\text{eff}}$（$L_{\text{eff}}$ 为等效特征长度）。

### 3.2 电容计算的通用四步法与三大经典模型

忽略极板边缘电场向外弯曲发散的**边缘效应**（Fringing / Edge effect），计算任意给定几何构型电容器电容 $C$ 的标准四步法如下：

1. **设电荷**：假设两极板分别带有等量异号电荷 $+q$ 和 $-q$；
2. **求电场**：利用对称性与高斯定理 $\epsilon_0\oint \vec{E}\cdot d\vec{A} = q_{\text{enc}}$（或镜像法）求出两极板之间的电场分布 $\vec{E}(\vec{r})$；
3. **算电压**：任选一条从负极板到正极板的积分路径，计算电势差绝对值 $V = -\int_-^+ \vec{E}\cdot d\vec{s} = \int_+^- \vec{E}\cdot d\vec{l}$；
4. **得电容**：代入定义式 $C = \dfrac{q}{V}$ 消去 $q$ 即得电容。

三大经典真空电容器模型的推导过程与结论对比如下表（Examples 6.1, 6.2 & 6.3）：

| 电容器几何构型 | 极板间电场强度 $E$ | 极板间电势差 $V = \int_+^- \vec{E}\cdot d\vec{l}$ | 电容公式 $C = q/V$ |
| :--- | :--- | :--- | :--- |
| **1. 平行板电容器**<br>（Parallel-Plate，面积 $S$，间距 $d$） | $E = \dfrac{\sigma_s}{\epsilon_0} = \dfrac{q}{\epsilon_0 S}$<br>（板间匀强场，板外为 $0$） | $V = Ed = \dfrac{qd}{\epsilon_0 S}$ | $C = \dfrac{\epsilon_0 S}{d}$<br>（单位面积电容 $\dfrac{C}{S} = \dfrac{\epsilon_0}{d}$） |
| **2. 同轴圆柱形电容器**<br>（Cylindrical，长 $L \gg b > a$） | $E(r) = \dfrac{\lambda}{2\pi\epsilon_0 r} = \dfrac{q}{2\pi\epsilon_0 L r}$<br>（同轴圆柱高斯面，$a < r < b$） | $V = \displaystyle\int_a^b E(r)\,dr = \frac{q}{2\pi\epsilon_0 L}\ln\left(\frac{b}{a}\right)$ | $C = \dfrac{2\pi\epsilon_0 L}{\ln(b/a)}$<br>（单位长度电容 $\dfrac{C}{L} = \dfrac{2\pi\epsilon_0}{\ln(b/a)}$） |
| **3. 孤立导体球电容器**<br>（Isolated Sphere，半径 $a$，外极板在 $\infty$） | $E(r) = \dfrac{q}{4\pi\epsilon_0 r^2} \quad (r > a)$ | $V = \displaystyle\int_a^\infty E(r)\,dr = \frac{q}{4\pi\epsilon_0 a}$ | $C = 4\pi\epsilon_0 a$<br>（同心球壳 $b \to \infty$ 的极限） |

---

## 4 电介质中的静电场与材料物理拓展 (Dielectrics, Semiconductors & Superconductors)

### 4.1 电介质、电位移矢量 $\vec{D}$ 与极化强度 $\vec{P}$

在金属导体中，自由电子的移动可完全屏蔽外电场，使导体内 $\vec{E} = \vec{0}$。而在绝缘体或**电介质**（Dielectrics）中，电荷被束缚在原子或分子内部，电场可以穿透介质。为了避免处理在 $1\text{ \AA}$ 微观尺度上剧烈震荡的微观电场 $\vec{E}_m$，我们在宏观上考察其空间平均值 $\vec{E} = \langle\vec{E}_m\rangle$。

1. **微观极化机制与电极化强度 $\vec{P}$**：
   在外电场作用下，电介质中原本电中性的分子正负电荷中心发生相对偏移，形成微观电偶极子（Electric dipoles）。定义单位体积内的电偶极矩矢量为**电极化强度**（Polarization，矢量 $\vec{P}$）。极化会在介质内部和表面产生**束缚电荷**（Bound charge，又称极化电荷），其体密度与面密度分别为：
   $$
   \rho_{\text{bound}} = -\nabla \cdot \vec{P}, \qquad \sigma_{\text{bound}} = \vec{P} \cdot \hat{n}
   $$
   （因此对于均匀极化的电介质平板，$\nabla\cdot\vec{P} = 0$，内部无体束缚电荷，仅有表面束缚电荷 $\sigma_b = \vec{P}\cdot\hat{n}$）。
2. **电位移矢量 $\vec{D}$ 与介质中的高斯定理**：
   定义**电位移矢量**（Electric Displacement Vector）$\vec{D}$ 为：
   $$
   \vec{D} \equiv \epsilon_0 \vec{E} + \vec{P}
   $$
   对于均匀各向同性线性电介质（Linear dielectric），有 $\vec{D} = \epsilon \vec{E} = \epsilon_r \epsilon_0 \vec{E}$，其中 $\epsilon$ 称为材料的**介电常数**（Permittivity），无量纲比值 $\epsilon_r = \frac{\epsilon}{\epsilon_0} \ge 1$ 称为**相对介电常数**或**介电常数**（Dielectric constant / Relative permittivity，真空中 $\epsilon_r = 1$）。
   引入 $\vec{D}$ 后，**电介质中的高斯定理**（积分形式与微分形式）可统一写为仅包含**自由电荷**（Free charge，$q_{\text{free}}$ 与 $\rho_{\text{free}}$，不包含极化束缚电荷）的简洁形式：
   $$
   \oint_S \vec{D} \cdot d\vec{S} = q_{\text{free}}, \qquad \nabla \cdot \vec{D} = \rho_{\text{free}}
   $$
   当整个高斯面所在的介质均匀（$\epsilon$ 处处相同）时，也可直接写为 $\oint_S \vec{E}\cdot d\vec{S} = \frac{q_{\text{free}}}{\epsilon_r \epsilon_0}$。

**经典结论（Example 6.4：充满电介质的平行板电容器）**：
在极板自由面电荷密度 $\pm\sigma_s$ 不变的平行板电容器中填满相对介电常数为 $\epsilon_r$ 的电介质，由高斯定理 $\oint \vec{D}\cdot d\vec{S} = q_{\text{free}}$ 可知电位移矢量保持不变（$D = \sigma_s$），因此介质内宏观电场减弱为原来的 $1/\epsilon_r$，电容增大为真空时的 $\epsilon_r$ 倍：

$$
D = \sigma_s \implies E = \frac{D}{\epsilon} = \frac{\sigma_s}{\epsilon_r \epsilon_0} \implies V = Ed = \frac{\sigma_s d}{\epsilon_r \epsilon_0} \implies C = \frac{\epsilon_r \epsilon_0 S}{d} = \epsilon_r C_{\text{vac}}
$$

<details markdown="1">
<summary>Appendices 6A, 6B & 6C: 半导体物理、超导 BCS 理论与巴丁（John Bardeen）</summary>

**1. 半导体的导电特征与掺杂（Appendix 6A: Semiconductors）**

- **本征载流子浓度与负温度系数**：德鲁德公式 $\rho = \frac{m}{ne^2\tau}$ 同样适用于半导体（如 $\text{Si}, \text{Ge}, \text{GaAs}$）。与金属不同，半导体在室温下的本征载流子浓度 $n_i$ 极小（故室温电阻率远高于铜），但随着温度 $T$ 升高，热激发使更多价电子跃迁成为自由载流子，$n(T)$ **随温度呈指数级急剧上升**。这完全压倒了 $\tau$ 的减小，导致半导体的电阻率随温度升高而显著下降，即具有**大且为负的电阻率温度系数**（Negative temperature coefficient of resistivity）。
- **掺杂（Doping）**：通过在硅中掺入微量特定杂质（如掺入五价磷 $\text{P}$ 形成电子导电的 **$n$ 型硅 $n\text{-Si}$**，或掺入三价硼 $\text{B}$ 形成空穴导电的 **$p$ 型硅 $p\text{-Si}$**），可以人工精确调控自由载流子浓度与电阻率（跨越 $8$ 个数量级以上），这构成了现代微电子工业的基石。

---

**2. 超导现象与 BCS 库珀对机制（Appendices 6B & 6C: Superconductors & John Bardeen）**

- **超导零电阻发现**：1911 年荷兰物理学家昂内斯（Kamerlingh Onnes）发现汞（$\text{Hg}$）在冷却至临界温度 $T_c \approx 4.2\text{ K}$ 以下时，其电阻突然完全消失（严格降为 $0$）。
- **BCS 理论与库珀对（Cooper Pairs）**：1957 年，巴丁（Bardeen）、库珀（Cooper）与施里弗（Schrieffer）提出了著名的 **BCS 超导微观理论**。在极低温下，一个运动电子穿过晶格时会吸引周围的正离子使晶格发生微小畸变，形成一个短暂的正电荷富集区（声子媒介），进而吸引第二个电子跟随其后，使两个电子配对形成**库珀对**（Cooper pair）。这种电子间的协同配对运动阻止了单个电子与晶格离子的非弹性碰撞散射，从而彻底消除了电阻，使电流在超导体中流动而无任何焦耳热损耗。
- **约翰·巴丁（John Bardeen, 1908–1991）**：科学史上唯一一位在同一领域（物理学）两度荣获诺贝尔奖的科学家——1947 年在贝尔实验室与 Brattain、Shockley 发明**晶体管**（Transistor，获 1956 年诺贝尔物理学奖），随后又创立 **BCS 超导理论**（获 1972 年诺贝尔物理学奖）。

</details>

---

## 5 Chapter 6 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 6.1 & 6.2: Coaxial Cylindrical Resistor & Copper Wire Numerical Estimates（同轴圆柱漏电电阻与铜导线微观参数计算）</summary>

**Problem Statement:**
- **Ex 6.1**: A copper cylinder has radius $a$ and length $l$. It is surrounded by a coaxial copper tube of equal length. The inner radius of the copper tube is $b$ ($l \gg b$, so edge effects are neglected). The space between the cylinder and the tube is filled with a uniform material of conductivity $\sigma$; the copper conducts far better than this material, so treat both copper pieces as perfect conductors. Find the resistance $R$ between the cylinder and the tube.
- **Ex 6.2**: A copper cylinder has a cross-sectional area of $1000\text{ mm}^2$ and length $2.0\text{ m}$. The potential difference between the two ends of the cylinder is $100\text{ mV}$. The conductivity of copper is $\sigma = 5.7 \times 10^7\text{ S/m}$ and the number density of charge carriers is $n = 8.49 \times 10^{28}\text{ m}^{-3}$ (equivalently, $ne = 1.36 \times 10^{10}\text{ C/m}^3$). Compute: (a) The resistivity $\rho_e$; (b) The current $I$; (c) The current density $j$; (d) The electric field $E$ inside the copper cylinder; (e) The drift velocity $v_d$ of the electrons.

---

**中文解析：**

**1. 同轴圆柱导体间的径向电阻推导（Exercise 6.1）**：
设从内铜柱流向外铜管的稳恒总电流为 $I$。由柱对称性，在半径为 $r \ (a < r < b)$、长为 $l$ 的同轴圆柱面上，电流密度 $\vec{j}$ 沿径向均匀向外分布：

$$
j(r) = \frac{I}{2\pi r l} \implies E(r) = \frac{j(r)}{\sigma} = \frac{I}{2\pi \sigma l r}
$$

沿径向从 $a$ 到 $b$ 积分求内外铜导体之间的电势差 $V$：

$$
V = \int_a^b E(r)\,dr = \frac{I}{2\pi \sigma l} \int_a^b \frac{dr}{r} = \frac{I}{2\pi \sigma l} \ln\left(\frac{b}{a}\right)
$$

因此，内外导体间的电阻为：

$$
R = \frac{V}{I} = \frac{\ln(b/a)}{2\pi \sigma l}
$$

*（趣味对比：结合同轴圆柱形电容器公式 $C = \frac{2\pi\epsilon L}{\ln(b/a)}$，可以看到在相同几何构型下恒有乘积关系 $RC = \frac{\epsilon}{\sigma} = \rho_e \epsilon$！）*

---

**2. 铜导线的宏观与微观电学量数值计算（Exercise 6.2）**：
统一化为国际单位：$S = 1000\text{ mm}^2 = 1.0 \times 10^{-3}\text{ m}^2$，$L = 2.0\text{ m}$，$V = 100\text{ mV} = 0.10\text{ V}$。

- **(a) 电阻率 $\rho_e$**：
  $$
  \rho_e = \frac{1}{\sigma} = \frac{1}{5.7 \times 10^7\text{ S/m}} \approx 1.75 \times 10^{-8}\ \Omega\cdot\text{m}
  $$
- **(b) 总电流 $I$**：
  先算电阻 $R = \frac{L}{\sigma S} = \frac{2.0}{5.7 \times 10^7 \times 1.0 \times 10^{-3}} \approx 3.51 \times 10^{-5}\ \Omega$，故电流为：
  $$
  I = \frac{V}{R} = \frac{\sigma S V}{L} = \frac{5.7 \times 10^7 \times 10^{-3} \times 0.10}{2.0} = 2.85 \times 10^3\text{ A}
  $$
- **(c) 电流密度 $j$**：
  $$
  j = \frac{I}{S} = \frac{2.85 \times 10^3\text{ A}}{1.0 \times 10^{-3}\text{ m}^2} = 2.85 \times 10^6\text{ A/m}^2
  $$
- **(d) 铜柱内部电场强度 $E$**：
  $$
  E = \frac{V}{L} = \frac{0.10\text{ V}}{2.0\text{ m}} = 0.050\text{ V/m} \qquad (\text{或由 } E = j/\sigma \text{ 验证一致})
  $$
- **(e) 电子的漂移速率 $v_d$**：
  $$
  v_d = \frac{j}{ne} = \frac{2.85 \times 10^6\text{ A/m}^2}{1.36 \times 10^{10}\text{ C/m}^3} \approx 2.10 \times 10^{-4}\text{ m/s} = 0.21\text{ mm/s}
  $$

</details>

<details markdown="1">
<summary>Exercise 6.3, 6.4 & 6.5: Three Coaxial Tubes, Two-Wire Line & Wire-to-Plane Capacitance（三同轴圆管、双平行传输线与导线-接地平面电容）</summary>

**Problem Statement:**
- **Ex 6.3**: Consider three thin coaxial metallic tubes of the same length $l$, and radii $a, b, c \ (a < b < c)$ in vacuum. The inner and outer tubes are connected via a conducting wire. Ignore edge effects ($l \gg c$). Calculate the capacitance $C$ between the middle tube and the other two.
- **Ex 6.4**: Two parallel long wires are separated by a distance $d$ measured between their axes, and each wire has a radius $a \ (d \gg a)$ in vacuum. Calculate the capacitance per unit length.
- **Ex 6.5**: Consider a long wire of radius $a$ parallel to an infinite grounded metallic plate ($V = 0$). The distance from the axis of the wire to the plate is $h \ (h \gg a)$ in vacuum. Calculate the capacitance per unit length.

---

**中文解析：**

**1. 三同轴金属管（内外管相连）的并联总电容（Exercise 6.3）**：
由于内管（半径 $a$）与外管（半径 $c$）用导线相连，二者处于同一电势（记为 $V = 0$）。设中间管（半径 $b$）电势为 $V > 0$，所带总电荷为 $Q$，其中分布在中间管内壁的电荷为 $q_1$，分布在外壁的电荷为 $q_2$（满足 $Q = q_1 + q_2$）。
- 在内腔区域 $a < r < b$：高斯定理给出 $E_1(r) = \frac{q_1}{2\pi\epsilon_0 l r}$，积分得电势差 $V = \frac{q_1}{2\pi\epsilon_0 l}\ln\left(\frac{b}{a}\right) \implies q_1 = \frac{2\pi\epsilon_0 l}{\ln(b/a)}V$；
- 在外腔区域 $b < r < c$：高斯定理给出 $E_2(r) = \frac{q_2}{2\pi\epsilon_0 l r}$，积分得电势差 $V = \frac{q_2}{2\pi\epsilon_0 l}\ln\left(\frac{c}{b}\right) \implies q_2 = \frac{2\pi\epsilon_0 l}{\ln(c/b)}V$。

因此，该系统等效于内外两个圆柱形电容器的**并联**，总电容为：

$$
C = \frac{Q}{V} = \frac{q_1 + q_2}{V} = 2\pi\epsilon_0 l \left[ \frac{1}{\ln(b/a)} + \frac{1}{\ln(c/b)} \right]
$$

---

**2. 双平行长直导线传输线的单位长度电容（Exercise 6.4）**：
设两根平行导线分别携带线电荷密度 $+\lambda$ 和 $-\lambda$。由于 $d \gg a$，忽略导线表面电荷分布的非均匀性（视作位于各自轴线 $x = 0$ 与 $x = d$ 处的无限长均匀带电直线）。
在两导线轴线连线上距左导线轴心为 $x \ (a \le x \le d - a)$ 处，两导线产生的电场方向相同，叠加为：

$$
E(x) = \frac{\lambda}{2\pi\epsilon_0 x} + \frac{\lambda}{2\pi\epsilon_0(d - x)}
$$

从正导线外表面 $x = a$ 积分至负导线外表面 $x = d - a$，得两导线间的电势差：

$$
V = \int_a^{d - a} \frac{\lambda}{2\pi\epsilon_0}\left(\frac{1}{x} + \frac{1}{d - x}\right)dx = \frac{\lambda}{2\pi\epsilon_0}\left[\ln x - \ln(d - x)\right]_a^{d - a} = \frac{\lambda}{\pi\epsilon_0}\ln\left(\frac{d - a}{a}\right) \approx \frac{\lambda}{\pi\epsilon_0}\ln\left(\frac{d}{a}\right)
$$

因此，单位长度的电容为：

$$
\frac{C}{L} = \frac{\lambda}{V} = \frac{\pi\epsilon_0}{\ln\left(\dfrac{d - a}{a}\right)} \approx \frac{\pi\epsilon_0}{\ln(d/a)} \qquad (d \gg a)
$$

---

**3. 长直导线与无限大接地金属平板间的单位长度电容（Exercise 6.5）**：
利用第五章的镜像法（Method of images）：将位于 $z = +h$ 处带 $+\lambda$ 的导线与位于 $z = 0$ 的接地平板，等效替换为位于 $z = +h$ 的 $+\lambda$ 与位于 $z = -h$ 的镜像线电荷 $-\lambda$（两者轴心间距为 $d = 2h$）。
接地平面 $z = 0$ 恰为该双线系统的零电势对称面，因此导线表面（$z = h - a$）与接地平面（$z = 0$）之间的电势差 $V$ 恰好是间距为 $d = 2h$ 的双平行导线电势差的一半：

$$
V = \int_0^{h - a} \frac{\lambda}{2\pi\epsilon_0}\left(\frac{1}{h - z} + \frac{1}{h + z}\right)dz = \frac{\lambda}{2\pi\epsilon_0}\ln\left(\frac{2h - a}{a}\right) \approx \frac{\lambda}{2\pi\epsilon_0}\ln\left(\frac{2h}{a}\right)
$$

由此立即得到导线与接地平板之间单位长度的电容为：

$$
\frac{C}{L} = \frac{\lambda}{V} = \frac{2\pi\epsilon_0}{\ln\left(\dfrac{2h - a}{a}\right)} \approx \frac{2\pi\epsilon_0}{\ln(2h/a)} \qquad (h \gg a)
$$

</details>

<details markdown="1">
<summary>Exercise 6.6, 6.7 & 6.8: Two-Carrier Conductivity, Interface Charge & Hemisphere Grounding Electrode（双载流子导电、异质界面自由电荷与半球接地极跨步电压）</summary>

**Problem Statement:**
- **Ex 6.6**: A uniform material contains two kinds of mobile charge carrier: positive ($+e, n_+, m_+, \tau_+$) and negative ($-e, n_-, m_-, \tau_-$). A uniform field $\vec{E} = E_0\hat{x}$ is applied. (a) Find the drift velocities $\vec{v}_+$ and $\vec{v}_-$. (b) Find the current density $\vec{j}$ and conductivity $\sigma$. Under what condition do the two kinds contribute equally?
- **Ex 6.7**: Two long rods with the same area $S$ and conductivities $\sigma_1, \sigma_2$ are joined end to end along the $x$ axis. A steady current $I > 0$ flows in the $+x$ direction from rod 1 into rod 2 (permittivity of both is $\epsilon_0$). (a) Find $\vec{E}$ in each rod. Why can the fields differ when the current is the same? (b) Find the free charge $Q$ on the interface between the two rods. For which ordering of $\sigma_1$ and $\sigma_2$ is $Q$ positive?
- **Ex 6.8**: A metal hemisphere of radius $a$ is buried in level ground (conductivity $\sigma$) with its flat face in the ground's surface. A steady current $I$ flows radially outward from the hemisphere into the ground. (a) Find $\vec{j}$ and $\vec{E}$ at $r > a$, and the resistance $R$ between the hemisphere and a distant electrode. (b) A person stands with one foot at $r$ and the other at $r + s$. Find the potential difference $V(r) - V(r + s)$, and explain why it is safer to keep the feet close together.

---

**中文解析：**

**1. 双载流子体系（如半导体中的空穴与电子）的漂移与电导率（Exercise 6.6）**：

- **(a)** 直接套用平均自由时间漂移公式 $\vec{v}_d = \frac{q\vec{E}}{m}\tau$：
  $$
  \vec{v}_+ = +\frac{e\tau_+}{m_+}E_0\hat{x}, \qquad \vec{v}_- = -\frac{e\tau_-}{m_-}E_0\hat{x}
  $$
- **(b)** 正载流子沿 $+\hat{x}$ 漂移，负载流子沿 $-\hat{x}$ 漂移，两者产生的电流密度方向**相同**（均沿 $+\hat{x}$），叠加得：
  $$
  \vec{j} = n_+ e\vec{v}_+ + n_-(-e)\vec{v}_- = e^2\left(\frac{n_+\tau_+}{m_+} + \frac{n_-\tau_-}{m_-}\right)E_0\hat{x} \implies \sigma = e^2\left(\frac{n_+\tau_+}{m_+} + \frac{n_-\tau_-}{m_-}\right)
  $$
  当 $\dfrac{n_+\tau_+}{m_+} = \dfrac{n_-\tau_-}{m_-}$ 时，两种载流子对电流密度的贡献相等。

---

**2. 异质材料串联界面上的稳恒自由电荷积累（Exercise 6.7，高频必考概念题）**：

- **(a)** 在稳恒电流下，由连续性方程知两棒内的电流密度相等：$j_1 = j_2 = \frac{I}{S}$。但因两棒电导率 $\sigma_1 \neq \sigma_2$，由 $\vec{E} = \vec{j}/\sigma$ 可知两棒内的电场强度不同：
  $$
  \vec{E}_1 = \frac{I}{\sigma_1 S}\hat{x}, \qquad \vec{E}_2 = \frac{I}{\sigma_2 S}\hat{x}
  $$
  物理原因：为了在导电能力较弱（电导率较小）的材料中维持同样大小的稳恒电流密度，必须有更强的电场来驱动载流子。
- **(b)** 跨接两棒交界面作底面积为 $S$ 的扁圆柱高斯面（左底面在棒 1 内，右底面在棒 2 内）。由高斯定理 $\epsilon_0\oint \vec{E}\cdot d\vec{S} = Q$：
  $$
  \epsilon_0(E_2 S - E_1 S) = Q \implies Q = \epsilon_0 I\left(\frac{1}{\sigma_2} - \frac{1}{\sigma_1}\right)
  $$
  当 **$\sigma_1 > \sigma_2$**（即电流从良导体流入较差导体）时，界面上积累的自由电荷 $Q > 0$（正是这一层界面静电荷产生的附加电场，使得左侧电场减弱为 $E_1$、右侧电场增强为 $E_2$，从而自动维持稳恒条件 $j_1 = j_2$！）。

---

**3. 半球形接地电极的接地电阻与跨步电压（Exercise 6.8）**：

- **(a)** 大地仅占下半空间，半径为 $r \ (r > a)$ 的半球面面积为 $2\pi r^2$。电流沿径向均匀流入大地：
  $$
  \vec{j}(r) = \frac{I}{2\pi r^2}\hat{r} \implies \vec{E}(r) = \frac{\vec{j}(r)}{\sigma} = \frac{I}{2\pi\sigma r^2}\hat{r}
  $$
  对电场从 $r = a$ 积分至 $\infty$ 得半球电极相对于无穷远处的电势 $V(a) = \int_a^\infty \frac{I}{2\pi\sigma r^2}\,dr = \frac{I}{2\pi\sigma a}$，故接地电阻为：
  $$
  R = \frac{V(a)}{I} = \frac{1}{2\pi\sigma a}
  $$
- **(b) 跨步电压（Step Voltage）**：
  两脚分别位于 $r$ 与 $r + s$ 处，两脚之间的电势差为：
  $$
  V(r) - V(r + s) = \int_r^{r + s} \frac{I}{2\pi\sigma r'^2}\,dr' = \frac{I}{2\pi\sigma}\left(\frac{1}{r} - \frac{1}{r + s}\right) = \frac{Is}{2\pi\sigma r(r + s)}
  $$
  当人靠近接地电极或高压电线落地点时，两脚间距 $s$ 越大，加在人体两脚之间的跨步电压就越大，驱动流过人体的触电电流也越危险；若将双脚并拢紧贴（$s \to 0$），则两脚处于同一等势面上，电势差趋近于零，从而保证安全。

</details>

<details markdown="1">
<summary>Exercise 6.9 & 6.10: Charge Relaxation Time & Dielectric-Filled Capacitors（欧姆导体电荷弛豫时间与电介质串并联电容器）</summary>

**Problem Statement:**
- **Ex 6.9**: A material of uniform conductivity $\sigma$ obeys $\vec{j} = \sigma\vec{E}$; take its permittivity to be $\epsilon_0$.
  (a) Using the continuity equation and Gauss' law in differential form, show that a free charge density $\rho(\vec{r}, 0)$ present at $t = 0$ becomes $\rho(\vec{r}, t) = \rho(\vec{r}, 0)e^{-t/\tau_q}$ at every point, and find the time constant $\tau_q$.
  (b) A ball of this material, of radius $b$, is isolated in vacuum and carries no charge. At $t = 0$ a charge $Q$ is placed on a small metal bead of radius $a$ at its center. Find the current $I(r, t)$ flowing outward through a concentric sphere of radius $r \ (a < r < b)$, and the charge $Q_S(t)$ on the surface of the ball.
- **Ex 6.10**: A parallel-plate capacitor has plates of area $S$ a distance $d$ apart, carrying charges $+q$ and $-q$.
  (a) A slab of dielectric of dielectric constant $\epsilon_r$ and thickness $w < d$, with area $S$, is placed between the plates and parallel to them. Find $\vec{D}$ and $\vec{E}$ in the empty part of the gap and in the slab, and the capacitance $C$. Does $C$ depend on where the slab is placed?
  (b) The slab is removed, and a block of the same dielectric, of thickness $d$ and area $S/2$, is placed so that it touches both plates and fills half of the space between them. Find the capacitance.

---

**中文解析：**

**1. 导电介质内的电荷指数弛豫（Charge Relaxation）与球体向外放电过程（Exercise 6.9，核心压轴题）**：

- **(a) 推导电荷弛豫方程与时间常数 $\tau_q$**：
  将欧姆定律 $\vec{j} = \sigma\vec{E}$ 代入连续性方程 $\frac{\partial\rho}{\partial t} + \nabla\cdot\vec{j} = 0$，并利用高斯定理微分形式 $\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0}$：
  $$
  \frac{\partial\rho}{\partial t} + \sigma(\nabla\cdot\vec{E}) = \frac{\partial\rho}{\partial t} + \frac{\sigma}{\epsilon_0}\rho = 0
  $$
  这是一个关于时间 $t$ 的一阶常系数齐次线性微分方程，对空间每一点 $\vec{r}$ 积分即得指数衰减解：
  $$
  \rho(\vec{r}, t) = \rho(\vec{r}, 0) e^{-t/\tau_q}, \qquad \text{其中弛豫时间常数 } \tau_q = \frac{\epsilon_0}{\sigma} = \rho_e \epsilon_0
  $$
- **(b) 球体内部的瞬态径向电流 $I(r, t)$ 与外表面电荷 $Q_S(t)$**：
  在 $a < r < b$ 的球壳介质区域内，由于初始时刻 $t = 0$ 时没有体电荷（$\rho(\vec{r}, 0) = 0$），根据 (a) 的结论 $\rho(\vec{r}, t) = \rho(\vec{r}, 0)e^{-t/\tau_q}$，在 $t > 0$ 的任何时刻，**$a < r < b$ 的介质内部体电荷密度始终保持为零（$\rho(\vec{r}, t) \equiv 0$）**！
  这意味着电荷从中心金属小珠流出后，直接穿过介质层到达最外表面 $r = b$，而不会在中间介质层内堆积。
  设时刻 $t$ 中心金属珠上剩余的电荷量为 $q(t)$（满足 $q(0) = Q$）。在半径为 $r \ (a < r < b)$ 的同心球面上，所包围的内部总电荷就是 $q(t)$。由高斯定理与欧姆定律：
  $$
  E(r, t) = \frac{q(t)}{4\pi\epsilon_0 r^2} \implies j(r, t) = \sigma E(r, t) = \frac{\sigma q(t)}{4\pi\epsilon_0 r^2}
  $$
  因此，穿过半径为 $r$ 的同心球面向外流出的总电流为：
  $$
  I(r, t) = 4\pi r^2 j(r, t) = \frac{\sigma}{\epsilon_0} q(t) = \frac{q(t)}{\tau_q}
  $$
  由电荷守恒 $I(r, t) = -\frac{dq(t)}{dt}$，得 $\frac{dq}{dt} = -\frac{q}{\tau_q} \implies q(t) = Q e^{-t/\tau_q}$。代入即得：
  $$
  I(r, t) = \frac{Q}{\tau_q} e^{-t/\tau_q} = \frac{\sigma Q}{\epsilon_0} e^{-\sigma t / \epsilon_0} \quad (\text{与半径 } r \text{ 无关！}), \qquad Q_S(t) = Q - q(t) = Q\left(1 - e^{-t/\tau_q}\right)
  $$

---

**2. 平行板电容器的分层（串联）与分块（并联）电介质填充（Exercise 6.10）**：

- **(a) 平行于极板插入厚度为 $w < d$ 的电介质板（等效串联）**：
  极板自由面电荷密度为 $\sigma_s = \frac{q}{S}$。由介质高斯定理 $\oint \vec{D}\cdot d\vec{S} = q_{\text{free}}$，在真空层和电介质板内部，电位移矢量大小处处相同且垂直于极板：
  $$
  D_{\text{vac}} = D_{\text{slab}} = \frac{q}{S}
  $$
  从而两部分区域内的电场强度大小分别为：
  $$
  E_{\text{vac}} = \frac{D}{\epsilon_0} = \frac{q}{\epsilon_0 S}, \qquad E_{\text{slab}} = \frac{D}{\epsilon_r\epsilon_0} = \frac{q}{\epsilon_r\epsilon_0 S}
  $$
  沿垂直极板路径积分，总电势差等于真空段电压（总厚度 $d - w$）与介质段电压（厚度 $w$）之和：
  $$
  V = E_{\text{vac}}(d - w) + E_{\text{slab}}w = \frac{q}{\epsilon_0 S}\left(d - w + \frac{w}{\epsilon_r}\right) \implies C = \frac{q}{V} = \frac{\epsilon_0 S}{d - w + \dfrac{w}{\epsilon_r}}
  $$
  显然，总电容 $C$ 仅取决于真空总厚度 $d - w$ 与介质厚度 $w$，**与电介质板在极板间放置的具体上下位置完全无关**。
- **(b) 厚度为 $d$、面积为 $S/2$ 的电介质块填充左半边（等效并联）**：
  上下金属极板各自为等势体，故真空右半区与介质左半区承受相同的电势差 $V$，内部电场均为 $E = \frac{V}{d}$。
  但在介质区 $D_1 = \epsilon_r\epsilon_0 E = \epsilon_r\epsilon_0\frac{V}{d}$（对应极板自由面密度 $\sigma_1 = D_1$），在真空区 $D_2 = \epsilon_0 E = \epsilon_0\frac{V}{d}$（对应极板自由面密度 $\sigma_2 = D_2$）。因此极板总自由电荷量为：
  $$
  q = \sigma_1\frac{S}{2} + \sigma_2\frac{S}{2} = \frac{\epsilon_0 S}{2d}(\epsilon_r + 1)V \implies C = \frac{q}{V} = \frac{\epsilon_0 S}{2d}(\epsilon_r + 1)
  $$

</details>