# Chapter 4: The Triangle of Electrostatics（静电学三角关系）

!!! abstract
    General Physics II (Electromagnetism) | 第四章课堂与讲义笔记
    
    参考：
    
    - Lecture 4: *The Triangle of Electrostatics* (Xin Lu / Gentaro Watanabe, ZJU)
    - Course Handout Chapter 4: *Triangle of Electrostatics*
    - D. J. Griffiths, *Introduction to Electrodynamics* & Halliday, Resnick & Krane, *Physics*, Chapters 25–28

## 1 矢量微积分基础 (Vector Calculus in Electrostatics)

### 1.1 梯度算符与电势梯度 (Gradient)

在三维直角坐标系中，定义矢量微分算符 **$\nabla$**（读作 "del" 或 "nabla"，又称**哈密顿算符**）为：

$$
\nabla \equiv \hat{x}\frac{\partial}{\partial x} + \hat{y}\frac{\partial}{\partial y} + \hat{z}\frac{\partial}{\partial z}
$$

当 $\nabla$ 作用于空间标量函数 $\phi(x, y, z)$ 时，得到一个矢量函数，称为 $\phi$ 的**梯度**（Gradient）：

$$
\nabla\phi = \hat{x}\frac{\partial\phi}{\partial x} + \hat{y}\frac{\partial\phi}{\partial y} + \hat{z}\frac{\partial\phi}{\partial z}
$$

对于无穷小位移矢量 $d\vec{r} = \hat{x}\,dx + \hat{y}\,dy + \hat{z}\,dz$（课件中亦记为 $d\vec{s}$），标量场 $\phi$ 的全微分（Total differential）可写为梯度与位移矢量的点乘：

$$
d\phi = \frac{\partial\phi}{\partial x}dx + \frac{\partial\phi}{\partial y}dy + \frac{\partial\phi}{\partial z}dz = \nabla\phi \cdot d\vec{r}
$$

因此，$\nabla\phi$ 在空间任意两点 $\vec{r}_1$ 与 $\vec{r}_2$ 之间的线积分恒等于 $\phi$ 的差值，且与路径无关：

$$
\int_{\vec{r}_1}^{\vec{r}_2} \nabla\phi \cdot d\vec{r} = \int_{\vec{r}_1}^{\vec{r}_2} d\phi = \phi(\vec{r}_2) - \phi(\vec{r}_1) = \Delta\phi
$$

将 $\phi$ 取为静电势 $V$，对比电势差的定义式 $V(\vec{r}') - V(\vec{r}) = -\int_{\vec{r}}^{\vec{r}'} \vec{E}\cdot d\vec{l}$（对任意路径均成立），立即得到电场强度与电势的微分关系：

$$
\vec{E} = -\nabla V
$$

!!! note "梯度的几何意义与最优化算法应用（Gradient Descent）"
    由 $d\phi = \nabla\phi \cdot d\vec{r} = |\nabla\phi|\,|d\vec{r}|\cos\theta$ 可知：
    
    1. **正交性**：当位移 $d\vec{r}$ 垂直于 $\nabla\phi$ 时，$d\phi = 0$，即 **$\nabla\phi$ 处处垂直于等值面（Contour surface / Equipotential surface）$\phi = \text{const}$**；
    2. **最速上升方向（Direction of Steepest Ascent）**：当 $d\vec{r}$ 与 $\nabla\phi$ 同向（$\theta = 0$）时，$d\phi$ 取得最大值，即 **$\nabla\phi$ 指向标量函数 $\phi$ 增长最快的方向**（而电场 $\vec{E} = -\nabla V$ 则指向电势下降最快的方向，即“下坡方向” Downhill direction）；
    3. **极值点与科学计算**：在函数极大值点、极小值点或鞍点（Saddle point）处必有 $\nabla\phi = \vec{0}$。在科学计算与机器学习（Machine Learning）中，求解 $N$ 维函数 $f(x_1, \dots, x_N)$ 的最小值广泛采用**梯度下降法**（Gradient Descent / Steepest Descent）、**随机梯度下降**（Stochastic Gradient Descent, SGD）及**共轭梯度法**（Conjugate Gradient）——其核心思想是从初始点出发，逆着高维梯度 $\nabla f = \left(\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_N}\right)$ 的方向迭代移动，直至梯度为零。

<details markdown="1">
<summary>课堂经典推导（Example 4.1 & 4.2）：利用矢量梯度公式求点电荷与电偶极子的电场</summary>

在矢量微积分运算中，位置矢量 $\vec{r} = x\hat{x} + y\hat{y} + z\hat{z}$ 的模长为 $r = \sqrt{x^2 + y^2 + z^2}$。由 $\frac{\partial r}{\partial x} = \frac{x}{r}$ 可知核心梯度基本公式：

$$
\nabla r = \frac{x\hat{x} + y\hat{y} + z\hat{z}}{r} = \frac{\vec{r}}{r} = \hat{r}, \qquad \nabla(r^n) = n r^{n-1} \nabla r = n r^{n-1}\hat{r}
$$

**1. 点电荷的电场（Example 4.1）**

已知原点处点电荷的电势为 $V(r) = \frac{1}{4\pi\epsilon_0}\frac{q}{r}$。利用 $\nabla\left(\frac{1}{r}\right) = -\frac{1}{r^2}\nabla r = -\frac{\hat{r}}{r^2}$，直接求负梯度：

$$
\vec{E} = -\nabla V = -\frac{q}{4\pi\epsilon_0}\nabla\left(\frac{1}{r}\right) = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}\hat{r}
$$

---

**2. 电偶极子的电场（Example 4.2）**

已知原点处点偶极子 $\vec{p}$ 的电势为 $V(\vec{r}) = \frac{1}{4\pi\epsilon_0}\frac{\vec{p}\cdot\vec{r}}{r^3}$。
对于常矢量 $\vec{p} = p_x\hat{x} + p_y\hat{y} + p_z\hat{z}$，显然有：

$$
\nabla(\vec{p}\cdot\vec{r}) = \nabla(p_x x + p_y y + p_z z) = p_x\hat{x} + p_y\hat{y} + p_z\hat{z} = \vec{p}
$$

同时由链式法则有 $\nabla(r^3) = 3r^2\nabla r = 3r^2\hat{r}$。应用商的梯度法则，立即导出电偶极子电场矢量通式：

$$
\begin{aligned}
\vec{E} &= -\nabla V = -\frac{1}{4\pi\epsilon_0}\nabla\left(\frac{\vec{p}\cdot\vec{r}}{r^3}\right) \\
&= -\frac{1}{4\pi\epsilon_0}\frac{r^3\nabla(\vec{p}\cdot\vec{r}) - (\vec{p}\cdot\vec{r})\nabla(r^3)}{r^6} \\
&= -\frac{1}{4\pi\epsilon_0}\frac{r^3\vec{p} - 3r^2(\vec{p}\cdot\vec{r})\hat{r}}{r^6} = \frac{1}{4\pi\epsilon_0}\frac{3(\vec{p}\cdot\hat{r})\hat{r} - \vec{p}}{r^3}
\end{aligned}
$$

</details>

### 1.2 散度与旋度 (Divergence and Curl)

微分算符 $\nabla$ 作用于矢量场 $\vec{A}(x, y, z) = A_x\hat{x} + A_y\hat{y} + A_z\hat{z}$ 时，存在点乘与叉乘两种方式，分别生成标量场与矢量场：

| 运算名称 | 符号记法与结果类型 | 直角坐标系展开表达式 |
| :--- | :--- | :--- |
| **梯度（Gradient）** | $\nabla\phi$（标量 $\to$ 矢量） | $\hat{x}\dfrac{\partial\phi}{\partial x} + \hat{y}\dfrac{\partial\phi}{\partial y} + \hat{z}\dfrac{\partial\phi}{\partial z}$ |
| **散度（Divergence）** | $\nabla \cdot \vec{A}$（矢量 $\to$ 标量） | $\dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$ |
| **旋度（Curl / Rotation）** | $\nabla \times \vec{A}$（矢量 $\to$ 矢量） | $\begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix} = \hat{x}\left(\dfrac{\partial A_z}{\partial y} - \dfrac{\partial A_y}{\partial z}\right) + \hat{y}\left(\dfrac{\partial A_x}{\partial z} - \dfrac{\partial A_z}{\partial x}\right) + \hat{z}\left(\dfrac{\partial A_y}{\partial x} - \dfrac{\partial A_x}{\partial y}\right)$ |

**静电场的无旋性（Irrotational Property of Electrostatic Field）**：

对于任意具有二阶连续偏导数的标量函数 $\phi(x, y, z)$，**梯度的旋度恒等于零**：

$$
\nabla \times (\nabla\phi) \equiv \vec{0}
$$

*证明*：将 $A_x = \frac{\partial\phi}{\partial x}, \ A_y = \frac{\partial\phi}{\partial y}, \ A_z = \frac{\partial\phi}{\partial z}$ 代入旋度公式，其 $x$ 分量为 $(\nabla\times\nabla\phi)_x = \frac{\partial^2\phi}{\partial y\partial z} - \frac{\partial^2\phi}{\partial z\partial y} = 0$（混合偏导数可交换次序），同理 $y, z$ 分量亦恒为零。

由于静电场满足 $\vec{E} = -\nabla V$，由此直接推出静电场的基本微分性质（即静电场环路定理 $\oint \vec{E}\cdot d\vec{l} = 0$ 的微分形式，两者可通过斯托克斯定理 Stokes' Theorem 互推）：

$$
\nabla \times \vec{E} = \vec{0}
$$

在场论语言中，这意味着**静电场是无旋场（Irrotational field）**。这也回答了课件中的核心问题：为什么仅凭一个标量函数 $V(x,y,z)$ 就能完整包含三维矢量场 $\vec{E}(x,y,z)$ 三个分量的全部信息？正是因为 $\vec{E}$ 的三个分量并非彼此独立，而是受到 $\nabla\times\vec{E} = \vec{0}$ 的严格约束！

### 1.3 常用矢量分析恒等式 (Vector Identities)

设 $f, g$ 为标量函数，$\vec{v}, \vec{w}$ 为矢量函数，由 $\nabla$ 的定义及莱布尼茨乘积求导法则可得以下五条基本恒等式：

1. **标量乘积的梯度**：$\nabla(fg) = (\nabla f)g + f(\nabla g)$
2. **标量与矢量乘积的散度**：$\nabla \cdot (f\vec{v}) = (\nabla f) \cdot \vec{v} + f(\nabla \cdot \vec{v})$
3. **标量与矢量乘积的旋度**：$\nabla \times (f\vec{v}) = (\nabla f) \times \vec{v} + f(\nabla \times \vec{v})$
4. **叉乘的散度**：$\nabla \cdot (\vec{v} \times \vec{w}) = \vec{w} \cdot (\nabla \times \vec{v}) - \vec{v} \cdot (\nabla \times \vec{w})$
5. **叉乘的旋度**：$\nabla \times (\vec{v} \times \vec{w}) = \vec{v}(\nabla \cdot \vec{w}) - \vec{w}(\nabla \cdot \vec{v}) + (\vec{w} \cdot \nabla)\vec{v} - (\vec{v} \cdot \nabla)\vec{w}$

---

## 2 高斯定理的微分形式与泊松方程 (Differential Form of Gauss' Law & Poisson's Equation)

### 2.1 高斯定理微分形式的微元推导

积分形式的高斯定理 $\oint_S \vec{E}\cdot d\vec{A} = \frac{q_{\text{enc}}}{\epsilon_0}$ 给出的是闭合曲面内的总电荷。为了建立空间某点 $\vec{r} = (x, y, z)$ 处的局域体电荷密度 $\rho(\vec{r})$ 与电场 $\vec{E}(\vec{r})$ 的直接关系，我们在位置 $\vec{r}$ 处取一个边长分别为 $\Delta x, \Delta y, \Delta z$ 的无穷小长方体微元（体积 $\Delta V = \Delta x\Delta y\Delta z$，其内所含电荷量约为 $q_{\text{enc}} \approx \rho(\vec{r})\Delta x\Delta y\Delta z$）。

考察垂直于 $x$ 轴、位于 $x \pm \frac{\Delta x}{2}$ 处的左右两个矩形侧面（面积均为 $\Delta y\Delta z$，外法线分别为 $+\hat{x}$ 与 $-\hat{x}$）。在领头阶近似下，穿过这两个面的净电通量为：

$$
\begin{aligned}
\Phi_x &\approx \vec{E}\left(x + \frac{\Delta x}{2}, y, z\right)\cdot\hat{x}\,\Delta y\Delta z + \vec{E}\left(x - \frac{\Delta x}{2}, y, z\right)\cdot(-\hat{x})\,\Delta y\Delta z \\
&= \left[E_x\left(x + \frac{\Delta x}{2}, y, z\right) - E_x\left(x - \frac{\Delta x}{2}, y, z\right)\right]\Delta y\Delta z \approx \frac{\partial E_x}{\partial x}\Delta x\Delta y\Delta z
\end{aligned}
$$

完全同理，穿过垂直于 $y$ 轴和 $z$ 轴的另外两对相对侧面的净电通量分别为 $\Phi_y \approx \frac{\partial E_y}{\partial y}\Delta x\Delta y\Delta z$ 与 $\Phi_z \approx \frac{\partial E_z}{\partial z}\Delta x\Delta y\Delta z$。将六个面的总通量相加并代入高斯定理：

$$
\Phi_{\text{tot}} = \Phi_x + \Phi_y + \Phi_z \approx \left(\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}\right)\Delta V = \frac{q_{\text{enc}}}{\epsilon_0} \approx \frac{\rho(\vec{r})\Delta V}{\epsilon_0}
$$

两边同除以 $\Delta V$ 并取体积收缩至单点的极限 $\Delta V \to 0$，即得**高斯定理的微分形式**（Differential Form of Gauss' Law）：

$$
\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0} \iff \nabla \cdot \vec{E}(\vec{r}) = \lim_{\Delta V \to 0} \frac{1}{\Delta V} \oint_S \vec{E} \cdot d\vec{A} = \frac{\rho(\vec{r})}{\epsilon_0}
$$

!!! tip "散度的几何意义与散度定理（Divergence Theorem）"
    - **散度的物理图像**：散度 $\nabla\cdot\vec{E}$ 度量了矢量场从某点向外涌出（发散）的趋势。在静电场中，只有存在净电荷（$\rho \neq 0$）的位置散度才非零（$\rho > 0$ 处为正散度“源”，$\rho < 0$ 处为负散度“汇”）。
    - **散度的两种几何成因（Lecture 4 Slides 19–20）**：判断某点散度是否为零，需同时考察**场线的张开程度（Spreading out）**与**场矢量模长的沿线变化（Changing length）**：
      1. 即使场线彼此平行（如 $\vec{A} = A_z(z)\hat{z}$），若箭头沿流动方向变长（$\partial_z A_z > 0$），则流出大于流入，散度依然为正（$\nabla\cdot\vec{A} > 0$）；若箭头变短则散度为负。
      2. 在球对称径向场 $\vec{E} = f(r)\hat{r}$ 中，虽然场线向外张开（贡献正项 $\frac{2}{r}f(r)$），但如果场强模长随 $r$ 按 $1/r^2$ 快速衰减（贡献负项 $f'(r) = -\frac{2}{r^3}$），两者在 $r > 0$ 处恰好抵消，使得无电荷空间 $\nabla\cdot\vec{E} = 0$！
    - **散度定理 / 高斯公式（Divergence Theorem / Gauss' Theorem）**：对任意光滑矢量场 $\vec{v}$，穿过闭合曲面 $S$ 的总通量恒等于其散度在内部体积 $V$ 上的体积分：
      $$
      \oint_S \vec{v} \cdot d\vec{A} = \int_V (\nabla \cdot \vec{v})\,dV
      $$
      利用散度定理，可将积分形式的高斯定理瞬间转化为微分形式：$\int_V (\nabla\cdot\vec{E})\,dV = \oint_S \vec{E}\cdot d\vec{A} = \int_V \frac{\rho}{\epsilon_0}\,dV \implies \nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0}$。

### 2.2 拉普拉斯算符、泊松方程与拉普拉斯方程

对标量场连续作用两次 $\nabla$（即先取梯度再取散度 $\nabla\cdot\nabla$），得到二阶标量微分算符 **$\nabla^2$**，称为**拉普拉斯算符**（Laplacian）：

$$
\nabla^2 \equiv \nabla \cdot \nabla = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}
$$

将 $\vec{E} = -\nabla V$ 代入高斯定理微分形式 $\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0}$，消去电场 $\vec{E}$，即得到直接联系电势 $V$ 与电荷密度 $\rho$ 的二阶偏微分方程——**泊松方程**（Poisson's Equation）：

$$
\nabla^2 V = \nabla \cdot (\nabla V) = -\frac{\rho}{\epsilon_0}
$$

特别地，在不含电荷的空间区域（$\rho = 0$），泊松方程简化为**拉普拉斯方程**（Laplace's Equation）：

$$
\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0
$$

拉普拉斯方程在工程与物理中极为重要：在由给定电势的导体所围成的无电荷空间内，结合边界条件（Boundary conditions）求解拉普拉斯方程即可唯一确定空间的电势分布（如第五章将介绍的镜像法 Method of image charges）。

---

## 3 静电学三角关系总览 (The Triangle of Electrostatics)

至此，我们已经集齐了静电学中连接三个基本物理量——**电荷密度 $\rho(\vec{r})$**、**电场强度 $\vec{E}(\vec{r})$** 与 **静电势 $V(\vec{r})$** 的全套工具。它们分别位于一个三角形的三个顶点，每条边上都具有双向互推的积分形式与微分形式：

| 转化方向 | 微分形式 / 局域关系（Differential Form） | 积分形式 / 全局关系（Integral Form） | 物理与计算说明 |
| :--- | :--- | :--- | :--- |
| **$V \longrightarrow \vec{E}$** | $\vec{E} = -\nabla V$ | — | 纯几何关系：电场指向电势下降最快的方向 |
| **$\vec{E} \longrightarrow V$** | — | $V(\vec{r}) = -\displaystyle\int_{\mathcal{O}}^{\vec{r}} \vec{E} \cdot d\vec{l}$ | 依赖静电场的无旋性 $\nabla \times \vec{E} = \vec{0}$（路径无关） |
| **$\vec{E} \longrightarrow \rho$** | $\nabla \cdot \vec{E} = \dfrac{\rho}{\epsilon_0}$（且 $\nabla \times \vec{E} = \vec{0}$） | $q_{\text{enc}} = \epsilon_0 \displaystyle\oint_S \vec{E} \cdot d\vec{A}$ | 高斯定理：由已知电场分布反推源电荷密度 |
| **$\rho \longrightarrow \vec{E}$** | — | $\vec{E}(\vec{r}) = \dfrac{1}{4\pi\epsilon_0}\displaystyle\int \frac{\hat{r}_q}{r_q^2}\rho(\vec{r}')\,d\tau'$ | 库仑定律叠加（高度对称时可用 $\oint \vec{E}\cdot d\vec{A} = q_{\text{enc}}/\epsilon_0$） |
| **$V \longrightarrow \rho$** | $\nabla^2 V = -\dfrac{\rho}{\epsilon_0}$（泊松方程） | — | 二阶拉普拉斯算符直接由电势求电荷密度 |
| **$\rho \longrightarrow V$** | 解边值问题 $\nabla^2 V = -\dfrac{\rho}{\epsilon_0}$ | $V(\vec{r}) = \dfrac{1}{4\pi\epsilon_0}\displaystyle\int \frac{\rho(\vec{r}')}{r_q}\,d\tau'$ | **实战首选路径**：除高度对称可用高斯定理外，通常优先算标量 $V$ 再求导得 $\vec{E}$ |

---

## 4 数学物理附录：球坐标散度与狄拉克 $\delta$ 函数 (Appendices 4A & 4B)

<details markdown="1">
<summary>Appendix 4A: Divergence in Spherical Coordinates（球坐标系下的散度公式）</summary>

在球坐标系 $(r, \theta, \phi)$ 中，设矢量场分解为 $\vec{F} = F_r\hat{r} + F_\theta\hat{\theta} + F_\phi\hat{\phi}$。由 Appendix 2A 可知位移线元为 $d\vec{s} = dr\,\hat{r} + r\,d\theta\,\hat{\theta} + r\sin\theta\,d\phi\,\hat{\phi}$，球坐标微元六面体（Spherical cuboid）的体积为 $\Delta V = r^2\sin\theta\,dr\,d\theta\,d\phi$。

根据散度的通量极限定义 $\nabla\cdot\vec{F} = \lim_{\Delta V \to 0}\frac{1}{\Delta V}\oint \vec{F}\cdot d\vec{A}$，计入曲率引起的面积因子变化后，可得**球坐标系下的散度展开式**：

$$
\nabla \cdot \vec{F} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 F_r\right) + \frac{1}{r\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta F_\theta\right) + \frac{1}{r\sin\theta}\frac{\partial F_\phi}{\partial\phi}
$$

特别地，对于纯径向矢量场 $\vec{F} = f(r)\hat{r}$（即 $F_r = f(r), \ F_\theta = F_\phi = 0$），散度公式简化为：

$$
\nabla \cdot \big(f(r)\hat{r}\big) = \frac{1}{r^2}\frac{d}{dr}\left[r^2 f(r)\right] = \frac{2}{r}f(r) + f'(r)
$$

</details>

<details markdown="1">
<summary>Appendix 4B: Dirac Delta Function（点电荷奇异性与狄拉克 δ 函数）</summary>

**1. 点电荷场的散度佯谬（Paradox at $r = 0$）**

考察原点处点电荷产生的核核心径向场 $\vec{F} = \frac{\hat{r}}{r^2}$（即 $f(r) = \frac{1}{r^2}$）。若直接套用上面的球坐标散度公式，在 $r \neq 0$ 处有：

$$
\nabla \cdot \left(\frac{\hat{r}}{r^2}\right) = \frac{1}{r^2}\frac{d}{dr}\left(r^2 \cdot \frac{1}{r^2}\right) = \frac{1}{r^2}\frac{d}{dr}(1) = 0 \qquad (r > 0)
$$

然而，在以原点为中心、半径为 $R$ 的球面上计算面积分，却有 $\oint_S \frac{\hat{r}}{r^2}\cdot d\vec{A} = 4\pi \neq 0$！如果散度在全空间处处为零，就会与散度定理 $\oint \vec{F}\cdot d\vec{A} = \int_V (\nabla\cdot\vec{F})\,dV$ 矛盾。原因在于 **$r = 0$ 处被积函数发散（奇点）**，全部非零散度都集中在原点 $r = 0$ 这一单点上（因为点电荷体积为零而电荷量有限，其体电荷密度在原点处发散为无穷大）。

---

**2. 狄拉克 $\delta$ 函数（Dirac Delta Function）**

为了严格描述这类“单点无穷大、但空间积分有限”的奇异密度分布，物理学家引入了一维**狄拉克 $\delta$ 函数** $\delta(x)$（可视为宽度趋于 $0$、高度趋于 $\infty$、面积恒为 $1$ 的矩形函数序列 $R_n(x)$ 或三角形函数序列 $T_n(x)$ 的极限）：

$$
\delta(x) = \begin{cases}
0, & x \neq 0, \\
\infty, & x = 0,
\end{cases} \qquad \text{且满足归一化条件：} \int_{-\infty}^{+\infty} \delta(x)\,dx = 1
$$

推广至三维空间，定义三维狄拉克 $\delta$ 函数为 $\delta^3(\vec{r}) = \delta(x)\delta(y)\delta(z)$（在包含原点的任意体积域 $V$ 上积分恒为 $\int_V \delta^3(\vec{r})\,dV = 1$）。由此可写出著名的**点电荷散度恒等式**：

$$
\nabla \cdot \left(\frac{\hat{r}}{r^2}\right) = 4\pi\delta^3(\vec{r}), \qquad \nabla^2\left(\frac{1}{r}\right) = -4\pi\delta^3(\vec{r})
$$

利用 $\delta$ 函数，位于 $\vec{r}_0$ 处的单个点电荷 $q$ 的空间体电荷密度可简洁地表示为：

$$
\rho(\vec{r}) = q\delta^3(\vec{r} - \vec{r}_0)
$$

**课堂综合例题（Lecture 4 Slide 27：汤川势 Yukawa Potential 的完整电荷分布）**：
已知电势 $V(r) = \frac{q}{4\pi\epsilon_0}\frac{e^{-r/a}}{r}$。求负梯度得电场 $\vec{E}(\vec{r}) = \frac{q}{4\pi\epsilon_0}e^{-r/a}\left(\frac{\hat{r}}{r^2} + \frac{\hat{r}}{ar}\right)$。求散度时同时计入原点奇异项 $\nabla\cdot\left(\frac{\hat{r}}{r^2}\right) = 4\pi\delta^3(\vec{r})$ 与 $r > 0$ 处的连续导数项，可得全空间电荷密度为：

$$
\rho(\vec{r}) = \epsilon_0 \nabla\cdot\vec{E} = q\delta^3(\vec{r}) - \frac{q}{4\pi a^2 r}e^{-r/a}
$$

这清晰地表明该系统由**位于原点的一个点电荷 $+q$** 以及**包围在周围的指数衰减负电荷云（总电量为 $-\int_0^\infty \frac{q}{4\pi a^2 r}e^{-r/a}\cdot 4\pi r^2\,dr = -q$）**共同组成！

</details>

---

## 5 Chapter 4 核心课后习题精解 (Selected Exercises)

<details markdown="1">
<summary>Exercise 4.1 & 4.2: Vector Identities Proof & Quadratic Potential Analysis（矢量恒等式证明与二次型电势的场及电荷密度）</summary>

**Problem Statement:**
- **Ex 4.1**: Prove equations (a) and (d) in Section 4.1.3, where $f$ and $g$ are scalar functions and $\vec{v}$ and $\vec{w}$ are vector functions, namely:
  $$\nabla(fg) = (\nabla f)g + f(\nabla g) \quad \text{and} \quad \nabla\cdot(\vec{v}\times\vec{w}) = \vec{w}\cdot(\nabla\times\vec{v}) - \vec{v}\cdot(\nabla\times\vec{w})$$
- **Ex 4.2**: An electric potential is given in Cartesian coordinates: $V = A(x^2 + y^2) + Bz^2$, where $A$ and $B$ are positive constants. (a) Find the electric field $\vec{E}$. (b) Show that the electric field satisfies the fundamental property $\nabla\times\vec{E} = \vec{0}$. (c) Find the charge density $\rho(x, y, z)$ using the differential form of Gauss' law $\nabla\cdot\vec{E} = \rho/\epsilon_0$.

---

**中文解析：**

**1. 矢量恒等式 (a) 与 (d) 的分量证明（Exercise 4.1）**：

- **证明 (a) $\nabla(fg) = (\nabla f)g + f(\nabla g)$**：
  由梯度定义及一元函数乘积求导法则 $\frac{\partial(fg)}{\partial x} = \frac{\partial f}{\partial x}g + f\frac{\partial g}{\partial x}$，展开得：
  $$
  \begin{aligned}
  \nabla(fg) &= \hat{x}\frac{\partial(fg)}{\partial x} + \hat{y}\frac{\partial(fg)}{\partial y} + \hat{z}\frac{\partial(fg)}{\partial z} \\
  &= \left(\hat{x}\frac{\partial f}{\partial x} + \hat{y}\frac{\partial f}{\partial y} + \hat{z}\frac{\partial f}{\partial z}\right)g + f\left(\hat{x}\frac{\partial g}{\partial x} + \hat{y}\frac{\partial g}{\partial y} + \hat{z}\frac{\partial g}{\partial z}\right) = (\nabla f)g + f(\nabla g)
  \end{aligned}
  $$
- **证明 (d) $\nabla\cdot(\vec{v}\times\vec{w}) = \vec{w}\cdot(\nabla\times\vec{v}) - \vec{v}\cdot(\nabla\times\vec{w})$**：
  先写出叉乘 $\vec{v}\times\vec{w} = \hat{x}(v_y w_z - v_z w_y) + \hat{y}(v_z w_x - v_x w_z) + \hat{z}(v_x w_y - v_y w_x)$。代入散度定义并按乘积法则展开导数：
  $$
  \begin{aligned}
  \nabla\cdot(\vec{v}\times\vec{w}) &= \frac{\partial}{\partial x}(v_y w_z - v_z w_y) + \frac{\partial}{\partial y}(v_z w_x - v_x w_z) + \frac{\partial}{\partial z}(v_x w_y - v_y w_x) \\
  &= w_x\left(\frac{\partial v_z}{\partial y} - \frac{\partial v_y}{\partial z}\right) + w_y\left(\frac{\partial v_x}{\partial z} - \frac{\partial v_z}{\partial x}\right) + w_z\left(\frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y}\right) \\
  &\quad - \left[ v_x\left(\frac{\partial w_z}{\partial y} - \frac{\partial w_y}{\partial z}\right) + v_y\left(\frac{\partial w_x}{\partial z} - \frac{\partial w_z}{\partial x}\right) + v_z\left(\frac{\partial w_y}{\partial x} - \frac{\partial w_x}{\partial y}\right) \right] \\
  &= \vec{w}\cdot(\nabla\times\vec{v}) - \vec{v}\cdot(\nabla\times\vec{w})
  \end{aligned}
  $$

---

**2. 二次型电势的电场、无旋性验证与体电荷密度（Exercise 4.2）**：

- **(a) 求电场 $\vec{E}$**：
  $$
  \vec{E} = -\nabla V = -\left(\hat{x}\frac{\partial V}{\partial x} + \hat{y}\frac{\partial V}{\partial y} + \hat{z}\frac{\partial V}{\partial z}\right) = -2Ax\hat{x} - 2Ay\hat{y} - 2Bz\hat{z}
  $$
- **(b) 验证 $\nabla\times\vec{E} = \vec{0}$**：
  由于 $E_x = -2Ax$（仅依赖 $x$）、$E_y = -2Ay$（仅依赖 $y$）、$E_z = -2Bz$（仅依赖 $z$），所有交叉偏导数均为零：
  $$
  \nabla\times\vec{E} = \hat{x}\left(\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}\right) + \hat{y}\left(\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x}\right) + \hat{z}\left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right) = \vec{0}
  $$
- **(c) 求体电荷密度 $\rho(x, y, z)$**：
  由高斯定理微分形式 $\rho = \epsilon_0(\nabla\cdot\vec{E})$：
  $$
  \rho(x, y, z) = \epsilon_0\left(\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}\right) = \epsilon_0(-2A - 2A - 2B) = -2\epsilon_0(2A + B)
  $$
  即该电势对应全空间均匀分布的负体电荷密度。

</details>

<details markdown="1">
<summary>Exercise 4.3 & 4.4: Circulation/Curl Connection & Charged Sphere Divergence（微元环流与旋度关系及带电球散度悖论解析）</summary>

**Problem Statement:**
- **Ex 4.3**: In Chapter 3 the electrostatic field was shown to satisfy $\oint \vec{E}\cdot d\vec{l} = 0$ around every closed path. This exercise connects that statement with $\nabla\times\vec{E} = \vec{0}$.
  (a) A small rectangle lies in the plane $z = z_0$, centered at $(x_0, y_0, z_0)$, with sides $\Delta x$ and $\Delta y$ parallel to the $x$ and $y$ axes, traversed counterclockwise as seen from $+z$. Show that, to leading order in $\Delta x$ and $\Delta y$, $\oint \vec{E}\cdot d\vec{l} = \left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right)\Delta x\Delta y$.
  (b) A field is proposed as $\vec{E} = E_0(y/a)\hat{x}$ everywhere ($E_0, a > 0$). Find $\nabla\times\vec{E}$. Then calculate $\oint \vec{E}\cdot d\vec{l}$ directly around the square with corners $(0,0,0), (L,0,0), (L,L,0), (0,L,0)$, compare with (a), and state whether any arrangement of charges at rest can produce this field.
- **Ex 4.4**: A ball of radius $R$ centered at the origin carries a total charge $Q$ spread uniformly through its volume, with $\vec{E} = \frac{Q\vec{r}}{4\pi\epsilon_0 R^3}$ ($r < R$) and $\vec{E} = \frac{Q\vec{r}}{4\pi\epsilon_0 r^3}$ ($r > R$).
  (a) Calculate $\nabla\cdot\vec{E}$ for $r < R$, and compare with $\rho/\epsilon_0$.
  (b) Calculate $\nabla\cdot\vec{E}$ for $r > R$, using identity (b) of Sec. 4.1.3 with $f = r^{-3}$ and $\vec{v} = \vec{r}$.
  (c) The flux of $\vec{E}$ through a sphere of radius $b > R$ is $Q/\epsilon_0$, although $\nabla\cdot\vec{E} = 0$ at every point of that sphere and everywhere else outside the ball. Explain why this does not contradict Gauss' theorem.

---

**中文解析：**

**1. 微元矩形环流与旋度 $z$ 分量的推导及非保守场判别（Exercise 4.3）**：

- **(a)** 逆时针沿矩形四条边积分：下边（$y = y_0 - \frac{\Delta y}{2}$，沿 $+\hat{x}$）与上边（$y = y_0 + \frac{\Delta y}{2}$，沿 $-\hat{x}$）的贡献之和为：
  $$
  \left[E_x\left(x_0, y_0 - \frac{\Delta y}{2}, z_0\right) - E_x\left(x_0, y_0 + \frac{\Delta y}{2}, z_0\right)\right]\Delta x \approx -\frac{\partial E_x}{\partial y}\Delta x\Delta y
  $$
  右边（$x = x_0 + \frac{\Delta x}{2}$，沿 $+\hat{y}$）与左边（$x = x_0 - \frac{\Delta x}{2}$，沿 $-\hat{y}$）的贡献之和为：
  $$
  \left[E_y\left(x_0 + \frac{\Delta x}{2}, y_0, z_0\right) - E_y\left(x_0 - \frac{\Delta x}{2}, y_0, z_0\right)\right]\Delta y \approx +\frac{\partial E_y}{\partial x}\Delta x\Delta y
  $$
  相加即得 $\oint \vec{E}\cdot d\vec{l} \approx \left(\dfrac{\partial E_y}{\partial x} - \dfrac{\partial E_x}{\partial y}\right)\Delta x\Delta y = (\nabla\times\vec{E})_z \Delta S$。
- **(b)** 对 $\vec{E} = E_0\frac{y}{a}\hat{x}$，直接求旋度得：
  $$
  \nabla\times\vec{E} = -\hat{z}\frac{\partial E_x}{\partial y} = -\frac{E_0}{a}\hat{z} \neq \vec{0}
  $$
  沿顶点为 $(0,0,0) \to (L,0,0) \to (L,L,0) \to (0,L,0) \to (0,0,0)$ 的正方形直接计算环流：
  - 底边 $y=0$：$E_x = 0 \implies \int = 0$；
  - 右边 $x=L$ 与左边 $x=0$：$d\vec{l} = \pm dy\,\hat{y} \perp \hat{x} \implies \int = 0$；
  - 顶边 $y=L$（从 $x=L$ 到 $x=0$，$d\vec{l} = dx\,\hat{x}$）：$\int_L^0 \frac{E_0 L}{a}\,dx = -\dfrac{E_0 L^2}{a}$。
  故 $\oint \vec{E}\cdot d\vec{l} = -\frac{E_0 L^2}{a}$，与 (a) 中 $(\nabla\times\vec{E})_z L^2 = -\frac{E_0}{a}L^2$ 完全吻合。因为 $\nabla\times\vec{E} \neq \vec{0}$（环流非零），**没有任何静止电荷分布能够产生该电场**（此类有旋电场只能由随时间变化的磁场感应产生）。

---

**2. 均匀带电实心球内外的散度计算与散度定理辨析（Exercise 4.4）**：

- **(a) 球内（$r < R$）**：因 $\vec{r} = x\hat{x} + y\hat{y} + z\hat{z}$，有 $\nabla\cdot\vec{r} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 3$。故：
  $$
  \nabla\cdot\vec{E} = \frac{Q}{4\pi\epsilon_0 R^3}\nabla\cdot\vec{r} = \frac{3Q}{4\pi\epsilon_0 R^3} = \frac{Q / \left(\frac{4}{3}\pi R^3\right)}{\epsilon_0} = \frac{\rho}{\epsilon_0}
  $$
- **(b) 球外（$r > R$）**：利用恒等式 (b) $\nabla\cdot(f\vec{v}) = (\nabla f)\cdot\vec{v} + f(\nabla\cdot\vec{v})$，取 $f = r^{-3}, \ \vec{v} = \vec{r}$。注意到 $\nabla(r^{-3}) = -3r^{-4}\nabla r = -3r^{-4}\hat{r} = -3r^{-5}\vec{r}$，且 $\vec{r}\cdot\vec{r} = r^2$，$\nabla\cdot\vec{r} = 3$：
  $$
  \nabla\cdot\left(\frac{\vec{r}}{r^3}\right) = \left(-3r^{-5}\vec{r}\right)\cdot\vec{r} + r^{-3}(3) = -3r^{-3} + 3r^{-3} = 0 \implies \nabla\cdot\vec{E} = 0 \quad (r > R)
  $$
- **(c) 为什么不违背散度定理？**
  散度定理 $\oint_{r=b} \vec{E}\cdot d\vec{S} = \int_{r \le b} (\nabla\cdot\vec{E})\,dV$ 右侧的体积分**必须遍及球面 $r = b$ 所包围的整个内部体积 $0 \le r \le b$**，而不仅仅是在球面 $r = b$ 表面或外部区域 $R < r \le b$。虽然在 $R < r \le b$ 的无电荷球壳层内 $\nabla\cdot\vec{E} = 0$，但在核心区域 $0 \le r < R$ 内 $\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0} \neq 0$，对该核心球体积分恰好给出 $\int_{r < R} \frac{\rho}{\epsilon_0}\,dV = \frac{Q}{\epsilon_0}$，与散度定理完全一致！

</details>

<details markdown="1">
<summary>Exercise 4.5, 4.6 & 4.7: Box Flux Verification, 1D Poisson Equation & Earnshaw's Theorem（长方体散度定理验证、一维泊松方程与恩绍定理）</summary>

**Problem Statement:**
- **Ex 4.5**: Take $\vec{E}(x, y, z) = E_0\left[\left(1 + \frac{xy}{a^2}\right)\hat{x} + \frac{x^2}{2a^2}\hat{y}\right]$ ($E_0, a > 0$).
  (a) Use $\nabla\cdot\vec{E} = \rho/\epsilon_0$ to find $\rho(x, y, z)$, and evaluate both $\rho$ and $\vec{E}$ at the origin.
  (b) Let $S$ be the closed surface of the rectangular box $0 \le x \le a, \ 0 \le y \le b, \ 0 \le z \le c$. Calculate the total electric flux $\Phi$ through $S$ directly from its six faces.
  (c) Calculate $q_{\text{enc}}$ by integrating $\rho$ over the box, and verify Gauss' theorem and Gauss' law.
- **Ex 4.6**: A volume charge distribution has $\rho(x) = \rho_0\frac{x}{a}$ ($\rho_0, a > 0$). Assume $V$ depends only on $x$, with $V(0) = V_c$ and $E_x(0) = E_c < 0$.
  (a) Solve Poisson's equation for $V(x)$ and find $\vec{E}(x)$.
  (b) Explain separately the physical roles of $V_c$ and $E_c$.
  (c) Find the two planes on which $\vec{E} = \vec{0}$, and evaluate $\rho$ on each plane.
- **Ex 4.7 (Earnshaw's Theorem)**: Poisson's equation limits where a charged particle can rest in stable equilibrium.
  (a) Show that at any point of a region that contains no charge, $\partial^2 V/\partial x^2$, $\partial^2 V/\partial y^2$, and $\partial^2 V/\partial z^2$ cannot all be positive.
  (b) Four point charges, each $Q > 0$, are fixed at $(\pm a, 0, 0)$ and $(0, \pm a, 0)$. Show that $\nabla V = \vec{0}$ at the origin, and calculate the three second derivatives of $V$ there.
  (c) A small particle of charge $q > 0$ is placed at the origin. Is its equilibrium stable against a small displacement along $x$? Along $z$? Use (a) to show that, at a point where there is no other charge, no arrangement of fixed charges can make the second derivatives of a positive charge's potential energy positive along all three axes.

---

**中文解析：**

**1. 长方体六面电通量与散度定理直接验证（Exercise 4.5）**：

- **(a)** 计算散度：$\frac{\partial E_x}{\partial x} = \frac{E_0 y}{a^2}$，$\frac{\partial E_y}{\partial y} = 0$，$\frac{\partial E_z}{\partial z} = 0$。故体电荷密度为：
  $$
  \rho(x, y, z) = \epsilon_0 \nabla\cdot\vec{E} = \frac{\epsilon_0 E_0 y}{a^2}
  $$
  在原点 $(0, 0, 0)$ 处：$\rho(0, 0, 0) = 0$，但电场 $\vec{E}(0, 0, 0) = E_0\hat{x} \neq \vec{0}$。
- **(b)** 分别计算六个面的通量：
  - 垂直于 $z$ 轴的上下两面（$z=0, c$）：因 $E_z = 0$，通量为 $0$；
  - 垂直于 $y$ 轴的前后两面（$y=0$ 与 $y=b$）：因 $E_y = E_0\frac{x^2}{2a^2}$ 与 $y$ 无关，两面法线相反（$-\hat{y}$ 与 $+\hat{y}$），通量精确抵消为 $0$；
  - 垂直于 $x$ 轴的左面（$x=0$，$\hat{n}=-\hat{x}$）与右面（$x=a$，$\hat{n}=+\hat{x}$）：
    $$
    \Phi = \int_0^c dz \int_0^b \left[E_x(a, y, z) - E_x(0, y, z)\right] dy = c \int_0^b E_0\left[\left(1 + \frac{ay}{a^2}\right) - 1\right] dy = \frac{E_0 c}{a}\left[\frac{y^2}{2}\right]_0^b = \frac{E_0 b^2 c}{2a}
    $$
- **(c)** 对体积分求包围总电荷：
  $$
  q_{\text{enc}} = \int_0^c dz \int_0^a dx \int_0^b \frac{\epsilon_0 E_0 y}{a^2}\,dy = c \cdot a \cdot \frac{\epsilon_0 E_0}{a^2}\frac{b^2}{2} = \frac{\epsilon_0 E_0 b^2 c}{2a} = \epsilon_0 \Phi
  $$
  散度定理与高斯定理得到严格验证。

---

**2. 一维泊松方程求解与积分常数的物理意义（Exercise 4.6）**：

- **(a)** 一维泊松方程为 $\frac{d^2 V}{dx^2} = -\frac{\rho(x)}{\epsilon_0} = -\frac{\rho_0}{\epsilon_0 a}x$。
  第一次积分求电场 $E_x(x) = -\frac{dV}{dx}$：
  $$
  \frac{dE_x}{dx} = \frac{\rho_0}{\epsilon_0 a}x \implies E_x(x) = \frac{\rho_0}{2\epsilon_0 a}x^2 + C_1
  $$
  代入初始条件 $E_x(0) = E_c$ 得 $C_1 = E_c$，故 $\vec{E}(x) = \left(E_c + \dfrac{\rho_0 x^2}{2\epsilon_0 a}\right)\hat{x}$。
  再积分求电势 $V(x) = -\int E_x(x)\,dx$ 并代入 $V(0) = V_c$：
  $$
  V(x) = V_c - E_c x - \frac{\rho_0}{6\epsilon_0 a}x^3
  $$
- **(b) $V_c$ 与 $E_c$ 的物理角色**：$V_c$ 仅代表**电势零点（参考点）的选取**，改变 $V_c$ 不会对电场 $\vec{E}$ 或电荷密度 $\rho$ 产生任何物理影响；$E_c$ 则代表**叠加在系统上的背景匀强外电场**（由无穷远处的边界条件或外部电荷平面产生），由于匀强电场的散度为零（$\frac{dE_c}{dx} = 0$），求二阶导数 $-\epsilon_0\frac{d^2 V}{dx^2}$ 时 $V_c$ 与 $E_c x$ 均消去，总是给出同一个局域电荷密度 $\rho(x)$。
- **(c) 零电场平面**：令 $E_x(x) = 0$（注意 $E_c < 0$，故 $-E_c = |E_c| > 0$）：
  $$
  \frac{\rho_0}{2\epsilon_0 a}x^2 + E_c = 0 \implies x = \pm\sqrt{\frac{-2\epsilon_0 a E_c}{\rho_0}}
  $$
  在这两个平面上的电荷密度分别为 $\rho = \pm\rho_0\sqrt{\dfrac{-2\epsilon_0 E_c}{\rho_0 a}}$。

---

**3. 恩绍定理（Earnshaw's Theorem）：静电场中不存在稳定平衡点（Exercise 4.7，经典名题）**：

- **(a)** 在无电荷区域（$\rho = 0$），电势满足拉普拉斯方程：
  $$
  \nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0
  $$
  三个实数之和为零，显然**不可能三个二阶偏导数同时为正**（若三个均 $>0$，其和必 $>0$，矛盾）。
- **(b)** 四个正电荷 $Q$ 位于 $(\pm a, 0, 0)$ 和 $(0, \pm a, 0)$，空间点 $(x, y, z)$ 的电势为：
  $$
  V(x, y, z) = \frac{Q}{4\pi\epsilon_0}\left[ \frac{1}{\sqrt{(x-a)^2+y^2+z^2}} + \frac{1}{\sqrt{(x+a)^2+y^2+z^2}} + \frac{1}{\sqrt{x^2+(y-a)^2+z^2}} + \frac{1}{\sqrt{x^2+(y+a)^2+z^2}} \right]
  $$
  由对称性（关于 $x, y, z$ 均为偶函数），在原点 $(0, 0, 0)$ 处一阶偏导数全为零，即 $\nabla V(0,0,0) = \vec{0}$。
  分别沿 $x$ 轴、$y$ 轴和 $z$ 轴在原点附近作二阶泰勒展开（或直接求二阶偏导）：
  - 在 $z$ 轴上 $(0, 0, z)$：$V(0, 0, z) = \frac{4Q}{4\pi\epsilon_0(a^2+z^2)^{1/2}} \approx \frac{4Q}{4\pi\epsilon_0 a}\left(1 - \frac{z^2}{2a^2}\right)$，故：
    $$
    \left.\frac{\partial^2 V}{\partial z^2}\right|_0 = -\frac{4Q}{4\pi\epsilon_0 a^3} = -\frac{Q}{\pi\epsilon_0 a^3} < 0
    $$
  - 由 $x, y$ 的完全对称性 $\left.\frac{\partial^2 V}{\partial x^2}\right|_0 = \left.\frac{\partial^2 V}{\partial y^2}\right|_0$，结合拉普拉斯方程 $\partial_x^2 V + \partial_y^2 V + \partial_z^2 V = 0$（或直接对 $V(x, 0, 0)$ 求二阶导：前两项贡献 $+\frac{4Q}{4\pi\epsilon_0 a^3}$，后两项贡献 $-\frac{2Q}{4\pi\epsilon_0 a^3}$），立即得到：
    $$
    \left.\frac{\partial^2 V}{\partial x^2}\right|_0 = \left.\frac{\partial^2 V}{\partial y^2}\right|_0 = +\frac{2Q}{4\pi\epsilon_0 a^3} = +\frac{Q}{2\pi\epsilon_0 a^3} > 0
    $$
- **(c) 稳定性判别与恩绍定理**：
  正电荷 $q > 0$ 的电势能为 $U = qV$。在原点处：
  - 沿 $x$（或 $y$）方向：$\frac{\partial^2 U}{\partial x^2} = q\frac{\partial^2 V}{\partial x^2} > 0$，势能处于极小值，故**沿 $x$（及 $y$）方向是稳定平衡（Stable）**；
  - 沿 $z$ 方向：$\frac{\partial^2 U}{\partial z^2} = q\frac{\partial^2 V}{\partial z^2} < 0$，势能处于极大值，一旦沿 $z$ 轴有微小偏移就会被推离原点，故**沿 $z$ 方向是不稳定平衡（Unstable）**（原点是电势的鞍点 Saddle point）。
  - **普遍结论（Earnshaw's Theorem）**：要使正电荷 $q > 0$ 在无源自由空间某点处于三维全方向稳定平衡，其势能 $U = qV$ 在该点必须取得严格局部极小值，这要求 $\frac{\partial^2 V}{\partial x^2}, \frac{\partial^2 V}{\partial y^2}, \frac{\partial^2 V}{\partial z^2}$ 在三个方向上同时为正；但由 (a) 中的拉普拉斯方程 $\nabla^2 V = 0$ 知这在数学上绝无可能。因此，**仅靠静电力作用，任何带电粒子都无法在无电荷的自由空间中实现稳定的静态悬浮平衡**。

</details>