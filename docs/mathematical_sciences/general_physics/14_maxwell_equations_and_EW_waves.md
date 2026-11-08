# Chapter 14: Maxwell's Equations and EM Waves（麦克斯韦方程组与电磁波）

!!! abstract
    General Physics II (Electromagnetism) | 第十四章课堂与讲义笔记
    
    参考：
    
    - Lecture 14: *Maxwell's Equations and EM Waves* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 14: *Maxwell's Equations and EM Waves*
    - Halliday, Resnick & Krane, *Physics*, Chapter 38

## 1 位移电流与麦克斯韦方程组 (Displacement Current and Maxwell's Equations)

### 1.1 原安培定理在非稳恒情形下的数学矛盾与“位移电流”修正

在第十一章引入法拉第电磁感应定律后，当时的电磁学基本方程组写为：

$$
\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}, \qquad \nabla \cdot \vec{B} = 0, \qquad \nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}, \qquad \nabla \times \vec{B} = \mu_0 \vec{j}
$$

在矢量微积分中，对于任意光滑矢量场 $\vec{A}$，**旋度的散度恒等于零**：$\nabla \cdot (\nabla \times \vec{A}) \equiv 0$。用这一数学恒等式分别检验上述两个旋度方程：

1. **检验法拉第定律**：对 $\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$ 两边取散度，得 $\nabla \cdot (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \cdot \vec{B}) = 0$，这与磁场高斯定理 $\nabla \cdot \vec{B} = 0$ 完全自洽。
2. **检验安培环路定理（致命矛盾 Fatal Inconsistency）**：对 $\nabla \times \vec{B} = \mu_0 \vec{j}$ 两边取散度，结合第六章的电荷守恒连续性方程 $\nabla \cdot \vec{j} = -\frac{\partial\rho}{\partial t}$ 与电场高斯定理 $\rho = \epsilon_0(\nabla \cdot \vec{E})$：
   $$
   \nabla \cdot (\nabla \times \vec{B}) = \mu_0(\nabla \cdot \vec{j}) = -\mu_0 \frac{\partial\rho}{\partial t} = -\mu_0 \epsilon_0 \frac{\partial}{\partial t}(\nabla \cdot \vec{E}) = -\nabla \cdot \left(\mu_0 \epsilon_0 \frac{\partial\vec{E}}{\partial t}\right)
   $$
   当电流非稳恒、空间电荷分布随时间变化（$\frac{\partial\rho}{\partial t} \neq 0$）时，上式右侧不为零，直接违背了数学恒等式 $\nabla \cdot (\nabla \times \vec{B}) \equiv 0$！

**麦克斯韦的修正（Maxwell's Fix）**：
麦克斯韦敏锐地指出，只需在安培环路定理右侧补上一项由变化电场产生的等效电流密度——**位移电流密度**（Displacement Current Density，记作 $\vec{j}_d$ 或 $\vec{J}_d$）：

$$
\vec{j}_d \equiv \epsilon_0 \frac{\partial\vec{E}}{\partial t}, \qquad i_d \equiv \int_S \vec{j}_d \cdot d\vec{S} = \epsilon_0 \frac{d}{dt}\int_S \vec{E} \cdot d\vec{S} = \epsilon_0 \frac{d\Phi_E}{dt}
$$

将安培定理修正为**安培-麦克斯韦定律**（Ampère-Maxwell Law）：

$$
\nabla \times \vec{B} = \mu_0(\vec{j} + \vec{j}_d) = \mu_0\left(\vec{j} + \epsilon_0\frac{\partial\vec{E}}{\partial t}\right) \iff \oint_C \vec{B} \cdot d\vec{l} = \mu_0 i_{\text{enc}} + \mu_0 \epsilon_0 \frac{d}{dt}\int_S \vec{E} \cdot d\vec{S}
$$

此时再取散度：$\nabla \cdot (\nabla \times \vec{B}) = \mu_0\left(\nabla \cdot \vec{j} + \epsilon_0\frac{\partial}{\partial t}\nabla \cdot \vec{E}\right) = \mu_0\left(\nabla \cdot \vec{j} + \frac{\partial\rho}{\partial t}\right) = 0$，数学矛盾彻底消除！

### 1.2 充电电容器的张成曲面佯谬与物理意义

考察正在通过直导线以电流 $i = \frac{dq}{dt}$ 充电的平行板电容器（极板面积为 $A$，忽略边缘效应）。围绕左端输电导线取一个闭合安培环路 $C$，并根据斯托克斯定理任选以 $C$ 为边界的张成曲面：

- **选取平坦圆盘面 $S_1$（直接切割导线）**：穿过 $S_1$ 的传导电流为 $i_{\text{enc}} = i$，而导线外无电场（$\Phi_E = 0 \implies i_d = 0$），安培环路积分给出 $\oint_C \vec{B}\cdot d\vec{l} = \mu_0 i$。
- **选取袋状曲面 $S_2$（从两极板之间的空隙穿过，不接触任何导线）**：穿过 $S_2$ 的真实传导电流为零（$i_{\text{enc}} = 0$）！但极板间存在随时间增强的匀强电场 $E = \frac{q}{\epsilon_0 A}$，穿过 $S_2$ 的位移电流恰好为：
  $$
  i_d = \epsilon_0 \frac{d}{dt}(EA) = \epsilon_0 A \frac{d}{dt}\left(\frac{q}{\epsilon_0 A}\right) = \frac{dq}{dt} = i
  $$
  因此，在计入位移电流项后，曲面 $S_2$ 同样给出 $\oint_C \vec{B}\cdot d\vec{l} = \mu_0(0 + i_d) = \mu_0 i$！

**深刻的物理对称性**：位移电流 $i_d$ 在形式上将导线中的传导电流 $i$ 连续地“接力延续”穿过了电容器极板间隙。更重要的是，在电容器两极板之间虽无任何传导电流（$j = 0$），但变化的电场 $\frac{\partial\vec{E}}{\partial t}$ 依然在极板间激发出了环绕轴线的真实磁场 $\vec{B}$。**正如法拉第定律指出“变化的磁场激发电场”，麦克斯韦位移电流揭示了其逆过程——“变化的电场激发磁场”**！

### 1.3 麦克斯韦方程组汇总与磁单极子讨论

至此，经典电动力学的全部理论大厦由**麦克斯韦方程组**（Maxwell's Equations）与**洛伦兹力定律**（Lorentz Force Law）完整概括：

| 定律名称 | 微分形式（Differential Form） | 积分形式（Integral Form，静止回路/曲面） | 物理角色与内涵 |
| :--- | :--- | :--- | :--- |
| **1. 电场高斯定理**<br>（Gauss' Law for $\vec{E}$） | $$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$$ | $$\oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\epsilon_0}\int_V \rho\,dV = \frac{q_{\text{enc}}}{\epsilon_0}$$ | **瞬时空间约束**：电荷是电场的源与汇（库仑平方反比律） |
| **2. 磁场高斯定理**<br>（Gauss' Law for $\vec{B}$） | $$\nabla \cdot \vec{B} = 0$$ | $$\oint_S \vec{B} \cdot d\vec{S} = 0$$ | **瞬时空间约束**：自然界无磁单极子，磁感线恒闭合 |
| **3. 法拉第感应定律**<br>（Faraday's Law） | $$\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$$ | $$\oint_C \vec{E} \cdot d\vec{l} = -\frac{d}{dt}\int_S \vec{B} \cdot d\vec{S}$$ | **场的时间演化**：变化的磁场激发涡旋电场 |
| **4. 安培-麦克斯韦定律**<br>（Ampère-Maxwell Law） | $$\nabla \times \vec{B} = \mu_0\left(\vec{j} + \epsilon_0\frac{\partial\vec{E}}{\partial t}\right)$$ | $$\oint_C \vec{B} \cdot d\vec{l} = \mu_0\int_S \vec{j}\cdot d\vec{S} + \mu_0\epsilon_0\frac{d}{dt}\int_S \vec{E}\cdot d\vec{S}$$ | **场的时间演化**：传导电流与变化的电场共同激发磁场 |
| **洛伦兹力公式**<br>（Lorentz Force Law） | \multicolumn{2}{c|}{$$\vec{F} = q\left(\vec{E} + \vec{v} \times \vec{B}\right)$$（结合牛顿第二定律决定电荷运动）} | **场对物质的作用**：电磁场对带电粒子施加作用力 |

*注：关于磁荷（Magnetic Charge, Section 14.2）：麦克斯韦方程组中唯一的不对称性在于存在电的静止源（电荷 $\rho$ 与电流 $\vec{j}$），却不存在磁荷 $\rho_m$ 与磁流 $\vec{j}_m$。保罗·狄拉克（Paul Dirac）曾证明，宇宙中只要存在一个磁单极子，就能从量子力学上完美解释为什么电荷是量子化的；但迄今为止所有实验搜寻均未发现磁单极子，$\nabla\cdot\vec{B} = 0$ 在实验精度内严格成立。*

---

## 2 电磁波与平面波性质 (The Traveling Electromagnetic Wave)

### 2.1 真空中电磁波动方程的严格推导与光速的理论预言

在没有电荷和电流的真空区域（$\rho = 0, \ \vec{j} = \vec{0}$），麦克斯韦方程组具有高度的对称性：

$$
\nabla \cdot \vec{E} = 0, \qquad \nabla \cdot \vec{B} = 0, \qquad \nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}, \qquad \nabla \times \vec{B} = \mu_0 \epsilon_0 \frac{\partial\vec{E}}{\partial t}
$$

为了将耦合的一阶偏微分方程组解耦，分别对后两个旋度方程两边再取一次旋度，并交换空间求导与时间求导的次序：

$$
\nabla \times (\nabla \times \vec{E}) = \nabla \times \left(-\frac{\partial\vec{B}}{\partial t}\right) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0 \epsilon_0 \frac{\partial^2\vec{E}}{\partial t^2}
$$

$$
\nabla \times (\nabla \times \vec{B}) = \nabla \times \left(\mu_0 \epsilon_0 \frac{\partial\vec{E}}{\partial t}\right) = \mu_0 \epsilon_0 \frac{\partial}{\partial t}(\nabla \times \vec{E}) = -\mu_0 \epsilon_0 \frac{\partial^2\vec{B}}{\partial t^2}
$$

应用矢量分析中著名的**旋度之旋度恒等式**（由矢量三重积 $\vec{A}\times(\vec{B}\times\vec{C}) = \vec{B}(\vec{A}\cdot\vec{C}) - (\vec{A}\cdot\vec{B})\vec{C}$ 取 $\vec{A}=\vec{B}=\nabla$ 导出）：

$$
\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2\vec{A}
$$

代入真空条件 $\nabla \cdot \vec{E} = 0$ 与 $\nabla \cdot \vec{B} = 0$，左边简化为 $-\nabla^2\vec{E}$ 与 $-\nabla^2\vec{B}$。消去负号，即得到 $\vec{E}$ 和 $\vec{B}$ 满足的三维**波动方程**（Wave Equation）：

$$
\nabla^2 \vec{E} = \mu_0 \epsilon_0 \frac{\partial^2\vec{E}}{\partial t^2}, \qquad \nabla^2 \vec{B} = \mu_0 \epsilon_0 \frac{\partial^2\vec{B}}{\partial t^2}
$$

对比标准波动方程 $\nabla^2 \psi = \frac{1}{c^2}\frac{\partial^2 \psi}{\partial t^2}$（一维形式 $\frac{\partial^2\psi}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2}$ 的通解为沿 $\pm x$ 方向传播的行波 $\psi = \psi_1(x - ct) + \psi_2(x + ct)$），麦克斯韦发现电磁波在真空中的传播速率 $c$ 完全由两个电磁学基本常数决定：

$$
c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = \frac{1}{\sqrt{(4\pi \times 10^{-7}\text{ N/A}^2)(8.854 \times 10^{-12}\text{ F/m})}} \approx 2.998 \times 10^8\text{ m/s}
$$

这一数值与实验测得的**光速**惊人地吻合！麦克斯韦据此断定**光就是一种电磁波**，在赫兹（Hertz, 1887）于实验室产生无线电波二十多年前，便将整个光学（Optics）统一为电磁学的一个分支。

**电磁波谱（The Electromagnetic Spectrum）与电磁波的发射**：
所有电磁波在真空中均以同一光速 $c = \lambda f = \omega/k$ 传播。按波长 $\lambda$ 从长到短（频率从低到高），电磁波谱依次涵盖：**无线电波**（Radio waves, $\lambda > 0.1\text{ m}$）、**微波**（Microwaves）、**红外线**（Infrared）、**可见光**（Visible light，仅占 $400\text{ nm} \sim 700\text{ nm}$ 的极窄窗口）、**紫外线**（Ultraviolet）、**X 射线**（X-rays）与 **$\gamma$ 射线**（Gamma rays, $\lambda < 10^{-11}\text{ m}$）。宏观上，电磁波由**加速运动的电荷**（Accelerating charges，如 LC 振荡器通过传输线驱动电偶极天线 Electric dipole antenna 中的振荡电荷）向外辐射产生。

### 2.2 平面电磁波的三大结构性质

考察沿 $+x$ 方向（波矢 $\vec{k} = k\hat{x}$，其中波数 $k = \frac{2\pi}{\lambda}$，角频率 $\omega = \frac{2\pi}{T} = ck$，传播方向单位矢量 $\hat{k} = \hat{x}$）传播的单色平面电磁波试探解：

$$
\vec{E}(x, t) = \vec{E}_0 \cos[k(x - ct) + \phi] = \vec{E}_0 \cos(kx - \omega t + \phi), \qquad \vec{B}(x, t) = \vec{B}_0 \cos[k'(x - ct) + \phi']
$$

虽然波动方程允许任意方向的常矢量 $\vec{E}_0, \vec{B}_0$，但一阶**麦克斯韦方程组对 $\vec{E}$ 和 $\vec{B}$ 施加了三条严格的附加几何与代数约束**：

1. **横波性（Transverse Wave Property）**：
   计算散度得 $\nabla \cdot \vec{E} = -k(\hat{x}\cdot\vec{E}_0)\sin(kx - \omega t + \phi) = 0$，以及 $\nabla \cdot \vec{B} = -k'(\hat{x}\cdot\vec{B}_0)\sin(k'x - \omega' t + \phi') = 0$。这要求在任意时刻和位置必有：
   $$
   \hat{k} \cdot \vec{E} = 0, \qquad \hat{k} \cdot \vec{B} = 0 \iff E_x = B_x = 0
   $$
   即**电场矢量 $\vec{E}$ 与磁场矢量 $\vec{B}$ 均垂直于波的传播方向 $\hat{k}$，真空中的电磁波是严格的横波**！
2. **同频同相性（Identical Frequency and In-Phase Oscillation）**：
   将 $\nabla \times \vec{E} = -k(\hat{x} \times \vec{E}_0)\sin(kx - \omega t + \phi)$ 与 $-\frac{\partial\vec{B}}{\partial t} = -k'c\vec{B}_0\sin(k'x - \omega' t + \phi')$ 代入法拉第定律 $\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$。要使该式在所有 $(x, t)$ 处恒成立，两正弦函数必须完全同步：
   $$
   k' = k \quad (\omega' = \omega), \qquad \phi' = \phi
   $$
   即**电场 $\vec{E}$ 与磁场 $\vec{B}$ 具有相同的频率和完全相同的相位**（在同一时刻、同一空间位置同时达到波峰、波谷或零点）。
3. **正交右手螺旋与振幅锁定关系（Mutual Orthogonality and Amplitude Ratio）**：
   由法拉第定律的系数相等，直接得到 $\vec{E}$ 与 $\vec{B}$ 的矢量叉乘锁定关系（推广至任意传播方向 $\hat{k}$）：
   $$
   \vec{k} \times \vec{E}_0 = \omega \vec{B}_0 \iff \vec{B} = \frac{1}{c}\left(\hat{k} \times \vec{E}\right), \qquad E_0 = c B_0 \quad (E = cB)
   $$
   这表明：**$\vec{E}$ 与 $\vec{B}$ 处处相互垂直（$\vec{E} \perp \vec{B}$）**，且 $(\vec{E}, \vec{B}, \hat{k})$ 严格构成**右手正交螺旋系**（$\vec{E} \times \vec{B}$ 指向波的传播方向 $\hat{k}$）。

---

## 3 电磁波的能量传输与动量光压 (Energy Transport, Poynting Vector & Radiation Pressure)

### 3.1 坡印廷定理与坡印廷矢量 (Poynting's Theorem and Poynting Vector)

空间电磁场的总能量密度为电场能密度与磁场能密度之和：

$$
u = u_E + u_B = \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0} B^2
$$

**1. 电磁场能量的局域守恒定律（坡印廷定理）**

对总能量密度 $u$ 求时间偏导数，并代入麦克斯韦旋度方程 $\epsilon_0\frac{\partial\vec{E}}{\partial t} = \frac{1}{\mu_0}\nabla\times\vec{B} - \vec{j}$ 与 $\frac{\partial\vec{B}}{\partial t} = -\nabla\times\vec{E}$：

$$
\frac{\partial u}{\partial t} = \epsilon_0 \vec{E}\cdot\frac{\partial\vec{E}}{\partial t} + \frac{1}{\mu_0}\vec{B}\cdot\frac{\partial\vec{B}}{\partial t} = \frac{1}{\mu_0}\vec{E}\cdot(\nabla\times\vec{B}) - \frac{1}{\mu_0}\vec{B}\cdot(\nabla\times\vec{E}) - \vec{j}\cdot\vec{E}
$$

应用第四章的叉乘散度恒等式 $\nabla \cdot (\vec{E} \times \vec{B}) = \vec{B}\cdot(\nabla\times\vec{E}) - \vec{E}\cdot(\nabla\times\vec{B})$，立即得到**电磁能量连续性方程（坡印廷定理微分形式）**：

$$
\nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = -\vec{j} \cdot \vec{E} \qquad \left(\text{在无电流真空中 }\vec{j} = \vec{0} \implies \nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = 0\right)
$$

其中定义了表征单位时间内垂直穿过单位面积的电磁能量流——**坡印廷矢量**（Poynting Vector，又称**能流密度矢量**，SI 单位为 $\text{W/m}^2$）：

$$
\vec{S} \equiv \frac{1}{\mu_0} \vec{E} \times \vec{B}
$$

（物理意义：右端源项 $-\vec{j}\cdot\vec{E}$ 表示电磁场对电流载流子做功的功率密度；当电流在电阻中流动时，$\vec{j}\cdot\vec{E} = \rho_e J^2 > 0$ 为焦耳热功率密度，表现为电磁场能量的“汇” Sink）。

**2. 平面电磁波中的能量均分与波强 / 光强（Intensity）**

在平面电磁波中，由于 $B = E/c$ 且 $c^2 = \frac{1}{\mu_0\epsilon_0}$，**电场能量密度与磁场能量密度在任何时刻、任何地点都严格相等**：

$$
u_B = \frac{B^2}{2\mu_0} = \frac{(E/c)^2}{2\mu_0} = \frac{\mu_0 \epsilon_0 E^2}{2\mu_0} = \frac{1}{2}\epsilon_0 E^2 = u_E \implies u = u_E + u_B = \epsilon_0 E^2 = \frac{B^2}{\mu_0}
$$

瞬时能流密度大小为 $S = \frac{EB}{\mu_0} = \epsilon_0 c E^2 = u c = (u_E + u_B)c$。对高频余弦平方项 $\cos^2(kx - \omega t + \phi)$ 在一个周期内求时间平均（$\langle\cos^2\rangle = \frac{1}{2}$），定义坡印廷矢量的时间平均值为电磁波的**波强**或**光强**（Intensity，记作 $I$ 或 $\overline{S}$）：

$$
\overline{\vec{S}} = \frac{1}{2\mu_0}\vec{E}_0 \times \vec{B}_0, \qquad I = \overline{S} = S_{\text{avg}} = \frac{E_0 B_0}{2\mu_0} = \frac{1}{2}\epsilon_0 c E_0^2 = \frac{E_0^2}{2\mu_0 c} = \frac{c B_0^2}{2\mu_0}
$$

对于辐射总功率为 $P_s$ 的各向同性点波源（Isotropic point source），球面波前在半径 $r$ 处的球面面积为 $4\pi r^2$，由能量守恒可知波强随距离按**平方反比律**衰减：

$$
I(r) = \frac{P_s}{4\pi r^2}
$$

### 3.2 电磁波的动量与辐射压强 / 光压 (Momentum and Radiation Pressure)

电磁波不仅携带能量，还携带**线动量**（Linear Momentum）。由麦克斯韦方程组消去电荷与电流后可以证明，全空间机械动量 $\vec{p}_{\text{mech}}$ 与电磁场动量的总和守恒：

$$
\frac{\partial}{\partial t}\left(\vec{p}_{\text{mech}} + \frac{1}{c^2}\int_V \vec{S}\,dV\right) = \vec{0} \implies \text{电磁场的动量密度 } \vec{g} = \frac{\vec{S}}{c^2}, \qquad \text{动量流率 } \frac{\vec{S}}{c}
$$

即若物体吸收了能量为 $\Delta U$ 的电磁辐射，则物体获得的动量大小为 $\Delta p = \frac{\Delta U}{c}$。

当波强为 $I$ 的平行光束（或电磁波）**垂直入射**到面积为 $A$ 的平坦表面上时，在 $\Delta t$ 时间内入射到表面上的总能量为 $\Delta U = I A \Delta t$，产生的平均作用力为 $F = \frac{\Delta p}{\Delta t}$，由此得到作用在单位面积上的**辐射压强 / 光压**（Radiation Pressure，记作 $p_r = \frac{F}{A}$，单位 $\text{Pa} = \text{N/m}^2$）：

| 表面光学性质 | $\Delta t$ 时间内传递的动量 $\Delta p$ | 辐射压强（光压）公式 $p_r = F/A$ | 物理机制说明 |
| :--- | :---: | :---: | :--- |
| **1. 完全吸收（Total Absorption）** | $\Delta p = \dfrac{\Delta U}{c} = \dfrac{I A \Delta t}{c}$ | $$p_r = \frac{I}{c}$$ | 入射光子动量全部被靶面吸收，无反射波 |
| **2. 完全反射（Total Reflection）** | $\Delta p = \dfrac{2\Delta U}{c} = \dfrac{2 I A \Delta t}{c}$ | $$p_r = \frac{2I}{c}$$ | 光波原路反向弹回，动量改变量加倍（如同弹性碰撞） |

---

## 4 Chapter 14 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 14.1, 14.2 & 14.3: Capacitor Displacement Current, Plane Wave Parameters & Wire Poynting Vector（电容器位移电流、平面波参数与载流导线内坡印廷矢量）</summary>

**Problem Statement:**
- **Ex 14.1**: A capacitor consists of two parallel circular plates, each of radius $a$. We connect the capacitor to an AC emf such that the charge on the capacitor follows $Q = Q_0\sin\omega t$. Calculate the displacement current density $j_d$, the total displacement current $i_d$, and the magnetic field $B$ at a distance $r < a$ from the axis, assuming $\omega a \ll c$ and ignoring boundary effects.
- **Ex 14.2**: An electromagnetic wave is traveling in vacuum, where the electric field part is given by $E_x = 0, \ E_y = 0.30\cos[\omega(t - x/c)]\text{ V/m}, \ E_z = 0$, where $\omega = 2\pi \times 10^8\text{ s}^{-1}$. Calculate: (a) The wavelength; (b) The propagation direction; (c) The magnitude and direction of the magnetic field.
- **Ex 14.3**: A steady current $i$ is flowing through a long cylindrical lead of radius $a$ and resistivity $\rho_e$ (uniform current and electric field). (a) Calculate the magnitudes and directions of $\vec{E}, \vec{B}$ and the Poynting vector $\vec{S}$ at a distance $r < a$ from the central axis. (b) Verify the continuity equation $\nabla\cdot\vec{S} + \frac{\partial u}{\partial t} = -\rho_e J^2 = -\vec{j}\cdot\vec{E}$ inside the lead.

---

**中文解析：**

**1. 圆形平行板电容器内的位移电流与感生磁场（Exercise 14.1）**：
极板面积为 $A = \pi a^2$，极板间匀强电场大小为 $E(t) = \frac{Q(t)}{\epsilon_0 \pi a^2} = \frac{Q_0}{\epsilon_0 \pi a^2}\sin(\omega t)$。

- **位移电流密度 $j_d$**：
  $$
  j_d = \epsilon_0 \frac{\partial E}{\partial t} = \frac{Q_0 \omega}{\pi a^2}\cos(\omega t)
  $$
- **总位移电流 $i_d$**：
  $$
  i_d = j_d (\pi a^2) = Q_0 \omega \cos(\omega t) \qquad \left(\text{恰好等于传导电流 } i = \frac{dQ}{dt}\right)
  $$
- **极板间距离轴线 $r < a$ 处的磁感应强度 $B(r, t)$**：
  由轴对称性，取半径为 $r < a$ 的同心圆作为安培环路（穿过该圆面的传导电流为 $0$，位移电流为 $\pi r^2 j_d$），应用安培-麦克斯韦定律 $2\pi r B = \mu_0(\pi r^2 j_d)$：
  $$
  B(r, t) = \frac{1}{2}\mu_0 j_d r = \frac{\mu_0 Q_0 \omega r}{2\pi a^2}\cos(\omega t) \qquad (r < a)
  $$

---

**2. 真空平面电磁波的波长、传播方向与伴随磁场（Exercise 14.2）**：

- **(a) 波长 $\lambda$**：
  由 $\omega = 2\pi f = 2\pi \times 10^8\text{ rad/s}$ 得频率 $f = 10^8\text{ Hz}$。故波长为：
  $$
  \lambda = \frac{c}{f} = \frac{2\pi c}{\omega} = \frac{3.00 \times 10^8\text{ m/s}}{10^8\text{ s}^{-1}} = 3.0\text{ m}
  $$
- **(b) 传播方向**：
  相位因子为 $\omega\left(t - \frac{x}{c}\right) = \omega t - kx$，等相面满足 $x - ct = \text{const}$，故电磁波沿 **$+x$ 轴正方向**（$\hat{k} = +\hat{x}$）传播。
- **(c) 磁场的方向与大小**：
  由平面波正交关系 $\vec{B} = \frac{1}{c}(\hat{k}\times\vec{E})$，因 $\hat{k} = \hat{x}$ 且 $\vec{E} = E_y\hat{y}$，故 $\vec{B}$ 沿 **$+z$ 轴方向**（$\hat{x}\times\hat{y} = \hat{z}$）。
  磁场振幅为 $B_0 = \frac{E_0}{c} = \frac{0.30\text{ V/m}}{3.00 \times 10^8\text{ m/s}} = 1.0 \times 10^{-9}\text{ T} = 1.0\text{ nT}$，完整表达式为：
  $$
  \vec{B}(x, t) = \left(1.0 \times 10^{-9}\text{ T}\right)\cos\left[\omega\left(t - \frac{x}{c}\right)\right]\hat{z}
  $$

---

**3. 稳恒载流圆柱导线内部的坡印廷矢量与焦耳热能量流守恒（Exercise 14.3，深刻物理图像题）**：

- **(a) 求导线内部 $r < a$ 处的 $\vec{E}, \vec{B}$ 与 $\vec{S}$**：
  设圆柱导线轴线沿 $+z$ 方向，电流 $i$ 沿 $+\hat{z}$ 均匀分布，电流密度大小为 $J = \frac{i}{\pi a^2}$：
  1. **电场 $\vec{E}$**：由欧姆定律 $\vec{E} = \rho_e \vec{j}$，方向**沿轴向 $+\hat{z}$（平行于电流方向）**，大小为：
     $$
     E = \rho_e J = \frac{\rho_e i}{\pi a^2}
     $$
  2. **磁场 $\vec{B}$**：由安培环路定理 $2\pi r B = \mu_0(\pi r^2 J)$，方向**沿方位角 $+\hat{\phi}$（右手螺旋环绕轴线）**，大小为：
     $$
     B(r) = \frac{1}{2}\mu_0 J r = \frac{\mu_0 i r}{2\pi a^2}
     $$
  3. **坡印廷矢量 $\vec{S}$**：利用柱坐标基矢叉乘 $\hat{z}\times\hat{\phi} = -\hat{r}$：
     $$
     \vec{S}(r) = \frac{1}{\mu_0}\vec{E} \times \vec{B} = \frac{1}{\mu_0}(\rho_e J\hat{z}) \times \left(\frac{1}{2}\mu_0 J r\hat{\phi}\right) = -\frac{1}{2}\rho_e J^2 r\,\hat{r} = -\frac{\rho_e i^2 r}{2\pi^2 a^4}\hat{r}
     $$
     即坡印廷矢量大小为 $S(r) = \frac{1}{2}\rho_e J^2 r = \dfrac{\rho_e i^2 r}{2\pi^2 a^4}$，方向**沿径向垂直指向导线中心轴线（$-\hat{r}$，Radially inward）**！
     *（物理图像：导线发热所需的能量并不是顺着导线内部轴向流动的，而是由周围空间的电磁场通过导线侧面沿径向源源不断地流入导线内部并转化为焦耳热的！）。*
- **(b) 验证能量连续性方程**：
  由于是稳恒电流，$\vec{E}$ 与 $\vec{B}$ 不随时间变化，故能量密度的时间导数 $\frac{\partial u}{\partial t} = 0$。
  在柱坐标系下计算径向矢量场 $\vec{S} = S_r(r)\hat{r}$ 的散度（其中 $S_r(r) = -\frac{1}{2}\rho_e J^2 r$）：
  $$
  \nabla \cdot \vec{S} + \frac{\partial u}{\partial t} = \frac{1}{r}\frac{d}{dr}\big(r S_r(r)\big) + 0 = \frac{1}{r}\frac{d}{dr}\left(-\frac{1}{2}\rho_e J^2 r^2\right) = -\rho_e J^2 = -\vec{j} \cdot \vec{E}
  $$
  方程两端严格相等，证毕。

</details>

<details markdown="1">
<summary>Exercise 14.4, 14.5 & 14.6: Feynman's Angular Momentum Paradox, Leaky Capacitor & Magnetic Monopoles（球形电容器电磁角动量、漏电电容器与磁单极子超导环）</summary>

**Problem Statement:**
- **Ex 14.4**: A spherical capacitor has inner shell radius $r_1$ (charge $+Q$) and outer shell radius $r_2$ (charge $-Q$). Initially it is at rest in a uniform field $\vec{B} = B\hat{z}$, which is later slowly removed. The two insulating shells are rigidly joined and can turn freely about the $z$ axis with moment of inertia $I$. Find the final angular velocity $\vec{\omega}$, with its sense relative to $+z$.
- **Ex 14.5**: A circular parallel-plate capacitor (radius $a$, separation $d \ll a$) is filled with a weakly conducting material ($\sigma, \epsilon_0$). At $t = 0$ the isolated plates carry $\pm Q_0$. (a) Find $Q(t)$ for $t > 0$. (b) Find the conduction current density $\vec{j}_c$, displacement current density $\vec{j}_d$, and magnetic field $\vec{B}$ between the plates. (c) Find the total heat produced, compare with initial stored energy, and explain using $\vec{S}$ where that heat comes from.
- **Ex 14.6**: Suppose magnetic charge existed ($\rho_m, \vec{j}_m$) with $\nabla\cdot\vec{B} = \mu_0\rho_m$ and $\nabla\cdot\vec{j}_m + \partial\rho_m/\partial t = 0$, where a point magnetic charge $q_m$ produces $\vec{B} = \frac{\mu_0 q_m \hat{r}}{4\pi r^2}$.
  (a) Show that Faraday's law requires adding $-\mu_0\vec{j}_m$ to its right-hand side to satisfy $\nabla\cdot(\nabla\times\vec{E}) = 0$, and write the integral form.
  (b) A superconducting ring ($R = 0$, self-inductance $L$) lies in the plane $z = 0$ with no initial current. A magnetic charge $q_m > 0$ moves along the $z$ axis from $-\infty$ to $+\infty$. Find the final current in the ring and its sense seen from above ($+z$).

---

**中文解析：**

**1. 球形电容器在撤去外磁场时的旋转效应——费曼角动量佯谬（Exercise 14.4，经典压轴名题）**：
当沿 $+z$ 轴的匀强磁场 $B_z(t)$ 随时间缓慢减弱时，由轴对称性与法拉第定律，在距 $z$ 轴垂直距离为 $\rho = r\sin\theta$ 的水平圆周上会激发出沿方位角方向的感生电场 $E_\phi$：

$$
2\pi \rho E_\phi = -\frac{d}{dt}\left(\pi \rho^2 B_z(t)\right) \implies E_\phi(r, \theta) = -\frac{1}{2}\rho \frac{dB_z}{dt} = -\frac{1}{2}r\sin\theta \frac{dB_z}{dt}
$$

考察半径为 $R$、均匀带有总电荷 $q$（面密度 $\sigma = \frac{q}{4\pi R^2}$）的绝缘球壳：在极角 $\theta \to \theta + d\theta$ 的细圆环带上，所带电荷为 $dq = \sigma(2\pi R^2\sin\theta\,d\theta) = \frac{1}{2}q\sin\theta\,d\theta$，力臂为 $\rho = R\sin\theta$。感生电场对该细圆环施加的绕 $z$ 轴微元力矩为：

$$
d\tau_z = \rho (E_\phi\,dq) = (R\sin\theta)\left(-\frac{1}{2}R\sin\theta\frac{dB_z}{dt}\right)\left(\frac{1}{2}q\sin\theta\,d\theta\right) = -\frac{1}{4}q R^2 \frac{dB_z}{dt}\sin^3\theta\,d\theta
$$

利用积分 $\int_0^\pi \sin^3\theta\,d\theta = \left[-\cos\theta + \frac{1}{3}\cos^3\theta\right]_0^\pi = \frac{4}{3}$，积分得到单层球壳所受的总力矩为 $\tau_z(R, q) = -\frac{1}{3}q R^2\frac{dB_z}{dt}$。
将内球壳（$r_1, +Q$）与外球壳（$r_2, -Q$）所受力矩相加，应用刚体定轴转动定律 $I\frac{d\omega_z}{dt} = \tau_{\text{tot}, z}$：

$$
I\frac{d\omega_z}{dt} = -\frac{1}{3}Q r_1^2 \frac{dB_z}{dt} - \frac{1}{3}(-Q) r_2^2 \frac{dB_z}{dt} = \frac{1}{3}Q(r_2^2 - r_1^2)\frac{dB_z}{dt}
$$

对时间从初态（$B_z = B, \ \omega_z = 0$）积分至终态（$B_z = 0, \ \Delta B_z = -B$），解得终态角速度为：

$$
\omega_z = -\frac{Q B (r_2^2 - r_1^2)}{3I} \iff \vec{\omega} = -\frac{Q B (r_2^2 - r_1^2)}{3I}\hat{z}
$$

由于 $r_2 > r_1$，外球壳 $-Q$ 的力臂更大，其顺时针力矩占优，故终态角速度沿 **$-\hat{z}$ 方向（从 $+z$ 往下看为顺时针旋转 Clockwise）**，大小为 $\dfrac{QB(r_2^2 - r_1^2)}{3I}$。
*（注：这恰好等于初态储存在两球壳之间正交电磁场中的总电磁角动量 $L_{\text{em}, z} = \int [\vec{r}\times(\epsilon_0\vec{E}\times\vec{B})]_z\,dV = -\frac{1}{3}QB(r_2^2 - r_1^2)$，完美体现了“电磁场角动量转化为机械角动量”的角动量守恒定律！）。*

---

**2. 漏电平行板电容器的自放电：传导电流与位移电流精确抵消（Exercise 14.5）**：

- **(a) 正极板电荷量 $Q(t)$ 的衰减规律**：
  设极板面积为 $A = \pi a^2$。任意时刻极板间电场为 $E(t) = \frac{Q(t)}{\epsilon_0 A}$，弱导电介质中的传导电流密度为 $j_c(t) = \sigma E(t) = \frac{\sigma}{\epsilon_0 A}Q(t)$。
  由电荷守恒，正极板电荷减少率等于流过介质的传导电流 $I_c = j_c A$：
  $$
  -\frac{dQ}{dt} = j_c A = \frac{\sigma}{\epsilon_0}Q(t) \implies Q(t) = Q_0 \exp\left(-\frac{\sigma}{\epsilon_0}t\right) \qquad (t > 0)
  $$
- **(b) 传导电流密度 $\vec{j}_c$、位移电流密度 $\vec{j}_d$ 与极板间磁场 $\vec{B}$**：
  设从正极板指向负极板的方向为 $\hat{z}$。则电场为 $\vec{E}(t) = \frac{Q(t)}{\epsilon_0 \pi a^2}\hat{z}$：
  - **传导电流密度**：
    $$
    \vec{j}_c(t) = \sigma\vec{E}(t) = +\frac{\sigma Q_0}{\epsilon_0 \pi a^2}\exp\left(-\frac{\sigma}{\epsilon_0}t\right)\hat{z}
    $$
  - **位移电流密度**：
    $$
    \vec{j}_d(t) = \epsilon_0\frac{\partial\vec{E}}{\partial t} = \frac{1}{\pi a^2}\frac{dQ}{dt}\hat{z} = -\frac{\sigma Q_0}{\epsilon_0 \pi a^2}\exp\left(-\frac{\sigma}{\epsilon_0}t\right)\hat{z} = -\vec{j}_c(t)
    $$
  - **极板间磁场 $\vec{B}$**：
    由于在极板间每一点处，传导电流密度与位移电流密度都等大反向（**$\vec{j}_c + \vec{j}_d \equiv \vec{0}$**），代入安培-麦克斯韦定律 $2\pi r B_\phi = \mu_0 \int (\vec{j}_c + \vec{j}_d)\cdot d\vec{S} = 0$，结合轴对称性可知**极板间的磁场处处恒等于零（$\vec{B} = \vec{0}$）**！
- **(c) 产生的总焦耳热与坡印廷矢量解释**：
  整个介质体积为 $V = A d$，耗散的总焦耳热为：
  $$
  H = \int_0^\infty (j_c E)(A d)\,dt = A d \sigma \int_0^\infty \frac{Q_0^2}{\epsilon_0^2 A^2}\exp\left(-\frac{2\sigma}{\epsilon_0}t\right)dt = \frac{Q_0^2 d}{2\epsilon_0 A} = \frac{Q_0^2}{2C} = U_E(0)
  $$
  即产生的总热量精确等于初始储存在电容器中的全部静电能！
  **坡印廷矢量解释**：因为极板间磁场处处为零（$\vec{B} = \vec{0}$），所以**坡印廷矢量处处为零（$\vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B} = \vec{0}$）**！这意味着没有任何能量需要从其他地方流入或流出，每一小块体积元内的静电能密度 $u_E = \frac{1}{2}\epsilon_0 E^2$ 直接**就地（Locally）**转化为该体积元内的焦耳热（$\frac{\partial u_E}{\partial t} = -\vec{j}_c\cdot\vec{E}$）。

---

**3. 含磁单极子的广义法拉第定律与超导环俘获磁荷电流（Exercise 14.6）**：

- **(a) 修正法拉第定律**：
  若 $\nabla\cdot\vec{B} = \mu_0\rho_m \neq 0$，则原法拉第定律取散度会给出 $\nabla\cdot(\nabla\times\vec{E}) = -\frac{\partial}{\partial t}(\nabla\cdot\vec{B}) = -\mu_0\frac{\partial\rho_m}{\partial t} = +\mu_0(\nabla\cdot\vec{j}_m) \neq 0$，违背恒等式 $\nabla\cdot(\nabla\times\vec{E}) \equiv 0$。
  在法拉第定律右侧加上 $-\mu_0\vec{j}_m$ 项：
  $$
  \nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t} - \mu_0 \vec{j}_m
  $$
  此时取散度得 $\nabla\cdot(\nabla\times\vec{E}) = -\mu_0\left(\frac{\partial\rho_m}{\partial t} + \nabla\cdot\vec{j}_m\right) = 0$，矛盾消除！
  应用斯托克斯定理，对固定闭合回路 $C$ 及张成曲面 $S$ 的积分形式为：
  $$
  \oint_C \vec{E} \cdot d\vec{l} = -\frac{d}{dt}\int_S \vec{B} \cdot d\vec{S} - \mu_0 \int_S \vec{j}_m \cdot d\vec{S}
  $$
- **(b) 磁单极子穿过超导环激发的持久电流**：
  取固定闭合回路 $C$ 沿着超导环导线内部，张成曲面 $S$ 为环所围的平圆盘（法向沿 $+\hat{z}$，逆时针为正）。
  由于超导体电阻为零，导线内部电场恒为零（$\vec{E} = \vec{0} \implies \oint_C \vec{E}\cdot d\vec{l} = 0$）。因此修正法拉第定律给出：
  $$
  \frac{d\Phi_B}{dt} + \mu_0 I_{m,\text{enc}}(t) = 0
  $$
  将上式对时间从 $t = -\infty$（磁荷在极下方，环中无电流）积分至 $t = +\infty$（磁荷已远去至极上方）：
  1. 磁单极子 $q_m > 0$ 从下方穿过圆盘 $S$ 到上方，穿过曲面的总积分磁荷量为 $\int_{-\infty}^{+\infty} I_{m,\text{enc}}(t)\,dt = +q_m$；
  2. 因此穿过超导环的磁通量总改变量必为 $\Delta\Phi_B = \Phi_B(+\infty) - \Phi_B(-\infty) = -\mu_0 q_m$；
  3. 而在 $t = \pm\infty$ 时，磁单极子距环无穷远，其自身在环处产生的磁通为零，环的终态磁通完全由环自身的持久自感电流 $I$ 产生：$\Phi_B(+\infty) = L I$（且初态 $\Phi_B(-\infty) = 0$）。
  联立立得：
  $$
  L I = -\mu_0 q_m \implies I = -\frac{\mu_0 q_m}{L}
  $$
  负号表示从上方（$+z$）往下看，超导环中的终态持久电流方向为**顺时针方向（Clockwise）**，大小为 $\dfrac{\mu_0 q_m}{L}$。

</details>

<details markdown="1">
<summary>Exercise 14.7, 14.8 & 14.9: Standing EM Waves, Radiating Current Sheet & Solar Sail Mechanics（电磁驻波、辐射电流薄板与全反射太阳帆力学）</summary>

**Problem Statement:**
- **Ex 14.7**: Two plane waves of amplitude $E_0$ and frequency $\omega = ck$ travel in opposite directions along $x$: $\vec{E}_1 = E_0\cos(kx - \omega t)\hat{y}$ and $\vec{E}_2 = E_0\cos(kx + \omega t)\hat{y}$.
  (a) Find the total fields $\vec{E}$ and $\vec{B}$, the nodal positions where $\vec{E} = \vec{0}$ at all times and where $\vec{B} = \vec{0}$ at all times, and the time from a maximum of $\vec{E}$ to the next maximum of $\vec{B}$.
  (b) Find the Poynting vector $\vec{S}$ of the total field, its time average at each $x$, and verify $\nabla\cdot\vec{S} + \partial u/\partial t = 0$.
  (c) If the two waves traveled at an unknown speed $v = \omega/k$ with $\vec{B} = (\hat{k}\times\vec{E})/v$, show that the total field satisfies Faraday's law for every $v$, but Ampère-Maxwell in vacuum only if $v = 1/\sqrt{\mu_0\epsilon_0}$.
- **Ex 14.8**: An infinitely thin sheet at $x = 0$ carries a driven surface current $\vec{K}(t) = K_0\cos(\omega t)\hat{y}$, radiating plane waves away on both sides ($\vec{E}$ along $y$, $\vec{B}$ along $z$).
  (a) Show that $E_y$ is continuous at $x = 0$ while $B_z(0^+, t) - B_z(0^-, t) = -\mu_0 K_0\cos(\omega t)$.
  (b) Find $\vec{E}$ and $\vec{B}$ on both sides ($x > 0$ and $x < 0$).
  (c) Find the time-averaged power per unit area carried away on each side, and show that together they equal the time-averaged power per unit area spent by the source, $\langle -\vec{K}\cdot\vec{E}(0, t) \rangle$.
- **Ex 14.9**: A flat mirror sail of area $A$ reflects light specularly in a beam of intensity $I$, with its normal at angle $\theta \ (0 \le \theta < \pi/2)$ to the beam.
  (a) Find the time-averaged force on the sail (magnitude and direction), and check $\theta = 0$.
  (b) Facing the Sun ($\theta = 0$, $L_\odot = 3.83 \times 10^{26}\text{ W}$, $M_\odot = 1.99 \times 10^{30}\text{ kg}$), find the areal mass density $m/A$ for which light's force balances solar gravity, show it is independent of $r$, and evaluate it.
  (c) Find the force component perpendicular to the beam, and the angle $\theta$ at which it is largest.

---

**中文解析：**

**1. 电磁驻波（Standing Electromagnetic Wave）的节点、能流吞吐与波速唯一性（Exercise 14.7）**：

- **(a) 总电场 $\vec{E}$、总磁场 $\vec{B}$ 与波节位置**：
  第一列波沿 $+\hat{x}$ 传播，$\vec{B}_1 = \frac{1}{c}(\hat{x}\times\vec{E}_1) = +\frac{E_0}{c}\cos(kx - \omega t)\hat{z}$；第二列波沿 $-\hat{x}$ 传播，$\vec{B}_2 = \frac{1}{c}(-\hat{x}\times\vec{E}_2) = -\frac{E_0}{c}\cos(kx + \omega t)\hat{z}$。
  利用和差化积公式相加：
  $$
  \vec{E}(x, t) = \vec{E}_1 + \vec{E}_2 = 2E_0 \cos(kx)\cos(\omega t)\,\hat{y}
  $$
  $$
  \vec{B}(x, t) = \vec{B}_1 + \vec{B}_2 = \frac{2E_0}{c}\sin(kx)\sin(\omega t)\,\hat{z}
  $$
  - **电场波节（$\vec{E} \equiv \vec{0}$）**：令 $\cos(kx) = 0 \implies x = \left(n + \dfrac{1}{2}\right)\dfrac{\pi}{k} = \left(n + \dfrac{1}{2}\right)\dfrac{\lambda}{2} \quad (n \in \mathbb{Z})$；
  - **磁场波节（$\vec{B} \equiv \vec{0}$）**：令 $\sin(kx) = 0 \implies x = \dfrac{n\pi}{k} = n\dfrac{\lambda}{2} \quad (n \in \mathbb{Z})$（注意电场的波节恰为磁场的波腹，反之亦然！）；
  - **时间相位差**：$|\vec{E}| \propto |\cos(\omega t)|$ 在 $\omega t = m\pi$ 时达到最大，而 $|\vec{B}| \propto |\sin(\omega t)|$ 在 $\omega t = \left(m + \frac{1}{2}\right)\pi$ 时达到最大，故从 $\vec{E}$ 最大到下一个 $\vec{B}$ 最大的间隔时间为 $\Delta t = \dfrac{\pi}{2\omega} = \dfrac{T}{4}$。
- **(b) 驻波的坡印廷矢量与局域能量守恒验证**：
  $$
  \vec{S}(x, t) = \frac{1}{\mu_0}\vec{E} \times \vec{B} = \frac{4E_0^2}{\mu_0 c}\sin(kx)\cos(kx)\sin(\omega t)\cos(\omega t)\,\hat{x} = \frac{E_0^2}{\mu_0 c}\sin(2kx)\sin(2\omega t)\,\hat{x}
  $$
  在一个周期内对时间求平均，因 $\langle\sin(2\omega t)\rangle = 0$，故**驻波在任何位置处的平均能流均为零（$\langle\vec{S}\rangle = \vec{0}$）**（能量仅在相邻的电场波腹与磁场波腹之间来回振荡吞吐，不向远处净传输）。
  验证连续性方程：
  $$
  \nabla \cdot \vec{S} = \frac{\partial S_x}{\partial x} = \frac{2k E_0^2}{\mu_0 c}\cos(2kx)\sin(2\omega t) = 2\epsilon_0 \omega E_0^2 \cos(2kx)\sin(2\omega t)
  $$
  而总能量密度为 $u = \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0}B^2 = 2\epsilon_0 E_0^2\left[\cos^2(kx)\cos^2(\omega t) + \sin^2(kx)\sin^2(\omega t)\right]$，求时间偏导数：
  $$
  \frac{\partial u}{\partial t} = 2\epsilon_0 \omega E_0^2 \sin(2\omega t)\left[-\cos^2(kx) + \sin^2(kx)\right] = -2\epsilon_0 \omega E_0^2 \cos(2kx)\sin(2\omega t) = -\nabla \cdot \vec{S}
  $$
  故 $\nabla\cdot\vec{S} + \frac{\partial u}{\partial t} = 0$ 恒成立。
- **(c) 任意假想波速 $v = \omega/k$ 的检验**：
  若将 $c$ 换为 $v = \omega/k$，则 $E_y = 2E_0\cos(kx)\cos(\omega t), \ B_z = \frac{2E_0}{v}\sin(kx)\sin(\omega t)$。
  - 检验法拉第定律：$(\nabla\times\vec{E})_z = \frac{\partial E_y}{\partial x} = -2kE_0\sin(kx)\cos(\omega t)$，而 $-\frac{\partial B_z}{\partial t} = -\frac{2\omega E_0}{v}\sin(kx)\cos(\omega t)$。由于 $\frac{\omega}{v} = k$，**对任意 $v$ 法拉第定律均自动满足**！
  - 检验安培-麦克斯韦定律：$(\nabla\times\vec{B})_y = -\frac{\partial B_z}{\partial x} = -\frac{2kE_0}{v}\cos(kx)\sin(\omega t)$，而右侧 $\mu_0\epsilon_0\frac{\partial E_y}{\partial t} = -2\mu_0\epsilon_0 \omega E_0\cos(kx)\sin(\omega t)$。要使两者相等，必须有 $\frac{k}{v} = \mu_0\epsilon_0\omega = \mu_0\epsilon_0 k v \implies v^2 = \frac{1}{\mu_0\epsilon_0}$，即**仅当 $v = \dfrac{1}{\sqrt{\mu_0\epsilon_0}} = c$ 时安培-麦克斯韦定律才成立**！

---

**2. 无限大交变面电流薄板向两侧辐射平面电磁波（Exercise 14.8，经典天线辐射原型）**：

- **(a) 跨接 $x = 0$ 薄板的边界条件推导**：
  1. 取位于 $xy$ 平面内、跨接 $x = 0$ 的扁矩形回路（两条平行于 $y$ 轴的长边位于 $x = 0^\pm$，长为 $l$；法向沿 $+\hat{z}$）。当矩形宽度 $\Delta x \to 0$ 时，穿过矩形的磁通量 $\Phi_B \to 0$，由法拉第定律 $\oint \vec{E}\cdot d\vec{l} = \left[E_y(0^+, t) - E_y(0^-, t)\right]l = -\frac{d\Phi_B}{dt} = 0$，证得 **$E_y$ 在 $x = 0$ 处连续**：$E_y(0^+, t) = E_y(0^-, t)$。
  2. 取位于 $xz$ 平面内、跨接 $x = 0$ 的扁矩形安培环路（两条平行于 $z$ 轴的长边位于 $x = 0^\pm$，长为 $l$；积分绕行方向使右手拇指指向 $+\hat{y}$）。当宽度 $\Delta x \to 0$ 时，电通量变化率项为零，环路包围的净传导电流为 $I_{\text{enc}} = K_y(t)l = K_0 l\cos(\omega t)$。由右手法则（在 $x = 0^+$ 边沿 $-\hat{z}$ 走，在 $x = 0^-$ 边沿 $+\hat{z}$ 走）：
     $$
     \oint \vec{B}\cdot d\vec{l} = \left[-B_z(0^+, t) + B_z(0^-, t)\right]l = \mu_0 K_0 l \cos(\omega t) \implies B_z(0^+, t) - B_z(0^-, t) = -\mu_0 K_0 \cos(\omega t)
     $$
- **(b) 两侧向外传播的辐射平面波 $\vec{E}(x, t)$ 与 $\vec{B}(x, t)$**：
  薄板向右侧（$x > 0$，波矢 $+\hat{x}$）和左侧（$x < 0$，波矢 $-\hat{x}$）对称辐射外行平面波（含延迟相位 $\omega(t - |x|/c) = \omega t - k|x|$）。
  由偶对称性知两侧 $E_y$ 相等；对向外辐射的波，在 $x > 0$ 区有 $B_z = +\frac{1}{c}E_y$，在 $x < 0$ 区有 $B_z = -\frac{1}{c}E_y$（故 $B_z(0^+, t) = -B_z(0^-, t)$）。
  代入 (a) 的磁场跃变条件：$2B_z(0^+, t) = -\mu_0 K_0\cos(\omega t) \implies B_z(0^+, t) = -\frac{1}{2}\mu_0 K_0\cos(\omega t)$，进而 $E_y(0, t) = c B_z(0^+, t) = -\frac{1}{2}\mu_0 c K_0\cos(\omega t)$。
  将 $t$ 替换为推迟时间 $t - \frac{|x|}{c}$，即得两侧全空间的辐射电磁场：
  $$
  \vec{E}(x, t) = -\frac{1}{2}\mu_0 c K_0 \cos\left[\omega\left(t - \frac{|x|}{c}\right)\right]\hat{y} \qquad (\forall x \neq 0)
  $$
  $$
  \vec{B}(x, t) = -\frac{1}{2}\mu_0 K_0 \operatorname{sgn}(x) \cos\left[\omega\left(t - \frac{|x|}{c}\right)\right]\hat{z} = \begin{cases}
  -\dfrac{1}{2}\mu_0 K_0 \cos\left[\omega\left(t - \dfrac{x}{c}\right)\right]\hat{z}, & x > 0, \\[8pt]
  +\dfrac{1}{2}\mu_0 K_0 \cos\left[\omega\left(t + \dfrac{x}{c}\right)\right]\hat{z}, & x < 0.
  \end{cases}
  $$
- **(c) 辐射功率与外源驱动功率守恒验证**：
  单侧辐射平面波的电场振幅为 $E_0 = \frac{1}{2}\mu_0 c K_0$，磁场振幅为 $B_0 = \frac{1}{2}\mu_0 K_0$。因此每侧单位面积带走的时间平均辐射功率（波强）为：
  $$
  \overline{S}_{\text{each side}} = \frac{E_0 B_0}{2\mu_0} = \frac{1}{8}\mu_0 c K_0^2
  $$
  两侧合计辐射的总平均功率密度为 $2\overline{S}_{\text{each side}} = \dfrac{1}{4}\mu_0 c K_0^2$。
  另一方面，在 $x = 0$ 平面上，薄板自身产生的辐射电场 $E_y(0, t) = -\frac{1}{2}\mu_0 c K_0\cos(\omega t)$ 总是反抗面电流 $K_y(t) = K_0\cos(\omega t)$（这就是**辐射阻尼反作用力**！）。外源为单位面积面电流克服该电场做功的平均功率为：
  $$
  P_{\text{source}} = \big\langle -\vec{K}(t) \cdot \vec{E}(0, t) \big\rangle = \left\langle \frac{1}{2}\mu_0 c K_0^2 \cos^2(\omega t) \right\rangle = \frac{1}{4}\mu_0 c K_0^2 = 2\overline{S}_{\text{each side}}
  $$
  外源消耗的功率一分不少地转化为了向两侧空间辐射出去的电磁波能量！

---

**3. 镜面全反射太阳帆（Solar Sail）的斜入射光压力学与星际航行（Exercise 14.9）**：

- **(a) 斜入射角 $\theta$ 下的平均光压力大小与方向**：
  设入射光束沿单位矢量 $\hat{k}_{\text{in}}$ 方向传播，太阳帆受光面的内法线（顺着受力方向背离光源一侧）单位矢量为 $\hat{n}$，两者夹角为 $\theta \ (0 \le \theta < \pi/2)$。
  1. **有效截光面积**：面积为 $A$ 的帆在垂直于入射光束平面上的投影截面积为 $A_\perp = A\cos\theta$，故单位时间内拦截的入射光功率为 $P_{\text{int}} = I A\cos\theta$；
  2. **动量传递方向与大小**：入射光束输入动量流率为 $\vec{\Pi}_{\text{in}} = \frac{P_{\text{int}}}{c}\hat{k}_{\text{in}}$；根据镜面反射定律（Specular reflection），反射光束方向为 $\hat{k}_{\text{ref}} = \hat{k}_{\text{in}} - 2(\hat{k}_{\text{in}}\cdot\hat{n})\hat{n} = \hat{k}_{\text{in}} - 2\cos\theta\,\hat{n}$，带走动量流率为 $\vec{\Pi}_{\text{ref}} = \frac{P_{\text{int}}}{c}\hat{k}_{\text{ref}}$。
  由动量守恒，光束对太阳帆施加的时间平均作用力为：
  $$
  \vec{F} = \vec{\Pi}_{\text{in}} - \vec{\Pi}_{\text{ref}} = \frac{I A\cos\theta}{c}\left(\hat{k}_{\text{in}} - \hat{k}_{\text{ref}}\right) = \frac{2 I A \cos^2\theta}{c}\hat{n}
  $$
  即光压力**方向严格垂直于帆面（沿法向 $\hat{n}$）**，大小为 $F = \dfrac{2IA\cos^2\theta}{c}$。当 $\theta = 0$（正入射）时，$F/A = \frac{2I}{c}$，与正文完全反射光压公式一致。
- **(b) 太阳光压平衡太阳万有引力的临界比面质量 $m/A$**：
  在距太阳中心距离为 $r$ 处，太阳辐射强度为 $I(r) = \frac{L_\odot}{4\pi r^2}$。当正对太阳（$\theta = 0$）时，向外的光压力为 $F_{\text{rad}} = \frac{2 I(r) A}{c} = \frac{L_\odot A}{2\pi c r^2}$；太阳对总质量 $m$ 的万有引力为 $F_{\text{grav}} = \frac{G M_\odot m}{r^2}$。
  注意到**光压力与万有引力均严格按 $1/r^2$ 衰减**！令二力平衡，距离 $r^2$ 直接消去：
  $$
  \frac{L_\odot A}{2\pi c r^2} = \frac{G M_\odot m}{r^2} \implies \frac{m}{A} = \frac{L_\odot}{2\pi c G M_\odot} \qquad (\text{与距太阳的距离 } r \text{ 完全无关！})
  $$
  代入数值 $L_\odot = 3.83 \times 10^{26}\text{ W}, \ M_\odot = 1.99 \times 10^{30}\text{ kg}, \ G = 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2, \ c = 3.00 \times 10^8\text{ m/s}$：
  $$
  \frac{m}{A} = \frac{3.83 \times 10^{26}}{2\pi \times (3.00 \times 10^8) \times (6.67 \times 10^{-11}) \times (1.99 \times 10^{30})} \approx 1.53 \times 10^{-3}\text{ kg/m}^2 = 1.53\text{ g/m}^2
  $$
- **(c) 垂直于入射光束的横向升力分量 $F_\perp$ 及最佳倾角 $\theta$**：
  由于总力 $\vec{F}$ 沿法线 $\hat{n}$（与光束夹角为 $\theta$），其垂直于光束方向的横向分量大小为：
  $$
  F_\perp(\theta) = F \sin\theta = \frac{2IA}{c}\cos^2\theta \sin\theta
  $$
  对 $\theta$ 求导令其为零：$\frac{d}{d\theta}(\cos^2\theta\sin\theta) = \cos\theta(-2\sin^2\theta + \cos^2\theta) = 0 \implies \tan^2\theta = \frac{1}{2}$。
  因此当倾角为：
  $$
  \theta = \arctan\left(\frac{1}{\sqrt{2}}\right) = \arcsin\left(\frac{1}{\sqrt{3}}\right) \approx 35.26^\circ
  $$
  时，横向控制力达到最大值 $F_{\perp,\max} = \dfrac{4}{3\sqrt{3}}\dfrac{IA}{c} \approx 0.770\,\dfrac{IA}{c}$（太阳帆正是利用这一横向分力来改变轨道角动量，实现星际变轨航行的！）。

</details>