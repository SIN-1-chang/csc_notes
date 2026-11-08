# Chapter 8: The Magnetic Field（磁场）

!!! abstract
    General Physics II (Electromagnetism) | 第八章课堂与讲义笔记
    
    参考：
    
    - Lecture 8: *The Magnetic Field* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 8: *The Magnetic Field*
    - Halliday, Resnick & Krane, *Physics*, Chapter 32

## 1 磁场与洛伦兹力 (The Magnetic Field and Lorentz Force)

### 1.1 磁感线与无磁单极子特征

除了静电场外，永磁体（Magnets）与电流（Electric currents）还会在周围空间建立**磁场**（Magnetic Field，用矢量 $\vec{B}$ 表示）。与电场类似，我们可以用**磁感线**（Magnetic Field Lines）来形象化描述磁场：

1. **切线方向**：空间任意一点处磁感线的切线方向（Tangent direction）代表该点磁场矢量 $\vec{B}$ 的方向；
2. **疏密程度**：垂直截面上磁感线的数密度（Density / Spacing of lines）正比于该处磁场强度的大小 $|\vec{B}|$；
3. **无头无尾的闭合曲线（无磁单极子）**：这是磁场与静电场最本质的区别！静电场的电场线总是起自正电荷、终止于负电荷（或延伸至无穷远）；而在自然界中从未观测到孤立的**磁单极子**（Magnetic Monopole / Magnetic Charge），因此**磁感线没有起点也没有终点，永远形成闭合回路**。所有磁体都必然同时具有北极（North pole, N）和南极（South pole, S），称为**磁偶极子**（Magnetic Dipoles）：在磁体外部，磁感线从 N 极穿出并进入 S 极；在磁体内部，磁感线则从 S 极指向 N 极。（注：地球本身是一个巨大的磁偶极子，地磁北极位于南极洲附近，而地理北极附近实际上是地磁南极）。

### 1.2 运动电荷所受的洛伦兹力

当带电粒子（电荷量为 $q$，含正负号）以速度 $\vec{v}$ 在磁场 $\vec{B}$ 中运动时，会受到磁场施加的偏转力，称为**磁场力**或**洛伦兹力**（Magnetic Force / Lorentz Force）：

$$
\vec{F}_B = q\vec{v} \times \vec{B}
$$

其中 $\vec{v}$ 与 $\vec{B}$ 必须在同一个参考系中测量。洛伦兹力的方向由**右手定则**（Right-hand rule）判定：伸开右手，四指从速度矢量 $\vec{v}$ 转向磁场矢量 $\vec{B}$，大拇指所指方向即为 $\vec{v}\times\vec{B}$ 的方向（正电荷 $q > 0$ 受力方向与 $\vec{v}\times\vec{B}$ 相同；负电荷 $q < 0$ 受力方向与 $\vec{v}\times\vec{B}$ 相反）。

| 物理特性 | 洛伦兹力（磁场力 $\vec{F}_B = q\vec{v}\times\vec{B}$） | 静电力（库仑力 $\vec{F}_E = q\vec{E}$） |
| :--- | :--- | :--- |
| **作用对象** | 仅对**运动电荷**（$\vec{v} \nparallel \vec{B}$）产生作用力 | 对静止电荷和运动电荷均产生作用力 |
| **力的方向** | **恒垂直于 $\vec{v}$ 和 $\vec{B}$ 构成的平面**（$\vec{F}_B \perp \vec{v}$ 且 $\vec{F}_B \perp \vec{B}$） | 平行于电场矢量 $\vec{E}$ 的方向 |
| **做功与动能改变** | **对单个运动电荷永不做功**（$dW = \vec{F}_B\cdot d\vec{r} = \vec{F}_B\cdot\vec{v}\,dt = 0$），只改变速度方向，**不改变速率 $\vec{v}$ 和动能** | 一般做功（$dW = q\vec{E}\cdot d\vec{r} \neq 0$），可改变粒子的速率与动能 |

**磁感应强度 $\vec{B}$ 的单位**：
在国际单位制（SI）中，$\vec{B}$ 的单位是**特斯拉**（Tesla，简记为 $\text{T}$）；常用的非 SI 旧单位为**高斯**（Gauss，简记为 $\text{G}$）：

$$
1\text{ T} = 1\ \frac{\text{N}}{\text{C}\cdot(\text{m/s})} = 1\ \frac{\text{N}}{\text{A}\cdot\text{m}}, \qquad 1\text{ T} = 10^4\text{ G}
$$

（地球表面的地磁场强度约为 $0.5\text{ G} \sim 1\text{ G}$，即 $50\ \mu\text{T} \sim 100\ \mu\text{T}$）。

---

## 2 带电粒子在磁场及复合电磁场中的运动 (Motion of Charged Particles in Fields)

### 2.1 匀强磁场中的圆周与螺旋运动 (Circulating Charges and Helical Path)

设质量为 $m$、带电量为 $q$ 的粒子以初速度 $\vec{v}$ 进入匀强磁场 $\vec{B}$（速度与磁场夹角为 $\phi$）。将速度分解为平行于磁场的分量 $v_\parallel = v\cos\phi$ 和垂直于磁场的分量 $v_\perp = v\sin\phi$：

1. **平行方向（匀速直线运动）**：沿 $\vec{B}$ 方向不受磁场力，$v_\parallel$ 保持恒定不变。
2. **垂直平面（匀速圆周运动）**：洛伦兹力大小恒为 $F_B = |q|v_\perp B$，方向始终垂直于 $\vec{v}_\perp$ 并指向圆心，充当向心力：
   $$
   |q|v_\perp B = \frac{mv_\perp^2}{R}
   $$
   结合 $v_\perp = \omega R$，立即解得圆周运动的**回旋半径**（Cyclotron radius, $R$ or $r$）、**回旋角频率**（Cyclotron angular frequency, $\omega$）及**螺距**（Pitch, $p$，即每旋转一周沿磁场方向前进的距离）：

$$
R = \frac{mv_\perp}{|q|B} = \frac{v_\perp}{\omega}, \qquad \omega = \frac{|q|B}{m} \quad \left(\text{矢量形式 }\vec{\omega} = -\frac{q\vec{B}}{m}\right), \qquad p = v_\parallel T = \frac{2\pi m v_\parallel}{|q|B}
$$

- 当 $v_\parallel = 0 \ (\phi = 90^\circ)$ 时，轨迹为平面**圆周**；当 $v_\perp = 0 \ (\phi = 0^\circ)$ 时，轨迹为**直线**；一般情形下轨迹为**螺旋线**（Helix）。
- **核心特征**：在非相对论条件下，回旋角频率 $\omega = \frac{|q|B}{m}$ 和周期 $T = \frac{2\pi m}{|q|B}$ **仅取决于粒子的荷质比（Charge-to-mass ratio）$\frac{|q|}{m}$ 和磁感应强度 $B$，而与粒子的运动速率 $v$ 及轨道半径 $R$ 完全无关**！
- **非均匀磁场中的磁镜反射（Magnetic Mirror）**：当带电粒子在两端磁场较强、中间较弱的非均匀磁场（磁瓶）中作螺旋运动时，强场端会聚的磁感线使洛伦兹力产生一个指向弱场区的纵向分量，能将粒子反射回中间区域。

**应用一：回旋加速器（Cyclotron）**
回旋加速器由置于垂直匀强磁场 $\vec{B}$ 中的两个中空半圆形金属盒——**D 形盒**（Dees）组成。D 形盒内部因静电屏蔽无电场，粒子在盒内仅受磁场力作半圆周运动；两盒狭缝（Gap）间施加高频交变电场。只要交变电场的频率严格等于粒子的回旋频率：

$$
f_{\text{osc}} = f_{\text{cyclotron}} = \frac{\omega}{2\pi} = \frac{|q|B}{2\pi m}
$$

粒子每次穿过狭缝时都会恰好遇到正向加速电场，动能不断增加，轨道半径 $R = \frac{mv}{|q|B}$ 随之逐圈向外呈螺旋状扩大，最终从边缘偏转板（Deflector plate）引出高能粒子束。

### 2.2 匀强复合电磁场中的运动与 $\vec{E}\times\vec{B}$ 漂移 (Combined $\vec{E}$ and $\vec{B}$ Fields)

当空间同时存在匀强电场 $\vec{E}$ 和匀强磁场 $\vec{B}$ 时，带电粒子所受总电磁力（广义洛伦兹力）为：

$$
\vec{F} = q\vec{E} + q\vec{v} \times \vec{B}
$$

讲义（Example 8.1）重点剖析了两种最典型的正交与平行位形：

**情形 1：电场与磁场平行（$\vec{E} \parallel \vec{B}$，设 $\vec{E} = E\hat{z}, \ \vec{B} = B\hat{z}$）**
运动分解为两个互不相干的独立部分：沿 $z$ 轴受恒定电场力作匀加速运动 $a_z = \frac{d^2 z}{dt^2} = \frac{qE}{m}$；在垂直的 $xy$ 平面内受洛伦兹力作角速度为 $\omega = \frac{|q|B}{m}$ 的匀速圆周运动。合轨迹为螺距随时间二次方增大的变螺距螺旋线。

**情形 2：电场与磁场垂直（$\vec{E} \perp \vec{B}$，设 $\vec{E} = E\hat{x}, \ \vec{B} = B\hat{z}$，初速度 $\vec{v}(0) = \vec{0}$）**
粒子始终在 $xy$ 平面内运动，牛顿第二定律的分量方程为（记 $a = \frac{qE}{m}, \ \omega = \frac{qB}{m}$）：

$$
\begin{cases}
m\dfrac{dv_x}{dt} = qE + qv_y B \implies \dfrac{dv_x}{dt} = a + \omega v_y \\
m\dfrac{dv_y}{dt} = -qv_x B \implies \dfrac{dv_y}{dt} = -\omega v_x
\end{cases}
$$

对第一式求导并将第二式代入，得简谐振动方程 $\ddot{v}_x + \omega^2 v_x = 0$。结合初始条件 $v_x(0) = v_y(0) = 0$（从而 $\dot{v}_x(0) = a$），解得速度与位置随时间的演化（注意到 $\frac{a}{\omega} = \frac{E}{B}$）：

$$
v_x(t) = \frac{E}{B}\sin(\omega t), \qquad v_y(t) = \frac{E}{B}\big(\cos(\omega t) - 1\big)
$$

$$
x(t) = \frac{E}{\omega B}\big(1 - \cos(\omega t)\big), \qquad y(t) = \frac{E}{\omega B}\big(\sin(\omega t) - \omega t\big)
$$

这是一条标准的**摆线**（Cycloid，即滚动的车轮边缘一点描出的轨迹）！

!!! tip "核心物理结论：$\vec{E}\times\vec{B}$ 漂移速度与运动参考系消场法"
    1. **与电荷、质量均无关的 $\vec{E}\times\vec{B}$ 漂移**：
       在正交电磁场中，粒子除了以回旋频率 $\omega$ 作圆周回旋外，其导心还沿着同时垂直于 $\vec{E}$ 和 $\vec{B}$ 的方向作匀速漂移，平均漂移速度矢量为：
       $$
       \vec{v}_d = \frac{\vec{E} \times \vec{B}}{B^2}, \qquad |\vec{v}_d| = \frac{E}{B}
       $$
       极其奇妙的是，该漂移速度**既不依赖于粒子的质量 $m$，也不依赖于电荷量 $q$ 的大小和正负号**（正负电荷向同一个方向漂移）！
    2. **参考系变换法（Reference Frame Boost）**：
       将观测参考系变换到以恒定速度 $\vec{v}_0 = \frac{\vec{E}\times\vec{B}}{B^2}$（在上述坐标系下即 $\vec{v}_0 = -\frac{E}{B}\hat{y}$）运动的动参考系中。令实验室速度为 $\vec{v} = \vec{u} + \vec{v}_0$（$\vec{u}$ 为相对动系的速度），代入总电磁力：
       $$
       \vec{F} = q\vec{E} + q(\vec{u} + \vec{v}_0)\times\vec{B} = q\vec{u}\times\vec{B} + \underbrace{q\left(\vec{E} + \vec{v}_0\times\vec{B}\right)}_{=\,\vec{0}} = q\vec{u}\times\vec{B}
       $$
       可以看到，在以 $\vec{v}_0$ 运动的参考系中，**电场被完全抵消（只要满足非相对论条件 $E < cB$）**，粒子仅感受到纯磁场并以初速度 $-\vec{v}_0$ 作匀速圆周运动！将动系中的匀速圆周运动叠加参考系自身的匀速直线运动 $\vec{v}_0$，在实验室系中看到的就是完美的摆线轨迹。

### 2.3 汤姆孙发现电子 (Discovery of the Electron, 1897) 与霍尔效应 (The Hall Effect, 1879)

**1. 汤姆孙阴极射线管测定电子荷质比（J. J. Thomson's Experiment）**

1897 年，J. J. Thomson 利用阴极射线管（Cathode ray tube）测量了当时未知的阴极射线粒子的荷质比，发现其质量比氢原子轻一千倍以上（现代精确值为 $1/1836.15$），从而发现了**电子**（Electron）：

1. **加速阶段**：热灯丝（Filament）发射出的电子经电势差 $V$ 加速后穿过狭缝，由能量守恒 $\frac{1}{2}mv^2 = |q|V$ 获得速率：
   $$
   v = \sqrt{\frac{2|q|V}{m}}
   $$
2. **正交场速度选择阶段**：电子束进入正交的匀强电场 $\vec{E}$ 与匀强磁场 $\vec{B}$ 区域。调节场强使荧光屏（Fluorescent screen）上的光斑不发生偏转，此时静电力与洛伦兹力精确平衡：
   $$
   |q|E = |q|vB \implies v = \frac{E}{B}
   $$
3. **联立求荷质比**：消去速率 $v$，即得荷质比测量公式：
   $$
   \frac{|q|}{m} = \frac{1}{2V}\left(\frac{E}{B}\right)^2
   $$

**2. 霍尔效应（The Hall Effect, 1879）与量子霍尔效应**

设宽度为 $d$、横截面积为 $A$ 的导电薄带沿 $x$ 方向通有电流 $i$（电流密度 $\vec{j} = nq\vec{v}_d$，其中 $n$ 为载流子数密度，$q$ 为带符号的单个载流子电荷），并置于垂直于薄带平面的匀强磁场 $\vec{B} = B_z\hat{z}$ 中：

1. **横向霍尔电场与平衡条件**：磁场对漂移载流子施加横向洛伦兹力，使其向薄带一侧边缘偏转堆积，从而在薄带两侧建立起横向**霍尔电场** $\vec{E}_H$ 及**霍尔电压**（Hall voltage, $V_H = E_H d$）。达到动态平衡时，横向静电力与洛伦兹力平衡：
   $$
   \vec{E}_H + \vec{v}_d \times \vec{B} = \vec{0} \implies \vec{E}_H = -\vec{v}_d \times \vec{B} = -\frac{1}{nq}\vec{j} \times \vec{B}
   $$
2. **霍尔电阻率与霍尔系数**：
   定义横向电场与纵向电流密度之比为**霍尔电阻率**（Hall resistivity, $\rho_H$ 或 $\rho_{xy}$），进一步除以磁场 $B$ 定义为**霍尔系数**（Hall coefficient, $R_H$）：
   $$
   \rho_H = \rho_{xy} = \frac{E_y}{j_x} = \frac{B}{nq}, \qquad R_H = \frac{E_y}{B_z j_x} = \frac{1}{nq}, \qquad |V_H| = E_H d = \frac{iBd}{n|q|A}
   $$
   **核心物理用途**：由于 $q$ 带有正负号，通过测量霍尔电压的正负（即哪一侧边缘电势更高），可以直接**判定导体中的载流子是正电荷（空穴）还是负电荷（电子，$q = -e \implies R_H = -1/(ne) < 0$）**；同时由 $|R_H|$ 可直接测出导体内的**载流子数密度 $n$**。
3. **量子霍尔效应（Quantum Hall Effect, 1980 & 1982）**：
   在极低温和强磁场下的二维电子气中，由于量子力学朗道能级分立化（Level discretization），横向霍尔电阻 $R_{xy}$ 不再随磁场线性增长，而是出现一系列极其平坦的量子化平台 $R_{xy} = \frac{h}{\nu e^2}$（其中电阻量子 $h/e^2 = 25,812.807449(86)\ \Omega$，$\nu$ 取整数或特定分数），同时在平台区纵向电阻 $R_{xx}$ 降为零。

---

## 3 载流导线在磁场中所受的安培力 (Magnetic Force on a Current-Carrying Wire)

当一根长度为 $L$、横截面积为 $A$、通有稳恒电流 $i = n|q|v_d A$ 的直导线置于匀强磁场 $\vec{B}$ 中时，导线内的每个运动载流子均受到洛伦兹力 $\vec{F}_q = q\vec{v}_d\times\vec{B}$。由于载流子无法逸出导线边界，它们通过与晶格离子的碰撞以及在导线侧面堆积形成的内部霍尔电场，将动量与作用力全部传递给导线晶格整体。

整段导线内共含有 $N = nAL$ 个载流子，注意到电流密度 $\vec{j} = nq\vec{v}_d$ 的方向与沿着电流方向的导线长度矢量 $\vec{L}$ 一致，且 $jA = i$，因此整根直导线所受的总磁场力为：

$$
\vec{F} = (nAL) q\vec{v}_d \times \vec{B} = (\vec{j} \times \vec{B}) AL = i\vec{L} \times \vec{B}
$$

对于任意弯曲形状的导线或非均匀磁场，可将导线分割为无穷小有向线元 $d\vec{l}$（方向沿电流方向），其所受微元磁场力称为**安培力**（Ampère Force）：

$$
d\vec{F} = i\,d\vec{l} \times \vec{B} \implies \vec{F} = \int_{\text{wire}} i\,d\vec{l} \times \vec{B}
$$

!!! note "重要推论：匀强磁场中弯曲导线的等效弦长定理"
    若磁场 $\vec{B}$ 是**匀强磁场**（常矢量），可将 $\vec{B}$ 提到积分号外：
    $$
    \vec{F} = i\left(\int_A^B d\vec{l}\right) \times \vec{B} = i\vec{L}_{\text{AB}} \times \vec{B}
    $$
    其中 $\vec{L}_{\text{AB}}$ 是直接从导线起点 $A$ 指向终点 $B$ 的有向直线段矢量（等效弦矢量）！特别地，**任意闭合载流线圈在匀强磁场中所受的净安培力恒为零**（$\oint d\vec{l} = \vec{0} \implies \vec{F}_{\text{net}} = \vec{0}$）。

---

## 4 载流线圈的磁力矩与磁偶极矩 (Torque on a Current Loop and Magnetic Dipole)

### 4.1 矩形线圈力矩推导与磁偶极矩定义

考察置于匀强磁场 $\vec{B}$ 中的矩形载流线圈（边长分别为 $a$ 和 $b$，面积 $A = ab$，通有电流 $i$）。首先定义线圈平面的**单位法向矢量** $\hat{n}$（或面积矢量 $\vec{A} = A\hat{n}$）：按**右手螺旋定则**，四指弯曲方向顺着电流 $i$ 的环绕方向，大拇指所指方向即为法向 $\hat{n}$ 的正方向。设 $\hat{n}$ 与磁场 $\vec{B}$ 的夹角为 $\theta$。

- **净平动力为零**：矩形四条边所受安培力两两等大反向（$\vec{F}_1 = -\vec{F}_3, \ \vec{F}_2 = -\vec{F}_4$），故合力 $\vec{F}_{\text{net}} = \vec{0}$。
- **合力矩（Net Torque）推导**：
  - **方法 1（力臂法）**：长为 $b$ 的两条边所受安培力共线且平行于转轴，不产生力矩；长为 $a$ 的两条边始终垂直于 $\vec{B}$，各自受安培力大小 $F_1 = F_3 = iaB$，方向相反且作用线相距力臂（Lever arm）$b\sin\theta$，构成一对力偶（Couple），总力矩大小为：
    $$
    \tau = (iaB)(b\sin\theta) = i(ab)B\sin\theta = iAB\sin\theta
    $$
  - **方法 2（矢量三重积法，Lecture 8 Slides 24–25 & Appendix 8A）**：设沿边 2（长 $b$）和边 3（长 $a$）顺着电流方向的边长矢量为 $\vec{L}_2$ 和 $\vec{L}_3$（满足 $\vec{L}_2\cdot\vec{L}_3 = 0$ 且 $\vec{L}_3\cdot\vec{B} = 0$）。利用**矢量三重积公式**（Vector triple product）：
    $$
    \vec{A}\times(\vec{B}\times\vec{C}) = \vec{B}(\vec{A}\cdot\vec{C}) - \vec{C}(\vec{A}\cdot\vec{B}), \qquad (\vec{A}\times\vec{B})\times\vec{C} = -\vec{A}(\vec{B}\cdot\vec{C}) + \vec{B}(\vec{A}\cdot\vec{C})
    $$
    可直接将力矩矢量展开化简为：
    $$
    \vec{\tau} = \vec{L}_2 \times \vec{F}_3 = i\vec{L}_2 \times (\vec{L}_3 \times \vec{B}) = i(\vec{L}_2 \times \vec{L}_3) \times \vec{B} = i\vec{A} \times \vec{B}
    $$

虽然上述推导针对矩形线圈，但由于任意形状的平面闭合回路均可被无限细分为无数个微小矩形网格（内部公共边电流正反抵消，仅剩外边界电流），因此 $\vec{\tau} = i\vec{A}\times\vec{B}$ **对匀强磁场中任意形状的平面载流线圈均严格成立**。

若平面线圈共有 $N$ 匝（Turns），则总力矩放大 $N$ 倍。为此定义 $N$ 匝载流线圈的**磁偶极矩**（Magnetic Dipole Moment，简称**磁矩**，记作 $\vec{\mu}$，SI 单位为 $\text{A}\cdot\text{m}^2$ 或 $\text{J/T}$）为：

$$
\vec{\mu} = Ni\vec{A} = NiA\hat{n} \implies \vec{\tau} = \vec{\mu} \times \vec{B}
$$

该力矩总是试图将线圈的法向矢量 $\hat{n}$（即磁偶极矩 $\vec{\mu}$）旋转到与外磁场 $\vec{B}$ 一致的方向。

### 4.2 磁偶极子与电偶极子的对称类比及直流电动机

| 物理量维度 | 磁场中的磁偶极子（Magnetic Dipole） | 电场中的电偶极子（Electric Dipole） |
| :--- | :--- | :--- |
| **偶极矩定义** | $\vec{\mu} = Ni\vec{A}$（方向由电流右手螺旋定则确定） | $\vec{p} = q\vec{d}$（方向从 $-q$ 指向 $+q$） |
| **匀强外场中的净力** | $\vec{F}_{\text{net}} = \vec{0}$ | $\vec{F}_{\text{net}} = \vec{0}$ |
| **匀强外场中的力矩** | $\vec{\tau}_B = \vec{\mu} \times \vec{B}$ | $\vec{\tau}_E = \vec{p} \times \vec{E}$ |
| **外场中的取向趋势** | 力矩驱使 $\vec{\mu}$ 转向与 $\vec{B}$ 同向（$\theta \to 0$） | 力矩驱使 $\vec{p}$ 转向与 $\vec{E}$ 同向（$\theta \to 0$） |

**应用：直流电动机（DC Electric Motor，§8.3.1 & Appendix 8B）**
在直流电动机中，为了防止载流线圈转到 $\vec{\mu}$ 与 $\vec{B}$ 同向的平衡位置（$\theta = 0$）后停止转动（或因力矩反向而来回摆动），必须在线圈每转过半圈（越过平衡位置）的瞬间自动反转线圈中的电流方向。这一自动换向功能通过与转轴同步旋转的**开口环换向器**（Split-ring commutator）配合固定不动的导电**电刷**（Brushes）来实现，从而保证磁力矩 $\vec{\tau}$ 始终沿同一旋转方向驱动转子持续做功。

---

## 5 Chapter 8 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 8.1, 8.2 & 8.3: Helical Pitch, Copper Strip Hall Effect & Partial Loop in B Field（螺旋螺距、铜带霍尔效应测算与半平面磁场中的载流圆环）</summary>

**Problem Statement:**
- **Ex 8.1**: A particle with mass $m$ and charge $q$ enters a region of uniform magnetic field $B$ large enough to contain at least one full turn of the helix. The initial velocity has magnitude $v$ and makes an angle of $30^\circ$ with the magnetic field direction; ignore gravity. (a) Describe the resulting motion (discuss separately the component of velocity parallel/perpendicular to the field). (b) Calculate the pitch (distance traveled along the field direction per revolution) of the helical path.
- **Ex 8.2**: A thin copper strip with thickness $t = 0.50\text{ mm}$ and width $w = 2.0\text{ cm}$ carries a current of $I = 15\text{ A}$ in the $+x$ direction. The strip is placed in a uniform magnetic field of magnitude $B = 1.5\text{ T}$ pointing in the $+z$ direction (perpendicular to the flat face of the strip). A Hall voltage of magnitude $V_H = 3.3\ \mu\text{V}$ is measured across the width of the strip. Assume that each carrier has a charge of magnitude $e$. (a) Calculate the drift velocity $v_d$ of the charge carriers. (b) Determine the number density $n$ (charge carriers per unit volume) in the copper.
- **Ex 8.3**: A magnetic field $B$ along the $+z$ axis is present in the $y \ge a$ region of the $xy$-plane. If we put a circular loop of radius $R \ (0 \le a < R)$ and current $I$ (counterclockwise seen from $+z$) in the $xy$ plane with its center located at the origin, what would the total force be on the loop?

---

**中文解析：**

**1. 匀强磁场中的螺旋线运动与螺距计算（Exercise 8.1）**：

- **(a)** 将初速度分解为平行于磁场的分量 $v_\parallel = v\cos 30^\circ = \frac{\sqrt{3}}{2}v$ 和垂直于磁场的分量 $v_\perp = v\sin 30^\circ = \frac{1}{2}v$：
  - 沿磁场方向不受洛伦兹力，粒子以恒定速度 $v_\parallel = \frac{\sqrt{3}}{2}v$ 作匀速直线运动；
  - 在垂直于磁场的平面内，粒子受洛伦兹力作用作匀速圆周运动，轨道半径为 $R = \frac{mv_\perp}{|q|B} = \dfrac{mv}{2|q|B}$，回旋角频率为 $\omega = \dfrac{|q|B}{m}$。两者合成为等距螺旋运动（Helical motion）。
- **(b)** 回旋周期为 $T = \frac{2\pi}{\omega} = \frac{2\pi m}{|q|B}$，故螺旋线的螺距（Pitch）为：
  $$
  p = v_\parallel T = \left(\frac{\sqrt{3}}{2}v\right)\left(\frac{2\pi m}{|q|B}\right) = \frac{\sqrt{3}\pi m v}{|q|B}
  $$

---

**2. 铜薄带霍尔效应的漂移速率与载流子浓度计算（Exercise 8.2）**：
统一化为国际单位：$t = 5.0 \times 10^{-4}\text{ m}$，$w = 2.0 \times 10^{-2}\text{ m}$，$I = 15\text{ A}$，$B = 1.5\text{ T}$，$V_H = 3.3 \times 10^{-6}\text{ V}$。

- **(a) 求载流子漂移速率 $v_d$**：
  霍尔平衡时横向电场 $E_H = \frac{V_H}{w} = v_d B$，故：
  $$
  v_d = \frac{V_H}{Bw} = \frac{3.3 \times 10^{-6}\text{ V}}{1.5\text{ T} \times 2.0 \times 10^{-2}\text{ m}} = 1.1 \times 10^{-4}\text{ m/s}
  $$
- **(b) 求载流子数密度 $n$**：
  横截面积为 $A = tw$，由 $I = nev_d A = nev_d tw$ 得：
  $$
  n = \frac{I}{e v_d t w} = \frac{IB}{e t V_H} = \frac{15 \times 1.5}{1.602 \times 10^{-19} \times 5.0 \times 10^{-4} \times 3.3 \times 10^{-6}} \approx 8.5 \times 10^{28}\text{ m}^{-3}
  $$

---

**3. 局部半平面磁场中载流圆环所受的总安培力（Exercise 8.3）**：
圆环只有位于 $y \ge a$ 区域内的圆弧段受到磁场 $\vec{B} = B\hat{z}$ 的作用。圆环方程为 $x^2 + y^2 = R^2$，与边界直线 $y = a$ 的两个交点坐标为 $(\pm\sqrt{R^2 - a^2}, a, 0)$。
由于电流 $I$ 沿逆时针方向流动，电流在右交点 $P_{\text{in}} = (+\sqrt{R^2 - a^2}, a, 0)$ 进入磁场区，在左交点 $P_{\text{out}} = (-\sqrt{R^2 - a^2}, a, 0)$ 离开磁场区。
在匀强磁场中，弯曲圆弧所受安培力等于从起点指向终点的等效直导线弦矢量 $\vec{L}_{\text{eff}} = \int_{\text{arc}} d\vec{l} = P_{\text{out}} - P_{\text{in}} = -2\sqrt{R^2 - a^2}\,\hat{x}$ 所受的安培力：

$$
\vec{F} = I\vec{L}_{\text{eff}} \times \vec{B} = I\left(-2\sqrt{R^2 - a^2}\,\hat{x}\right) \times (B\hat{z}) = +2IB\sqrt{R^2 - a^2}\,\hat{y}
$$

即圆环所受总磁场力大小为 $2IB\sqrt{R^2 - a^2}$，方向沿 $+y$ 轴方向。

</details>

<details markdown="1">
<summary>Exercise 8.4 & 8.5: Rotating Charged Disk Torque & Cyclotron Orbit Analysis（旋转带电圆盘磁力矩与回旋加速器能量及加速次数）</summary>

**Problem Statement:**
- **Ex 8.4**: A plastic disk is rotating with angular velocity $\omega$ in a uniform magnetic field $\vec{B}$ that is perpendicular to the disk's rotating axis (`Figure 8.4`). The disk has radius $R$, and it has a uniform surface charge density $\sigma$. Compute the magnitude of the total torque exerted by the magnetic field on the disk.
- **Ex 8.5**: In a cyclotron the two dees have radius $R$ and lie in a uniform magnetic field of magnitude $B$ perpendicular to the plane of the orbits. A particle of mass $m$ and charge $q > 0$ starts from rest at the center and is accelerated across the gap between the dees every time it crosses, by a potential difference of magnitude $V$. Neglect the time spent in the gap and any relativistic correction. (a) Find the kinetic energy of the particle when its orbit has grown to radius $R$, and show that it does not depend on $V$. (b) Find the number of gap crossings needed to reach that energy, assuming $V$ is such that this number comes out whole. Say in one line what limits the energy the machine delivers when it does not.

---

**中文解析：**

**1. 旋转均匀带电绝缘圆盘在磁场中所受的总力矩（Exercise 8.4，经典必考题）**：
将半径为 $R$ 的圆盘分割为无数个半径为 $r$、径向宽度为 $dr$ 的同心细圆环。
每个细圆环的面积为 $dS = 2\pi r\,dr$，所带电荷量为 $dq = \sigma\,dS = 2\pi\sigma r\,dr$。
当圆盘以角速度 $\omega$（周期 $T = \frac{2\pi}{\omega}$）绕中心轴旋转时，该细圆环等效于一个环形电流，其微元电流强度为：

$$
di = \frac{dq}{T} = \frac{2\pi\sigma r\,dr}{2\pi / \omega} = \sigma\omega r\,dr
$$

该环形电流所包围的圆面积为 $A(r) = \pi r^2$，因此它具有沿转轴方向的微元磁偶极矩 $d\mu = A(r)\,di = \pi\sigma\omega r^3\,dr$。
从盘心 $r = 0$ 积分至边缘 $r = R$，得到整个旋转圆盘的总磁偶极矩大小：

$$
\mu = \int_0^R \pi\sigma\omega r^3\,dr = \frac{1}{4}\pi\sigma\omega R^4
$$

由于外磁场 $\vec{B}$ 垂直于圆盘转轴（即 $\vec{\mu} \perp \vec{B}$，夹角 $\theta = 90^\circ$），由 $\vec{\tau} = \vec{\mu}\times\vec{B}$ 可得磁场对圆盘施加的总力矩大小为：

$$
\tau = \mu B \sin 90^\circ = \frac{1}{4}\pi\sigma\omega B R^4
$$

---

**2. 回旋加速器的最大动能与狭缝加速次数（Exercise 8.5）**：

- **(a)** 当粒子轨道半径增长到 D 形盒的最大半径 $R$ 时，由向心力公式 $qv_{\max}B = \frac{mv_{\max}^2}{R}$ 解得最大速率 $v_{\max} = \frac{qBR}{m}$。此时的最终动能为：
  $$
  K = \frac{1}{2}mv_{\max}^2 = \frac{q^2 B^2 R^2}{2m}
  $$
  可见最终动能仅由加速器的磁感应强度 $B$、D 形盒半径 $R$ 以及粒子的属性 $q, m$ 决定，**与加速电压 $V$ 的大小完全无关**（$V$ 较小只会导致粒子需要绕行更多圈才能达到半径 $R$）。
- **(b)** 粒子每穿过一次狭缝，电场力做功使其动能增加 $\Delta K = qV$。因此达到最大动能所需的狭缝穿越次数为：
  $$
  N = \frac{K}{\Delta K} = \frac{q B^2 R^2}{2mV}
  $$
  若该比值不是整数，则粒子所能达到的能量受限于轨道半径不超过 $R$ 的最大整数次加速（即 $\lfloor N \rfloor qV$，因为下一次加速后轨道半径将超出 D 形盒边界 $R$ 而撞壁或被引出）。

</details>

<details markdown="1">
<summary>Exercise 8.6, 8.7, 8.8 & 8.9: Crossed/Parallel E-B Trajectories, Mass Spectrometer & Motional Rod Work Paradox（复合场轨迹、质谱仪与滑杆安培力做功佯谬）</summary>

**Problem Statement:**
- **Ex 8.6**: Uniform, time-independent fields $\vec{E} = E\hat{z}$ and $\vec{B} = B\hat{z}$ ($E, B > 0$) fill all of space. At $t = 0$ a particle ($m, q > 0$) is at the origin with $\vec{v}(0) = v_\perp\hat{x} - u\hat{z}$ ($v_\perp, u > 0$). (a) Find the position and velocity of the particle at the first time $t_* > 0$ at which it returns to the plane $z = 0$. (b) Find the values of $E$ for which it returns to the origin itself at that moment.
- **Ex 8.7**: Uniform fields $\vec{E} = E\hat{x}$ and $\vec{B} = B\hat{z}$ ($E, B > 0$) fill all of space. At $t = 0$ a particle ($m, q \neq 0$) is released from rest at the origin. (a) Find the average velocity over one cyclotron period $T = 2\pi m/(|q|B)$, and show it is the same for every $q$ and $m$. (b) Find the largest value of $|x|$ that the particle reaches, and state for which sign of $q$ it moves toward $+x$.
- **Ex 8.8**: A beam of positive ions ($q > 0$) travels along $-\hat{y}$ into a velocity selector with $\vec{E}_1 = E_1\hat{x}$ and $\vec{B}_1 = B_1\hat{z}$ ($E_1, B_1 > 0$). Undeflected ions pass through a slit at the origin into a second region with uniform $\vec{B}_2 = B_2\hat{z}$ ($B_2 > 0$), turn through a half circle, and strike a detector on $x < 0, y = 0$. (a) Find the speed the selector transmits. (b) Two isotopes of masses $m_1, m_2$ cross the selector; find the distance between the two points at which they strike the detector.
- **Ex 8.9**: A straight conducting rod of length $L$ slides without friction along two horizontal rails a distance $L$ apart, in a uniform magnetic field $B$ perpendicular to the rails. A source maintains a steady current $i = nqv_d A$ ($q > 0$) in the rod. At the instant considered the rod moves along the rails with speed $u$ in the direction of the Ampère force. (a) Find the rate at which the Ampère force $i\vec{L}\times\vec{B}$ does work on the rod. (b) Each carrier moves with drift velocity $\vec{v}_d$ along the rod and with velocity $\vec{u}$ along the rails. Find the total rate at which the magnetic force does work on all the carriers in the rod, and reconcile it with your answer to (a).

---

**中文解析：**

**1. 平行电磁场中的折返运动与重回原点条件（Exercise 8.6）**：

- **(a)** 沿 $z$ 方向粒子受恒定电场力，加速度为 $a_z = \frac{qE}{m} > 0$，初速度为 $v_z(0) = -u$。由 $z(t) = -ut + \frac{1}{2}a_z t^2 = 0$ 解得首次返回 $z = 0$ 平面的时刻为：
  $$
  t_* = \frac{2u}{a_z} = \frac{2mu}{qE}, \qquad \text{此时 } v_z(t_*) = -u + a_z t_* = +u
  $$
  在 $xy$ 平面内，初速度为 $v_\perp\hat{x}$，初始洛伦兹力为 $qv_\perp B(\hat{x}\times\hat{z}) = -qv_\perp B\hat{y}$，故粒子在 $xy$ 平面内绕圆心 $(0, -R, 0)$（其中 $R = \frac{mv_\perp}{qB}$）以角频率 $\omega = \frac{qB}{m}$ 作顺时针匀速圆周运动：$v_x(t) = v_\perp\cos(\omega t), \ v_y(t) = -v_\perp\sin(\omega t)$，$x(t) = R\sin(\omega t), \ y(t) = R(\cos(\omega t) - 1)$。
  将 $t_* = \frac{2mu}{qE}$ 代入（记旋转角 $\theta_* = \omega t_* = \frac{2Bu}{E}$），得到该时刻的位置与速度矢量：
  $$
  \vec{r}(t_*) = \frac{mv_\perp}{qB}\left[ \sin\left(\frac{2Bu}{E}\right)\hat{x} + \left(\cos\left(\frac{2Bu}{E}\right) - 1\right)\hat{y} \right]
  $$
  $$
  \vec{v}(t_*) = v_\perp\cos\left(\frac{2Bu}{E}\right)\hat{x} - v_\perp\sin\left(\frac{2Bu}{E}\right)\hat{y} + u\hat{z}
  $$
- **(b)** 要使粒子在 $t_*$ 时刻恰好回到原点 $(0, 0, 0)$，要求在 $t_*$ 时间内粒子在 $xy$ 平面内刚好完成整数圈回旋，即 $\theta_* = \omega t_* = 2n\pi \ (n = 1, 2, 3, \dots)$：
  $$
  \frac{2Bu}{E} = 2n\pi \implies E = \frac{Bu}{n\pi}, \qquad n = 1, 2, 3, \dots
  $$

---

**2. 正交电磁场中摆线运动的周期平均速度与最大横向位移（Exercise 8.7）**：

- **(a)** 由 §2.2（Example 8.1）的解，设带符号的 $\omega = \frac{qB}{m}$，则 $v_x(t) = \frac{E}{B}\sin(\omega t)$，$v_y(t) = \frac{E}{B}(\cos(\omega t) - 1)$。在一个完整回旋周期 $T = \frac{2\pi}{|\omega|} = \frac{2\pi m}{|q|B}$ 内，$\sin(\omega t)$ 与 $\cos(\omega t)$ 的积分平均值均为零，因此平均速度为：
  $$
  \langle\vec{v}\rangle = \frac{1}{T}\int_0^T \vec{v}(t)\,dt = -\frac{E}{B}\hat{y} = \frac{\vec{E}\times\vec{B}}{B^2}
  $$
  它仅由外场 $E, B$ 决定，对任何电荷 $q$（无论正负）和质量 $m$ 均完全相同。
- **(b)** 对 $v_x(t)$ 积分得 $x(t) = \frac{E}{\omega B}(1 - \cos(\omega t)) = \frac{mE}{qB^2}(1 - \cos(\omega t))$。
  当 $\cos(\omega t) = -1$ 时，$|x|$ 达到最大值：
  $$
  |x|_{\max} = \frac{2mE}{|q|B^2}
  $$
  由于 $1 - \cos(\omega t) \ge 0$，当 **$q > 0$（正电荷）**时，$x(t) \ge 0$，粒子向 $+x$ 方向偏移运动。

---

**3. 速度选择器（Velocity Selector）与质谱仪（Mass Spectrometer）同位素分离（Exercise 8.8）**：

- **(a)** 正离子沿 $-\hat{y}$ 进入速度选择器（$\vec{v} = -v\hat{y}$），所受电场力为 $+qE_1\hat{x}$，洛伦兹力为 $q(-v\hat{y})\times(B_1\hat{z}) = -qvB_1\hat{x}$。不偏转通过狭缝要求二力平衡：
  $$
  qE_1 - qvB_1 = 0 \implies v = \frac{E_1}{B_1} \qquad (\text{与离子的质量 } m \text{ 和电荷 } q \text{ 均无关})
  $$
- **(b)** 进入只有匀强磁场 $\vec{B}_2 = B_2\hat{z}$ 的第二区域后，质量为 $m_i$ 的同位素向左偏转（$-x$ 方向）作半圆周运动，打在探测器平面 $y = 0$ 上的位置距原点（狭缝）的距离等于圆轨道直径 $D_i = 2R_i = \frac{2m_i v}{qB_2}$。因此两种同位素落点之间的距离为：
  $$
  \Delta x = |D_1 - D_2| = \frac{2|m_1 - m_2|v}{qB_2} = \frac{2|m_1 - m_2|E_1}{q B_1 B_2}
  $$

---

**4. 导轨滑杆模型：宏观安培力做功与微观洛伦兹力不做功的调和（Exercise 8.9，深度概念压轴题）**：

- **(a) 宏观安培力对滑杆做功的功率**：
  滑杆受宏观安培力大小为 $F_{\text{Amp}} = iLB$，方向与滑杆沿导轨的运动速度 $\vec{u}$ 相同。因此安培力对滑杆做功的功率（机械功率）为：
  $$
  P_{\text{mech}} = F_{\text{Amp}} u = iLBu
  $$
- **(b) 微观洛伦兹力对所有载流子做功的总功率及佯谬调和**：
  每个正载流子 $q > 0$ 同时具有沿导杆方向的漂移速度 $\vec{v}_d$ 和随导杆沿导轨运动的速度 $\vec{u}$（二者相互垂直：$\vec{v}_d \perp \vec{u}$），故载流子的总速度为 $\vec{v}_{\text{tot}} = \vec{v}_d + \vec{u}$。
  对应的微观洛伦兹力 $\vec{F}_B = q(\vec{v}_d + \vec{u})\times\vec{B}$ 可分解为两个正交分量：
  1. **沿导轨方向的分量** $\vec{F}_{\parallel\text{rail}} = q\vec{v}_d\times\vec{B}$（大小为 $qv_d B$，与导杆速度 $\vec{u}$ 同向）：该分量通过霍尔侧面挤压传递给导杆晶格，宏观上表现为推动导杆前进的安培力，其做功功率为：
     $$
     P_{\text{rail}} = N(qv_d B)u = (nAL)qv_d Bu = (nqv_d A)LBu = +iLBu
     $$
  2. **沿导杆方向的分量** $\vec{F}_{\parallel\text{rod}} = q\vec{u}\times\vec{B}$（大小为 $quB$，方向与载流子漂移速度 $\vec{v}_d$ **相反**，即下一章的动生反电动势）：该分量阻碍载流子沿导杆的漂移运动，对载流子做**负功**，功率为：
     $$
     P_{\text{rod}} = N(-quB)v_d = -(nAL)quBv_d = -(nqv_d A)LBu = -iLBu
     $$
  将两部分相加，**微观洛伦兹力对所有载流子做功的总功率恒等于零**：
  $$
  P_{\text{total magnetic}} = P_{\text{rail}} + P_{\text{rod}} = +iLBu - iLBu = 0
  $$
  **物理本质调和**：由于 $\vec{F}_B \perp \vec{v}_{\text{tot}}$，**磁场本身绝不提供任何能量（总做功恒为零）**！在这里，磁场扮演了一个纯粹的**“能量中转站 / 换向器”**：外部维持恒定电流 $i$ 的电源必须克服沿杆反向的磁力分量 $quB$（反电动势 $BLu$）额外输出电功率 $P_{\text{source}} = iLBu$（通过 $P_{\text{rod}} = -iLBu$ 输入系统），而磁场通过另一个正交分量 $P_{\text{rail}} = +iLBu$ 将这部分由电源提供的电能一分不少地转化为了导杆宏观运动的机械能！

</details>