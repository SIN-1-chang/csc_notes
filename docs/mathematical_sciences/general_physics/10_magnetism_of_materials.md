# Chapter 10: Magnetic Properties of Materials（物质的磁性）

!!! abstract
    General Physics II (Electromagnetism) | 第十章课堂与讲义笔记
    
    参考：
    
    - Lecture 10: *Magnetic Properties of Materials* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 10: *Magnetic Properties of Materials*
    - Halliday, Resnick & Krane, *Physics*, Chapter 35

## 1 磁偶极子及其磁场 (The Magnetic Dipole and Its Field)

### 1.1 磁偶极矩、力矩与取向势能

由于自然界中不存在磁单极子（$\nabla\cdot\vec{B} = 0$），**磁偶极子**（Magnetic Dipole）是磁学中最基本的结构单元。磁偶极子可以来源于以下四类物理系统：

1. **载流线圈或闭合回路**（Current-carrying coil or loop）；
2. **永磁体**（Permanent magnet，如条形磁铁 Bar magnet）；
3. **旋转的带电球体**（Rotating sphere of charge，如地球磁场）；
4. **亚原子基本粒子**（Subatomic particles，如电子、质子等具有内禀自旋磁矩的粒子）。

对于一个有 $N$ 匝、每匝通有电流 $i$、面积矢量为 $\vec{A} = A\hat{n}$（方向由右手螺旋定则确定）的平面载流线圈，其**磁偶极矩**（Magnetic Dipole Moment）定义为：

$$
\vec{\mu} = Ni\vec{A} \qquad (\text{SI 单位：}\text{A}\cdot\text{m}^2 \text{ 或 } \text{J/T})
$$

当磁偶极子置于外磁场 $\vec{B}$ 中（设 $\vec{\mu}$ 与 $\vec{B}$ 夹角为 $\theta$），且假定线圈电流 $i$ 恒定（即 $|\vec{\mu}|$ 保持不变）时：

- **磁力矩（Magnetic Torque）**：外磁场对偶极子施加恢复力矩 $\vec{\tau} = \vec{\mu} \times \vec{B}$，标量形式（以增大 $\theta$ 为正方向）为 $\tau = -\mu B\sin\theta = -\frac{\partial}{\partial\theta}(-\mu B\cos\theta)$，总是试图将 $\vec{\mu}$ 转向与 $\vec{B}$ 同向；
- **磁偶极子的取向势能（Magnetic Potential Energy）**：类比于力与势能的关系 $F_x = -\frac{\partial U}{\partial x}$，由外力克服磁力矩做功 $U_B = -\int_{\pi/2}^\theta \tau\,d\theta'$（选定 $\theta = 90^\circ$ 即 $\vec{\mu} \perp \vec{B}$ 时为势能零点），定义磁偶极子在外磁场中的取向势能为：
  $$
  U_B = -\vec{\mu} \cdot \vec{B} = -\mu B \cos\theta
  $$
  - **最低能量态（稳定平衡）**：当 $\vec{\mu}$ 与 $\vec{B}$ **同向平行**（$\theta = 0^\circ$）时，$U_B = -\mu B$ 最小；
  - **最高能量态（不稳定平衡）**：当 $\vec{\mu}$ 与 $\vec{B}$ **反向平行**（$\theta = 180^\circ$）时，$U_B = +\mu B$ 最大。

### 1.2 载流圆弧与磁偶极子的磁场

**1. 载流圆弧在曲率中心处的磁场（Magnetic Field of a Circular Arc，Lecture 10 Slides 9–10）**

设半径为 $R$、圆心角为 $\phi$（弧度制）的圆弧形导线通有电流 $i$。在圆弧曲率中心 $C$ 处，弧长微元 $ds = R\,d\phi$ 与径向单位矢量 $\hat{r}$ 处处垂直（$|d\vec{s}\times\hat{r}| = ds$），且各微元产生的磁场方向相同（由右手螺旋定则判定垂直于纸面）。由毕奥-萨伐尔定律积分得：

$$
B = \int dB = \int_0^\phi \frac{\mu_0}{4\pi}\frac{i(R\,d\phi')}{R^2} = \frac{\mu_0 i \phi}{4\pi R}
$$

特别地，对于一整圈闭合圆环（$\phi = 2\pi$），环心处的磁感应强度为（代入 $\mu = i\pi R^2$）：

$$
B_{\text{center}} = \frac{\mu_0 i}{2R} = \frac{\mu_0}{2\pi}\frac{\mu}{R^3}
$$

**2. 载流圆环（磁偶极子）轴线上的磁场与远场公式**

对于半径为 $R$、通有电流 $i$ 的单匝圆环，在中心轴线上距环心为 $z$ 的点 $P$ 处，由第九章毕奥-萨伐尔定律积分（径向分量抵消，轴向分量 $\cos\alpha = \frac{R}{\sqrt{R^2 + z^2}}$ 叠加）并代入磁矩 $\vec{\mu} = i\pi R^2\hat{z}$，可得精确轴线磁场及远场（$|z| \gg R$）近似公式：

$$
\vec{B}(z) = \frac{\mu_0 i R^2}{2(R^2 + z^2)^{3/2}}\hat{z} = \frac{\mu_0}{2\pi}\frac{\vec{\mu}}{(R^2 + z^2)^{3/2}} \xrightarrow{|z| \gg R} \vec{B}_{\text{far}}(z) = \frac{\mu_0}{2\pi}\frac{\vec{\mu}}{|z|^3}
$$

（注：分母取绝对值 $|z|^3$ 是因为无论在环平面上方 $z > 0$ 还是下方 $z < 0$，轴线上的磁场方向始终与磁偶极矩 $\vec{\mu}$ 的方向相同，是关于 $z$ 的偶函数）。

### 1.3 磁偶极子与电偶极子的对称类比总表

| 物理属性 | 磁偶极子（Magnetic Dipole） | 电偶极子（Electric Dipole） |
| :--- | :--- | :--- |
| **偶极矩定义** | $\vec{\mu} = Ni\vec{A}$ | $\vec{p} = q\vec{d}$ |
| **外场中的力矩** | $\vec{\tau}_B = \vec{\mu} \times \vec{B}$ | $\vec{\tau}_E = \vec{p} \times \vec{E}$ |
| **外场中的取向势能** | $U_B = -\vec{\mu} \cdot \vec{B}$ | $U_E = -\vec{p} \cdot \vec{E}$ |
| **轴线远场公式**（$z \gg R, d$） | $\vec{B}(z) = \dfrac{\mu_0}{2\pi}\dfrac{\vec{\mu}}{\|z\|^3}$ | $\vec{E}(z) = \dfrac{1}{2\pi\epsilon_0}\dfrac{\vec{p}}{\|z\|^3}$ |
| **空间任意点远场通式**（$r \gg R, d$） | $\vec{B}(\vec{r}) = \dfrac{\mu_0}{4\pi r^3}\left[3(\vec{\mu}\cdot\hat{r})\hat{r} - \vec{\mu}\right]$ | $\vec{E}(\vec{r}) = \dfrac{1}{4\pi\epsilon_0 r^3}\left[3(\vec{p}\cdot\hat{r})\hat{r} - \vec{p}\right]$ |
| **核心拓扑差异（近场内部）** | 磁感线无头无尾，**永远形成闭合回路**（无磁单极子，$\nabla\cdot\vec{B}=0$） | 电场线起自 $+q$、终止于 $-q$，在偶极子内部方向与外部相反 |

---

## 2 磁性材料的分类与物理机制 (Classification of Magnetic Materials)

宏观磁性材料包含海量的原子或分子级微观磁偶极矩（源于电子轨道运动与电子内禀自旋）。根据原子是否具有永久磁偶极矩以及相邻原子磁矩之间的相互作用性质，材料的磁性主要分为**顺磁性**（Paramagnetism）、**抗磁性**（Diamagnetism）与**铁磁性**（Ferromagnetism）三大类。

<details markdown="1">
<summary>前沿拓展：自旋玻璃与阻挫（Spin Glasses and Frustration — 2021 诺贝尔物理学奖）</summary>

**自旋玻璃（Spin Glass）**是一类无序磁性合金系统，例如将少量磁性原子（如铁 $\text{Fe}$ 或锰 $\text{Mn}$）随机掺杂混合到非磁性金属基质（如铜 $\text{Cu}$）晶格中。
每个磁性原子表现为一个微小磁偶极子（自旋 Spin），通过基质传导电子传递的偶极子间相互作用随间距增大而正负交替变化。由于磁性原子位置随机，导致某些自旋同时受到相互冲突的排列要求（例如正三角形三个顶点上的反铁磁自旋：若第一个朝上 $\uparrow$、第二个朝下 $\downarrow$，则第三个自旋无论朝上还是朝下都无法同时满足与前两者反向的要求）。这种无法同时满足所有相互作用能量最小化的现象称为**阻挫**（Frustration）。
意大利物理学家乔治·帕里西（Giorgio Parisi）因对自旋玻璃及无序复杂系统理论的开创性贡献荣获 **2021 年诺贝尔物理学奖**，其数学方法深刻影响了数学、生物学、神经科学以及机器学习（优化算法）等众多领域。

</details>

### 2.1 顺磁性 (Paramagnetism) 与居里定律

**顺磁性**（Paramagnetism）出现在原子本身具有**永久磁偶极矩**（Permanent atomic magnetic dipole moments）$\vec{\mu}$、但相邻原子磁矩之间几乎无相互作用的材料中（如 $\text{Al}, \text{Na}, \text{O}_2$ 等）。

- **无外场时**：由于热运动（Thermal agitation）的随机搅乱，各原子磁矩取向完全无序，宏观净磁矩为零。
- **加外磁场 $\vec{B}_{\text{ext}}$ 时**：原子磁矩倾向于顺着外磁场方向排列（受强烈磁场吸引）。定义单位体积内的净磁偶极矩矢量为材料的**磁化强度**（Magnetization，记作 $\vec{M}$，SI 单位为 $\text{A/m}$）：
  $$
  \vec{M} = \frac{\sum \vec{\mu}_i}{\text{Volume } V}
  $$

**1. 居里定律（Curie's Law, 1895）与饱和磁化强度**

实验与统计力学表明，在弱场或较高温度下（即 $\mu B_{\text{ext}} \ll k_B T$ 时），顺磁体的磁化强度 $M$ 与外磁场 $B_{\text{ext}}$ 成正比，与绝对温度 $T$ 成反比：

$$
M = C \frac{B_{\text{ext}}}{T} \qquad (\text{居里定律 Curie's Law，其中 } C \text{ 为居里常数 Curie constant})
$$

而当外磁场极强或温度极低（$\mu B_{\text{ext}} \gg k_B T$）时，所有原子的磁矩全部顺着外场方向完全对齐，磁化强度达到最大值——**饱和磁化强度**（Saturation magnetization）：

$$
M_{\max} = \frac{N\mu}{V} = n\mu \qquad (n = N/V \text{ 为单位体积内的原子数})
$$

**2. 二能级玻尔兹曼统计模型（Two-State Boltzmann Model，Section 10.3 & Exercise 10.3）**

设顺磁固体单位体积有 $n$ 个互不作用的原子，每个原子磁矩大小为 $\mu$，且在外场 $\vec{B} = B\hat{z}$ 中只能取平行（$\theta = 0$，能量 $U_+ = -\mu B$）或反平行（$\theta = \pi$，能量 $U_- = +\mu B$）两个量子态。由统计力学玻尔兹曼分布，处于两态的原子数占比分别正比于 $e^{-U_+/k_B T} = e^{+\mu B/k_B T}$ 与 $e^{-U_-/k_B T} = e^{-\mu B/k_B T}$。因此净磁化强度为：

$$
M = n\mu \left( \frac{e^{\mu B/k_B T} - e^{-\mu B/k_B T}}{e^{\mu B/k_B T} + e^{-\mu B/k_B T}} \right) = M_{\max} \tanh\left(\frac{\mu B}{k_B T}\right)
$$

当 $\frac{\mu B}{k_B T} \ll 1$ 时，利用泰勒展开 $\tanh x \approx x$，上式立即退化为居里定律 $M \approx \left(\frac{n\mu^2}{k_B}\right)\frac{B}{T}$，从而给出居里常数的微观表达式 **$C = \dfrac{n\mu^2}{k_B}$**！

### 2.2 抗磁性 (Diamagnetism) 的经典电子轨道推导

**抗磁性**（Diamagnetism）是**所有物质普遍具有的本征属性**（但在具有永久磁矩的材料中被更强的顺磁性或铁磁性所掩盖，仅在原子净永久磁矩为零的材料如 $\text{He}, \text{Cu}, \text{Ag}, \text{Au}, \text{Bi}, \text{H}_2\text{O}$ 中显现）。抗磁体会被强磁铁微弱地**排斥**（Repelled from strong magnetic fields）。

**微观经典解释（Section 10.4 & Exercise 10.4）**：
将无净磁矩的原子模拟为成对的、以相同半径 $r$ 和相同初始角速率 $\omega_0$ 分别作逆时针和顺时针圆周运动的电子（电荷 $-e$，质量 $m$）。

1. **无外磁场时**：库仑引力提供向心力 $F_C = m\omega_0^2 r$。两个反向运动的电子轨道磁矩大小均为 $\mu_0^{\text{orb}} = iA = \left(\frac{e\omega_0}{2\pi}\right)(\pi r^2) = \frac{1}{2}er^2\omega_0$，方向相反（记带符号的 $\mu = -\frac{e}{2}r^2\omega$），净磁矩抵消为零。
2. **施加垂直于轨道平面的外磁场 $\vec{B}$ 时**：电子额外受到径向洛伦兹力 $\pm e\omega r B$（向心或离心取决于绕行方向）。保持轨道半径 $r$ 不变，径向牛顿第二定律写为（将绕行方向正负号归入角速度 $\omega$ 的符号中）：
   $$
   m\omega^2 r = m\omega_0^2 r + e\omega r B \implies \omega^2 - \omega_0^2 = (\omega - \omega_0)(\omega + \omega_0) = \frac{eB}{m}\omega
   $$
3. **一阶近似求解拉莫尔频移 $\Delta\omega$ 与感生磁矩 $\Delta\mu$**：
   由于原子内部库仑力远大于外磁场洛伦兹力（$|\Delta\omega| \ll |\omega_0|$），取 $\omega + \omega_0 \approx 2\omega_0 \approx 2\omega$，保留至 $B$ 的一阶项，消去 $\omega_0$ 得：
   $$
   \Delta\omega = \omega - \omega_0 \approx \frac{eB}{2m} \qquad (\text{对正反两种绕行方向，角速度偏移量 }\Delta\omega\text{ 符号完全相同！})
   $$
   这意味着原本磁矩与 $\vec{B}$ 同向的电子被减速（$|\omega|$ 减小），而原本磁矩与 $\vec{B}$ 反向的电子被加速（$|\omega|$ 增大）。因此，无论电子原本沿哪个方向绕行，单个电子产生的**感生磁偶极矩变化量**（Induced magnetic moment）恒为：
   $$
   \Delta\vec{\mu} = -\frac{e}{2}r^2 \Delta\vec{\omega} = -\frac{e^2 r^2}{4m}\vec{B}
   $$
   负号表明**抗磁体感生出的磁偶极矩永远与外加磁场 $\vec{B}$ 方向相反**，因此抗磁体的磁化率恒为负值（$\chi < 0$），且与温度无关。

### 2.3 铁磁性 (Ferromagnetism)、磁滞回线与居里温度

**铁磁性**（Ferromagnetism，典型元素包括铁 $\text{Fe}$、钴 $\text{Co}$、镍 $\text{Ni}$、钆 $\text{Gd}$、镝 $\text{Dy}$ 及其合金）表现出极强的永久磁性。

1. **交换相互作用（Exchange Interaction）**：
   铁磁体与顺磁体的本质区别在于：铁磁体相邻原子的永久磁偶极矩之间存在强烈的量子力学**交换相互作用**，系统的总能量可由海森堡模型表示为：
   $$
   U = -J \sum_{\langle ij \rangle} \vec{\mu}_i \cdot \vec{\mu}_j - \sum_i \vec{\mu}_i \cdot \vec{B}
   $$
   其中 $\langle ij \rangle$ 表示对最近邻原子对求和。当交换耦合常数 **$J > 0$** 时，相邻原子磁矩平行排列可大幅降低系统能量，从而在无外磁场（$\vec{B} = \vec{0}$）时也能维持自发平行排列（Spontaneous alignment）。（若 $J < 0$，相邻磁矩倾向于反平行排列，则称为**反铁磁性 Antiferromagnetism**，如铬 $\text{Cr}$、锰 $\text{Mn}$）。
2. **磁畴（Magnetic Domains）**：
   为什么一块普通的铁块在自然状态下并不表现为强磁铁？因为宏观铁磁体内部自发分裂为许多微小的区域，称为**磁畴**（Magnetic domains，见 Figure 10.3）。每个磁畴内部的所有原子磁矩均高度平行排列（已达饱和），但不同磁畴之间的磁矩取向彼此闭合抵消，使宏观净磁矩为零。施加外磁场 $\vec{B}_{\text{ext}}$ 时，磁矩顺着外场方向的磁畴通过畴壁移动而不断扩大（Domain growth），且畴内磁矩转向外场方向，从而使整块样品获得极强的宏观磁化。
3. **磁滞回线（Hysteresis Loop）**：
   铁磁体的磁化曲线具有**不可逆性**，称为**磁滞**（Hysteresis，见 Figure 10.2）：
   - 从未磁化状态 $a$ 出发，随外场 $H$ 增大沿初始磁化曲线到达**饱和磁化强度** $M_s$（点 $b$）；
   - 当外场降回 $H = 0$ 时，磁畴无法完全恢复原状，样品保留了非零的**剩余磁化强度 / 剩磁**（Remanent magnetization，点 $c$），这就形成了永磁体（Permanent magnet）；
   - 必须施加反向磁场至**矫顽力**（Coercive field, $-H_c$），才能使宏观磁化强度降为零；继续反向加场至负向饱和点 $d$ 再正向加场经过反向剩磁点 $e$ 回到 $b$，形成闭合的**磁滞回线**（Hysteresis loop $b\text{-}c\text{-}d\text{-}e\text{-}b$）。这种磁记忆效应是硬盘等磁信息存储（Magnetic storage）的物理基础。
4. **居里温度（Curie Temperature, $T_C$）与相变**：
   交换相互作用（特征能量 $\sim J\mu^2$，倾向于有序排列）与热运动（特征能量 $\sim k_B T$，倾向于无序搅乱）相互竞争。当温度升高到临界温度——**居里温度** $T_C$（对铁约为 $1043\text{ K}$）以上时，热运动战胜交换作用，自发磁化消失（铁磁体发生相变转化为**顺磁体**，其磁化率遵循居里-外斯定律 $\chi \propto \frac{1}{T - T_C}$）。
5. **反常霍尔效应（Anomalous Hall Effect, 1880）**：
   在铁磁材料中，由于材料自身的自发磁化强度 $\vec{M}$，即使外加磁场 $B = 0$，霍尔电阻率 $R_H$ 依然非零（且随 $B$ 呈现出与磁滞回线一致的回滞环）。在特定拓扑磁性材料中，甚至可以在零外磁场下观测到霍尔电导量子化的**量子反常霍尔效应**（Quantum Anomalous Hall Effect，薛其坤团队于 2013 年首次实验发现）。

---

## 3 磁场强度 $\vec{H}$ 与束缚电流 (Magnetic Field Strength $\vec{H}$ and Bound Currents)

### 3.1 磁场强度 $\vec{H}$、磁化率 $\chi$ 与相对磁导率 $\mu_r$

当空间存在磁性材料时，空间总磁感应强度 $\vec{B}$ 由我们可控的宏观**自由电流**（Free currents, $i_{\text{free}}$）和磁化材料自身的原子磁矩共同产生。为了剥离磁化响应并简化计算，定义辅助矢量——**磁场强度**（Magnetic Field Strength，记作 $\vec{H}$）为：

$$
\vec{H} \equiv \frac{\vec{B}}{\mu_0} - \vec{M} \iff \vec{B} = \mu_0(\vec{H} + \vec{M})
$$

需要注意：**$\vec{H}$ 与磁化强度 $\vec{M}$ 具有完全相同的量纲和单位，均为安培每米（$\text{A/m}$）**，只有磁感应强度 $\vec{B}$ 的单位才是特斯拉（$\text{T}$）。

对于顺磁体（在 $\mu B \ll k_B T$ 线性区）和抗磁体，磁化强度 $\vec{M}$ 与磁场强度 $\vec{H}$ 成正比：

$$
\vec{M} = \chi \vec{H}
$$

其中无量纲比例常数 $\chi$ 称为**磁化率**（Magnetic susceptibility）。将其代入 $\vec{B} = \mu_0(\vec{H} + \vec{M})$，可得线性磁介质中的本构关系：

$$
\vec{B} = \mu_0(1 + \chi)\vec{H} = \mu_r \mu_0 \vec{H} = \mu \vec{H}
$$

其中 $\mu_r \equiv 1 + \chi$ 称为材料的**相对磁导率**（Relative permeability），$\mu \equiv \mu_r\mu_0$ 称为材料的**磁导率**（Permeability，注意勿与磁偶极矩 $\vec{\mu}$ 混淆）。

三大磁性材料的特征参数对比如下表：

| 材料类型 | 微观原子磁矩特征 | 磁化率 $\chi$ 与相对磁导率 $\mu_r = 1+\chi$ | 外磁场中的宏观受力与记忆特性 |
| :--- | :--- | :--- | :--- |
| **抗磁体（Diamagnet）** | 无永久磁矩（$\vec{\mu}_0 = \vec{0}$），外场诱导反向轨道磁矩 | $\chi < 0$（极小，约 $-10^{-5} \sim -10^{-9}$）<br>$\mu_r \lesssim 1$（与温度无关） | 被强磁场微弱排斥；无磁滞 |
| **顺磁体（Paramagnet）** | 有永久磁矩（$\vec{\mu}_0 \neq \vec{0}$），相邻磁矩无相互作用 | $\chi > 0$（较小，约 $10^{-5} \sim 10^{-3}$）<br>$\mu_r \gtrsim 1$（随温度按 $\chi \propto 1/T$ 减小） | 被强磁场微弱吸引；无磁滞 |
| **铁磁体（Ferromagnet）** | 有永久磁矩，且存在强交换耦合 $J > 0$（形成磁畴） | 非线性（$\vec{M}$ 与 $\vec{H}$ 不成正比）<br>初始等效 $\mu_r$ 可达 $10^3 \sim 10^5$ | 被磁场强烈吸引；具有**磁滞回线**与剩磁（$T > T_C$ 时转变为顺磁体） |

### 3.2 磁介质中的安培环路定理与束缚电流

引入 $\vec{H}$ 的最大优势在于，**关于 $\vec{H}$ 的安培环路定理（积分形式与微分形式）右侧仅包含自由电流（Free current）**：

$$
\oint_C \vec{H} \cdot d\vec{l} = i_{\text{free}}, \qquad \nabla \times \vec{H} = \vec{j}_{\text{free}}
$$

从等效电流的角度看，非均匀或有界磁化材料内部和表面未抵消的微观原子环形电流，在宏观上等效为**束缚体电流密度**（Bound volume current density, $\vec{j}_b$）与**束缚面电流密度**（Bound surface current density, $\vec{K}_b$）：

$$
\vec{j}_b = \nabla \times \vec{M}, \qquad \vec{K}_b = \vec{M} \times \hat{n} \qquad (\hat{n} \text{ 为材料表面的外法向单位矢量})
$$

空间总电流密度为 $\vec{j}_{\text{tot}} = \vec{j}_{\text{free}} + \vec{j}_b$。将 $\nabla\times\vec{B} = \mu_0(\vec{j}_{\text{free}} + \nabla\times\vec{M})$ 移项组合为 $\nabla\times\left(\frac{\vec{B}}{\mu_0} - \vec{M}\right) = \vec{j}_{\text{free}}$，立即验证了 $\nabla\times\vec{H} = \vec{j}_{\text{free}}$ 的自洽性。

### 3.3 静磁学中的磁介质与静电学中的电介质完整对偶表

讲义（Section 10.6 Page 94）特别总结了电介质与磁介质方程体系的对应关系（注意本构定义中的正负号差异以及束缚源中的负号差异）：

| 物理量与基本定律维度 | 静电学中的电介质（Dielectrics, §6.4） | 静磁学中的磁介质（Magnetic Materials, §10.6） |
| :--- | :--- | :--- |
| **基本总场强（Total Field）** | 电场强度 $\vec{E}$ | 磁感应强度 $\vec{B}$ |
| **介质宏观响应（Dipole Density）** | 电极化强度 $\vec{P}$（单位体积电偶极矩） | 磁化强度 $\vec{M}$（单位体积磁偶极矩） |
| **辅助场矢量定义（Auxiliary Field）** | 电位移矢量 $\vec{D} = \epsilon_0\vec{E} + \vec{P}$ | 磁场强度 $\vec{H} = \dfrac{\vec{B}}{\mu_0} - \vec{M}$ |
| **仅含自由源的积分定理** | $\displaystyle\oint_S \vec{D} \cdot d\vec{S} = q_{\text{free}}$（高斯定理） | $\displaystyle\oint_C \vec{H} \cdot d\vec{l} = i_{\text{free}}$（安培环路定理） |
| **仅含自由源的微分定理** | $\nabla \cdot \vec{D} = \rho_{\text{free}}$ | $\nabla \times \vec{H} = \vec{j}_{\text{free}}$ |
| **线性各向同性介质本构关系** | $\vec{D} = \epsilon\vec{E}, \quad \epsilon = \epsilon_r\epsilon_0 = (1 + \chi_e)\epsilon_0$ | $\vec{B} = \mu\vec{H}, \quad \mu = \mu_r\mu_0 = (1 + \chi)\mu_0$ |
| **等效束缚源（体密度与面密度）** | $\rho_b = -\nabla \cdot \vec{P}, \qquad \sigma_b = \vec{P} \cdot \hat{n}$ | $\vec{j}_b = \nabla \times \vec{M}, \qquad \vec{K}_b = \vec{M} \times \hat{n}$ |

---

## 4 Chapter 10 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 10.1: Far-Field Magnetic Field of a Current Ring at Arbitrary Angle（载流圆环在空间任意远点处的磁偶极子场严格推导）</summary>

**Problem Statement:**
Consider a circular ring of radius $R$ placed in the $xy$-plane and its center located at the origin. The ring carries a current $I$, flowing counterclockwise when viewed from the positive $z$ axis.
(a) For a point $\vec{r} = (r\sin\theta, 0, r\cos\theta)$ located in the $xz$-plane, show that for $r \gg R$ the magnetic field has the following form:
$$\vec{B} = -\frac{\mu_0 \vec{\mu}}{4\pi r^3} + \frac{3\mu_0(\vec{\mu}\cdot\vec{r})\vec{r}}{4\pi r^5}$$
where the magnetic dipole moment is $\vec{\mu} = I\pi R^2\hat{z}$.
(b) What is the potential energy of a magnetic dipole $\vec{\mu}'$ if it is placed at $\vec{r} \ (r \gg R)$?

---

**中文解析：**

**(a) 载流圆环远场磁偶极子通式的微元积分展开推导**：
设圆环上方位角为 $\phi \in [0, 2\pi)$ 的源点位置矢量为 $\vec{r}' = R(\cos\phi\,\hat{x} + \sin\phi\,\hat{y})$，逆时针电流元线矢量为：

$$
d\vec{l} = R\,d\phi\,(-\sin\phi\,\hat{x} + \cos\phi\,\hat{y})
$$

场点位于 $xz$ 平面内 $\vec{r} = r\sin\theta\,\hat{x} + r\cos\theta\,\hat{z}$（模长为 $|\vec{r}| = r$）。从源点指向场点的位移矢量为：

$$
\vec{R}_{\text{rel}} = \vec{r} - \vec{r}' = (r\sin\theta - R\cos\phi)\hat{x} - R\sin\phi\,\hat{y} + r\cos\theta\,\hat{z}
$$

当 $r \gg R$ 时，将距离分母 $|\vec{r} - \vec{r}'|^{-3}$ 对小量 $R/r$ 展开至一阶项（保留至 $\mathcal{O}(R/r)$）：

$$
|\vec{r} - \vec{r}'|^{-3} = \left(r^2 - 2\vec{r}\cdot\vec{r}' + R^2\right)^{-3/2} = r^{-3}\left(1 - \frac{2R\sin\theta\cos\phi}{r} + \frac{R^2}{r^2}\right)^{-3/2} \approx \frac{1}{r^3}\left(1 + \frac{3R\sin\theta\cos\phi}{r}\right)
$$

计算分子中的叉乘 $d\vec{l} \times (\vec{r} - \vec{r}')$：

$$
\begin{aligned}
d\vec{l} \times (\vec{r} - \vec{r}') &= R\,d\phi \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ -\sin\phi & \cos\phi & 0 \\ r\sin\theta - R\cos\phi & -R\sin\phi & r\cos\theta \end{vmatrix} \\
&= R\,d\phi \left[ (r\cos\theta\cos\phi)\hat{x} + (r\cos\theta\sin\phi)\hat{y} + (R - r\sin\theta\cos\phi)\hat{z} \right]
\end{aligned}
$$

将分子与分母展开式相乘代入毕奥-萨伐尔定律 $\vec{B}(\vec{r}) = \frac{\mu_0 I}{4\pi}\int_0^{2\pi} \frac{d\vec{l}\times(\vec{r}-\vec{r}')}{|\vec{r}-\vec{r}'|^3}$。
注意到在 $[0, 2\pi]$ 上积分时，凡是含单次 $\cos\phi$ 或 $\sin\phi$ 的项积分均为 $0$（$\int_0^{2\pi}\cos\phi\,d\phi = \int_0^{2\pi}\sin\phi\,d\phi = \int_0^{2\pi}\sin\phi\cos\phi\,d\phi = 0$），只有常数项（积分为 $2\pi$）和含 $\cos^2\phi$ 的项（$\int_0^{2\pi}\cos^2\phi\,d\phi = \pi$）非零！保留至领头阶 $\mathcal{O}(R^2/r^3)$：

- **$x$ 分量**：来自 $(r\cos\theta\cos\phi)$ 与修正项 $\left(\frac{3R\sin\theta\cos\phi}{r}\right)$ 的乘积：
  $$
  B_x = \frac{\mu_0 I R}{4\pi r^3} \int_0^{2\pi} \frac{3R\sin\theta\cos\theta\cos^2\phi}{r} r\,d\phi = \frac{\mu_0 (I\pi R^2)}{4\pi r^3} (3\sin\theta\cos\theta) = \frac{3\mu_0 \mu \sin\theta\cos\theta}{4\pi r^3}
  $$
- **$y$ 分量**：因被积函数含 $\sin\phi$ 或 $\sin\phi\cos\phi$，积分精确为零：$B_y = 0$；
- **$z$ 分量**：来自常数项 $R$（乘以 $1$）与 $(-r\sin\theta\cos\phi)$ 乘以修正项 $\left(\frac{3R\sin\theta\cos\phi}{r}\right)$ 的组合：
  $$
  B_z = \frac{\mu_0 I R}{4\pi r^3} \int_0^{2\pi} \left(R - 3R\sin^2\theta\cos^2\phi\right) d\phi = \frac{\mu_0 (I\pi R^2)}{4\pi r^3}\left(2 - 3\sin^2\theta\right) = \frac{\mu_0 \mu}{4\pi r^3}\left(3\cos^2\theta - 1\right)
  $$

另一方面，注意到 $\vec{\mu} = \mu\hat{z}$，$\vec{r} = r(\sin\theta\,\hat{x} + \cos\theta\,\hat{z})$，故 $\vec{\mu}\cdot\vec{r} = \mu r\cos\theta$。将上面求出的分量合并为矢量形式：

$$
\vec{B} = B_x\hat{x} + B_z\hat{z} = \frac{\mu_0 \mu}{4\pi r^3}\left[ 3\cos\theta(\sin\theta\,\hat{x} + \cos\theta\,\hat{z}) - \hat{z} \right] = -\frac{\mu_0\vec{\mu}}{4\pi r^3} + \frac{3\mu_0(\vec{\mu}\cdot\vec{r})\vec{r}}{4\pi r^5}
$$

由于圆环绕 $z$ 轴具有旋转对称性，该矢量表达式对三维空间任意远点 $\vec{r}$ 均普遍成立，证毕。

---

**(b) 第二个磁偶极子 $\vec{\mu}'$ 置于 $\vec{r}$ 处的相互作用势能**：
直接应用磁偶极子在外场中的势能公式 $U_B = -\vec{\mu}' \cdot \vec{B}(\vec{r})$：

$$
U_B = -\vec{\mu}' \cdot \vec{B}(\vec{r}) = \frac{\mu_0}{4\pi r^3}\left[ \vec{\mu}\cdot\vec{\mu}' - \frac{3(\vec{\mu}\cdot\vec{r})(\vec{\mu}'\cdot\vec{r})}{r^2} \right] = \frac{\mu_0}{4\pi r^3}\left[ \vec{\mu}\cdot\vec{\mu}' - 3(\vec{\mu}\cdot\hat{r})(\vec{\mu}'\cdot\hat{r}) \right]
$$

</details>

<details markdown="1">
<summary>Exercise 10.2: Long Solenoid Filled with Magnetic Material（填充磁介质的长直螺线管内场与束缚面电流）</summary>

**Problem Statement:**
A long solenoid with $n$ turns per unit length carries a free current $i$, and its interior is completely filled with a material of relative permeability $\mu_r$. Find the magnetic field strength $\vec{H}$, the magnetic field $\vec{B}$, the magnetization $\vec{M}$, and the bound surface current $\vec{K}_b$ on the surface of the material.

---

**中文解析：**

设螺线管轴线沿 $+z$ 方向（按右手螺旋定则，自由电流 $i$ 沿 $+\hat{\phi}$ 方向环绕，内部场沿 $+\hat{z}$ 方向）：

1. **求磁场强度 $\vec{H}$**：
   在无限长螺线管外部，$\vec{H} = \vec{0}$。跨接螺线管管壁作矩形安培环路（管内平行于轴线的边长为 $l$），直接应用关于 $\vec{H}$ 的安培环路定理 $\oint_C \vec{H}\cdot d\vec{l} = i_{\text{free, enc}}$：
   $$
   Hl = (nl)i \implies \vec{H} = ni\,\hat{z} \qquad (\text{大小为 } H = ni)
   $$
2. **求磁感应强度 $\vec{B}$**：
   由线性磁介质本构关系 $\vec{B} = \mu\vec{H} = \mu_r\mu_0\vec{H}$：
   $$
   \vec{B} = \mu_r \mu_0 n i\,\hat{z} \qquad (\text{大小为 } B = \mu_r \mu_0 n i)
   $$
3. **求磁化强度 $\vec{M}$**：
   由 $\vec{M} = \chi\vec{H} = (\mu_r - 1)\vec{H}$（或 $\vec{M} = \frac{\vec{B}}{\mu_0} - \vec{H}$）：
   $$
   \vec{M} = (\mu_r - 1)n i\,\hat{z} \qquad (\text{大小为 } M = (\mu_r - 1)n i)
   $$
4. **求磁介质圆柱外表面的束缚面电流密度 $\vec{K}_b$**：
   在圆柱形磁介质外表面上，外法向单位矢量为径向 $\hat{n} = \hat{r}$。由束缚面电流公式 $\vec{K}_b = \vec{M} \times \hat{n}$ 及柱坐标基矢叉乘关系 $\hat{z}\times\hat{r} = \hat{\phi}$：
   $$
   \vec{K}_b = \vec{M} \times \hat{r} = (\mu_r - 1)n i\,(\hat{z} \times \hat{r}) = (\mu_r - 1)n i\,\hat{\phi} \qquad (\text{大小为 } K_b = (\mu_r - 1)n i)
   $$
   （物理意义：当 $\mu_r > 1$ 时，磁介质表面的束缚面电流 $K_b$ 与螺线管自由面电流 $ni$ 的环绕方向相同，两者叠加的总面电流密度恰好为 $J_{s,\text{tot}} = ni + (\mu_r - 1)ni = \mu_r ni$，从而将管内磁场放大为 $\mu_r\mu_0 ni$！）。

</details>

<details markdown="1">
<summary>Exercise 10.3: Two-Level Statistical Model of a Paramagnetic Solid（二能级顺磁固体的磁化曲线与居里常数推导）</summary>

**Problem Statement:**
A paramagnetic solid contains $n$ identical atoms per unit volume, each carrying a permanent magnetic dipole moment of magnitude $\mu$. The solid is held at absolute temperature $T$ in a uniform external magnetic field $\vec{B} = B\hat{z}$ with $B > 0$, and the dipoles do not interact with one another. Assume, as in Section 10.3, that each moment can point only parallel or antiparallel to $\vec{B}$, and that the fractions of atoms in the two states are proportional to $e^{\mu B/k_B T}$ and $e^{-\mu B/k_B T}$ respectively, where $k_B$ is Boltzmann's constant.
(a) Find the magnetization $M$ of the solid. Show that for $\mu B \ll k_B T$ it reduces to Curie's law $M = CB/T$, and give both the Curie constant $C$ and the saturation magnetization $M_{\max}$ in terms of $n, \mu$ and $k_B$.
(b) Find the value of $B/T$ at which the magnetization reaches half of $M_{\max}$.

---

**中文解析：**

**(a) 磁化强度精确解、饱和磁化强度与高温弱场居里定律极限**：
设单位体积内磁矩平行于 $\vec{B}$（$\mu_z = +\mu$）和反平行于 $\vec{B}$（$\mu_z = -\mu$）的原子数分别为 $n_+$ 和 $n_-$（满足 $n_+ + n_- = n$）。
由题意知两态占据概率之比为 $\frac{n_+}{n_-} = \frac{e^{\mu B/k_B T}}{e^{-\mu B/k_B T}}$，归一化后两态各自的原子数密度为：

$$
n_+ = n \frac{e^{\mu B/k_B T}}{e^{\mu B/k_B T} + e^{-\mu B/k_B T}}, \qquad n_- = n \frac{e^{-\mu B/k_B T}}{e^{\mu B/k_B T} + e^{-\mu B/k_B T}}
$$

因此，单位体积内的净磁偶极矩（即磁化强度 $M$）为：

$$
M = \mu n_+ - \mu n_- = n\mu \left( \frac{e^{\mu B/k_B T} - e^{-\mu B/k_B T}}{e^{\mu B/k_B T} + e^{-\mu B/k_B T}} \right) = n\mu \tanh\left(\frac{\mu B}{k_B T}\right)
$$

- **饱和磁化强度 $M_{\max}$**：当 $\frac{\mu B}{k_B T} \to \infty$ 时，$\tanh\left(\frac{\mu B}{k_B T}\right) \to 1$，所有偶极子完全对齐，故：
  $$
  M_{\max} = n\mu
  $$
- **弱场高温极限（$\mu B \ll k_B T$）与居里常数 $C$**：
  当无量纲小量 $x = \frac{\mu B}{k_B T} \ll 1$ 时，利用一阶泰勒展开 $e^{\pm x} \approx 1 \pm x$（故 $\tanh x = \frac{(1+x)-(1-x)}{(1+x)+(1-x)} \approx x$）：
  $$
  M \approx n\mu \left(\frac{\mu B}{k_B T}\right) = \left(\frac{n\mu^2}{k_B}\right)\frac{B}{T} = C\frac{B}{T}
  $$
  这正是居里定律，其中居里常数为 **$C = \dfrac{n\mu^2}{k_B}$**。

---

**(b) 磁化强度达到饱和值一半（$M = \frac{1}{2}M_{\max}$）时的 $B/T$ 值**：
令 $\frac{M}{M_{\max}} = \tanh\left(\frac{\mu B}{k_B T}\right) = \frac{1}{2}$，即：

$$
\frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{1}{2} \implies 2(e^{2x} - 1) = e^{2x} + 1 \implies e^{2x} = 3 \implies x = \frac{1}{2}\ln 3
$$

将 $x = \frac{\mu B}{k_B T}$ 代回，解得：

$$
\frac{B}{T} = \frac{k_B \ln 3}{2\mu} = \frac{k_B}{\mu}\operatorname{artanh}\left(\frac{1}{2}\right) \approx 0.549\,\frac{k_B}{\mu}
$$

</details>

<details markdown="1">
<summary>Exercise 10.4: Classical Orbital Model of Diamagnetism（抗磁性的经典电子轨道模型严格推导）</summary>

**Problem Statement:**
In a classical model of diamagnetism, an electron of charge $-e$ (with $e > 0$) and mass $m$ moves in a circle of radius $r$ about a fixed nucleus, the electrostatic attraction supplying the centripetal force, with angular speed $\omega_0$. A uniform magnetic field $\vec{B} = B\hat{n}$ with $B > 0$ is then applied along the normal $\hat{n}$ to the plane of the orbit, slowly enough that the electron stays on a circular orbit, of the same radius $r$, at every stage. Work to first order in $B$.
(a) Find the new angular speed, for each of the two senses in which the electron may circulate about $\hat{n}$.
(b) Find the change $\Delta\vec{\mu}$ in the orbital magnetic dipole moment in each case, and show that $\Delta\vec{\mu}$ opposes $\vec{B}$ whichever way the electron circulates.

---

**中文解析：**

**(a) 两种绕行方向下的新角速率 $\omega$**：
在未加磁场时，原子核对电子的静电库仑引力提供向心力：$F_E = m\omega_0^2 r$（这里规定 $\omega_0 > 0$ 为角速率大小）。
当沿轨道平面法向 $\hat{n}$ 施加外磁场 $\vec{B} = B\hat{n}$ 后，分两种绕行方向考察电子所受洛伦兹力 $\vec{F}_B = -e\vec{v}\times\vec{B}$ 的方向（保持轨道半径 $r$ 不变，故 $F_E = m\omega_0^2 r$ 不变）：

1. **情形 I：电子沿右手螺旋正方向（绕 $\hat{n}$ 逆时针 Counterclockwise）运动**：
   此时速度方向为 $+\hat{\phi}$，$\vec{v}\times\vec{B} = (\omega r\hat{\phi})\times(B\hat{n}) = +\omega r B\,\hat{r}$（指向圆外），由于电子带负电（$-e$），洛伦兹力 $\vec{F}_B = -e\omega r B\,\hat{r}$ **指向圆心**（与库仑引力同向，共同提供向心力）：
   $$
   m\omega^2 r = F_E + e\omega r B = m\omega_0^2 r + e\omega r B \implies \omega^2 - \omega_0^2 = \frac{eB}{m}\omega
   $$
   设 $\omega = \omega_0 + \Delta\omega_1$，保留至 $B$ 的一阶小量（$\omega^2 - \omega_0^2 \approx 2\omega_0 \Delta\omega_1$，右侧 $\omega \approx \omega_0$）：
   $$
   2\omega_0 \Delta\omega_1 \approx \frac{eB}{m}\omega_0 \implies \Delta\omega_1 = +\frac{eB}{2m}, \qquad \omega_{\text{CCW}} = \omega_0 + \frac{eB}{2m}
   $$
2. **情形 II：电子沿右手螺旋反方向（绕 $\hat{n}$ 顺时针 Clockwise）运动**：
   此时速度方向为 $-\hat{\phi}$，洛伦兹力 $\vec{F}_B = +e\omega r B\,\hat{r}$ **背离圆心向外**（抵消一部分库仑向心力）：
   $$
   m\omega^2 r = F_E - e\omega r B = m\omega_0^2 r - e\omega r B \implies \omega^2 - \omega_0^2 = -\frac{eB}{m}\omega
   $$
   设 $\omega = \omega_0 + \Delta\omega_2$，同样保留至 $B$ 的一阶项：
   $$
   2\omega_0 \Delta\omega_2 \approx -\frac{eB}{m}\omega_0 \implies \Delta\omega_2 = -\frac{eB}{2m}, \qquad \omega_{\text{CW}} = \omega_0 - \frac{eB}{2m}
   $$

---

**(b) 两种绕行方向下轨道磁偶极矩的变化量 $\Delta\vec{\mu}$**：
电子圆周运动形成的等效环形电流大小为 $i = \frac{e\omega}{2\pi}$，轨道面积为 $A = \pi r^2$，故磁矩大小为 $\mu = iA = \frac{1}{2}er^2\omega$。注意电子带负电，电流方向与电子运动方向相反：

1. **情形 I（电子逆时针运动）**：
   电流顺时针流动，由右手定则知初始磁矩方向沿 **$-\hat{n}$**（与 $\vec{B}$ 反向）：$\vec{\mu}_{\text{CCW}} = -\frac{1}{2}er^2\omega_{\text{CCW}}\,\hat{n}$。
   由于 $\Delta\omega_1 = +\frac{eB}{2m} > 0$（角速率增大，反向磁矩的模长变大），磁矩矢量的变化量为：
   $$
   \Delta\vec{\mu}_{\text{CCW}} = -\frac{1}{2}er^2 \Delta\omega_1\,\hat{n} = -\frac{e^2 r^2}{4m}B\hat{n} = -\frac{e^2 r^2}{4m}\vec{B}
   $$
2. **情形 II（电子顺时针运动）**：
   电流逆时针流动，由右手定则知初始磁矩方向沿 **$+\hat{n}$**（与 $\vec{B}$ 同向）：$\vec{\mu}_{\text{CW}} = +\frac{1}{2}er^2\omega_{\text{CW}}\,\hat{n}$。
   由于 $\Delta\omega_2 = -\frac{eB}{2m} < 0$（角速率减小，同向磁矩的模长变小），磁矩矢量的变化量为：
   $$
   \Delta\vec{\mu}_{\text{CW}} = +\frac{1}{2}er^2 \Delta\omega_2\,\hat{n} = -\frac{e^2 r^2}{4m}B\hat{n} = -\frac{e^2 r^2}{4m}\vec{B}
   $$

**结论**：无论电子原本沿哪个方向绕核旋转，外磁场诱导出的轨道磁偶极矩变化量恒为 **$\Delta\vec{\mu} = -\dfrac{e^2 r^2}{4m}\vec{B}$**，永远与外加磁场 $\vec{B}$ 方向相反！

</details>