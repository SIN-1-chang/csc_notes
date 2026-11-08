# Chapter 7: DC Circuits（直流电路）

!!! abstract
    General Physics II (Electromagnetism) | 第七章课堂与讲义笔记
    
    参考：
    
    - Lecture 7: *DC Circuits* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 7: *DC Circuits*
    - Halliday, Resnick & Krane, *Physics*, Chapters 30 & 31

## 1 电路基本概念与电动势 (Concepts in Electric Circuits and Emf)

### 1.1 电动势与实际电源模型

**电路**（Electric Circuit）是电荷可以沿着流动的闭合路径。为了使载流子持续流过电阻或灯泡等耗能元件，必须在元件两端维持稳定的电势差。这需要引入**电动势装置**（Emf device，其中 emf 代表 **Electromotive Force**），它通过内部非静电力做功来维持两端端子（Terminals）之间的电势差并为载流子提供能量：

- **化学电池（Battery / Fuel cell）**：依靠内部电化学反应驱动电荷移动；
- **发电机（Electric generator）**：依靠机械力与电磁感应驱动电荷；
- **太阳能电池（Solar cell）**：依靠光能激发驱动电荷。

**电动势的定义**：电动势装置将单位正电荷从低电势端子（负极 $-$）移动到高电势端子（正极 $+$）所做的功称为该装置的**电动势**（Emf，记作 $\mathcal{E}$），其 SI 单位为**伏特**（Volt，$\text{V} = \text{J/C}$）：

$$
\mathcal{E} = \frac{W}{q} \iff dW = \mathcal{E}\,dq
$$

在电路图中，电动势 $\mathcal{E}$ 用一个**从负极（$-$）指向正极（$+$）、尾端带有小圆圈的箭头**表示（以区别于电流箭头）。

| 电源类型 / 工作状态 | 内部结构与电流方向特征 | 端电压（Terminal Voltage）$V_b - V_a$ | 能量转化方向 |
| :--- | :--- | :--- | :--- |
| **理想电源（Ideal emf device）** | 内部对电荷移动无任何阻碍（内阻 $r = 0$） | $V = \mathcal{E}$（恒等于电动势，与电流无关） | 视电流方向而定 |
| **实际电源放电（Discharging）** | 含内阻（Internal resistance）$r > 0$；内部电流**顺着** $\mathcal{E}$ 箭头方向（从 $-$ 到 $+$） | $V = \mathcal{E} - ir < \mathcal{E}$ | 将化学能/其他能转化为电路电能与内阻热能 |
| **实际电源被充电（Charging）** | 外电源驱动电流**逆着** $\mathcal{E}$ 箭头方向（从 $+$ 流入 $-$） | $V = \mathcal{E} + ir > \mathcal{E}$ | 从外电路吸收电能转化为内部化学能及内阻热能 |

### 1.2 电路测量仪表与接地 (Ammeter, Voltmeter and Grounding)

1. **电流表 / 安培计（Ammeter）**：
   用于测量支路中的电流 $i$。必须断开导线将电流表**串联**（In series）接入待测支路中。为了不改变原电路的待测电流，电流表的内阻 $R_A$ 必须远小于电路中的其他电阻（**$R_A \ll R$**；理想电流表 $R_A = 0$）。
2. **电压表 / 伏特计（Voltmeter）**：
   用于测量电路任意两点间的电势差 $V$。必须将电压表两端**并联**（In parallel）跨接在待测元件两端。为了不分流原电路电流从而不改变待测电压，电压表的内阻 $R_V$ 必须远大于待测元件的电阻（**$R_V \gg R$**；理想电压表 $R_V = \infty$）。
3. **电路接地（Grounding a Circuit）**：
   将电路中的某特定节点与大地（地下导电湿润土壤或岩石）相连。由于地球电容极大，吸收或提供电荷时电势几乎不变，因此单点接地**仅意味着将该接地节点的电势规定为零参考点（$V_{\text{ground}} = 0$）**，单一接地线本身没有电流流过，也不会改变电路各支路的电流分布。

---

## 2 电路中的能量守恒与基尔霍夫定律 (Energy Conservation and Kirchhoff's Rules)

### 2.1 电阻的热耗散功率 (Joule Heating / Power Dissipation)

当电子在电场驱动下以恒定的漂移速度 $v_d$ 通过电阻 $R$ 时，其平均动能保持不变，减少的电势能通过电子与晶格分子的频繁碰撞转化为电阻及周围环境的**热能**（Thermal energy，表现为晶格温度升高）。

在时间间隔 $dt$ 内，流过电阻的电荷量为 $dq = i\,dt$，损失的电势能为 $dU = V_R\,dq = i V_R\,dt$。因此，电阻上的**电能耗散功率**（Rate of electrical energy dissipation，单位为瓦特 Watt，$1\text{ W} = 1\text{ V}\cdot\text{A} = 1\text{ J/s}$）为：

$$
P = i V_R = i^2 R = \frac{V_R^2}{R}
$$

对于由理想电源 $\mathcal{E}$ 与单个电阻 $R$ 组成的简单闭合回路，在 $dt$ 时间内电源提供的能量为 $dU_{\text{emf}} = \mathcal{E}\,dq = i\mathcal{E}\,dt$。由能量守恒定律（Conservation of energy），回路总能量变化率为零：

$$
\frac{dU}{dt} = i\mathcal{E} - i^2 R = 0 \implies \mathcal{E} - iR = 0
$$

### 2.2 基尔霍夫两大定律 (Kirchhoff's Circuit Rules)

求解任意复杂多回路直流电路（Multiloop circuits）的普适工具是基尔霍夫两大定律：

**1. 基尔霍夫回路定律（Kirchhoff's Loop Rule / KVL，基于能量守恒与静电场环路定理）**

沿电路中任意闭合回路绕行一周，所经历的各段**电势变化量的代数和恒为零**：

$$
\sum_{\text{closed loop}} \Delta V = 0
$$

使用回路定律时，需先为每条支路预先标定参考电流方向，再任选回路绕行方向（顺时针或逆时针），并严格遵守以下**电势升降符号规则**：

| 跨过的电路元件 | 绕行方向与元件方向的关系 | 电势变化量 $\Delta V = V_{\text{final}} - V_{\text{initial}}$ | 物理原因说明 |
| :--- | :--- | :---: | :--- |
| **电阻 $R$** | **顺着**电流 $i$ 的方向通过电阻 | **$-iR$**（电势降低） | 电流在电阻中总是从高电势流向低电势 |
| **电阻 $R$** | **逆着**电流 $i$ 的方向通过电阻 | **$+iR$**（电势升高） | 逆流而上，从低电势端走向高电势端 |
| **理想电动势 $\mathcal{E}$** | **顺着**电动势 $\mathcal{E}$ 箭头方向（从 $-$ 到 $+$） | **$+\mathcal{E}$**（电势升高） | 正极电势高于负极电势 |
| **理想电动势 $\mathcal{E}$** | **逆着**电动势 $\mathcal{E}$ 箭头方向（从 $+$ 到 $-$） | **$-\mathcal{E}$**（电势降低） | 从高电势正极走向低电势负极 |
| **电容器 $C$** | 从带正电 $+q$ 极板跨越到带负电 $-q$ 极板 | **$-\dfrac{q}{C}$**（电势降低） | 正极板电势高于负极板（反之从 $-$ 到 $+$ 为 $+\dfrac{q}{C}$） |

**2. 基尔霍夫节点定律（Kirchhoff's Junction / Node Rule / KCL，基于稳恒条件下的电荷守恒）**

包围电路中任意一个节点（Node / Junction）作闭合曲面 $S$，在稳恒电流下节点处无电荷堆积，故 $\oint_S \vec{j}\cdot d\vec{S} = 0$。即**流入任意节点的电流之和恒等于流出该节点的电流之和**：

$$
\sum_{\text{in}} i_{\text{in}} = \sum_{\text{out}} i_{\text{out}} \iff \sum_{\alpha} i_\alpha = 0
$$

### 2.3 电阻与电容器的串并联等效对比 (Series and Parallel Combinations)

利用回路定律与节点定律，可将串联（In series）或并联（In parallel）的多个电阻或电容器替换为单一等效元件（$R_{\text{eq}}$ 或 $C_{\text{eq}}$）。两者的记忆口诀与公式对比如下表（Appendix 7A）：

| 组合方式 | 电阻组合（Resistors） | 电容器组合（Capacitors） |
| :--- | :--- | :--- |
| **串联（In Series）** | **特征：等电流（"ser-$i$"，$i$ 处处相同）**<br>总电压 $V = \sum V_j = i\sum R_j$<br>$$R_{\text{eq}} = \sum_{j=1}^n R_j$$ | **特征：等电荷（"seri-$q$"，各极板感应电荷 $q$ 相同）**<br>总电压 $V = \sum V_j = q\sum \frac{1}{C_j}$<br>$$\frac{1}{C_{\text{eq}}} = \sum_{j=1}^n \frac{1}{C_j}$$ |
| **并联（In Parallel）** | **特征：等电压（"par-$V$"，两端电势差 $V$ 相同）**<br>总电流 $i = \sum i_j = V\sum \frac{1}{R_j}$<br>$$\frac{1}{R_{\text{eq}}} = \sum_{j=1}^n \frac{1}{R_j}$$ | **特征：等电压（"par-$V$"，两端电势差 $V$ 相同）**<br>总电荷 $q = \sum q_j = V\sum C_j$<br>$$C_{\text{eq}} = \sum_{j=1}^n C_j$$ |

<details markdown="1">
<summary>课堂经典模型（Example 7.2）：立方体十二电阻网络的体对角线等效电阻</summary>

**问题**：一个正方体框架的 $12$ 条棱上各有一个阻值为 $R$ 的电阻。求正方体两个体对角顶点 $P$ 与 $P'$ 之间的等效电阻 $R_{\text{eq}}$。

**解（对称性电流分配法）**：
假设总电流 $i$ 从顶点 $P$ 流入，并从体对角顶点 $P'$ 流出。立方体绕体对角线 $P\text{-}P'$ 具有三重旋转对称性（Three-fold rotational symmetry）以及过体对角线的镜面反射对称性：

1. **与起点 $P$ 相连的 3 条棱**：由于地位完全等价，流入 $P$ 的总电流 $i$ 必然被这 $3$ 条棱均分，每条棱上的电流均为：
   $$
   i_1 = \frac{i}{3}
   $$
2. **中间层的 6 条棱**：每条从 $P$ 出发的棱到达相邻顶点后，都会分叉进入两条地位完全等价的中间棱，因此流入该顶点的电流 $\frac{i}{3}$ 再次被平分，中间层 $6$ 条棱上的电流均为：
   $$
   i_2 = \frac{1}{2} \times \frac{i}{3} = \frac{i}{6}
   $$
3. **汇入终点 $P'$ 的 3 条棱**：由出入口对称性，最后汇入 $P'$ 的 $3$ 条棱每条各承载电流：
   $$
   i_3 = \frac{i}{6} + \frac{i}{6} = \frac{i}{3}
   $$

任选一条从 $P$ 到 $P'$ 的三步最短路径，计算 $P$ 与 $P'$ 之间的总电势降：

$$
V = i_1 R + i_2 R + i_3 R = \frac{i}{3}R + \frac{i}{6}R + \frac{i}{3}R = \frac{5}{6}iR \implies R_{\text{eq}} = \frac{V}{i} = \frac{5}{6}R
$$

</details>

---

## 3 电容器储能与电场能量密度 (Energy Stored in a Capacitor & Energy Density)

### 3.1 电容器的静电能公式

给电容器充电的过程，本质上是由外力（或电源）克服极板间已建立的电场力，将电子从正极板逐个搬运到负极板的过程。

设在充电过程中的某一瞬时，两极板上已积累的电荷量为 $q'$，此时两极板间的瞬时电势差为 $V' = \frac{q'}{C}$。若继续搬运无穷小电荷微元 $dq'$，外力所需做的元功为：

$$
dW = V'\,dq' = \frac{q'}{C}\,dq'
$$

从初始未充电状态（$q' = 0$）积分至最终带电量 $q$，外力所做的总功全部转化为储存在电容器中的**静电能**（Electric Potential Energy Stored in a Capacitor）：

$$
U = W = \int_0^q \frac{q'}{C}\,dq' = \frac{q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}qV
$$

*注：当极板电荷量 $q$ 固定不变时，宜用 $U = \frac{q^2}{2C}$ 分析；当极板与恒压电源相连使电压 $V$ 固定不变时，宜用 $U = \frac{1}{2}CV^2$ 分析。*

### 3.2 电场的能量密度 (Energy Density of the Electric Field)

静电能究竟储存在哪里？考察忽略边缘效应的平行板电容器（面积 $S$，间距 $d$，电容 $C = \frac{\epsilon_0 S}{d}$，板间匀强电场 $E = \frac{V}{d}$）。将其储能公式改写为：

$$
U = \frac{1}{2}CV^2 = \frac{1}{2}\left(\frac{\epsilon_0 S}{d}\right)(Ed)^2 = \frac{1}{2}\epsilon_0 E^2 (Sd)
$$

注意到 $Sd$ 正好是两极板之间存在电场的空间体积！因此，静电能可视为直接储存在空间电场本身之中。定义单位体积内储存的电场能量为**电场能量密度**（Electric Energy Density，记作 $u_E$ 或 $u$，单位 $\text{J/m}^3$）：

$$
u_E = \frac{1}{2}\epsilon_0 E^2 \quad (\text{真空中}), \qquad u_E = \frac{1}{2}\epsilon E^2 = \frac{1}{2}\kappa\epsilon_0 E^2 = \frac{1}{2}\vec{E}\cdot\vec{D} \quad (\text{线性电介质中})
$$

虽然上式由平行板电容器导出，但它是**对空间任意静电场均普适成立的基本定理**。对于任意空间电场分布 $\vec{E}(\vec{r})$，系统储存的总静电能等于能量密度在全空间的体积分：

$$
U = \int_{\text{all space}} u_E\,d^3r = \int \frac{1}{2}\epsilon_0 E^2\,dV
$$

<details markdown="1">
<summary>课堂双向验证（Examples 7.3 & 7.4）：圆柱形与球形电容器的能量密度积分</summary>

**1. 圆柱形电容器的单位长度储能（Example 7.3）**

设同轴圆柱形电容器内外半径为 $a, b \ (b > a)$，长为 $L$，单位长度带电量为 $\pm\lambda$（总电荷 $q = \lambda L$）。

- **方法 1（直接用电容公式）**：代入第六章结果 $C = \frac{2\pi\epsilon_0 L}{\ln(b/a)}$：
  $$
  \frac{U}{L} = \frac{1}{L}\frac{q^2}{2C} = \frac{\lambda^2 L^2}{2L \cdot \frac{2\pi\epsilon_0 L}{\ln(b/a)}} = \frac{\lambda^2}{4\pi\epsilon_0}\ln\left(\frac{b}{a}\right)
  $$
- **方法 2（空间能量密度积分）**：在 $a < r < b$ 区域内，电场为 $E(r) = \frac{\lambda}{2\pi\epsilon_0 r}$，能量密度为 $u_E(r) = \frac{1}{2}\epsilon_0 E^2 = \frac{\lambda^2}{8\pi^2\epsilon_0 r^2}$。取半径为 $r$、厚为 $dr$、单位长度的薄圆筒体积元 $dV/L = 2\pi r\,dr$ 积分：
  $$
  \frac{U}{L} = \int_a^b u_E(r) \cdot 2\pi r\,dr = \frac{\lambda^2}{4\pi\epsilon_0}\int_a^b \frac{dr}{r} = \frac{\lambda^2}{4\pi\epsilon_0}\ln\left(\frac{b}{a}\right)
  $$

---

**2. 球形电容器的总储能（Example 7.4）**

设同心球形电容器内外半径为 $a, b \ (b > a)$，带电量为 $\pm q$。在 $a < r < b$ 内径向场为 $E(r) = \frac{q}{4\pi\epsilon_0 r^2}$，电势差为 $V = \int_a^b E\,dr = \frac{q(b-a)}{4\pi\epsilon_0 ab}$，故球形电容器电容为 $C = \frac{q}{V} = 4\pi\epsilon_0\frac{ab}{b - a}$。

- **方法 1（直接用电容公式）**：
  $$
  U = \frac{q^2}{2C} = \frac{q^2(b - a)}{8\pi\epsilon_0 ab}
  $$
- **方法 2（空间能量密度积分）**：能量密度为 $u_E(r) = \frac{1}{2}\epsilon_0 E^2 = \frac{q^2}{32\pi^2\epsilon_0 r^4}$。取薄球壳体积元 $dV = 4\pi r^2\,dr$ 在 $[a, b]$ 上积分：
  $$
  U = \int_a^b \left(\frac{q^2}{32\pi^2\epsilon_0 r^4}\right) 4\pi r^2\,dr = \frac{q^2}{8\pi\epsilon_0}\int_a^b \frac{dr}{r^2} = \frac{q^2}{8\pi\epsilon_0}\left(\frac{1}{a} - \frac{1}{b}\right) = \frac{q^2(b - a)}{8\pi\epsilon_0 ab}
  $$
  两种方法结果完全一致（当令 $b \to \infty$ 时，即退化为半径为 $a$ 的孤立导体球静电能 $U = \frac{q^2}{8\pi\epsilon_0 a}$）。

</details>

---

## 4 RC 暂态电路 (RC Circuits: Charging and Discharging)

由电阻 $R$、电容器 $C$ 与理想电源 $\mathcal{E}$ 组成的串联回路称为 **RC 电路**，其中电流 $i(t)$ 与极板电荷 $q(t)$ 随时间发生暂态指数变化。

### 4.1 容性时间常数 ($\tau = RC$)

无论充电还是放电，RC 电路的特征时间尺度均由**容性时间常数**（Capacitive Time Constant，记作 $\tau$）决定。由量纲分析可知：

$$
\tau = RC, \qquad [\tau] = [R][C] = \left(\frac{\text{V}}{\text{A}}\right)\left(\frac{\text{C}}{\text{V}}\right) = \frac{\text{C}}{\text{C/s}} = \text{s}
$$

### 4.2 电容器的充电与放电过程对比

**1. 充电过程（Charging a Capacitor，初始条件 $q(0) = 0$）**

合上开关接通电源 $\mathcal{E}$，电源输出的功率 $i\mathcal{E}$ 一部分被电阻以热功率 $i^2 R$ 耗散，另一部分转化为电容器储能的增长率 $\frac{d}{dt}\left(\frac{q^2}{2C}\right) = \frac{q}{C}\frac{dq}{dt} = i\frac{q}{C}$：

$$
i\mathcal{E} = i^2 R + i\frac{q}{C} \iff R\frac{dq}{dt} + \frac{q}{C} = \mathcal{E} \iff \frac{dq}{dt} + \frac{q}{RC} = \frac{\mathcal{E}}{R}
$$

（该方程同样可由基尔霍夫回路定律 $\mathcal{E} - iR - \frac{q}{C} = 0$ 及 $i = \frac{dq}{dt}$ 直接写出）。结合初始条件 $q(0) = 0$ 积分求解，得到充电过程的电荷、电流与电容电压响应。

**2. 放电过程（Discharging a Capacitor，初始条件 $q(0) = q_0 = C V_0$）**

将已充电至电荷量 $q_0$（电压 $V_0 = q_0/C$）的电容器断开电源，在 $t = 0$ 时刻直接通过电阻 $R$ 短路放电。此时电容器释放能量的速率等于电阻的热耗散功率：

$$
\frac{d}{dt}\left(\frac{q^2}{2C}\right) + i^2 R = 0 \implies R\frac{dq}{dt} + \frac{q}{C} = 0 \iff \frac{dq}{dt} + \frac{q}{RC} = 0
$$

RC 电路充电与放电全套物理量的解析表达式及渐近特征汇总如下表：

| 暂态过程 | 控制微分方程 | 极板电荷量 $q(t)$ | 回路电流 $i(t) = \dfrac{dq}{dt}$ | 电容器端电压 $V_C(t) = \dfrac{q(t)}{C}$ | $t = 0^+$ 与 $t \to \infty$ 的等效特征 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RC 充电**<br>（$q(0) = 0$） | $R\dfrac{dq}{dt} + \dfrac{q}{C} = \mathcal{E}$ | $C\mathcal{E}\left(1 - e^{-t/\tau}\right)$ | $+\dfrac{\mathcal{E}}{R}e^{-t/\tau} = i_0 e^{-t/\tau}$ | $\mathcal{E}\left(1 - e^{-t/\tau}\right)$ | $t=0^+$ 时 $V_C=0$（电容**相当于短路导线**，$i_0 = \mathcal{E}/R$）；<br>$t\to\infty$ 时 $i=0$（电容**相当于断路**，$q \to C\mathcal{E}$） |
| **RC 放电**<br>（$q(0) = q_0$） | $R\dfrac{dq}{dt} + \dfrac{q}{C} = 0$ | $q_0 e^{-t/\tau}$ | $-\dfrac{q_0}{RC}e^{-t/\tau} = -\dfrac{V_0}{R}e^{-t/\tau}$ | $V_0 e^{-t/\tau}$ | 负号表示放电电流方向与原充电电流方向相反；经过 $t = \tau$ 后，电荷与电流均衰减至初值的 $e^{-1} \approx 36.8\%$ |

!!! tip "能量守恒结论：为电容器充电时的 50% 焦耳热损耗铁律"
    当用恒定电动势为 $\mathcal{E}$ 的理想电源通过任意电阻 $R$ 将原本未充电的电容器 $C$ 完全充满（$t \to \infty$，最终电荷 $q_f = C\mathcal{E}$）时：
    - 电源总共做的功为：$W_{\text{battery}} = \int_0^\infty \mathcal{E} i\,dt = \mathcal{E} q_f = C\mathcal{E}^2$；
    - 最终储存在电容器中的静电能为：$U_C = \frac{1}{2}C\mathcal{E}^2$；
    - 电阻上产生的总焦耳热为：$H = \int_0^\infty i^2 R\,dt = \frac{\mathcal{E}^2}{R}\int_0^\infty e^{-2t/(RC)}\,dt = \frac{1}{2}C\mathcal{E}^2$。
    可以看到，**无论串联电阻 $R$ 的阻值取多大，电源输出的总能量中恒有一半（$50\%$）储存在电容器内，另一半（$50\%$）在电阻上转化为焦耳热耗散掉**！

---

## 5 电介质电容器与原子极化微观机制 (Capacitors with Dielectrics & Atomic View)

### 5.1 介电常数、击穿场强与感应束缚电荷

法拉第发现，在电容器两极板间填满绝缘电介质（Dielectric）后，电容会增大为真空时的 $\kappa$ 倍（讲义中记为 $\epsilon_r$，课件中记为 $\kappa \ge 1$，称为**介电常数** Dielectric constant）：

$$
C = \kappa C_{\text{vac}} \qquad (\text{在充满均匀电介质的区域，所有静电公式只需将 } \epsilon_0 \text{ 替换为 } \epsilon = \kappa\epsilon_0)
$$

- **恒定电荷（孤立极板，$q$ 不变）**：插入电介质后，$C$ 增大为 $\kappa C_0$，极板间电场减弱为 $E = \frac{E_0}{\kappa}$，电势差降为 $V = \frac{V_0}{\kappa}$，储能降为 $U = \frac{q^2}{2C} = \frac{U_0}{\kappa}$（减少的能量转化为电介质板被吸入极板间隙时电场力对介质板所做的机械功）。
- **恒定电压（接电源，$V$ 不变）**：插入电介质后，$V$ 不变，$E = V/d$ 不变，但极板自由电荷增大为 $q = \kappa q_0$，储能增大为 $U = \frac{1}{2}CV^2 = \kappa U_0$。
- **介电强度（Dielectric Strength）**：每种电介质所能承受而不被击穿的最大电场强度称为介电强度（单位 $\text{kV/mm}$，如空气约为 $3\text{ kV/mm}$）。一旦外加电场超过该阈值，电介质将发生**电击穿**（Breakdown），内部束缚电子被电离并形成导电通道。

**极化束缚面电荷 $q'$ 与高斯定理（Lecture 7 Slides 31–32）**：
当极板带自由电荷 $\pm q$ 时，电介质上下表面感应出相反符号的束缚电荷 $\mp q'$。在电介质内部，总电场是自由电荷产生的场 $\vec{E}_0$ 与极化电荷产生的反向退极化场 $\vec{E}'$ 的叠加，使总场强减弱为 $E = \frac{E_0}{\kappa}$：

$$
E = \frac{E_0}{\kappa} = \frac{q}{\kappa\epsilon_0 A} = \frac{q - q'}{\epsilon_0 A} \implies q - q' = \frac{q}{\kappa} \implies q' = q\left(1 - \frac{1}{\kappa}\right)
$$

对包围上极板自由电荷 $+q$ 与电介质上表面极化电荷 $-q'$ 的高斯面应用高斯定理，即可写出两种等价形式：

$$
\epsilon_0 \oint_S \vec{E} \cdot d\vec{A} = q_{\text{net}} = q - q' = \frac{q}{\kappa} \iff \oint_S \vec{D} \cdot d\vec{A} = \epsilon_0 \oint_S \kappa\vec{E} \cdot d\vec{A} = q_{\text{free}}
$$

<details markdown="1">
<summary>Appendix 7B: An Atomic View of Dielectrics（有极分子与无极分子电介质的微观极化机制）</summary>

从原子与分子层面看，电介质按分子结构可分为两大类：

1. **有极分子电介质（Type I: Polar Dielectrics，如水 $\text{H}_2\text{O}$）**：
   每个分子本身就具有永久电偶极矩（Permanent electric dipole moment）$\vec{p}$。在无外电场时，由于热运动搅乱，各分子的偶极矩取向完全随机，宏观净极化为零；当施加外电场 $\vec{E}_0$ 后，偶极子受到力矩 $\vec{\tau} = \vec{p}\times\vec{E}_0$ 作用，倾向于顺着外电场方向排列（取向极化）。
2. **无极分子电介质（Type II: Nonpolar Dielectrics，如稀有气体、$\text{O}_2, \text{Si}$ 等）**：
   在无外电场时，分子的正负电荷中心重合，无永久偶极矩；当置于外电场 $\vec{E}_0$ 中时，外电场使原子核与电子云发生相对位移畸变（位移极化），感应出顺着外电场方向的感生电偶极矩 $\vec{p}$。

**宏观退极化场效应**：无论是取向极化还是位移极化，均匀电介质板内部相邻分子的正负端彼此中和（体束缚电荷 $\rho_b = 0$），但在电介质靠近正极板的左表面会露出一层负束缚电荷（$-q'$），在靠近负极板的右表面露出一层正束缚电荷（$+q'$）。这两层表面束缚电荷在介质内部建立起一个**与外加电场 $\vec{E}_0$ 方向相反的附加电场 $\vec{E}'$**，从而削弱了介质内部的合电场 $\vec{E} = \vec{E}_0 + \vec{E}'$（模长降为 $E_0/\kappa$）。

</details>

---

## 6 Chapter 7 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 7.1, 7.2 & 7.3: Coaxial Energy, Tunable Resistor Bridge & Wheatstone Bridge（同轴圆柱储能、可调电桥最小电流与惠斯通电桥）</summary>

**Problem Statement:**
- **Ex 7.1**: A metallic cylinder (radius $a$, length $l$) and a coaxial metallic cylindrical shell (radius $b$, length $l$) have vacuum between $a < r < b$. The inner cylinder carries $+Q$ and the outer shell $-Q$ (ignore boundary effects). (a) What is the energy density $u_E$ at radius $r \ (a < r < b)$? (b) What is the total potential energy $U$ of the system? (c) What is the capacitance $C$ of the system?
- **Ex 7.2**: Consider a DC circuit composed of 4 resistors and an ideal emf $\mathcal{E}$ (`Figure 7.6`: triangle $ABC$ with $r_1$ on $AB$, $r_3$ on $AC$, potentiometer $r_4$ on $BC$; central branch from $A$ has $\mathcal{E}$ and $r_2$ connected to sliding contact $D$ on $r_4$). Let $x$ be the resistance of the part of $r_4$ between $B$ and $D$, and assume $r_4 \ge |r_1 - r_3|$. Find the value of $x$ for which the current $i$ in the branch $AD$ is smallest, and that smallest current.
- **Ex 7.3**: Consider the Wheatstone bridge (`Figure 7.7`: $\mathcal{E}$ and $r_0$ in main branch between $A$ and $B$; bridge arms $AC=r_1, AD=r_2, CB=r_3, DB=r_4$, and central galvanometer resistor $CD=r_g$). Take $I$ positive from $C$ to $D$. (a) Compute the current $I$ going through $r_g$. (b) What is the condition for $I$ to be zero?

---

**中文解析：**

**1. 同轴圆柱电容器的能量密度、总储能与电容（Exercise 7.1）**：

- **(a)** 由高斯定理，在 $a < r < b$ 处径向电场为 $E(r) = \frac{Q}{2\pi\epsilon_0 l r}$，故电场能量密度为：
  $$
  u_E(r) = \frac{1}{2}\epsilon_0 E^2(r) = \frac{Q^2}{8\pi^2\epsilon_0 l^2 r^2}
  $$
- **(b)** 对 $a < r < b$ 的圆柱壳体积元 $dV = 2\pi r l\,dr$ 积分求总静电能：
  $$
  U = \int_a^b u_E(r) 2\pi r l\,dr = \frac{Q^2}{4\pi\epsilon_0 l}\int_a^b \frac{dr}{r} = \frac{Q^2}{4\pi\epsilon_0 l}\ln\left(\frac{b}{a}\right)
  $$
- **(c)** 由 $U = \frac{Q^2}{2C}$ 直接反解电容：
  $$
  C = \frac{Q^2}{2U} = \frac{2\pi\epsilon_0 l}{\ln(b/a)}
  $$

---

**2. 滑动变阻器分流网络的最小干路电流（Exercise 7.2）**：
触头 $D$ 将底边电阻 $r_4$ 分为左段 $R_{BD} = x$ 与右段 $R_{DC} = r_4 - x$。观察拓扑结构可知，从节点 $A$ 到节点 $D$ 之间有两条并联外支路：
- 左支路 $A \to B \to D$ 的总电阻为 $R_L(x) = r_1 + x$；
- 右支路 $A \to C \to D$ 的总电阻为 $R_R(x) = r_3 + r_4 - x$。

这两条支路并联后再与中间支路 $AD$（含电源 $\mathcal{E}$ 与内阻 $r_2$）串联闭合。因此，$AD$ 支路中的总电流为：

$$
i(x) = \frac{\mathcal{E}}{r_2 + R_{\parallel}(x)}, \qquad \text{其中 } R_{\parallel}(x) = \frac{(r_1 + x)(r_3 + r_4 - x)}{(r_1 + x) + (r_3 + r_4 - x)} = \frac{(r_1 + x)(r_3 + r_4 - x)}{r_1 + r_3 + r_4}
$$

要使电流 $i(x)$ 最小，必须使并联等效电阻 $R_{\parallel}(x)$ 最大。由于分母 $(r_1 + x) + (r_3 + r_4 - x) = r_1 + r_3 + r_4$ 为定值，根据均值不等式，当分子中的两个正因子相等时乘积取得最大值：

$$
r_1 + x = r_3 + r_4 - x \implies x = \frac{r_3 + r_4 - r_1}{2}
$$

（由题设条件 $r_4 \ge |r_1 - r_3|$，易验证 $0 \le x \le r_4$ 恒成立，触头 $D$ 落在 $r_4$ 范围内）。
此时最大并联电阻为 $R_{\parallel,\max} = \frac{(r_1 + r_3 + r_4)^2 / 4}{r_1 + r_3 + r_4} = \frac{r_1 + r_3 + r_4}{4}$，对应的最小干路电流为：

$$
i_{\min} = \frac{\mathcal{E}}{r_2 + \dfrac{r_1 + r_3 + r_4}{4}} = \frac{4\mathcal{E}}{4r_2 + r_1 + r_3 + r_4}
$$

---

**3. 惠斯通电桥（Wheatstone Bridge）检流计电流与平衡条件（Exercise 7.3）**：

- **(a)** 设通过 $r_1$（$A\to C$）、$r_2$（$A\to D$）的电流分别为 $i_1, i_2$，通过桥支路 $r_g$（$C\to D$）的电流为 $I$。由节点定律知：通过 $r_3$（$C\to B$）的电流为 $i_1 - I$，通过 $r_4$（$D\to B$）的电流为 $i_2 + I$，通过电源干路（$B\to A$）的总电流为 $i_1 + i_2$。
  对三个独立回路列出基尔霍夫回路方程（KVL）：
  1. 左三角回路 $A \to C \to D \to A$：$-i_1 r_1 - I r_g + i_2 r_2 = 0 \implies i_2 r_2 - i_1 r_1 = I r_g$
  2. 右三角回路 $C \to B \to D \to C$：$-(i_1 - I)r_3 + (i_2 + I)r_4 + I r_g = 0 \implies -i_1 r_3 + i_2 r_4 + I(r_3 + r_4 + r_g) = 0$
  3. 外侧底回路 $A \to D \to B \to A$：$\mathcal{E} - (i_1 + i_2)r_0 - i_2 r_2 - (i_2 + I)r_4 = 0 \implies i_1 r_0 + i_2(r_0 + r_2 + r_4) + I r_4 = \mathcal{E}$

  由式 (1)、(2) 将 $i_1, i_2$ 用 $I$ 表示并代入式 (3) 消元（或直接应用克莱姆法则 / 戴维南等效定理），解得流过检流计 $r_g$ 的电流精确通式为：
  $$
  I = \frac{\mathcal{E}(r_2 r_3 - r_1 r_4)}{r_0\left[(r_1 + r_3)(r_2 + r_4) + r_g(r_1 + r_2 + r_3 + r_4)\right] + r_g(r_1 + r_3)(r_2 + r_4) + r_1 r_3(r_2 + r_4) + r_2 r_4(r_1 + r_3)}
  $$
- **(b) 电桥平衡条件（Condition for $I = 0$）**：
  令分子为零，立得电桥平衡充要条件：
  $$
  r_2 r_3 - r_1 r_4 = 0 \iff r_1 r_4 = r_2 r_3 \iff \frac{r_1}{r_2} = \frac{r_3}{r_4}
  $$
  （物理意义：当上下两条支路的分压比相等时，$C, D$ 两点电势相等 $V_C = V_D$，桥支路中无电流通过，且该平衡条件与电源内阻 $r_0$ 及检流计内阻 $r_g$ 完全无关）。

</details>

<details markdown="1">
<summary>Exercise 7.4 & 7.5: Single-Loop & Multi-Branch RC Charging Transients（单回路与含分流支路的 RC 暂态充电演化）</summary>

**Problem Statement:**
- **Ex 7.4**: Consider the RC circuit in `Figure 7.8` (an ideal emf $\mathcal{E}$, resistor $r_1$, and capacitor $C$ in a single series loop with a switch). The capacitor was not charged before the switch was closed at $t = 0$. Let $Q$ be the magnitude of the charge on either plate. What is the time dependence of $Q$ at time $t > 0$?
- **Ex 7.5**: Consider the RC circuit shown in `Figure 7.9` (bottom branch has ideal emf $\mathcal{E}$ in series with $r_1$ and switch; middle branch has resistor $r_2$ in parallel; top branch has capacitor $C$ in series with resistor $r_3$). The capacitor is uncharged when the switch is closed at $t = 0$. Find the time dependence of $Q$ for $t > 0$, and its limit as $t \to \infty$.

---

**中文解析：**

**1. 标准单回路 RC 充电过程（Exercise 7.4）**：
闭合开关后，由基尔霍夫回路定律得 $\mathcal{E} - i r_1 - \frac{Q}{C} = 0$，将 $i = \frac{dQ}{dt}$ 代入得：

$$
r_1 \frac{dQ}{dt} + \frac{Q}{C} = \mathcal{E}
$$

结合初始条件 $Q(0) = 0$，解得极板电荷随时间的演化规律为：

$$
Q(t) = C\mathcal{E}\left(1 - e^{-\frac{t}{r_1 C}}\right) \qquad (t > 0)
$$

---

**2. 含并联分流电阻的多回路 RC 充电过程（Exercise 7.5，高频必考题型）**：
设流过电容支路（含 $C$ 和 $r_3$）的充电电流为 $i_3 = \frac{dQ}{dt}$，流过中间并联电阻 $r_2$ 的电流为 $i_2$。由节点定律，流过底部电源支路（含 $\mathcal{E}$ 和 $r_1$）的干路总电流为 $i_1 = i_2 + i_3$。

列出两个独立回路的基尔霍夫回路方程（KVL）：
1. 下方回路（含 $\mathcal{E}, r_1, r_2$）：
   $$
   \mathcal{E} - (i_2 + i_3)r_1 - i_2 r_2 = 0 \implies i_2 = \frac{\mathcal{E} - i_3 r_1}{r_1 + r_2}
   $$
2. 上方外圈回路（或由并联节点电压 $V_{\text{node}} = i_2 r_2 = i_3 r_3 + \frac{Q}{C}$）：
   $$
   i_3 r_3 + \frac{Q}{C} = i_2 r_2 = \frac{r_2}{r_1 + r_2}(\mathcal{E} - i_3 r_1)
   $$

将含 $i_3 = \frac{dQ}{dt}$ 的项移至等式左侧合并：

$$
\left(r_3 + \frac{r_1 r_2}{r_1 + r_2}\right)\frac{dQ}{dt} + \frac{Q}{C} = \frac{r_2}{r_1 + r_2}\mathcal{E}
$$

定义等效电阻 $R_{\text{eq}}$、等效电动势 $\mathcal{E}_{\text{eq}}$ 与时间常数 $\tau$：

$$
R_{\text{eq}} = r_3 + \frac{r_1 r_2}{r_1 + r_2} = \frac{r_1 r_2 + r_1 r_3 + r_2 r_3}{r_1 + r_2}, \qquad \mathcal{E}_{\text{eq}} = \frac{r_2}{r_1 + r_2}\mathcal{E}, \qquad \tau = R_{\text{eq}} C
$$

代入初始条件 $Q(0) = 0$，立即解得 $Q(t)$ 及其稳态极限（$t \to \infty$）：

$$
Q(t) = \frac{r_2}{r_1 + r_2}C\mathcal{E}\left[1 - \exp\left(-\frac{(r_1 + r_2)t}{(r_1 r_2 + r_1 r_3 + r_2 r_3)C}\right)\right], \qquad \lim_{t \to \infty} Q(t) = \frac{r_2}{r_1 + r_2}C\mathcal{E}
$$

*（物理直观验证：当 $t \to \infty$ 时，电容器充满断路 $i_3 = 0$，电路退化为 $r_1$ 与 $r_2$ 简单串联分压，电容器两端电压恰等于 $r_2$ 上的分压 $V_2 = \frac{r_2}{r_1 + r_2}\mathcal{E}$）。*

</details>

<details markdown="1">
<summary>Exercise 7.6, 7.7 & 7.8: Ammeter/Voltmeter Error Analysis, Grounding Shift & Parallel Batteries（伏安法内外接误差分析、接地点平移与双电池并联充放电）</summary>

**Problem Statement:**
- **Ex 7.6**: An unknown resistor $R$ is measured with an ammeter ($R_A$) and a voltmeter ($R_V$), powered by a battery ($\mathcal{E}, r$). The measured resistance is $R_m = V/i$. In connection (i) the voltmeter is connected across $R$ only (ammeter outside). In connection (ii) the voltmeter is connected across both the ammeter and $R$ (ammeter inside).
  (a) Find $R_m$ for each connection. Does it depend on $\mathcal{E}$ or $r$?
  (b) Find the relative error $(R_m - R)/R$ for each connection, and the value $R^*$ of $R$ at which the two errors have equal magnitudes. Which connection gives the smaller error when $R > R^*$?
- **Ex 7.7**: An ideal emf $\mathcal{E} > 0$ is connected between $A$ and $B$ (arrow from $A$ to $B$). Branch 1 from $B$ to $A$ contains $R_1$, node $C$, and $R_2$; Branch 2 contains $R_3$.
  (a) Find $i_{12}$, $i_3$, $i$, and $R_{\text{eq}} = \mathcal{E}/i$.
  (b) Node $A$ is grounded; find $V_A, V_B, V_C$. The ground is then moved from $A$ to $C$; find the three potentials again. Which quantities in (a) change?
  (c) Show that the power supplied by $\mathcal{E}$ equals the total power dissipated in the three resistors.
- **Ex 7.8**: Two batteries ($\mathcal{E}_1, r_1$) and ($\mathcal{E}_2, r_2$) are connected in parallel with their positive terminals joined to one end of a load resistor $R > 0$.
  (a) Find the current $i_R$ through $R$, and the current $i_2$ leaving battery 2.
  (b) Find the condition on $\mathcal{E}_2$ under which battery 2 is being charged ($i_2 < 0$). What does the condition become when $R \to \infty$ and when $\mathcal{E}_1 = \mathcal{E}_2$?

---

**中文解析：**

**1. 伏安法测电阻的电流表外接法 (i) 与内接法 (ii) 误差分析（Exercise 7.6）**：

- **(a)**
  - **接法 (i)（电流表外接法，电压表直接并联在 $R$ 两端）**：电压表读数 $V$ 为 $R$ 两端真实电压，但电流表读数 $i = i_R + i_V = \frac{V}{R} + \frac{V}{R_V}$ 包含了电压表的分流。故测量值为：
    $$
    R_m^{(i)} = \frac{V}{i} = \frac{1}{\frac{1}{R} + \frac{1}{R_V}} = \frac{R R_V}{R + R_V}
    $$
  - **接法 (ii)（电流表内接法，电压表跨接在电流表和 $R$ 串联整体两端）**：电流表读数 $i$ 为流过 $R$ 的真实电流，但电压表读数 $V = i(R + R_A)$ 包含了电流表的分压。故测量值为：
    $$
    R_m^{(ii)} = \frac{V}{i} = R + R_A
    $$
  两种接法下的 $R_m$ **均与电源电动势 $\mathcal{E}$ 和电源内阻 $r$ 完全无关**。
- **(b) 相对误差与临界电阻 $R^*$**：
  - 接法 (i) 相对误差（测量值偏小）：$\delta_{(i)} = \dfrac{R_m^{(i)} - R}{R} = -\dfrac{R}{R + R_V}$；
  - 接法 (ii) 相对误差（测量值偏大）：$\delta_{(ii)} = \dfrac{R_m^{(ii)} - R}{R} = +\dfrac{R_A}{R}$。
  令两者绝对值相等：
  $$
  \frac{R^*}{R^* + R_V} = \frac{R_A}{R^*} \implies (R^*)^2 - R_A R^* - R_A R_V = 0 \implies R^* = \frac{R_A + \sqrt{R_A^2 + 4R_A R_V}}{2} \quad (\approx \sqrt{R_A R_V})
  $$
  当待测电阻较大（**$R > R^*$**）时，$\delta_{(ii)} = \frac{R_A}{R}$ 随 $R$ 增大而减小，而 $|\delta_{(i)}|$ 随 $R$ 增大而增大，故**接法 (ii)（电流表内接法）的误差更小**（口诀：“大内偏大，小外偏小”）。

---

**2. 双支路并联电路、接地点平移与功率平衡验证（Exercise 7.7）**：

- **(a)** $A, B$ 间电势差为 $\mathcal{E}$。支路 1 总电阻为 $R_1 + R_2$，支路 2 电阻为 $R_3$：
  $$
  i_{12} = \frac{\mathcal{E}}{R_1 + R_2}, \qquad i_3 = \frac{\mathcal{E}}{R_3}, \qquad i = i_{12} + i_3 = \mathcal{E}\left(\frac{1}{R_1 + R_2} + \frac{1}{R_3}\right), \qquad R_{\text{eq}} = \frac{(R_1 + R_2)R_3}{R_1 + R_2 + R_3}
  $$
- **(b) 接地点平移**：
  - 当节点 $A$ 接地时：$V_A = 0$，$V_B = \mathcal{E}$，$V_C = V_A + i_{12} R_2 = \dfrac{R_2}{R_1 + R_2}\mathcal{E}$。
  - 当接地点移至节点 $C$ 时（所有节点电势整体平移 $-\frac{R_2}{R_1 + R_2}\mathcal{E}$）：
    $$
    V_C' = 0, \qquad V_A' = -\frac{R_2}{R_1 + R_2}\mathcal{E}, \qquad V_B' = +\frac{R_1}{R_1 + R_2}\mathcal{E}
    $$
  **(a) 中求出的所有电流（$i_{12}, i_3, i$）以及等效电阻 $R_{\text{eq}}$ 均完全不变**（因为电流只取决于电势差，与电势零点的选取无关）。
- **(c) 功率守恒验证**：
  三个电阻耗散的总热功率为：
  $$
  P_{\text{diss}} = i_{12}^2 R_1 + i_{12}^2 R_2 + i_3^2 R_3 = i_{12}^2(R_1 + R_2) + i_3^2 R_3 = \frac{\mathcal{E}^2}{R_1 + R_2} + \frac{\mathcal{E}^2}{R_3} = \mathcal{E}(i_{12} + i_3) = i\mathcal{E} = P_{\text{emf}}
  $$

---

**3. 双电池并联供电与电池反充条件（Exercise 7.8）**：

- **(a)** 设两电池正极汇合端与负极汇合端（即负载电阻 $R$ 两端）的电势差为 $V = i_R R$。由回路定律知两电池支路的电流分别为 $i_1 = \frac{\mathcal{E}_1 - i_R R}{r_1}$ 和 $i_2 = \frac{\mathcal{E}_2 - i_R R}{r_2}$。代入节点定律 $i_R = i_1 + i_2$：
  $$
  i_R = \frac{\mathcal{E}_1}{r_1} + \frac{\mathcal{E}_2}{r_2} - i_R R\left(\frac{1}{r_1} + \frac{1}{r_2}\right) \implies i_R = \frac{\mathcal{E}_1 r_2 + \mathcal{E}_2 r_1}{r_1 r_2 + R(r_1 + r_2)}
  $$
  将 $i_R$ 代回 $i_2 = \frac{\mathcal{E}_2 - i_R R}{r_2}$ 通分化简，得流过电池 2 的电流：
  $$
  i_2 = \frac{\mathcal{E}_2(r_1 + R) - \mathcal{E}_1 R}{r_1 r_2 + R(r_1 + r_2)}
  $$
- **(b) 电池 2 被充电的条件（$i_2 < 0$）**：
  由于分母恒正，令分子小于零即得：
  $$
  \mathcal{E}_2 < \frac{R}{r_1 + R}\mathcal{E}_1
  $$
  - 当移除外负载（$R \to \infty$）时：$\frac{R}{r_1 + R} \to 1$，条件简化为 $\mathcal{E}_2 < \mathcal{E}_1$（高电动势电池直接给低电动势电池充电）；
  - 当 $\mathcal{E}_1 = \mathcal{E}_2$ 时：由于 $\frac{R}{r_1 + R} < 1$，不等式 $\mathcal{E}_2 < \frac{R}{r_1 + R}\mathcal{E}_2$ 绝无可能成立，即两个相同电动势的电池并联接负载时绝不会发生相互反充。

</details>

<details markdown="1">
<summary>Exercise 7.9 & 7.10: Capacitor Plate Force via Virtual Work & Two-Capacitor Discharge（虚功原理求极板引力及双电容放电能量损耗）</summary>

**Problem Statement:**
- **Ex 7.9**: A parallel-plate capacitor in vacuum has plates of area $S$ separated by $x$. The lower plate is fixed, and the upper plate is moved slowly by $dx$. Let $F$ be the electric force on the upper plate (positive in the direction of increasing $x$).
  (a) The plates are isolated and carry charges $\pm q$. Find $U(x)$, and from the change of $U$ in $dx$, find $F$.
  (b) The plates are instead connected to an ideal battery that keeps their potential difference at $V$. Find $U(x)$, and the work $dW_b$ done by the battery when $x$ increases by $dx$. Explain why $F = -dU/dx$ now gives the wrong sign, find $F$ from energy conservation, and compare with (a).
- **Ex 7.10**: Two ideal capacitors $C_1, C_2$ have their lower plates joined ($V = 0$). Initially their upper plates are isolated at potentials $V_1 > V_2 \ge 0$ (charges $C_1 V_1$ and $C_2 V_2$). At $t = 0$ a switch joins the two upper plates through a resistor $R > 0$.
  (a) Using charge conservation, find the final common potential $V_f$ and final charges $q_1, q_2$.
  (b) Find $i(t)$, $q_1(t)$, $q_2(t)$ for $t \ge 0$, and the time constant $\tau$.
  (c) Find the initial energy $U_i$, final energy $U_f$, and heat $H = \int_0^\infty i^2 R\,dt$ produced in $R$. Show that $H = U_i - U_f$, and that $H$ does not depend on $R$.

---

**中文解析：**

**1. 平行板电容器极板间引力的虚功原理分析：孤立恒流源 vs. 恒压源（Exercise 7.9，经典必考压轴题）**：

- **(a) 极板孤立（电荷量 $q$ 恒定）**：
  电容为 $C(x) = \frac{\epsilon_0 S}{x}$，故储存的静电能为：
  $$
  U(x) = \frac{q^2}{2C(x)} = \frac{q^2 x}{2\epsilon_0 S}
  $$
  由于系统与外界无电荷及电能交换，当上极板缓慢移动 $dx$ 时，电场力对上极板所做的功等于系统静电能的减少量 $F\,dx = -dU$：
  $$
  F = -\frac{dU}{dx} = -\frac{q^2}{2\epsilon_0 S} \qquad (\text{负号表示上极板受到向下的吸引力})
  $$
  *（注：这与第五章 Exercise 5.7 由静电压强 $P = \frac{\sigma^2}{2\epsilon_0}$ 乘以面积 $S$ 得到的结果完全一致！）*
- **(b) 极板接恒压电源（电压 $V$ 恒定）**：
  此时储存的静电能写为：
  $$
  U(x) = \frac{1}{2}C(x)V^2 = \frac{\epsilon_0 S V^2}{2x}
  $$
  当间距 $x$ 增大 $dx$ 时，电容减小 $dC = -\frac{\epsilon_0 S}{x^2}dx$，极板上的电荷量变化为 $dq = V\,dC = -\frac{\epsilon_0 S V}{x^2}dx < 0$（即有电荷 $|dq|$ 退回电源，电源做负功）。电源在此过程中所做的功为：
  $$
  dW_b = V\,dq = -\frac{\epsilon_0 S V^2}{x^2}dx = 2\,dU
  $$
  **为什么此时 $F = -dU/dx$ 会给出错误的正号？**
  因为公式 $F = -dU/dx$ 仅适用于**孤立系统**（无外界电源做功 $dW_b = 0$）。当连接电源时，系统不再孤立！由完整的功能原理（外力做功 $F_{\text{ext}}\,dx = -F\,dx$ 加上电源做功 $dW_b$ 等于储能变化 $dU$）：
  $$
  -F\,dx + dW_b = dU \implies F = \frac{dW_b - dU}{dx} = -\frac{\epsilon_0 S V^2}{2x^2} = -\frac{q^2}{2\epsilon_0 S}
  $$
  可以看到，计入电源做功 $dW_b = 2\,dU$ 后，实际的静电力 $F$ 与 (a) 中完全相同（因为瞬时静电力仅取决于当时的极板电荷状态，与极板是否连着导线无关）。

---

**2. 双电容器通过电阻互连放电的暂态演化与能量耗散（Exercise 7.10）**：

- **(a) 最终稳态电压 $V_f$ 与最终电荷**：
  由两上极板总电荷守恒，任意时刻均有 $q_1(t) + q_2(t) = C_1 V_1 + C_2 V_2$。当 $t \to \infty$ 达到稳态时，电流降为零，两电容上极板达到共同电势 $V_f$：
  $$
  (C_1 + C_2)V_f = C_1 V_1 + C_2 V_2 \implies V_f = \frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}
  $$
  最终电荷量分别为 $q_1(\infty) = C_1 V_f = \dfrac{C_1(C_1 V_1 + C_2 V_2)}{C_1 + C_2}$，$q_2(\infty) = C_2 V_f = \dfrac{C_2(C_1 V_1 + C_2 V_2)}{C_1 + C_2}$。
- **(b) 暂态电流 $i(t)$、电荷 $q_1(t), q_2(t)$ 与时间常数 $\tau$**：
  由于电流 $i(t)$ 从 $C_1$ 上极板流向 $C_2$ 上极板，故有：
  $$
  i(t) = -\frac{dq_1}{dt} = +\frac{dq_2}{dt}
  $$
  对闭合回路应用基尔霍夫回路定律（KVL）：
  $$
  \frac{q_1(t)}{C_1} - i(t)R - \frac{q_2(t)}{C_2} = 0
  $$
  两边对时间 $t$ 求导，并将 $\frac{dq_1}{dt} = -i, \ \frac{dq_2}{dt} = +i$ 代入：
  $$
  R\frac{di}{dt} + \left(\frac{1}{C_1} + \frac{1}{C_2}\right)i = 0 \implies \frac{di}{dt} + \frac{i}{\tau} = 0, \qquad \text{其中等效时间常数 } \tau = \frac{C_1 C_2}{C_1 + C_2}R = C_{\text{series}}R
  $$
  结合初始电流 $i(0) = \frac{V_1 - V_2}{R}$，立即解得：
  $$
  i(t) = \frac{V_1 - V_2}{R} e^{-t/\tau}
  $$
  对 $i(t)$ 积分可得两极板电荷量随时间的演化：
  $$
  \begin{aligned}
  q_1(t) &= C_1 V_1 - \int_0^t i(t')\,dt' = \frac{C_1(C_1 V_1 + C_2 V_2)}{C_1 + C_2} + \frac{C_1 C_2(V_1 - V_2)}{C_1 + C_2} e^{-t/\tau} \\
  q_2(t) &= C_2 V_2 + \int_0^t i(t')\,dt' = \frac{C_2(C_1 V_1 + C_2 V_2)}{C_1 + C_2} - \frac{C_1 C_2(V_1 - V_2)}{C_1 + C_2} e^{-t/\tau}
  \end{aligned}
  $$
- **(c) 初始储能、终态储能与电阻焦耳热积分**：
  - 初始总静电能：$U_i = \frac{1}{2}C_1 V_1^2 + \frac{1}{2}C_2 V_2^2$；
  - 终态总静电能：$U_f = \frac{1}{2}(C_1 + C_2)V_f^2 = \frac{(C_1 V_1 + C_2 V_2)^2}{2(C_1 + C_2)}$；
  - 直接积分计算电阻 $R$ 上产生的总焦耳热 $H$：
    $$
    H = \int_0^\infty i^2(t) R\,dt = \frac{(V_1 - V_2)^2}{R} \int_0^\infty e^{-2t/\tau}\,dt = \frac{(V_1 - V_2)^2}{R} \cdot \frac{\tau}{2} = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2
    $$
  另一方面，计算初末静电能之差：
  $$
  U_i - U_f = \frac{1}{2}C_1 V_1^2 + \frac{1}{2}C_2 V_2^2 - \frac{(C_1 V_1 + C_2 V_2)^2}{2(C_1 + C_2)} = \frac{C_1 C_2(V_1^2 - 2V_1 V_2 + V_2^2)}{2(C_1 + C_2)} = \frac{1}{2}\frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2 = H
  $$
  由此严格证得 $H = U_i - U_f$，且总耗散热量 $H$ **与连接电阻 $R$ 的阻值大小完全无关**（$R$ 越小，放电峰值电流越大但持续时间 $\tau$ 越短，积分总热量恒定不变）。

</details>