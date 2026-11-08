# Chapter 9: Magnetic Field of a Current（电流的磁场）

!!! abstract
    General Physics II (Electromagnetism) | 第九章课堂与讲义笔记
    
    参考：
    
    - Lecture 9: *Magnetic Field of a Current* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 9: *Magnetic Field of a Current*
    - Halliday, Resnick & Krane, *Physics*, Chapter 33

## 1 毕奥-萨伐尔定律与电流间的磁场力 (Biot-Savart Law and Force Between Currents)

### 1.1 毕奥-萨伐尔定律 (The Biot-Savart Law)

静止电荷产生不随时间变化的静电场（Electrostatics），而**稳恒电流**（Steady current）则产生不随时间变化的稳恒磁场，这一理论称为**静磁学**（Magnetostatics）。两者的关键区别在于：产生电场的电荷微元 $dq$ 是**标量**（Scalar），而产生磁场的**电流元**（Current-length element）$i\,d\vec{l}$（课件中亦记为 $i\,d\vec{s}$）则是**矢量**（Vector）。

实验表明，电流元 $i\,d\vec{l}$ 在距离为 $r$ 的空间点 $P$ 处产生的微元磁场 $d\vec{B}$ 遵循平方反比律，称为**毕奥-萨伐尔定律**（Biot-Savart Law）：

$$
d\vec{B} = \frac{\mu_0}{4\pi} \frac{i\,d\vec{l} \times \vec{r}}{r^3} = \frac{\mu_0}{4\pi} \frac{i\,d\vec{l} \times \hat{r}}{r^2}
$$

公式中各物理量的定义与方向准则如下：

- $\vec{r}$：从电流元 $i\,d\vec{l}$ 指向场点 $P$ 的位置矢量（$\hat{r} = \vec{r}/r$ 为对应的单位矢量）；若点 $P$ 恰位于电流元延长线上（$\theta = 0$ 或 $\pi$），则 $d\vec{l}\times\vec{r} = \vec{0}$，$d\vec{B} = \vec{0}$；
- $\mu_0$：**真空磁导率**（Permeability constant / Vacuum permeability）：
  $$
  \mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A} = 4\pi \times 10^{-7}\text{ N/A}^2
  $$
- **右手握线定则（Right-hand grip rule / Curled-straight right-hand rule）**：用右手握住载流导线，伸直的大拇指指向电流 $i$ 的方向，四指自然弯曲的方向即为磁感线环绕的方向（对于弯曲导线，需对每一小段电流元分别应用叉乘 $i\,d\vec{l}\times\vec{r}$ 再积分叠加）。

### 1.2 两个基础积分模型：载流圆环与无限长直导线

**1. 载流圆环轴线上的磁场（Example 9.1: A Circular Ring Carrying Current $i$）**

设半径为 $a$ 的细圆环置于 $xy$ 平面内，圆心在原点，通有逆时针方向的稳恒电流 $i$（从 $+z$ 轴往下看）。求 $z$ 轴上 $(0, 0, z)$ 处的磁场 $\vec{B}$：

1. **取微元与叉乘**：在柱坐标 $(r, \theta, z)$ 下，取方位角 $\theta \to \theta + d\theta$ 处的电流元 $d\vec{l} = \hat{\theta}\,a\,d\theta$。从电流元指向轴线点 $P(0, 0, z)$ 的矢量为 $\vec{r} = -a\hat{r} + z\hat{z}$，距离为 $r = \sqrt{a^2 + z^2}$。利用正交基矢叉乘关系 $\hat{\theta}\times\hat{r} = -\hat{z}$ 与 $\hat{\theta}\times\hat{z} = +\hat{r}$：
   $$
   d\vec{B} = \frac{\mu_0}{4\pi} \frac{i\hat{\theta}\,a\,d\theta \times (-a\hat{r} + z\hat{z})}{(a^2 + z^2)^{3/2}} = \frac{\mu_0 i a\,d\theta}{4\pi(a^2 + z^2)^{3/2}}(a\hat{z} + z\hat{r})
   $$
2. **对称性抵消与积分**：绕圆环积分一周（$\theta \in [0, 2\pi]$），径向分量 $z\hat{r}$ 成对完全抵消，仅剩沿 $+z$ 轴的分量：
   $$
   \vec{B}(0, 0, z) = \hat{z} \frac{\mu_0 i a^2}{4\pi(a^2 + z^2)^{3/2}} \int_0^{2\pi} d\theta = \frac{\mu_0 i a^2}{2(a^2 + z^2)^{3/2}}\hat{z}
   $$
   （注：当 $z = 0$ 时，环心磁场为 $B = \frac{\mu_0 i}{2a}$；当远场 $z \gg a$ 时，注意到圆环磁矩 $\mu = i(\pi a^2)$，上式化为 $\vec{B} \approx \frac{\mu_0}{2\pi}\frac{\vec{\mu}}{|z|^3}$，这与电偶极子在轴线上的远场 $\vec{E} = \frac{1}{2\pi\epsilon_0}\frac{\vec{p}}{|z|^3}$ 形式完全对应！）。

**2. 无限长载流直导线的磁场（Example 9.2: Infinitely Long Straight Wire）**

设无限长直导线沿 $z$ 轴放置，通有沿 $+z$ 方向的电流 $i$。求距导线垂直距离为 $R$（讲义记为 $x$）的点 $P(x, 0, 0)$ 处的磁场：

1. **取微元**：在位置 $z \to z+dz$ 处取电流元 $i\,d\vec{l} = i\,dz\,\hat{z}$，到点 $P$ 的位移矢量为 $\vec{r} = x\hat{x} - z\hat{z}$，距离 $r = \sqrt{x^2 + z^2}$。由于 $\hat{z}\times\hat{x} = \hat{y}$ 且 $\hat{z}\times\hat{z} = \vec{0}$，所有微元在 $P$ 点产生的磁场均沿 $+\hat{y}$ 方向（切向环绕导线）：
   $$
   d\vec{B} = \frac{\mu_0}{4\pi} \frac{i\hat{z}\,dz \times (x\hat{x} - z\hat{z})}{(x^2 + z^2)^{3/2}} = \hat{y} \frac{\mu_0 i x\,dz}{4\pi(x^2 + z^2)^{3/2}}
   $$
2. **积分求解**：令 $z = x\tan\alpha \ (\alpha \in (-\pi/2, \pi/2))$，或利用课件中的角度换元 $\sin\theta = x/r$（$\int_{-\infty}^{+\infty} \frac{x\,dz}{(x^2+z^2)^{3/2}} = \frac{1}{x}\int_0^\pi \sin\theta\,d\theta = \frac{2}{x}$）：
   $$
   \vec{B} = \hat{y} \frac{\mu_0 i x}{4\pi} \int_{-\infty}^{+\infty} \frac{dz}{(x^2 + z^2)^{3/2}} = \frac{\mu_0 i}{2\pi x}\hat{y} \iff B = \frac{\mu_0 i}{2\pi R}
   $$
   （若为半无限长直导线，积分区间为 $[0, \infty)$，在端点垂线上的磁场大小减半为 $B = \frac{\mu_0 i}{4\pi R}$）。

### 1.3 两平行载流直导线间的相互作用力与“安培”的定义

设两根无限长平行直导线 $a$ 和 $b$ 相距为 $d$，分别通有稳恒电流 $i_a$ 和 $i_b$。计算导线 $a$ 对导线 $b$（取长度为 $L$ 的一段）所施加的磁场力，分为两步：

1. **先求场**：导线 $a$ 在导线 $b$ 所在位置产生的磁感应强度大小为 $B_a = \frac{\mu_0 i_a}{2\pi d}$，方向垂直于两导线构成的平面；
2. **再求力**：通有电流 $i_b$ 的导线 $b$ 在磁场 $\vec{B}_a$ 中受到安培力 $\vec{F}_{ba} = i_b\vec{L}\times\vec{B}_a$，单位长度所受磁力大小为：
   $$
   \frac{F_{ba}}{L} = \frac{\mu_0 i_a i_b}{2\pi d}
   $$
   由右手定则可知：**同向平行电流相互吸引（Parallel currents attract），反向平行电流相互排斥（Antiparallel currents repel）**。

!!! note "计量学常识：SI 基本单位“安培（Ampere）”的定义演变"
    - **旧定义（1948–2019 年）**：在真空中相距 $d = 1\text{ m}$ 的两根无限长平行细直导线，若通以相等的恒定电流，当每米导线长度上所受作用力恰好为 $2 \times 10^{-7}\text{ N/m}$ 时，该电流定义为 $1\text{ A}$。这一定义人为将真空磁导率精确锁定为 $\mu_0 \equiv 4\pi \times 10^{-7}\text{ N/A}^2$。
    - **现行定义（2019 年起至今）**：通过将元电荷的值精确固定为 $e = 1.602176634 \times 10^{-19}\text{ C}$ 来定义安培（$1\text{ A} = 1\text{ C/s}$），而真空磁导率 $\mu_0$ 则变为一个由实验测定的物理量（在 $10^{-10}$ 相对精度内仍等于 $4\pi \times 10^{-7}\text{ N/A}^2$）。

---

## 2 安培环路定理及其对称性应用 (Ampère's Law and Symmetric Applications)

### 2.1 磁场环流与安培环路定理

对于无限长载流直导线产生的圆形磁场 $\vec{B} = \frac{\mu_0 i}{2\pi r}\hat{\phi}$，考察任意闭合路径（称为**安培环路** Amperian loop）$C$ 上的线积分 $\oint_C \vec{B}\cdot d\vec{l}$。由于线元在方位角方向的分量为 $dl_\phi = r\,d\phi$，故 $\vec{B}\cdot d\vec{l} = \frac{\mu_0 i}{2\pi}\,d\phi$：

- 若闭合路径 $C$ 沿右手螺旋方向单次包围导线（$\Delta\phi = 2\pi$），则环流（Circulation）恒为 $\oint_C \vec{B}\cdot d\vec{l} = \mu_0 i$（与路径形状及离导线的远近无关：越远虽然场强按 $1/r$ 减弱，但路径周长按 $r$ 成正比变长，两者精确抵消）；
- 若闭合路径不包围导线（$\Delta\phi = 0$），则环流为零；若路径绕导线 $m$ 圈（计入正负号），则环流为 $m\mu_0 i$。

将这一结果推广至任意稳恒电流分布，即得到静磁学基本定律——**安培环路定理**（Ampère's Law）：

$$
\oint_C \vec{B} \cdot d\vec{l} = \mu_0 i_{\text{enc}} = \mu_0 \sum_{\text{enc}} i = \mu_0 \int_S \vec{j} \cdot d\vec{S}
$$

其中 $i_{\text{enc}}$ 为安培环路 $C$ 所包围（穿过以 $C$ 为边界的任意张成曲面 $S$）的**净电流代数和**。

**包围电流的正负号右手定则（Sign Convention，Example 9.3）**：
弯曲右手四指使其顺着安培环路 $C$ 的积分绕行方向（Direction of integration），伸直的大拇指所指方向即为正方向：

- 与大拇指方向一致穿出环路的电流计为**正**（$+i$）；
- 与大拇指方向相反穿入环路的电流计为**负**（$-i$）；
- **未被安培环路包围的外部电流**（尽管它们对环路各点上的局域场强 $\vec{B}$ 有贡献）对环流积分 $\oint_C \vec{B}\cdot d\vec{l}$ 的**净贡献恒为零**！

!!! warning "对称性分析的重要差异：磁场 $\vec{B}$ 在镜面反射下的轴矢量性质"
    在应用安培环路定理前，需先通过对称性确定 $\vec{B}$ 的方向。讲义（Section 9.2）特别提醒：由于磁场 $\vec{B}$ 是由叉乘 $i\,d\vec{l}\times\vec{r}$ 构造的**赝矢量 / 轴矢量**（Pseudovector / Axial vector），当电流分布关于某镜面对称时，镜像点处的磁场 $\vec{B}$ **垂直于镜面的分量保持不变，而平行于镜面的分量方向反转**——这与真矢量电场 $\vec{E}$ 的镜面反射规律恰好相反！如果不确定方向，最稳妥的方法是直接用毕奥-萨伐尔定律叉乘判别。

### 2.2 四大高度对称体系的安培环路求解

当稳恒电流分布具有柱对称、平面对称或螺线管/螺绕环对称性时，可选取适当的安培环路 $C$ 秒解磁场分布：

**1. 无限长圆柱形载流导线的内外磁场（Example 9.4：半径为 $R$，均匀通有总电流 $i$）**

由柱对称性，磁感线为同心圆，取半径为 $r$ 的同心圆作为安培环路（$\oint \vec{B}\cdot d\vec{l} = 2\pi r B$）：

- **导线外部（$r \ge R$）**：包围全部电流 $i_{\text{enc}} = i$，故 $2\pi r B = \mu_0 i \implies B(r) = \dfrac{\mu_0 i}{2\pi r}$（按 $1/r$ 衰减）。
- **导线内部（$r < R$）**：电流密度均匀（$j = \frac{i}{\pi R^2}$），安培环路包围的电流按截面积之比缩放为 $i_{\text{enc}} = i\frac{\pi r^2}{\pi R^2} = i\frac{r^2}{R^2}$，故：
  $$
  2\pi r B = \mu_0 i \frac{r^2}{R^2} \implies B(r) = \frac{\mu_0 i}{2\pi R^2} r \qquad (\text{在导线内部随 } r \text{ 线性增长})
  $$

**2. 无限大均匀载流平板 / 运动电荷薄板（Example 9.5: A Sheet / Slab of Moving Charge）**

设无限大平板厚度为 $w \ (-w/2 \le y \le w/2)$，内部载流子浓度为 $n$、电荷大小为 $e$、定向漂移速率为 $v$，形成沿 $+z$（或垂直纸面向外）的均匀体电流密度 $j = nev$（对应单位宽度的**面电流密度** Surface current density 为 $J_s = jw = nevw$）。
由平面对称性，磁场 $\vec{B}$ 平行于平板且垂直于电流方向，在平板上下两侧等大反向。跨接平板作长边为 $a$（平行于 $\vec{B}$）、短边垂直于平板的矩形安培环路：

- **平板外部（$|y| \ge w/2$）**：$\oint \vec{B}\cdot d\vec{l} = 2Ba = \mu_0(jwa) = \mu_0 J_s a$，解得：
  $$
  B_{\text{outside}} = \frac{1}{2}\mu_0 J_s = \frac{1}{2}\mu_0 nevw \qquad (\text{处处恒定，与距平板的距离无关，类比于无限大带电平板 } E = \frac{\sigma}{2\epsilon_0})
  $$
- **平板内部（$|y| < w/2$）**：取上下长边位于 $\pm y$ 处的对称矩形环路，包围厚度为 $2|y|$，故 $2Ba = \mu_0 j(2|y|a) \implies B_{\text{inside}}(y) = \mu_0 j |y| = \mu_0 nev|y|$。

**3. 理想无限长螺线管（Example 9.6: Infinitely Long Solenoid）**

**螺线管**（Solenoid）是由导线紧密缠绕而成的长螺旋线圈（长度远大于直径）。在理想无限长密绕螺线管极限下，绕组可视为纯粹绕轴环流的圆柱面电流层：

- **管外磁场为零（$\vec{B}_{\text{outside}} = \vec{0}$）**：由于无轴向电流故无方位角分量 $B_\phi$；由磁通连续性知无径向分量 $B_r$；在管外取矩形安培环路知轴向分量 $B_z$ 为常数，结合无穷远处场强为零，可知**理想长直螺线管外部磁场处处为零**。
- **管内匀强磁场（$\vec{B}_{\text{inside}}$）**：取矩形安培环路 $abcda$，使边 $ab$（长为 $h$ 或 $a$）位于管内平行于轴线，边 $cd$ 位于管外（$B = 0$），两条垂直短边与管内轴向磁场垂直无贡献。设单位长度匝数为 $n$，则环路包围 $nh$ 匝线圈，净电流为 $i_{\text{enc}} = nih$：
  $$
  \oint_{abcda} \vec{B}\cdot d\vec{l} = Bh = \mu_0 (nih) \implies B = \mu_0 n i
  $$
  即**理想螺线管内部是平行于轴线的匀强磁场**（大小仅取决于单位长度匝数 $n$ 与电流 $i$，与螺线管的直径、总长度及管内距轴线的位置均无关，其在磁学中的地位正如平行板电容器在电学中的地位）。

**4. 环形螺线管 / 螺绕环（Example 9.7: Toroid / Torus）**

将长螺线管弯曲首尾相接形成中空圆环（甜甜圈形状），称为**螺绕环**（Toroid / Torus），总匝数为 $N$，通有电流 $i$。由旋转对称性，磁感线为环管内部的同心圆。取半径为 $r$ 的同心圆作为安培环路：

- **在环管内部空腔中**：安培环路包围全部 $N$ 匝内圈导线，$i_{\text{enc}} = Ni$，故：
  $$
  (B)(2\pi r) = \mu_0 N i \implies B(r) = \frac{\mu_0 N i}{2\pi r} \qquad (\text{注意：螺绕环截面上的磁场不均匀，与半径 } r \text{ 成反比})
  $$
- **在中心空洞区（$r < R_{\text{inner}}$）与环管外部（$r > R_{\text{outer}}$）**：安培环路包围的净电流为零（外部环路同时穿过内圈 $N$ 匝与外圈反向 $N$ 匝，正负抵消），故 **$B = 0$**。

| 对称电流模型 | 安培环路选取 | 环路积分方程 | 磁感应强度大小 $B$ |
| :--- | :--- | :--- | :--- |
| **无限长圆柱直导线**（半径 $R$，电流 $i$） | 半径为 $r$ 的同心圆 | $2\pi r B = \mu_0 i_{\text{enc}}$ | $B = \begin{cases} \dfrac{\mu_0 i r}{2\pi R^2}, & r < R \\ \dfrac{\mu_0 i}{2\pi r}, & r \ge R \end{cases}$ |
| **无限大均匀电流薄片**（面电流密度 $J_s$） | 跨接薄片的矩形回路（宽 $a$） | $2Ba = \mu_0 J_s a$ | $B = \dfrac{1}{2}\mu_0 J_s$（两侧反向匀强场） |
| **理想无限长螺线管**（单位长度 $n$ 匝，电流 $i$） | 一边在管内、一边在管外的矩形 | $Bh = \mu_0 (nh)i$ | 管内 $B = \mu_0 n i$（匀强），管外 $B = 0$ |
| **理想螺绕环（Toroid）**（总匝数 $N$，电流 $i$） | 半径为 $r$ 的同心圆 | $2\pi r B = \mu_0 N i$ | 管内 $B = \dfrac{\mu_0 N i}{2\pi r}$，管外及中心孔 $B = 0$ |

---

## 3 安培定理的微分形式与磁场高斯定理 (Differential Forms & Gauss' Law for Magnetism)

### 3.1 斯托克斯定理与安培环路定理的微分形式 ($\nabla\times\vec{B} = \mu_0\vec{j}$)

根据矢量分析中的**斯托克斯定理**（Stokes' Theorem，又称旋度基本定理 Fundamental theorem for curls，见 Appendix 9B），任意矢量场 $\vec{A}$ 沿闭合路径 $C$ 的环流等于其旋度穿过以 $C$ 为边界的任意曲面 $S$ 的通量（曲面法向 $d\vec{S}$ 与路径 $C$ 方向满足右手螺旋定则）：

$$
\oint_C \vec{A} \cdot d\vec{l} = \int_S (\nabla \times \vec{A}) \cdot d\vec{S}
$$

将斯托克斯定理应用于安培环路定理左侧 $\oint_C \vec{B}\cdot d\vec{l} = \mu_0 \int_S \vec{j}\cdot d\vec{S}$，移项得：

$$
\int_S \left(\nabla \times \vec{B} - \mu_0 \vec{j}\right) \cdot d\vec{S} = 0
$$

由于该式对任意闭合路径 $C$ 所张成的任意曲面 $S$ 均恒成立，被积函数必须处处为零，从而得到**安培环路定理的微分形式**：

$$
\nabla \times \vec{B}(\vec{r}) = \mu_0 \vec{j}(\vec{r})
$$

*（物理说明：在稳恒电流条件下，连续性方程 $\nabla\cdot\vec{j} = 0$ 保证了穿过以同一回路 $C$ 为边界的任意不同曲面的总电流 $\int_S \vec{j}\cdot d\vec{S}$ 完全相等；而在非稳恒的时变情况下，$\nabla\cdot\vec{j} = -\partial_t \rho \neq 0$，不同曲面上的电流积分不再相等，这促使麦克斯韦引入了位移电流 Displacement current 并建立了完整的麦克斯韦方程组）。*

### 3.2 磁场的散度与磁场高斯定理 ($\nabla\cdot\vec{B} = 0$)

对于连续分布的体电流密度 $\vec{j}(\vec{r}')$，将电流元 $i\,d\vec{l}$ 替换为 $\vec{j}(\vec{r}')\,d^3r'$，毕奥-萨伐尔定律写为：

$$
\vec{B}(\vec{r}) = \frac{\mu_0}{4\pi} \int \frac{\vec{j}(\vec{r}') \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3}\,d^3r'
$$

对场点坐标 $\vec{r} = (x, y, z)$ 求散度 $\nabla\cdot\vec{B}$，并将算符 $\nabla$ 移入积分号内。利用第四章的叉乘散度恒等式 $\nabla\cdot(\vec{C}\times\vec{D}) = (\nabla\times\vec{C})\cdot\vec{D} - \vec{C}\cdot(\nabla\times\vec{D})$：

1. 因为源电流密度 $\vec{j}(\vec{r}')$ 仅依赖于源点坐标 $\vec{r}' = (x', y', z')$，与场点坐标 $\vec{r} = (x, y, z)$ 无关，故 $\nabla_{\vec{r}} \times \vec{j}(\vec{r}') = \vec{0}$；
2. 注意到 $\dfrac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|^3} = -\nabla_{\vec{r}}\left(\frac{1}{|\vec{r} - \vec{r}'|}\right)$ 正好是一个标量函数的梯度（即点电荷电势的梯度），而**任何梯度的旋度恒等于零**：$\nabla_{\vec{r}} \times \left(\frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|^3}\right) = -\nabla_{\vec{r}} \times \nabla_{\vec{r}}\left(\frac{1}{|\vec{r} - \vec{r}'|}\right) = \vec{0}$！

因此，被积函数恒为零，我们严格证得**磁场的高斯定理（微分形式与积分形式）**：

$$
\nabla \cdot \vec{B} = 0 \iff \Phi_B = \oint_S \vec{B} \cdot d\vec{A} = \int_V (\nabla \cdot \vec{B})\,dV = 0
$$

- **物理内涵**：穿过任意闭合高斯面 $S$ 的**净磁通量（Net magnetic flux）恒等于零**。这在数学上严格表述了“**自然界中不存在磁单极子（Magnetic monopoles do not exist）**，磁感线永远是无头无尾的闭合曲线”。
- **普适性**：与电场高斯定理 $\nabla\cdot\vec{E}(\vec{x}, t) = \rho(\vec{x}, t)/\epsilon_0$ 一样，磁场高斯定理 $\nabla\cdot\vec{B}(\vec{x}, t) = 0$ 是麦克斯韦方程组的四大基本方程之一，对随时间变化的动态磁场同样严格成立。

### 3.3 静磁学与静电学基本规律全面对比

| 理论维度 | 静电学（Electrostatics） | 静磁学（Magnetostatics） |
| :--- | :--- | :--- |
| **基本场源微元** | 标量电荷元 $dq$ | 矢量电流元 $i\,d\vec{s}$（或 $\vec{j}\,dV$） |
| **基本实验叠加定律** | **库仑定律**：$d\vec{E} = \dfrac{1}{4\pi\epsilon_0}\dfrac{dq\,\hat{r}}{r^2}$ | **毕奥-萨伐尔定律**：$d\vec{B} = \dfrac{\mu_0}{4\pi}\dfrac{i\,d\vec{s}\times\hat{r}}{r^2}$ |
| **散度与通量定理（Gauss' Law）** | $\oint_S \vec{E}\cdot d\vec{A} = \dfrac{q_{\text{enc}}}{\epsilon_0} \iff \nabla\cdot\vec{E} = \dfrac{\rho}{\epsilon_0}$（有源场） | $\oint_S \vec{B}\cdot d\vec{A} = 0 \iff \nabla\cdot\vec{B} = 0$（无源场，无磁单极） |
| **旋度与环流定理（Circulation）** | $\oint_C \vec{E}\cdot d\vec{s} = 0 \iff \nabla\times\vec{E} = \vec{0}$（无旋保守场） | **安培环路定理**：$\oint_C \vec{B}\cdot d\vec{s} = \mu_0 i_{\text{enc}} \iff \nabla\times\vec{B} = \mu_0\vec{j}$（有旋场） |

<details markdown="1">
<summary>Appendices 9A & 9B: 旋度的几何意义（小叶轮旋转判据）与斯托克斯定理</summary>

**1. 旋度的几何意义与常见误区辨析（Appendix 9A: Geometrical Meaning of Curl）**

- **物理图像**：矢量场的旋度 $\nabla\times\vec{v}$ 度量了场围绕某点发生旋转或环流（Circulate / Swirl）的趋势。如果把矢量场看作流体流速场，并在某点放入一个微小的浮体或小叶轮（Paddlewheel），**只要该点处的旋度 $\nabla\times\vec{v} \neq \vec{0}$，小浮体就会开始绕自身中心自转**！
- **常见误区**：不要以为“流线弯曲才有旋度，流线平直就没有旋度”。旋度不仅取决于流线的曲率（Curvature），还取决于场强大小在垂直于流线方向上的剪切变化（Shear variation）：
  - **平直流线但旋度非零**（如 Lecture 9 Slide 34 图 b，$\vec{v} = -ky\hat{x}$）：虽然所有流线都是平行于 $x$ 轴的直线，但由于上下两侧流速不等（产生剪切力差），放入其中的小浮体依然会发生旋转（$\nabla\times\vec{v} = k\hat{z} \neq \vec{0}$）；
  - **辐射直线且旋度为零**（如点电荷径向场 $\vec{E} \propto \hat{r}/r^2$）：处处满足 $\nabla\times\vec{E} = \vec{0}$，称为**无旋场**（Irrotational field）。

---

**2. 斯托克斯定理与电势存在性回顾（Appendix 9B: Stokes' Theorem）**

斯托克斯定理 $\int_S (\nabla\times\vec{v})\cdot d\vec{A} = \oint_P \vec{v}\cdot d\vec{s}$ 表明：曲面上所有微观涡旋（Curl）的总通量，完全等于沿着曲面边界闭合路径 $P$ 的宏观环流。
将其应用于静电场 $\vec{E}$：正是因为处处有 $\nabla\times\vec{E} = \vec{0}$，才保证了沿任意闭合回路 $\oint \vec{E}\cdot d\vec{s} = 0$（积分与路径无关），从而使我们能够单值地定义静电势 $V(\vec{r}) \equiv -\int_O^{\vec{r}} \vec{E}\cdot d\vec{s}$。

</details>

---

## 4 Chapter 9 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 9.1 & 9.2: Three-Segment Bent Wire & Rotating Charged Spherical Shell（三段折线导线磁场与旋转带电球壳内外磁场）</summary>

**Problem Statement:**
- **Ex 9.1**: Three straight leads carry a current $I$ in the directions shown in `Figure 9.8`. The middle lead has length $l$. The two outer leads are semi-infinite; each is joined to one end of the middle lead, lies on the side of it away from $P$, and makes an angle of $45^\circ$ with the line of the middle lead. The foot of the perpendicular dropped from $P$ onto the middle lead is a distance $a$ from its left end ($0 < a < l$), and $P$ is a distance $b$ from the lead. Calculate the magnitude and direction of the magnetic field at point $P$.
- **Ex 9.2**: A sphere with radius $R$ has a uniform charge distribution on its surface, carrying a total charge $Q$. The center of the sphere is at the origin, and the sphere is rotating around the $z$ axis with angular velocity $\omega$ in a counterclockwise fashion, as seen from the positive $z$ axis. Calculate the magnitude of the magnetic field at point $(0, 0, z)$ for both $|z| < R$ and $|z| > R$.

---

**中文解析：**

**1. 三段折线导线在点 $P$ 产生的合磁场（Exercise 9.1）**：
以点 $P$ 到中间导线的垂足为原点 $(0, 0, 0)$，令中间导线沿 $x$ 轴从左端点 $A(-a, 0)$ 延伸至右端点 $B(l-a, 0)$（电流沿 $+\hat{x}$ 方向），点 $P$ 位于 $(0, -b, 0)$，纸面外法向为 $+\hat{z}$。分别用毕奥-萨伐尔定律计算三段导线的贡献（以**垂直纸面向里 $-\hat{z}$** 为正方向）：

1. **中间直导线段 $AB$**：
   点 $P$ 到 $AB$ 的垂直距离为 $b$，左端点 $A$ 和右端点 $B$ 到原点的距离分别为 $a$ 和 $l-a$（斜边距离分别为 $r_1 = \sqrt{a^2 + b^2}$ 和 $r_2 = \sqrt{(l-a)^2 + b^2}$）。由有限长直导线公式，磁场方向垂直纸面向里（$-\hat{z}$），大小为：
   $$
   B_{\text{mid}} = \frac{\mu_0 I}{4\pi b}\left( \frac{a}{\sqrt{a^2 + b^2}} + \frac{l - a}{\sqrt{(l - a)^2 + b^2}} \right)
   $$
2. **左侧半无限长引线（从左上方以 $45^\circ$ 流入端点 $A(-a, 0)$）**：
   沿电流方向（指向 $A$）的单位矢量为 $\hat{u}_1 = \frac{1}{\sqrt{2}}(\hat{x} - \hat{y})$，从 $A$ 指向 $P$ 的矢量为 $\vec{R}_1 = a\hat{x} - b\hat{y} \ (r_1 = \sqrt{a^2 + b^2})$。
   点 $P$ 到该引线所在直线的有向垂直距离（对应向里 $-\hat{z}$ 方向）为 $d_1 = (-\hat{z})\cdot(\hat{u}_1\times\vec{R}_1) = \frac{b - a}{\sqrt{2}}$，且沿引线方向投影为 $-\hat{u}_1\cdot\vec{R}_1 = -\frac{a + b}{\sqrt{2}}$。代入半无限长导线公式 $B = \frac{\mu_0 I}{4\pi d_\perp}(1 - \cos\alpha_1) = \frac{\mu_0 I d_\perp}{4\pi r_1(r_1 - \vec{R}_1\cdot\hat{u}_{\text{ray}})}$，得向里分量为：
   $$
   B_{\text{left}} = \frac{\mu_0 I}{4\pi} \frac{b - a}{\sqrt{a^2 + b^2}\left(\sqrt{2(a^2 + b^2)} + a + b\right)} = \frac{\mu_0 I}{4\pi(b - a)}\left( \sqrt{2} - \frac{a + b}{\sqrt{a^2 + b^2}} \right)
   $$
3. **右侧半无限长引线（从端点 $B(l-a, 0)$ 向右上方以 $45^\circ$ 流出）**：
   由左右镜像对称性，只需将左引线公式中的 $a$ 替换为 $l - a$，即得向里分量为：
   $$
   B_{\text{right}} = \frac{\mu_0 I}{4\pi} \frac{b - (l - a)}{\sqrt{(l - a)^2 + b^2}\left(\sqrt{2[(l - a)^2 + b^2]} + l - a + b\right)} = \frac{\mu_0 I}{4\pi(b - l + a)}\left( \sqrt{2} - \frac{l - a + b}{\sqrt{(l - a)^2 + b^2}} \right)
   $$

将三部分相加，总磁场沿 $z$ 轴方向，指向纸面内（$-\hat{z}$）的总大小为：

$$
B_P = B_{\text{mid}} + B_{\text{left}} + B_{\text{right}} = \frac{\mu_0 I}{4\pi}\left[ \frac{a}{b r_1} + \frac{l - a}{b r_2} + \frac{b - a}{r_1\left(\sqrt{2}\,r_1 + a + b\right)} + \frac{b - l + a}{r_2\left(\sqrt{2}\,r_2 + l - a + b\right)} \right]
$$

其中 $r_1 = \sqrt{a^2 + b^2}$，$r_2 = \sqrt{(l - a)^2 + b^2}$。

---

**2. 旋转均匀带电薄球壳在旋转轴（$z$ 轴）上的磁场分布（Exercise 9.2，经典必考积分题）**：
球壳面电荷密度为 $\sigma = \frac{Q}{4\pi R^2}$。将球壳按极角 $\theta \in [0, \pi]$ 切分为无数个平行于 $xy$ 平面的细圆环：
- 极角 $\theta$ 处的细圆环半径为 $a(\theta) = R\sin\theta$，中心位于 $(0, 0, R\cos\theta)$，环宽为 $R\,d\theta$；
- 细圆环所带电荷量为 $dq = \sigma(2\pi R\sin\theta)(R\,d\theta) = \frac{Q}{2}\sin\theta\,d\theta$；
- 随球壳以角速度 $\omega$ 旋转时，细圆环形成的微元电流为 $di = \frac{\omega}{2\pi}dq = \frac{Q\omega}{4\pi}\sin\theta\,d\theta$。

直接套用 §1.2 中 Example 9.1 的载流圆环轴线磁场公式 $dB_z = \frac{\mu_0 [a(\theta)]^2 di}{2\left([a(\theta)]^2 + (z - R\cos\theta)^2\right)^{3/2}}$，从 $\theta = 0$ 到 $\pi$ 积分：

$$
B_z(z) = \frac{\mu_0 Q \omega R^2}{8\pi} \int_0^\pi \frac{\sin^3\theta\,d\theta}{\left(R^2 + z^2 - 2Rz\cos\theta\right)^{3/2}}
$$

作换元 $s = \sqrt{R^2 + z^2 - 2Rz\cos\theta}$，则 $\cos\theta = \frac{R^2 + z^2 - s^2}{2Rz}$，$\sin\theta\,d\theta = \frac{s\,ds}{Rz}$，积分上下限从 $s_{\min} = \big||z| - R\big|$ 到 $s_{\max} = |z| + R$：

$$
\begin{aligned}
\int_0^\pi \frac{\sin^3\theta\,d\theta}{s^3} &= \frac{1}{Rz} \int_{\big||z|-R\big|}^{|z|+R} \frac{1}{s^2}\left[1 - \left(\frac{R^2 + z^2 - s^2}{2Rz}\right)^2\right] ds \\
&= \frac{1}{4R^3 z^3} \int_{\big||z|-R\big|}^{|z|+R} \left[ 2(R^2 + z^2) - s^2 - \frac{(R^2 - z^2)^2}{s^2} \right] ds \\
&= \frac{1}{4R^3 z^3} \left[ 2(R^2 + z^2)s - \frac{s^3}{3} + \frac{(R^2 - z^2)^2}{s} \right]_{\big||z|-R\big|}^{|z|+R}
\end{aligned}
$$

分球内和球外两种情况代入上下限：
- **当 $|z| < R$（球壳内部，$\big||z| - R\big| = R - |z|$）**：
  方括号计算结果为 $\frac{16}{3}|z|^3$，与分母中的 $4R^3 |z|^3$ 约分后消去 $z$，得到 $\frac{4}{3R^3}$。因此**旋转带电球壳内部是沿 $+z$ 方向的匀强磁场**：
  $$
  \vec{B}_{\text{inside}} = \frac{\mu_0 Q \omega}{6\pi R}\hat{z} \qquad (|z| < R)
  $$
- **当 $|z| > R$（球壳外部，$\big||z| - R\big| = |z| - R$）**：
  方括号计算结果为 $\frac{16}{3}R^3$，约分后得到 $\frac{4}{3|z|^3}$。因此**球壳外部轴线上表现为标准磁偶极子场**：
  $$
  \vec{B}_{\text{outside}} = \frac{\mu_0 Q \omega R^2}{6\pi |z|^3}\hat{z} \qquad (|z| > R)
  $$

</details>

<details markdown="1">
<summary>Exercise 9.3, 9.4 & 9.5: Coaxial Cable, Overlapping Cylinders Cavity & Intersecting Current Sheets（同轴电缆、交叠圆柱空腔匀强场与正交电流板）</summary>

**Problem Statement:**
- **Ex 9.3**: A long straight coaxial cable consists of a conducting cylinder with radius $a$, and a conducting tube with inner radius $b$ and outer radius $c \ (a < b < c)$. Currents of same magnitude $I$ but opposite directions are passing through the system (`Figure 9.9`), distributed uniformly within each conductor. Calculate the magnitude of $B$ at radius $r$ for: (a) $r < a$; (b) $a < r < b$; (c) $b < r < c$; (d) $r > c$.
- **Ex 9.4**: Consider two infinitely long cylinders of radius $R$ whose parallel axes are a distance $2a$ apart ($R > a$). In the shaded non-overlapping area two opposite currents are passing through (`Figure 9.10`), where the current density is uniform with magnitude $j$, and no current flows in the overlap. Calculate the magnitude and direction of the magnetic field at any point inside the overlapping area.
- **Ex 9.5**: Two infinitely large thin inter-penetrating boards are assembled as shown in `Figure 9.11` ($xy$ plane carries surface current density $J_s\hat{y}$, $xz$ plane carries $J_s\hat{z}$). Calculate the magnitude of the magnetic field in each of the four regions of space.

---

**中文解析：**

**1. 同轴电缆四个区域的磁场分布（Exercise 9.3）**：
由柱对称性，取半径为 $r$ 的同心圆作为安培环路，$\oint \vec{B}\cdot d\vec{l} = 2\pi r B = \mu_0 I_{\text{enc}}(r)$：

- **(a) 内导体内部（$r < a$）**：$I_{\text{enc}} = I\frac{\pi r^2}{\pi a^2} = I\frac{r^2}{a^2}$，故：
  $$
  B(r) = \frac{\mu_0 I r}{2\pi a^2} \qquad (r < a)
  $$
- **(b) 内外导体之间（$a < r < b$）**：包围全部内导体电流 $I_{\text{enc}} = I$，故：
  $$
  B(r) = \frac{\mu_0 I}{2\pi r} \qquad (a < r < b)
  $$
- **(c) 外导体管壁内部（$b < r < c$）**：外导体截面积为 $\pi(c^2 - b^2)$，反向电流密度为 $j_{\text{out}} = \frac{I}{\pi(c^2 - b^2)}$。安培环路包围的净电流为 $I_{\text{enc}} = I - I\frac{\pi(r^2 - b^2)}{\pi(c^2 - b^2)} = I\frac{c^2 - r^2}{c^2 - b^2}$，故：
  $$
  B(r) = \frac{\mu_0 I}{2\pi r}\left(\frac{c^2 - r^2}{c^2 - b^2}\right) \qquad (b < r < c)
  $$
- **(d) 电缆外部（$r > c$）**：正反电流完全抵消，$I_{\text{enc}} = I - I = 0$，故：
  $$
  B(r) = 0 \qquad (r > c, \ \text{同轴电缆对外部空间实现磁屏蔽})
  $$

---

**2. 两交叠反向载流圆柱空腔内的匀强磁场（Exercise 9.4，高频必考压轴模型）**：
本题是静磁学中与第二章 Exercise 2.5（两交叠带电球体）完全对偶的经典名题！
**第一步（建立完整实心圆柱内部磁场的矢量公式）**：
设无限长实心圆柱内部通有沿轴向的均匀电流密度 $\vec{j}$。在柱内距轴心位置矢量为 $\vec{r}$（垂直于轴线）处，由安培环路定理知磁场大小为 $B = \frac{\mu_0(\pi r^2 j)}{2\pi r} = \frac{1}{2}\mu_0 j r$，方向遵循右手螺旋定则（沿 $\vec{j}\times\vec{r}$ 方向）。因此，写成矢量叉乘形式恒有：

$$
\vec{B}_{\text{inside}}(\vec{r}) = \frac{1}{2}\mu_0 (\vec{j} \times \vec{r})
$$

**第二步（叠加原理消去交叠区）**：
将“在交叠区无电流、在两侧月牙区分别流过 $-\vec{j}$（左柱，向里 $\otimes$）和 $+\vec{j}$（右柱，向外 $\odot$）”的系统，等效看作**两个完整的实心圆柱电流的直接叠加**：在交叠区内，左柱的 $-\vec{j}$ 与右柱的 $+\vec{j}$ 叠加恰好为 $\vec{j}_{\text{net}} = \vec{0}$（无电流），与原系统完全一致！
设垂直纸面向外为 $+z$ 方向（$\hat{z}$），两圆柱轴心位于 $x$ 轴上：左柱心 $O_1(-a, 0)$ 的电流密度为 $\vec{j}_1 = -j\hat{z}$，右柱心 $O_2(+a, 0)$ 的电流密度为 $\vec{j}_2 = +j\hat{z}$，从左柱心指向右柱心的位移矢量为 $\vec{d} = \overrightarrow{O_1 O_2} = 2a\hat{x}$。
对于交叠区内的任意一点 $P$，记其相对于左柱心 $O_1$ 的位置矢量为 $\vec{r}_1 = \overrightarrow{O_1 P}$，相对于右柱心 $O_2$ 的位置矢量为 $\vec{r}_2 = \overrightarrow{O_2 P}$（满足 $\vec{r}_1 - \vec{r}_2 = \overrightarrow{O_1 O_2} = \vec{d} = 2a\hat{x}$）。由叠加原理：

$$
\vec{B} = \vec{B}_1 + \vec{B}_2 = \frac{1}{2}\mu_0 (-j\hat{z} \times \vec{r}_1) + \frac{1}{2}\mu_0 (+j\hat{z} \times \vec{r}_2) = -\frac{1}{2}\mu_0 j \hat{z} \times (\vec{r}_1 - \vec{r}_2) = -\frac{1}{2}\mu_0 j (\hat{z} \times 2a\hat{x}) = -\mu_0 j a\,\hat{y}
$$

**结论**：交叠区域内的磁场是一个**处处均匀的匀强磁场**！其大小恒为 **$B = \mu_0 j a$**，方向垂直于两轴心连线**竖直向下**（$-\hat{y}$ 方向）。

---

**3. 两正交无限大载流薄板在四个象限中的磁场（Exercise 9.5）**：
由 §2.2 Example 9.5 可知，单块面电流密度为 $J_s$ 的无限大薄板在两侧产生的匀强磁场大小均为 $B_0 = \frac{1}{2}\mu_0 J_s$，方向由右手定则 $\frac{1}{2}\mu_0 \vec{J}_s \times \hat{n}$（$\hat{n}$ 为从薄板指向场点的法向量）给出：
1. **水平板（位于 $z = 0$ 的 $xy$ 平面，电流沿 $+\hat{y}$，即 $\vec{J}_{s1} = J_s\hat{y}$）**：
   在 $z > 0$（上半空间，$\hat{n} = +\hat{z}$）产生 $\vec{B}_1 = +\frac{1}{2}\mu_0 J_s (\hat{y}\times\hat{z}) = +\frac{1}{2}\mu_0 J_s \hat{x}$；在 $z < 0$（下半空间）产生 $-\frac{1}{2}\mu_0 J_s \hat{x}$。故对任意位置恒有：
   $$
   \vec{B}_1 = \frac{1}{2}\mu_0 J_s \operatorname{sgn}(z)\,\hat{x}
   $$
2. **竖直板（位于 $y = 0$ 的 $xz$ 平面，电流沿 $+\hat{z}$，即 $\vec{J}_{s2} = J_s\hat{z}$）**：
   在 $y > 0$（右半空间，$\hat{n} = +\hat{y}$）产生 $\vec{B}_2 = \frac{1}{2}\mu_0 J_s (\hat{z}\times\hat{y}) = -\frac{1}{2}\mu_0 J_s \hat{x}$；在 $y < 0$（左半空间）产生 $+\frac{1}{2}\mu_0 J_s \hat{x}$。故对任意位置恒有：
   $$
   \vec{B}_2 = -\frac{1}{2}\mu_0 J_s \operatorname{sgn}(y)\,\hat{x}
   $$

将两板磁场在四个象限（Four regions）内叠加：
- **在第一象限（$y > 0, z > 0$）和第三象限（$y < 0, z < 0$）**（即 $yz > 0$ 的两个对角区域）：$\operatorname{sgn}(y) = \operatorname{sgn}(z)$，$\vec{B}_1$ 与 $\vec{B}_2$ 等大反向，**合磁场大小 $B = 0$**；
- **在第二象限（$y < 0, z > 0$）和第四象限（$y > 0, z < 0$）**（即 $yz < 0$ 的两个对角区域）：$\operatorname{sgn}(y) = -\operatorname{sgn}(z)$，$\vec{B}_1$ 与 $\vec{B}_2$ 同向叠加，**合磁场大小 $B = \mu_0 J_s$**（在 $y<0, z>0$ 区沿 $+\hat{x}$，在 $y>0, z<0$ 区沿 $-\hat{x}$）。

</details>

<details markdown="1">
<summary>Exercise 9.6, 9.7 & 9.8: Repelling Hanging Wires, Figure-Eight Circulation & Helical Solenoid（悬挂导线斥力平衡、“8”字回路环流与考虑轴向电流的螺旋螺线管）</summary>

**Problem Statement:**
- **Ex 9.6**: Two long, straight, parallel wires, each of mass $\lambda$ per unit length, hang side by side from a common horizontal axis by light insulating threads of length $L$. When carrying equal opposite currents $I$, they repel each other, and in equilibrium the threads of each wire make an angle $\theta$ with the vertical. Find $I$ in terms of $\lambda, L, \theta, \mu_0$ and $g$.
- **Ex 9.7**: Two long straight wires cross the plane of the page at right angles at $A$ (current $i_1 > 0$ out of the page) and $B$ (current $i_2 > 0$ into the page). Evaluate $\oint \vec{B}\cdot d\vec{l}$ along: (a) A path that goes around $A$ twice, counterclockwise, without going around $B$; (b) A figure-eight path whose two loops meet at a single crossing point, where one loop goes around $A$ counterclockwise and the other goes around $B$.
- **Ex 9.8**: A long solenoid of radius $R$ is wound from a single wire as a tight, single-layer helix with $n$ turns per unit length, carrying steady current $i$. Model the winding as a thin cylindrical sheet of radius $R$ that carries a current $ni$ per unit length around the axis and, in addition, a total current $i$ along the axis. (a) Find the magnitudes of the axial and azimuthal components of $\vec{B}$ inside ($r < R$) and outside ($r > R$). (b) Find the ratio of the magnitude of the field just outside the winding to its magnitude inside.

---

**中文解析：**

**1. 双悬挂反向载流导线的平衡电流（Exercise 9.6）**：
当每根导线的悬线与竖直方向夹角为 $\theta$ 时，两根平行导线之间的水平间距为：

$$
d = 2L\sin\theta
$$

考察其中一根导线的单位长度受力：它受到竖直向下的重力 $\lambda g$、水平向外的安培排斥力 $f_B = \frac{\mu_0 I^2}{2\pi d} = \frac{\mu_0 I^2}{4\pi L\sin\theta}$ 以及沿悬线方向的拉力 $T$。由三力平衡条件 $\tan\theta = \frac{f_B}{\lambda g}$：

$$
\frac{\mu_0 I^2}{4\pi L\sin\theta} = \lambda g \tan\theta \implies I = 2\sin\theta\sqrt{\frac{\pi \lambda g L}{\mu_0 \cos\theta}}
$$

---

**2. 绕行两圈路径与“8”字形自交路径的安培环流（Exercise 9.7）**：

- **(a)** 路径逆时针（从读者方向看）绕导线 $A$ 两圈且不包围 $B$。由右手定则，穿出纸面的电流 $i_1$ 对应逆时针绕行方向为正，绕行两圈（$\Delta\phi = 4\pi$）累加两次：
  $$
  \oint \vec{B} \cdot d\vec{l} = +2\mu_0 i_1
  $$
- **(b)** 对于在交点处发生交叉（Crosses itself）的“8”字形连续路径：当左半环逆时针绕过 $A$（贡献 $+\mu_0 i_1$）并通过交叉点进入右半环时，右半环的绕行方向必然自动反转变为**顺时针**（Clockwise）绕过 $B$！
  由于导线 $B$ 的电流 $i_2$ 是穿入纸面的（$\otimes$），顺时针绕行方向通过右手定则判别恰与穿入纸面的方向一致（贡献也为正：$+\mu_0 i_2$）。因此总环流为两部分之和：
  $$
  \oint_{\text{figure-eight}} \vec{B} \cdot d\vec{l} = \mu_0(i_1 + i_2)
  $$

---

**3. 计入轴向推进电流的单层螺旋螺线管（Exercise 9.8）**：
将圆柱面电流分解为“环向電流层（单位长度 $ni$）”与“轴向圆柱面电流（总电流 $i$ 均匀分布在周长 $2\pi R$ 上）”两部分的独立叠加：

- **(a) 管内（$r < R$）与管外（$r > R$）的轴向分量 $B_z$ 和方位角分量 $B_\phi$**：
  1. **轴向分量 $B_z$（由环向电流 $ni$ 产生，即标准理想螺线管模型）**：
     $$
     B_z = \begin{cases}
     \mu_0 n i, & r < R \quad (\text{管内}), \\
     0, & r > R \quad (\text{管外}).
     \end{cases}
     $$
  2. **方位角分量 $B_\phi$（由轴向圆管电流 $i$ 产生，取半径为 $r$ 的同心圆安培环路 $2\pi r B_\phi = \mu_0 I_{\text{axial, enc}}$）**：
     - 当 $r < R$（管内）时：圆环路内部无轴向电流（$I_{\text{axial, enc}} = 0$），故 $B_\phi = 0$；
     - 当 $r > R$（管外）时：圆环路包围全部轴向电流 $I_{\text{axial, enc}} = i$，故 $B_\phi = \dfrac{\mu_0 i}{2\pi r}$。
- **(b) 紧贴管外壁（$r = R^+$）与管内（$r < R$）的磁感应强度模长之比**：
  在管内 $|\vec{B}_{\text{in}}| = \mu_0 n i$；在紧贴管外壁 $r = R^+$ 处，$|\vec{B}_{\text{out}}(R^+)| = \frac{\mu_0 i}{2\pi R}$。两者之比为：
  $$
  \frac{B(R^+)}{B_{\text{inside}}} = \frac{\mu_0 i / (2\pi R)}{\mu_0 n i} = \frac{1}{2\pi n R}
  $$

</details>

<details markdown="1">
<summary>Exercise 9.9 & 9.10: Wire Threaded Through a Toroid & Validity Test of Magnetic Fields（穿过螺绕环的导线受力与磁场无散性判别）</summary>

**Problem Statement:**
- **Ex 9.9**: An ideal toroidal coil of $N$ turns carries a steady current $I$. Its tube has a circular cross section of radius $a$, whose center runs around a circle of radius $R \ (R > a)$ in the $xy$ plane, centered at the origin. The magnetic field inside the tube circulates counterclockwise as seen from $+z$. A thin, straight test wire is threaded through the winding along the $x$ axis, from $x = R - a$ to $x = R + a$, carrying current $i$ in the $+x$ direction.
  (a) Find the magnetic force on this segment of wire.
  (b) Let $B_0$ be the magnitude of the field on the central circle of the tube ($r = R$). Show that the magnitude of the force is larger than $2aiB_0$.
- **Ex 9.10**: Each of the following time-independent vector fields ($k \neq 0$) is proposed as the magnetic field in some region of space. For each, decide whether it can be a magnetic field. If it can, find the current density $\vec{j}$ that must flow in that region; if it cannot, find its outward flux through the surface of the cube $0 \le x \le s, \ 0 \le y \le s, \ 0 \le z \le s$ ($s > 0$):
  (a) $\vec{B} = k(x\hat{x} - y\hat{y})$; (b) $\vec{B} = k(x\hat{x} + y\hat{y})$; (c) $\vec{B} = kx\hat{z}$.

---

**中文解析：**

**1. 沿径向穿过螺绕环管腔的载流直导线所受安培力（Exercise 9.9）**：

- **(a)** 在 $x$ 轴上从 $x = R - a$ 到 $x = R + a$ 的管腔区间内，螺绕环的磁场逆时针环绕，因此在正 $x$ 半轴上磁场方向沿 $+\hat{y}$ 方向，大小为 $B(x) = \frac{\mu_0 NI}{2\pi x}$：
  $$
  \vec{B}(x, 0, 0) = \frac{\mu_0 NI}{2\pi x}\hat{y} \qquad (R - a \le x \le R + a)
  $$
  测试导线线元为 $i\,d\vec{l} = i\,dx\,\hat{x}$，所受微元安培力为 $d\vec{F} = i\,dx\,\hat{x} \times \left(\frac{\mu_0 NI}{2\pi x}\hat{y}\right) = \frac{\mu_0 NI i}{2\pi x}dx\,\hat{z}$。在 $[R - a, R + a]$ 上积分得总磁力：
  $$
  \vec{F} = \hat{z} \frac{\mu_0 NI i}{2\pi} \int_{R - a}^{R + a} \frac{dx}{x} = \frac{\mu_0 NI i}{2\pi}\ln\left(\frac{R + a}{R - a}\right)\hat{z}
  $$
- **(b) 与中心圆场强 $B_0 = \frac{\mu_0 NI}{2\pi R}$ 均匀估算值 $2aiB_0$ 的大小比较**：
  注意到 $\frac{\mu_0 NI}{2\pi} = R B_0$，故实际磁力大小可写为 $F = i R B_0 \ln\left(\frac{1 + a/R}{1 - a/R}\right)$。
  利用对数函数的泰勒级数展开（对 $0 < u = \frac{a}{R} < 1$）：
  $$
  \ln\left(\frac{1 + u}{1 - u}\right) = 2\left(u + \frac{u^3}{3} + \frac{u^5}{5} + \cdots\right) > 2u = \frac{2a}{R}
  $$
  （或从凸函数性质看：因 $B(x) \propto \frac{1}{x}$ 是严格下凸函数，$f''(x) > 0$，由琴生不等式知其在对称区间 $[R-a, R+a]$ 上的积分平均值必严格大于中点值 $B(R) = B_0$）。因此恒有：
  $$
  F = i R B_0 \ln\left(\frac{1 + a/R}{1 - a/R}\right) > i R B_0 \left(\frac{2a}{R}\right) = 2aiB_0
  $$

---

**2. 候选磁场矢量的无散性检验（$\nabla\cdot\vec{B} = 0$）、电流密度与立方体磁通量（Exercise 9.10）**：
判断一个稳恒矢量场能否作为真实物理磁场的充要条件是它必须满足磁场高斯定理 **$\nabla\cdot\vec{B} = 0$**。若满足，则由安培环路定理微分形式 $\vec{j} = \frac{1}{\mu_0}(\nabla\times\vec{B})$ 求出所需电流密度；若不满足，则由散度定理 $\Phi = \oint_S \vec{B}\cdot d\vec{A} = \int_{\text{cube}} (\nabla\cdot\vec{B})\,dV$ 求出穿过边长为 $s$ 的立方体的净通量：

- **(a) $\vec{B} = k(x\hat{x} - y\hat{y})$**：
  计算散度：$\nabla\cdot\vec{B} = \frac{\partial(kx)}{\partial x} + \frac{\partial(-ky)}{\partial y} = k - k = 0$。
  因此它**可以作为真实磁场**！计算其旋度求电流密度：
  $$
  \vec{j} = \frac{1}{\mu_0}(\nabla\times\vec{B}) = \vec{0} \qquad (\text{该区域内无电流，磁场由区域外部的电流或磁极产生})
  $$
- **(b) $\vec{B} = k(x\hat{x} + y\hat{y})$**：
  计算散度：$\nabla\cdot\vec{B} = \frac{\partial(kx)}{\partial x} + \frac{\partial(ky)}{\partial y} = k + k = 2k \neq 0$。
  因此它**不能作为真实磁场**！利用散度定理计算穿过立方体 $[0, s]^3$（体积 $V = s^3$）的向外通量：
  $$
  \Phi = \int_V (\nabla\cdot\vec{B})\,dV = 2k \cdot s^3 = 2ks^3
  $$
- **(c) $\vec{B} = kx\hat{z}$**：
  计算散度：$\nabla\cdot\vec{B} = \frac{\partial(kx)}{\partial z} = 0$。
  因此它**可以作为真实磁场**！由安培环路定理微分形式计算区域内的电流密度：
  $$
  \vec{j} = \frac{1}{\mu_0}(\nabla\times\vec{B}) = \frac{1}{\mu_0}\left(-\hat{y}\frac{\partial B_z}{\partial x}\right) = -\frac{k}{\mu_0}\hat{y}
  $$

</details>