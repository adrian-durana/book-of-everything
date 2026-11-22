# MATH1071 / MATH2400 / MATH2401 — transcription, part 1: MATH1071 handwritten notes (HW1071 01–66)

_Transcription phase. This group of courses is filed under the name `math1071`: MATH1071 Advanced Calculus & Linear Algebra I, MATH2400 Mathematical Analysis and MATH2401 Mathematical Analysis & Advanced Topics. Parts: `-1` MATH1071 handwritten (this doc), `-2` MATH2400 handwritten 001–051, `-3` MATH2400 handwritten 052–102, `-4` typed notes (index and figures). Inventory: `claude/inventory-math1071.md`._

**Source.** `math1071.zip`: 66 photos, one notebook page per photo, in shooting order. (The zip holds every photo twice — once at the top level and once in a `math1071/` subfolder — and the copies are byte-identical; only one copy is counted.) "HW1071 nn" = photo nn. Each heading gives the photo file name and the page header written in the notebook.

**Two notebooks.** HW1071 01–43 are lecture notes on linear algebra, headed "Lecture 10.4" … "Lecture 13.4" (lecture numbers, not dates). HW1071 44–66 are a numbered list of proofs 1–23 (analysis), with no lecture headers; item 4 is missing (the list goes 1, 2, 3.1, 3.2, 5, 6.1, 7, …).

**Conventions.** Faithful transcription: the notes' wording, labels (Th., Def., P./Proof, Ex., Rem./Rmk., Note, Coro., Prop.) and line breaks of displays are kept; the notes label many theorems "Def." or "Th." — kept as written, with [a theorem] where it matters. Maths uses the macros of `notation.tex` (`\R`, `\C`, `\N`, `\abs`, `\norm`, `\inner`, `\T` for transpose, `\dd`, `\vect`). The notes' plain (non-bold) $A$, $x$ for matrices and vectors are kept as written. `[possible error: …]` marks a suspected error (nothing is corrected silently); `[…]` without that label is a transcriber's note (crossed-out text, layout, reading of an ambiguous symbol). `[illegible]` marks text that cannot be read. Figures are labelled F1071-n and described for TikZ.

**Legibility.** All 66 photos are sharp and fully readable. HW1071 28 has its page header cut off at the top (content complete). Unresolved readings are handwriting, not photo quality: HW1071 08 (a course code after "refer to", reads "361b"/"3616"), HW1071 13 (one exponent: "$\R^{[illegible]}$"), HW1071 16 (third row of the transpose example is crossed out and overwritten).

---

## HW1071 01 · `20261121_224154.jpg` · Lecture 10.4

**An introduction to linear algebra.**

**Th.** Linear algebra
- Informal: study of vectors, matrices, tensors and linear functions
- Formal: study of vectorspaces, and linear transformations between them.

**Motivation.**
From analysis: differential calculus is a tool for studying more 'complicated' functions; reduce to simpler, linear ones.
- e.g. $\ell(x) = f(x_0) + f'(x_0)(x - x_0)$ is the best linear approx. to $f(x)$ near $x_0$.
- e.g. is $f$ increasing near $x_0$? yes, if $f'(x_0) > 0$.

To study multivariable calculus we must first study simpler functions (i.e. linear) w/ several variables, i.e. trivial case is linear algebra.

## HW1071 02 · `20261121_224158.jpg` · Lecture 10.4

**Th.** Systems of linear equations

**Ex.** Consider
$$\begin{aligned} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1\\ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2\\ &\ \,\vdots\\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m \end{aligned}$$
where $x_1, \dots, x_n$ are unknowns, $a_{ij}, b_i \in \R$, $1 \le i \le m$, $1 \le j \le n$.

Convert into matrices:
$$\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} & a_{22} & \cdots & a_{2n}\\ \vdots & & \ddots & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn}\end{bmatrix} \quad \text{coefficient matrix } (m \times n \text{ matrix})$$
$$\left[\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1\\ a_{21} & a_{22} & \cdots & a_{2n} & b_2\\ \vdots & & \ddots & \vdots & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m\end{array}\right] \quad \text{augmented matrix}$$

Matrices more or less save time in notation.

## HW1071 03 · `20261121_224203.jpg` · Lecture 10.4

**Th.** Elementary row operations
- interchange rows
- multiply a row by non-zero constant
- add constant multiple of one row to another

**Th.** Row-echelon form
$$\begin{bmatrix} a_{11} & \cdots & \cdots & \cdots\\ 0 & a_{22} & \cdots & \cdots\\ 0 & 0 & a_{33} & \cdots \end{bmatrix}$$

**Th.** Gaussian elimination: basically just repeated row operations until in RRE form. [possible error: the worked example stops at row-echelon form with leading 1s, not reduced row-echelon form]

**Ex.**
$$\begin{cases} x + y + z = 3,\\ x - y + z = 1,\\ x + y - z = 1, \end{cases} \implies \left(\begin{array}{ccc|c} 1&1&1&3\\ 1&-1&1&1\\ 1&1&-1&1 \end{array}\right)$$
$$\begin{matrix} \\ R_2 - R_1\\ R_3 - R_1 \end{matrix} \left(\begin{array}{ccc|c} 1&1&1&3\\ 0&-2&0&-2\\ 0&0&-2&-2 \end{array}\right) \implies \left(\begin{array}{ccc|c} 1&1&1&3\\ 0&1&0&1\\ 0&0&1&1 \end{array}\right)$$
which is equivalent to $\begin{cases} x + y + z = 3\\ y = 1\\ z = 1 \end{cases}$

## HW1071 04 · `20261121_224213.jpg` · Lecture 10.4

**Ex.**
$$\begin{cases} x + 3y - 2z = 5\\ -x + y - 2z = -9\\ 2x + 4y - 2z = 12 \end{cases} \to \left(\begin{array}{ccc|c} 1&3&-2&5\\ -1&1&-2&-9\\ 2&4&-2&12 \end{array}\right)$$
$$\begin{matrix} \\ R_1 + R_2\\ R_3 - 2R_1 \end{matrix} \left(\begin{array}{ccc|c} 1&3&-2&5\\ 0&4&-4&-4\\ 0&-2&2&2 \end{array}\right) \longrightarrow \left(\begin{array}{ccc|c} 1&3&-2&5\\ 0&1&-1&-1\\ 0&0&0&0 \end{array}\right)$$
[possible error: the row label "$R_1 + R_2$" should read $R_2 + R_1$ (row 2 is replaced)]
which is equivalent to $\begin{cases} x + 3y - 2z = 5\\ y - z = -1\\ 0 = 0 \end{cases}$

For any value of $z$, $z = \alpha \in \R$ $\implies z = \alpha$, $y = -1 + \alpha$, $x = 8 - \alpha$.
$\implies$ There are infinite solutions parameterised by the variable $\alpha$. $\{(8 - \alpha, \alpha - 1, \alpha) : \alpha \in \R\}$ is the set of solutions.

**Ex.**
$$\begin{cases} x + 3y - 2z = 5\\ -x + y - 2z = -9\\ 2x + 4y - 2z = 14 \end{cases} \to \left(\begin{array}{ccc|c} 1&3&-2&5\\ -1&1&-2&-9\\ 2&4&-2&14 \end{array}\right) \to \left(\begin{array}{ccc|c} 1&3&2&5\\ 0&1&-1&-1\\ 0&0&0&1 \end{array}\right)$$
[possible error: the (1,3) entry of the reduced matrix is written $2$; it should be $-2$]
$\implies$ The last equation is $0 = 1$, the system has NO solutions. The set of solutions is $\emptyset$.

## HW1071 05 · `20261121_224218.jpg` · Lecture 11.1

**Th.** Matrix rank
- number of non-zero rows in row-reduced echelon form
- a linear system has a solution iff the rank of the coefficient matrix is equal to the rank of the augmented matrix
- a linear system has infinitely many solutions, if the rank is LESS than the number of unknowns. [possible error: needs the system to be consistent (rank of coefficient matrix = rank of augmented matrix); the third example below is the counterexample]

**Ex.**
$$\operatorname{rk}\begin{pmatrix}1&1&1\\0&1&0\\0&0&1\end{pmatrix} = \operatorname{rk}\left(\begin{array}{ccc|c}1&1&1&3\\0&1&0&1\\0&0&1&1\end{array}\right) = 3 = 3\ (\#\text{sol}) \implies \text{unique solution}$$
[the "#sol" annotation labels 3 as the number of unknowns]
$$\operatorname{rk}\begin{pmatrix}1&3&2\\0&1&-1\\0&0&0\end{pmatrix} = \operatorname{rk}\left(\begin{array}{ccc|c}1&3&2&5\\0&1&-1&-1\\0&0&0&0\end{array}\right) = 2 < 3\ (\#\text{sol})$$
$\implies$ infinitely many sol., depending on $(3 - 2 = 1)$ parameters.
$$\operatorname{rk}\begin{pmatrix}1&3&2\\0&1&-1\\0&0&0\end{pmatrix} < \operatorname{rk}\left(\begin{array}{ccc|c}1&3&2&5\\0&1&-1&-1\\0&0&0&1\end{array}\right) \implies 2 < 3$$
$\implies$ but the system has no solutions.
[possible error: the (1,3) entries are again written $2$ for $-2$, carried from HW 04]

**Th.** $n$-dimensional vectors
- an array of $n$ numbers: $x_i \in \R$, $1 \le i \le n$
- row vector $(x_1, \dots, x_n)$ or column vector $\begin{pmatrix}x_1\\ \vdots\\ x_n\end{pmatrix}$
- vectors can be added (coordinate-wise)
- vectors can be multiplied by a scalar $\lambda \in \R$
- i.e. $1 \times n$ matrix (row) or $n \times 1$ matrix (column)

The set of $n$-dimensional vectors is denoted by:
$$\R^n = \underbrace{\R \times \R \times \dots \times \R}_{n \text{ times}} = \{(x_1, \dots, x_n) : x_i \in \R\}$$
i.e. $n$-dimensional real space $\R^n$.

## HW1071 06 · `20261121_224220.jpg` · Lecture 11.1

**Th.** Consider a matrix $A = (a_{ij})_{i = 1, \dots, m;\ j = 1, \dots, n}$, i.e.
$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} & \cdots & & a_{2n}\\ \vdots & & & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn}\end{pmatrix}$$
The matrix $A$ applied to a COLUMN vector $x = \begin{pmatrix} x_1\\ \vdots\\ x_n\end{pmatrix}$ is the resultant column vector:
$$\underset{m \times \underline{n}\ \ \underline{n} \times 1}{A\,x} = \begin{pmatrix} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n\\ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n\\ \vdots\\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n\end{pmatrix} \to m \times 1$$
(ticks under $m \times \underline{n}$ and $\underline{n} \times 1$ mark the matching inner dimensions.)

Letting $b = \begin{pmatrix} b_1\\ \vdots\\ b_n\end{pmatrix}$, our linear system becomes $Ax = b$. [possible error: $b$ has $m$ entries, $b_1, \dots, b_m$]

**Th.** Homogenous systems
- If $Ax = b$, $b = 0$. Otherwise inhomogenous.
- null-set / kernel of $A$ is the set of solutions to homogenous system $Ax = 0$.
  - denoted by $NS(A) = \ker A := \{x \in \R^n : Ax = 0\}$
  - i.e. the set of vectors $x$ s.t. you get $0$ when you apply $A$ to $x$.

Note that $\ker(A)$ is a set.

Note $Ax$ can be written as: $(Ax)_i = \sum_{p=1}^{n} A_{ip}x_p$.

## HW1071 07 · `20261121_224226.jpg` · Lecture 11.1

**Th.** If $p$ is a vector such that $Ap = b$, $p \in \R^n$, then $\{x \in \R^n \mid Ax = b\} = \{y + p \mid y \in \ker A\}$.

**Proof.** Notice $\forall x, y \in \R^n$, $\lambda \in \R$ we have:
$A(x + y) = Ax + Ay$ (distributivity), $A(\lambda x) = \lambda Ax$ (commutativity).

$\supseteq$) Let $y \in \ker A$ ($Ay = 0$), and set $x := y + p$ where $p$ solves $Ap = b$. Then,
$$Ax = A(y + p) = Ay + Ap = 0 + b = b \implies Ax = b.$$
$\therefore y + p \in \{x \in \R^n \mid Ax = b\}$. Therefore $\{y + p \mid y \in \ker A\} \subseteq \{x \in \R^n \mid Ax = b\}$.

$\subseteq$) Suppose $x \in \R^n$ satisfies $Ax = b$. Then $y := x - p$ solves:
$$A(x - p) = Ax - Ap = b - b = 0 \implies y = x - p \in \ker A.$$
Therefore $\{x \in \R^n \mid Ax = b\} \subseteq \{y + p \mid y \in \ker A\}$.

**Rem.** Since both sets are improper subsets of each other, they must be equal.
$\therefore$ Any solution of $Ax = b$ is of the form $y + p$, $y \in \ker A$. $\square$

## HW1071 08 · `20261121_224229.jpg` · Lecture 11.2

**Matrices as linear functions**

**Th.** One way to think about an $m \times n$ matrix $A = (A_{ij})$ is as a linear function:
- $T_A : \R^n \to \R^m$
- $T_A(x) = Ax \in \R^m$, where $x = \begin{pmatrix} x_1\\ \vdots\\ x_n\end{pmatrix} \in \R^n$.

**Th.** A function $T : \R^n \to \R^m$ is a linear transformation if:
- $T(x + y) = T(x) + T(y)$ $\quad \forall x, y \in \R^n$
- $T(\lambda x) = \lambda \cdot T(x)$ $\quad \forall x \in \R^n,\ \forall \lambda \in \R$
- $T(0) = 0$ $\quad 0 \in \R^n$

Note: transform $\approx$ function
- refer to [unclear: course code, reads "361b" or "3616"] linear algebra course:
- input vector(s) move to output vector(s) in $\R^n$. [possible error: outputs lie in $\R^m$]

Note: linear transformations, visually:
- straight lines remain straight (first two)
- the origin remains constant ($T(0) = 0$)

## HW1071 09 · `20261121_224234.jpg` · Lecture 11.2

**Th.** A function $T : \R^n \to \R^m$ is a linear transform iff $\exists$ an $(m \times n)$ matrix $A$ s.t. $T = T_A$.

**Rem.** Think of a transform as a function with vector input.

**Proof.**
$\Rightarrow$) Let $e_1 = \begin{pmatrix}1\\0\\ \vdots\\0\end{pmatrix}$, $e_2 = \begin{pmatrix}0\\1\\ \vdots\\0\end{pmatrix}$, …, $e_n = \begin{pmatrix}0\\ \vdots\\0\\1\end{pmatrix}$.

**Rem.** $e_k$ are unit vectors.
$$T(e_1) =: \begin{pmatrix} a_{11}\\ a_{21}\\ \vdots\\ a_{m1}\end{pmatrix} \in \R^m,\quad T(e_2) =: \begin{pmatrix} a_{12}\\ a_{22}\\ \vdots\\ a_{m2}\end{pmatrix},\ \dots,\ T(e_n) =: \begin{pmatrix} a_{1n}\\ a_{2n}\\ \vdots\\ a_{mn}\end{pmatrix} \in \R^m.$$
Define the matrix $A$ by $A_{ij} := a_{ij}$, $1 \le i \le n$, $1 \le j \le n$. [possible error: should be $1 \le i \le m$] We can now prove $T = T_A$:

for $x = \begin{pmatrix} x_1\\ x_2\\ \vdots\\ x_n\end{pmatrix}$, $x = x_1e_1 + x_2e_2 + \dots + x_ne_n$ (margin: "linear combination"; annotation over $x_k$: "scalars!").
Since $T$ is linear,
$$\begin{aligned} T(x) &= x_1T(e_1) + x_2T(e_2) + \dots + x_n \cdot T(e_n)\\ &= x_1 \cdot \begin{pmatrix} a_{11}\\ a_{21}\\ \vdots\\ a_{m1}\end{pmatrix} + x_2 \cdot \begin{pmatrix} a_{12}\\ a_{22}\\ \vdots\\ a_{m2}\end{pmatrix} + \dots + x_n \cdot \begin{pmatrix} a_{1n}\\ a_{2n}\\ \vdots\\ a_{mn}\end{pmatrix}\\ &= \begin{pmatrix} x_1a_{11} + x_2a_{12} + \dots + x_na_{1n}\\ x_1a_{21} + x_2a_{22} + \dots + x_na_{2n}\\ \vdots\\ x_1a_{m1} + x_2a_{m2} + \dots + x_na_{mn}\end{pmatrix} = Ax = T_A(x) \end{aligned}$$

$\Leftarrow$) Exercise: check $A(x + y) = Ax + Ay$, $A(\lambda x) = \lambda(Ax)$.

## HW1071 10 · `20261121_224237.jpg` · Lecture 11.3

**Matrix multiplication**

**Th.** Element-wise matrix multiplication
- $A \cdot B = (AB)_{ij} = A_{ij}B_{ij}$
- has limited uses, but has very poor properties

**Th.** Matrix multiplication
- the multiplication $C = AB$ for $m \times n$ $A$, $n \times p$ $B$ is defined as $m \times p$ matrix $C$.
- entry at $(i, j)$th position given by $C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}$, $1 \le i \le m$, $1 \le j \le p$

**Ex.** Let $m = n = p = 2$. $A = \begin{pmatrix} a & b\\ c & d\end{pmatrix}$, $B = \begin{pmatrix} e & f\\ g & h\end{pmatrix}$,
$$C = AB = \begin{pmatrix} a & b\\ c & d\end{pmatrix} \cdot \begin{pmatrix} e & f\\ g & h\end{pmatrix} = \begin{pmatrix} ae + bg & af + bh\\ ce + dg & cf + dh\end{pmatrix}$$

**Rem.** $BA = \begin{pmatrix} e & f\\ g & h\end{pmatrix} \cdot \begin{pmatrix} a & b\\ c & d\end{pmatrix} = \begin{pmatrix} ea + fc & eb + fd\\ ga + hc & gb + hd\end{pmatrix} \ne AB.$
Generally, matrix multiplication is NOT commutative!

**Rem.** Dot product ($\cdot$) $n_1$th row of $A$ with the $n_2$th column of $B$, for the $(n_1, n_2)$th element of $C$.

## HW1071 11 · `20261121_224243.jpg` · Lecture 11.3

**Properties of matrix multiplication**

**Th.** Matrix multiplication is
- NOT commutative $A \cdot B \ne B \cdot A$
- associative $A \cdot (B \cdot C) = (A \cdot B) \cdot C$
- distributive $A \cdot (B + C) = A \cdot B + A \cdot C$, $(A + B) \cdot C = A \cdot C + B \cdot C$

**Proof.** Associativity of matrix multiplication
$$\begin{aligned} (A \cdot (B \cdot C))_{ij} &:= \sum_k A_{ik}(B \cdot C)_{kj} && \leftarrow (i, j)\text{th element}\\ &= \sum_k A_{ik}\Bigl(\sum_l B_{kl}C_{lj}\Bigr)\\ &= \sum_k \sum_l A_{ik}B_{kl}C_{lj} && \leftarrow \text{distributivity of } \R\\ ((A \cdot B) \cdot C)_{ij} &:= \sum_k (A \cdot B)_{ik} \cdot C_{kj}\\ &= \sum_k \Bigl(\sum_l A_{il}B_{lk}\Bigr)C_{kj}\\ &= \sum_k \sum_l A_{il}B_{lk}C_{kj} \end{aligned}$$
Interchange $k \leftrightarrow l$. Therefore, $(A \cdot (B \cdot C))_{ij} = ((A \cdot B) \cdot C)_{ij}$. $\square$

**Rem.** $i, j, k, l$ are dummy variables for $\sum$. You can interchange $\sum_k \sum_l = \sum_l \sum_k$, as addition is commutative.

## HW1071 12 · `20261121_224246.jpg` · Lecture 11.3

**Motivations for matrix multiplication**

**Ex.** Consider an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$, for some $m, n, p \in \N$.
Take some $x \in \R^n$. Observe that the vector $Ax \in \R^m$, as $A$ has the same number of columns as $x$ has rows.
$\implies T_A : \R^n \to \R^m$ (a mapping which sends a vector from $\R^n$ to $\R^m$).
Similarly, for some $x \in \R^p$, for a vector $Bx \in \R^n$, $\implies T_B : \R^p \to \R^n$.
A mapping $T_C : \R^p \to \R^m$, where $T_C = T_{AB} = T_A \circ T_B$, i.e. $Cx = (AB)x = A(Bx)$, is a good candidate for the product of $A$ and $B$.
$Cx$ can be thought of as the composition of the two transformations $A$ and $B$ applied to $x$. As an analogy, compare to $h(x) = f(g(x))$, with $\updownarrow$ arrows matching $h(x) \leftrightarrow Cx$, $f \leftrightarrow A$, $g(x) \leftrightarrow (Bx)$.

**Rem.** [Figure F1071-1: commutative triangle] Three nodes: $\R^p$ (bottom left), $\R^n$ (bottom right), $\R^m$ (top right, directly above $\R^n$). Arrow $\R^p \to \R^n$ labelled $B$; arrow $\R^n \to \R^m$ (upward) labelled $A$; diagonal arrow $\R^p \to \R^m$ labelled $C$.
Beside it: $A \cdot (Bx) = (A \cdot B)x$, with $\hat{T}_A \leftarrow \hat{T}_B$ written under $A \cdot (Bx)$ and $\hat{T}_C$ under $(A \cdot B)$.
$\implies T_A \circ T_B = T_C$

## HW1071 13 · `20261121_224635.jpg` · Lecture 11.3

**Motivations for matrix multiplication** (cont.)

**Ex.** We must show that, for $Cx = (AB)x$, that $C$ is given by a matrix. Hence we will compute $A(Bx)$ for some $x \in \R^p$.
By definition of matrix-vector multiplication, $(Bx)_i = \sum_{k=1}^{p} B_{ik}x_k$.
Using the property of matrix product associativity, $A(Bx) = (AB)x$ immediately follows.
Hence $AB = C$ is a matrix? [possible error: the argument is circular (it uses associativity of the matrix product to show the composition is given by the product); the "?" is in the notes]

**Note.** To see why we must prove $(AB)x = A(Bx) \iff (T_A \circ T_B)x = T_A(T_B \cdot x)$, refer to the diagram of mapping $\R^{[illegible]}$ (Figure F1071-1).

**Note.** This is for the following page: $\R^2 = \C$. $i(x + iy) = -y + ix \implies (x, y) \mapsto (-y, x)$. Applying $i$ rotates a vector counter-clockwise by $90^\circ$.

## HW1071 14 · `20261121_224639.jpg` · Lecture 11.3

**Matrix multiplication** (cont.)

**Ex.** Rotation by $90^\circ$ (counter-clockwise), $R : \R^2 \to \R^2$.
[Figure F1071-2: two small coordinate-axis sketches side by side, joined by a curved arrow labelled $R$ from left to right. Left axes: a vector along the positive $x$-axis (marked with a double arrowhead) and a vector pointing into the third quadrant (towards $(-1, -1)$). Right axes: the first vector now along the positive $y$-axis (double arrowhead), and the second now pointing into the fourth quadrant (towards $(1, -1)$). Beside the right sketch: $(1, 0) \mapsto (0, 1)$, $(-1, -1) \mapsto (1, -1)$.]

Notice that $R\begin{pmatrix} x\\ y\end{pmatrix} = \begin{pmatrix} -y\\ x\end{pmatrix}$ $\implies R = T_A$, $A = \begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix}$ as $\begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix}\begin{pmatrix} x\\ y\end{pmatrix} = \begin{pmatrix} -y\\ x\end{pmatrix}$.

When applying $A^2$ to $\begin{pmatrix} x\\ y\end{pmatrix}$,
$$\begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix} \cdot \begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix} \cdot \begin{pmatrix} x\\ y\end{pmatrix} = \begin{pmatrix} -1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix} x\\ y\end{pmatrix}$$
which represents an $180^\circ$ rotation.

**Th.** The identity matrix
- $(I_n)_{ij} = \begin{cases} 1, & i = j\\ 0, & i \ne j\end{cases}$, e.g. $\begin{pmatrix} 1&0&0\\0&1&0\\0&0&1\end{pmatrix}$ for $\R^3$
- $A \cdot I_n = I_n \cdot A = A$
- identity element for $\R^n$.

**Rem.** If $I_n$ is $n \times n$:
$I_n \cdot A = A$ $\forall\ \underline{n} \times p$ matrix $A$.
$A \cdot I_n = A$ $\forall\ m \times \underline{n}$ matrix $A$.
Dimension '$n$' must still match.

## HW1071 15 · `20261121_224741.jpg` · Lecture 11.3

**Th.** Elementary matrices
- every elementary row operation (recall: Gaussian elimination) is given by multiplication by these matrices.
- differs from $I_n$ by only the row operation.

a) multiplying row $i$ of matrix $A$ by $\lambda \in \R$.
- equivalent to multiplying $A$ by $\begin{bmatrix} 1 & & & & 0\\ & \ddots & & & \\ & & \lambda & & \\ & & & \ddots & \\ 0 & & & & 1\end{bmatrix}$, where $\lambda$ is the $(i, i)$th coefficient.
- i.e. row-multiplying transformation

b) swapping rows $i$ and $j$ of matrix $A$.
- equivalent to multiplying $A$ by [sketch of $I_n$ with a dotted square marking rows/columns $i$ and $j$: $0$ on the two diagonal corners, $1$ on the two off-diagonal corners], adding $1$ in $(i, j)$th and $(j, i)$th spots, adding $0$ in $(i, i)$th and $(j, j)$th spots
- i.e. row-switching transformation

c) adding to row $j$ a multiple ($\lambda$) of row $i$ of matrix $A$.
- equivalent to multiplying $A$ by [sketch of $I_n$ with a single $\lambda$ below the diagonal], adding $\lambda$ in the $(i, j)$th spot. [possible error: to add $\lambda$ times row $i$ to row $j$, $\lambda$ goes in the $(j, i)$th spot, not $(i, j)$; the sketch (below the diagonal) is right for $j > i$]
- i.e. row-addition transform

**Rem.** Multiplication on the left: i.e. $[\ ] \cdot A$.

**Th.** Every $n \times n$ matrix $A$, $\underline{\operatorname{rk}(A) = n}$, can be written as: $A = E_1 \cdot E_2 \cdots E_k$, where $E_i$ are elementary matrices. Compare to Gaussian elimination.

## HW1071 16 · `20261121_224745.jpg` · Lecture 11.3 / 11.4

**Transpose of a matrix**

**Th.** Matrix transpose
- If $A$ is $m \times n$, $A\T$ is $n \times m$.
- $(A\T)_{ij} = A_{ji}$
- reflects elements along diagonal

**Ex.**
$$\begin{bmatrix} 1&2&3\\0&1&2\\ \cdot&\cdot&\cdot \end{bmatrix}\T = \begin{bmatrix} 1&0&\cdot\\2&1&\cdot\\3&2&\cdot \end{bmatrix}$$
[the third row of the left matrix is crossed out in the notes (it reads roughly "0 2 1" under the strike-through), and the third column of the right matrix is overwritten (it reads roughly $0$, $2$, $-1$); neither is reliably legible — use only the first two rows]

**Th.** Transpose properties
- $(A + B)\T = A\T + B\T$
- $(A\T)\T = A$
- $(AB)\T = B\T \cdot A\T$

**P.** First two properties are left as (easy) exercises. We will prove $(AB)\T = B\T \cdot A\T$.
Assume $A$ is $m \times n$, $B$ is $n \times p$. Then,
$$\begin{aligned} ((A \cdot B)\T)_{ij} &= (A \cdot B)_{ji} = \sum_{k=1}^{n} A_{jk} \cdot B_{ki} && \leftarrow \text{def. by m. product}\\ (B\T \cdot A\T)_{ij} &= \sum_{k=1}^{n} (B\T)_{ik} \cdot (A\T)_{kj} = \sum_{k=1}^{n} B_{ki} \cdot A_{jk} \end{aligned}$$
$\implies (AB)\T = B\T \cdot A\T$ $\square$

## HW1071 17 · `20261121_224752.jpg` · Lecture 12.1

**Matrix inverses**

**Th.** Matrix inverses
- if $A$ is $m \times n$, $A^{-1}$ is an $n \times m$ matrix s.t. $A \cdot A^{-1} = A^{-1} \cdot A = I_n$ (identity matrix) [possible error: inverses are defined for square $n \times n$ matrices only; with $m \ne n$ the two products have different sizes]
- $A^{-1}$ is unique for a given matrix $A$
  - Proof: Assume $B, C$ are inverses of $A$: $C = I_nC = (B \cdot A) \cdot C = B \cdot (A \cdot C) = B \cdot I_n = B \implies B = C$, the inverse is unique. $\square$
- not every matrix has an inverse

**Th.** Transpose of inverse matrices
- if $A$ is invertible, so is $A\T$
- $(A\T)^{-1} = (A^{-1})\T$
  - Proof:
    $(A \cdot A^{-1})\T = I_n\T = I_n \Leftarrow (A^{-1})\T \cdot (A\T)$
    $(A \cdot A^{-1})\T = I_n\T = I_n \Leftarrow (A\T) \cdot (A^{-1})\T$ $\square$
    [possible error: both lines start from $(A \cdot A^{-1})\T$; the second should start from $(A^{-1} \cdot A)\T$, since $(A^{-1}A)\T = A\T(A^{-1})\T$]

**Rem.** A matrix $A$ is invertible iff:
- $A$ can be reduced to $I_n$, using only elementary row operations
  - This will be seen in the following pages.
- The determinant of $A$ ($\det A$) $\ne 0$.

**Th.** Matrix inverse properties
- $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$
- $((A)^{-1})^{-1} = A$

## HW1071 18 · `20261121_224756.jpg` · Lecture 12.1

**Finding the inverse**

**Th.** Finding the inverse

If we have some $n \times n$ matrix $A$, how do we find $X$ such that $AX = I_n$? i.e.
$$\begin{bmatrix} A_{11} & \cdots & A_{1n}\\ \vdots & \ddots & \vdots\\ A_{n1} & \cdots & A_{nn}\end{bmatrix} \cdot \begin{bmatrix} X_{11} & \cdots & X_{1n}\\ \vdots & \ddots & \vdots\\ X_{n1} & \cdots & X_{nn}\end{bmatrix} = I_n.$$
Let $x_i$ be a column vector representing the $i$th column of $X$, i.e.
$$x_1 = \begin{pmatrix} X_{11}\\ \vdots\\ X_{n1}\end{pmatrix},\quad x_2 = \begin{pmatrix} X_{12}\\ \vdots\\ X_{n2}\end{pmatrix},\ \dots,\ x_n = \begin{pmatrix} X_{1n}\\ \vdots\\ X_{nn}\end{pmatrix}$$
Now, the matrix equation $AX = I_n$ can be written in terms of each $x_i$ as:
$$A \cdot x_1 = \begin{pmatrix} 1\\0\\ \vdots\\0\end{pmatrix},\quad A \cdot x_2 = \begin{pmatrix} 0\\1\\0\\ \vdots\\0\end{pmatrix},\ \dots,\ A \cdot x_n = \begin{pmatrix} 0\\ \vdots\\0\\1\end{pmatrix}$$
i.e. $A \cdot x_1 = e_1$, $A \cdot x_2 = e_2$, $A \cdot x_n = e_n$.
This can be thought of as $n$ systems of $n$ equations, where we want $A \cdot x_i = i$th row of $I_n$ [possible error: $i$th column of $I_n$], i.e. $A \cdot x_i = e_i$. We can solve this using Gaussian elimination.

## HW1071 19 · `20261121_224803.jpg` · Lecture 12.1

**Th.** Finding the inverse, continued

Since the $n$ linear systems have the same matrix $A$, we can use Gaussian elimination on all of the linear systems at once, by constructing a larger augmented matrix: i.e.
$$(A \mid I_n) = \left(\begin{array}{ccc|cccc} A_{11} & \cdots & A_{1n} & 1 & 0 & \cdots & 0\\ \vdots & \ddots & \vdots & 0 & 1 & & \vdots\\ & & & \vdots & & \ddots & 0\\ A_{n1} & \cdots & A_{nn} & 0 & \cdots & 0 & 1\end{array}\right)$$
We want to reduce this to:
$$\begin{bmatrix} 1 & & \\ & \ddots & \\ & & 1\end{bmatrix}\begin{bmatrix} X_{11} & \cdots & X_{1n}\\ \vdots & \ddots & \vdots\\ X_{n1} & \cdots & X_{nn}\end{bmatrix} = \left(\begin{array}{ccc|ccc} 1 & & & * & \cdots & *\\ & \ddots & & \vdots & \ddots & \vdots\\ & & 1 & * & \cdots & *\end{array}\right)$$
with a brace under the right block labelled $X$.

## HW1071 20 · `20261121_224807.jpg` · Lecture 12.1

**Ex.** Finding the inverse of $A = \begin{bmatrix} 2&-3&1\\1&-2&-3\\-2&-2&5\end{bmatrix}$. Form the augmented matrix $[A \mid I_3]$:
$$\left[\begin{array}{ccc|ccc} 2&-3&1&1&0&0\\1&-2&-3&0&1&0\\-2&-2&5&0&0&1\end{array}\right] \xrightarrow{R_2 \leftarrow 2R_2} \left[\begin{array}{ccc|ccc} 2&-3&1&1&0&0\\2&-4&-6&0&2&0\\-2&-2&5&0&0&1\end{array}\right]$$
$$\xrightarrow[R_3 \leftarrow R_3 + R_1]{R_2 \leftarrow R_2 - R_1} \left[\begin{array}{ccc|ccc} 2&-3&1&1&0&0\\0&-1&-7&-1&2&0\\0&-5&6&1&0&1\end{array}\right] \xrightarrow[R_3 \leftarrow R_3 + R_1]{R_1 \leftarrow R_1 - 3R_2} \left[\begin{array}{ccc|ccc} 2&0&22&4&-6&0\\0&-1&-7&-1&2&0\\0&0&41&6&-10&1\end{array}\right]$$
[possible error: the second label of the last step should be $R_3 \leftarrow R_3 - 5R_2$; "$R_3 \leftarrow R_3 + R_1$" does not give the row shown]
$$\longrightarrow \left[\begin{array}{ccc|ccc} 1&0&0&\frac{16}{41}&-\frac{13}{41}&-\frac{11}{41}\\[2pt] 0&1&0&-\frac{1}{41}&-\frac{13}{41}&-\frac{7}{41}\\[2pt] 0&0&1&\frac{6}{41}&-\frac{10}{41}&\frac{1}{41}\end{array}\right]$$
[possible error: the $(2, 5)$ entry is written $-\frac{13}{41}$; it should be $-\frac{12}{41}$, as in the final answer]
Therefore, $A^{-1} = \dfrac{1}{41} \cdot \begin{bmatrix} 16&-13&-11\\-1&-12&-7\\6&-10&1\end{bmatrix}$. (checked: correct)

**Ex.** Finding the inverse of $A = \begin{bmatrix} 1&1\\1&-1\end{bmatrix}$.
$$\left[\begin{array}{cc|cc} 1&1&1&0\\1&-1&0&1\end{array}\right] \to \left[\begin{array}{cc|cc} 1&1&1&0\\0&-2&-1&1\end{array}\right] \to \left[\begin{array}{cc|cc} 1&1&1&0\\0&1&\frac12&-\frac12\end{array}\right] \to \left[\begin{array}{cc|cc} 1&0&\frac12&\frac12\\0&1&\frac12&-\frac12\end{array}\right]$$
(the first matrix is written without its right block.) Therefore $A^{-1} = \frac12\begin{pmatrix} 1&1\\1&-1\end{pmatrix}$.

## HW1071 21 · `20261121_224813.jpg` · Lecture 12.1

**Th.** For an $n \times n$ matrix $A$, the following are equivalent:
i) $A$ is invertible
ii) $A$ has a right inverse
iii) $\operatorname{rank}(A) = n$
iv) $\ker(A) = \{0\}$

**Proof.** This proof will be split into four sub-proofs, in a notable cyclical manner.

1: $A$ is invertible $\implies \ker(A) = \{0\}$.
$A \cdot 0 = 0 \to 0 \in \ker(A)$. If $Ax = 0$, $x = (A^{-1} \cdot A)x = A^{-1} \cdot (A \cdot x) = A^{-1} \cdot 0 = 0$. Therefore $\ker A = \{0\}$. $\square$

2: [crossed-out box, original text unreadable] $\operatorname{rank}(A) = n \Leftarrow \ker(A) = \{0\}$.
If $\ker(A) = \{0\}$, $Ax = 0$ has a unique solution $x = 0$. Thus the r.e. form of $A$ cannot have any 'zero rows'. Therefore, $\operatorname{rank}(A) = n$.

3: $\operatorname{rank}(A) = n \implies A$ has a right inverse.
If $\operatorname{rank}(A) = n$, then $(A \mid b)$ also has rank $n$, for any $b \in \R^n$, i.e. $\operatorname{rank}(A) = n \implies \operatorname{rank}(A \mid b) = n$. $\square$
[possible error: this shows every system $Ax = b$ is solvable; the step to a right inverse (solve $Ax_i = e_i$, HW 18) is not written]

## HW1071 22 · `20261121_224815.jpg` · Lecture 12.1

**Th.** Proof from previous pages continued

3: $\operatorname{rank}(A) = n \implies$ [one crossed-out word] $A$ has a right inverse.
$\operatorname{rank}(A) = n \implies \operatorname{rank}(A \mid b) = n$. Hence, the system $Ax = b$ has a unique solution for all $b \in \R^n$.
In particular, if $b = e_1 = \begin{pmatrix} 1\\0\\ \vdots\\0\end{pmatrix}$, we obtain $x_1 \in \R^n$ such that $A \cdot x_1 = e_1$. Similarly, for $b = e_i$, $x_i \in \R^n$ s.t. $A \cdot x_i = e_i$.
Let $C$ be the matrix with columns $x_1, \dots, x_n$.
$$A \cdot C = A \cdot \begin{pmatrix} | & & |\\ x_1 & \cdots & x_n\\ | & & |\end{pmatrix} = \begin{pmatrix} \vdots & & \vdots\\ Ax_1 & \cdots & Ax_n\\ \vdots & & \vdots\end{pmatrix} = \begin{pmatrix} | & & |\\ e_1 & \cdots & e_n\\ | & & |\end{pmatrix} = I_n$$
Therefore $C$ is a right inverse for $A$. $\square$

4: $A$ has a right inverse $\implies A$ is invertible.
$A \cdot C = I_n$. $\ker(C) = \{0\} \to$ if $Cx = 0$, $x = I_nx = (AC)x$ [crossed out] $= 0x = 0$. [the intended step is $(AC)x = A(Cx) = A0 = 0$]
By (2) and (3), $C$ has a right inverse $B \in \R^n$, such that $C \cdot B = I_n$. [possible error: $B$ is an $n \times n$ matrix, not an element of $\R^n$]
$I_n = A \cdot C = C \cdot B$. As the inverse is unique, $A = B \implies I_n = A \cdot C = C \cdot A$. Therefore $A$ is invertible. $\square$
[possible error: uniqueness of the (two-sided) inverse (HW 17) does not apply directly here; the step is $A = A(CB) = (AC)B = B$]

## HW1071 23 · `20261121_224824.jpg` · Lecture 12.2

**Determinants**

**Th.** Matrix determinants
- a number that measures the distortion of a (signed, $n$-dimensional) volume caused by the linear [crossed-out word] transformation $T_A$.
- $T_A$ preserves area in $\R^2$ iff $ad - bc = 1$, i.e. $\det\begin{bmatrix} a & b\\ c & d\end{bmatrix} = ad - bc$ [possible error: (unsigned) area is preserved iff $\abs{ad - bc} = 1$; $ad - bc = 1$ is the signed version]
- $T_A$ preserves volume (corrected from "area") in $\R^3$ if $\det(A) = 1$, i.e.
$$\det\begin{pmatrix} a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix} = a_{11} \cdot \det\begin{pmatrix} a_{22}&a_{23}\\a_{32}&a_{33}\end{pmatrix} - a_{12} \cdot \det\begin{pmatrix} a_{21}&a_{23}\\a_{31}&a_{33}\end{pmatrix} + a_{13} \cdot \det\begin{pmatrix} a_{21}&a_{22}\\a_{31}&a_{32}\end{pmatrix}$$
(the $(3,3)$ entry of the left matrix is written like $a_{32}$; read as $a_{33}$.)
- A general formula for the determinant for a matrix $A \in \R^n$ is as follows: [possible error: $A$ is an $n \times n$ matrix]
  1) For $n = 1$, $A = [a_{11}]$, $a_{11} \in \R$, $\det A := a_{11}$
  2) For $A = [a_{ij}]_{i,j=1}^{n}$, we set $c_{ij} := (-1)^{i+j} \cdot \det \hat{A}_{ij}$, $\hat{A}_{ij}$ is $(n-1) \times (n-1)$, derived from $A$ after removing the $i$th row and $j$th column, i.e.
$$\hat{A}_{ij} := \begin{bmatrix} a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n}\\ \vdots & & \vdots & \vdots & & \vdots\\ a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j+1} & \cdots & a_{i-1,n}\\ a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j+1} & \cdots & a_{i+1,n}\\ \vdots & & \vdots & \vdots & & \vdots\\ a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn}\end{bmatrix}$$
  Then $\det A := \sum_{j=1}^{n} a_{ij} \cdot c_{ij} = \sum_{j=1}^{n} (-1)^{i+j} \cdot a_{ij} \cdot \det \hat{A}_{ij}$
  [the row $i$ is not fixed in the definition; the later pages expand along any row, so independence of $i$ is assumed but not stated or proved]

## HW1071 24 · `20261121_224828.jpg` · Lecture 12.2

**Determinants: property 1**

**Th.** If $A$ is a diagonal matrix, $\det A = a_{11} \cdot a_{22} \cdots a_{nn}$

**Th.** If $A$ has a zero-row, $\det A = 0$.

**Th.** Linearity of the determinant
Suppose $u, v$, and $a_1, \dots, a_n$ are row vectors in $\R^n$. Consider the matrices
$$A = \begin{bmatrix} a_1\\ \vdots\\ a_{r-1}\\ u + \lambda v\\ a_{r+1}\\ \vdots\\ a_n\end{bmatrix},\quad B = \begin{bmatrix} a_1\\ \vdots\\ a_{r-1}\\ u\\ a_{r+1}\\ \vdots\\ a_n\end{bmatrix},\quad C = \begin{bmatrix} a_1\\ \vdots\\ a_{r-1}\\ v\\ a_{r+1}\\ \vdots\\ a_n\end{bmatrix} \leftarrow r\text{th row}.$$
Then, $\det A = \det B + \lambda \det C$

**Proof.** Expand $\det A$ by the $r$th row. By definition, $\hat{A}_{rj} = \hat{B}_{rj} = \hat{C}_{rj}$ $\forall j = 1, \dots, n$.
Therefore $\det A = \sum_{j=1}^{n} (-1)^{r+j} \cdot (u + \lambda v)_j \cdot \det \hat{A}_{rj}$ ($\leftarrow$ $j$th component of vector $u + \lambda v$, i.e. $u_1 + \lambda v_1 = (u + \lambda v)_1$).
$u = (u_1, \dots, u_n)$, $v = (v_1, \dots, v_n)$ $\implies u + \lambda v = (u_1 + \lambda v_1, \dots, u_n + \lambda v_n)$
$$\begin{aligned} \implies \det A &= \sum_{j=1}^{n} (-1)^{r+j}(u_j + \lambda v_j) \cdot \det \hat{A}_{rj}\\ \text{(by def.)} &= \sum_{j=1}^{n} (-1)^{r+j}u_j \cdot \det \hat{B}_{rj} + \lambda \sum_{j=1}^{n} (-1)^{r+j}v_j \cdot \det \hat{C}_{rj}\\ &= \det B + \lambda \cdot \det C \end{aligned}$$
$\square$

**Rem.** $\det(A + B) \ne \det A + \det B$

(The first two theorems are stated without proof.)

## HW1071 25 · `20261121_224834.jpg` · Lecture 12.3

**Determinants: property 2**

**Th.** Two rows identical $\implies \det A = 0$.
Suppose $A$ is an $n$-square matrix. If two rows are identical, $\det A = 0$.

**Proof.** We will prove by induction on $n$.
For $n = 2$: $A = \begin{bmatrix} a & b\\ a & b\end{bmatrix} \implies \det A = ab - ab = 0$.
Assume that the proposition holds for any $(n-1)$-square matrix, for all $n \ge 3$.
Let $B$ be an $n \times n$ matrix, assume that the rows $k$ and $l$ are equal, $1 \le k < l \le n$. Pick a row $i$ such that $i \ne k$, $i \ne l$, and expand $\det A$ by that row: [possible error: the matrix is called $B$ here and $A$ from now on]
$$\det A = \sum_{j=1}^{n} (-1)^{i+j} \cdot a_{ij} \cdot \det \hat{A}_{ij}$$
By definition, $\hat{A}_{ij}$ is an $(n-1) \times (n-1)$ matrix, and two of its rows are equal. By PMI, $\det \hat{A}_{ij} = 0 \implies \det A = 0$. $\square$

## HW1071 26 · `20261121_224840.jpg` · Lecture 12.3

**Determinants: property 3**

**Th.** Let $A$ be an $m \times n$ matrix. [possible error: should be $n \times n$] Let $B$ be obtained from $A$ by swapping two rows. Then $\det B = -\det A$.

**Proof.** Let $a_1, \dots, a_n \in \R^n$ be the rows of $A$, such that
$$A = \begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_s\\ \vdots\\ a_n\end{pmatrix},\quad B = \begin{pmatrix} a_1\\ \vdots\\ a_s\\ \vdots\\ a_r\\ \vdots\\ a_n\end{pmatrix}$$
note $r$th and $s$th rows are swapped.
Consider the matrix $M$ given by:
$$M = \begin{pmatrix} a_1\\ \vdots\\ a_r + a_s\\ \vdots\\ a_s + a_r\\ \vdots\\ a_n\end{pmatrix} \begin{matrix} \\ \\ \leftarrow r\\ \\ \leftarrow s\\ \\ \\ \end{matrix} \implies \text{Since two rows are identical, } \det M = 0.$$
By linearity of the determinant,
$$\begin{aligned} 0 = \det M &= \det\begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_r + a_s\\ \vdots\\ a_n\end{pmatrix} + \det\begin{pmatrix} a_1\\ \vdots\\ a_s\\ \vdots\\ a_r + a_s\\ \vdots\\ a_n\end{pmatrix} && \text{expand } r\text{th row}\\ &= \det\begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_r\\ \vdots\\ a_n\end{pmatrix} + \det\begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_s\\ \vdots\\ a_n\end{pmatrix} + \det\begin{pmatrix} a_1\\ \vdots\\ a_s\\ \vdots\\ a_r\\ \vdots\\ a_n\end{pmatrix} + \det\begin{pmatrix} a_1\\ \vdots\\ a_s\\ \vdots\\ a_s\\ \vdots\\ a_n\end{pmatrix} && \text{expand } s\text{th row}\\ &= 0 + \det A + \det B + 0 = \det A + \det B. \end{aligned}$$
$\implies \det A + \det B = 0 \implies \det B = -\det A$. $\square$

**Rem.** Compare to $(x + y)^2 = x^2 + x \cdot y + y \cdot x + y^2$, $x := a_r$, $y := a_s$.

## HW1071 27 · `20261121_224846.jpg` · Lecture 12.3

**Uniqueness of the determinant**

**Th.** Let $\R^{n \times n} := A$. There exists a unique function $f : \R^{n \times n} \to \R$ which satisfy the following properties:
i) $f$ is multilinear (linear in each row)
ii) $f$ is alternating ($f$ switches sign when swapping two rows)
iii) $f(I_n) = 1$.
The unique function is called the determinant, denoted by $\det$.
(Stated without proof.)

**Rem.** $\det A = \abs{A}$

**Prop.** Every elementary matrix is invertible, with $E^{-1}$ also being an invertible matrix. In fact, $E^{-1}$ will also be an elementary matrix.

**Ex.** The inverse of:
a) replace $\lambda$ with $\lambda^{-1}$, multiply
b) is its own inverse
c) replace [unfinished in the notes]
(a), b), c) refer to the three elementary matrices of HW 15.)

**Rem.** The [crossed-out word] determinant of an elementary matrix is always non-zero.

## HW1071 28 · `20261121_224850.jpg` · Lecture 12.3

(The page header is cut off at the top of the photo; the content is complete.)

**Th.** If an $n \times n$ matrix $B$ is obtained by $A$, by adding to row $s$ a multiple of row $r$, then $\det B = \det A$.

**Proof.**
$$A = \begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_s\\ \vdots\\ a_n\end{pmatrix},\quad B = \begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_s + \lambda \cdot a_r\\ \vdots\\ a_n\end{pmatrix},\quad \lambda \in \R$$
By linearity of the determinant,
$$\det B = \det\begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_s\\ \vdots\\ a_n\end{pmatrix} + \lambda \cdot \det\begin{pmatrix} a_1\\ \vdots\\ a_r\\ \vdots\\ a_r\\ \vdots\\ a_n\end{pmatrix} = \det A + \lambda \cdot 0 = \det A$$
$\square$

**Ex.** Compute $\det\begin{pmatrix} 1&1&2\\2&1&4\\6&1&6\end{pmatrix}$. We use elementary row operations:
$$\begin{vmatrix} 1&1&2\\2&1&4\\6&1&6\end{vmatrix} = \begin{vmatrix} 1&1&2\\2&1&4\\0&-5&-6\end{vmatrix} = \begin{vmatrix} 1&1&2\\0&-1&0\\0&-5&-6\end{vmatrix} = \begin{vmatrix} 1&1&2\\0&-1&0\\0&0&-6\end{vmatrix} = 1(-1)(-6) = 6$$
(checked: correct.) An arrow points to the last step with the note "assignment! you prove it ☺" (i.e. the determinant of a triangular matrix is the product of its diagonal entries; not proved in the notes).

**Th.** If $A$ is an $n \times n$ matrix such that $\operatorname{rank} A < n$, then $\det A = 0$. (Stated without proof.)

## HW1071 29 · `20261121_224857.jpg` · Lecture 12.4

**Th.** Let $A$ and $B$ be $n \times n$ matrices. Then $\det(A \cdot B) = \det A \cdot \det B$.

With the previous characteristics of matrix determinants, we are finally in a position to prove one of the most [word missing] properties of the determinant.

**P.** Recall: apply elementary row operations $\iff$ multiplying (on left) by elementary matrices.
We will split this proof into cases.

Case 1: $\operatorname{rank} A = n$
Recall: the matrix $A$ can be rewritten as a product of elementary matrices – $A = E_1 \cdots E_r$.
Previous results imply $\det(E \cdot B) = \det E \cdot \det B$, for all elementary matrices $E$.
$$\det A = \det(E_1 \times \dots \times E_r) = \det E_1 \cdot \det(E_2 \times \dots \times E_r) = \dots = \det E_1 \times \det E_2 \times \dots \times \det E_r$$
Also,
$$\det(AB) = \det(E_1 \times \dots \times E_r \times B) = \det E_1 \cdot \det(E_2 \times \dots \times E_r \times B) = \dots = \det E_1 \times \det E_2 \times \dots \times \det E_r \times \det B = \det A \cdot \det B$$
(by previous work)

**Rmk.** If $\operatorname{rank} A > n$, no inverse, no determinant. [possible error: should be $\operatorname{rank} A < n$; then $A$ has no inverse and $\det A = 0$ (HW 28), it does not lack a determinant]

## HW1071 30 · `20261121_224901.jpg` · Lecture 12.4

**Th.** Let $A$ and $B$ be $n \times n$ matrices. Then $\det(A \cdot B) = \det A \cdot \det B$

**P.** Case 2: $\operatorname{rank} A < n$
Recall: by the definition of rank, after a number of elementary row operations we get a row echelon form $\tilde{A}$ with some zero rows:
$$E_1 \times \dots \times E_r \times A = \tilde{A} = \begin{pmatrix} 1 & & & \\ & 1 & & \\ & & \ddots & \\ 0 & 0 & \cdots & 0\end{pmatrix} \Big\} \text{ since } \operatorname{rk} A < n$$
$$\implies 0 = \det \tilde{A} = \det(E_1 \times \dots \times E_r \times A) = \det E_1 \times \dots \times \det E_r \times \det A = c \cdot \det A \quad (c \ne 0)$$
$\implies \det A = 0$
Also, $E_1 \times \dots \times E_r \times A \cdot B = \tilde{A} \cdot B$
$$= \begin{pmatrix} * & & \\ & \ddots & * \\ 0 & \cdots & 0\ 0\end{pmatrix} \cdot \begin{pmatrix} * & \cdots & *\\ \vdots & \ddots & \vdots\\ * & \cdots & *\end{pmatrix} = \begin{pmatrix} * & \cdots & *\\ \vdots & & \vdots\\ 0 & \cdots & 0\end{pmatrix}$$
$\implies 0 = \det(E_1 \times \dots \times E_r \cdot A \cdot B) = \det E_1 \times \dots \times \det E_r \times \det AB = c \cdot \det AB$ $(c \ne 0)$
$\implies 0 = \det AB = \det A \cdot \det B$ $\square$

## HW1071 31 · `20261121_224908.jpg` · Lecture 12.4

**Th.** Recall: if $A$ has a zero-row, $\det A = 0$. Similarly, if $A$ has a zero-column, $\det A = 0$.

**Proof.** We will use induction on $n$. The case $n = 1$ is trivial.
We now assume the proposition is true for all $(n-1) \times (n-1)$ matrices.
Let $A$ be an $n \times n$ matrix whose $r$th column is zero.
We expand $\det A$ by the first row: $\det A = \sum_{j=1}^{n} (-1)^{i+j} \cdot a_{ij} \cdot \det \hat{A}_{ij}$ [possible error: expanding by the first row means $i = 1$ throughout]
Notice that if $j \ne r$, $\hat{A}_{ij}$ is $(n-1) \times (n-1)$ and has a column of zeroes $\implies$ by inductive hypothesis, $\det \hat{A}_{ij} = 0$.
For $j = r$, we have $a_{1r} = 0$.
$a_{ij} \cdot \det \hat{A}_{ij} = 0$ $\forall j = 1, \dots, n$ $\implies \det A = 0$. $\square$

## HW1071 32 · `20261121_224912.jpg` · Lecture 12.4

**Th.** $\det A\T = \det A$

**P.** This is easy to prove for elementary matrices. We will split this proof into cases.

Case 1: $\operatorname{rank} A = n$
$\implies A = E_1 \times \dots \times E_k$, $A\T = E_k\T \times \dots \times E_1\T$ ($E_i$ is elementary matrix)
$$\implies \det A\T = \det E_k\T \times \dots \times \det E_1\T = \det E_k \times \dots \times \det E_1 = \det(E_1 \times \dots \times E_k) = \det A$$

Case 2: $\operatorname{rank} A < n$
Recall that if $\operatorname{rank} A < n$, $\det A = 0$.
$\implies E_1 \times \dots \times E_k \cdot A = \tilde{A}$, where $\tilde{A}$ has a zero row.
$$\implies 0 = \det \tilde{A}\T = \det(A\T \cdot E_k\T \times \dots \times E_1\T) = \det A\T \cdot \det E_k\T \times \dots \times \det E_1\T = c \cdot \det A\T \quad (c \ne 0)$$
$\implies 0 = \det A\T = \det A$ $\square$
($\det \tilde{A}\T = 0$ because $\tilde{A}\T$ has a zero column, HW 31; the notes do not say so.)

## HW1071 33 · `20261121_224918.jpg` · Lecture 12.4

**Th.** $A$ is invertible iff $\det A \ne 0$.

**P.** We first prove in the forward direction:
Recall: [crossed-out word] $\operatorname{rank} A = n$ iff $A$ is invertible.
If $\operatorname{rank} A = n \implies A = E_1 \times \dots \times E_k \implies \det A = \underbrace{\det E_1}_{\ne 0} \times \dots \times \underbrace{\det E_k}_{\ne 0}$ [crossed out] $\ne 0$.
Therefore $A$ is invertible if $\det A \ne 0$. [possible error: what was shown is "$A$ invertible $\implies \det A \ne 0$" ("only if")]
We now prove in the reverse direction:
Suppose $A$ is not invertible. $\implies \operatorname{rank} A < n \implies \det A = 0$ by previous work. $\square$

## HW1071 34 · `20261121_224923.jpg` · Lecture 13.1

**Eigenvalues and eigenvectors**

**Th.** Suppose $A$ is an $n \times n$ matrix.
- $x \in \C^n$, $x \ne 0$, $x$ is an eigenvector of $A$ if $Ax = \lambda x$
- eigenvector: $x$, eigenvalue: $\lambda$
- An eigenvector of a matrix $A$ retains its direction after the linear transformation $T_A$, only changing magnitude (in proportion to $\lambda$)

**Ex.** Suppose $A$ is a diagonal matrix. The eigenvalues of $A$ are $a_{11}, a_{22}, \dots, a_{nn}$. The corresponding eigenvectors are $e_1, e_2, \dots, e_n$.

**Ex.** $A = \begin{pmatrix} 1 & 3\\ 4 & 2\end{pmatrix}$, $x = \begin{pmatrix} -1\\ 1\end{pmatrix}$
$\implies Ax = \begin{pmatrix} 1 & 3\\ 4 & 2\end{pmatrix} \cdot \begin{pmatrix} -1\\ 1\end{pmatrix} = \begin{pmatrix} 2\\ -2\end{pmatrix} = -2 \cdot x$
$\implies -2$ is an eigenvalue, with eigenvector $x = \begin{pmatrix} -1\\ 1\end{pmatrix}$

## HW1071 35 · `20261121_224931.jpg` · Lecture 13.1

**Finding eigenvalues and eigenvectors**

**Th.** Finding eigenvalues and eigenvectors
- first: find eigenvalues
  - we must find $\lambda \in \R$ such that $Ax = \lambda x$ has a non-zero solution $x$.
  - $Ax - \lambda x = 0 \implies (A - \lambda \cdot I)x = 0$
  - This homogenous system has a non-zero solution $x$ iff $\operatorname{rank}(A - \lambda \cdot I) < n \iff \det(A - \lambda I) = 0$
  - $\det(A - \lambda I) = 0$ is a polynomial equation for $\lambda$.

**Def.** Given an $n \times n$ matrix $A$, the function $P_A(\lambda) := \det(A - \lambda I)$ is called the characteristic polynomial of $A$.
The roots of the characteristic polynomial are the eigenvalues of $A$.
For each eigenvalue $\lambda$, we solve the system $(A - \lambda I)x = 0$ and the solutions are the eigenvectors corresponding to $\lambda$. [the zero solution is not an eigenvector (HW 34); not said here]

## HW1071 36 · `20261121_224935.jpg` · Lecture 13.1

**Vector spaces**

**Th.** Vector spaces
- A vector space over a field $\mathbb{F}$ is a non-empty set $V$ equipped with two operations, $+ : V \times V \to V$, $\times : V \times V \to V$ [possible error: scalar multiplication is $\mathbb{F} \times V \to V$]
- such that the following axioms hold $\forall u, v, w \in V$, $a, b \in \mathbb{F}$:
  1) $u + (v + w) = (u + v) + w$ (associative)
  2) $u + v = v + u$ (commutative)
  3) $\exists\, 0 \in V$ s.t. $u + 0 = u$ (add. identity element; "zero element" crossed out)
  4) $\forall u \in V$, $\exists -u \in V$ s.t. $u + (-u) = 0$ (add. inverse)
  5) $a \cdot (b \cdot v) = (a \cdot b) \cdot v$ (associative; "distributivity" crossed out)
  6) $\exists\, 1 \in \mathbb{F}$ s.t. $1 \cdot u = u$ (mult. identity element)
  7) $a \cdot (u + v) = a \cdot u + a \cdot v$ (distributivity, 1)
  8) $(a + b) \cdot u = a \cdot u + b \cdot u$ (distributivity, 2) [the label reads "distributivity, v" or "2"]
- Notation: elements of $V$ are vectors, elements of $\mathbb{F}$ are scalars
- Note: vector spaces do not define multiplication between vectors – this is performed by other mathematical structures beyond the depth of this course.

**Rmk.** Uniqueness:
- $0 \in V$ is unique
- $\forall u \in V$, $-u \in V$ is unique
(stated without proof)
Difference between two vectors: $u - v := u + (-v)$

## HW1071 37 · `20261121_224943.jpg` · Lecture 13.2

**Examples of vector spaces**

**Ex.**
1) $V = \R^n \implies \mathbb{F} = \R$; $V = \C^n \implies \mathbb{F} = \C$ (and over $\R$); $V = \{0\} \implies$ any $\mathbb{F}$
2) $V = \R[x]$ (polynomials with real coefficients); $V = \R_n[x] = \{p \in \R[x] : \deg(p) \le n\} \implies \R$
3) $V = C([a, b]) := \{f : [a, b] \to \R : f \text{ is continuous}\} \implies \R \cap [a, b]$ [possible error: the field is $\R$; "$\R \cap [a, b]$" is not a field]
4) $V = M_{m \times n}(\mathbb{F})$ (vector space of $m \times n$ matrices with coefficients from $\mathbb{F}$) $\implies \mathbb{F}$
5) $V = \R \implies \mathbb{F} = \Q$
(the arrow "$\implies$" gives the field over which $V$ is a vector space.)

**Non-ex.**
1) $\{(a_1, \dots, a_n) \in \R^n : a_i > 0,\ i = 1, \dots, n\}$ is not a vector space – no additive inverses
2) $\{(1, 2), (3, 4)\} \subset \R^2$ is not a vector space over $\R$; we can make it a vector space over $\mathbb{F} = \{0, 1\}$ defining $(1, 2) + (3, 4) = (1, 2)$, etc.

## HW1071 38 · `20261121_224947.jpg` · Lecture 13.2

**Subsets of vector spaces (vector subspace)**

**Th.** [crossed-out word] Vector subspaces
- a subset $W \subseteq V$ of a vector space $V$ is a vector subspace if it is a vector space w.r.t. the operations of $V$.
- denoted by $W \le V$.
- $W$ is a subspace of $V$ iff $\forall u, v \in \mathbb{F}$, $\lambda \in \mathbb{F}$, [possible error: should be $\forall u, v \in W$; and $W \ne \emptyset$ is needed, as the next item says]
  1) $u + v \in W$
  2) $\lambda \cdot u \in W$
  - This allows you to verify a set $W$ is a subspace by verifying:
    1) $W$ is non-empty (show $0 \in W$)
    2) addition is closed under $W$
    3) scalar multiplication under $W$
(stated without proof.)

**Ex.** A line/plane which goes through the origin is a subspace of $\R^n$. A line/plane which does NOT go through the origin is NOT a subspace of $\R^n$, as it does not contain an additive identity.

**Ex.** $W = \{(x, y, z) \in \R^3 : x + y = 2z\}$ is a subspace of $\R^3$. (no working given)

## HW1071 39 · `20261121_224956.jpg` · Lecture 13.2

**Eigenspaces**

**Th.** Let $A \in M_{n \times n}(\C)$, $\lambda \in \C$. Then, the set $W := \{v \in \C^n : Av = \lambda v\}$ is a vector subspace of $\C^n$.

**Rmk.** $W \ne \{0\}$ iff $\lambda$ is an eigenvalue of $A$. In this case, $W$ is an eigenspace of $A$.

**P.** If $0 \in W$, $A \cdot \begin{pmatrix} 0\\ \vdots\\ 0\end{pmatrix} = \begin{pmatrix} 0\\ \vdots\\ 0\end{pmatrix} = \lambda\begin{pmatrix} 0\\ \vdots\\ 0\end{pmatrix}$ [read: "$0 \in W$ since …"]
Let $v, w \in W$, $c \in \C$. Then,
$$A(v + w) = Av + Aw = \lambda v + \lambda w = \lambda(v + w) \implies v + w \in W$$
$$A(c \cdot v) = c \cdot Av = c\lambda v = \lambda(cv) \implies cv \in W$$
$\therefore W \le V$ [possible error: $W \le \C^n$] $\square$

**Coro.** $\ker(A)$ is a subspace of $\C^n$.
- if $\ker(A) \ne \{0\}$, $\ker A$ is the eigenspace associated to $\lambda = 0$.

## HW1071 40 · `20261121_225001.jpg` · Lecture 13.3

**Span and linear combinations**

**Th.** Linear combinations: $a_1v_1 + \dots + a_nv_n$, $v_1, \dots, v_n \in V$, $a_1, \dots, a_n \in \mathbb{F}$

**Th.** Span
- Let $\Omega \subseteq V$. The span of $\Omega$ ($\operatorname{span} \Omega$) is the set of all finite linear combinations of vectors in $\Omega$.
- $\operatorname{span}(\Omega)$ is the intersection of all subspaces of $V$ that contain $\Omega$.
- $\operatorname{span}(\Omega)$ is a subspace of $V$.
(the last two stated without proof.)

**Ex.** $V = \R_4[x]$, $\Omega = \{1, x, x^2\} \implies \operatorname{span}(\Omega) = \R_2[x]$.
$V = \R_3$ [read as $\R^3$], $\Omega = \{(x, y, z) \in \R^3 : z = 0,\ x^2 + y^2 \le 1\} \implies \operatorname{span}(\Omega) = \{(x, y, z) \in \R^3 : z = 0\}$
In general, $\operatorname{span}\{e_1, e_2, \dots, e_n\} = \R^n$.

## HW1071 41 · `20261121_225006.jpg` · Lecture 13.3

**Linear dependence**

**Th.** Linear dependence
- $\Omega \subseteq V$ is linearly dependent if $\exists v_1, \dots, v_n \in \Omega$ s.t. $a_1v_1 + \dots + a_nv_n = 0$ for some $a_1, \dots, a_n \in \mathbb{F}$, where not all $a_i = 0$.
- $\Omega$ is linearly dependent if one (or more) of the vectors in $\Omega$ can be removed s.t. the span remains unchanged.
  - i.e. one of the vec. is a lin. comb. of the others.

**Rem.** Checking linear independence
- If $0 \in \Omega$, then $1 \cdot 0 = 0$, so $\Omega$ is automatically linearly dependent ("independent" corrected to "dependent").
- Let $\Omega = \{u, v\}$ for distinct $u, v$. $\Omega$ is linearly $\underline{\text{dependent}}$ iff $u = \alpha v$ or $v = \alpha u$ for $\alpha \in \mathbb{F}$ (i.e. $u, v$ are parallel)
- Let $\Omega = \{v_1, \dots, v_n\} \subset V$. $\Omega$ is linearly $\underline{\text{independent}}$ iff the only sol. to $a_1v_1 + \dots + a_nv_n = 0$ is $a_1 = \dots = a_n = 0$.

**Th.** Let $A \in M_{n \times n}(\R)$, let $a_1, \dots, a_n$ be its rows. $\Omega := \{a_1, \dots, a_n\} \subseteq \R^n$ is linearly independent iff $\operatorname{rank} A = n$. (stated without proof)
[the $v_i$ in the first item should be distinct; not stated]

## HW1071 42 · `20261121_225012.jpg` · Lecture 13.4

**Th.** Vector space basis
- subset $B \subseteq V$ s.t.
  1) $\operatorname{span}(B) = V$
  2) $B$ is linearly independent

**Ex.**
- $V = \R^n$, $B = \{e_1, \dots, e_n\}$ is a basis
- $V = \R_n[x]$, $B = \{1, x, x^2, \dots, x^n\}$ is a basis
- $V = \{(a, b, c) \in \R^3 : a + b = c\}$, $B = \{(1, 0, 1), (0, 1, 1)\}$ is a basis
- $V = \C$, $\mathbb{F} = \R \implies B = (1, i)$ is a basis.

**Th.** Dimension
- $V$ is finite dimensional if its basis $B$ is finite.
- the number of elements in $B$ is its dimension – $\dim_{\mathbb{F}} V$ or $\dim V$.
- the dimension is well-defined, i.e. independent of $B$. (stated without proof)

**Ex.** $\dim_{\R} \R^n = n$, $\dim_{\mathbb{F}} \C^n = \begin{cases} n & \text{if } \mathbb{F} = \C\\ 2n & \text{if } \mathbb{F} = \R\end{cases}$, $\dim \R[x] = \infty$, $\dim_{\R} M_{m \times n}(\R) = m \cdot n$, $\dim \R^\infty$ is undef. (infinite)

## HW1071 43 · `20261121_225018.jpg` · Lecture 13.4

**Th.** Let $B = \{v_1, \dots, v_n\}$ be a basis of $V$. For each $v \in V$, $\exists$ unique set of scalars, $a_1, \dots, a_n \in \mathbb{F}$ s.t. $v = a_1v_1 + a_2v_2 + \dots + a_nv_n$.
We call $(a_1, \dots, a_n) =: [v]_B$ the $\underline{\text{coordinates}}$ of $v$, with respect to $B$.

**Proof.** $V = \operatorname{span}(B) \implies \exists a_1, \dots, a_n \in \mathbb{F}$.
Regarding uniqueness, suppose $\tilde{a}_1, \dots, \tilde{a}_n \in \mathbb{F}$ satisfy $v = \tilde{a}_1v_1 + \dots + \tilde{a}_nv_n$.
Then, $0 = v - v = (a_1 - \tilde{a}_1) \cdot v_1 + \dots + (a_n - \tilde{a}_n) \cdot v_n$
(basis, lin. ind) $\implies a_i - \tilde{a}_i = 0$ $\forall i = 1, \dots, n$ $\implies (a_1, \dots, a_n) = (\tilde{a}_1, \dots, \tilde{a}_n)$ $\square$

**Th.** Let $V$ be a vector space over $\R$, s.t. $\dim V < \infty$. Letting $n = \dim V$, $V$ is isomorphic (as a vector space) to $\R^n$, i.e. there exists an invertible $\underline{\text{linear}}$ transformation which maps $V$ to $\R^n$. $\mapsto T : V \to \R^n$. (stated without proof)

**Rem.** $T(u + v) = T(u) + T(v)$, $T(\lambda v) = \lambda \cdot T(v)$

---
*(From HW 44 the notebook changes: pages have no lecture header, and results are numbered 1., 2., … They are analysis results — a list of proofs.)*

## HW1071 44 · `20261121_225046.jpg` · [no header] 1.

**1. The squeeze theorem for sequences**

**Def.** [possible error: this is a theorem, not a definition] Suppose $(a_n)_{n \in \N}$, $(b_n)_{n \in \N}$ and $(c_n)_{n \in \N}$ are sequences of real numbers such that:
1) $a_n \le b_n \le c_n$ $\forall n \in \N$
2) $\lim a_n = \lim c_n = L$, $L \in \R$
Then $\lim b_n = L$.

**P.**
$$\begin{aligned} \abs{b_n - L} &= \abs{b_n - a_n + a_n - L}\\ &\le \abs{b_n - a_n} + \abs{a_n - L} && \text{by } \Delta\\ &= b_n - a_n + \abs{a_n - L} && \text{by 1)}\\ &\le c_n - a_n + \abs{a_n - L} && \text{by 1)}\\ &= c_n - L + L - a_n + \abs{a_n - L}\\ &= \abs{c_n - L + L - a_n} + \abs{a_n - L}\\ &\le \abs{c_n - L} + \abs{L - a_n} + \abs{a_n - L} && \text{by } \Delta \end{aligned}$$
Fix $\varepsilon > 0$.
$\lim a_n = L \overset{\text{def.}}{\implies} \exists N_1 \in \N$ s.t. if $n > N_1$, then $\abs{a_n - L} < \frac13\varepsilon$
$\lim c_n = L \overset{\text{def.}}{\implies} \exists N_2 \in \N$ s.t. if $n > N_2$, then $\abs{c_n - L} < \frac13\varepsilon$
Allow $N = \max\{N_1, N_2\}$. If $n \ge N$, then: [possible error: should be $n > N$, to match $n > N_1$, $n > N_2$]
$$\abs{b_n - L} \le \abs{c_n - L} + \abs{L - a_n} + \abs{a_n - L} < \tfrac13\varepsilon + \tfrac13\varepsilon + \tfrac13\varepsilon \implies \abs{b_n - L} < \varepsilon.$$
Therefore, by the definition of the limit, $\lim b_n = L$. $\square$

## HW1071 45 · `20261121_225051.jpg` · [no header] 2.

**2. Every sequence has a monotone subsequence.** Consider the sequence of reals $(a_n)_{n \in \N}$.

**P.** We will split this proof into cases.

(Lemma) [definition] $k \in \N$ is a peak point of $(a_n)_{n \in \N}$ if $a_k > a_n$ for all $n > k$.

Case 1. There are infinitely many peak points $n_1, n_2, n_3, \dots$, where $n_1 < n_2 < \cdots$.
By definition, $a_{n_1} > a_{n_2} > \cdots$. Thus $(a_{n_k})_{k \in \N}$ is monotone.

Case 2. There are finitely many peak points $k_1, k_2, k_3, \dots, k_m$, $m \in \N$. [the case of no peak points is not mentioned; the argument covers it with $n_1 = 1$]
Let $n_1 = \max\{k_1, k_2, \dots, k_m\} + 1$. Since $n_1 \notin \{k_1, k_2, \dots, k_m\}$, $n_1$ is not a peak point. $\implies \exists n_2 > n_1$ such that $a_{n_2} > a_{n_1}$ [possible error: "not a peak point" gives $a_{n_2} \ge a_{n_1}$, not $>$]
Since $n_2 \notin \{k_1, k_2, \dots, k_m\}$, $n_2$ is not a peak point. $\implies \exists n_3 > n_2$ such that $a_{n_3} > a_{n_2}$.
Inductively, $(a_{n_k})_{k \in \N}$ is monotone. $\square$

## HW1071 46 · `20261121_225055.jpg` · [no header] 3.1

**3.1. Property of limits:** $\lim_{x \to a}(f(x) + g(x)) = \ell + m$.

**P.**
$$\abs{f(x) + g(x) - (\ell + m)} = \abs{f(x) - \ell + g(x) - m} \le \abs{f(x) - \ell} + \abs{g(x) - m}$$
Fix $\varepsilon > 0$.
$\lim_{x \to a} f(x) = \ell \overset{\text{def.}}{\implies} \exists \delta_1 > 0$ s.t. if $0 < \abs{x - a} < \delta_1$ then $\abs{f(x) - \ell} < \frac12\varepsilon$
$\lim_{x \to a} g(x) = m \overset{\text{def.}}{\implies} \exists \delta_2 > 0$ s.t. if $0 < \abs{x - a} < \delta_2$ then $\abs{g(x) - m} < \frac12\varepsilon$
Allow $\delta = \min\{\delta_1, \delta_2\}$. If $0 < \abs{x - a} < \delta$, then:
$$\abs{f(x) + g(x) - (\ell + m)} \le \abs{f(x) - \ell} + \abs{g(x) - m} < \tfrac12\varepsilon + \tfrac12\varepsilon < \varepsilon.$$
[possible error: the last "$<$" should be "$=$"]
Therefore, by the definition of the limit, $\lim_{x \to a}(f(x) + g(x)) = \ell + m$.

## HW1071 47 · `20261121_225104.jpg` · [no header] 3.2

**3.2. Property of limits:** $\lim_{x \to a} f(x) \cdot g(x) = \ell \cdot m$

**P.**
$$\begin{aligned} \abs{f(x) \cdot g(x) - \ell \cdot m} &= \abs{f(x) \cdot g(x) - g(x) \cdot \ell + g(x) \cdot \ell - \ell \cdot m}\\ &= \abs{g(x) \cdot (f(x) - \ell) + \ell(g(x) - m)}\\ &\le \abs{g(x)} \cdot \abs{f(x) - \ell} + \abs{\ell} \cdot \abs{g(x) - m} \end{aligned}$$
Fix $\varepsilon > 0$.
$\lim_{x \to a} g(x) = m \overset{\text{def.}}{\implies} \exists \delta_2 > 0$ s.t. if $0 < \abs{x - a} < \delta_2$ then $\abs{g(x) - L_2} < \varepsilon'$
$\implies -\varepsilon' < g(x) - L_2 < \varepsilon' \implies L_2 - \varepsilon' < g(x) < L_2 + \varepsilon' \implies \abs{g(x)} < \max\{\abs{L_2 - \varepsilon'}, \abs{L_2 + \varepsilon'}\}$.
[possible error: the limit is called $m$ and then $L_2$; $\varepsilon'$ is not fixed (any fixed $\varepsilon' > 0$, e.g. $1$, works)]
Let $g' = \max\{\abs{L_2 - \varepsilon'}, \abs{L_2 + \varepsilon'}\}$. Therefore $\abs{g(x)} < g'$.
$\lim_{x \to a} f(x) = \ell \overset{\text{def.}}{\implies} \exists \delta_1 > 0$ s.t. if $0 < \abs{x - a} < \delta_1$ then $\abs{f(x) - \ell} < \frac{\varepsilon}{2} \cdot \frac{1}{g'}$
$\lim_{x \to a} g(x) = m \overset{\text{def.}}{\implies} \exists \delta_3 > 0$ s.t. if $0 < \abs{x - a} < \delta_3$ then $\abs{g(x) - m} < \frac{\varepsilon}{2} \cdot \frac{1}{\ell}$
[possible error: needs $\abs{\ell}$ and $\ell \ne 0$ (the case $\ell = 0$ is not treated)]
Let $\delta = \min\{\delta_1, \delta_2, \delta_3\}$. If $0 < \abs{x - a} < \delta$, then
$$\begin{aligned} \abs{f(x) \cdot g(x) - \ell \cdot m} &\le \abs{g(x)} \cdot \abs{f(x) - \ell} + \abs{\ell} \cdot \abs{g(x) - m}\\ &< g' \cdot \frac{\varepsilon}{2} \cdot \frac{1}{g'} + \ell \cdot \frac{\varepsilon}{2} \cdot \frac{1}{\ell} < \varepsilon/2 + \varepsilon/2 < \varepsilon. \end{aligned}$$
Therefore, by the definition of the limit, $\lim_{x \to a} f(x) \cdot g(x) = \ell \cdot m$. $\square$

## HW1071 48 · `20261121_225111.jpg` · [no header] 5., 6.1

(No item 4 appears in the photos; the numbering jumps from 3.2 to 5.)

**5. Differentiable implies continuous**

**P.**
$$\begin{aligned} \lim_{x \to x_0} f(x) &= \lim_{x \to x_0}\Bigl(\frac{f(x) - f(x_0)}{x - x_0} \cdot (x - x_0) + f(x_0)\Bigr)\\ &= \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} \cdot \lim_{x \to x_0}(x - x_0) + f(x_0)\\ &= f'(x_0) \cdot 0 + f(x_0) = f(x_0) \end{aligned}$$

**Tips.** def. of continuity $\to$ def. of derivative

**6.1. Property of derivative:** $(f + g)'(x) = f'(x) + g'(x)$

**P.**
$$\begin{aligned} (f + g)'(x_0) &= \lim_{x \to x_0} \frac{(f(x) + g(x)) - (f(x_0) + g(x_0))}{x - x_0}\\ &= \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} + \frac{g(x) - g(x_0)}{x - x_0}\\ &= f'(x_0) + g'(x_0) \end{aligned}$$

## HW1071 49 · `20261121_225117.jpg` · [no header] 7.

**7. Extrema are critical points**

**Def.** [a theorem] Suppose a function $f : [a, b] \to \R$ has a local extremum on $c \in (a, b)$. If $f'(c)$ exists, then $f'(c) = 0$.

**P.** WLOG, assume $c$ is a local maximum. If $c$ is a local minimum, apply to $-f$.
(✡ marker, referring to the note at the bottom.)
Let $f$ be defined on $[c, c + \delta)$. $f(x) - f(c)$ [crossed out] $\le 0$. $x - c \ge 0$. $\forall x \in [c, c + \delta)$. Therefore $\dfrac{f(x) - f(c)}{x - c} \le 0$.
Let $f$ be defined on $(c - \delta, c]$. $f(x) - f(c)$ [crossed out] $\le 0$. $x - c \le 0$. Therefore $\dfrac{f(x) - f(c)}{x - c} \ge 0$.
[the quotient is undefined at $x = c$; the intervals should exclude $c$]

✡ For a point $c \in (a, b)$, for all $\delta > 0$, $\exists$ interval $(c - \delta, c + \delta)$ s.t. $(c - \delta, c + \delta) \subseteq (a, b)$ [possible error: should be "there exists $\delta > 0$ such that $(c - \delta, c + \delta) \subseteq (a, b)$"]

Since $\lim_{x \to c^+} \dfrac{f(x) - f(c)}{x - c} = \lim_{x \to c^-} \dfrac{f(x) - f(c)}{x - c} = 0$
$\implies \lim_{x \to c} \dfrac{f(x) - f(c)}{x - c} = 0 \implies f'(c) = 0$.
[possible error: the step that the right limit is $\le 0$, the left limit $\ge 0$, and both equal $f'(c)$ (so $f'(c) = 0$) is not written; the notes assert both one-sided limits are $0$]

## HW1071 50 · `20261121_225120.jpg` · [no header] 8.

**8. Rolle's theorem**

**Def.** [a theorem] Suppose $f : [a, b] \to \R$ is continuous on $[a, b]$ and differentiable on $(a, b)$. If $f(a) = f(b)$, $\exists c \in (a, b)$ s.t. $f'(c) = 0$.

**Proof.** If $f(x)$ is constant, the theorem immediately follows. Assume $f$ is not constant.
WLOG, there exists either (or both)
- $x_0 \in (a, b)$ s.t. $f(x_0) > f(a)$
- $x_1 \in (a, b)$ s.t. $f(x_0) < f(a)$ [possible error: should be $f(x_1) < f(a)$]
By EVT, $f$ has a global maximum $c$ on $[a, b]$. $f(c) \ge f(x_0) > f(a) = f(b)$, therefore $c \ne a$ and $c \ne b$.
Therefore $c \in (a, b)$, and since $c$ is an extremum, and $f'(c)$ exists, $f'(c) = 0$.
[only the $x_0$ case is written; the $x_1$ case (global minimum) is left to "WLOG"]

## HW1071 51 · `20261121_225127.jpg` · [no header] 9.

**9. The Mean Value theorem**

**Def.** [a theorem] Suppose $f : [a, b] \to \R$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Then $\exists c \in (a, b)$ s.t. $f'(c) = \dfrac{f(b) - f(a)}{b - a}$

**Rem.** Consider this an extension of Rolle's theorem, where $f(a)$ may not necessarily equal $f(b)$.

**P.** Consider the arbitrary function $\varphi$:
$$\varphi(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$$
Observe that $\varphi(b) = 0$ and $\varphi(a) = 0$. As $\varphi(a) = \varphi(b) = 0$, apply Rolle's theorem. Therefore $\exists c \in (a, b)$ s.t. $\varphi'(c) = 0$.
Observe that
$$\varphi'(x) = f'(x) - \frac{f(b) - f(a)}{b - a},\qquad \varphi'(c) = 0 = f'(c) - \frac{f(b) - f(a)}{b - a}$$
Therefore $f'(c) = \dfrac{f(b) - f(a)}{b - a}$.

## HW1071 52 · `20261121_225131.jpg` · [no header] 10.

**10. Integrability through partitions**

**Def.** [a theorem (Riemann criterion)] A function $f : [a, b] \to \R$ is integrable on $[a, b]$ iff $\forall \varepsilon > 0$, $\exists$ partition $P$ such that $U(f, P) - L(f, P) < \varepsilon$.

**Proof.** We will first prove in the forward direction. Assume $f$ is integrable. Fix $\varepsilon > 0$. $\exists$ partitions $P_1, P_2$ such that
$$\int_a^b f(x) \dd x = \underline{\int_a^b} f(x) \dd x < L(f, P_1) + \frac{\varepsilon}{2}$$
$$\int_a^b f(x) \dd x = \overline{\int_a^b} f(x) \dd x > U(f, P_2) - \frac{\varepsilon}{2}$$
Define $P = P_1 \cup P_2$.
$$U(f, P) - L(f, P) \le U(f, P_2) - L(f, P_1) < \int_a^b f(x) \dd x + \frac{\varepsilon}{2} - \int_a^b f(x) \dd x - \frac{\varepsilon}{2} < \varepsilon.$$
[possible error: the second term should be $-\bigl(\int_a^b f(x) \dd x - \frac{\varepsilon}{2}\bigr)$, giving $= \varepsilon$; as written the line equals $0$]
Now we prove in the reverse direction. Fix $\varepsilon > 0$. Assume $\exists P_\varepsilon$ s.t. $U(f, P) - L(f, P) < \varepsilon$. By the definition of the lower and upper integral,
$$0 \le \overline{\int_a^b} f(x) \dd x - \underline{\int_a^b} f(x) \dd x \le U(f, P) - L(f, P) < \varepsilon$$
Since any $\varepsilon > 0$ can be taken, $\overline{\int_a^b} f(x) \dd x - \underline{\int_a^b} f(x) \dd x = 0$. Therefore $f$ is integrable.
(Upper and lower integrals are written with a bar on the upper / lower limit of the integral sign: $\int_a^{\bar b}$, $\int_{\underline a}^b$.)

## HW1071 53 · `20261121_225138.jpg` · [no header] 11.

**11. Continuous implies integrable**

**Def.** [a theorem] If $f : [a, b] \to \R$ is bounded and continuous at all but finitely many points, then $f$ is integrable.

**P.** Case 1: $f$ is continuous on $[a, b]$
Assume $f$ is continuous on $[a, b]$. Hence $f$ is uniformly continuous on $[a, b]$.
Fix $\varepsilon > 0$. $\exists \delta > 0$ such that $\forall x, y \in \R$ OR $\forall x, y \in [a, b]$, if $\abs{x - y} < \delta$ then $\abs{f(x) - f(y)} < \frac{\varepsilon}{\abs{b - a}}$
Choose $P$ such that $\abs{x_i - x_{i-1}} < \delta$ for all $i = 1, \dots, n$. Then,
$$U(f, P) - L(f, P) = \sum_{i=1}^{n}\Bigl(\sup_{x \in [x_{i-1}, x_i]} f(x) - \inf_{x \in \dots} f(x)\Bigr)(x_i - x_{i-1})$$
Since $f$ is continuous, by the EVT, $\exists x_i', x_i'' \in [x_{i-1}, x_i]$ such that:
$$f(x_i') = \sup_{x \in [x_{i-1}, x_i]} f(x),\quad f(x_i'') = \inf_{x \in [x_{i-1}, x_i]} f(x)$$
Therefore,
$$\begin{aligned} U(f, P) - L(f, P) &= \sum_{i=1}^{n}(f(x_i') - f(x_i''))(x_i - x_{i-1}) < \sum \varepsilon/\abs{b - a} \cdot (x_i - x_{i-1})\\ &= \varepsilon/\abs{b - a} \cdot \sum_{i=1}^{n}(x_i - x_{i-1}) = \varepsilon/\abs{b - a} \cdot (x_n - x_0) = \varepsilon/\abs{b - a} \cdot \abs{b - a} = \varepsilon \end{aligned}$$
$\implies U(f, P) - L(f, P) < \varepsilon$. $\square$
(Only Case 1 is written on this page.)

## HW1071 54 · `20261121_225142.jpg` · [no header] 11. (cont.)

**11. Continuous implies integrable** (cont.)

**P.** Case 2: $f$ has one discontinuity $c \in [a, b]$ [possible error: the choice of $\delta$ below needs $c \in (a, b)$; an endpoint discontinuity is not covered]
Fix $\varepsilon > 0$. Since $f$ is bounded, $\exists M > 0$ such that $\abs{f(x)} < M$ for all $x \in [a, b]$.
Define $\delta := \min\{\frac{\varepsilon}{8M}, \frac{b - c}{2}, \frac{c - a}{2}\} > 0$. By our choice of $\delta$, $[c - \delta, c + \delta] \subseteq [a, b]$.
Since $f$ is continuous on $[a, c - \delta]$ and $[c + \delta, b]$, $f$ is integrable on those intervals.
Therefore $\exists P_1$ of $[a, c - \delta]$ and $\exists P_2$ of $[c + \delta, b]$ such that: $U(f, P_1) - L(f, P_1) < \varepsilon/4$ and $U(f, P_2) - L(f, P_2) < \varepsilon/4$.
Define $P = P_1 \cup P_2$, a partition of $[a, b]$.
$$\begin{aligned} U(f, P) &= U(f, P_1) + U(f, P_2) + \sup_{x \in [c - \delta, c + \delta]} f(x) \cdot (c + \delta - (c - \delta)) < U(f, P_1) + U(f, P_2) + M \cdot 2\delta\\ L(f, P) &= L(f, P_1) + L(f, P_2) + \inf_{x \in [c - \delta, c + \delta]} f(x) \cdot (c + \delta - (c - \delta)) > L(f, P_1) + L(f, P_2) - M \cdot 2\delta\\ U(f, P) - L(f, P) &< [U(f, P_1) - L(f, P_1)] + [U(f, P_2) - L(f, P_2)] + 2M \cdot 2\delta\\ &= \varepsilon/4 + \varepsilon/4 + 4M \cdot \delta \le \varepsilon/4 + \varepsilon/4 + 4M \cdot \frac{\varepsilon}{8M} \le \varepsilon/2 + \varepsilon/2 = \varepsilon. \end{aligned}$$
[possible error: "$= \varepsilon/4 + \varepsilon/4 + \dots$" should be "$<$"; the final "$\le \varepsilon/2 + \varepsilon/2$" is in fact "$=$"] $\square$

Case 3: If $f$ has more discontinuities (but still a finite amount), apply Case 2 repeatedly. $\square$

## HW1071 55 · `20261121_225149.jpg` · [no header] 12.

**12. Monotone implies integrable**

**Th.** If $f : [a, b] \to \R$ is integrable, it is monotone. [possible error: converse stated; should be "If $f$ is monotone, it is integrable", as in the title]

**P.** Without loss of generality, assume $f$ is monotone increasing.
Fix $\varepsilon > 0$. Let $P$ be the partition that splits $[a, b]$ into $n$ equal parts, with trivial length $\frac{b - a}{n}$, $x_k = a + k \cdot \frac{b - a}{n}$, $n \in \N$. Then,
$$\begin{aligned} U(f, P) - L(f, P) &= \sum_{i=1}^{n}\Bigl(\sup_{x \in [x_{i-1}, x_i]} f(x) - \inf_{x \in [x_{i-1}, x_i]} f(x)\Bigr) \cdot (x_i - x_{i-1})\\ &= \sum_{i=1}^{n}(f(x_i) - f(x_{i-1})) \cdot (x_i - x_{i-1})\\ &= (-f(x_0) + f(n)) \cdot (x_i - x_{i-1})\\ &= (f(b) - f(a)) \cdot \Bigl(\frac{b - a}{n}\Bigr) \end{aligned}$$
[possible error: "$f(n)$" should be $f(x_n)$; the factor $(x_i - x_{i-1}) = \frac{b-a}{n}$ is constant, which is why the sum telescopes]
Choose $n \in \N$ such that $n > \frac{b - a}{\varepsilon} \cdot (f(b) - f(a))$. This implies $U(f, P) - L(f, P) < \varepsilon$. $\square$

## HW1071 56 · `20261121_225153.jpg` · [no header] 13.

**13.**

**Th.** Let $f : [a, b] \to \R$ be integrable. The function $F(x) = \int_a^x f(t) \dd t$, $F : [a, b] \to \R$ is continuous on $[a, b]$.

**P.** Let $c \in [a, b]$. Let $M$ be such that $\abs{f(x)} \le M$ for all $x \in [a, b]$. Fix $h > 0$. [the case $h < 0$ is not written]
$$F(c + h) - F(c) = \int_a^{c+h} f(x) \dd x - \int_a^c f(x) \dd x = \int_c^{c+h} f(x) \dd x$$
(a crossed-out symbol before the last integral.)
Since $\abs{f(x)} \le M$, $\int_c^{c+h} f(x) \dd x \le M(c + h - c) = Mh$.
Also, $-Mh \le \int_c^{c+h} f(x) \dd x$, so,
$$\abs{F(c + h) - F(c)} = \Bigl\lvert \int_c^{c+h} f(x) \dd x \Bigr\rvert \le Mh$$
Therefore, if $\varepsilon > 0$, $\abs{F(c + h) - F(c)} < \varepsilon$, provided $h < \frac{\varepsilon}{M}$.
Therefore $\lim_{h \to 0} F(c + h) = F(c)$. $\square$

## HW1071 57 · `20261121_225200.jpg` · [no header] 14.

**14. Mean value theorem for integrals**

**Th.** If $f : [a, b] \to \R$ is continuous, there exists $c \in [a, b]$ such that $\int_a^b f(x) \dd x = f(c) \cdot (b - a)$

**P.** If $f$ is constant, the result is trivial. Assume $f$ is not constant.
Let $m := \inf_{x \in [a, b]} f(x)$, $M := \sup_{x \in [a, b]} f(x)$. By the EVT, $\exists x_m, x_M \in [a, b]$ such that $m = f(x_m)$ and $M = f(x_M)$.
Without loss of generality, assume $x_m < x_M$.
$$m(b - a) \le \int_a^b f(x) \dd x \le M(b - a) \implies m \le \frac{\int_a^b f(x) \dd x}{b - a} \le M$$
By the IVT, for $f$ on $[x_m, x_M]$, there exists $c \in$ [crossed out] $[x_m, x_M]$ such that
$$f(c) = \frac{\int_a^b f(x) \dd x}{b - a} \implies \int_a^b f(x) \dd x = f(c) \cdot (b - a)$$
$\square$

## HW1071 58 · `20261121_225204.jpg` · [no header] 15.

**15. First fundamental theorem of calculus** (heading spelt "fundametal")

**Th.** Let $f : [a, b] \to \R$ be a continuous function, and define $F : [a, b] \to \R$, $F(x) = \int_a^x f(t) \dd t$. Then $F$ is differentiable on $[a, b]$ and $\frac{\dd}{\dd x}F(x) = f(x)$.

**P.** We will first show that $F$ is differentiable on $(a, b)$ and $F'(x) = f(x)$.
Fix $h > 0$.
$$F(x + h) - F(x) = \int_a^{x+h} f(t) \dd t - \int_a^x f(t) \dd t = \int_x^{x+h} f(t) \dd t$$
By the MVT for integrals, $\exists c \in [x, x + h]$ such that $\int_x^{x+h} f(t) \dd t = f(c) \cdot (x + h - x) = h \cdot f(c)$.
As $f$ is continuous on a closed and bounded interval, it is uniformly continuous on $[a, b]$. Therefore, $\forall \varepsilon > 0$, $\exists \delta > 0$ such that if $0 < \abs{x - y} < \delta$ then $\abs{f(x) - f(y)} < \varepsilon$.
If $h < \delta$, $x \le c \le x + h < x + \delta \implies \abs{c - x} < \delta \implies \abs{f(c) - f(x)} < \varepsilon$.
Thus,
$$\Bigl\lvert \frac{F(x + h) - F(x)}{h} - f(x) \Bigr\rvert = \Bigl\lvert \frac{h \cdot f(c)}{h} - f(x) \Bigr\rvert = \abs{f(c) - f(x)} < \varepsilon.$$
Therefore, $\lim_{h \to 0^+} \dfrac{F(x + h) - F(x)}{h} = f(x)$. $\square$
[possible error: only the right-hand limit ($h > 0$) is shown, and the endpoints $a$, $b$ announced in the statement are not treated]

## HW1071 59 · `20261121_225210.jpg` · [no header] 16.

**16. Second fundamental theorem of calculus**

**Th.** If $f$ is integrable on $[a, b]$, and $f = g'$, then $\int_a^b f(x) \dd x = g(b) - g(a)$

**P.** Let $P = \{a = x_0, \dots, x_n = b\}$ be a partition of $[a, b]$. By the MVT, $\exists c_i \in [x_{i-1}, x_i]$ such that
$$g(x_i) - g(x_{i-1}) = g'(c_i) \cdot (x_i - x_{i-1}) = f(c_i) \cdot (x_i - x_{i-1})$$
Define $m_i := \inf_{x \in [x_{i-1}, x_i]} f(x)$, $M_i := \sup_{x \in [x_{i-1}, x_i]} f(x)$.
Therefore,
$$m_i \le f(c_i) \le M_i$$
$$m_i(x_i - x_{i-1}) \le f(c_i) \cdot (x_i - x_{i-1}) \le M_i \cdot (x_i - x_{i-1})$$
$$m_i(x_i - x_{i-1}) \le g(x_i) - g(x_{i-1}) \le M_i(x_i - x_{i-1})$$
Hence,
$$\sum_{i=1}^{n} m_i(x_i - x_{i-1}) \le g(b) - g(a) \le \sum_{i=1}^{n} M_i(x_i - x_{i-1})$$
$$m_i(x_n - x_0) \le g(b) - g(a) \le M_i(x_n - x_0) \qquad \text{(margin: "optional (?)")}$$
$$L(f, P) \le g(b) - g(a) \le U(f, P)$$
[possible error: the "optional (?)" line is wrong ($m_i$, $M_i$ depend on $i$) and should be dropped; the previous line already is $L(f, P) \le g(b) - g(a) \le U(f, P)$]
Since this holds for any $P$, and $f$ is integrable, $g(b) - g(a) = \int_a^b f(x) \dd x$. $\square$

## HW1071 60 · `20261121_225213.jpg` · [no header] 17.

**17. Integration by parts**

**Th.** If $u, v : [a, b] \to \R$ are continuous on $[a, b]$ and differentiable on $(a, b)$, then
$$\int u \cdot v' \dd x = u \cdot v - \int u' \cdot v \dd x,\qquad \int_a^b u \cdot v' \dd x = u \cdot v \Big|_a^b - \int_a^b u' \cdot v \dd x$$

**P.**
$$\frac{\dd}{\dd x}(u \cdot v) = u \cdot \frac{\dd v}{\dd x} + v \cdot \frac{\dd u}{\dd x}$$
$$\int \frac{\dd}{\dd x}(u \cdot v) \dd x = \int u \frac{\dd v}{\dd x} \dd x + \int v \cdot \frac{\dd u}{\dd x} \dd x$$
$$u \cdot v = \int u \cdot v' \dd x + \int v \cdot u' \dd x \implies \int u \cdot v' \dd x = u \cdot v - \int u' \cdot v \dd x$$

## HW1071 61 · `20261121_225219.jpg` · [no header] 18.

**18. Integration by substitution**

**Th.** If $f, g$ are continuous on $[a, b]$, and $g$ is differentiable on $(a, b)$ with continuous $g'$, then
$$\int_{g(a)}^{g(b)} f(u) \dd u = \int_a^b f(g(x)) \cdot g'(x) \dd x$$

**P.** Suppose $F$ is an antiderivative of $f$. By the FTC,
$$\int_{g(a)}^{g(b)} f(u) \dd u = F(g(b)) - F(g(a))$$
By the chain rule, $(F \circ g)' = (F' \circ g) \cdot g' = (f \circ g) \cdot g'$.
Therefore, $(F \circ g)'$ is an antiderivative of $(f \circ g) \cdot g'$. [possible error: $F \circ g$ (not its derivative) is the antiderivative]
By the FTC,
$$\int_a^b (f \circ g)(x) \cdot g'(x) \dd x = (F \circ g)(b) - (F \circ g)(a) = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u) \dd u$$
$\square$
[possible error: $f$ needs to be continuous on the range of $g$ (an interval containing $g([a, b])$), not on $[a, b]$]

## HW1071 62 · `20261121_225226.jpg` · [no header] 19.

**19. Comparison criterion**

**Th.** Assume $0 \le a_n \le b_n$ for all $n \in \N$. If $\sum_{n=1}^{\infty} b_n$ converges, so does $\sum_{n=1}^{\infty} a_n$.

**P.** Let $S_k = \sum_{n=1}^{k} a_n$, $T_k = \sum_{n=1}^{k} b_n$.
$S_k = S_{k-1} + a_k \ge S_{k-1}$, $T_k = T_{k-1} + b_k \ge T_{k-1}$ $\implies$ both sequences monotone increasing.
$S_k \le T_k \le \lim_{k \to \infty} T_k$
Since $S_k$ and $T_k$ are monotone and bounded they must converge. Therefore $\sum_{n=1}^{\infty} a_n$ converges. $\square$

## HW1071 63 · `20261121_225234.jpg` · [no header] 20.

**20. The integral test**

**Th.** Let $f : [1, \infty) \to [0, \infty)$ be a non-negative, monotone decreasing continuous function. Then, the series $\sum_{n=1}^{\infty} f(n)$ converges iff the improper integral $\int_{[\cdot]}^{\infty} f(x)$ does so. [the lower limit is a dot or a small "1"; read as $\int_1^\infty f(x) \dd x$]

**P.** Consider the interval $[1, k + 1]$. $P = \{1, 2, 3, \dots, k + 1\}$ is a partition of $[1, k + 1]$.
Since $f$ is decreasing, $\inf_{x \in [x_{i-1}, x_i]} f(x) = f(x_i)$, $\sup_{x \in [x_{i-1}, x_i]} f(x) = f(x_{i-1})$
$$U(f, P) = \sum_{i=1}^{n} \sup_{x \in [x_{i-1}, x_i]} f(x)(x_i - x_{i-1}) = \sum_{i=1}^{n} f(x_{i-1})(1) = \sum_{i=1}^{n} f(i) = S_k$$
$$L(f, P) = \sum_{i=1}^{n} \inf_{x \in [x_{i-1}, x_i]} f(x) \cdot (x_i - x_{i-1}) = \sum_{i=1}^{n} f(x_i)(1) = \sum_{i=1}^{n} f(i + 1) = S_{k+1} - f(1)$$
[the upper summation limit is written $n$ but should be $k$; $S_k$ (the partial sums of $\sum f(n)$) is not defined on the page]
We know that $0 \le L(f, P) \le \int_1^{n+1} f(x) \dd x \le U(f, P)$
If $\int_1^\infty f(x)$ converges, $L(f, P) = \sum_{i=1}^{n} f(i + 1) = \sum_{i=2}^{n} f(i)$ by comp. Thus $\sum_{i=1}^{\infty} f(i)$ converges.
If $\int_1^\infty f(x)$ diverges, $U(f, P) = \sum_{i=1}^{n} f(i)$ diverges. $\square$

## HW1071 64 · `20261121_225241.jpg` · [no header] 21.

**21. Limit comparison test**

**Th.** Let $a_n, b_n > 0$, $\forall n \in \N$. If $\lim_{n \to \infty} \frac{a_n}{b_n} = c \in (0, \infty)$, then $\sum_{n=1}^{\infty} a_n$ converges iff $\sum_{n=1}^{\infty} b_n$ does so.

**P.** Assume $\sum_{n=1}^{\infty} b_n$ converges. Since $\lim_{n \to \infty} \frac{a_n}{b_n} = c$, $\forall \varepsilon > 0$, $\exists N \in \N$ such that for all $n \ge N$, $\bigl\lvert \frac{a_n}{b_n} - c \bigr\rvert < \varepsilon$.
Take $\varepsilon = c$. $\bigl\lvert \frac{a_n}{b_n} - c \bigr\rvert < c \implies \frac{a_n}{b_n} < 2c \implies a_n < 2c \cdot b_n$
Since $\sum_{n=1}^{\infty} b_n$ converges, $\sum_{n=N}^{\infty} b_n$ converges. Thus, since $\sum_{n=N}^{\infty} a_n < 2c \cdot \sum_{n=N}^{\infty} b_n$, $a_n$ converges by comparison.
Since they differ by a finite number of terms, $\sum_{n=1}^{\infty} a_n$ converges as well.
If $\sum_{n=1}^{\infty} a_n$ converges, $\lim_{n \to \infty} \frac{b_n}{a_n} = \frac1c > 0$, and $b_n$ converges by a similar argument. $\square$

## HW1071 65 · `20261121_225246.jpg` · [no header] 22.

**22. Ratio test**

**Th.** Let $a_n > 0$, $\forall n \in \N$. If $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} < 1$, then $\sum_{n=1}^{\infty} a_n$ converges. If $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} > 1$, then $\sum_{n=1}^{\infty} a_n$ diverges.

**P.** Assume $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = r \in \R_{\ge 0}$. $\forall \varepsilon > 0$, $\exists N \in \N$ such that $\forall n \ge N$, $\bigl\lvert \frac{a_{n+1}}{a_n} - r \bigr\rvert < \varepsilon$.

Case 1: $r < 1$. Choose $\varepsilon > 0$ such that $r + \varepsilon < 1$.
$$\Bigl\lvert \frac{a_{n+1}}{a_n} - r \Bigr\rvert < \varepsilon \implies \frac{a_{n+1}}{a_n} - r < \varepsilon \implies \frac{a_{n+1}}{a_n} < \varepsilon + r = s < 1$$
$\frac{a_{N+1}}{a_N} < s \implies a_{N+1} < s \cdot a_N$; $\frac{a_{N+2}}{a_{N+1}} < s \implies a_{N+2} < s \cdot a_{N+1} < s^2 \cdot a_N$
Therefore, $a_{N+k} < s^k \cdot a_N$
As $0 < s = r + \varepsilon < 1$, $\sum_{m=1}^{\infty} s^m$ converges. Therefore, $\sum_{n=1}^{\infty} a_N \cdot s^n$ converges. By comparison, $\sum_{n=N}^{\infty} a_n$ converges. Therefore, $\sum_{n=1}^{\infty} a_n$ converges.

Case 2: $r > 1$. $\exists N \in \N$ such that $\forall n \ge N$, $\frac{a_{n+1}}{a_n} > 1 \implies a_{n+1} > a_n$. Eventually $(a_n)_{n=1}^{\infty}$ will monotone increase. Therefore, $\lim_{n \to \infty} a_n \ne 0$, so $\sum_{n=1}^{\infty} a_n$ diverges. $\square$

## HW1071 66 · `20261121_225253.jpg` · [no header] 23.

**23. Leibniz test**

**Th.** Let $(a_n)_{n=1}^{\infty}$ be a sequence satisfying $a_n \ge 0$, $a_n \ge a_{n+1}$, $\forall n \ge 1$, $\lim_{n \to \infty} a_n = 0$. Then the alternating series $\sum_{n=1}^{\infty} (-1)^{n+1}a_n$ converges.

**P.** Let $S_n = \sum_{k=1}^{n} (-1)^{k+1}a_k$.
Observe $S_1 \ge S_3 \ge S_5 \ge \cdots$
$$S_{2n+3} = S_{2n+1} - a_{2n+2} + a_{2n+3} = S_{2n+1} + (a_{2n+3} - a_{2n+2}) \ge S_{2n+1}$$
since $a_{2n+3} - a_{2n+2} \ge 0$ by monotonicity.
$$S_{2n+2} = S_{2n} + (a_{2n+1} - a_{2n+2}) \le S_{2n}$$
since $a_{2n+1} - a_{2n+2} \ge 0$ by monotonicity.
[possible error: both inequalities point the wrong way. By monotonicity $a_{2n+3} - a_{2n+2} \le 0$, so $S_{2n+3} \le S_{2n+1}$ (as in "$S_1 \ge S_3 \ge \cdots$"), and $a_{2n+1} - a_{2n+2} \ge 0$ gives $S_{2n+2} \ge S_{2n}$ (as used in the next line)]
$$S_{2n+1} = S_{2n} + a_{2n+1} \ge S_{2n}$$
Therefore, $S_{2n} \le S_{2n+1} \le S_1$ and $S_{2n+1} \ge S_{2n} \ge S_2$. Hence $(S_{2n})_{n=1}^{\infty}$ and $(S_{2n+1})_{n=1}^{\infty}$ are bounded. Since they are both monotone, both sequences converge.
Let $\lim_{n \to \infty} S_{2n} = \alpha$, $\lim_{n \to \infty} S_{2n+1} = \beta$.
$$\beta - \alpha = \lim_{n \to \infty} S_{2n+1} - \lim_{n \to \infty} S_{2n} = \lim_{n \to \infty}(S_{2n+1} - S_{2n}) = \lim_{n \to \infty} a_{2n+1} = 0.$$
Thus $\alpha = \beta$, so $\sum_{n=1}^{\infty} (-1)^{n+1}a_n$ converges. $\square$
[the step from "both subsequences converge to the same limit" to "$S_n$ converges" is not written]
