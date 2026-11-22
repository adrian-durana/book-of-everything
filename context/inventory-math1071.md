# Coverage inventory: MATH1071, MATH2400 and MATH2401 (analysis group, filed as `math1071`)

_Built in the transcription phase from 66 photos of the MATH1071 handwritten notes, 102 photos of the MATH2400 handwritten notes, and three typed PDFs (MATH1071 130 pp., MATH2400 119 pp., MATH2401 66 pp.). Transcription: `claude/notes-math1071-1.md` (HW1071 01–66), `-2.md` (HW2400 001–051), `-3.md` (HW2400 052–102), `-4.md` (typed-notes index and all typed figures)._

**Sources.** "HW1071 nn" = MATH1071 photo nn; "HW2400 nnn" = MATH2400 photo nnn (file names in the notes docs). "CN1071 §x.y" = MATH1071 typed notes (printed page numbers; PDF page = printed + 6); "CN2400 §x / item n" = MATH2400 typed notes; "CN2401 Lnn" = MATH2401 typed notes, lecture nn. **Main source:** the handwritten notes, as requested; typed notes supplement them. **MATH2401** (the book's designated primary source for analysis) is represented **only** by its typed notes — there are no MATH2401 handwritten notes in this upload. All typed notes were written by other students (not lecturer notes).

**Code:** none in any of the sources. Part I uses Python, but nothing here needs code.

**Content rule:** source material only, with corrections. Section titles below are proposals; `tools/chapters.py` lists chapters only.

**Status:** ✅ written, ◻ to do. **↔ merge** = overlaps material already written (Ch 25–31) or another course's inventory. **(typed only)** = appears only in a typed PDF; the drafting chat needs the PDF.

**Big picture for the hub.**
1. **Duplicates within this group are heavy.** Most single-variable results appear two or three times (HW1071 44–66 proofs list, HW2400 001–068, CN1071 Ch 2–8, CN2401 L1–15). Use HW2400 as the base text for Ch 9–13 (it is the most complete handwritten version), HW1071 for the proofs it does better (noted below), and the typed notes for what the HW lacks.
2. **MATH1071's linear algebra (HW1071 01–43, CN1071 Ch 9–10)** goes to Ch 6, Ch 7 and Ch 8. `tools/chapters.py` lists Ch 8 *Vector Spaces and Inner Products* as MATH2001 only; MATH1071 contributes vector spaces, subspaces, span, independence, basis, dimension and coordinates, and MATH2400 contributes the Cauchy–Schwarz and triangle inequalities. Proposed: add MATH1071 (and MATH2400) to Ch 8.
3. **Metric spaces and topology (Ch 14) come only from CN2401**, which is informal lecture transcription (several statements need correcting, see the error list).
4. **The implicit function theorem** is typed only (CN2400 §7); the multivariable inverse function theorem is proved only in CN2401 L19–21 (via the contraction mapping theorem).
5. **Nothing for Ch 54** (*Interpolation, Numerical Differentiation and Quadrature*, listed with MATH1071) and **nothing numerical for Ch 53** (listed with MATH2400) was found in these sources. The closest items are the contraction mapping theorem (CN2401 L19, ↔ fixed-point iteration) and the $e$ approximation with an error bound (HW2400 083).

---

## Ch 6 Vectors, Matrices and Linear Systems (`ch:vectors-matrices-linear-systems`)

### 6.1 Linear systems and Gaussian elimination
- ◻ Motivation: linear algebra informally/formally; linearisation $\ell(x) = f(x_0) + f'(x_0)(x - x_0)$ as the reason to study linear functions (HW1071 01)
- ◻ Linear system of $m$ equations in $n$ unknowns; coefficient and augmented matrices (HW1071 02, CN1071 §9.1)
- ◻ Elementary row operations; row-echelon form; Gaussian elimination (HW1071 03, CN1071 Defs 9.1.3–9.1.4)
- ◻ Ex. $x + y + z = 3$, $x - y + z = 1$, $x + y - z = 1$: unique solution (HW1071 03)
- ◻ Ex. the same left side with right sides $(5, -9, 12)$: infinitely many solutions $\{(8 - \alpha, \alpha - 1, \alpha)\}$; with $(5, -9, 14)$: no solution (HW1071 04) — **keep one or two** (one-example rule)
- ◻ Rank; solvable iff rank of coefficient matrix = rank of augmented matrix; infinitely many solutions if rank < number of unknowns (consistency needed, see errors); the three examples revisited (HW1071 05, CN1071 Def 9.1.5)

### 6.2 Vectors and matrix–vector products
- ◻ $n$-dimensional vectors, row/column, addition, scalar multiplication; $\R^n$ (HW1071 05, CN1071 Defs 9.1.6, 9.1.9)
- ◻ Matrix applied to a column vector, $(Ax)_i = \sum_p A_{ip}x_p$; $Ax = b$ (HW1071 06, CN1071 Def 9.1.7)
- ◻ Homogeneous / inhomogeneous systems; kernel (null space) $\ker A = NS(A)$ (HW1071 06, CN1071 Defs 9.1.8, 9.1.10)
- ◻ Th. solution set of $Ax = b$ is $\{y + p : y \in \ker A\}$, proof by double inclusion (HW1071 07, CN1071 Prop 9.1.11)

### 6.3 Linear transformations
- ◻ $T_A(x) = Ax$; definition of a linear transformation (three conditions); visual remarks (lines stay straight, origin fixed) (HW1071 08)
- ◻ Th. $T$ linear $\iff T = T_A$ for some $m \times n$ matrix $A$, proof via $T(e_j)$ as columns; reverse direction "exercise" (HW1071 09)

### 6.4 Matrix multiplication
- ◻ Element-wise product (mentioned, "poor properties"); matrix product $C_{ij} = \sum_k A_{ik}B_{kj}$; $2 \times 2$ example showing $AB \ne BA$; dot-product remark (HW1071 10, CN1071 Def 9.2.1)
- ◻ Th. not commutative, associative (proof), distributive (HW1071 11, CN1071 Thm 9.2.2)
- ◻ Motivation: $T_{AB} = T_A \circ T_B$; **Figure F1071-1** (triangle $\R^p \to \R^n \to \R^m$) ↔ CN1071 **Fig 9.1** (same diagram; keep one) (HW1071 12–13)
- ◻ Ex. rotation by $90°$: $\R^2 = \C$, $i(x + iy) = -y + ix$; $A = \begin{pmatrix} 0 & -1\\ 1 & 0\end{pmatrix}$; $A^2$ = rotation by $180°$; **Figure F1071-2** (vectors before/after rotation) (HW1071 13–14)
- ◻ Identity matrix $I_n$; $AI_n = I_nA = A$ with matching dimensions (HW1071 14, CN1071 Def 9.2.3)
- ◻ Elementary matrices for the three row operations (sketches of the three matrices); left multiplication; Th. every rank-$n$ square matrix is a product of elementary matrices (stated) (HW1071 15, CN1071 Def 9.2.4, Cor 9.2.1)

### 6.5 Transpose and inverse
- ◻ Transpose, example (only first two rows legible), properties; proof of $(AB)\T = B\T A\T$; first two "easy exercises" (HW1071 16, CN1071 §9.3)
- ◻ Inverse; uniqueness (proof); not every matrix invertible (HW1071 17, CN1071 Def 9.3.3, Prop 9.3.4)
- ◻ $(A\T)^{-1} = (A^{-1})\T$ with proof; invertible iff reducible to $I_n$ / $\det \ne 0$ (remark); $(AB)^{-1} = B^{-1}A^{-1}$, $(A^{-1})^{-1} = A$ (stated) (HW1071 17, CN1071 Props 9.3.5–9.3.6, Thm 9.3.8)
- ◻ Method: finding $A^{-1}$ by solving $Ax_i = e_i$ simultaneously, $(A \mid I_n) \to (I_n \mid A^{-1})$ (HW1071 18–19)
- ◻ Ex. inverse of a $3 \times 3$ matrix, $A^{-1} = \frac{1}{41}(\dots)$ (checked correct; two slips in the working); Ex. inverse of $\begin{pmatrix} 1 & 1\\ 1 & -1\end{pmatrix}$ (HW1071 20) — keep one
- ◻ Th. for square $A$: invertible ⟺ right inverse ⟺ rank $n$ ⟺ $\ker A = \{0\}$, cyclic proof (HW1071 21–22, CN1071 Thm 9.3.7). The CN proof is tidier (uses Prop 9.3.5 left = right inverse).

### 6.6 Determinants
- ◻ Determinant as signed volume distortion; $2 \times 2$ and $3 \times 3$ formulas; recursive cofactor definition $\det A = \sum_j (-1)^{i+j}a_{ij}\det \hat A_{ij}$ (HW1071 23, CN1071 Def 9.4.1)
- ◻ Independence of the expansion row: used in HW but proved only in CN1071 Thm 9.4.3 with Lemma 9.4.1 **(typed only)**
- ◻ Diagonal matrix; zero row (stated) (HW1071 24, CN1071 Cor 9.4.1)
- ◻ Th. linearity in a row, with proof; $\det(A + B) \ne \det A + \det B$ (HW1071 24, CN1071 Thm 9.4.2)
- ◻ Th. two equal rows ⟹ $\det = 0$, by induction (HW1071 25, CN1071 Cor 9.4.2)
- ◻ Th. swapping rows changes sign, proof via the matrix with rows $a_r + a_s$; remark comparing $(x + y)^2$ (HW1071 26, CN1071 Thm 9.4.4)
- ◻ Th. $\det$ is the unique multilinear alternating function with $\det I_n = 1$ (stated); $\det A = \abs{A}$ notation (HW1071 27)
- ◻ Prop. elementary matrices invertible, inverses elementary (the three cases, (c) unfinished); their determinants non-zero (HW1071 27)
- ◻ Th. adding a multiple of a row leaves $\det$ unchanged, proof (HW1071 28, CN1071 Thm 9.4.5)
- ◻ Ex. $\det$ of a $3 \times 3$ matrix by row reduction $= 6$ (checked); triangular determinant = product of diagonal (left as an assignment) (HW1071 28, CN1071 remark p. 112)
- ◻ Th. rank $< n$ ⟹ $\det A = 0$ (stated in HW; proof CN1071 Cor 9.4.3) (HW1071 28)
- ◻ Th. $\det(AB) = \det A \det B$, two cases by rank (HW1071 29–30, CN1071 Thm 9.4.6); Cor $\det A^{-1} = 1/\det A$ (CN1071 Cor 9.4.4, typed only)
- ◻ Th. zero column ⟹ $\det = 0$, by induction (HW1071 31)
- ◻ Th. $\det A\T = \det A$, two cases (HW1071 32, CN1071 Thm 9.4.7)
- ◻ Th. $A$ invertible ⟺ $\det A \ne 0$ (HW1071 33, CN1071 Thm 9.4.8)
- ◻ Adjugate formula for $A^{-1}$ (CN1071 remark p. 114, typed only)

## Ch 7 Eigenvalues, Diagonalisation and Quadratic Forms (`ch:eigenvalues-diagonalisation`) — ↔ merge with MATH2001
- ◻ Eigenvector, eigenvalue ($x \in \C^n$, $x \ne 0$); direction preserved by $T_A$ (HW1071 34, CN1071 Def 9.5.1)
- ◻ Ex. diagonal matrix: eigenvalues $a_{ii}$, eigenvectors $e_i$; Ex. $\begin{pmatrix} 1 & 3\\ 4 & 2\end{pmatrix}$, eigenvalue $-2$, eigenvector $(-1, 1)$ (HW1071 34); CN1071 Ex 9.5.1 $\begin{pmatrix} -5 & 2\\ 2 & -2\end{pmatrix}$ — keep one
- ◻ Method: $\det(A - \lambda I) = 0$; characteristic polynomial $P_A(\lambda)$; eigenvectors from $(A - \lambda I)x = 0$ (HW1071 35)
- ◻ Eigenspace $\{v : Av = \lambda v\}$ is a subspace of $\C^n$ (proof); $\ker A$ is the eigenspace for $\lambda = 0$ (HW1071 39, CN1071 Prop 10.1.5, Cor 10.1.1) — or in Ch 8 next to subspaces
- Nothing on diagonalisation or quadratic forms in these sources (MATH2001 territory).

## Ch 8 Vector Spaces and Inner Products (`ch:vector-spaces-inner-products`) — add MATH1071 (and MATH2400) to this chapter; ↔ merge with MATH2001
### 8.1 Vector spaces
- ◻ Vector space over a field $\mathbb{F}$: eight axioms; vectors and scalars; no vector–vector product (HW1071 36, CN1071 Def 10.1.1)
- ◻ Uniqueness of $0$ and of $-u$ (stated); $u - v := u + (-v)$ (HW1071 36)
- ◻ Examples: $\R^n$, $\C^n$, $\{0\}$, $\R[x]$, $\R_n[x]$, $C([a, b])$, $M_{m \times n}(\mathbb{F})$, $\R$ over $\Q$; non-examples (positive orthant; a two-point set, made a space over $\{0, 1\}$) (HW1071 37)
### 8.2 Subspaces
- ◻ Subspace $W \le V$; test (non-empty, closed under $+$ and scalar multiplication) (HW1071 38, CN1071 Thm 10.1.4 with proof)
- ◻ Ex. lines/planes through the origin; Ex. $\{x + y = 2z\}$ (HW1071 38)
### 8.3 Span and linear independence
- ◻ Linear combination; span; span = intersection of subspaces containing $\Omega$ (stated); span is a subspace (stated; CN1071 Prop 10.2.3 "exercise") (HW1071 40)
- ◻ Ex. $\operatorname{span}\{1, x, x^2\} = \R_2[x]$; span of a disc in the $xy$-plane; $\operatorname{span}\{e_i\} = \R^n$ (HW1071 40, CN1071 Exs 10.2.1–10.2.3)
- ◻ Linear dependence (two formulations); remarks: $0 \in \Omega$ ⟹ dependent, two vectors dependent iff parallel, independence via the trivial solution (HW1071 41, CN1071 Def 10.2.4)
- ◻ Th. rows of $A$ independent ⟺ $\operatorname{rank} A = n$ (stated) (HW1071 41, CN1071 Prop 10.2.5)
### 8.4 Bases, dimension and coordinates
- ◻ Basis; examples ($\R^n$, $\R_n[x]$, the plane $a + b = c$, $\C$ over $\R$) (HW1071 42, CN1071 Def 10.3.1)
- ◻ Dimension; well-defined (stated); examples incl. $\dim_\R \C^n = 2n$, $\dim M_{m \times n} = mn$, $\dim \R[x] = \infty$ (HW1071 42, CN1071 Def 10.3.2)
- ◻ Th. unique coordinates $[v]_B$, proof (HW1071 43, CN1071 Thm 10.3.3)
- ◻ Th. $\dim V = n$ ⟹ $V \cong \R^n$ (stated) (HW1071 43)
### 8.5 Inner products and norms in $\R^n$
- ◻ Standard inner product and Euclidean norm on $\R^n$ (HW2400 087, CN2400 §4.1)
- ◻ Th. Cauchy–Schwarz $\abs{\inner{x, y}} \le \norm{x}\norm{y}$, proof via the discriminant (HW2400 087, CN2400 Thm 29) ↔ MATH2001
- ◻ Th. triangle inequality in $\R^n$, proof (HW2400 087, CN2400 Thm 30); ↔ CN1071 Fig 2.4 (vector triangle) — could illustrate it here
- ◻ Norms on vector spaces in general → Ch 14 (CN2401 L5)

## Ch 9 The Real Numbers, Sequences and Series (`ch:real-numbers-sequences-series`)
### 9.1 Constructing the number systems (typed only, CN2401)
- ◻ ZFC (informal list); Peano axioms with $\N = \{0, 1, 2, \dots\}$ (conflicts with the book's $\N$); recursive $+$ and $\cdot$; $(\N, +, 0)$ commutative monoid (CN2401 L1) ↔ MATH1061 Ch 3 (induction, WOP)
- ◻ $\Z$ as classes of pairs; ordered commutative ring; $\Q$ as classes of pairs; ordered field (CN2401 L1–2) ↔ MATH1061 Ch 2 (equivalence relations)
- ◻ $\R$ as Cauchy sequences of rationals modulo null sequences; field (sketch), trichotomy, order, ordered field (CN2401 L2–3)
- Decide whether this goes in Ch 9 or as an appendix to Ch 2/5 (it is the only construction in the sources; CN1071 says the construction of $\R$ "will not be covered").
### 9.2 Fields, order and completeness
- ◻ Number sets $\N \subset \Z \subset \Q \subset \R \subset \C$; $\R$ is a field, ordered, complete (HW2400 002, CN1071 §1.2)
- ◻ Field axioms and consequences $a \cdot 0 = 0$, uniqueness of $0$, no zero divisors, with proofs (CN1071 §1.4, typed only) ↔ MATH1061 Ch 5 (fields)
- ◻ Order properties list (HW2400 003)
- ◻ Absolute value and its properties; triangle inequality (proof); $n$-term version (proof unfinished in HW); reverse triangle inequality (stated) (HW2400 003–004, CN1071 Thm 2.2.5 two proofs, Thm 2.2.6; **Fig 2.4**)
- ◻ Upper/lower bounds, sup/inf; $\sup \emptyset = -\infty$, $\inf \emptyset = \infty$; sup need not be in the set; examples (HW2400 002, CN1071 §2.1; **Fig 2.1**)
- ◻ Least-upper-bound property (completeness); $\Q$ lacks it ($\{x^2 < 2\}$) (HW2400 002, CN1071 §2.1, CN2401 Thm 3.2 not proved)
- ◻ Prop. sup/inf unique; Th. ε-characterisation of sup, with proof (CN1071 Prop 2.1.3, Thm 2.1.4; **Fig 2.2**) (typed only)
### 9.3 Sequences and limits
- ◻ Sequence as a map $\N \to X$; limit; convergence (HW2400 001, 005, CN1071 Defs 2.2.1–2.2.4; **Fig 2.3**)
- ◻ Ex. $1/n \to 0$ (HW2400 005); Ex. $(n^2 + 1)/(n^2 + n) \to 1$ (HW2400 006); Ex. $(-1)^n$ diverges (HW2400 006, CN1071 Prop 3.2.4, **Fig 3.3**) — keep two
- ◻ Th. convergent ⟹ bounded (proof); bounded ⇏ convergent (HW2400 007, CN1071 Thm 2.2.9)
- ◻ Th. limits are unique (HW2400 007, CN1071 Thm 2.2.7; **Fig 2.5**)
- ◻ Th. limit laws: sum (proof), scalar, product, quotient (HW2400 008 proves sum only and cites "Lebl, Prop 2.2.5, or the 1071 notes"; CN1071 Thm 2.2.10 proves all) — use CN1071 for the proofs
- ◻ Prop. limits of rational functions of $n$ (CN1071 Prop 2.2.11); standard limits $\lambda^n$, $c^{1/n}$, $n^{1/n}$ (CN1071 Thm 2.2.12, "not proved in this course") (typed only)
- ◻ Th. squeeze theorem — **two proofs**: HW2400 009 (direct, short) and HW1071 44 (triangle-inequality version; HW2400 009 notes "a separate proof compared to MATH1071"); CN1071 Thm 2.2.8 (**Fig 2.6**). Use HW2400's; mention one only.
- ◻ Th. $\lim \abs{x_n} = \abs{\lim x_n}$ via the reverse triangle inequality (HW2400 009)
- ◻ Limits $\pm\infty$ (CN1071 Def 3.1.4, typed only)
### 9.4 Monotone sequences and subsequences
- ◻ Monotone sequences; Th. monotone: bounded ⟺ convergent, proof via sup (HW2400 010, CN1071 Thm 3.1.2; **Fig 3.1**)
- ◻ Bernoulli inequality; $(1 + 1/n)^n \to e$ (CN1071 Lemma 3.1.1, Thm 3.1.3, typed only) ↔ Ch 29 (Poisson limit uses $(1 - \lambda/n)^n \to e^{-\lambda}$, if it does)
- ◻ Subsequences; Th. subsequences of a convergent sequence converge to the same limit (HW2400 011, CN1071 Def 3.2.3; **Fig 3.2**)
- ◻ Cluster points of a sequence; three characterisations (HW2400 011 def only; CN1071 Def 3.2.5, Thm 3.2.6, **Fig 3.4**)
- ◻ Th. every sequence has a monotone subsequence, peak-point proof — **two versions**: HW1071 45 (strict peak) and HW2400 011 ($\ge$ peak); CN1071 Thm 3.3.4 (**Fig 3.6**). Use one (strict version avoids an error, see list).
- ◻ Th. Bolzano–Weierstrass (HW2400 012, CN1071 Thm 3.3.5; **Fig 3.7** is a joke figure, "should be a cartoon" — drop or redraw plainly)
### 9.5 Cauchy sequences and completeness
- ◻ Cauchy sequence; Ex. $1/n$ Cauchy; Ex. $(-1)^n$ not (HW2400 013, CN1071 Def 3.3.1; **Fig 3.5**)
- ◻ Th. Cauchy ⟹ bounded (HW2400 013, CN1071 Lemma 3.3.1)
- ◻ Th. Cauchy ⟺ convergent (both directions) (HW2400 014, CN1071 Thms 3.3.2, 3.3.6, CN2401 Thm 3.3)
### 9.6 Upper and lower limits
- ◻ limsup, liminf via $a_n = \sup_{k \ge n} x_k$; may be $\pm\infty$; existence for bounded sequences (proof); bounded converges ⟺ limsup = liminf (stated) (HW2400 015, CN1071 Def 3.2.1, Thm 3.2.2); examples (CN1071 Exs 3.2.1–3.2.2); limsup/liminf = largest/smallest cluster points (CN1071 remark)
### 9.7 Series
- ◻ Series, partial sums, convergence (HW2400 016, CN1071 §8.1); Achilles and the turtle (**Fig 8.1**, raster, drop)
- ◻ Cauchy criterion for series (HW2400 016, CN1071 Thm 8.2.2); linearity of series (CN1071 Thm 8.2.3)
- ◻ Th. $\sum x_n$ converges ⟹ $x_n \to 0$ — two proofs; contrapositive remark (HW2400 017, CN1071 Thm 8.2.1)
- ◻ Ex. harmonic series diverges ($S_{2^k} \ge 1 + k/2$) (HW2400 018)
- ◻ Geometric series (CN1071 Def 8.2.8, Prop 8.2.9, typed only)
- ◻ Non-negative series converge iff partial sums bounded (stated) (HW2400 019)
- ◻ Absolute and conditional convergence; absolute ⟹ convergent (proof); $\sum (-1)^n/n$ conditionally convergent (HW2400 019, CN1071 Def 8.2.12, Prop 8.2.13)
### 9.8 Convergence tests
- ◻ Comparison test — **two proofs**: HW2400 020 and HW1071 62 (CN1071 Thm 8.2.4)
- ◻ p-series test: divergent cases proved (HW2400 020; convergent cases blank); all cases CN1071 Thm 8.2.6 via Exs 8.2.3–8.2.6
- ◻ Limit comparison test with proof (HW1071 64, CN1071 Thm 8.2.7)
- ◻ Ratio test: statement (HW2400 021, proof blank); proof (HW1071 65, CN1071 Thm 8.2.10)
- ◻ Root test with limsup (stated, HW2400 022; not in CN1071)
- ◻ Alternating series (Leibniz) test: statement (HW2400 023, proof blank); proof (HW1071 66, contains an error; CN1071 Thm 8.2.11, **Fig 8.3**)
- ◻ Integral test → Ch 12 (it needs the integral)
### 9.9 Rearrangements
- ◻ Th. absolutely convergent series can be rearranged (stated, HW2400 024; proof CN2401 L8–9 Thm 8.1/9.1 i)
- ◻ Riemann rearrangement theorem: conditionally convergent series can be rearranged to any sum (remark, HW2400 024; proof CN2401 Thm 9.1 ii) (proof typed only)

## Ch 10 Continuity (`ch:continuity`)
### 10.1 Limits of functions
- ◻ Limit point (cluster point) of a set (CN1071 Def 4.1.1, **Fig 4.1**; HW2400 uses "cluster point" without defining it)
- ◻ ε–δ limit; remark $f$ need not be defined at $c$ (HW2400 001, 025, CN1071 Def 4.1.2, **Fig 4.2**)
- ◻ Ex. $\lim_{x \to 3}(x - 1)/2 = 1$; $\lim(mx + b)$; $\lim_{x \to 4} x^2 = 16$ with $\delta = \min\{1, \varepsilon/9\}$ (HW2400 025) — keep one or two
- ◻ Th. limits are unique (HW2400 026)
- ◻ Sequential characterisation of limits, both directions (HW2400 027–028, CN1071 Thm 4.1.10, **Fig 4.7**)
- ◻ Ex. $\sin(1/x)$ has no limit at 0 (two sequences) (HW2400 028); Ex. $x\sin(1/x) \to 0$ (HW2400 029, CN1071 §4.1)
- ◻ Limit laws for functions (HW1071 46–47 prove sum and product; CN1071 Thm 4.1.3)
- ◻ Th. $f \le g$ ⟹ $\lim f \le \lim g$; squeeze theorem for functions ("similar to sequences") (HW2400 029, CN1071 Thm 4.1.9)
- ◻ One-sided limits; equal one-sided limits ⟹ limit (CN1071 Def 4.1.7, Prop 4.1.8, **Fig 4.6**, typed only)
- ◻ Limits to and at infinity; rational functions at ∞ (CN1071 Defs 4.1.4–4.1.5, Prop 4.1.6, typed only)
- ◻ Figures on limits: **CN1071 Figs 4.3, 4.4, 4.5** (constant function, jump, $\delta$ depending on the point)
### 10.2 Continuity
- ◻ Continuity at a point (ε–δ and via limits), sequential continuity, continuity on a set (HW2400 001, 030, CN1071 Def 4.2.1, **Fig 4.8**)
- ◻ Ex. $\sin$ continuous via $\sin(c + \Delta x) - \sin c = 2\sin\frac{\Delta x}{2}\cos\frac{2c + \Delta x}{2}$ (HW2400 030)
- ◻ Ex. polynomials continuous (sequential proof) (HW2400 031, CN1071 Thm 4.2.2 remark)
- ◻ Sums, products, quotients, compositions continuous (HW2400 031 composition stated; CN1071 Thm 4.2.2)
- ◻ Lemma: continuous and positive at $x$ ⟹ positive nearby (CN2401 Lemma 4.1)
### 10.3 Continuous functions on closed intervals
- ◻ Th. continuous on $[a, b]$ ⟹ bounded (proof by Bolzano–Weierstrass) (HW2400 032)
- ◻ Th. EVT, proof via sup and Bolzano–Weierstrass (HW2400 033, CN1071 Thm 4.4.3, CN2401 Thm 5.1)
- ◻ Th. IVT, proof via $\sup\{x : f < 0 \text{ on } [a, x]\}$ (HW2400 034, CN2401 Thm 4.1; CN1071 Thm 4.4.1, **Fig 4.10**); Ex. $x^3 - 2x^2 + x - 1$ has a root in $(1, 2)$ (HW2400 035)
- ◻ Cor. continuous image of a closed interval is a closed interval (CN2401 Cor 5.1)
### 10.4 Uniform and Lipschitz continuity
- ◻ Uniform continuity; $\delta$ depends only on $\varepsilon$; global vs local; u.c. ⟹ continuous (HW2400 035, CN1071 Def 4.3.1, Prop 4.3.2)
- ◻ Th. continuous on $[a, b]$ ⟹ u.c. (stated HW2400 036; proof CN1071 Thm 4.3.3 with **Fig 4.9**, typed only)
- ◻ Ex. $x^2$ not u.c. on $\R$ (HW2400 036); Ex. $1/x$ u.c. on $(a, 1)$ (HW2400 037, $\delta$ needs correcting); Ex. $1/x$ not u.c. on $(0, 1)$ (HW2400 037) — keep two
- ◻ Lipschitz continuity; Lipschitz ⟹ u.c. (proof) (HW2400 038)
### 10.5 Monotone functions and inverses
- ◻ Lemma: continuous monotone $f$ maps intervals to intervals (proof via IVT) (HW2400 047, CN2400 Lemma 2)
- ◻ Lemma: strictly monotone $f$ is invertible on its range, $f^{-1}$ monotone and continuous (HW2400 048–049, CN2400 Lemma 3)
- ◻ Th. continuous + injective on an interval ⟹ strictly monotone, $f^{-1}$ continuous (CN1071 Thm 5.1.7, "proof left to MATH2401"; **Fig 5.4**)
- ◻ Injective function, inverse function (CN1071 Defs 5.1.5–5.1.6, **Fig 5.3**) ↔ MATH1061 Ch 2 (injective, inverse)

## Ch 11 Differentiation (`ch:differentiation`)
### 11.1 The derivative
- ◻ Derivative (two limit forms); differentiable on $I$; difference quotient $Q_{f,c}$ (HW2400 001, 039, CN1071 Def 5.1.1, **Fig 5.1**); tangent-line remark (CN1071)
- ◻ Ex. $x^2$ from first principles; Ex. $\abs{x}$ not differentiable at 0 (HW2400 039)
- ◻ Th. differentiable ⟹ continuous (HW1071 48, HW2400 040, CN1071 Prop 5.1.2) — identical proofs
- ◻ Linearity (HW2400 040; HW1071 48 sum rule); product rule (proof), quotient rule (stated) (HW2400 041, CN1071 Thm 5.1.3)
- ◻ Chain rule, proof with the auxiliary functions $u$, $v$ (HW2400 042, CN1071 Thm 5.1.4, **Fig 5.2**)
- ◻ Ex. $\frac{\dd}{\dd x}\sin x = \cos x$ via $\lim \frac{\sin x}{x} = 1$ (squeeze, no figure) and $\lim \frac{\cos x - 1}{x} = 0$ (HW2400 043)
- ◻ L'Hôpital's rule with examples (CN1071 Thm 5.1.9, typed only)
### 11.2 The inverse function theorem in one variable
- ◻ Lemma: $f'(x_0) = 0$ ⟹ $f^{-1}$ not differentiable at $f(x_0)$; Ex. $x^3$ (HW2400 047, CN2400 Lemma 1, Ex 1)
- ◻ Lemma: derivative of the inverse $(f^{-1})'(y) = 1/f'(f^{-1}(y))$, proof via $h(k)$ (HW2400 049–050, CN2400 Lemma 4)
- ◻ Th. inverse function theorem (1-D), proof from the lemmas (HW2400 050, CN2400 Thm 5; CN1071 Thm 5.1.8 different hypotheses)
- ◻ $\ln$, $\exp$ as an application → Ch 12 §12.7
### 11.3 Extrema and mean value theorems
- ◻ Local max/min (HW2400 044, CN1071 Def 5.2.1, **Fig 5.5**)
- ◻ Th. interior local extremum ⟹ $f'(c) = 0$ — **two proofs**: HW2400 044 (sequences) and HW1071 49 (one-sided limits); CN1071 Thm 5.2.2 with Lemma 5.2.1
- ◻ Rolle's theorem (HW2400 046, HW1071 50, CN1071 Thm 5.2.3, **Fig 5.6**) — identical proofs
- ◻ Mean value theorem (HW2400 045, HW1071 51, CN1071 Thm 5.2.4, **Fig 5.7**) — identical proofs
- ◻ Cauchy's mean value theorem (CN2401 Thm 15.2, typed only)
- ◻ Second derivative test, with Lemma 5.2.2 (CN1071 Thm 5.2.5, typed only)
### 11.4 Taylor's theorem
- ◻ $n$-th derivative; Taylor polynomial $P_{n,a}$ (HW2400 079, CN2400 Defs 17–19)
- ◻ Th. Taylor's theorem, integral form of the remainder, proof by induction and integration by parts (HW2400 079–080, CN2400 Thm 24)
- ◻ Th. Lagrange form of the remainder, proof via EVT/IVT (HW2400 082, CN2400 Lemma 26, CN2401 Thm 15.1)
- (Taylor series, analyticity → Ch 13)

## Ch 12 Integration (`ch:integration`)
### 12.1 Darboux sums and the integral
- ◻ Partition; lower and upper Darboux sums (HW2400 051, CN2400 Defs 1–2, CN1071 Defs 6.1.1–6.1.2) — **Figures**: CN1071 **Fig 6.1** and CN2400 p. 9 image (same idea; draw one)
- ◻ Lemma $m(b - a) \le L(f, P) \le U(f, P) \le M(b - a)$ (HW2400 051, CN2400 Lemma 6)
- ◻ Ex. step function on $[0, 4]$: $L(f, P_1)$, $U(f, P_1)$ and after refining (CN2400 Ex 2, typed only)
- ◻ Refinement; Lemma refining raises $L$, lowers $U$ (proof) (HW2400 052, CN2400 Lemma 7, CN1071 Lemma 6.1.1)
- ◻ Lower and upper integrals; $L(f, P_1) \le U(f, P_2)$; lower ≤ upper integral (proofs) (HW2400 053, CN2400 Lemmas 8–9)
- ◻ Integrable; Ex. constant function (HW2400 054, CN2400 Def 5, Ex 3)
### 12.2 Criteria for integrability
- ◻ Th. Riemann criterion $U - L < \varepsilon$, both directions (HW2400 055, HW1071 52, CN2400 Thm 10, CN1071 Thm 6.2.1) — use HW2400 (HW1071 has an algebra error)
- ◻ Ex. Dirichlet function not integrable (HW2400 056, CN2400 Ex 4)
- ◻ Ex. $f = 1, \frac12, 0$ on $[0, 2]$ integrable (CN2400 Ex 5, typed only)
- ◻ Th. bounded and continuous except at finitely many points ⟹ integrable: continuous case via uniform continuity, one discontinuity, $n$ discontinuities (HW2400 057–058, HW1071 53–54, CN2400 Thm 11, CN1071 Thm 6.2.2 with **Fig 6.2**)
- ◻ Th. monotone ⟹ integrable (HW2400 059, HW1071 55, CN2400 Thm 12, CN1071 Thm 6.2.3 with **Fig 6.3**)
### 12.3 Properties of the integral
- ◻ Th. linearity, monotonicity, additivity over intervals, restriction, $\abs{\int f} \le \int \abs{f}$; conventions $\int_a^a$, $\int_b^a$ (stated HW2400 060; CN1071 Thm 6.3.1 proves most, Lemma 6.3.1)
### 12.4 Fundamental theorem of calculus
- ◻ MVT for integrals (HW2400 061, HW1071 57, CN2400 Thm 14, CN1071 Thm 6.4.1 **Fig 6.4**)
- ◻ Th. $F(x) = \int_a^x f$ continuous for integrable $f$ (HW1071 56, CN1071 Thm 6.4.2 **Fig 6.5**)
- ◻ FTC part 1: $F' = f$ for continuous $f$ — **two proofs**: HW2400 061–062 ($c_h$ and squeeze, both signs of $h$) and HW1071 58 (uniform continuity, $h > 0$ only); CN2400 Thm 15, CN1071 Thm 6.4.3
- ◻ FTC part 2: $\int_a^b g' = g(b) - g(a)$ for integrable $g'$, via MVT on each subinterval (HW1071 59) — stronger than HW2400 063's "$G' = f$" remark; antiderivative (CN1071 Def 6.4.4, CN2400 Def 7)
- ◻ Ex. $\operatorname{sgn}$: $\int_{-1}^x \operatorname{sgn} = \abs{x} - 1$ not differentiable; integrating "upgrades" a function (HW2400 063, CN2400 Ex 6, CN1071 remark)
### 12.5 Techniques of integration
- ◻ Integration by parts (HW1071 60, HW2400 064, CN1071 Thm 7.1.3, CN2400 Thm 16)
- ◻ Substitution, proof via chain rule + FTC (HW1071 61, HW2400 064 stated, CN1071 Thm 7.1.4)
- ◻ Partial fractions (HW2400 064 refers to Lebl / 1071; CN1071 Def 7.1.5, Lemmas 7.1.1–7.1.2, examples) (typed only)
- ◻ Table of standard integrals; Weierstrass substitution with triangle figure (CN1071 Prop 7.1.2, Ex 7.1.11, p. 75 figure) (typed only)
- ◻ Areas between curves; Ex. $x^n$ vs $x^{n+1}$ with figure (CN1071 §7.2, typed only)
### 12.6 Improper integrals
- ◻ First kind (unbounded integrand at an endpoint) and second kind (infinite interval); $\int_{-\infty}^{\infty}$ as two limits, not a symmetric limit; Ex. $\int x \dd x$ (HW2400 065, CN2400 Defs 8–10, CN1071 Def 7.3.1 **Fig 7.1**)
- ◻ Ex. $\int_0^1 x^{-1/2} = 2$; $\int_0^1 x^p$ exists iff $p > -1$ (HW2400 066, CN2400 Exs 7–9)
- ◻ Th. integral test — **two proofs**: HW2400 067 and HW1071 63; CN2400 Thm 17, CN1071 Thm 8.2.5 (**Fig 8.2**; p. 84 counter-example figure when $f$ is not monotone)
### 12.7 The logarithm and exponential
- ◻ $\ln x = \int_1^x \frac{1}{t} \dd t$; Th. $\ln$ is a bijection $(0, \infty) \to \R$ (HW2400 068, CN2400 Def 11)
- ◻ $\exp$ as the inverse; $\exp' = \exp$ via the inverse function theorem (HW2400 068, CN2400 Def 12)
- ◻ $e^x$ defined by $f' = f$, $f(0) = 1$, uniqueness (CN2401 Def 14.1, Lemma 14.1, exercise) — alternative definition; keep one

## Ch 13 Sequences and Series of Functions (`ch:sequences-series-of-functions`)
### 13.1 Pointwise and uniform convergence
- ◻ Pointwise convergence; $N$ depends on $\varepsilon$ and $x$ (HW2400 069, CN2400 Def 13, CN2401 Def 10.1)
- ◻ Ex. $x^n$ on $[0, 1]$: pointwise limit discontinuous (HW2400 069) — **Figure**: CN2401 Fig 1 (graphs of $x$, $x^2$, $x^3$, $x^{100}$)
- ◻ Uniform convergence, notation $f_n \rightrightarrows f$; uniform ⟹ pointwise; "speed of convergence" remark (HW2400 069–070, CN2400 Def 14, CN2401 Def 10.2)
- ◻ Ex. $x^n$ not uniformly convergent on $[0, 1]$ ($x_n = (3/4)^{1/n}$), uniformly convergent on $[0, p]$, $p < 1$ (HW2400 071, CN2400 Exs 14–15)
- ◻ Ex. $\sin^n x$ not uniformly convergent; homework question (HW2400 072, CN2400 Ex 16)
- ◻ Prop. uniform convergence = convergence in the sup norm $\norm{\cdot}_\infty$ (CN2401 Prop 10.1, typed only) ↔ Ch 14 (norms)
- ◻ Examples: moving bump, delta-like triangular spikes (CN2401 L10–11, typed only); lists of sequences of functions (CN2400 Exs 10–12, no working; skip)
### 13.2 Uniform convergence and continuity, integrals, derivatives
- ◻ Th. uniform limit theorem (continuity), $\varepsilon/3$ proof (HW2400 070, CN2400 Thm 18, CN2401 Thm 10.1); interchange of limits remark (HW2400 072)
- ◻ Examples where limits cannot be interchanged: $n/(n + k)$; $\sin(nx)/\sqrt n$ (derivative); $n^2x(1 - x^2)^n$ (integral; $\int_0^1 = n^2/(2n + 2)$ checked) (HW2400 073, CN2400 Exs 17–19) — keep two
- ◻ Th. uniform convergence and integration (HW2400 074, CN2400 Thm 19, CN2401 Thm 11.1 — CN2401 also proves $f$ integrable)
- ◻ Th. differentiation under uniform convergence of $f_n'$ (HW2400 075, CN2400 Thm 20, CN2401 Thm 12.1)
- ◻ Uniformly Cauchy; Th. uniformly Cauchy ⟺ uniformly convergent (HW2400 076, CN2400 Def 15, Thm 21)
### 13.3 Series of functions
- ◻ Pointwise/uniform convergence of $\sum f_n$ (HW2400 077, CN2400 Def 16, CN2401 Def 12.1)
- ◻ Th. Weierstrass M-test (HW2400 077, CN2400 Thm 22, CN2401 Thm 12.4); Ex. $\sum \sin(nx)/n^2$ (CN2400 Ex 20, typed only)
- ◻ Th. term-by-term continuity, integration, differentiation (HW2400 078, CN2400 Thm 23, CN2401 Thms 12.2–12.3)
- ◻ Th. a continuous nowhere-differentiable function $\sum 10^{-n}\{10^n x\}$ (CN2401 Thm 12.5, typed only)
### 13.4 Power series
- ◻ Power series centred at $b$ (HW2400 085, CN2400 Def 22, CN2401 Def 13.1)
- ◻ Th. convergence at $x_0$ ⟹ uniform and absolute convergence on $[-a, a]$, $0 < a < \abs{x_0}$, and termwise differentiation (proof via M-test; derivative part sketched) (HW2400 085, CN2400 Thm 27, CN2401 Thm 13.2)
- ◻ Th. a power series converging on an open interval is its own Taylor series, $a_k = f^{(k)}(b)/k!$ (HW2400 086, CN2400 Thm 28)
- ◻ Radius of convergence (CN1071 Def 8.3.2, typed only)
- ◻ Power series form a ring $\R[[x]]$; inverse of $1 - x$; invertible iff $a_0 \ne 0$ (CN2401 Thm 13.1, Ex 13.1, typed only)
### 13.5 Taylor series and analytic functions
- ◻ Taylor series; Th. $P_{n,a}(x) \to f(x)$ ⟺ $R_{n,a}(x) \to 0$ (HW2400 079, 081, CN2400 Def 20, Lemma 25, CN1071 Def 8.3.1)
- ◻ Analytic at $a$ (HW2400 081, CN2400 Def 21)
- ◻ Maclaurin expansions of $\sin$, $\cos$, $\exp$ with Lagrange remainders; exercise: analytic at 0 (HW2400 083, CN2400 Ex 21, CN1071 §8.3)
- ◻ Ex. $e$ to within $5 \times 10^{-6}$ with $n = 9$ (checked) (HW2400 083, CN2400 Ex 22)
- ◻ Ex. $e$ is irrational (HW2400 084, CN2400 Ex 23, CN2401 Thm 15.3 with $e < 3$)
- ◻ Ex. Taylor series of $\ln x$ about 1; open question on its interval (HW2400 084, CN2400 Ex 24)
- ◻ Ex. $e^{-1/x^2}$ smooth but not analytic (CN2400 Ex 25, CN2401 L14 claim; typed only)

## Ch 14 Metric Spaces (`ch:metric-spaces`) — all from CN2401 (typed only)
### 14.1 Metrics and norms
- ◻ Metric; examples: Euclidean on $\R$, $\R^2$, $p$-adic, discrete, $2\abs{x - y}$; non-example $\abs{xy}$ (CN2401 Def 3.3)
- ◻ Convergence in a metric space; limit unique (exercise); discrete metric: convergent ⟺ eventually constant (exercise) (CN2401 Def 3.4, Exs 3.3–3.4)
- ◻ Norm; examples on $\R^n$ (Euclidean, taxicab) and function spaces; a norm defines a metric (CN2401 Def 5.1, Lemma 6.1)
- ◻ Th. all norms on $\R^n$ are equivalent ("proved later", not proved) (CN2401 Thm 15.4)
- ◻ Subspace metric (CN2401 L6)
### 14.2 Continuity
- ◻ Continuity between metric spaces; discrete metric example; sequential continuity; equivalence (proof) (CN2401 Defs 6.1–6.2, Prop)
- ◻ Open and closed balls (examples in $\R$, $\R^3$; taxicab ball in $\R^2$ — **figure p. 20**); neighbourhood; continuity via neighbourhoods (exercise) (CN2401 Defs 6.3–6.4) ↔ HW2400 088 (balls in $\R^n$)
### 14.3 Open and closed sets
- ◻ Open, closed; examples (intervals, $X$ and $\emptyset$, $[a, b)$, discrete metric) (CN2401 Def 7.1)
- ◻ Prop. closed ⟺ contains all limits of its sequences (proof) (CN2401 Prop 7.1)
- ◻ Relatively open sets (CN2401 Lemma 21.1)
### 14.4 Completeness and the contraction mapping theorem
- ◻ Complete metric space; $\Q$ not complete (CN2401 Def 19.2)
- ◻ Contraction; Lemma $\abs{f'} < c < 1$ ⟹ contraction (MVT); $\R^2$ version; examples with $x^2$ (CN2401 Def 19.1, Lemmas 19.1–19.2)
- ◻ Th. contraction mapping theorem (Banach fixed point), proof (CN2401 Thm 19.1) ↔ Ch 53 (fixed-point iteration, COSC2500)
### 14.5 Connectedness
- ◻ Connected metric space; examples ($\{0, 1\}$, $[1, 2) \cup (2, 3]$); connected subsets of $\R$ are intervals (exercise); continuous image of connected is connected (proof); IVT as a corollary (CN2401 Def 21.1, Thm 21.2, Cor 21.1)
### 14.6 Topological spaces and compactness
- ◻ Topology; continuity; continuous image of connected is connected (CN2401 Defs 21.2–21.3, Thm 21.3)
- ◻ Homeomorphism, diffeomorphism (CN2401 Def 20.1)
- ◻ Open cover, compactness; $(0, 1]$ not compact; finite intersection property; equivalences; continuous image of compact is compact; EVT as a corollary (CN2401 Defs 21.4–21.6, Thms 21.4–21.5, Cor 21.2)
- ◻ Compactness in metric spaces (incl. sequential compactness) with proof and examples (CN2401 Thm 22.1, L22)

## Ch 15 Differential Calculus in Several Variables (`ch:differential-calculus-several-variables`) — ↔ merge with MATH1072, MATH2001
### 15.1 Limits and continuity in $\R^n$
- ◻ Components $f = (f_1, \dots, f_m)\T$, $f_i = \inner{f, e_i}$ (HW2400 088, CN2400 Rem p. 77)
- ◻ Limit point of $\Omega \subseteq \R^n$; Exs limit points of $B_1(0)$ and $B_1(0) \setminus \{0\}$ (HW2400 088, CN2400 Def 23, Exs 27–28 typed only)
- ◻ Open and closed $r$-balls (HW2400 088, CN2400 Def 24) ↔ Ch 14
- ◻ Limit of $f : \Omega \to \R^m$; continuity (HW2400 088, CN2400 Defs 25–26; **CN2400 Fig 1**, $\delta$-disc and $\varepsilon$-interval); Exs for $(n, m) = (1,1), (2,1), (2,2)$ (CN2400 Exs 29–31, typed only)
- ◻ Th. uniqueness; limit laws (exercise); squeeze theorem (proof); componentwise limits, both directions (HW2400 088–090, CN2400 Thms 31–34)
- ◻ Ex. $xy/\sqrt{x^2 + y^2} \to 0$; Ex. $xy^2/(x^2 + y^2) \to 0$ (HW2400 090, CN2400 Exs 32–33); Ex. $(x^2 + xy)/(x^2 + y^2)$ has no limit (CN2400 Ex 34, typed only) — keep two
- ◻ Th. limit of a composition with a continuous function (HW2400 091, CN2400 Thm 35)
- ◻ Two-path rule (proof); Ex. $(xy + y^2 + zx)/(x^2 + y^2 + z^2)$ (HW2400 091–092, CN2400 Cor, Ex 35); Ex. $x^2/(y - x)$: limit 0 along every curve $y = mt^\alpha$ but no limit (CN2400 Ex 36, typed only); path-limit proposition (CN2401 Prop 16.1)
### 15.2 The derivative
- ◻ Lemma $\abs{T\vect h} \le M\abs{\vect h}$ for a matrix $T$ (HW2400 092, CN2400 Lemma 36)
- ◻ Open set; differentiability at $\vect a$ via a matrix $J$; $f'(\vect a) = Df(\vect a)$; differentiable on $\Omega$ (HW2400 093, CN2400 Defs 27–29, CN2401 Def 17.1)
- ◻ Ex. $f(\vect x) = B\vect x$ has $f' = B$ (HW2400 093, CN2400 Ex 37)
- ◻ Th. differentiable ⟹ continuous (HW2400 094, CN2400 Thm 37)
- ◻ Partial derivatives; Jacobian matrix $J_f$; Jacobian (determinant) (HW2400 095, CN2400 Defs 30–32, CN2401 Defs 17.2–17.3); Ex. Jacobian of $(x^2 + xy, x + y^3)$ (CN2400 Ex 38, typed only)
- ◻ Th. differentiable ⟹ partials exist and $f'(\vect a) = J_f(\vect a)$; $J$ unique (HW2400 095–096, CN2400 Thm 38)
- ◻ Ex. $xy/(x^2 + y^2)$: partials exist at 0 but not differentiable (HW2400 097, CN2400 Ex 39)
- ◻ Th. continuous partials ⟹ differentiable (stated in HW2400 097; proved in CN2401 Thm 17.1); $C^1$ (HW2400 097, CN2400 Def 33)
- ◻ Th. chain rule $(f \circ g)'(\vect a) = f'(g(\vect a))g'(\vect a)$; proof sketched in HW ("exercise"), complete in CN2400 Thm 40 (HW2400 098)
### 15.3 The inverse function theorem
- ◻ Lemma: $\det J_f(\vect x_0) = 0$ ⟹ $f^{-1}$ not differentiable at $f(\vect x_0)$ (HW2400 099, CN2400 Lemma 41)
- ◻ Th. inverse function theorem in $\R^n$ (two versions; derivative of the inverse is the inverse of the derivative) (HW2400 099–100, CN2400 Thms 42–43, CN2401 Thms 18.1, 20.1, 21.1)
- ◻ Proof via Lemma 20.1 and the contraction mapping theorem (CN2401 L20–21, typed only; HW2400 099 says "see 2401")
- ◻ Ex. $(e^x\cos y, e^x\sin y)$ locally but not globally invertible (HW2400 101, CN2400 Ex 40); Ex. $(x^2y + yx, 2xy + xy^2)$ near $(1, 1)$, $J_{f^{-1}}(2, 3) = \frac16\begin{pmatrix} 4 & -2\\ -3 & 3\end{pmatrix}$ (checked) (HW2400 102, CN2400 Ex 41)
### 15.4 The implicit function theorem (typed only)
- ◻ Stacked vectors $(\vect h, \vect k)$, maps $\pi_1$, $\pi_2$ (CN2400 Defs 34–35)
- ◻ Ex. the circle $x^2 + y^2 = 1$ (CN2400 Ex 42)
- ◻ Th. implicit function theorem with block matrices $A_x$, $A_y$; proof via the IFT, Claims 1–3 (CN2400 Thm 44)
- ◻ Ex. the system $x^2 + y^2 - (z + 1)^3 = -1$, $e^x + e^y + e^z = 3$ near 0 (CN2400 Ex 43)

## Ch 53 Floating-Point Arithmetic, Error and Root-Finding (`ch:floating-point-root-finding`)
- Nothing numerical found in the MATH2400 sources. Cross-reference candidates only: contraction mapping theorem (CN2401 Thm 19.1, placed in Ch 14) ↔ fixed-point iteration; Lagrange remainder error bound for $e$ (HW2400 083, placed in Ch 13). Ask the hub whether MATH2400 should stay listed for Ch 53.

## Ch 54 Interpolation, Numerical Differentiation and Quadrature (`ch:interpolation-quadrature`)
- Nothing found in the MATH1071 sources (no numerical methods in either the notebook or CN1071). Ask the hub whether MATH1071 should stay listed for Ch 54.

## Part III (Ch 25–32): ↔ merge notes
No item in these courses belongs in Part III, but several Part III chapters already use results whose home is now Ch 6–15:
- Ch 25 (countable unions, sets) ↔ Ch 9/Ch 2: nothing new.
- Ch 27–29 use integrals, improper integrals, series and the exponential: their proofs live in Ch 9 (series), Ch 12 (improper integrals, $\ln$, $\exp$). Ch 29's Poisson limit and normal/gamma calculations rely on $(1 + x/n)^n \to e^x$ (CN1071 Thm 3.1.3 has the $x = 1$ case only) and improper integrals (Ch 12 §12.6).
- Ch 28 (PGFs, MGFs) uses power series and termwise differentiation ↔ Ch 13 §13.4 (radius of convergence, CN1071 Def 8.3.2).
- Ch 30 (covariance matrix, $\Cov(AX) = A\Cov(X)A\T$) uses $(AB)\T = B\T A\T$ ↔ Ch 6 §6.5.
- Ch 32 (Jacobian transformations, not yet written) uses the Jacobian determinant ↔ Ch 15 §15.2.
These are linking-phase cross-references, not merges of text.

## Other courses
- ↔ **MATH1061** (`claude/inventory-math1061.md`): fields (its Ch 5 cites "(1071)" for field axioms and $\Z_p$ a field) ↔ CN1071 §1.4; sets, functions, injective/surjective/inverse ↔ CN1071 §1.1, Defs 5.1.5–5.1.6; equivalence relations ↔ CN2401 L1–2 constructions; induction/WOP ↔ Peano axioms (CN2401 L1); rationals, density, sequences, arithmetic/geometric sequences ↔ Ch 9; matrix notation $M_{m \times n}$ ↔ HW1071 37 uses $M_{m \times n}(\mathbb{F})$; countability and Cantor — **not** covered in these analysis sources (MATH1061 keeps it).
- ↔ **MATH2001** (analysis/linear algebra II): Ch 7 (eigenvalues → diagonalisation), Ch 8 (vector spaces, inner products, Cauchy–Schwarz), Ch 15–16.
- ↔ **MATH1072**: Ch 15 (partial derivatives, Jacobian, chain rule) — expect duplicates at a computational level.
- ↔ **COSC2500**: Ch 53 fixed-point iteration ↔ contraction mapping theorem.
- ↔ **MATH2100/MATH2010** (`notes-math2100-*`): if the ODE notes use Picard iteration or the contraction mapping theorem, Ch 14 §14.4 is its home.

## Not used yet
- Course administration in CN2401 (quiz details, L5.1 and L16.1) and CN1071 (preface, changelog, "Roses are red" remark); lecturer anecdotes; references to Spivak's drawing (CN2400 Ex 1) and to a maths website (CN1071 p. 112).
- HW2400 blank proof slots (p-series cases 5–6, ratio, root and alternating series tests) and homework prompts (HW2400 072, 084).
- Crossed-out text throughout (noted inline in the transcription).

## Suspected errors in the notes
Flagged inline in the transcription as `[possible error: …]`. None are applied yet. Grouped by source; minor variable-name slips are listed only where they change meaning.

**HW1071 (linear algebra, 01–43)**
1. HW1071 03: the method says "until in RRE form" but the example stops at row-echelon form with leading 1s.
2. HW1071 04: row label $R_1 + R_2$ should be $R_2 + R_1$; the reduced matrix has $(1,3)$ entry $2$ for $-2$ (repeated in HW1071 05).
3. HW1071 05: "rank < number of unknowns ⟹ infinitely many solutions" needs the system to be consistent (the third example is a counterexample).
4. HW1071 06: $b$ has $m$ entries, not $n$. HW1071 08: outputs of $T : \R^n \to \R^m$ lie in $\R^m$. HW1071 09: index range $1 \le i \le m$.
5. HW1071 13: the argument that $T_A \circ T_B$ is given by $AB$ uses associativity of the product, so it is circular (the notes add "?").
6. HW1071 15: the $\lambda$ for "add $\lambda$ × row $i$ to row $j$" goes in position $(j, i)$, not $(i, j)$.
7. HW1071 17: inverses defined for $m \times n$ matrices (should be square); in the $(A\T)^{-1}$ proof both lines start from $(AA^{-1})\T$.
8. HW1071 18: $Ax_i = e_i$, the $i$th **column** of $I_n$.
9. HW1071 20: in the $3 \times 3$ inverse, one row-operation label is wrong ($R_3 - 5R_2$) and one entry is $-\frac{13}{41}$ for $-\frac{12}{41}$; the final answer is correct.
10. HW1071 21–22: step 3 doesn't construct the right inverse until HW1071 22; in step 4 $B$ is a matrix (not in $\R^n$), and $A = B$ follows from $A = A(CB) = (AC)B = B$, not from uniqueness of the inverse.
11. HW1071 23: area preserved iff $\abs{ad - bc} = 1$; the definition writes "$A \in \R^n$" for an $n \times n$ matrix; independence of the expansion row is assumed (proved in CN1071 Thm 9.4.3).
12. HW1071 25: the matrix is called $B$ then $A$. HW1071 26: "$m \times n$" should be $n \times n$.
13. HW1071 29: "If rank $A > n$, no inverse, no determinant" should read rank $A < n$ ⟹ no inverse and $\det A = 0$.
14. HW1071 31: "expand by the first row" but the formula keeps a general $i$.
15. HW1071 33: the first part proves "invertible ⟹ $\det A \ne 0$" but concludes the converse.
16. HW1071 36: scalar multiplication written $V \times V \to V$ (should be $\mathbb{F} \times V \to V$). HW1071 37: the field for $C([a, b])$ is $\R$, not "$\R \cap [a, b]$".
17. HW1071 38: subspace test written "$\forall u, v \in \mathbb{F}$" (should be $W$). HW1071 39: concludes $W \le V$ (should be $\C^n$).

**HW1071 (proof list, 44–66)**
18. HW1071 44: "Def." for a theorem; "$n \ge N$" vs $n > N_i$.
19. HW1071 45: "not a peak point" gives $a_{n_2} \ge a_{n_1}$, not $>$ (the subsequence is still monotone); the no-peak case is not mentioned.
20. HW1071 46: final "$< \varepsilon$" should be "$= \varepsilon$". HW1071 47: limit renamed $L_2$; $\varepsilon'$ not fixed; divides by $\ell$ (needs $\abs{\ell}$ and $\ell \ne 0$).
21. HW1071 49: the δ-neighbourhood sentence is garbled; the one-sided limits are claimed to be 0 instead of $\le 0$ and $\ge 0$.
22. HW1071 50: "$f(x_0) < f(a)$" should be $f(x_1) < f(a)$; only one case written.
23. HW1071 52: sign error, the bound evaluates to $0$ as written (should be $\varepsilon$).
24. HW1071 54: endpoint discontinuity not covered; "$=$" vs "$<$" slips.
25. HW1071 55: theorem stated backwards ("integrable ⟹ monotone"); "$f(n)$" for $f(x_n)$.
26. HW1071 58: FTC proof covers $h > 0$ only and not the endpoints.
27. HW1071 59: the "optional (?)" line with $m_i(x_n - x_0)$ is wrong (drop it).
28. HW1071 61: "$(F \circ g)'$ is an antiderivative" should be $F \circ g$; $f$ must be continuous on the range of $g$.
29. HW1071 63: summation limit $n$ for $k$; $S_k$ undefined.
30. HW1071 66: in the Leibniz test proof both monotonicity inequalities point the wrong way (the next lines use the right ones); the final step from the two subsequences to $S_n$ is not written.

**HW2400 (001–068)**
31. HW2400 001, 030: $c$ and $a$ mixed in the definitions of limit and continuity; "cluster point" used without definition.
32. HW2400 002: the least-upper-bound property needs $S$ non-empty and bounded above.
33. HW2400 003: order properties attributed to the field axioms (they need the order axioms).
34. HW2400 004: the $n$-term triangle inequality proof stops after the inductive hypothesis.
35. HW2400 005: sequence written as a map $X \leftarrow \N$.
36. HW2400 007: notation switches mid-proof ($x_n, x, M$ → $a_n, L, N$).
37. HW2400 008: quotient law needs $\lim b_n \ne 0$.
38. HW2400 011: subsequence proof has a spurious middle term; monotone-subsequence proof writes $k_1$ for $n_1$ and uses $\ge$-peaks (so "not a peak" gives strict $>$; fine) — compare HW1071 45.
39. HW2400 013: $M = \ceil{2/\varepsilon}$ with $k, l \ge M$ gives $\le \varepsilon$, not $<$.
40. HW2400 015: "$a_{n+1} \le a_n \iff$ inclusion" should be "⟸".
41. HW2400 018: inner summation limit $2i$ for $2^i$.
42. HW2400 021: hypothesis $x_n > 0$ with absolute values (presumably $x_n \ne 0$).
43. HW2400 025: $\lim(mx + b)$ needs $m \ne 0$; argument written backwards.
44. HW2400 027–028: sequential definition needs $x_n \in S \setminus \{c\}$; the negation of the ε–δ statement is mis-stated (needs "∃x").
45. HW2400 028: the second $\sin(1/x)$ argument wrongly concludes "the limit exists" before the contradiction.
46. HW2400 029: comparison theorem writes $\lim f = L_2$ for $\lim g$, and a sequence converging to $L$ for $c$.
47. HW2400 030: $\abs{\sin x} \le x$ should be $\le \abs{x}$.
48. HW2400 031: composition theorem omits "continuous".
49. HW2400 032: "continuous on $\R$ ⟹ bounded" is false; needs $[a, b]$. "bounded" for "unbounded"; "not continuous at $x$" for "at $L$".
50. HW2400 034: IVT proof concludes "$f(\alpha) < 0$" (should be $= 0$); the general case should use $f(x) - c$.
51. HW2400 037: $\delta = \frac{1}{a^2}\varepsilon$ should be $a^2\varepsilon$ (the displayed chain does not give $< \varepsilon$).
52. HW2400 038: "$<$" for "$\le$"; needs $K > 0$.
53. HW2400 043: $\sin(x + h)$ expanded with a minus sign (sign slip).
54. HW2400 044: Fermat's theorem stated for $c \in [a, b]$; needs $c \in (a, b)$.
55. HW2400 047: "If $f$ were differentiable" should be "$f^{-1}$"; second display should read $(f^{-1})'(f(x_0)) \cdot 0 = 1$.
56. HW2400 048: "monotone" should be "strictly monotone" (and continuous for $f^{-1}$ continuous); "$x_0 < b$" for "$x_0 + \varepsilon < b$"; "$\in I$" for "$\subseteq I$".
57. HW2400 049: "Since the inverse is monotone, $h(k) = 0$" should be "since $f^{-1}$ is continuous, $h(k) \to 0$" (and $h(k) \ne 0$).
58. HW2400 050: "$f'(x_0) \ge 0$" should be "$> 0$".
59. HW2400 052: missing factor $(x_j - x_{j-1})$.
60. HW2400 055: "$> U(f, P_2) + \frac{\varepsilon}{2}$" should be "$- \frac{\varepsilon}{2}$".
61. HW2400 057: theorem omits "bounded" (the proof uses it). HW2400 058: "$<$" vs "$\le$" slips; $c$ must be interior.
62. HW2400 060: item (7) is a convention, not a property.
63. HW2400 061: MVT for integrals: IVT gives $c$ between $x_m$ and $x_M$, so $c \in [a, b]$, not $(a, b)$.
64. HW2400 062: FTC claims $F' = f$ on $[a, b]$ but proves it on $(a, b)$.
65. HW2400 063: $G(b) - G(a)$ computed with $G(b) - c$ for $F(b) + c$; "derivative 0 ⟹ constant" used without proof.
66. HW2400 064: substitution hypotheses as in HW1071 61.
67. HW2400 066: "If $p = 1$, the integral must diverge" should be $p = -1$.
68. HW2400 068: "$\ln(c^{-1}) = -\ln c = M$" should be $-M$; in $\exp' = \exp$ the denominator $(\ln(\exp y))'$ should be $\ln'(\exp y)$.

**HW2400 (069–102)**
69. HW2400 070: "pointwise and uniform continuity" should be "convergence"; "Let $\Omega \to \R$" for $\Omega \subseteq \R$.
70. HW2400 071: $N = \floor{\ln\varepsilon/\ln p} + 1$ needs $0 < p < 1$.
71. HW2400 072: "$m \in \N$" should be $m \in \Z$; "continuous" for "convergent".
72. HW2400 078: the termwise-differentiation theorem assumes its conclusion (calls the limit $f'$).
73. HW2400 079: integral-form Taylor needs $f^{(n+1)}$ integrable; "$m \in M$" for $m \in \N$.
74. HW2400 080: the cancellation of the boundary term is not shown.
75. HW2400 081: forward direction writes $\lim P_{n,a}$ twice.
76. HW2400 082: Lagrange remainder: IVT gives $z \in [a, x]$; the case $x < a$ is not covered by "WLOG" for odd $n$.
77. HW2400 083: "$\exp(1) = \sum_{k=0}^{\infty}$" should be the finite sum plus remainder; "$0 < t < 1$" for $0 < z < 1$.
78. HW2400 084: "$(n - 1)^k$" for $(x - 1)^k$ in the $\ln$ series.
79. HW2400 085: "$\forall n\ \exists M$" for "$\exists M\ \forall n$"; derivative part only sketched.
80. HW2400 087: Cauchy–Schwarz written with $\norm{\cdot}$ on the scalar $\inner{x, y}$ (means $\abs{\cdot}$).
81. HW2400 088: limit written $\lim_{\vect x \to \vect x_0} f(\vect x_0)$; the "equivalent statement" remark is the definition of continuity, not of the limit.
82. HW2400 089: squeeze theorem must assume equal limits of $f$ and $h$; strict/non-strict slip; componentwise sum to $n$ for $m$.
83. HW2400 090: $m\varepsilon^2(1/\sqrt m)^2 = \varepsilon^2$, not $\varepsilon$.
84. HW2400 092: in the bound for $\abs{T\vect h}$ the sum is misplaced, $K = \max\norm{T(\vect e_i)}$, last line should read $\norm{T\vect h} \le M\norm{\vect h}$.
85. HW2400 094: sign slip $+J\vect h$ for $-J\vect h$; "$<$" for "$\le$".
86. HW2400 096: the squeeze step needs absolute values; the factor $\abs{t}/t$ is dropped in the limit line.
87. HW2400 097: $f_x(0, 0)$ computed with $f(0, h)$ (should be $f(h, 0)$; same value).
88. HW2400 098: $F = f \circ g$ not defined; second limit variable.
89. HW2400 099: IFT hypothesis "continuously differentiable at $\vect x_0$" should be "near $\vect x_0$" (HW2400 100 restates it correctly); the lemma needs $f$ injective.
90. HW2400 102: "$\abs{J_f(\vect x)} = 6$" means $\abs{J_f(1, 1)}$; "$f$ is invertible on an open set containing $(2, 3)$" means $f^{-1}$ is defined there.

**Typed notes**
91. CN1071 Thm 5.1.4 (chain rule): codomain written $R$ for $\R$. CN1071 Fig 4.3 (right panel) shows a function without limit $l$ at $a$ without saying so.
92. CN2401 Def 1.1: $\N = \{0, 1, 2, \dots\}$, against the book's $\N = \{1, 2, \dots\}$ — convert.
93. CN2401 p. 20: the taxicab unit ball is a square rotated by $\pi/4$ (not $\pi/2$).
94. CN2401 Def 10.2: "$x > N$" should be "$n > N$".
95. CN2401 Thm 13.2: "$0 < a < x_0$" should be $0 < a < \abs{x_0}$.
96. CN2401 Thm 15.2 (Cauchy MVT): $g'(x)$, $f'(x)$ should be $g'(c)$, $f'(c)$.
97. CN2401 Def 17.1: "$x_0 \in \R^m$" should be $\R^n$.
98. CN2401 Def 19.1: contraction written $\norm{f(x) - f(y)} < \abs{x - y}$; the constant $c$ is missing ($\le c\norm{x - y}$).
99. CN2401 Def 21.4: a cover written with $\bigcap$ (should be $\bigcup$); also in Def 21.5.
100. CN2401 Thm 3.2: least-upper-bound property called "Cauchy complete".

## Notation the book doesn't have yet
To go through `NOTATION_REQUESTS.md` in the hub chat.

| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\F` | $\mathbb{F}$ | a general field | Vector spaces over $\mathbb{F}$ (HW1071 36–43, CN1071 Ch 10). |
| `\Mat{m}{n}{\F}` | $M_{m \times n}(\mathbb{F})$ | $m \times n$ matrices over $\mathbb{F}$ | HW1071 37, HW2400 092; MATH1061 inventory proposed the same macro — one decision for both. |
| (convention) `\ker` (built-in) | $\ker A$ | null space | Notes use both $NS(A)$ and $\ker A$ (HW1071 06); CN1071 uses $\mathrm{NS}(A)$. Pick one. |
| `\Id` or `\mat{I}_n` (convention) | $I_n$ | identity matrix | HW1071 14; bold by the book's matrix rule. |
| `\coord{v}{B}` | $[v]_B$ | coordinates w.r.t. a basis | HW1071 43. |
| (convention) `\R[x]`, `\R_n[x]` | | polynomials, of degree $\le n$ | HW1071 37, 40, 42. |
| `\sgn` | $\operatorname{sgn}$ | sign function | HW2400 063, CN2400 Ex 6. |
| `\uconv` | $\rightrightarrows$ | uniform convergence | HW2400 070–076. |
| `\Lsum`, `\Usum` | $L(f, P)$, $U(f, P)$ | lower and upper Darboux sums | HW2400 051–059 (italic), CN1071 (upright L, U). |
| `\lowint`, `\upint` | $\underline{\int_a^b}$, $\overline{\int_a^b}$ | lower and upper integrals | HW1071 52, HW2400 053–055 (also written $\mathbb{L}$, $\mathbb{U}$). |
| `\ball{r}{x}`, `\cball{r}{x}` | $B_r(x)$, $\overline{B}_r(x)$ | open and closed balls | HW2400 088, CN2401 Def 6.3. |
| `\Jac{f}` | $J_f$ | Jacobian matrix | HW2400 095–102; also $\det J_f$ for the Jacobian. Ch 32 (transformations) will need it too. |
| `\D` | $\mathrm{D}f(\vect a)$ | total derivative | HW2400 093 ($f'(\vect a) \equiv Df(\vect a)$). |
| `\pdv{f}{x}` | $\dfrac{\partial f}{\partial x}$ | partial derivative | HW2400 095–102; MATH1072/2001 will need it. |
| (convention) $C^1$, $C^k$, $C^\infty$ | | continuously differentiable classes | HW2400 097, CN2401. |
| `\restr{f}{U}` | $f\vert_U$ | restriction | HW2400 050, 099. |
| `\dist` or (convention) $d(x, y)$ | | metric | CN2401 (Ch 14). |
| (convention) $\limsup$, $\liminf$ (built-in) | | upper/lower limits | HW2400 015, 022. |
| (convention) $e$ vs $\exp$ | | exponential | HW2400 068 defines $\exp$ and writes $e^z$. |
| (convention) $\N$ | | naturals | CN2401 uses $\{0, 1, \dots\}$; book uses $\{1, 2, \dots\}$. |

## Code in the notes
None (no code in any of the five sources).

## Questions for the hub
1. **Typed PDFs for drafting.** Much of Ch 14, §15.4, and many proofs are typed only. The PDFs were uploaded to this chat but are not in the project; the drafting chat will need them re-uploaded (CN1071, CN2400, CN2401).
2. **Chapter lists.** Add MATH1071 (and MATH2400, for Cauchy–Schwarz) to Ch 8; confirm whether MATH2400 stays on Ch 53 and MATH1071 on Ch 54 (no material found for either).
3. **Construction of the number systems** (CN2401 L1–3, typed only): a section of Ch 9, or an appendix/section in Ch 2 or Ch 5 next to MATH1061's equivalence relations and fields?
4. **Duplicate proofs.** Several results have two or three different proofs (squeeze theorem, monotone subsequence, comparison test, FTC part 1, Fermat's theorem, IFT). The inventory suggests one per result; confirm the "one proof" policy for duplicates across courses.
5. **CN1071 Fig 3.7 and Fig 8.1** are a joke figure and a raster sketch with no maths. Drop them?
