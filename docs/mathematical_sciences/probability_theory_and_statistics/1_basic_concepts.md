# 第一章：概率论的基本概念 (Chapter 1: Introduction to Probability)

!!! abstract
    概率论与数理统计 | 第一章课堂笔记
    
    -  **核心关键词**：样本空间 (Sample Space)、随机事件 (Events)、频率与概率 (Frequency & Probability)、古典概型 (Classical Probability)、条件概率 (Conditional Probability)、独立性 (Independence)
  
    参考：  
    - 《概率论与数理统计（第二版）》，高等教育出版社，2023 — Chapter 1: Introduction to Probability
    - 浙江大学数学科学学院《概率论和数理统计》课程讲义（黄炜）
    


---

## §1.1 样本空间与随机事件 (Sample Space and Events)

### 1. 随机现象与随机试验
* **随机现象 (Random Phenomenon)**：在个别试验中结果呈现不确定性，但在大量重复试验中结果具有**统计规律性 (Statistical Regularity)**。
* **随机试验 (Random Experiment, $E$) 的三个基本特性**：
  1. **可重复性**：可以在相同条件下重复进行；
  2. **结果已知且多样**：每次试验的可能结果不止一个，且事先知道所有可能结果；
  3. **事前不确定性**：完成试验之前不能确定哪一个结果会出现。

### 2. 样本空间与随机事件
* **样本空间 (Sample Space, $S$ 或 $\Omega$)**：随机试验 $E$ 的所有可能结果构成的集合，记为 $S = \{s_1, s_2, \dots, s_n\}$。
* **样本点 (Sample Point)**：$S$ 中的元素 $s_i$（或 $\omega_i$）。

* **随机事件 (Event, $A$)**：样本空间 $S$ 的子集。当且仅当 $A$ 所包含的某一个样本点出现时，称事件 $A$ 发生。
>  * **基本事件**：只含有一个样本点的事件。
>  * **必然事件**：样本空间 $S$ 本身（每次试验必定发生）。
>  * **不可能事件**：空集 $\emptyset$（不包含任何样本点，每次试验都不发生）。
* **可列集与不可列集 (Countable / Uncountable Sets)**：
  * **可列集 (Countable)**:能与自然数集 $\{1, 2, 3, \dots\}$ 建立一一对应关系的无限集;
  * **不可列集 (Uncountable)**:既非有限集也非可列集的集合；
  * **至多可列 (At most countable)**：有限集或可列集。

### 3. 事件的关系与运算（集合论映射）

| 事件关系/运算 | 符号记法 | 概率论含义 | 集合论含义与注意点 |
| :--- | :--- | :--- | :--- |
| **包含** | $A \subset B$ | $A$ 发生必然导致 $B$ 发生 | 特别地，$\emptyset \subset A \subset S$ |
| **相等** | $A = B$ | $A$ 与 $B$ 等价 | $A \subset B$ 且 $B \subset A$ |
| **和事件 (并)** | $A \cup B$ 或 $\bigcup_{i=1}^n A_i$ | $A$ 与 $B$ **至少有一个发生** | **切勿写成 $A + B$** |
| **积事件 (交)** | $A \cap B$、$A \cdot B$ 或 $AB$ | $A$ 与 $B$ **同时发生** | 多事件积记为 $\bigcap_{i=1}^n A_i$ |
| **差事件** | $A - B$ 或 $A\overline{B}$ | **$A$ 发生且 $B$ 不发生** | 永远化为交集 $A\overline{B}$ 进行运算 |
| **互斥 (互不相容)** | $AB = \emptyset$ | $A$ 与 $B$ **不能同时发生** | 基本事件两两互不相容 |
| **互逆 (对立事件)** | $\overline{A}$ 或 $A^c$ | $A$ 不发生 | 需同时满足 $A \cup B = S$ 且 $AB = \emptyset$ |

### 4. 事件的运算律与系统模型
* **交换律**：$A \cup B = B \cup A$，$A \cap B = B \cap A$
* **结合律**：$(A \cup B) \cup C = A \cup (B \cup C)$，$(A \cap B) \cap C = A \cap (B \cap C)$
* **分配律**：$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$，$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
* **德摩根律 (De Morgan's Laws)**（核心化简工具）：
  $$\overline{A \cup B} = \overline{A} \cap \overline{B}, \quad \overline{A \cap B} = \overline{A} \cup \overline{B}$$
  $$\overline{\bigcup_{j=1}^n A_j} = \bigcap_{j=1}^n \overline{A_j}, \quad \overline{\bigcap_{j=1}^n A_j} = \bigcup_{j=1}^n \overline{A_j}$$
* **串联与并联系统**：设 $A_i = \{\text{第 } i \text{ 个部件未损坏}\}$，$A = \{\text{系统未损坏}\}$：
  * **串联系统**（一损俱损）：$A = \bigcap_{i=1}^n A_i$
  * **并联系统**（一通百通）：$A = \bigcup_{i=1}^n A_i$

---

## §1.2 频率和概率 (Frequency and Probability)

### 1. 频率及其性质
* **定义**：在相同条件下进行的 $n$ 次重复试验中，事件 $A$ 发生 $n_A$ 次，则频率定义为：
  $$f_n(A) = \frac{n_A}{n}$$

* **性质**：
  1. $0 \le f_n(A) \le 1$；
  2. $f_n(S) = 1$；
  3. 若 $A_1, A_2, \dots, A_k$ 两两互不相容，则 $f_n\left(\bigcup_{j=1}^k A_j\right) = \sum_{j=1}^k f_n(A_j)$。
* **统计性定义**：当试验次数 $n$ 足够大时，频率 $f_n(A)$ 稳定于某常数，该稳定值即为事件 $A$ 的概率 $P(A)$。

### 2. 概率的公理化定义 (Axiomatic Definition)
设 $S$ 为样本空间，若对每个事件 $A$ 赋予一个实数 $P(A)$，满足以下三条公理，则称 $P(A)$ 为事件 $A$ 的概率：
1. **非负性 (Non-negativity)**：对任意事件 $A$，$P(A) \ge 0$；
2. **规范性 (Normalization)**：$P(S) = 1$；
3. **可列可加性 (Countable Additivity)**：对两两互不相容的事件序列 $A_1, A_2, \dots$（即 $A_i A_j = \emptyset, i \neq j$），有：
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

### 3. 概率的重要性质与证明
1. **不可能事件概率为零**：$P(\emptyset) = 0$。

2. **有限可加性**：若 $A_1, \dots, A_n$ 两两互不相容，则 $P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)$。

3. **逆事件概率公式**：$P(\overline{A}) = 1 - P(A)$。
4. **差事件概率与单调性**：
   * 如果 $A \subset B$，则 $P(B - A) = P(B\overline{A}) = P(B) - P(A)$，且 $P(B) \ge P(A)$，进而对任意事件有 $P(A) \le P(S) = 1$。
5. **加法公式（容斥原理，“多还少补”）**：
   * **两事件**：$P(A \cup B) = P(A) + P(B) - P(AB)$
   * **三事件**：$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(AC) - P(BC) + P(ABC)$
   * **$n$ 事件**：
     $$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \sum_{1 \le i < j < k \le n} P(A_i A_j A_k) - \dots + (-1)^{n-1} P(A_1 A_2 \dots A_n)$$
   * **常用二级结论（三事件中至少发生两个）**：
     $$P(AB \cup AC \cup BC) = P(AB) + P(AC) + P(BC) - 2P(ABC)$$

> **【高频易错点】**：
> * 若 $P(A) = 0$，**不能**推出 $A = \emptyset$；若 $P(B) = 1$，**不能**推出 $B = S$。
> * **反例**：在 $S = [0, 1]$ 上均匀任取一数，令 $A = \{0.3\}$，则 $P(A) = 0$ 但 $A \neq \emptyset$；令 $B = \overline{A} = [0, 0.3) \cup (0.3, 1]$，则 $P(B) = 1$ 但 $B \neq S$。

---

## §1.3 等可能概型 / 古典概型 (Classical Probability)

### 1. 定义与计数基础
* **古典概型 (Simple Sample Space) 的两个条件**：
  1. **有限性**：样本空间 $S$ 中只有有限个样本点（共 $n$ 个）；
  2. **等可能性**：每个样本点出现的概率相等（均为 $1/n$）。
* **计算公式**：若事件 $A$ 包含 $m$ 个样本点，则
  $$P(A) = \frac{\#A}{\#S} = \frac{m}{n}$$
* **排列与组合**：
  * **排列数 (Permutation)**（讲究顺序）：$A_n^k = P_n^k = \frac{n!}{(n-k)!} = n(n-1)\cdots(n-k+1)$
  * **组合数 (Combination)**（不讲顺序）：$C_n^k = \binom{n}{k} = \frac{A_n^k}{k!} = \frac{n!}{k!(n-k)!}$（当 $k > n$ 或 $k < 0$ 时规定 $C_n^k = 0$）

### 2. 五大经典古典概型模型
1. **不放回抽样（超几何模型）**：
   $N$ 件产品中有 $D$ 件次品，不放回地取 $n$ 件，则“恰有 $k$ 件次品”的概率为：
   $$P(A_k) = \frac{C_D^k C_{N-D}^{n-k}}{C_N^n}, \quad k = 0, 1, \dots, n$$
2. **分球入盒问题**：
   将 $n$ 个不同的球随机投入 $N$ 个不同的盒中（$n \le N$，每盒容量不限），总样本点数为 $N^n$。“恰有 $n$ 个盒子各有一球”的概率为：
   $$P(A) = \frac{C_N^n \cdot n!}{N^n} = \frac{A_N^n}{N^n}$$
3. **生日问题 (Birthday Problem)**：
   $n \ (\le 365)$ 人的班级中，“至少有两人生日相同”的概率为：
   $$P(B) = 1 - \frac{C_{365}^n \cdot n!}{365^n} = 1 - \frac{A_{365}^n}{365^n}$$
4. **抽签问题 (Lottery Problem)**：
   袋中有 $a$ 个红球、$b$ 个白球（$a+b=n$），$n$ 个人依次不放回摸球，第 $k$ 个人摸到红球的概率为：
   $$P(A_k) = \frac{a(n-1)!}{n!} = \frac{C_{n-1}^{a-1}}{C_n^a} = \frac{a}{a+b}, \quad k = 1, 2, \dots, n$$
   *结论：抽签概率与先后顺序 $k$ 无关。注意不能直接以颜色 $\{红, 白\}$ 作为样本空间（当 $a \neq b$ 时不等可能）。*
5. **配对问题 / 错排问题 (Matching Problem)**：
   $n$ 个人每人准备一件礼物混在一起随机抽取，求“没有人拿到自己礼物”的概率。
   设 $A_i = \{\text{第 } i \text{ 人拿到自己礼物}\}$，$P(A_{i_1} A_{i_2} \dots A_{i_k}) = \frac{(n-k)!}{n!}$，由容斥原理得：
   $$P(\text{无人拿到自己礼物}) = 1 - P\left(\bigcup_{i=1}^n A_i\right) = 1 - \sum_{k=1}^n (-1)^{k-1} C_n^k \frac{(n-k)!}{n!} = \sum_{i=0}^n \frac{(-1)^i}{i!} \xrightarrow{n \to \infty} \frac{1}{e}$$

---

## §1.4 条件概率 (Conditional Probability)

### 1. 条件概率的定义与性质
* **定义**：设 $P(B) > 0$，在事件 $B$ 已发生的条件下，事件 $A$ 发生的条件概率为：
  $$P(A|B) = \frac{P(AB)}{P(B)}$$
  *几何本质：将原样本空间 $S$ 缩小为新样本空间 $S_B = B$，在 $S_B$ 上度量 $AB$ 的占比。*
* **条件概率的性质**（固定条件 $B$ 后，$P(\cdot|B)$ 是一组合格的概率测度）：
  * **非负性与规范性**：$P(A|B) \ge 0$，$P(S|B) = 1$；
  * **可列可加性**：若 $A_1, A_2, \dots$ 两两互斥，则 $P\left(\bigcup_{i=1}^\infty A_i \middle| B\right) = \sum_{i=1}^\infty P(A_i|B)$；
  * **逆事件**：$P(\overline{A}|B) = 1 - P(A|B)$；
  * **加法公式**：$P(A \cup C | B) = P(A|B) + P(C|B) - P(AC|B)$。
  * *注：当 $B \neq D$ 时，$P(A|B) + P(C|D)$ 无意义；记号 $A|B$ 本身不是一个事件；无条件概率 $P(A)$ 可视为 $P(A|S)$。*

### 2. 乘法公式 (Multiplication Formula)
当相关条件概率均有意义（分母概率大于 0）时：
* $P(AB) = P(A)P(B|A) = P(B)P(A|B)$
* $P(ABC) = P(A)P(B|A)P(C|AB)$
* **一般形式**（$n \ge 2$）：
  $$P(A_1 A_2 \dots A_n) = P(A_1) P(A_2|A_1) P(A_3|A_1 A_2) \cdots P(A_n|A_1 A_2 \dots A_{n-1})$$

### 3. 全概率公式与贝叶斯公式 (Law of Total Probability & Bayes' Formula)
* **完备事件组 / 样本空间的划分 (Partition)**：
  事件组 $B_1, B_2, \dots, B_n$ 满足：
  1. **不漏 (Exhaustive)**：$\bigcup_{i=1}^n B_i = S$；
  2. **不重 (Mutually Exclusive)**：$B_i \cap B_j = \emptyset \ (i \neq j)$。
* **全概率公式（由因求果）**：
  设 $B_1, \dots, B_n$ 为 $S$ 的一个划分且 $P(B_i) > 0$，则对任意事件 $A$：
  $$P(A) = \sum_{j=1}^n P(AB_j) = \sum_{j=1}^n P(B_j)P(A|B_j)$$
  * **条件概率形式的全概率公式**：
    $$P(A|C) = \sum_{j=1}^n P(B_j|C) P(A|B_j C)$$
* **贝叶斯公式 (Bayes' Formula，执果索因)**：
  在全概率公式条件下，若 $P(A) > 0$，则：
  $$P(B_i|A) = \frac{P(AB_i)}{P(A)} = \frac{P(B_i)P(A|B_i)}{\sum_{j=1}^n P(B_j)P(A|B_j)}$$
  *统计意义：在观测到结果 $A$ 发生后，将原因 $B_i$ 的**先验概率 (Prior)** $P(B_i)$ 更新为**后验概率 (Posterior)** $P(B_i|A)$。*

---

## §1.5 独立性 (Independence)

### 1. 两事件的独立性
* **定义**：若两随机事件 $A, B$ 满足：
  $$P(AB) = P(A)P(B)$$
  则称 $A, B$ **相互独立**。
  * 若 $P(A) > 0, P(B) > 0$，则 $A, B \text{ 独立} \iff P(B|A) = P(B) \iff P(A|B) = P(A)$。
  * 若 $0 < P(A) < 1$，则 $A, B \text{ 独立} \iff P(B) = P(B|A) = P(B|\overline{A})$。
* **等价命题 (Proposition 1)**：
  以下四个命题完全等价：
  1. $A$ 与 $B$ 相互独立；
  2. $\overline{A}$ 与 $B$ 相互独立；
  3. $A$ 与 $\overline{B}$ 相互独立；
  4. $\overline{A}$ 与 $\overline{B}$ 相互独立。
  * *证明思路*：$P(\overline{A}B) = P(B - AB) = P(B) - P(AB) = P(B) - P(A)P(B) = P(B)[1 - P(A)] = P(\overline{A})P(B)$。

> **【核心辨析：独立 vs. 互斥】**：
> 当 $P(A) > 0$ 且 $P(B) > 0$ 时，“$A, B$ 相互独立”与“$A, B$ 互不相容（互斥）”**绝不可能同时成立**！
> * 若独立，则 $P(AB) = P(A)P(B) > 0 \implies AB \neq \emptyset$（必不互斥）；
> * 若互斥，则 $AB = \emptyset \implies P(AB) = 0 \neq P(A)P(B)$（必不独立）。

### 2. 多事件的独立性
* **定义**：对 $n$ 个事件 $A_1, A_2, \dots, A_n \ (n \ge 2)$，若对**任意** $2 \le k \le n$ 及任意指标 $1 \le i_1 < i_2 < \dots < i_k \le n$，均有：
  $$P(A_{i_1} A_{i_2} \dots A_{i_k}) = \prod_{j=1}^k P(A_{i_j})$$
  则称 $A_1, A_2, \dots, A_n$ **相互独立**。
* **两两独立 vs. 相互独立**：
  * $n$ 个事件相互独立 $\implies$ 两两独立；
  * 两两独立 $\not\implies$ 相互独立（经典反例：正四面体三面分别涂红、黄、蓝，第四面涂红黄蓝三色，令 $A_1, A_2, A_3$ 分别表示抽到面含红、黄、蓝，则 $P(A_i)=1/2$，$P(A_i A_j)=1/4=P(A_i)P(A_j)$ 两两独立，但 $P(A_1 A_2 A_3) = 1/4 \neq (1/2)^3$）。

### 3. 四大典型综合题型模板
1. **赛制比较问题（三局两胜 vs. 五局三胜）**：
   设单局获胜概率为 $p$，各局独立：
   * 三局两胜胜率：$p_1 = p^2 + C_2^1 p^2(1-p)$（前两局胜，或前两局一胜一负且第三局胜）；
   * 五局三胜胜率：$p_2 = p^3 + C_3^1 p^3(1-p) + C_4^2 p^3(1-p)^2$；
   * 作差比较：$p_2 - p_1 = 3p^2(p-1)^2(2p-1)$，故当 $p > 1/2$ 时五局三胜有利，当 $p < 1/2$ 时三局两胜有利。
2. **桥式系统可靠性（全概率公式降维法）**：
   对于含有跨接桥元件 $A_3$ 的 5 元件系统，不能直接化为串并联，需按 $A_3$ 是否正常作全概率展开：
   $$P(A) = P(A_3)P(A|A_3) + P(\overline{A}_3)P(A|\overline{A}_3)$$
   * 当 $A_3$ 导通时：先并后串，$P(A|A_3) = P((A_1 \cup A_4)(A_2 \cup A_5)) = (2p - p^2)^2$；
   * 当 $A_3$ 断开时：先串后并，$P(A|\overline{A}_3) = P(A_1 A_2 \cup A_4 A_5) = 2p^2 - p^4$。
3. **独立重复试验中的递推全概率（无记忆性建方程）**：
   求独立重复试验中“事件 $B$ 出现在事件 $C$ 之前”的概率 $P(A)$：
   按**第一次试验**的结果划分为 $B$、$C$、$D=\overline{B \cup C}$，利用 $P(A|B)=1$、$P(A|C)=0$ 以及重头开始性质 **$P(A|D) = P(A)$**，由全概率公式得：
   $$P(A) = P(B) \cdot 1 + P(C) \cdot 0 + P(D) \cdot P(A) \implies P(A) = \frac{P(B)}{1 - P(D)} = \frac{P(B)}{P(B) + P(C)}$$
4. **条件独立性模型（抽枪连射 / 疾病的多次独立复检）**：
   设 $A$ 为原因（如“抽到已校正的枪”或“确实患病”），$B_1, B_2$ 为同一原因下的两次独立试验结果（如“两枪均命中”或“两次检测均阳性”）。
   * **注意**：$B_1, B_2$ 在给定 $A$（或 $\overline{A}$）的条件下**条件独立**，即 $P(B_1 B_2 | A) = P(B_1|A)P(B_2|A)$，但 $B_1, B_2$ 本身**并不独立**（$P(B_1 B_2) \neq P(B_1)P(B_2)$）！
   * 计算两次均发生的概率及后验概率时，必须按 $A$ 与 $\overline{A}$ 展开：
     $$P(B_1 B_2) = P(A)P(B_1|A)P(B_2|A) + P(\overline{A})P(B_1|\overline{A})P(B_2|\overline{A})$$
     $$P(A | B_1 B_2) = \frac{P(A)P(B_1|A)P(B_2|A)}{P(A)P(B_1|A)P(B_2|A) + P(\overline{A})P(B_1|\overline{A})P(B_2|\overline{A})}$$