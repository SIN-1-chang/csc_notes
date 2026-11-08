# Chapter 13: Alternating-Current Circuits（交流电路）

!!! abstract
    General Physics II (Electromagnetism) | 第十三章课堂与讲义笔记
    
    参考：
    
    - Lecture 13: *Alternating-Current Circuits* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 13: *Alternating-Current Circuits*
    - Halliday, Resnick & Krane, *Physics*, Chapter 37

## 1 LC 电磁振荡与电-力类比 (Electromagnetic LC Oscillations)

### 1.1 电路中的三个基本特征时间尺度

至此我们已经集齐了电磁学中的三大基本无源元件：**电阻器**（Resistor, $R$）、**电容器**（Capacitor, $C$）与**电感器**（Inductor, $L$）。由它们两两组合可构成三个具有时间量纲的特征时间常数（Characteristic time scales）：

$$
\tau_C = RC, \qquad \tau_L = \frac{L}{R}, \qquad \tau_{LC} = \sqrt{LC}
$$

- **耗散衰减时间（$\tau_C$ 与 $\tau_L$）**：在 RC 和 RL 电路中，由于包含耗能元件电阻 $R$，电荷与电流随时间作单调的指数增长或指数衰减，经过几个 $\tau_C$ 或 $\tau_L$ 后暂态过程即告终结。
- **无损振荡周期尺度（$\tau_{LC}$）**：理想 LC 电路不含电阻，没有任何能量耗散。电容器储存电场能（$\propto q^2$），电感器储存磁场能（$\propto i^2 = \dot{q}^2$）。因此 $\tau_{LC} = \sqrt{LC}$ 不再代表衰减时间，而是决定了能量在电场与磁场之间周期性往复转换的**振荡时间尺度**，对应的固有振荡周期为 $T = 2\pi\tau_{LC} = 2\pi\sqrt{LC}$，**固有角频率**（Natural angular frequency）为：
  $$
  \omega_0 = \frac{1}{\tau_{LC}} = \frac{1}{\sqrt{LC}}
  $$

### 1.2 电-力类比 (The Electrical-Mechanical Analogy)

理想 LC 电路中的**电磁振荡**（Electromagnetic oscillations）与经典力学中的**弹簧-物块简谐振子**（Block-spring harmonic oscillator）在数学形式与物理内涵上一一对应：

| 力学弹簧振子系统（Block-Spring System） | 物理量 / 方程形式 | 电学 LC 振荡系统（LC Oscillator） | 物理量 / 方程形式 |
| :--- | :---: | :--- | :---: |
| **广义坐标：位移**（Displacement） | $x$ | **极板电荷量**（Charge） | $q$ |
| **广义速度：运动速度**（Velocity） | $v = \dfrac{dx}{dt}$ | **回路电流**（Current） | $i = \dfrac{dq}{dt}$ |
| **惯性元件：物块质量**（Mass） | $m$ | **电感器电感**（Inductance） | $L$ |
| **恢复元件：弹簧劲度系数**（Spring constant） | $k$ | **电容器电容的倒数**（Inverse capacitance） | $\dfrac{1}{C}$ |
| **动能**（Kinetic Energy） | $K = \dfrac{1}{2}mv^2$ | **电感磁场能**（Magnetic Energy） | $U_B = \dfrac{1}{2}Li^2$ |
| **弹性势能**（Potential Energy） | $U_p = \dfrac{1}{2}kx^2$ | **电容电场能**（Electrical Energy） | $U_E = \dfrac{1}{2}\left(\dfrac{1}{C}\right)q^2$ |
| **简谐运动微分方程** | $m\dfrac{d^2x}{dt^2} + kx = 0$ | **LC 振荡微分方程** | $L\dfrac{d^2q}{dt^2} + \dfrac{1}{C}q = 0$ |
| **固有角频率**（Natural Angular Frequency） | $\omega_0 = \sqrt{\dfrac{k}{m}}$ | **固有角频率**（Natural Angular Frequency） | $\omega_0 = \dfrac{1}{\sqrt{LC}}$ |

### 1.3 LC 振荡的定量推导与能量守恒分析

设任意时刻 $t$ 电容器极板电荷量为 $q(t)$，回路电流为 $i(t) = \frac{dq}{dt}$。在无电阻、无外电源的理想 LC 回路中，系统的总电磁能 $U$ 等于电感磁能 $U_B$ 与电容电能 $U_E$ 之和，且保持守恒（$\frac{dU}{dt} = 0$）：

$$
U = U_B + U_E = \frac{1}{2}Li^2 + \frac{q^2}{2C} = \text{const} \implies \frac{dU}{dt} = Li\frac{di}{dt} + \frac{q}{C}\frac{dq}{dt} = 0
$$

代入 $i = \frac{dq}{dt}$ 与 $\frac{di}{dt} = \frac{d^2q}{dt^2}$ 并消去公因子 $i$，即得到控制 LC 自由振荡的二阶常系数齐次线性微分方程：

$$
L\frac{d^2q}{dt^2} + \frac{1}{C}q = 0 \iff \frac{d^2q}{dt^2} + \omega_0^2 q = 0 \qquad \left(\omega_0 = \frac{1}{\sqrt{LC}}\right)
$$

**1. 电荷与电流的通解及相位关系**

方程的通解为正弦/余弦简谐函数（其中电荷振幅 $Q$ 与初相 $\phi$ 由初始条件 $q(0) = Q\cos\phi$ 及 $i(0) = -\omega_0 Q\sin\phi$ 唯一确定）：

$$
q(t) = Q\cos(\omega_0 t + \phi)
$$

$$
i(t) = \frac{dq}{dt} = -\omega_0 Q\sin(\omega_0 t + \phi) = -I\sin(\omega_0 t + \phi) = I\cos\left(\omega_0 t + \phi + \frac{\pi}{2}\right)
$$

其中电流振幅为 $I = \omega_0 Q = \frac{Q}{\sqrt{LC}}$，且**电流 $i(t)$ 在相位上超前于极板电荷 $q(t)$（及电容端电压 $v_C = q/C$）$\dfrac{\pi}{2}$（即 $90^\circ$）**。

**2. 电场能与磁场能的交替振荡**

将 $q(t)$ 与 $i(t)$ 代入电场能与磁场能表达式（利用 $LI^2 = L\omega_0^2 Q^2 = \frac{Q^2}{C}$）：

$$
U_E(t) = \frac{q^2(t)}{2C} = \frac{Q^2}{2C}\cos^2(\omega_0 t + \phi), \qquad U_B(t) = \frac{1}{2}Li^2(t) = \frac{1}{2}L\omega_0^2 Q^2\sin^2(\omega_0 t + \phi) = \frac{Q^2}{2C}\sin^2(\omega_0 t + \phi)
$$

- $U_E(t)$ 与 $U_B(t)$ 的最大值相等，均为总能量 $U_{\max} = \dfrac{Q^2}{2C} = \dfrac{1}{2}LI^2$；
- 在任意瞬时，二者之和恒为常数：$U_E(t) + U_B(t) = \dfrac{Q^2}{2C}$；
- 当电容充满电（$|q| = Q, \ i = 0$）时，$U_E$ 最大而 $U_B = 0$；经过四分之一周期（$T/4$），电容放电完毕（$q = 0, \ |i| = I$），能量全部转化为电感磁能（$U_B$ 最大而 $U_E = 0$）。

---

## 2 RLC 电路中的阻尼振荡 (Damped Oscillations in an RLC Circuit)

### 2.1 阻尼振荡微分方程与复数形式解法 (Complex Formalism)

在实际电路中总是存在电阻 $R$，它将电磁场的能量不可逆地转化为焦耳热耗散掉（类比于力学弹簧振子受到的摩擦阻尼力）：

$$
\frac{dU}{dt} = \frac{d}{dt}\left(\frac{1}{2}Li^2 + \frac{q^2}{2C}\right) = Li\frac{di}{dt} + \frac{q}{C}\frac{dq}{dt} = -i^2 R
$$

代入 $i = \frac{dq}{dt}$ 并整理，得到 **RLC 串联电路的阻尼振荡微分方程**：

$$
L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{1}{C}q = 0
$$

**复数指数解法（The Complex Formalism）**：
注意到一阶电路的解为指数衰减 $e^{-t/\tau}$，而无阻尼 LC 电路的解为复指数实部 $\mathfrak{R}[Qe^{i\omega_0 t}e^{i\phi}]$。因此对于一般阻尼振荡，我们构造统一的复指数试探解：

$$
q(t) = \mathfrak{R}\left[\tilde{Q} e^{i\tilde{\omega}t}\right]
$$

其中 $\tilde{Q} = Qe^{i\phi}$ 为**复振幅**（Complex amplitude），$\tilde{\omega} = \omega + \frac{i}{\tau_d}$ 为**复角频率**（Complex frequency）。将其代入微分方程并消去非零因子 $\tilde{Q}e^{i\tilde{\omega}t}$，二阶微分方程直接转化为关于 $\tilde{\omega}$ 的一元二次代数方程：

$$
-L\tilde{\omega}^2 + i\tilde{\omega}R + \frac{1}{C} = 0 \implies \tilde{\omega}^2 - i\frac{R}{L}\tilde{\omega} - \omega_0^2 = 0
$$

由求根公式立即解得：

$$
\tilde{\omega} = i\frac{R}{2L} \pm \sqrt{\omega_0^2 - \left(\frac{R}{2L}\right)^2} = \frac{i}{\tau_d} \pm \omega
$$

其中定义了**阻尼时间常数**（Damping time constant）$\tau_d$ 与**阻尼振荡角频率** $\omega$：

$$
\tau_d \equiv \frac{2L}{R} = 2\tau_L \iff \frac{1}{\tau_d} = \frac{R}{2L}, \qquad \omega \equiv \sqrt{\omega_0^2 - \left(\frac{1}{\tau_d}\right)^2} = \sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}
$$

（在欠阻尼情形下，复频率在复平面上构成直角三角形：实部为 $\omega$，虚部为 $1/\tau_d$，斜边模长恰为固有频率 $|\tilde{\omega}| = \sqrt{\omega^2 + (1/\tau_d)^2} = \omega_0$）。

### 2.2 三种阻尼状态的分类与响应特征

根据阻尼率 $\frac{1}{\tau_d} = \frac{R}{2L}$ 与固有角频率 $\omega_0 = \frac{1}{\sqrt{LC}}$ 的相对大小，RLC 电路呈现三种截然不同的动力学行为：

| 阻尼状态 | 频率与电阻判据 | $\omega$ 的性质 | 电荷时间演化通解 $q(t)$ | 物理图像与工程应用 |
| :--- | :--- | :---: | :--- | :--- |
| **1. 欠阻尼**<br>（Underdamped） | $\dfrac{1}{\tau_d} < \omega_0$<br>$\iff R < 2\sqrt{\dfrac{L}{C}}$ | 正实数<br>（$0 < \omega < \omega_0$） | $$q(t) = Q e^{-t/\tau_d}\cos(\omega t + \phi)$$ | 电荷作准周期振荡，振幅按包络线 $e^{-t/\tau_d}$ 指数衰减（电磁能以 $\propto e^{-2t/\tau_d} = e^{-Rt/L}$ 衰减） |
| **2. 过阻尼**<br>（Overdamped） | $\dfrac{1}{\tau_d} > \omega_0$<br>$\iff R > 2\sqrt{\dfrac{L}{C}}$ | 纯虚数<br>（无振荡） | $$q(t) = Q_1 e^{-t/\tau_1} + Q_2 e^{-t/\tau_2}$$<br>$\dfrac{1}{\tau_{1,2}} = \dfrac{R}{2L} \pm \sqrt{\dfrac{R^2}{4L^2} - \dfrac{1}{LC}}$ | 阻力过大，系统不发生任何振荡，由快慢两个纯指数衰减项叠加缓慢回到平衡位置 |
| **3. 临界阻尼**<br>（Critically Damped） | $\dfrac{1}{\tau_d} = \omega_0$<br>$\iff R = 2\sqrt{\dfrac{L}{C}}$ | $\omega = 0$<br>（二重重根） | $$q(t) = (Q_1 + Q_2 t)e^{-t/\tau_d}$$ | 两个特征根合并，第二线性无关解出现因子 $t$；**在不发生超调振荡的前提下，以最快速度回归平衡态**（仪表指针、减震器理想设计点） |

---

## 3 交流电路、复阻抗与受迫振荡谐振 (AC Circuits, Complex Impedance & Resonance)

### 3.1 交流发电机与受迫振荡 (AC Generator and Forced Oscillations)

为了补偿电阻 $R$ 的热耗散使振荡持续下去，需接入周期性提供能量的外加交变电源。**交流发电机**（AC generator）通过使 $N$ 匝面积为 $A$ 的线圈在匀强磁场 $B$ 中以恒定角速度 $\omega_d$ 旋转，并经由**滑环**（Slip rings，区别于直流电机的开口换向器）和金属电刷引出正弦交变电动势：

$$
\mathcal{E}(t) = \mathcal{E}_m \cos(\omega_d t), \qquad \text{其中峰值电动势 } \mathcal{E}_m = NBA\omega_d
$$

（我国民用市电频率为 $f = 50\text{ Hz}$，每秒电流方向反转 $100$ 次，驱动角频率 $\omega_d = 2\pi f = 100\pi\text{ rad/s}$）。

- **自由振荡（Free oscillations）vs. 受迫振荡（Forced / Driven oscillations）**：无外源时，电路按自身固有频率 $\omega_0 = 1/\sqrt{LC}$ 自由振荡；接入交流电源后，具有固有频率的暂态项在几个阻尼时间 $\tau_d = 2L/R$ 内衰减殆尽，电路进入**正弦稳态**（Steady state），此时电荷、电压与电流全部以**外源的驱动角频率 $\omega_d$** 作受迫振荡：
  $$
  i(t) = I\cos(\omega_d t - \phi) \qquad (\phi \text{ 定义为电流滞后于驱动电动势的相位角})
  $$
- **峰值（Peak）与有效值 / 均方根值（Root-Mean-Square, RMS）**：
  本章公式中的 $\mathcal{E}_m, |\tilde{V}|, I$ 默认代表**峰值振幅**。工程与市电额定值（如 $220\text{ V}$）通常使用**有效值**（RMS value），定义为正弦量平方在一个周期内平均值的平方根：
  $$
  V_{\text{rms}} = \sqrt{\langle v^2(t) \rangle} = \frac{V_{\text{peak}}}{\sqrt{2}}, \qquad I_{\text{rms}} = \frac{I_{\text{peak}}}{\sqrt{2}}, \qquad P_{\text{avg}} = \langle i^2(t)R \rangle = \frac{1}{2}I_{\text{peak}}^2 R = I_{\text{rms}}^2 R
  $$

### 3.2 复阻抗方法 (The Complex Impedance Method)

在稳态交流电路中，将任意元件两端的电压（电流流入端电势减去流出端电势）与流过元件的电流表示为复指数的实部：

$$
v(t) = \mathfrak{R}\left(\tilde{V} e^{i\omega_d t}\right), \qquad i(t) = \mathfrak{R}\left(\tilde{I} e^{i\omega_d t}\right)
$$

由于对时间求导 $\frac{d}{dt}\left(e^{i\omega_d t}\right) = (i\omega_d)e^{i\omega_d t}$ 等效于直接乘以代数因子 **$i\omega_d$**（积分 $\int dt$ 等效于除以 $i\omega_d$），微积分方程瞬间简化为复代数方程！定义元件的**复阻抗**（Complex Impedance，记作 $\tilde{Z}$）为复电压振幅与复电流振幅之比：

$$
\tilde{Z} \equiv \frac{\tilde{V}}{\tilde{I}} = Z e^{i\phi}
$$

其中模长 $Z = |\tilde{Z}| = \frac{|\tilde{V}|}{|\tilde{I}|}$ 称为**阻抗大小**（Impedance magnitude，单位为欧姆 $\Omega$），辐角 $\phi$ 即为**电流滞后于电压的相位角**（Phase angle by which current lags voltage）。

三大基本无源元件的时域关系、复阻抗与相位特征汇总如下表：

| 电路元件 | 时域电压-电流关系 | 复阻抗 $\tilde{Z} = \tilde{V}/\tilde{I}$ | 阻抗模长（电抗 Reactance） | 电流与电压的相位关系（$\phi$ 为电流滞后角） |
| :--- | :---: | :---: | :---: | :--- |
| **纯电阻 $R$**<br>（Resistive Load） | $v_R = R i_R$ | $\tilde{Z}_R = R$ | $Z_R = R$ | **同相（In phase，$\phi = 0$）** |
| **纯电感 $L$**<br>（Inductive Load） | $v_L = L\dfrac{di_L}{dt}$ | $\tilde{Z}_L = i\omega_d L = \omega_d L e^{+i\pi/2}$ | 感抗 $X_L = \omega_d L$ | **电流滞后电压 $\dfrac{\pi}{2}$（$\phi = +\dfrac{\pi}{2}$，“感滞”）** |
| **纯电容 $C$**<br>（Capacitive Load） | $i_C = C\dfrac{dv_C}{dt}$ | $\tilde{Z}_C = \dfrac{1}{i\omega_d C} = -i\dfrac{1}{\omega_d C} = \dfrac{1}{\omega_d C}e^{-i\pi/2}$ | 容抗 $X_C = \dfrac{1}{\omega_d C}$ | **电流超前电压 $\dfrac{\pi}{2}$（$\phi = -\dfrac{\pi}{2}$，“容超”）** |

**复阻抗的串并联法则（与直流电阻完全同构）**：
由于基尔霍夫回路定律（KVL）与节点定律（KCL）对复振幅 $\tilde{V}, \tilde{I}$ 依然严格成立，复阻抗的串联与并联直接套用电阻公式：

$$
\text{串联（Series）：}\tilde{Z}_{\text{eq}} = \sum_k \tilde{Z}_k, \qquad \text{并联（Parallel）：}\frac{1}{\tilde{Z}_{\text{eq}}} = \sum_k \frac{1}{\tilde{Z}_k}
$$

### 3.3 串联 RLC 电路与谐振现象 (Series RLC Circuit and Resonance)

**1. 串联 RLC 电路的总复阻抗**

当电阻 $R$、电感 $L$ 与电容 $C$ 串联接入驱动频率为 $\omega_d$ 的交流电路时，总复阻抗为三者之和：

$$
\tilde{Z} = \tilde{Z}_R + \tilde{Z}_L + \tilde{Z}_C = R + i\left(\omega_d L - \frac{1}{\omega_d C}\right) = Z e^{i\phi}
$$

由复数的实部 $Z\cos\phi = R$ 与虚部 $Z\sin\phi = \omega_d L - \frac{1}{\omega_d C}$，立即得到**串联 RLC 电路的总阻抗大小 $Z$、相位角 $\phi$ 及稳态电流振幅 $I$**：

$$
Z = \sqrt{R^2 + \left(\omega_d L - \frac{1}{\omega_d C}\right)^2}, \qquad \tan\phi = \frac{\omega_d L - \dfrac{1}{\omega_d C}}{R}, \qquad I = \frac{\mathcal{E}_m}{Z} = \frac{\mathcal{E}_m}{\sqrt{R^2 + \left(\omega_d L - \dfrac{1}{\omega_d C}\right)^2}}
$$

**2. 串联谐振（Series Resonance）与选频特性**

当外加交流电源的驱动角频率 $\omega_d$ 恰好等于电路的固有角频率 $\omega_0$ 时，电路发生**谐振**（Resonance）：

$$
\omega_d = \omega_0 = \frac{1}{\sqrt{LC}}
$$

在谐振状态下，电路同时呈现以下四个标志性特征：

1. **感抗与容抗完全抵消**：$\omega_0 L = \dfrac{1}{\omega_0 C}$（电感与电容上的瞬时电压等大反向，$v_L(t) + v_C(t) \equiv 0$）；
2. **总阻抗达到最小值**：虚部电抗清零，总阻抗简化为纯电阻 $Z_{\min} = R$；
3. **电流振幅达到最大值**：$I_{\max} = \dfrac{\mathcal{E}_m}{R}$（在固定 $L, C$ 下，电阻 $R$ 越小，谐振峰越高越尖锐，选频调谐 Selectivity 越灵敏）；
4. **电流与驱动电动势完全同相**：$\tan\phi = 0 \implies \phi = 0$。

| 驱动频率区间 | 电抗主导关系 | 相位角 $\phi$ 符号 | 电流与电动势相位关系 | 电路整体性质 |
| :--- | :--- | :---: | :--- | :--- |
| **低频区（$\omega_d < \omega_0$）** | 容抗大于感抗（$\dfrac{1}{\omega_d C} > \omega_d L$） | $\phi < 0$ | 电流 **超前（Leads）** 电动势 | **容性（Capacitive）** |
| **谐振点（$\omega_d = \omega_0$）** | 感抗等于容抗（$\omega_0 L = \dfrac{1}{\omega_0 C}$） | $\phi = 0$ | 电流与电动势 **同相（In phase）** | **纯阻性（Purely resistive，$Z_{\min}=R$）** |
| **高频区（$\omega_d > \omega_0$）** | 感抗大于容抗（$\omega_d L > \dfrac{1}{\omega_d C}$） | $\phi > 0$ | 电流 **滞后（Lags）** 电动势 | **感性（Inductive）** |

!!! tip "对偶模型对比：理想并联 LC 回路的反谐振（Parallel LC Tank Circuit）"
    若将理想电感 $L$ 与电容 $C$ **并联**，其总复导纳与总复阻抗为：
    $$
    \frac{1}{\tilde{Z}} = \frac{1}{i\omega_d L} + i\omega_d C = i\left(\omega_d C - \frac{1}{\omega_d L}\right) \implies \tilde{Z} = \frac{i\omega_d L}{1 - \omega_d^2 LC}
    $$
    当驱动频率达到 $\omega_d = \omega_0 = \frac{1}{\sqrt{LC}}$ 时，分母为零，**并联总阻抗趋于无穷大（$|\tilde{Z}| \to \infty$，对外电路相当于开路断路）**！这是因为电感支路与电容支路的电流振幅相等但相位相反（相差 $\pi$），干路总电流完全抵消为零，能量在并联 LC 内部循环吞吐（若计入电感线圈内阻 $r$，详见 Exercise 13.8）。

---

## 4 Chapter 13 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 13.1, 13.2 & 13.3: Series RL, Mixed RLC Network & LC Voltage Divider（串联 RL、混联 RLC 电流与 LC 分压滤波器）</summary>

**Problem Statement:**
- **Ex 13.1**: Consider a series RL circuit with $R = 300\ \Omega$ and $L = 0.9\text{ H}$, driven in the steady state by an emf of fixed magnitude $50\text{ V}$ and fixed angular frequency of $1000\text{ rad/s}$. (a) Calculate the impedance $Z$ of the circuit. (b) Calculate the amplitude of the current. (c) Calculate the angle $\phi$ by which the current lags the emf.
- **Ex 13.2**: In the steady state, calculate the amplitude of the current through the resistor in the RLC circuit of `Figure 13.2` ($\mathcal{E}_m = 150\text{ V}$, $f = 60\text{ Hz}$; series branch has $C = 3\ \mu\text{F}$ and $L_1 = 0.2\text{ H}$; parallel branch has $L_2 = 1\text{ H}$ and $R = 100\ \Omega$).
- **Ex 13.3**: Consider the circuit of `Figure 13.3` in the steady state ($f = 60\text{ Hz}$, input voltage $U_1$, parallel $10\ \mu\text{F}$ capacitor, series inductor $L$, and output parallel $10\ \mu\text{F}$ capacitor with open terminals $U_2$). If the amplitude of the output voltage $U_2$ is to be $1/10$ of the amplitude of the input voltage $U_1$, what is the value of the self-inductance $L$?

---

**中文解析：**

**1. 串联 RL 交流电路的基本稳态计算（Exercise 13.1）**：
已知 $R = 300\ \Omega$，$L = 0.9\text{ H}$，$\mathcal{E}_m = 50\text{ V}$，$\omega_d = 1000\text{ rad/s}$。感抗为 $X_L = \omega_d L = 1000 \times 0.9 = 900\ \Omega$。

- **(a) 总阻抗大小 $Z$**：
  $$
  Z = \sqrt{R^2 + (\omega_d L)^2} = \sqrt{300^2 + 900^2} = 300\sqrt{10}\ \Omega \approx 948.7\ \Omega
  $$
- **(b) 电流振幅 $I$**：
  $$
  I = \frac{\mathcal{E}_m}{Z} = \frac{50}{300\sqrt{10}} = \frac{1}{6\sqrt{10}}\text{ A} \approx 0.0527\text{ A} = 52.7\text{ mA}
  $$
- **(c) 电流滞后于电动势的相位角 $\phi$**：
  $$
  \tan\phi = \frac{\omega_d L}{R} = \frac{900}{300} = 3 \implies \phi = \arctan(3) \approx 1.249\text{ rad} \approx 71.6^\circ
  $$

---

**2. 混联 RLC 网络中流过电阻支路的电流振幅（Exercise 13.2）**：
驱动角频率为 $\omega = 2\pi f = 2\pi \times 60 = 120\pi\text{ rad/s} \approx 376.991\text{ rad/s}$。

1. **计算串联干路复阻抗 $\tilde{Z}_1$**：
   干路包含 $C = 3\times 10^{-6}\text{ F}$ 与 $L_1 = 0.2\text{ H}$，其复阻抗为纯虚数 $\tilde{Z}_1 = i X_1$：
   $$
   X_1 = \omega L_1 - \frac{1}{\omega C} = 120\pi \times 0.2 - \frac{1}{120\pi \times 3 \times 10^{-6}} \approx 75.398 - 884.194 = -808.796\ \Omega
   $$
2. **计算右侧并联支路等效复阻抗 $\tilde{Z}_p$**：
   并联部分由 $L_2 = 1\text{ H}$（感抗 $X_2 = \omega L_2 = 120\pi \approx 376.991\ \Omega$，$\tilde{Z}_{L2} = i X_2$）与电阻 $R = 100\ \Omega$ 组成：
   $$
   \tilde{Z}_p = \frac{R(i X_2)}{R + i X_2}
   $$
3. **计算电阻 $R$ 上的复电压 $\tilde{V}_p$ 与电流振幅 $I_R$**：
   由复阻抗分压公式，并联节点电压为 $\tilde{V}_p = \mathcal{E}_m \frac{\tilde{Z}_p}{\tilde{Z}_1 + \tilde{Z}_p}$，故流过电阻 $R$ 的复电流为：
   $$
   \tilde{I}_R = \frac{\tilde{V}_p}{R} = \frac{\mathcal{E}_m}{R + \tilde{Z}_1\left(1 + \dfrac{R}{i X_2}\right)} = \frac{\mathcal{E}_m}{R\left(1 + \dfrac{X_1}{X_2}\right) + i X_1}
   $$
   代入数值计算分母实部与虚部：$R\left(1 + \frac{X_1}{X_2}\right) = 100\left(1 - \frac{808.796}{376.991}\right) \approx -114.540\ \Omega$，虚部为 $X_1 \approx -808.796\ \Omega$。
   因此电阻电流的振幅为：
   $$
   I_R = |\tilde{I}_R| = \frac{\mathcal{E}_m}{\sqrt{R^2\left(1 + \dfrac{X_1}{X_2}\right)^2 + X_1^2}} = \frac{150}{\sqrt{(-114.540)^2 + (-808.796)^2}} = \frac{150}{816.867} \approx 0.184\text{ A}
   $$

---

**3. Π 型 LC 滤波网络的分压电感求解（Exercise 13.3）**：
观察 `Figure 13.3` 电路：左侧第一个 $10\ \mu\text{F}$ 电容器直接并联在理想电压源 $U_1$ 两端，因此其两端电压恒等于输入电压 $\tilde{U}_1$（不影响右侧支路的分压比）。
右侧支路是由电感 $L$（复阻抗 $\tilde{Z}_L = i\omega L$）和第二个电容器 $C = 10\ \mu\text{F} = 10^{-5}\text{ F}$（复阻抗 $\tilde{Z}_C = \frac{1}{i\omega C}$）组成的串联分压支路，且输出端开路（无负载电流流出）。因此输出复电压 $\tilde{U}_2$ 与输入复电压 $\tilde{U}_1$ 的关系为：

$$
\frac{\tilde{U}_2}{\tilde{U}_1} = \frac{\tilde{Z}_C}{\tilde{Z}_L + \tilde{Z}_C} = \frac{\dfrac{1}{i\omega C}}{i\omega L + \dfrac{1}{i\omega C}} = \frac{1}{1 - \omega^2 LC}
$$

题目要求输出电压振幅是输入电压振幅的 $\frac{1}{10}$：

$$
\left|\frac{\tilde{U}_2}{\tilde{U}_1}\right| = \frac{1}{|1 - \omega^2 LC|} = \frac{1}{10} \implies 1 - \omega^2 LC = \pm 10
$$

由于 $\omega^2 LC > 0$（$L > 0, \ C > 0$），舍去正号解（对应 $\omega^2 LC = -9 < 0$），取负号解 $1 - \omega^2 LC = -10 \implies \omega^2 LC = 11$。
代入 $\omega = 2\pi f = 120\pi\text{ rad/s}$ 与 $C = 10^{-5}\text{ F}$：

$$
L = \frac{11}{\omega^2 C} = \frac{11}{(120\pi)^2 \times 10^{-5}} \approx 7.74\text{ H}
$$

</details>

<details markdown="1">
<summary>Exercise 13.4, 13.5 & 13.6: Coupled RLC Normal Modes, LC Switching Overvoltage & Overdamped Decay（互感耦合简正模、断电转 LC 振荡高压与过阻尼极值分析）</summary>

**Problem Statement:**
- **Ex 13.4**: Two identical RLC circuits ($L, C, R$) are coupled through a mutual inductance $M$ ($0 < M < L$). (a) With capacitor charges $q_1, q_2$, write down the coupled differential equations. (b) Introduce normal coordinates $q_+ \equiv q_1 + q_2$ and $q_- \equiv q_1 - q_2$; show that the differential equations decouple into two independent damped oscillators. (c) Setting $R = 0$, show that the normal mode frequencies are $\omega_+ = \frac{1}{\sqrt{(L+M)C}}$ and $\omega_- = \frac{1}{\sqrt{(L-M)C}}$.
- **Ex 13.5**: An ideal battery $\mathcal{E} > 0$, resistor $r > 0$, and a switch are in series between $A$ and $B$ ($+$ terminal on side $A$). An ideal inductor $L$ and a capacitor $C$ are also connected in parallel between $A$ and $B$. The switch has been closed for a long time and is opened at $t = 0$. Let $i_L$ be the inductor current from $A$ to $B$, and $q$ the charge on the $A$-plate of $C$.
  (a) Just before $t = 0$, find $i_L, q$ and $V_A - V_B$.
  (b) For $t > 0$, find $q(t), i_L(t)$ and $V_A - V_B$. Write $q(t) = Q\cos(\omega_0 t + \phi)$ with $Q > 0$, and give $Q, \omega_0, \phi$.
  (c) Find the largest value of $|V_A - V_B|$ for $t > 0$, the first time it is reached, and which terminal is higher. Evaluate for $\mathcal{E} = 12\text{ V}, r = 6.0\ \Omega, L = 0.20\text{ H}, C = 0.50\ \mu\text{F}$, and check by energy conservation.
- **Ex 13.6**: A capacitor $C$ with initial charge $Q_0 > 0$ is connected at $t = 0$ in series with $R$ and $L$ ($i(0) = 0$). Let $\omega_0 = 1/\sqrt{LC}$.
  (a) Take $R > 2\sqrt{L/C}$. Show that $q(t) = Q_0\frac{a e^{-bt} - b e^{-at}}{a - b}$, and find $a > b > 0$.
  (b) Find the leading forms of $1/a$ and $1/b$ when $R \gg 2\sqrt{L/C}$, and compare $1/b$ with $\tau_d = 2L/R$. Which time sets how long the capacitor takes to discharge?
  (c) Keep $L, C$ fixed and let $R$ vary. Show that the slowest decay rate of the system is largest at $R = 2\sqrt{L/C}$, where it equals $\omega_0$.

---

**中文解析：**

**1. 互感耦合双 RLC 电路的简正模解耦（Exercise 13.4，经典理论模型）**：

- **(a) 耦合微分方程组**：
  利用第十二章的电感矩阵关系及 $i_1 = \frac{dq_1}{dt}, \ i_2 = \frac{dq_2}{dt}$，每个回路的基尔霍夫回路定律给出：
  $$
  \begin{cases}
  L\dfrac{d^2 q_1}{dt^2} + M\dfrac{d^2 q_2}{dt^2} + R\dfrac{dq_1}{dt} + \dfrac{1}{C}q_1 = 0 \\[8pt]
  L\dfrac{d^2 q_2}{dt^2} + M\dfrac{d^2 q_1}{dt^2} + R\dfrac{dq_2}{dt} + \dfrac{1}{C}q_2 = 0
  \end{cases}
  $$
- **(b) 引入简正坐标（Normal coordinates）$q_\pm = q_1 \pm q_2$ 解耦**：
  将上面两式直接相加与相减，立即分解为两个彼此完全独立的单自由度阻尼振子方程：
  $$
  \begin{cases}
  (L + M)\dfrac{d^2 q_+}{dt^2} + R\dfrac{dq_+}{dt} + \dfrac{1}{C}q_+ = 0 \quad (\text{对称模 Symmetric mode，等效电感 } L_+ = L + M) \\[8pt]
  (L - M)\dfrac{d^2 q_-}{dt^2} + R\dfrac{dq_-}{dt} + \dfrac{1}{C}q_- = 0 \quad (\text{反对称模 Antisymmetric mode，等效电感 } L_- = L - M)
  \end{cases}
  $$
- **(c) 无阻尼简正模频率（$R = 0$）**：
  当 $R = 0$ 时，两个独立简谐振子的固有角频率分别为：
  $$
  \omega_+ = \frac{1}{\sqrt{(L + M)C}}, \qquad \omega_- = \frac{1}{\sqrt{(L - M)C}}
  $$
  由于 $M > 0$，对称同相模式 $q_+$ 的两线圈磁通同向相助，等效电感增大为 $L + M$，因此振荡频率较低（$\omega_+ < \omega_-$）。

---

**2. 直流稳态断电瞬间转入无损 LC 自由振荡的电压过冲（Exercise 13.5）**：

- **(a) 断开开关前瞬间（$t = 0^-$）**：
  开关长期闭合处于直流稳态，理想电感 $L$（无内阻）将 $A, B$ 两点完全**短路**！因此 $A, B$ 间电势差为零，电容器不带电，全部电流由电池经电阻 $r$ 和电感 $L$ 流过：
  $$
  V_A(0^-) - V_B(0^-) = 0, \qquad q(0^-) = 0, \qquad i_L(0^-) = \frac{\mathcal{E}}{r}
  $$
- **(b) 断开开关后（$t > 0$）的 LC 振荡**：
  开关断开后，$L$ 与 $C$ 构成闭合回路。由于 $i_L$ 从 $A$ 经 $L$ 流向 $B$，然后从 $B$ 流向电容器的 $A$ 极板为其充电，故有 $i_L(t) = -\frac{dq}{dt}$！
  初始条件为：$q(0^+) = 0$，$\left.\frac{dq}{dt}\right|_{t=0^+} = -i_L(0^+) = -\frac{\mathcal{E}}{r}$。
  代入标准通解 $q(t) = Q\cos(\omega_0 t + \phi)$（要求 $Q > 0$，其中 $\omega_0 = \frac{1}{\sqrt{LC}}$）：
  - 由 $q(0) = Q\cos\phi = 0$ 且 $\dot{q}(0) = -\omega_0 Q\sin\phi = -\frac{\mathcal{E}}{r} < 0$，可知 $\cos\phi = 0, \ \sin\phi = +1$，故：
    $$
    \omega_0 = \frac{1}{\sqrt{LC}}, \qquad \phi = +\frac{\pi}{2}, \qquad Q = \frac{\mathcal{E}}{\omega_0 r} = \frac{\mathcal{E}\sqrt{LC}}{r}
    $$
  - 从而各物理量的时间演化表达式为：
    $$
    q(t) = \frac{\mathcal{E}\sqrt{LC}}{r}\cos\left(\omega_0 t + \frac{\pi}{2}\right) = -\frac{\mathcal{E}\sqrt{LC}}{r}\sin(\omega_0 t)
    $$
    $$
    i_L(t) = -\frac{dq}{dt} = \frac{\mathcal{E}}{r}\cos(\omega_0 t), \qquad V_A(t) - V_B(t) = \frac{q(t)}{C} = -\frac{\mathcal{E}}{r}\sqrt{\frac{L}{C}}\sin(\omega_0 t)
    $$
- **(c) 最大电压过冲、首次达到时刻与能量守恒检验**：
  当 $\omega_0 t_1 = \frac{\pi}{2}$ 时，即首次达到时刻：
  $$
  t_1 = \frac{\pi}{2\omega_0} = \frac{\pi}{2}\sqrt{LC}
  $$
  $|V_A - V_B|$ 达到最大值：
  $$
  |V_A - V_B|_{\max} = \frac{\mathcal{E}}{r}\sqrt{\frac{L}{C}}
  $$
  此时 $V_A - V_B < 0$，故**端子 $B$ 处于高电势**。
  代入数值 $\mathcal{E} = 12\text{ V}, \ r = 6.0\ \Omega, \ L = 0.20\text{ H}, \ C = 0.50 \times 10^{-6}\text{ F}$（特征波阻抗 $\sqrt{L/C} = \sqrt{0.20 / (0.50\times 10^{-6})} = 632.46\ \Omega$）：
  $$
  |V_A - V_B|_{\max} = \frac{12}{6.0} \times 632.46 \approx 1.26 \times 10^3\text{ V} = 1.26\text{ kV}, \qquad \frac{|V_A - V_B|_{\max}}{\mathcal{E}} = \frac{1}{r}\sqrt{\frac{L}{C}} \approx 105
  $$
  **能量守恒检验**：初态电感磁能为 $U_B(0) = \frac{1}{2}Li_L^2(0) = \frac{1}{2}L\left(\frac{\mathcal{E}}{r}\right)^2$；在 $t_1$ 时刻电流为零，能量全部转化为电容电场能 $U_E(t_1) = \frac{1}{2}CV_{\max}^2$。令 $\frac{1}{2}CV_{\max}^2 = \frac{1}{2}L\left(\frac{\mathcal{E}}{r}\right)^2$，立即解得 $V_{\max} = \frac{\mathcal{E}}{r}\sqrt{\frac{L}{C}}$，完全一致！

---

**3. 过阻尼 RLC 放电的双指数衰减率与最快稳定判据（Exercise 13.6，核心数学物理题）**：

- **(a)** 当 $R > 2\sqrt{L/C}$ 时，特征方程 $L s^2 + R s + \frac{1}{C} = 0$（对 $q \propto e^{st}$）有两个负实根 $s_1 = -a, \ s_2 = -b$，其中衰减率 $a > b > 0$ 分别为：
  $$
  a = \frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 - \omega_0^2}, \qquad b = \frac{R}{2L} - \sqrt{\left(\frac{R}{2L}\right)^2 - \omega_0^2}
  $$
  通解为 $q(t) = C_1 e^{-bt} + C_2 e^{-at}$。代入初始条件 $q(0) = C_1 + C_2 = Q_0$ 与 $i(0) = \dot{q}(0) = -b C_1 - a C_2 = 0$，解得 $C_1 = \frac{a Q_0}{a - b}, \ C_2 = -\frac{b Q_0}{a - b}$，即：
  $$
  q(t) = Q_0 \frac{a e^{-bt} - b e^{-at}}{a - b}
  $$
- **(b) 强阻尼极限（$R \gg 2\sqrt{L/C}$，即 $\omega_0 \ll \frac{R}{2L}$）**：
  利用泰勒展开 $\sqrt{\left(\frac{R}{2L}\right)^2 - \omega_0^2} = \frac{R}{2L}\sqrt{1 - \frac{4L}{R^2 C}} \approx \frac{R}{2L} - \frac{1}{RC}$：
  - 快衰减率：$a \approx \frac{R}{L} \implies \dfrac{1}{a} \approx \dfrac{L}{R} = \tau_L = \dfrac{1}{2}\tau_d$；
  - 慢衰减率：$b \approx \frac{1}{RC} \implies \dfrac{1}{b} \approx RC = \tau_C \gg \tau_d$。
  由于 $b \ll a$，快指数项 $e^{-at}$ 迅速消失，长期放电过程由**较慢的衰减时间 $\dfrac{1}{b} \approx RC$ 主导**（物理原因：电阻 $R$ 极大时限制了放电电流，使电容器放电变得极其缓慢）。
- **(c) 证明临界阻尼 $R = 2\sqrt{L/C}$ 给出最快回归速率**：
  定义控制长期衰减的“最慢衰减率” $r_{\text{slow}}(R)$：
  - 当 $R < 2\sqrt{L/C}$（欠阻尼）时：包络衰减率为 $r_{\text{slow}}(R) = \frac{1}{\tau_d} = \frac{R}{2L}$，它随 $R$ 的增大而**单调递增**，在 $R \to 2\sqrt{L/C}$ 时达到 $\omega_0$；
  - 当 $R > 2\sqrt{L/C}$（过阻尼）时：慢衰减率为 $r_{\text{slow}}(R) = b = \frac{R}{2L} - \sqrt{\left(\frac{R}{2L}\right)^2 - \omega_0^2} = \dfrac{\omega_0^2}{\frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 - \omega_0^2}}$，由于分母随 $R$ 增大而严格增大，$b(R)$ 随 $R$ 的增大而**单调递减**！
  因此，最慢衰减率在分界点——**临界阻尼 $R = 2\sqrt{L/C}$ 处取得全局最大值 $r_{\text{slow, max}} = \omega_0 = \frac{1}{\sqrt{LC}}$**。

</details>

<details markdown="1">
<summary>Exercise 13.7, 13.8 & 13.9: AC Generator Torque, Practical Parallel Tank Circuit & Series Resonance Energy（交流发电机转矩极值、含阻并联谐振槽路与串联谐振恒定总储能）</summary>

**Problem Statement:**
- **Ex 13.7**: An AC generator coil ($N$ turns, area $A$) turns at constant $\omega$ about the $y$ axis in uniform $\vec{B} = B\hat{z}$ ($B > 0$). At $t$, its unit normal is $\hat{n} = \hat{x}\cos\omega t - \hat{z}\sin\omega t$. Slip rings connect it to a series $R$-$L$ load. Write $K = NAB$.
  (a) Find the generator's emf $\mathcal{E}(t)$, the current amplitude $I$, and the lag angle $\phi$.
  (b) Find the $y$ component of the magnetic torque $\tau_y(t)$ on the winding, its average over one turn, and the average torque the driving agent must supply.
  (c) For fixed $K, R, L$, find $\omega$ at which the average supplied torque is largest, and its largest value. How does it behave for $\omega \ll R/L$ and $\omega \gg R/L$?
- **Ex 13.8**: A coil (inductor $L$ in series with resistor $r > 0$) is connected in parallel with a capacitor $C$, driven by $\mathcal{E}_m\cos\omega_d t$. Let $\omega_0 = 1/\sqrt{LC}$.
  (a) Find the complex impedance $\tilde{Z}$ of the parallel pair.
  (b) Find the driving frequency $\omega_p > 0$ at which the current drawn from the source is in phase with the emf. Show that it exists only if $r < \sqrt{L/C}$, and that $\omega_p < \omega_0$.
  (c) At $\omega_d = \omega_p$, find the impedance $Z(\omega_p)$, and the ratio of the current amplitude in the coil to that drawn from the source. What do both become as $r \to 0$?
- **Ex 13.9**: A series RLC circuit ($R = 10.0\ \Omega, L = 0.100\text{ H}, C = 1.00\ \mu\text{F}$) is driven by an ideal ac source of $10.0\text{ V rms}$ at resonance $\omega_0 = 1/\sqrt{LC}$.
  (a) Find the peak current and peak values of $v_R, v_L, v_C$ (algebraically and numerically), and compare with $\mathcal{E}_{\text{peak}}$.
  (b) Show that $v_L + v_C = 0$ at every instant, so $v_R = \mathcal{E}(t)$.
  (c) Show that the total stored energy $U(t) = \frac{1}{2}Li^2 + \frac{q^2}{2C}$ does not change in time, find it, and compare with the heat produced in $R$ in one period.

---

**中文解析：**

**1. 交流发电机驱动 RL 负载的瞬时转矩、平均转矩与最佳负载转速（Exercise 13.7）**：

- **(a)** 穿过 $N$ 匝线圈的总磁通量为 $N\Phi_B(t) = NA(\vec{B}\cdot\hat{n}) = -NAB\sin(\omega t) = -K\sin(\omega t)$。由法拉第定律得感应电动势：
  $$
  \mathcal{E}(t) = -\frac{d(N\Phi_B)}{dt} = K\omega\cos(\omega t) \qquad (\text{峰值 } \mathcal{E}_m = K\omega)
  $$
  外接串联 RL 负载的阻抗大小为 $Z = \sqrt{R^2 + \omega^2 L^2}$，故稳态电流振幅 $I$ 与滞后角 $\phi$ 分别为：
  $$
  I = \frac{K\omega}{\sqrt{R^2 + \omega^2 L^2}}, \qquad \phi = \arctan\left(\frac{\omega L}{R}\right) \quad \left(\cos\phi = \frac{R}{\sqrt{R^2+\omega^2 L^2}}, \ \sin\phi = \frac{\omega L}{\sqrt{R^2+\omega^2 L^2}}\right)
  $$
  瞬时电流为 $i(t) = I\cos(\omega t - \phi)$。
- **(b) 磁力矩 $y$ 分量 $\tau_y(t)$ 与周期平均值**：
  线圈的磁偶极矩为 $\vec{\mu}(t) = NiA\hat{n} = i(t)\frac{K}{B}(\hat{x}\cos\omega t - \hat{z}\sin\omega t)$。
  由磁力矩公式 $\vec{\tau}_B = \vec{\mu} \times \vec{B} = i(t)\frac{K}{B}(\hat{x}\cos\omega t - \hat{z}\sin\omega t) \times (B\hat{z}) = -K i(t)\cos(\omega t)\,\hat{y}$，故 $y$ 分量为：
  $$
  \tau_{B, y}(t) = -K I \cos(\omega t)\cos(\omega t - \phi) = -\frac{1}{2}K I \big[\cos\phi + \cos(2\omega t - \phi)\big]
  $$
  在一个周期内对时间求平均，$\cos(2\omega t - \phi)$ 平均为零，$\langle\cos(\omega t)\cos(\omega t - \phi)\rangle = \frac{1}{2}\cos\phi$：
  $$
  \langle\tau_{B, y}\rangle = -\frac{1}{2}K I \cos\phi = -\frac{K^2 \omega R}{2(R^2 + \omega^2 L^2)}
  $$
  负号表示磁力矩阻碍线圈绕 $+y$ 轴旋转；因此外力维持恒定角速度 $\omega$ 所需提供的平均驱动力矩为：
  $$
  \langle\tau_{\text{agent}}\rangle = -\langle\tau_{B, y}\rangle = +\frac{K^2 \omega R}{2(R^2 + \omega^2 L^2)}
  $$
  *（验证：平均机械功率 $\langle\tau_{\text{agent}}\rangle\omega = \frac{1}{2}I^2 R$，恰好等于电阻的平均热耗散功率！）。*
- **(c) 使平均驱动转矩最大的角速度 $\omega$**：
  将 $\langle\tau_{\text{agent}}\rangle = \frac{K^2 R}{2\left(\frac{R^2}{\omega} + \omega L^2\right)}$ 的分母用均值不等式分析：当 $\frac{R^2}{\omega} = \omega L^2$，即：
  $$
  \omega = \frac{R}{L} = \frac{1}{\tau_L}
  $$
  时，平均转矩达到最大值，最大值为：
  $$
  \langle\tau_{\text{agent}}\rangle_{\max} = \frac{K^2}{4L}
  $$
  渐近行为：当 $\omega \ll R/L$ 时，$\langle\tau_{\text{agent}}\rangle \approx \frac{K^2}{2R}\omega \propto \omega$（随转速线性增大）；当 $\omega \gg R/L$ 时，感抗主导使电流趋于饱和且相位滞后趋于 $\pi/2$（功率因数 $\cos\phi \approx \frac{R}{\omega L} \to 0$），故 $\langle\tau_{\text{agent}}\rangle \approx \frac{K^2 R}{2L^2 \omega} \propto \frac{1}{\omega}$（随转速反比减小）！

---

**2. 实际电感线圈（$L$ 串 $r$）与电容 $C$ 并联谐振槽路（Practical Parallel Tank Circuit，Exercise 13.8）**：

- **(a) 并联总复阻抗 $\tilde{Z}$**：
  线圈支路复阻抗为 $\tilde{Z}_{\text{coil}} = r + i\omega_d L$，电容支路复阻抗为 $\tilde{Z}_C = \frac{1}{i\omega_d C}$。由并联公式：
  $$
  \frac{1}{\tilde{Z}} = \frac{1}{r + i\omega_d L} + i\omega_d C = \frac{r - i\omega_d L}{r^2 + \omega_d^2 L^2} + i\omega_d C = \frac{r}{r^2 + \omega_d^2 L^2} + i\omega_d\left(C - \frac{L}{r^2 + \omega_d^2 L^2}\right)
  $$
  取倒数即得：
  $$
  \tilde{Z} = \frac{r + i\omega_d L}{(1 - \omega_d^2 LC) + i\omega_d r C}
  $$
- **(b) 干路电流与电源同相的并联谐振角频率 $\omega_p$**：
  要使干路总电流与电动势同相，要求 $\tilde{Z}$（或 $1/\tilde{Z}$）的虚部为零：
  $$
  C - \frac{L}{r^2 + \omega_p^2 L^2} = 0 \implies r^2 + \omega_p^2 L^2 = \frac{L}{C} \implies \omega_p = \sqrt{\frac{1}{LC} - \frac{r^2}{L^2}} = \sqrt{\omega_0^2 - \left(\frac{r}{L}\right)^2}
  $$
  显然，要使根号内大于零从而存在实数解 $\omega_p > 0$，必须满足条件 **$r < \sqrt{\dfrac{L}{C}}$**，且恒有 **$\omega_p < \omega_0$**。
- **(c) 并联谐振时的纯阻阻抗 $Z(\omega_p)$ 与支路电流放大比**：
  在 $\omega_d = \omega_p$ 时，$r^2 + \omega_p^2 L^2 = \frac{L}{C}$ 且 $1/\tilde{Z}$ 的虚部为零，代入得此时的纯电阻阻抗：
  $$
  Z(\omega_p) = \frac{r^2 + \omega_p^2 L^2}{r} = \frac{L}{r C}
  $$
  此时干路电流振幅为 $I_{\text{source}} = \frac{\mathcal{E}_m}{Z(\omega_p)} = \frac{\mathcal{E}_m r C}{L}$，而流过线圈支路的电流振幅为 $I_{\text{coil}} = \frac{\mathcal{E}_m}{\sqrt{r^2 + \omega_p^2 L^2}} = \frac{\mathcal{E}_m}{\sqrt{L/C}}$。两者之比为：
  $$
  \frac{I_{\text{coil}}}{I_{\text{source}}} = \frac{Z(\omega_p)}{\sqrt{r^2 + \omega_p^2 L^2}} = \frac{L / (rC)}{\sqrt{L/C}} = \frac{1}{r}\sqrt{\frac{L}{C}}
  $$
  当 $r \to 0$ 时，$\omega_p \to \omega_0$，谐振阻抗 **$Z(\omega_p) = \frac{L}{rC} \to \infty$**，且电流比 **$\frac{I_{\text{coil}}}{I_{\text{source}}} \to \infty$**（干路无需输入电流，而 LC 环路内部存在巨大的环流，退化为 §3.3 末尾的理想并联 LC 反谐振槽路）。

---

**3. 串联 RLC 谐振时的电压放大（品质因数 $Q$）与恒定总电磁储能（Exercise 13.9，必考重点）**：

- **(a) 谐振时的峰值电流与各元件峰值电压**：
  在谐振频率 $\omega_0 = \frac{1}{\sqrt{LC}}$ 下，总阻抗 $Z = R$，电源峰值电动势为 $\mathcal{E}_m = \sqrt{2}\,\mathcal{E}_{\text{rms}}$。
  因此峰值电流及三个元件上的峰值电压分别为：
  $$
  I_{\text{peak}} = \frac{\sqrt{2}\,\mathcal{E}_{\text{rms}}}{R}, \qquad V_{R,\text{peak}} = I_{\text{peak}}R = \sqrt{2}\,\mathcal{E}_{\text{rms}} = \mathcal{E}_m
  $$
  $$
  V_{L,\text{peak}} = I_{\text{peak}}\omega_0 L = \frac{\sqrt{2}\,\mathcal{E}_{\text{rms}}}{R}\sqrt{\frac{L}{C}}, \qquad V_{C,\text{peak}} = \frac{I_{\text{peak}}}{\omega_0 C} = \frac{\sqrt{2}\,\mathcal{E}_{\text{rms}}}{R}\sqrt{\frac{L}{C}}
  $$
  代入数值 $R = 10.0\ \Omega, \ L = 0.100\text{ H}, \ C = 1.00 \times 10^{-6}\text{ F}, \ \mathcal{E}_{\text{rms}} = 10.0\text{ V}$（此时 $\mathcal{E}_m = 10\sqrt{2} \approx 14.14\text{ V}$，$\omega_0 = \frac{1}{\sqrt{10^{-7}}} = \sqrt{10}\times 10^3 \approx 3162.3\text{ rad/s}$，$\sqrt{L/C} = 100\sqrt{10} \approx 316.23\ \Omega$）：
  $$
  I_{\text{peak}} = \frac{10\sqrt{2}}{10.0} = \sqrt{2}\text{ A} \approx 1.41\text{ A}, \qquad V_{R,\text{peak}} = 10\sqrt{2}\text{ V} \approx 14.1\text{ V}
  $$
  $$
  V_{L,\text{peak}} = V_{C,\text{peak}} = \sqrt{2} \times 100\sqrt{10} = 200\sqrt{5}\text{ V} \approx 447\text{ V}
  $$
  **对比**：电感与电容上的峰值电压是电源峰值电动势（$14.1\text{ V}$）的 $\frac{1}{R}\sqrt{\frac{L}{C}} = 10\sqrt{10} \approx 31.6$ 倍（这一比值即为谐振电路的**品质因数 Quality factor**，体现了串联谐振的**电压放大效应**）！
- **(b) 证明任意时刻 $v_L(t) + v_C(t) \equiv 0$**：
  在谐振状态下 $\phi = 0$，设 $\mathcal{E}(t) = \mathcal{E}_m\cos(\omega_0 t)$，则稳态电流为 $i(t) = I_{\text{peak}}\cos(\omega_0 t)$，极板电荷为 $q(t) = \int i(t)\,dt = \frac{I_{\text{peak}}}{\omega_0}\sin(\omega_0 t)$。
  计算任意瞬时的电感压降与电容压降（利用 $\omega_0 L = \frac{1}{\omega_0 C}$）：
  $$
  v_L(t) = L\frac{di}{dt} = -\omega_0 L I_{\text{peak}}\sin(\omega_0 t), \qquad v_C(t) = \frac{q(t)}{C} = +\frac{I_{\text{peak}}}{\omega_0 C}\sin(\omega_0 t) = +\omega_0 L I_{\text{peak}}\sin(\omega_0 t)
  $$
  相加立即得到 **$v_L(t) + v_C(t) \equiv 0$**（在每一瞬间电感电压与电容电压都精确抵消），因此回路中永远有 $v_R(t) = \mathcal{E}(t)$。
- **(c) 证明谐振时电磁场总储能 $U(t)$ 恒定不变并与单周期焦耳热对比**：
  计算任意时刻储存在电感与电容中的总电磁能（利用 $\frac{1}{C\omega_0^2} = L$）：
  $$
  \begin{aligned}
  U(t) &= \frac{1}{2}Li^2(t) + \frac{q^2(t)}{2C} = \frac{1}{2}L I_{\text{peak}}^2\cos^2(\omega_0 t) + \frac{I_{\text{peak}}^2}{2C\omega_0^2}\sin^2(\omega_0 t) \\
  &= \frac{1}{2}L I_{\text{peak}}^2\big[\cos^2(\omega_0 t) + \sin^2(\omega_0 t)\big] = \frac{1}{2}L I_{\text{peak}}^2 = \frac{L\mathcal{E}_{\text{rms}}^2}{R^2} = \text{const}
  \end{aligned}
  $$
  代入数值：$U = \frac{1}{2} \times 0.100 \times (\sqrt{2})^2 = 0.100\text{ J}$。
  因为总储能 $U(t)$ 在谐振时完全不随时间变化，电源在每一瞬间输出的功率全部直接供给电阻发热！在一个周期 $T = \frac{2\pi}{\omega_0} = 2\pi\sqrt{LC}$ 内，电阻上产生的焦耳热为：
  $$
  H_T = P_{\text{avg}} T = \frac{\mathcal{E}_{\text{rms}}^2}{R} \cdot 2\pi\sqrt{LC} = 10.0\text{ W} \times 2\pi\times 10^{-3.5}\text{ s} \approx 0.0199\text{ J} = 19.9\text{ mJ}
  $$
  两者的比值为 $\dfrac{U}{H_T} = \dfrac{1}{2\pi R}\sqrt{\dfrac{L}{C}} \approx 5.03$（即品质因数 $Q = 2\pi\frac{U}{H_T} \approx 31.6$）。

</details>