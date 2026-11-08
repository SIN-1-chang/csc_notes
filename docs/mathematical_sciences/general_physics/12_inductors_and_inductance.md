# Chapter 12: Inductors and Inductance（电感器与电感）

!!! abstract
    General Physics II (Electromagnetism) | 第十二章课堂与讲义笔记
    
    参考：
    
    - Lecture 12: *Inductors and Inductance* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 12: *Inductors and Inductance*
    - Halliday, Resnick & Krane, *Physics*, Chapter 36

## 1 电感器与电感 (Inductors and Inductance)

### 1.1 电感器的定义与电感-电容对偶性

在静电学中，我们使用**电容器**（Capacitor，基本构型为平行板电容器）来产生所需的匀强电场并在电场中储存静电能；作为磁学中的严格对偶元件，我们使用**电感器**（Inductor，基本构型为远离端点的长直螺线管）来产生所需的匀强磁场并在磁场中储存磁能。

设一个共有 $N$ 匝的线圈（电感器）通有电流 $i$，电流在周围空间激发磁场，使得穿过每一匝线圈横截面的磁通量为 $\Phi_B$。我们将乘积 $N\Phi_B$ 称为**磁通匝链数**或**磁链**（Magnetic Flux Linkage）。由于根据毕奥-萨伐尔定律，空间各点的磁感应强度 $\vec{B}$ 与电流 $i$ 严格成正比，因此总磁链 $N\Phi_B$ 也与电流 $i$ 成正比。定义该比例常数为电感器的**电感**（Inductance，记作 $L$）：

$$
L = \frac{N\Phi_B}{i} \iff N\Phi_B = L i
$$

电感 $L$ 度量了单位电流在电感器中所产生的磁通匝链数。在国际单位制（SI）中，电感的单位为**亨利**（Henry，简记为 $\text{H}$，以独立发现电磁感应现象的美国物理学家 Joseph Henry 命名）：

$$
1\text{ H} = 1\ \frac{\text{T}\cdot\text{m}^2}{\text{A}} = 1\ \frac{\text{Wb}}{\text{A}} = 1\ \frac{\text{V}\cdot\text{s}}{\text{A}} = 1\ \Omega\cdot\text{s}
$$

电容器（Capacitor）与电感器（Inductor）的核心物理量对偶关系汇总如下表：

| 物理属性维度 | 电容器（Capacitor — 电场储能元件） | 电感器（Inductor — 磁场储能元件） |
| :--- | :--- | :--- |
| **基本理想几何构型** | 平行板电容器（面积 $S$，间距 $d$，忽略边缘效应） | 长直螺线管（截面积 $S$，长 $l$，忽略端部发散效应） |
| **内部匀强场强公式** | $E = \dfrac{\sigma}{\epsilon_0} = \dfrac{Q}{\epsilon_0 S}$ | $B = \mu_0 n i = \dfrac{\mu_0 N i}{l}$ |
| **本征参数定义式** | 电容 $C = \dfrac{Q}{V}$（单位电压储存的电荷量） | 电感 $L = \dfrac{N\Phi_B}{i}$（单位电流产生的磁通匝链数） |
| **理想构型参数公式** | $C = \dfrac{\epsilon_0 S}{d}$（填充电介质 $\epsilon_r$ 时乘以 $\epsilon_r$） | $L = \mu_0 n^2 l S = \dfrac{\mu_0 N^2 S}{l}$（填充磁芯 $\mu_r$ 时乘以 $\mu_r$） |
| **元件储存的总能量** | $U_E = \dfrac{Q^2}{2C} = \dfrac{1}{2}CV^2$ | $U_B = \dfrac{1}{2}Li^2 = \dfrac{(N\Phi_B)^2}{2L}$ |
| **空间场的能量密度** | 电场能量密度 $u_E = \dfrac{1}{2}\epsilon_0 E^2$ | 磁场能量密度 $u_B = \dfrac{1}{2\mu_0}B^2$ |

### 1.2 长直螺线管的电感推导

考察长度为 $l$、横截面积为 $S$（课件中亦记为 $A$）、单位长度匝数为 $n = N/l$ 的长直螺线管（满足 $l \gg \sqrt{S}$，忽略端部的磁场发散效应）：

1. 当通以电流 $i$ 时，由安培环路定理知管内匀强磁场为 $B = \mu_0 n i$；
2. 穿过单匝线圈横截面的磁通量为 $\Phi_B = BS = \mu_0 n S i$，总匝数为 $N = nl$，故总磁链为 $N\Phi_B = (nl)(\mu_0 n S i) = \mu_0 n^2 l S i$；
3. 代入电感定义式，即得**长直螺线管的自感公式**及其**单位长度电感**：
   $$
   L = \frac{N\Phi_B}{i} = \mu_0 n^2 l S = \frac{\mu_0 N^2 S}{l}, \qquad \frac{L}{l} = \mu_0 n^2 S
   $$

与电容一样，无磁芯电感器的电感 $L$ **仅取决于线圈的几何结构（尺寸、形状、匝数）**，而与电流 $i$ 无关（因为 $N$ 既决定磁场 $B \propto N$，又决定匝链数 $N\Phi_B \propto N B$，故电感总是与匝数的平方 $N^2$ 成正比）。若在螺线管内部填满相对磁导率为 $\mu_r$ 的线性磁介质（如铁芯或铁氧体磁芯 Ferrite core），管内磁场增强为 $B = \mu_r\mu_0 n i$，电感随之增大为真空时的 $\mu_r$ 倍：$L = \mu_r\mu_0 n^2 l S$。

---

## 2 自感现象与电感器端电压 (Self-Induction and Terminal Potential Difference)

### 2.1 自感电动势 (Self-Induced Emf)

当电感线圈自身的电流 $i(t)$ 随时间发生变化时，它自身激发并穿过自身的磁通匝链数 $N\Phi_B = Li$ 随之改变。根据法拉第电磁感应定律，在线圈自身内部必然产生感应电动势，这一现象称为**自感**（Self-Induction），所产生的电动势称为**自感电动势**（Self-Induced Emf，记作 $\mathcal{E}_L$）：

$$
\mathcal{E}_L = -\frac{d(N\Phi_B)}{dt} = -L\frac{di}{dt}
$$

根据楞次定律，公式中的负号表明：**自感电动势 $\mathcal{E}_L$ 的方向总是阻碍（Oppose）线圈自身电流 $i$ 的变化**：

- **当电流 $i$ 正在增大（$\frac{di}{dt} > 0$）时**：自感电动势 $\mathcal{E}_L$ 的方向与电流 $i$ 的方向**相反**，反抗电流的增长；
- **当电流 $i$ 正在减小（$\frac{di}{dt} < 0$）时**：自感电动势 $\mathcal{E}_L$ 的方向与电流 $i$ 的方向**相同**，试图维持原电流、反抗电流的衰减。

*日常生活实例（讲义 Section 12.2）*：当一台带有电动机或变压器的电器正在运转时，若直接拔下电源插头，由于绕组中的电流不能瞬间突变归零（在触点分离的极短时间内 $\left|\frac{di}{dt}\right|$ 极大），会产生高达数千伏的自感电动势 $\mathcal{E}_L = -L\frac{di}{dt}$，击穿插头与插座间隙的空气并产生肉眼可见的**电火花**（Spark）。

### 2.2 理想电感器两端的电势差 ($V_L$)

在第十一章中我们强调过：在线圈内部磁通量随时间变化的区域内，感生电场是非保守场（$\nabla\times\vec{E} \neq \vec{0}$），因此在线圈内部无法定义标量电势 $V$。

然而，在电路分析中，我们关心的是位于变化磁通区域**外部**的电感器两个引出端子 $a$ 和 $b$（那里只有由表面电荷分布建立的库仑静电场，电势依然严格良定义）。考察由理想无阻导线（$r = 0$）绕制的电感线圈，内部总电场必须为零（$\vec{E}_{\text{total}} = \vec{E}_{\text{static}} + \vec{E}_{\text{ind}} = \vec{0}$，否则无穷大电导率会导致无穷大电流）。对“从端子 $a$ 经线圈内部到端子 $b$、再沿磁通区外部路径回到 $a$”的闭合回路应用法拉第定律，可知外部路径积分得到的端子电势差 $V_a - V_b = \int_a^b \vec{E}_{\text{static}}\cdot d\vec{l}$ 在数值上恒等于自感电动势的大小：

$$
V_a - V_b = +L\frac{di}{dt} \qquad (\text{电流 } i \text{ 的正方向规定为从端子 } a \text{ 流向端子 } b)
$$

!!! warning "基尔霍夫回路定律（KVL）中电感器压降的符号铁律"
    设电流 $i$ 从端子 $a$ 流入电感器、从端子 $b$ 流出：
    
    - **顺着电流 $i$ 的方向跨越电感器（从 $a$ 到 $b$）**：电势变化量为 **$\Delta V = V_b - V_a = -L\dfrac{di}{dt}$**（当电流增大 $di/dt > 0$ 时电势降低；当电流减小 $di/dt < 0$ 时电势反而升高！）；
    - **逆着电流 $i$ 的方向跨越电感器（从 $b$ 到 $a$）**：电势变化量为 **$\Delta V = V_a - V_b = +L\dfrac{di}{dt}$**。

---

## 3 RL 暂态电路 (RL Circuits)

### 3.1 电流的建立（增长）与衰减过程

将电阻 $R$、电感器 $L$ 与电动势为 $\mathcal{E}$ 的理想电源串联构成 **RL 电路**。

**1. 接通电源时的电流增长过程（Current Rise，初始条件 $i(0) = 0$）**

在 $t = 0$ 时刻合上开关接通电源 $\mathcal{E}$，顺着电流方向应用基尔霍夫回路定律：

$$
\mathcal{E} - iR - L\frac{di}{dt} = 0 \iff L\frac{di}{dt} + Ri = \mathcal{E} \iff \frac{L}{R}\frac{di}{dt} + i = \frac{\mathcal{E}}{R}
$$

由量纲分析可知，比值 $\tau_L = \frac{L}{R}$ 具有时间的量纲（$[\tau_L] = \frac{\text{H}}{\Omega} = \frac{\text{V}\cdot\text{s/A}}{\text{V/A}} = \text{s}$），称为 RL 电路的**感性时间常数**（Inductive Time Constant）：

$$
\tau_L = \frac{L}{R}
$$

求解上述一阶常系数非齐次线性微分方程（代入初始条件 $i(0) = 0$），可得电流 $i(t)$、电阻电压 $V_R(t)$ 与电感端电压 $V_L(t)$ 随时间的演化：

$$
i(t) = \frac{\mathcal{E}}{R}\left(1 - e^{-t/\tau_L}\right), \qquad V_R(t) = i(t)R = \mathcal{E}\left(1 - e^{-t/\tau_L}\right), \qquad V_L(t) = L\frac{di}{dt} = \mathcal{E}e^{-t/\tau_L}
$$

- 在刚接通瞬间（$t = 0^+$）：由于电感电流不能突变（$i(0^+) = 0$），**电感器在 $t = 0^+$ 瞬间相当于断路（Open circuit）**，全部电源电压降落在电感两端（$V_L(0^+) = \mathcal{E}$）；
- 经过一个时间常数（$t = \tau_L$）：电流增长到稳态终值 $\frac{\mathcal{E}}{R}$ 的 $1 - e^{-1} \approx 63.2\%$；
- 经过很长时间达到稳态后（$t \to \infty$）：$\frac{di}{dt} \to 0 \implies V_L \to 0$，**理想电感器在直流稳态下相当于一根无阻短路导线（Short circuit / Ordinary connecting wire）**，稳态电流由纯电阻决定：$i(\infty) = \frac{\mathcal{E}}{R}$。

**2. 切除电源后的电流衰减过程（Current Decay，初始条件 $i(0) = i_0 = \mathcal{E}/R$）**

当电路达到稳态电流 $i_0$ 后，在新的 $t = 0$ 时刻将开关切换至直接通过电阻 $R$ 短路闭合（切除电源 $\mathcal{E}$）。此时回路方程化为：

$$
L\frac{di}{dt} + Ri = 0 \implies i(t) = i_0 e^{-t/\tau_L} = \frac{\mathcal{E}}{R}e^{-t/\tau_L}
$$

### 3.2 RL 电路与 RC 电路的暂态特性全面对比

| 对比维度 | RC 串联电路（Capacitive Circuit, Chapter 7） | RL 串联电路（Inductive Circuit, Chapter 12） |
| :--- | :--- | :--- |
| **控制微分方程（接通 $\mathcal{E}$）** | $R\dfrac{dq}{dt} + \dfrac{1}{C}q = \mathcal{E}$ | $L\dfrac{di}{dt} + Ri = \mathcal{E}$ |
| **特征时间常数（Time Constant）** | $\tau_C = RC$ | $\tau_L = \dfrac{L}{R}$ |
| **不能发生突变的连续状态量** | 极板电荷 $q(t)$（及电容电压 $V_C = q/C$）不能突变 | 电感电流 $i(t)$（及磁链 $N\Phi_B = Li$）不能突变 |
| **接通瞬间（$t = 0^+$）等效状态** | 未充电电容相当于**短路导线**（$V_C = 0, \ i = \mathcal{E}/R$） | 无初流电感相当于**断路开关**（$i = 0, \ V_L = \mathcal{E}$） |
| **直流稳态（$t \to \infty$）等效状态** | 充满电的电容相当于**断路开关**（$i = 0, \ V_C = \mathcal{E}$） | 稳恒流电感相当于**短路导线**（$V_L = 0, \ i = \mathcal{E}/R$） |
| **充电/建立过程演化公式** | $q(t) = C\mathcal{E}\left(1 - e^{-t/\tau_C}\right), \quad i(t) = \dfrac{\mathcal{E}}{R}e^{-t/\tau_C}$ | $i(t) = \dfrac{\mathcal{E}}{R}\left(1 - e^{-t/\tau_L}\right), \quad V_L(t) = \mathcal{E}e^{-t/\tau_L}$ |
| **放电/衰减过程演化公式** | $q(t) = q_0 e^{-t/\tau_C}, \quad i(t) = -\dfrac{q_0}{RC}e^{-t/\tau_C}$ | $i(t) = i_0 e^{-t/\tau_L}, \quad V_L(t) = -i_0 R e^{-t/\tau_L}$ |
| **稳态储存的场能量** | 电场能 $U_E = \dfrac{Q^2}{2C} = \dfrac{1}{2}C\mathcal{E}^2$ | 磁场能 $U_B = \dfrac{1}{2}Li^2 = \dfrac{1}{2}L\left(\dfrac{\mathcal{E}}{R}\right)^2$ |

---

## 4 磁场储能与磁能密度 (Energy Stored in a Magnetic Field)

### 4.1 电感器的磁能推导

将 RL 电路的回路方程 $\mathcal{E} = iR + L\frac{di}{dt}$ 两边同乘以瞬时电流 $i$，得到电路的瞬时功率平衡方程：

$$
\mathcal{E}i = i^2 R + L i \frac{di}{dt}
$$

根据能量守恒定律，等式三项的物理意义分别为：

1. **左侧 $\mathcal{E}i = \mathcal{E}\frac{dq}{dt}$**：电源克服非静电力做功、向电路输出总能量的功率；
2. **右侧第一项 $i^2 R$**：电阻上不可逆地转化为焦耳热（Thermal energy）耗散掉的功率；
3. **右侧第二项 $Li\frac{di}{dt}$**：输入到电感器中并储存在其磁场内的**磁能增长率** $\frac{dU_B}{dt}$：
   $$
   \frac{dU_B}{dt} = L i \frac{di}{dt} = \frac{d}{dt}\left(\frac{1}{2}Li^2\right)
   $$

从电流为 $0$ 积分至稳态电流 $i$，即得到通有电流 $i$ 的电感器 $L$ 所储存的总**磁场能量**（Magnetic Potential Energy）：

$$
U_B = \int_0^i L i'\,di' = \frac{1}{2} L i^2
$$

### 4.2 磁场能量密度 ($u_B = \frac{B^2}{2\mu_0}$)

考察长度为 $l$（课件记为 $h$）、横截面积为 $S$（课件记为 $A$）的理想长直螺线管。管外磁场为零，磁能完全均匀储存在管内体积 $V = Sl$ 的空间中。将 $L = \mu_0 n^2 l S$ 代入磁能公式，并利用管内磁场 $B = \mu_0 n i$：

$$
U_B = \frac{1}{2}Li^2 = \frac{1}{2}(\mu_0 n^2 l S)i^2 = \frac{(\mu_0 n i)^2}{2\mu_0}(Sl) = \frac{B^2}{2\mu_0}(Sl)
$$

由此定义单位体积内储存的磁场能量为**磁场能量密度**（Magnetic Energy Density，记作 $u_B$，SI 单位为 $\text{J/m}^3$）：

$$
u_B = \frac{U_B}{Sl} = \frac{B^2}{2\mu_0} \quad (\text{真空或非磁性介质中}), \qquad u_B = \frac{B^2}{2\mu} = \frac{B^2}{2\mu_r\mu_0} = \frac{1}{2}\vec{B}\cdot\vec{H} \quad (\text{线性磁介质中})
$$

虽然上式由理想螺线管导出，但它**对空间任意磁场分布均普适成立**！对于非均匀磁场（如同轴电缆或螺绕环），既可以先求自感 $L$ 再算 $\frac{1}{2}Li^2$，也可以先对全空间积分磁能密度 $U_B = \int \frac{B^2}{2\mu_0}\,dV$，进而利用 $L = \frac{2U_B}{i^2}$ 反推复杂导体系统的自感（见 Exercise 12.7）。

---

## 5 互感现象与电感矩阵 (Mutual Induction and Inductance Matrix)

### 5.1 互感系数与互感电动势

当两个线圈（Coil 1，匝数 $N_1$；Coil 2，匝数 $N_2$）彼此靠近放置时，线圈 1 中的电流 $i_1$ 激发的磁场 $\vec{B}_1$ 会有一部分穿过线圈 2，在线圈 2 的每一匝中产生磁通量 $\Phi_{21}$。这种通过磁通耦合在两个电路之间产生感应的物理过程称为**互感**（Mutual Induction）。

定义线圈 2 对线圈 1 的**互感系数**（Mutual Inductance，简称**互感**，记作 $M_{21}$，单位同样为亨利 $\text{H}$）为单位电流 $i_1$ 在线圈 2 中产生的磁通匝链数：

$$
M_{21} = \frac{N_2 \Phi_{21}}{i_1} \iff N_2 \Phi_{21} = M_{21} i_1
$$

当电流 $i_1(t)$ 随时间变化时，由法拉第定律，在线圈 2 中产生的**互感电动势**为：

$$
\mathcal{E}_{21} = -\frac{d(N_2 \Phi_{21})}{dt} = -M_{21}\frac{di_1}{dt}
$$

完全对称地，当线圈 2 通有变化电流 $i_2(t)$ 时，在线圈 1 中产生的互感系数与互感电动势分别为：

$$
M_{12} = \frac{N_1 \Phi_{12}}{i_2}, \qquad \mathcal{E}_{12} = -M_{12}\frac{di_2}{dt}
$$

**经典模型（Example 12.1：同轴共面大小圆线圈的互感）**：
设半径为 $R_1$、匝数为 $N_1$ 的大圆线圈与半径为 $R_2 \ll R_1$、匝数为 $N_2$ 的小圆线圈同心共面放置（或同轴近距放置）。由于 $R_2 \ll R_1$，不能直接求小线圈在整個大线圈截面上产生的非均匀磁场通量 $\Phi_{12}$，而应**先算大线圈通电 $i_1$ 在小线圈处产生的近乎均匀的磁场**：
大线圈在圆心处的磁场为 $B_1 = \frac{\mu_0 N_1 i_1}{2R_1}$，穿过小线圈单匝面积 $\pi R_2^2$ 的磁通量为 $\Phi_{21} \approx \pi R_2^2 B_1 = \frac{\mu_0 N_1 i_1 \pi R_2^2}{2R_1}$，从而一步求得互感：

$$
M = M_{21} = \frac{N_2 \Phi_{21}}{i_1} = \frac{\mu_0 N_1 N_2 \pi R_2^2}{2R_1}
$$

### 5.2 互感互易定理 ($M_{12} = M_{21}$) 的能量守恒证明与电感矩阵

互感系数仅由两个线圈的几何形状、大小、相对位置与取向决定。无论两个线圈的形状和大小多么不对称，恒有**互感互易定理**（Reciprocity Theorem）：

$$
M_{12} = M_{21} \equiv M
$$

<details markdown="1">
<summary>点击展开：利用双路径磁能守恒严格证明互易定理 M₁₂ = M₂₁（Section 12.5）</summary>

设两个固定且无电阻的线圈 $L_1, L_2$ 分别连接可控电流源 $\mathcal{E}_1, \mathcal{E}_2$。考察将两线圈电流从初态 $(0, 0)$ 缓慢建立到终态 $(i_1, i_2)$ 的两条不同路径，计算外电源所做的总功：

1. **路径 1（先将线圈 1 从 $0$ 升至 $i_1$ 并保持 $i_2 = 0$；再保持 $i_1$ 不变，将线圈 2 从 $0$ 升至 $i_2$）**：
   - 第一阶段（$0 \to i_1, \ i_2 = 0$）：电源 1 克服自感做功 $W_1 = \frac{1}{2}L_1 i_1^2$，电源 2 做功为 $0$；
   - 第二阶段（保持 $i_1$ 恒定，$i_2' : 0 \to i_2$）：电源 2 克服自身自感做功 $W_2 = \frac{1}{2}L_2 i_2^2$。**但在此过程中**，变化的 $i_2'$ 通过互感在线圈 1 中产生互感电动势 $\mathcal{E}_{12}' = -M_{12}\frac{di_2'}{dt}$！为了维持线圈 1 中的电流 $i_1$ 恒定不变，电源 1 必须输出补偿电压 $V_1' = -\mathcal{E}_{12}' = +M_{12}\frac{di_2'}{dt}$，从而电源 1 额外做功：
     $$
     W_1' = \int P_1'\,dt = \int_0^t i_1 \left(M_{12}\frac{di_2'}{dt'}\right)dt' = M_{12} i_1 \int_0^{i_2} di_2' = M_{12} i_1 i_2
     $$
   因此，沿路径 1 两电源所做的总功为：
   $$
   W_{\text{Path 1}} = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 + M_{12} i_1 i_2
   $$
2. **路径 2（先将线圈 2 从 $0$ 升至 $i_2$ 并保持 $i_1 = 0$；再保持 $i_2$ 不变，将线圈 1 从 $0$ 升至 $i_1$）**：
   完全对称地重复上述分析，在第二阶段电源 2 为维持 $i_2$ 恒定需克服 $\mathcal{E}_{21}' = -M_{21}\frac{di_1'}{dt}$ 额外做功 $W_2' = M_{21} i_1 i_2$，故沿路径 2 的总功为：
   $$
   W_{\text{Path 2}} = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 + M_{21} i_1 i_2
   $$
3. **由状态函数唯一性得出结论**：
   由于线圈无电阻热耗散，外电源所做的功全部转化为空间磁场的能量 $U_B = \int \frac{B^2}{2\mu_0}\,dV$。而终态空间合磁场 $\vec{B} = \vec{B}_1 + \vec{B}_2$ 仅由终态电流 $(i_1, i_2)$ 唯一确定，与建立电流的历史路径无关。因此必有 $W_{\text{Path 1}} = W_{\text{Path 2}}$，消去自感能量项即证得：
   $$
   M_{12} i_1 i_2 = M_{21} i_1 i_2 \implies M_{12} = M_{21} = M
   $$

</details>

**双耦合回路的对称电感矩阵（Inductance Matrix）与总磁能**：
将自感与互感同时计入，两个耦合线圈的总磁通匝链数、总感应电动势以及系统总磁能可写成优美的矩阵与二次型形式：

$$
\begin{pmatrix} N_1\Phi_1 \\ N_2\Phi_2 \end{pmatrix} = \begin{pmatrix} L_1 & M \\ M & L_2 \end{pmatrix} \begin{pmatrix} i_1 \\ i_2 \end{pmatrix}, \qquad \begin{pmatrix} \mathcal{E}_{\text{ind}, 1} \\ \mathcal{E}_{\text{ind}, 2} \end{pmatrix} = -\begin{pmatrix} L_1 & M \\ M & L_2 \end{pmatrix} \frac{d}{dt}\begin{pmatrix} i_1 \\ i_2 \end{pmatrix}
$$

$$
U_B = \frac{1}{2}\begin{pmatrix} i_1 & i_2 \end{pmatrix} \begin{pmatrix} L_1 & M \\ M & L_2 \end{pmatrix} \begin{pmatrix} i_1 \\ i_2 \end{pmatrix} = \frac{1}{2}L_1 i_1^2 + \frac{1}{2}L_2 i_2^2 + M i_1 i_2
$$

（注：互感项 $M$ 可正可负，取决于两线圈选定的电流正方向所产生的磁场是同向相助还是反向相消）。

---

## 6 Chapter 12 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 12.1, 12.2 & 12.3: Coaxial Shells, Rectangular Toroid & Wire-Loop Mutual Inductance（同轴圆筒自感、矩形螺绕环自感与直导线-矩形框互感）</summary>

**Problem Statement:**
- **Ex 12.1**: Consider two coaxial cylindrical conducting shells of radii $R_1$ and $R_2 \ (R_1 < R_2)$ and length $l$. A current $I$ flows down the inner shell and back along the outer one, spread uniformly round each shell. Ignore boundary effects. Calculate the self-inductance of the system.
- **Ex 12.2**: A toroidal coil with an air core has a rectangular cross-section. The inner radius is $a$, the outer radius is $b$, and the height is $h$. The toroid has $N$ turns of wire uniformly wound around it. Find the self-inductance $L$ of the toroid.
- **Ex 12.3**: An infinitely long straight wire carrying current $I$ lies in the same plane as a rectangular loop of dimensions $a \times b$. The near edge of the loop is at distance $c$ from the wire, and the far edge is at distance $b + c$ from the wire.
  (a) Find $M_{21}$, the flux through the loop per unit current in the wire.
  (b) If $a = 10\text{ cm}, \ b = 5\text{ cm}, \ c = 3\text{ cm}$, calculate $M$.
  (c) What is the induced emf in the loop if $dI/dt = 100\text{ A/s}$? Give its magnitude and the sense of the induced current on the side nearer the wire.

---

**中文解析：**

**1. 同轴薄圆柱壳传输线的自感（Exercise 12.1）**：
由安培环路定理，在 $r < R_1$（内壳内部）和 $r > R_2$（外壳外部）处磁场均为 $B = 0$；仅在两壳之间的环形空间 $R_1 < r < R_2$ 内存在方位角方向的磁场：

$$
B(r) = \frac{\mu_0 I}{2\pi r} \qquad (R_1 < r < R_2)
$$

- **方法 1（由穿过轴向矩形截面的磁通量计算）**：
  连接内外圆筒构成单匝闭合回路（$N = 1$），穿过长为 $l$、径向从 $R_1$ 到 $R_2$ 的子午面矩形截面的磁通量为：
  $$
  \Phi_B = \int_{R_1}^{R_2} B(r) l\,dr = \frac{\mu_0 I l}{2\pi} \int_{R_1}^{R_2} \frac{dr}{r} = \frac{\mu_0 l I}{2\pi}\ln\left(\frac{R_2}{R_1}\right) \implies L = \frac{\Phi_B}{I} = \frac{\mu_0 l}{2\pi}\ln\left(\frac{R_2}{R_1}\right)
  $$
- **方法 2（由磁场能量密度积分计算）**：
  $$
  U_B = \int_{R_1}^{R_2} \frac{B^2(r)}{2\mu_0} (2\pi r l\,dr) = \frac{\mu_0 l I^2}{4\pi}\ln\left(\frac{R_2}{R_1}\right) = \frac{1}{2}LI^2 \implies L = \frac{\mu_0 l}{2\pi}\ln\left(\frac{R_2}{R_1}\right)
  $$

---

**2. 矩形截面空芯螺绕环（Toroid）的自感（Exercise 12.2）**：
由第九章结论，螺绕环内部距中心轴距离为 $r \ (a < r < b)$ 处的磁感应强度为 $B(r) = \frac{\mu_0 N i}{2\pi r}$。
在矩形截面上取宽为 $dr$、高为 $h$ 的竖直窄条面元 $dS = h\,dr$，穿过单匝截面的磁通量为：

$$
\Phi_B = \int_a^b B(r) h\,dr = \frac{\mu_0 N i h}{2\pi} \int_a^b \frac{dr}{r} = \frac{\mu_0 N i h}{2\pi}\ln\left(\frac{b}{a}\right)
$$

因此，$N$ 匝螺绕环的自感为：

$$
L = \frac{N\Phi_B}{i} = \frac{\mu_0 N^2 h}{2\pi}\ln\left(\frac{b}{a}\right)
$$

---

**3. 无限长直导线与共面矩形线框的互感及互感电动势（Exercise 12.3）**：

- **(a)** 长直导线在距其 $r$ 处产生的磁场垂直于线框平面，大小为 $B(r) = \frac{\mu_0 I}{2\pi r}$。在矩形框内取平行于导线的窄条微元 $dS = a\,dr$（从 $r = c$ 积分至 $r = b + c$），穿过单匝矩形框（$N_2 = 1$）的磁通量为：
  $$
  \Phi_{21} = \int_c^{b+c} \frac{\mu_0 I}{2\pi r} a\,dr = \frac{\mu_0 a I}{2\pi}\ln\left(\frac{b + c}{c}\right) \implies M_{21} = \frac{\Phi_{21}}{I} = \frac{\mu_0 a}{2\pi}\ln\left(\frac{b + c}{c}\right)
  $$
- **(b)** 代入数值 $a = 0.10\text{ m}, \ b = 0.05\text{ m}, \ c = 0.03\text{ m}$ 及 $\frac{\mu_0}{2\pi} = 2 \times 10^{-7}\text{ H/m}$：
  $$
  M = (2 \times 10^{-7}) \times 0.10 \times \ln\left(\frac{5 + 3}{3}\right) = 2 \times 10^{-8}\ln\left(\frac{8}{3}\right)\text{ H} \approx 1.96 \times 10^{-8}\text{ H} = 19.6\text{ nH}
  $$
- **(c)** 当 $\frac{dI}{dt} = 100\text{ A/s}$ 时，互感电动势大小为：
  $$
  |\mathcal{E}| = M\left|\frac{dI}{dt}\right| \approx 1.96 \times 10^{-8}\text{ H} \times 100\text{ A/s} \approx 1.96 \times 10^{-6}\text{ V} = 1.96\ \mu\text{V}
  $$
  **近端边的感应电流方向**：由于直导线电流 $I$ 正在增大（$\frac{dI}{dt} > 0$），穿过矩形框的磁通量增加；根据楞次定律（或反向平行电流相互排斥以阻碍磁通增加），矩形框中靠近直导线的那条近端边上的感应电流方向必与直导线电流 $I$ 的方向**相反**（Opposite to the current $I$ in the wire）。

</details>

<details markdown="1">
<summary>Exercise 12.4: Neumann Formula for Mutual Inductance & Far-Field Dipole Coupling（互感的诺伊曼双线积分公式证明与远场偶极近似）</summary>

**Problem Statement:**
Two circular loops of radii $R_1$ and $R_2$ lie in parallel planes separated by distance $d$. Their centers are on the same axis perpendicular to both planes. Count both currents positive in the same sense about the axis.
(a) Show that the mutual inductance of any two loops can be written in the Neumann form:
$$M = \frac{\mu_0}{4\pi} \oint_{C_1} \oint_{C_2} \frac{d\vec{l}_1 \cdot d\vec{l}_2}{|\vec{r}_1 - \vec{r}_2|}$$
*Hint*: write the flux through loop 2 as $\oint \vec{A}\cdot d\vec{l}_2$ with $\vec{A}(\vec{r}_2) = \frac{\mu_0 i_1}{4\pi}\oint_{C_1} \frac{d\vec{l}_1}{|\vec{r}_1 - \vec{r}_2|}$. First show that $\nabla\times\vec{A}$ equals the magnetic field of loop 1 given by the Biot-Savart law; then use Stokes' theorem.
(b) Show that for the case of $d \gg R_1, R_2$, the mutual inductance is:
$$M \approx \frac{\pi\mu_0}{2d^3} R_1^2 R_2^2$$

---

**中文解析：**

**(a) 磁矢势 $\vec{A}$（Vector Potential）与诺伊曼互感公式（Neumann Formula）的严格证明**：
第一步：验证在场点 $\vec{r}_2$ 处对坐标 $\vec{r}_2$ 求旋度 $\nabla_2 \times \vec{A}(\vec{r}_2)$ 给出毕奥-萨伐尔定律。
将算符 $\nabla_2 \times$ 移入对源点 $\vec{r}_1$ 的线积分号内，应用第四章的标量乘矢量旋度恒等式 $\nabla_2 \times (f\vec{v}) = (\nabla_2 f)\times\vec{v} + f(\nabla_2\times\vec{v})$（此处 $f = \frac{1}{|\vec{r}_2 - \vec{r}_1|}$，且源线元 $\vec{v} = d\vec{l}_1$ 与场点坐标 $\vec{r}_2$ 无关，故 $\nabla_2 \times d\vec{l}_1 = \vec{0}$）：

$$
\nabla_2 \times \left(\frac{d\vec{l}_1}{|\vec{r}_2 - \vec{r}_1|}\right) = \nabla_2\left(\frac{1}{|\vec{r}_2 - \vec{r}_1|}\right) \times d\vec{l}_1 = \left(-\frac{\vec{r}_2 - \vec{r}_1}{|\vec{r}_2 - \vec{r}_1|^3}\right) \times d\vec{l}_1 = \frac{d\vec{l}_1 \times (\vec{r}_2 - \vec{r}_1)}{|\vec{r}_2 - \vec{r}_1|^3}
$$

代回积分式，立即得到回路 1 在 $\vec{r}_2$ 处产生的磁感应强度：

$$
\nabla_2 \times \vec{A}(\vec{r}_2) = \frac{\mu_0 i_1}{4\pi} \oint_{C_1} \frac{d\vec{l}_1 \times (\vec{r}_2 - \vec{r}_1)}{|\vec{r}_2 - \vec{r}_1|^3} = \vec{B}_1(\vec{r}_2)
$$

第二步：利用斯托克斯定理（Stokes' theorem）计算穿过回路 2（边界为 $C_2$，张成曲面为 $S_2$）的磁通量 $\Phi_{21}$：

$$
\Phi_{21} = \int_{S_2} \vec{B}_1(\vec{r}_2) \cdot d\vec{S}_2 = \int_{S_2} (\nabla_2 \times \vec{A}) \cdot d\vec{S}_2 = \oint_{C_2} \vec{A}(\vec{r}_2) \cdot d\vec{l}_2 = \frac{\mu_0 i_1}{4\pi} \oint_{C_1} \oint_{C_2} \frac{d\vec{l}_1 \cdot d\vec{l}_2}{|\vec{r}_1 - \vec{r}_2|}
$$

两边同除以 $i_1$，即证得**诺伊曼公式**（Neumann formula）：

$$
M = \frac{\Phi_{21}}{i_1} = \frac{\mu_0}{4\pi} \oint_{C_1} \oint_{C_2} \frac{d\vec{l}_1 \cdot d\vec{l}_2}{|\vec{r}_1 - \vec{r}_2|}
$$

*（注：由于点乘 $d\vec{l}_1\cdot d\vec{l}_2$ 与距离 $|\vec{r}_1 - \vec{r}_2|$ 关于下标 $1$ 和 $2$ 完全对称，诺伊曼公式从纯几何上直接彰显了互易定理 $M_{12} = M_{21}$！）。*

---

**(b) 远距离（$d \gg R_1, R_2$）下两平行共轴圆环的互感**：
当 $d \gg R_1, R_2$ 时，由第九章 Example 9.1 载流圆环轴线磁场公式可知，圆环 1（通有电流 $i_1$）在距离为 $d$ 的圆环 2 中心处产生的轴向磁场为：

$$
B_1(d) = \frac{\mu_0 i_1 R_1^2}{2(R_1^2 + d^2)^{3/2}} \approx \frac{\mu_0 i_1 R_1^2}{2d^3} \qquad (d \gg R_1)
$$

由于 $R_2 \ll d$，在整个圆环 2 的截面积 $\pi R_2^2$ 上，磁场可视为均匀且等于轴线值 $B_1(d)$。因此穿过圆环 2 的磁通量及互感系数为：

$$
\Phi_{21} \approx (\pi R_2^2) B_1(d) \approx \frac{\pi \mu_0 R_1^2 R_2^2}{2d^3} i_1 \implies M = \frac{\Phi_{21}}{i_1} \approx \frac{\pi \mu_0}{2d^3} R_1^2 R_2^2
$$

</details>

<details markdown="1">
<summary>Exercise 12.5 & 12.6: Linear Current Reversal in Solenoid & Inductive Voltage Spike on Opening Switch（螺线管线性电流反向与断电瞬间的电感高压尖峰）</summary>

**Problem Statement:**
- **Ex 12.5**: A long air-core solenoid of length $l$, area $S$, and $n$ turns/m has negligible resistance. Current is positive when entering at terminal $A$ and leaving at $B$. An ideal current source makes $i(t) = I_0(1 - 2t/T)$ for $0 \le t \le T$ ($I_0, T > 0$). Let $L = \mu_0 n^2 l S$ be its self-inductance.
  (a) Find the self-induced emf $\mathcal{E}_L$ and potential difference $V_A - V_B$. Which terminal is at higher potential, and does this change when $i$ passes through zero?
  (b) Find the magnetic energy $U_B$ at $t = 0, T/2, T$, and the work done by the source on the solenoid during $[0, T/2]$ and $[T/2, T]$.
- **Ex 12.6**: A coil of inductance $L$ and internal resistance $r$ has terminals $A$ and $B$. A resistor $R$ is connected directly between $A$ and $B$. An ideal battery $\mathcal{E}$ is connected between $A$ ($+$) and $B$ ($-$) through a switch. The switch has been closed for a long time and is opened at $t = 0$.
  (a) Just before $t = 0$, find the current through the coil, the current through $R$, and $V_A - V_B$.
  (b) For $t > 0$, find the current through the coil, and find $V_A - V_B$ just after $t = 0$. For which values of $R$ is $|V_A - V_B|$ just after $t = 0$ larger than $\mathcal{E}$?
  (c) Find the heat produced in $R$ after $t = 0$, and show that the total heat produced in $R$ and $r$ equals the initial magnetic energy stored in the coil.

---

**中文解析：**

**1. 线性反向电流驱动下的螺线管端电压与能量吞吐（Exercise 12.5）**：

- **(a)** 电流随时间的变化率为恒定负值：$\frac{di}{dt} = -\frac{2I_0}{T} < 0$。其中 $L = \mu_0 n^2 l S$。
  由自感电动势与端电压公式：
  $$
  \mathcal{E}_L = -L\frac{di}{dt} = +\frac{2LI_0}{T} = \frac{2\mu_0 n^2 l S I_0}{T}, \qquad V_A - V_B = L\frac{di}{dt} = -\frac{2LI_0}{T} < 0
  $$
  由于 $V_A - V_B < 0$（即 $V_B > V_A$），**端子 $B$ 始终处于高电势**！而且因为端电压取决于导数 $\frac{di}{dt}$（在整个 $[0, T]$ 内恒为 $-\frac{2I_0}{T}$）而非电流 $i$ 本身，所以**当 $t = T/2$ 电流穿过零点反号时，高电势端子并不会改变（始终是 $B$ 高于 $A$）**。
- **(b)** 由 $U_B(t) = \frac{1}{2}Li^2(t)$：
  - 在 $t = 0$ 时（$i = +I_0$）：$U_B(0) = \dfrac{1}{2}LI_0^2$；
  - 在 $t = T/2$ 时（$i = 0$）：$U_B(T/2) = 0$；
  - 在 $t = T$ 时（$i = -I_0$）：$U_B(T) = \dfrac{1}{2}L(-I_0)^2 = \dfrac{1}{2}LI_0^2$。
  无阻电感不产生焦耳热，电流源对螺线管所做的功等于磁能的变化量 $W = \Delta U_B$：
  - 在前半段 $0 \le t \le T/2$：$W_{0 \to T/2} = U_B(T/2) - U_B(0) = -\dfrac{1}{2}LI_0^2 < 0$（此时 $i > 0$ 从 $A$ 流向 $B$，但 $V_B > V_A$，电感器把储存的磁能释放回馈给电流源，源做负功）；
  - 在后半段 $T/2 \le t \le T$：$W_{T/2 \to T} = U_B(T) - U_B(T/2) = +\dfrac{1}{2}LI_0^2 > 0$（此时电流反向从 $B$ 流向 $A$，顺着电势降方向，电流源做正功重新为电感器建立反向磁场储能）。

---

**2. 实际电感线圈断电瞬间的反冲高压与焦耳热守恒（Exercise 12.6，经典必考电路题）**：

- **(a) 断开开关前瞬间（$t = 0^-$，直流稳态）**：
  理想电池直接跨接在 $A, B$ 两端，故端电压为 $V_A - V_B = \mathcal{E}$。
  电感器已达稳态（$\frac{di}{dt} = 0$），仅由其内阻 $r$ 限流，故流过线圈的稳恒电流（从 $A$ 到 $B$）和流过并联电阻 $R$ 的电流（从 $A$ 到 $B$）分别为：
  $$
  i_{\text{coil}}(0^-) = i_0 = \frac{\mathcal{E}}{r}, \qquad i_R(0^-) = \frac{\mathcal{E}}{R}, \qquad V_A(0^-) - V_B(0^-) = \mathcal{E}
  $$
- **(b) 断开开关后（$t > 0$）的衰减电流与 $t = 0^+$ 瞬间的反冲端电压**：
  断开开关后，线圈 $(L, r)$ 与外电阻 $R$ 构成串联闭合回路，总电阻为 $R + r$，时间常数为 $\tau = \frac{L}{R + r}$。
  由于电感中的电流不能突变，在 $t = 0^+$ 瞬间线圈电流保持为 $i_{\text{coil}}(0^+) = i_0 = \frac{\mathcal{E}}{r}$（方向仍在线圈内从 $A$ 流向 $B$，然后从端子 $B$ 流出、经外电阻 $R$ 从 $B$ 流向 $A$！）。因此在 $t > 0$ 时：
  $$
  i(t) = \frac{\mathcal{E}}{r} \exp\left(-\frac{R + r}{L}t\right)
  $$
  由于电流在外电阻 $R$ 中是**从 $B$ 流向 $A$** 的，因此在 $t > 0$ 时端子 $A$ 的电势低于端子 $B$：
  $$
  V_A(t) - V_B(t) = -i(t)R = -\frac{R}{r}\mathcal{E} \exp\left(-\frac{R + r}{L}t\right) \implies V_A(0^+) - V_B(0^+) = -\frac{R}{r}\mathcal{E}
  $$
  对比 $\mathcal{E}$ 可知：只要外电阻满足 **$R > r$**，断电瞬间端电压的绝对值 $|V_A(0^+) - V_B(0^+)| = \frac{R}{r}\mathcal{E}$ 就会**大于原电源电动势 $\mathcal{E}$**！（当 $R \gg r$ 时会产生极高的感应过电压尖峰）。
- **(c) 断电后在电阻 $R$ 上产生的焦耳热 $H_R$**：
  因为 $R$ 与线圈内阻 $r$ 串联流过同一个衰减电流 $i(t)$，两者消耗的焦耳热按阻值成正比分配。总耗散焦耳热为：
  $$
  H_{\text{tot}} = \int_0^\infty i^2(t)(R + r)\,dt = \frac{\mathcal{E}^2}{r^2}(R + r) \cdot \frac{L}{2(R + r)} = \frac{1}{2}L\left(\frac{\mathcal{E}}{r}\right)^2 = \frac{1}{2}Li_0^2 = U_B(0)
  $$
  其中外电阻 $R$ 上分得的焦耳热为：
  $$
  H_R = \frac{R}{R + r} H_{\text{tot}} = \frac{R}{R + r} \cdot \frac{L\mathcal{E}^2}{2r^2}
  $$

</details>

<details markdown="1">
<summary>Exercise 12.7, 12.8 & 12.9: Internal Inductance of Solid Coax, Gapped Iron Toroid & Coupled Solenoids（实心同轴电缆内自感辨析、开气隙铁芯螺绕环与同轴双螺线管）</summary>

**Problem Statement:**
- **Ex 12.7**: A long coaxial cable (length $l$) consists of a *solid* inner conductor of radius $a$ (carrying uniform current $I$ along $+z$) and a thin outer shell of radius $b > a$ (carrying $I$ back).
  (a) Find $B(r)$ for $r < a$, $a < r < b$, and $r > b$, and find the magnetic energy stored inside the inner conductor ($r < a$) and between the conductors ($a < r < b$).
  (b) Using $U_B = \frac{1}{2}LI^2$, find the self-inductance $L$ of length $l$.
  (c) A student instead computes the magnetic flux through a flat rectangle of length $l$ extending from $r = 0$ to $r = b$, and divides by $I$. Find the result, and explain why it is not the self-inductance.
- **Ex 12.8**: A thin toroidal iron core (mean circumference $l$, area $S$, linear relative permeability $\mu_r$) has a narrow air gap of width $g \ll \sqrt{S}$ cut across it. $N$ turns carry current $i$. Assume no flux leakage or fringing.
  (a) Explain why the magnitude $B$ is the same in the iron and in the gap, and find $B$.
  (b) Find the self-inductance $L$ of the winding.
  (c) Find the fraction of the stored energy $\frac{1}{2}Li^2$ that is in the gap, and evaluate it for $\mu_r = 5000, \ l = 0.20\text{ m}, \ g = 1.0\text{ mm}$.
- **Ex 12.9**: Two fixed, long, thin-wound solenoids share the $z$ axis and have the same length $l$: inner radius $a$ ($n_1$ turns/m) and outer radius $b > a$ ($n_2$ turns/m).
  (a) Find $L_1, L_2, M_{12}, M_{21}$.
  (b) Currents are brought from $0$ to $I_1, I_2$ along two paths; find the total work done by the two sources in each case.
  (c) Find the final magnetic energy by integrating $\frac{B^2}{2\mu_0}$ over $r < a$ and $a < r < b$, and compare with (b).

---

**中文解析：**

**1. 实心内导体同轴电缆的内自感：磁能法 vs. 朴素磁通法的深刻辨析（Exercise 12.7，核心压轴题）**：

- **(a) 各区域磁场与磁能积分**：
  由第九章同轴电缆安培环路结论，磁场方向沿方位角 $+\hat{\phi}$（逆时针），各区域大小为：
  $$
  B(r) = \begin{cases}
  \dfrac{\mu_0 I r}{2\pi a^2}, & r < a \quad (\text{实心内导体内部}), \\[6pt]
  \dfrac{\mu_0 I}{2\pi r}, & a < r < b \quad (\text{内外导体之间}), \\[6pt]
  0, & r > b \quad (\text{电缆外部}).
  \end{cases}
  $$
  利用磁能密度 $u_B = \frac{B^2}{2\mu_0}$ 在柱壳体积元 $dV = 2\pi r l\,dr$ 上分别积分：
  - **实心内导体内部（$0 \le r < a$）储存的磁能**：
    $$
    U_{\text{in}} = \int_0^a \frac{1}{2\mu_0}\left(\frac{\mu_0 I r}{2\pi a^2}\right)^2 (2\pi r l\,dr) = \frac{\mu_0 l I^2}{4\pi a^4} \int_0^a r^3\,dr = \frac{\mu_0 l I^2}{16\pi}
    $$
  - **两导体之间空腔（$a < r < b$）储存的磁能**：
    $$
    U_{\text{between}} = \int_a^b \frac{1}{2\mu_0}\left(\frac{\mu_0 I}{2\pi r}\right)^2 (2\pi r l\,dr) = \frac{\mu_0 l I^2}{4\pi} \int_a^b \frac{dr}{r} = \frac{\mu_0 l I^2}{4\pi}\ln\left(\frac{b}{a}\right)
    $$
- **(b) 由总磁能 $U_B = U_{\text{in}} + U_{\text{between}} = \frac{1}{2}LI^2$ 求真实总自感 $L$**：
  $$
  U_B = \frac{\mu_0 l I^2}{4\pi}\left[\frac{1}{4} + \ln\left(\frac{b}{a}\right)\right] = \frac{1}{2}LI^2 \implies L = \frac{\mu_0 l}{2\pi}\left[\frac{1}{4} + \ln\left(\frac{b}{a}\right)\right]
  $$
  （其中 $\frac{\mu_0 l}{8\pi}$ 称为实心导线的**内自感** Internal inductance，与半径 $a$ 无关！）。
- **(c) 为什么直接算 $0 \le r \le b$ 矩形截面的磁通量除以 $I$ 会出错？**
  若直接将 $B(r)$ 在 $[0, b]$ 上对 $l\,dr$ 积分求磁通量：
  $$
  \frac{\Phi_{\text{rect}}}{I} = \frac{1}{I}\left[ \int_0^a \frac{\mu_0 I r}{2\pi a^2}l\,dr + \int_a^b \frac{\mu_0 I}{2\pi r}l\,dr \right] = \frac{\mu_0 l}{2\pi}\left[\frac{1}{2} + \ln\left(\frac{b}{a}\right)\right] \neq L
  $$
  可以看到，内自感项变成了 $\frac{1}{2}$ 而不是正确的 $\frac{1}{4}$（多算了一倍）！
  **物理原因**：在实心内导体内部（$0 < r < a$）的磁通微元 $d\Phi(r) = B(r)l\,dr$，**并没有与全部电流 $I$ 发生匝链（Linkage）**，它只包围了半径 $r$ 以内的那一部分电流 $I_{\text{enc}}(r) = I\frac{r^2}{a^2}$（仅占总电流的权重因子 $\frac{r^2}{a^2}$）！如果計入部分匝链权重 $\int_0^a \left(\frac{r^2}{a^2}\right) B(r)l\,dr = \frac{\mu_0 l I}{2\pi a^4}\int_0^a r^3\,dr = \frac{\mu_0 l I}{8\pi}$，结果就与能量法完全一致了。

---

**2. 开气隙铁芯螺绕环的磁路分析与气隙储能占比（Exercise 12.8，工程磁路必考题）**：

- **(a) 为什么铁芯与气隙中的 $B$ 相等？求 $B$**：
  跨接铁芯与气隙的交界面作扁圆柱高斯药盒，由磁场高斯定理 $\oint \vec{B}\cdot d\vec{S} = 0$（且忽略边缘漏磁 Fringing）可知，磁感应强度的法向分量跨界面连续，故**铁芯中的 $B$ 与气隙中的 $B$ 大小严格相等**。
  然而磁场强度 $H = B/\mu$ 在两介质中截然不同：在铁芯中（长度 $l - g$）$H_{\text{iron}} = \frac{B}{\mu_r\mu_0}$；在空气隙中（宽度 $g$）$H_{\text{gap}} = \frac{B}{\mu_0}$。
  沿中心圆周应用关于 $\vec{H}$ 的安培环路定理 $\oint \vec{H}\cdot d\vec{l} = N i$：
  $$
  H_{\text{iron}}(l - g) + H_{\text{gap}} g = \frac{B}{\mu_0}\left(\frac{l - g}{\mu_r} + g\right) = Ni \implies B = \frac{\mu_0 N i}{\dfrac{l - g}{\mu_r} + g}
  $$
- **(b) 绕组的自感 $L$**：
  穿过单匝截面的磁通量为 $\Phi_B = BS$，故自感为：
  $$
  L = \frac{N\Phi_B}{i} = \frac{\mu_0 N^2 S}{\dfrac{l - g}{\mu_r} + g}
  $$
- **(c) 储存在狭窄空气隙中的磁能占总磁能的比例**：
  在气隙中磁能密度为 $u_{\text{gap}} = \frac{B^2}{2\mu_0}$（体积 $Sg$），在铁芯中磁能密度为 $u_{\text{iron}} = \frac{1}{2}BH_{\text{iron}} = \frac{B^2}{2\mu_r\mu_0}$（体积 $S(l - g)$）。因此气隙磁能占比为：
  $$
  f_{\text{gap}} = \frac{U_{\text{gap}}}{U_{\text{tot}}} = \frac{\dfrac{B^2}{2\mu_0}Sg}{\dfrac{B^2}{2\mu_0}Sg + \dfrac{B^2}{2\mu_r\mu_0}S(l - g)} = \frac{g}{g + \dfrac{l - g}{\mu_r}}
  $$
  代入 $\mu_r = 5000, \ l = 0.20\text{ m} = 200\text{ mm}, \ g = 1.0\text{ mm}$（此时 $\frac{l - g}{\mu_r} = \frac{199}{5000}\text{ mm} = 0.0398\text{ mm}$）：
  $$
  f_{\text{gap}} = \frac{1.0}{1.0 + 0.0398} \approx 0.962 = 96.2\%
  $$
  **惊人结论**：尽管空气隙的宽度（$1\text{ mm}$）仅占整个铁芯周长（$200\text{ mm}$）的 $0.5\%$，但由于气隙中 $H_{\text{gap}} = \mu_r H_{\text{iron}}$ 极高，**整个电感器中超过 $96\%$ 的磁场能量实际上都集中储存在这 $1\text{ mm}$ 宽的空气隙之中**！

---

**3. 两个同轴长直螺线管的自感、互感与空间磁能积分验证（Exercise 12.9）**：

- **(a)** 内螺线管截面积为 $\pi a^2$，外螺线管截面积为 $\pi b^2 \ (b > a)$：
  - 各自的自感分别为：$L_1 = \mu_0 n_1^2 \pi a^2 l$，$L_2 = \mu_0 n_2^2 \pi b^2 l$；
  - 计算 $M_{21}$：内管通电 $i_1$ 时，磁场 $B_1 = \mu_0 n_1 i_1$ 仅存在于 $r < a$ 内，故穿过外管单匝的磁通量为 $\Phi_{21} = B_1(\pi a^2) = \mu_0 n_1 \pi a^2 i_1$，外管总匝数 $N_2 = n_2 l$，得 $M_{21} = \frac{N_2\Phi_{21}}{i_1} = \mu_0 n_1 n_2 \pi a^2 l$；
  - 计算 $M_{12}$：外管通电 $i_2$ 时，在整个 $r < b$ 内产生均匀磁场 $B_2 = \mu_0 n_2 i_2$，穿过内管单匝（面积 $\pi a^2$）的磁通量为 $\Phi_{12} = B_2(\pi a^2) = \mu_0 n_2 \pi a^2 i_2$，内管总匝数 $N_1 = n_1 l$，得 $M_{12} = \frac{N_1\Phi_{12}}{i_2} = \mu_0 n_1 n_2 \pi a^2 l = M_{21} = M$。
- **(b)** 由 §5.2 的推导，无论先建立 $I_1$ 再建立 $I_2$，还是先建立 $I_2$ 再建立 $I_1$，计入维持恒流源克服互感电动势所做的附加功 $M I_1 I_2$ 后，两电源所做的总功完全相同：
  $$
  W_{\text{tot}} = \frac{1}{2}L_1 I_1^2 + \frac{1}{2}L_2 I_2^2 + M I_1 I_2 = \frac{1}{2}\mu_0 l \left[ n_1^2 \pi a^2 I_1^2 + n_2^2 \pi b^2 I_2^2 + 2n_1 n_2 \pi a^2 I_1 I_2 \right]
  $$
- **(c) 直接对空间分区域积分磁能密度 $\frac{B^2}{2\mu_0}$**：
  当两管电流分别为 $I_1, I_2$ 时，将空间分为两个有场区域：
  1. **内管内部核心区（$r < a$，体积 $V_1 = \pi a^2 l$）**：两管磁场同向叠加，$B_{\text{core}} = \mu_0(n_1 I_1 + n_2 I_2)$；
  2. **两管之间的环形区（$a < r < b$，体积 $V_2 = \pi(b^2 - a^2)l$）**：内管在此区域无磁场，仅有外管磁场 $B_{\text{annulus}} = \mu_0 n_2 I_2$。
  将两区域的磁能相加并展开合并：
  $$
  \begin{aligned}
  U_B &= \frac{B_{\text{core}}^2}{2\mu_0}(\pi a^2 l) + \frac{B_{\text{annulus}}^2}{2\mu_0}\pi(b^2 - a^2)l \\
  &= \frac{1}{2}\mu_0 l \left[ \pi a^2 (n_1 I_1 + n_2 I_2)^2 + \pi(b^2 - a^2) n_2^2 I_2^2 \right] \\
  &= \frac{1}{2}\mu_0 l \left[ n_1^2 \pi a^2 I_1^2 + 2n_1 n_2 \pi a^2 I_1 I_2 + n_2^2 \pi b^2 I_2^2 \right] = \frac{1}{2}L_1 I_1^2 + M I_1 I_2 + \frac{1}{2}L_2 I_2^2
  \end{aligned}
  $$
  与 (b) 中电源所做的总功完全相等！可以看到，交叉互感能项 $M I_1 I_2$ 的物理起源正是内管核心区（$r < a$）内两磁场叠加平方 $(\vec{B}_1 + \vec{B}_2)^2 = B_1^2 + B_2^2 + 2\vec{B}_1\cdot\vec{B}_2$ 中的**交叉干涉项** $\int \frac{\vec{B}_1\cdot\vec{B}_2}{\mu_0}\,dV$。

</details>