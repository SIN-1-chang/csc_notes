# Chapter 2: Continuous Charge and Gauss' Law（连续电荷分布与高斯定理）

!!! abstract
    General Physics II (Electromagnetism) | 第二章课堂与讲义笔记
    
    参考：
    
    - Lecture 2: *Continuous Charge and Gauss' Law* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 2: *Gauss' Law* & Halliday, Resnick & Krane, *Physics*, Chapters 25 & 27

## 1 连续电荷分布的电场 (Electric Field due to a Continuous Charge Distribution)

### 1.1 微元积分法与对称性简化

当带电体尺度和观测距离相当时，需要将连续带电体分割为无穷多个微小的电荷元（Differential elements of charge）$dq$，每个电荷元可视为点电荷并在场点 $P$ 产生微元电场 $d\vec{E}$：

$$
d\vec{E} = \frac{1}{4\pi\epsilon_0} \frac{dq}{r^2} \hat{r} \implies \vec{E} = \int d\vec{E}
$$

在直接积分前，通常先将矢量 $d\vec{E}$ 分解为正交分量（Decompose into components），并利用系统的几何对称性（Symmetry）判断哪些分量相互抵消（Cancel out），仅对相互叠加的分量进行积分。

### 1.2 均匀带电细圆环与圆盘轴线上的电场

**1. 均匀带电细圆环（A Ring of Charge）**

设半径为 $R$ 的细圆环均匀带有总电荷 $q > 0$，其**线电荷密度**（Linear charge density，单位长度电荷量）为 $\lambda = \frac{q}{2\pi R}$。考察圆环中心轴线上距环心为 $z$ 的点 $P$：

- **微元与对称性分析**：取弧长微元 $ds$，其电荷量为 $dq = \lambda\,ds$，到点 $P$ 的距离为 $r = \sqrt{z^2 + R^2}$。由于圆环关于中心轴旋转对称，$d\vec{E}$ 垂直于 $z$ 轴的分量成对抵消，仅剩沿 $z$ 轴的分量 $dE_z = dE\cos\theta$，其中 $\cos\theta = \frac{z}{r} = \frac{z}{(z^2 + R^2)^{1/2}}$。
- **积分求解**：由于环上各微元到点 $P$ 的距离 $r$ 与倾角 $\theta$ 均相同，沿整圈周长 $\int ds = 2\pi R$ 积分得：
  $$
  E_z = \int dE_z = \frac{z\lambda}{4\pi\epsilon_0(z^2 + R^2)^{3/2}} \int_0^{2\pi R} ds = \frac{qz}{4\pi\epsilon_0(z^2 + R^2)^{3/2}}
  $$
- **极限情况检验（Checking Limiting Cases）**：
  1. **远场极限（$z \gg R$）**：忽略分母中的 $R^2$，得 $E \approx \frac{1}{4\pi\epsilon_0}\frac{q}{z^2}$，即从极远处观察时，圆环退化为一个点电荷；
  2. **环心极限（$z = 0$）**：代入得 $E_z = 0$，符合关于 $z = 0$ 平面的镜像对称性（Mirror symmetry）。

**2. 均匀带电圆盘（A Charged Disk）**

设半径为 $R$ 的绝缘圆盘表面均匀带有正电荷，其**面电荷密度**（Surface charge density，单位面积电荷量）为 $\sigma = \frac{Q}{\pi R^2}$。求中心轴线上 $z > 0$ 处的电场：

- **复用细圆环结论（Recycling the Ring Result）**：将圆盘分割为半径为 $r$、径向宽度为 $dr$ 的同心细圆环（Concentric thin rings），微元面积为 $dA = 2\pi r\,dr$，所带电荷为 $dq = \sigma\,dA = \sigma(2\pi r\,dr)$。
- **直接套用圆环公式积分**：将圆环公式中的 $R$ 替换为 $r$、$q$ 替换为 $dq$，从盘心 $r = 0$ 积分至边缘 $r = R$：
  $$
  E_z = \int_0^R \frac{z\sigma(2\pi r\,dr)}{4\pi\epsilon_0(z^2 + r^2)^{3/2}} = \frac{\sigma z}{4\epsilon_0} \int_0^R (z^2 + r^2)^{-3/2}\,d(r^2) = \frac{\sigma}{2\epsilon_0}\left[1 - \frac{z}{\sqrt{z^2 + R^2}}\right]
  $$
  （若采用极坐标二重积分 $dS = r\,dr\,d\phi$，结果完全一致；对于 $z < 0$ 的一侧，由镜像对称性知电场方向相反，合并可写为含 $\operatorname{sgn}(z)$ 的形式）。

---

## 2 电通量与高斯定理 (Electric Flux and Gauss' Law)

### 2.1 电通量的定义与符号约定

为了克服直接微元积分的繁琐计算，我们借助对称性与**电通量**（Electric Flux，定量描述穿过某个曲面的电场线数量）来建立电荷与电场的全局关系。

1. **匀强场与平面微元**：对于面积为 $\Delta A$ 的微小平面块（Small patch），定义垂直于表面且模长等于面积的**面积矢量**（Area Vector）$\Delta\vec{A} = \Delta A\,\hat{n}$。当匀强电场 $\vec{E}$ 与法线夹角为 $\theta$ 时，穿过该面元的电通量为：
   $$
   \Delta\Phi = (E\cos\theta)\Delta A = \vec{E} \cdot \Delta\vec{A}
   $$
2. **一般曲面上的电通量**：对弯曲曲面或非均匀电场，将曲面细分为无穷小面元 $d\vec{A} = \hat{n}\,dA$（讲义中亦记作 $d\vec{S}$）并积分：
   $$
   \Phi = \int_S \vec{E} \cdot d\vec{A}
   $$
   电通量 $\Phi$ 是**标量**（Scalar），其国际单位制（SI unit）为 $\text{N}\cdot\text{m}^2/\text{C}$。
3. **闭合高斯面（Closed Gaussian Surface）的法向约定**：
   对于任意假想闭合曲面（高斯面），规定面积矢量 $d\vec{A}$ 的方向永远**由内向外**（Pointing outward from the interior）。由此得到三种穿透情形的通量符号：

| 电场线与高斯面的几何关系 | 夹角 $\theta$ 范围 | 局部电通量 $\Delta\Phi$ 符号 |
| :--- | :---: | :--- |
| **向外穿出（Pierce outward）** | $\theta < 90^\circ$ | **正通量（Positive flux，$\Delta\Phi > 0$）** |
| **掠过表面（Skim the surface）** | $\theta = 90^\circ$ | **零通量（Zero flux，$\Delta\Phi = 0$）** |
| **向内穿入（Pierce inward）** | $\theta > 90^\circ$ | **负通量（Negative flux，$\Delta\Phi < 0$）** |

穿过整个闭合高斯面的**净电通量**（Net Flux）记为环路曲面积分 $\Phi = \oint_S \vec{E} \cdot d\vec{A}$。

<details markdown="1">
<summary>课堂例题（Example 2.1）：匀强电场中穿过半球面的电通量</summary>

设半径为 $R$ 的半球面（Hemisphere）轴线沿 $+z$ 方向，外法线沿径向 $\hat{r}$。匀强电场 $\vec{E}$ 位于 $xz$ 平面内且与 $+z$ 轴夹角为 $\alpha$，即 $\vec{E} = E(-\hat{x}\sin\alpha + \hat{z}\cos\alpha)$。

在球坐标系 $(R, \theta, \phi)$ 下，球面微元为 $d\vec{S} = R^2\sin\theta\,d\theta\,d\phi\,\hat{r}$，其中 $\hat{r} = \hat{x}\sin\theta\cos\phi + \hat{y}\sin\theta\sin\phi + \hat{z}\cos\theta$。计算积分：

$$
\Phi = \int_S \vec{E}\cdot d\vec{S} = ER^2 \int_0^{\pi/2} \sin\theta\,d\theta \int_0^{2\pi} d\phi (-\sin\alpha\sin\theta\cos\phi + \cos\alpha\cos\theta)
$$

由于 $\int_0^{2\pi} \cos\phi\,d\phi = 0$，第一项积分为零，仅剩第二项：

$$
\Phi = ER^2 \cdot 2\pi\cos\alpha \int_0^{\pi/2} \sin\theta\cos\theta\,d\theta = E\pi R^2\cos\alpha
$$

</details>

### 2.2 高斯定理 (Gauss' Law) 及其与库仑定律的等价性

**高斯定理（Gauss' Law）**：在真空中，穿过任意闭合高斯面 $S$ 的净电通量 $\Phi$ 与该曲面所包围的**净电荷量**（Net Enclosed Charge）$q_{\text{enc}}$ 满足：

$$
\epsilon_0 \Phi = q_{\text{enc}} \iff \epsilon_0 \oint_S \vec{E} \cdot d\vec{A} = q_{\text{enc}} = \int_V \rho\,dV
$$

- 当 $q_{\text{enc}} > 0$ 时，净电通量向外（$\Phi > 0$，内部存在净正电荷“源” Source）；
- 当 $q_{\text{enc}} < 0$ 时，净电通量向内（$\Phi < 0$，内部存在净负电荷“汇” Drain）；
- 当 $q_{\text{enc}} = 0$ 时（内部无电荷，或所含正负电荷代数和为零），净电通量恒为零（$\Phi = 0$）。

!!! note "高斯定理的四点核心物理理解"
    1. **公式中 $\vec{E}$ 与 $q_{\text{enc}}$ 的关系**：积分号内的 $\vec{E}$ 是**空间所有电荷（既包含高斯面内部电荷，也包含外部电荷）**在高斯面上产生的总合电场；但**高斯面外部的电荷对闭合面净电通量的贡献恒为零**（因为外部电荷发出的电场线一旦穿入高斯面，必定从另一侧穿出，进出条数严格相等）。
    2. **与库仑定律的等价性及三维空间几何因子 $4\pi$**：以点电荷 $q$ 为中心作半径为 $r$ 的球形高斯面，由球对称性得 $\epsilon_0 E(4\pi r^2) = q \implies E = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}$。这表明常数中的 $4\pi$ 本质上源于三维空间球面面积 $4\pi r^2$（或全空间立体角 $\oint d\Omega = 4\pi$）的**几何因子**（Geometric factor），而高斯定理成立意味着静电力必然严格遵循**平方反比律**（Inverse-square law，$1/r^2$）。
    3. **普适性**：高斯定理是麦克斯韦方程组（Maxwell's equations）的四大方程之一，不仅适用于静电场，对运动电荷和随时间变化的动态场依然严格成立。
    4. **远场渐近特征（Revisit Quiz 1-1）**：对于包含多个点电荷的复杂系统（例如两个 $+Q$ 与一个 $-Q$），只要系统的总净电荷 $q_{\text{net}} = Q \neq 0$，在远离电荷分布区的远场尺度下，其电场线分布就趋近于单个点电荷 $Q$ 的径向辐射场。

---

## 3 高斯定理在对称绝缘带电体中的应用 (Applications to Charged Insulators)

当电荷分布具有**球对称**（Spherical symmetry）、**平面对称**（Planar symmetry）或**柱对称**（Cylindrical symmetry）时，通过构造与对称性匹配的高斯面，可将场强模长 $E$ 移出积分号，仅用几行代数即可求出电场分布。

### 3.1 球对称体系 (Spherical Symmetry)

球对称是指电荷体密度 $\rho(r)$ 仅依赖于距球心的径向距离 $r$，而与角度 $(\theta, \phi)$ 无关。统一选取**半径为 $r$ 的同心球面**作为高斯面（面积为 $4\pi r^2$）。

**1. 均匀带电薄球壳（Uniformly Charged Spherical Shell，半径 $R$，总电荷 $Q$）**

- **球壳外部（$r > R$）**：高斯面包含全部电荷 $q_{\text{enc}} = Q$，故 $4\pi r^2 E = \frac{Q}{\epsilon_0} \implies \vec{E} = \frac{Q}{4\pi\epsilon_0 r^2}\hat{r}$（等效于全部电荷集中在球心的点电荷）。
- **球壳内部（$r < R$）**：高斯面内部不包围任何电荷 $q_{\text{enc}} = 0$，故 $4\pi r^2 E = 0 \implies \vec{E} = \vec{0}$（球壳对内部空间不产生电场）。

**2. 均匀带电实心绝缘球（Uniformly Charged Solid Sphere，半径 $R$，总电荷 $q$）**

将实心球视为一层层同心薄球壳的叠加（Shell-by-shell theorem）：在半径 $r < R$ 处，位于 $r$ 外部的球壳对该点不产生电场，只有半径小于 $r$ 的内部球体产生贡献：

- **球体外部（$r \ge R$）**：$q_{\text{enc}} = q \implies \vec{E} = \dfrac{q}{4\pi\epsilon_0 r^2}\hat{r}$。
- **球体内部（$r \le R$）**：高斯球面包围的电荷量按体积比缩放为 $q' = q_{\text{enc}} = q\left(\frac{r}{R}\right)^3$。代入高斯定理 $(4\pi r^2)E = \frac{q'}{\epsilon_0}$：
  $$
  E = \frac{q}{4\pi\epsilon_0 R^3} r \implies \vec{E}(\vec{r}) = \left(\frac{q}{4\pi\epsilon_0 R^3}\right)\vec{r} = \frac{\rho}{3\epsilon_0}\vec{r} \qquad (r \le R)
  $$
  即均匀带电球体内部的电场强度与到球心的距离 $r$ 成正比。

### 3.2 平面对称体系 (Planar Symmetry)

平面对称是指电荷密度 $\rho(z)$ 仅依赖于直角坐标 $z$。统一选取跨接带电平面的**圆柱形高斯“药盒”**（Cylindrical Pillbox，两底面平行于带电平面，底面积均为 $A$）。

**无限大均匀带电绝缘薄板（Infinite Nonconducting Sheet，面电荷密度 $\sigma$）**：
由平面对称性与镜像反射不变性，电场 $\vec{E}$ 必垂直于薄板向外（$\sigma > 0$）或向内（$\sigma < 0$），且在薄板两侧等距处大小相等：$E_z(-z) = -E_z(z)$。因此圆柱药盒的侧面（Curved side）无电通量穿过，只有两个底面（End caps）各有通量 $EA$：

$$
\epsilon_0(EA + EA) = q_{\text{enc}} = \sigma A \implies E = \frac{\sigma}{2\epsilon_0}, \qquad \vec{E}(z) = \frac{\sigma}{2\epsilon_0}\operatorname{sgn}(z)\hat{z}
$$

这一结果与前文带电圆盘在 $R \to \infty$（或 $z \ll R$）时的极限完全吻合。

### 3.3 柱对称体系 (Cylindrical Symmetry)

柱对称是指电荷密度仅依赖于柱坐标系下距中心轴的垂直距离 $r$。统一选取与带电体同轴的**半径为 $r$、高为 $h$ 的闭合圆柱面**作为高斯面。

**无限长均匀带电直导线 / 细杆（Infinite Line / Rod of Charge，线电荷密度 $\lambda$）**：
由柱对称性，电场 $\vec{E}$ 必沿径向垂直于轴线向外（$\lambda > 0$）或向内（$\lambda < 0$）。闭合圆柱面的上下两个平底面与 $\vec{E}$ 平行（无通量），电通量仅穿过面积为 $2\pi r h$ 的圆柱侧面（Curved surface）：

$$
\Phi = E(2\pi r h), \quad \epsilon_0 \Phi = q_{\text{enc}} = \lambda h \implies E = \frac{\lambda}{2\pi\epsilon_0 r}
$$

四大经典对称模型的场强公式汇总对比如下表：

| 带电体几何模型 | 选用的高斯面 | 高斯定理核心方程 | 电场强度分布公式 |
| :--- | :--- | :--- | :--- |
| **均匀带电薄球壳**（半径 $R$，电量 $Q$） | 同心球面（半径 $r$） | $\epsilon_0(4\pi r^2 E) = q_{\text{enc}}$ | $E = \begin{cases} 0, & r < R \\ \dfrac{Q}{4\pi\epsilon_0 r^2}, & r > R \end{cases}$ |
| **均匀带电实心球**（半径 $R$，电量 $q$，体密度 $\rho$） | 同心球面（半径 $r$） | $\epsilon_0(4\pi r^2 E) = q\left(\dfrac{r}{R}\right)^3$ | $E = \begin{cases} \dfrac{qr}{4\pi\epsilon_0 R^3} = \dfrac{\rho r}{3\epsilon_0}, & r \le R \\ \dfrac{q}{4\pi\epsilon_0 r^2}, & r > R \end{cases}$ |
| **无限大均匀带电绝缘薄板**（面密度 $\sigma$） | 跨接薄板的圆柱药盒（底面积 $A$） | $\epsilon_0(2EA) = \sigma A$ | $E = \dfrac{\sigma}{2\epsilon_0}$（处处恒定，与距离无关） |
| **无限长均匀带电细直杆**（线密度 $\lambda$） | 同轴圆柱面（半径 $r$，高 $h$） | $\epsilon_0(2\pi r h E) = \lambda h$ | $E = \dfrac{\lambda}{2\pi\epsilon_0 r}$（反比于轴距 $r$） |

---

## 4 数学工具附录：球坐标系与曲面积分 (Appendices 2A & 2B)

<details markdown="1">
<summary>Appendix 2A: Spherical Coordinates（球坐标系的正交基矢、线元与体积元）</summary>

空间一点 $P$ 的**球坐标**（Spherical coordinates）记为 $(r, \theta, \phi)$，其中 $r \ge 0$ 为到原点的径向距离（Radial distance），$\theta \in [0, \pi]$ 为与 $+z$ 轴的夹角——**极角**（Polar angle），$\phi \in [0, 2\pi)$ 为在 $xy$ 平面投影与 $+x$ 轴的夹角——**方位角**（Azimuthal angle）。

**1. 与直角坐标 $(x, y, z)$ 的变换关系**：

$$
x = r\sin\theta\cos\phi, \qquad y = r\sin\theta\sin\phi, \qquad z = r\cos\theta
$$

**2. 正交单位基矢 $(\hat{r}, \hat{\theta}, \hat{\phi})$ 的分解表示**：
任意矢量可分解为 $\vec{A} = A_r\hat{r} + A_\theta\hat{\theta} + A_\phi\hat{\phi}$，其中三个正交单位基矢随点 $P$ 的角度变化而变化：

$$
\begin{aligned}
\hat{r} &= \sin\theta\cos\phi\,\hat{x} + \sin\theta\sin\phi\,\hat{y} + \cos\theta\,\hat{z} \\
\hat{\theta} &= \cos\theta\cos\phi\,\hat{x} + \cos\theta\sin\phi\,\hat{y} - \sin\theta\,\hat{z} \\
\hat{\phi} &= -\sin\phi\,\hat{x} + \cos\phi\,\hat{y}
\end{aligned}
$$

**3. 线元（Infinitesimal displacement）与体积元（Volume element）**：
在三个正交方向上的无穷小位移分量分别为 $dr$、$r\,d\theta$、$r\sin\theta\,d\phi$，因此位移线元、球面面元（固定 $r=R$）与空间体积元分别为：

$$
d\vec{s} = dr\,\hat{r} + r\,d\theta\,\hat{\theta} + r\sin\theta\,d\phi\,\hat{\phi}
$$

$$
d\vec{A}_{\text{sphere}} = R^2\sin\theta\,d\theta\,d\phi\,\hat{r} = R^2\,d\Omega\,\hat{r}, \qquad dV = (dr)(r\,d\theta)(r\sin\theta\,d\phi) = r^2\sin\theta\,dr\,d\theta\,d\phi
$$

</details>

<details markdown="1">
<summary>Appendix 2B: Surface Integral（一般曲面 z = f(x,y) 的法向量构造与投影曲面积分）</summary>

物理学中常遇到两类曲面积分：第一类是对标量函数（如电荷面密度 $\sigma$）的曲面积分 $\iint_S \sigma(x, y, z)\,dA$；第二类是对矢量场法向分量（如电通量）的曲面积分 $\iint_S \vec{F}\cdot d\vec{A} = \iint_S \vec{F}\cdot\hat{n}\,dA$。

**1. 显式曲面 $z = f(x, y)$ 的单位法向量 $\hat{n}$ 推导**：
在曲面 $z = f(x, y)$ 上的点 $P$ 处，分别平行于 $xz$ 平面和 $yz$ 平面构造两个不共线的切向量（Tangent vectors）：

$$
\vec{u} = u_x\hat{x} + \frac{\partial f}{\partial x}u_x\hat{z}, \qquad \vec{v} = v_y\hat{y} + \frac{\partial f}{\partial y}v_y\hat{z}
$$

将两切向量叉乘即可得到垂直于曲面的法向量 $\vec{N} = \vec{u}\times\vec{v} = \left(-\frac{\partial f}{\partial x}\hat{x} - \frac{\partial f}{\partial y}\hat{y} + \hat{z}\right)u_x v_y$。将其归一化，即得指向 $+z$ 一侧的**单位法向量**：

$$
\hat{n} = \frac{\vec{u}\times\vec{v}}{|\vec{u}\times\vec{v}|} = \frac{-\dfrac{\partial f}{\partial x}\hat{x} - \dfrac{\partial f}{\partial y}\hat{y} + \hat{z}}{\sqrt{1 + \left(\dfrac{\partial f}{\partial x}\right)^2 + \left(\dfrac{\partial f}{\partial y}\right)^2}}, \qquad \hat{n}\cdot\hat{z} = \frac{1}{\sqrt{1 + \left(\dfrac{\partial f}{\partial x}\right)^2 + \left(\dfrac{\partial f}{\partial y}\right)^2}}
$$

**2. 投影到 $xy$ 平面计算曲面积分（Projection Method）**：
曲面微元 $dA$ 在 $xy$ 平面上的投影矩形面积为 $dR = dx\,dy = (\hat{n}\cdot\hat{z})\,dA$，因此面积微元换元关系为 $dA = \sqrt{1 + (\partial_x f)^2 + (\partial_y f)^2}\,dx\,dy$。代入两类曲面积分即化为平面区域 $R$ 上的二重积分：

$$
\iint_S \sigma(x, y, z)\,dA = \iint_R \sigma\big(x, y, f(x, y)\big)\sqrt{1 + \left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2}\,dx\,dy
$$

$$
\iint_S \vec{F}\cdot d\vec{A} = \iint_R (\vec{F}\cdot\hat{n})\sqrt{1 + \left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2}\,dx\,dy = \iint_R \left[-\frac{\partial f}{\partial x}F_x - \frac{\partial f}{\partial y}F_y + F_z\right] dx\,dy
$$

</details>

---

## 5 Chapter 2 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 2.1, 2.2 & 2.3: Local Flux, Radial Field Density & Infinite Cylinder（局域通量密度、恒定径向场反推电荷密度与无限长圆柱）</summary>

**Problem Statement:**
- **Ex 2.1**: An electric field is given by $\vec{E} = y^2\hat{i} + (y - x^2)\hat{j} + \frac{xy}{z}\hat{k}$. At a point $\vec{r} = (3, 2, 1)$, please calculate the local flux per area if the local area vector is: (a) $\hat{i}\,dS$; (b) $\hat{j}\,dS$; (c) $\frac{1}{\sqrt{3}}(\hat{i} + \hat{j} + \hat{k})\,dS$.
- **Ex 2.2**: A spherically symmetric charge density $\rho(r)$ produces an electric field that points radially outward and has the same magnitude $E$ at every $r > 0$. Please give the expression of $\rho(r)$.
- **Ex 2.3**: Consider an infinitely long cylinder of radius $R$ and a uniform charge density $\rho_0 > 0$. Use Gauss' law to determine the magnitude of the electric field at a distance $r$ from the central axis of the cylinder. You should give the expressions of $E$ for both $r \le R$ and $r > R$.

---

**中文解析：**

**1. 局域面积通量密度计算（Exercise 2.1）**：
将坐标 $(x, y, z) = (3, 2, 1)$ 代入电场表达式，得该点处的电场矢量：

$$
\vec{E}(3, 2, 1) = 2^2\hat{i} + (2 - 3^2)\hat{j} + \frac{3 \times 2}{1}\hat{k} = 4\hat{i} - 7\hat{j} + 6\hat{k}
$$

单位面积的局域电通量即为 $\frac{d\Phi}{dS} = \vec{E} \cdot \hat{n}$：
- **(a)** $\hat{n} = \hat{i}$：$\vec{E}\cdot\hat{i} = 4$；
- **(b)** $\hat{n} = \hat{j}$：$\vec{E}\cdot\hat{j} = -7$；
- **(c)** $\hat{n} = \frac{1}{\sqrt{3}}(\hat{i} + \hat{j} + \hat{k})$：$\vec{E}\cdot\hat{n} = \frac{4 - 7 + 6}{\sqrt{3}} = \sqrt{3}$。

---

**2. 模长恒定的径向电场反推体电荷密度 $\rho(r)$（Exercise 2.2）**：
取半径为 $r$ 的同心球面作为高斯面，由球对称性及高斯定理：

$$
\epsilon_0 \oint_S \vec{E}\cdot d\vec{S} = q_{\text{enc}}(r) \implies \epsilon_0 (4\pi r^2 E) = \int_0^r \rho(r') 4\pi r'^2\,dr'
$$

由于场强大小 $E$ 为与 $r$ 无关的常数，将上式两边关于 $r$ 求导，利用微积分基本定理得：

$$
\epsilon_0 E \cdot 8\pi r = 4\pi r^2 \rho(r) \implies \rho(r) = \frac{2\epsilon_0 E}{r} \qquad (r > 0)
$$

---

**3. 无限长均匀带电圆柱体的电场分布（Exercise 2.3）**：
取半径为 $r$、长度为 $L$ 的同轴圆柱面作为高斯面。由柱对称性，电场沿径向向外且在侧面上大小处处相等，两端平底面法线与 $\vec{E}$ 垂直故无通量，因此总电通量为 $\Phi = 2\pi r L E(r)$：

- **当 $r \le R$（圆柱内部）**：高斯面内包围的电荷量为 $q_{\text{enc}} = \rho_0 (\pi r^2 L)$。由高斯定理：
  $$
  \epsilon_0 (2\pi r L E) = \rho_0 \pi r^2 L \implies E(r) = \frac{\rho_0 r}{2\epsilon_0} \qquad (r \le R)
  $$
- **当 $r > R$（圆柱外部）**：高斯面内包围的电荷量为整个圆柱段的总电荷 $q_{\text{enc}} = \rho_0 (\pi R^2 L)$。由高斯定理：
  $$
  \epsilon_0 (2\pi r L E) = \rho_0 \pi R^2 L \implies E(r) = \frac{\rho_0 R^2}{2\epsilon_0 r} \qquad (r > R)
  $$

</details>

<details markdown="1">
<summary>Exercise 2.4 & 2.5: Concentric Spherical Shells & Overlapping Charged Spheres（同心球壳屏蔽与两重叠带电球体交叠区匀强场）</summary>

**Problem Statement:**
- **Ex 2.4**: Two uniformly charged spherical shells are both centered at the origin, whose radii are $R_1$ and $R_2 \ (R_1 < R_2)$. Given that the surface charge density is $+\sigma \ (\sigma > 0)$ for the outer shell, and that the electric field is zero for any point located outside the outer shell, please calculate: (a) The surface charge density of the inner shell; (b) The magnitude of the electric field for $R_1 < r < R_2$; (c) The magnitude of the electric field inside the inner shell ($r < R_1$).
- **Ex 2.5**: Two uniformly charged balls, of radii $R_1$ and $R_2$ and charge densities $-\rho$ and $+\rho$ with $\rho > 0$, overlap: their centers are a distance $d < R_1 + R_2$ apart, and in the overlap region the two charge densities add. Let $\vec{d}$, with $|\vec{d}| = d$, be the vector from the center of the $-\rho$ ball to the center of the $+\rho$ ball. Please calculate both the magnitude and the direction of the electric field in the overlap region, in terms of $\rho$ and $\vec{d}$.

---

**中文解析：**

**1. 外部零电场的双同心球壳（Exercise 2.4）**：

- **(a)** 在外球壳外部 $r > R_2$ 区域取同心球面高斯面，因 $E = 0$，高斯面内包围的总净电荷必为零：
  $$
  q_{\text{enc}} = 4\pi R_1^2 \sigma_1 + 4\pi R_2^2 \sigma = 0 \implies \sigma_1 = -\frac{R_2^2}{R_1^2}\sigma
  $$
- **(b)** 当 $R_1 < r < R_2$ 时，高斯面仅包围内球壳电荷 $q_{\text{enc}} = 4\pi R_1^2 \sigma_1 = -4\pi R_2^2 \sigma$，由高斯定理 $4\pi r^2 E = \frac{|q_{\text{enc}}|}{\epsilon_0}$ 得场强大小为：
  $$
  E(r) = \frac{\sigma R_2^2}{\epsilon_0 r^2} \qquad (\text{方向指向球心})
  $$
- **(c)** 当 $r < R_1$ 时，高斯面内不包围任何电荷（$q_{\text{enc}} = 0$），故 $E(r) = 0$。

---

**2. 两个异号均匀带电球体交叠区（或偏心球腔）内的匀强电场（Exercise 2.5，高频必考模型）**：
由 §3.1 结论可知，体电荷密度为 $+\rho$ 的均匀带电实心球，在其内部任意一点（相对球心位置矢量为 $\vec{r}$）产生的电场矢量恒为：

$$
\vec{E}_{\text{inside}}(\vec{r}) = \frac{\rho}{3\epsilon_0}\vec{r}
$$

设 $-\rho$ 球的球心位于 $O_-$，$+\rho$ 球的球心位于 $O_+$，由题意知位移矢量 $\vec{d} = \overrightarrow{O_- O_+}$。
对于交叠区域（Overlap region）内的任意一点 $P$，记其相对于 $O_-$ 的位置矢量为 $\vec{r}_- = \overrightarrow{O_- P}$，相对于 $O_+$ 的位置矢量为 $\vec{r}_+ = \overrightarrow{O_+ P}$。由矢量三角形法则显然有：

$$
\vec{r}_- - \vec{r}_+ = \overrightarrow{O_- P} - \overrightarrow{O_+ P} = \overrightarrow{O_- O_+} = \vec{d}
$$

根据电场叠加原理，交叠区内任意点 $P$ 处的合电场等于两球各自在该点产生的内部电场的矢量和：

$$
\vec{E} = \vec{E}_+ + \vec{E}_- = \frac{+\rho}{3\epsilon_0}\vec{r}_+ + \frac{-\rho}{3\epsilon_0}\vec{r}_- = \frac{\rho}{3\epsilon_0}(\vec{r}_+ - \vec{r}_-) = -\frac{\rho}{3\epsilon_0}\vec{d}
$$

**结论**：交叠区域内是一个**处处均匀的匀强电场**！其大小为 $E = \dfrac{\rho d}{3\epsilon_0}$，方向为 $-\hat{d}$（即平行于两球心连线，由 $+\rho$ 球心指向 $-\rho$ 球心）。

</details>

<details markdown="1">
<summary>Exercise 2.6 & 2.7: Flux Through a Cube and a Circular Disk（立方体中心/顶点通量与圆盘/圆柱侧面通量）</summary>

**Problem Statement:**
- **Ex 2.6**: A point charge $q > 0$ and an imaginary cube of side $a$ are given. The normal of every face of the cube points out of the cube. (a) The charge sits at the center of the cube. Find the electric flux through each face. (b) The charge now sits at one corner of the cube. Find the electric flux through each of the six faces. (Hint: consider the eight identical cubes that share this corner.)
- **Ex 2.7**: A point charge $q > 0$ lies on the axis of a flat disk of radius $R$, at a distance $d > 0$ from the center of the disk. The normal of the disk points away from $q$. (a) The sphere of radius $\sqrt{d^2 + R^2}$ centered on $q$ passes through the rim of the disk. The disk and the part of this sphere on the far side of the disk from $q$ together enclose a region that contains no charge. Use Gauss' law for this closed surface to show that the flux through the disk equals the flux through that part of the sphere, and hence find the flux through the disk. Check your answer when $R \gg d$ and when $R \ll d$. (b) The charge is now at the center of a closed cylinder of radius $R$ and length $2d$ whose axis passes through $q$. Without evaluating any new integral, find the flux through the curved side of the cylinder.

---

**中文解析：**

**1. 立方体六个面的电通量巧解（Exercise 2.6）**：

- **(a) 电荷位于立方体中心**：由高斯定理，穿过整个立方体的总通量为 $\frac{q}{\epsilon_0}$。因六个面关于中心完全对称，每个面的电通量相等：
  $$
  \Phi_{\text{face}} = \frac{q}{6\epsilon_0}
  $$
- **(b) 电荷位于立方体的一个顶点（Corner）**：
  - 对于**相交于该顶点的 3 个相邻面**：点电荷发出的电场线始终平行于（掠过）这 3 个面（$\vec{E} \perp \hat{n}$），因此穿过这 3 个面的电通量均为 $\Phi_{\text{near}} = 0$。
  - 对于**不经过该顶点的另外 3 个远端面**：以该顶点为中心，用 $8$ 个完全相同的小立方体拼成一个边长为 $2a$ 的大立方体，使点电荷 $q$ 恰好位于大立方体的正中心。大立方体的总通量 $\frac{q}{\epsilon_0}$ 被其表面包含的 $8 \times 3 = 24$ 个等效小正方形面均分，因此穿过每个远端面的电通量为：
    $$
    \Phi_{\text{far}} = \frac{q}{24\epsilon_0}
    $$

---

**2. 圆盘电通量与闭合圆柱侧面电通量（Exercise 2.7）**：

- **(a) 穿过半径为 $R$ 的圆盘的电通量**：
  圆盘与以 $q$ 为球心、半径为 $r_0 = \sqrt{d^2 + R^2}$ 的远端球冠（Spherical cap）共同围成一个不含电荷的闭合空间。由高斯定理，从圆盘穿入该区域的通量必等于从球冠穿出的通量，故 $\Phi_{\text{disk}} = \Phi_{\text{cap}}$。
  在球冠上，电场处处沿径向且大小恒为 $E = \frac{q}{4\pi\epsilon_0 r_0^2}$。设圆盘边缘对 $q$ 的半张角为 $\theta_0$（满足 $\cos\theta_0 = \frac{d}{\sqrt{d^2 + R^2}}$），则球冠面积为 $\int_0^{\theta_0} 2\pi r_0^2\sin\theta\,d\theta = 2\pi r_0^2(1 - \cos\theta_0)$。因此：
  $$
  \Phi_{\text{disk}} = E \cdot S_{\text{cap}} = \frac{q}{2\epsilon_0}(1 - \cos\theta_0) = \frac{q}{2\epsilon_0}\left(1 - \frac{d}{\sqrt{d^2 + R^2}}\right)
  $$
  极限检验：当 $R \gg d$ 时，$\Phi_{\text{disk}} \to \frac{q}{2\epsilon_0}$（无限大平面截取点电荷一半的电场线）；当 $R \ll d$ 时，$(1 + R^2/d^2)^{-1/2} \approx 1 - \frac{R^2}{2d^2}$，故 $\Phi_{\text{disk}} \approx \frac{q}{4\pi\epsilon_0 d^2}\cdot (\pi R^2)$（远场小圆盘近似为轴线场强乘以圆盘面积）。
- **(b) 闭合圆柱体侧面的电通量**：
  点电荷 $q$ 位于高为 $2d$、半径为 $R$ 的闭合圆柱体正中心，总通量为 $\frac{q}{\epsilon_0}$，减去上下两个底面圆盘的通量 $2\Phi_{\text{disk}}$ 即得侧面（Curved side）通量：
  $$
  \Phi_{\text{side}} = \frac{q}{\epsilon_0} - 2\Phi_{\text{disk}} = \frac{q}{\epsilon_0}\frac{d}{\sqrt{d^2 + R^2}}
  $$

</details>

<details markdown="1">
<summary>Exercise 2.8, 2.9 & 2.10: Non-Symmetric Sphere, p-n Junction Slab & Modified Coulomb Law（非对称场平均、p-n结空间电荷区与库仑平方反比律检验）</summary>

**Problem Statement:**
- **Ex 2.8**: Two point charges, each $q > 0$, are fixed at $(0, 0, a)$ and $(0, 0, -a)$, where $a > 0$. Let $S$ be the sphere of radius $R > a$ centered at the origin, with its normal pointing outward. (a) Find the net electric flux through $S$. (b) Calculate the electric field at $(R, 0, 0)$ and $(0, 0, R)$ of $S$. (c) From (a), find the average outward component of the field over $S$, $\langle E_n \rangle = \frac{1}{4\pi R^2}\oint_S \vec{E}\cdot d\vec{S}$, and compare it with (b). Can Gauss' law alone give the electric field at every point of $S$? Why could it give the field of a uniformly charged spherical shell?
- **Ex 2.9**: In a simple model of a $p\text{-}n$ junction, the charge density depends only on $z$: $\rho(z) = -\rho_0$ for $-a < z < 0$, $\rho(z) = +\rho_0$ for $0 < z < a$, and $\rho(z) = 0$ for $|z| > a$, where $\rho_0 > 0$. (a) Treat the charge as a stack of thin charged plates to show that $E = 0$ for $|z| > a$. Explain why a pillbox placed symmetrically about $z = 0$ gives no information here. (b) Using a pillbox with one end in $z < -a$, find $E(z)$ for $-a < z < a$. Where is the magnitude of the field largest, and what is its value there?
- **Ex 2.10**: Suppose Coulomb's law were slightly different, so that a point charge $q > 0$ at the origin produced $\vec{E} = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}\left(\frac{r_0}{r}\right)^\delta \hat{r}$ ($\delta > 0$). (a) Calculate the flux of this field through a sphere of radius $R$ centered on $q$. Is the result consistent with Gauss' law? (b) Two concentric spheres of radii $R_1 < R_2$ centered on $q$ enclose a region with no charge. Calculate the net flux through this closed surface. Which property of the flux fails? What does this tell you about the exponent in Coulomb's law?

---

**中文解析：**

**1. 非球对称电荷分布下的高斯面平均值辨析（Exercise 2.8）**：

- **(a)** 球面 $S \ (R > a)$ 包围了两个 $+q$ 电荷，由高斯定理得净通量 $\Phi = \dfrac{2q}{\epsilon_0}$。
- **(b)** 由库仑定律直接叠加：
  在赤道点 $(R, 0, 0)$：$\vec{E}(R, 0, 0) = \dfrac{2qR}{4\pi\epsilon_0(R^2 + a^2)^{3/2}}\hat{x}$；
  在极点 $(0, 0, R)$：$\vec{E}(0, 0, R) = \frac{q}{4\pi\epsilon_0}\left[\frac{1}{(R-a)^2} + \frac{1}{(R+a)^2}\right]\hat{z} = \dfrac{q(R^2 + a^2)}{2\pi\epsilon_0(R^2 - a^2)^2}\hat{z}$。
- **(c)** 球面上的平均法向场强为 $\langle E_n \rangle = \frac{\Phi}{4\pi R^2} = \dfrac{2q}{4\pi\epsilon_0 R^2}$，恰好介于赤道较弱场强与极点较强场强之间。这说明当缺乏球对称性时，球面上各点 $E_n$ 并不相等，**单靠高斯定理只能给出球面上的积分平均值，而无法求出逐点场强**（均匀带电球壳之所以能用高斯定理求出逐点场强，是因为球对称性保证了球面上各点场强大小严格相等且方向均沿径向）。

---

**2. 半导体 $p\text{-}n$ 结空间电荷区的电场分布（Exercise 2.9）**：

- **(a)** 将 $-a < z < 0$ 与 $0 < z < a$ 视为无数层无限大带电薄板的堆叠，两侧总面电荷密度分别为 $-\rho_0 a$ 与 $+\rho_0 a$，在 $|z| > a$ 的外部区域两层产生的匀强电场等大反向，故 **$E(z) = 0 \ (|z| > a)$**。由于 $\rho(-z) = -\rho(z)$ 是关于 $z$ 的奇函数，导致电场满足偶对称 $E_z(-z) = +E_z(z)$（同向穿过对称药盒的两个底面，左进右出相互抵消），且对称药盒内包围的总净电荷恒为零，因此关于 $z=0$ 对称放置的药盒仅给出恒等式 $0 = 0$，无法解出 $E(z)$。
- **(b)** 取圆柱形高斯药盒，使其左底面固定在无场区 $z_1 < -a$（该底面 $E = 0$，无通量），右底面位于耗尽层内部 $z \in (-a, a)$：
  - 当 $-a < z \le 0$ 时：$q_{\text{enc}} = S \int_{-a}^z (-\rho_0)\,dz' = -\rho_0(z + a)S$，由 $\epsilon_0 E_z(z) S = q_{\text{enc}}$ 得 $E_z(z) = -\dfrac{\rho_0}{\epsilon_0}(a + z)$；
  - 当 $0 < z < a$ 时：$q_{\text{enc}} = S\left[-\rho_0 a + \int_0^z \rho_0\,dz'\right] = -\rho_0(a - z)S$，得 $E_z(z) = -\dfrac{\rho_0}{\epsilon_0}(a - z)$。
  合并写为 $\vec{E}(z) = -\dfrac{\rho_0}{\epsilon_0}(a - |z|)\hat{z} \ (|z| < a)$。在交界面 **$z = 0$ 处电场强度达到最大值**，最大模长为 $E_{\max} = \dfrac{\rho_0 a}{\epsilon_0}$。

---

**3. 库仑定律幂次修正对高斯定理的破坏（Exercise 2.10）**：

- **(a)** 穿过半径为 $R$ 的同心球面的通量为：
  $$
  \Phi(R) = 4\pi R^2 E(R) = \frac{q}{\epsilon_0}\left(\frac{r_0}{R}\right)^\delta
  $$
  当 $\delta \neq 0$ 时，通量依赖于高斯面半径 $R$，与高斯定理矛盾。
- **(b)** 对于无电荷的球壳区域 $R_1 < r < R_2$，穿过内外表面的净向外通量为：
  $$
  \Phi_{\text{net}} = \Phi(R_2) - \Phi(R_1) = \frac{q}{\epsilon_0}\left[\left(\frac{r_0}{R_2}\right)^\delta - \left(\frac{r_0}{R_1}\right)^\delta\right] < 0
  $$
  这意味着电场线在无电荷的真空区域内凭空消失（通量守恒性失效）！由此可见，**高斯定理的成立严格依赖于库仑定律中 $1/r^2$ 的精确平方反比幂次（$\delta \equiv 0$）**。

</details>