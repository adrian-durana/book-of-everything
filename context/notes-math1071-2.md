# MATH1071 / MATH2400 / MATH2401 — transcription, part 2: MATH2400 handwritten notes (HW2400 001–051)

_Continues `claude/notes-math1071-1.md` (read its header for conventions). Part 3 has HW2400 052–102; part 4 the typed notes._

**Source.** `math2400.zip`: 102 photos, one notebook page per photo, in shooting order (every photo is duplicated in a `math2400/` subfolder; copies identical, counted once). "HW2400 nnn" = photo nnn. Each page has a topic title, used as the heading. The notebook is a fair copy: Def./P./Ex./Rem./L. labels, with many theorems labelled "Def."; marked [a theorem] where it matters. Vectors are underlined in the notes ($\underline{x}$) and transcribed with `\vect`.

**Structure.** HW2400 001–046 revise single-variable analysis (real numbers, sequences, series, limits, continuity, derivatives; the notes cite "Lebl" and "the 1071 Ducky notes"); from HW2400 047 the notebook follows the MATH2400 typed notes (CN2400) item by item: inverse function theorem, Darboux integration, sequences and series of functions, Taylor series, power series, vector functions, multivariable differentiation, inverse function theorem in $\R^n$. The implicit function theorem (CN2400 §7) is not in the notebook.

**Legibility.** All 102 photos are readable. Most MATH2400 photos (roughly 017–102) have a broad diagonal shadow band across the page; it lowers contrast but hides nothing. One reading is uncertain because of the handwriting: HW2400 037 (the factor in $\delta = \frac{1}{a^2}\varepsilon$ vs $a^2\varepsilon$).

---

## HW2400 001 · `20261121_230307.jpg` · Introduction to Analysis

**Def.** A sequence $(x_n)_{n \in \N}$ converges to $x \in \R$ iff $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n > M$, $\abs{x_n - x} < \varepsilon$.

**Def.** Let $f : S \to \R$ be a function, and let $c$ be a cluster point of $S \subseteq \R$. $L \in \R$ is the limit of $f$ as $x$ approaches $a$, i.e. $\lim_{x \to a} f(x) = L$, if $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $0 < \abs{x - a} < \delta \implies \abs{f(x) - L} < \varepsilon$.
[possible error: the cluster point is called $c$ and then $a$; "cluster point" is not defined in the notes; $x \in S$ is not stated]

**Def.** Suppose $S \subseteq \R$ and $c \in S$. The function $f : S \to \R$ is continuous at $c$ iff $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $0 < \abs{x - a} < \delta \implies \abs{f(x) - f(a)} < \varepsilon$. In other words, $\lim_{x \to a} f(x) = f(a)$.
[possible error: $c$ and $a$ are mixed again (read $a = c$); "$\lim_{x \to a} f(x) = f(a)$" holds in this form only when $a$ is a cluster point of $S$]

**Def.** Let $I \subseteq \R$ be an interval, and let $f : I \to \R$ be a function. We define the derivative of $f$ at $x_0 \in I$ as
$$\frac{\dd}{\dd x}f(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

## HW2400 002 · `20261121_230312.jpg` · The real numbers

**N.** Sets of numbers: $\N \subset \Z \subset \Q \subset \R \subset \C$

The reals have three important properties:
- $\R$ is a field. ($\Q$, $\R$)
- $\R$ is ordered. ($\N$, $\Z$, $\Q$, $\R$)
- $\R$ is complete. ($\R$)
(the brackets list which number sets have the property.)

**N.** Bounds, supremum, infimum

Let $A \subseteq \R$. $b \in \R$ is:
- an upper bound of $A$ if $b \ge x$ $\forall x \in A$
- a lower bound of $A$ if $b \le x$ $\forall x \in A$

The supremum and infimum are the [crossed out: "greatest"] least upper bound, and the greatest lower bound, res.

When considering the empty set $\emptyset$:
- $\sup \emptyset = -\infty$
- $\inf \emptyset = \infty$

**Rem.** Unlike the maximum and minimum of an ordered set, the supremum and infimum of the set need not be elements of that set.

**Def.** The least-upper-bound property (i.e. the completeness, or Dedekind):
- $\forall S \subseteq \R$, $\exists x = \sup S \in \R$ [possible error: $S$ must be non-empty and bounded above]

## HW2400 003 · `20261121_230317.jpg` · Properties of the reals

**N.**
- $x > 0 \iff -x < 0$
- $x > 0$, $y < z \implies xy < xz$
- $x < 0$, $y < z \implies xy > xz$
- $x \ne 0 \implies x \cdot x > 0$
- $0 < x < y \implies 0 < 1/y < 1/x$, $\implies x^2 < y^2$
- $x \le y$, $z \le w \implies x + z \le y + w$

These properties are inherited by the definition of a field – $\Q$ shares these properties too. [possible error: these are consequences of the order axioms of an ordered field, not of the field axioms alone]

**N.** We define the absolute value by:
$$\lVert x \rVert = \begin{cases} x & \text{if } x \ge 0\\ -x & \text{if } x < 0\end{cases}$$
(written with double bars on this page; single bars $\abs{x}$ from HW 004 on.)
The properties of the absolute value are:
- $\lVert x \rVert \ge 0$, $\lVert x \rVert = 0 \iff x = 0$
- $\lVert -x \rVert = \lVert x \rVert$
- $\lVert xy \rVert = \lVert x \rVert \cdot \lVert y \rVert$
- $\lVert x^2 \rVert = x^2$
- $\lVert x \rVert \le y \iff -y \le x \le y$
- $-\lVert x \rVert \le x \le \lVert x \rVert$

**N.** We define the triangle inequality: $\lVert x + y \rVert \le \lVert x \rVert + \lVert y \rVert$

**Proof.** $-\lVert x \rVert \le x \le \lVert x \rVert$ and $-\lVert y \rVert \le y \le \lVert y \rVert$
$\implies -(\lVert x \rVert + \lVert y \rVert) \le x + y \le \lVert x \rVert + \lVert y \rVert$
$\implies \lVert x + y \rVert \le \bigl\lVert \lVert x \rVert + \lVert y \rVert \bigr\rVert = \lVert x \rVert + \lVert y \rVert$ ∎

## HW2400 004 · `20261121_230321.jpg` · Triangle inequality

**Def.** We extend the triangle inequality to $n$ terms: $\abs{x_1 + x_2 + \dots + x_n} \le \abs{x_1} + \abs{x_2} + \dots + \abs{x_n}$

**Proof.** We prove by induction. For $n = 1$, $\abs{x_1} \le \abs{x_1}$.
We now assume the inequality for $n$ terms. Then, $\abs{x_1 + x_2 + \dots + x_n + x_{n+1}}$ [the proof stops here; the rest of the space is blank]

**Def.** There are two important properties similar to the triangle inequality:
- $\abs{x - y} \ge \abs{(\abs{x} - \abs{y})}$
- $\abs{x - y} \le \abs{x} + \abs{y}$
(stated without proof)

## HW2400 005 · `20261121_230328.jpg` · Sequences

**Def.** A sequence of elements from a set $X \subseteq \R$ is a map $M : X \leftarrow \N$, assigning each $x \in \N$ to an element in $X$. [possible error: the arrow should point $\N \to X$]

**Def.** A sequence $(x_n)_{n \in \N}$ converges to $x \in \R$ iff $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n > M$, $\abs{x_n - x} < \varepsilon$. If so, the following are equivalent:
- $(x_n)_{n \in \N}$ is convergent
- $\lim_{n \to \infty} x_n = x$

**Rem.** In higher-dimensional space, instead of the interval $\abs{x_n - x} < \varepsilon$, we use open balls.
For each $\varepsilon > 0$ and $x \in X$, let $B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}$. ($d$ is not defined here.)

**Ex.** Prove that the sequence $\{1/n\}$ converges to $0$.

**P.** For $\varepsilon > 0$, we want $\abs{x_n - 0} < \varepsilon$. $\implies \abs{x_n - 0} = \abs{1/n} < \varepsilon$.
We pick $n \ge M \implies 1/n \le 1/M < \varepsilon \implies M = \ceil{\frac{1}{\varepsilon}} + 1$ $\square$

## HW2400 006 · `20261121_230331.jpg` · Proofs of sequences

**Ex.** Prove that $\lim_{n \to \infty} \frac{n^2 + 1}{n^2 + n} = 1$.

**P.**
$$\Bigl\lvert \frac{n^2 + 1}{n^2 + n} - 1 \Bigr\rvert = \Bigl\lvert \frac{n^2 + 1 - n^2 - n}{n^2 + n} \Bigr\rvert = \Bigl\lvert \frac{1 - n}{n^2 + n} \Bigr\rvert = \frac{n - 1}{n^2 + n} \le \frac{n}{n^2 + n} = \frac{1}{n + 1}$$
We choose $M = \ceil{\frac{1}{\varepsilon}} + 1$. Therefore, $\forall n > M$,
$$\Bigl\lvert \frac{n^2 + 1}{n^2 + n} - 1 \Bigr\rvert \le \frac{1}{n + 1} \le \frac{1}{M + 1} < \varepsilon. \quad \square$$

**Ex.** Prove that the sequence $\{(-1)^n\}$ is divergent.

**P.** We will prove by contradiction. Suppose $\exists M \in \N$ s.t. the definition of the limit. Then $\abs{(-1)^n - L} < \varepsilon$. We try $\varepsilon = 1/2$. For an even $n$, WLOG:
$$1/2 > \abs{x_n - x} = \abs{1 - x} \quad\text{and}\quad 1/2 > \abs{x_{n+1} - x} = \abs{-1 - x}$$
$$\implies 1 > \abs{1 - x} + \abs{-1 - x} \ge \abs{1 - x - (-1 - x)} = 2$$
which is a contradiction. $\square$
[the limit is called $L$ and then $x$]

## HW2400 007 · `20261121_230337.jpg` · Bounded sequences

**Def.** A sequence $(x_n)$ is bounded if $\exists B \in \R$ such that $\abs{x_n} \le B$ $\forall n \in \N$.

**Def.** [a theorem] If a sequence is convergent, it is bounded.

**P.** Suppose $\{x_n\}$ converges to $x$. Hence $\exists M \in \N$ s.t. $\forall n > M$, $\abs{x_n - x} < 1$. Therefore, for $\forall n > M$:
$$\abs{x_n} = \abs{x_n - x + x} \le \abs{x_n - x} + \abs{x} < 1 + \abs{x}$$
Thus the tail of the sequence is bounded. For the remaining elements, $\forall n \in \N$,
$$\abs{x_n} \le B = \max\{\abs{a_1}, \abs{a_2}, \dots, \abs{a_{N-1}}, \abs{L} + 1\}. \quad \square$$
[possible error: notation switches from $x_n$, $x$, $M$ to $a_n$, $L$, $N$; with $n > M$ for the tail, the finite part runs to $\abs{x_M}$]

**Rem.** A bounded sequence is not necessarily convergent: for example $\{(-1)^n\} \le 1$, but diverges.

**Def.** [a theorem] A convergent sequence has a unique limit.

**P.** We assume $\{x_n\}$ has limits $x_1$ (overwritten), $x_2$. Therefore, $\exists N_1, N_2$ s.t. $\forall n > N_1$, $\forall n > N_2$, then $\abs{x_n - x_1} < \varepsilon/2$ and $\abs{x_n - x_2} < \varepsilon/2$. For $n \ge \max\{N_1, N_2\}$:
$$\abs{x_1 - x_2} = \abs{x_1 - x_n + x_n - x_2} \le \abs{x_1 - x_n} + \abs{x_n - x_2} < \varepsilon/2 + \varepsilon/2 = \varepsilon. \implies x_1 = x_2 \quad \square$$
[$\varepsilon > 0$ is not fixed; "$n \ge \max$" should be "$n > \max$"; the step "for every $\varepsilon$" $\implies x_1 = x_2$ is implicit]

## HW2400 008 · `20261121_230339.jpg` · Continuity of algebraic operations

**Def.** [a theorem] Let $\{x_n\}$ and $\{y_n\}$ be convergent sequences. Fix $\lambda \in \R$. Then,
- $\lim_{n \to \infty} x_n + \lim_{n \to \infty} y_n = \lim_{n \to \infty} x_n + y_n$
- $\lim_{n \to \infty} \lambda x_n = \lambda \cdot \lim_{n \to \infty} x_n$
- $\lim_{n \to \infty} a_n \cdot \lim_{n \to \infty} b_n = \lim_{n \to \infty} a_nb_n$
- $\dfrac{\lim_{n \to \infty} a_n}{\lim_{n \to \infty} b_n} = \lim_{n \to \infty} \dfrac{a_n}{b_n}$ [possible error: needs $\lim b_n \ne 0$ (and $b_n \ne 0$)]

**P.** Let $z_n = x_n + y_n$. Fix $\varepsilon > 0$. Therefore,
$\exists M_1 \in \N$ s.t. $\forall n \ge M_1$, $\abs{x_n - x} < \varepsilon/2$
$\exists M_2 \in \N$ s.t. $\forall n \ge M_2$, $\abs{y_n - y} < \varepsilon/2$
$M = \max\{M_1, M_2\}$. Therefore, $\forall n \ge M$:
$$\abs{z_n - (x + y)} = \abs{x_n + y_n - x - y} \le \abs{x_n - x} + \abs{y_n - y} < \varepsilon/2 + \varepsilon/2 = \varepsilon$$

**Rem.** The three remaining proofs are in Proposition 2.2.5 in Lebl, or in the 1071 Ducky notes. [i.e. the MATH1071 typed notes, §2.2]

## HW2400 009 · `20261121_230345.jpg` · Squeeze theorem

**Def.** [a theorem] Suppose the sequences $\{a_n\}$, $\{b_n\}$, $\{c_n\}$ are such that:
- $\forall n \in \N$, $a_n \le b_n \le c_n$
- $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$.
Then $\lim_{n \to \infty} b_n = L$.

**P.** Fix $\varepsilon > 0$. Therefore,
$\exists M_1 \in \N$ s.t. $\forall n \ge M_1$, $\abs{a_n - L} < \varepsilon$
$\exists M_2 \in \N$ s.t. $\forall n \ge M_2$, $\abs{c_n - L} < \varepsilon$
$M = \max\{M_1, M_2\}$. Therefore, $\forall n \ge M$:
$$L - \varepsilon < a_n \le b_n \le c_n < L + \varepsilon \implies L - \varepsilon < b_n < L + \varepsilon \implies \abs{b_n - L} < \varepsilon. \quad \square$$

**Rem.** This is a separate proof compared to in MATH1071. [cf. MATH1071 HW 44]

**Def.** [a theorem] If $\{x_n\}$ is convergent, then $\{\abs{x_n}\}$ is convergent and $\lim_{n \to \infty} \abs{x_n} = \abs{\lim_{n \to \infty} x_n}$.

**P.** Fix $\varepsilon > 0$. By the definition of the limit, $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n \ge M$, $\abs{x_n - x} < \varepsilon$. By the reverse triangle inequality,
$$\bigl\lvert \abs{x_n} - \abs{x} \bigr\rvert \le \abs{x_n - x} < \varepsilon.$$

## HW2400 010 · `20261121_230349.jpg` · Monotonicity

**Def.** A sequence $\{x_n\}$ is monotone increasing if $x_n \le x_{n+1}$ $\forall n \in \N$. A sequence $\{x_n\}$ is monotone decreasing if $x_n \ge x_{n+1}$ $\forall n \in \N$.

**Def.** [a theorem] A monotone sequence $\{x_n\}$ is bounded iff it is convergent.

**P.** The reverse direction is proven already. [convergent $\implies$ bounded, HW 007]
For the forward direction, WLOG, consider a monotone sequence $\{x_n\}$. We assume $\{x_n\}$ is monotone increasing – if not, apply to $-x_n$.
Let $L = \sup\{x_n : n \in \N\} \in \R$. This exists as the sequence is bounded.
Fix $\varepsilon > 0$. $\exists M \in \N$ s.t. $x_M > L - \varepsilon$. As $\{x_n\}$ is monotone increasing, $\forall n \ge M$, $x_n \ge x_M$. Hence,
$$\abs{x_n - L} = L - x_n \le L - x_M < \varepsilon.$$
Thus $\{x_n\}$ converges to $L$. $\square$

## HW2400 011 · `20261121_230354.jpg` · Subsequences

**Def.** Let $(a_n)_{n=1}^{\infty}$ be a sequence and let $\{n_1, n_2, \dots\}$ be a strictly increasing sequence of naturals. Then, the sequence $(a_{n_i})_{i=1}^{\infty}$ is a subsequence of $(a_n)_{n=1}^{\infty}$.

**Def.** The number $a \in \R$ is a cluster point of $(a_n)_{n=1}^{\infty}$ if $\forall \varepsilon > 0$, $\exists$ infinitely many $n \in \N$ such that $\abs{a_n - a} < \varepsilon$.

**Def.** [a theorem] If $(a_n)_{n=1}^{\infty}$ is convergent, then every subsequence $(a_{n_i})_{i=1}^{\infty}$ is convergent, and $\lim_{n \to \infty} a_n = \lim_{i \to \infty} a_{n_i}$.

**P.** Let $L = \lim_{n \to \infty} a_n$. Hence $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n \ge M$, $\abs{a_n - L} < \varepsilon$.
Therefore, $\forall i \ge M$, $n_i \ge M$ (since $n_i \ge i$) and thus $\abs{a_{n_i} - L} \le \abs{a_n - L} < \varepsilon$.
[possible error: the middle term should be dropped: $n_i \ge M$ gives $\abs{a_{n_i} - L} < \varepsilon$ directly]

**Def.** [a theorem] Every sequence $(a_n)_{n=1}^{\infty}$ has a monotone subsequence.

**P.** We define $k \in \N$ as a peak index of $(a_n)_{n=1}^{\infty}$ if $a_k \ge a_n$ $\forall n \ge k$. Split the proof into two cases.
Case 1: $\exists$ infinitely many peak points $n_1, n_2, \dots$, where $n_1 < n_2 < \cdots$. By definition, $a_{n_1} \ge a_{n_2} \ge \cdots$, thus $(a_{n_i})_{i=1}^{\infty}$ is monotone.
Case 2: $\exists$ finitely many peak points $k_1, \dots, k_m$, $m \in \N$. Set $n_1 = \max\{k_1, \dots, k_m\} + 1$. Since $n_1 \notin \{\dots\}$, $k_1$ is not a peak index. Thus, $\exists n_2 > n_1$ s.t. $a_{n_2} \ge a_{n_1}$. Repeat to obtain monotone $(a_{n_i})_{i=1}^{\infty}$.
[possible error: "$k_1$ is not a peak index" should read "$n_1$"; with this definition of peak index, "not a peak index" gives $a_{n_2} > a_{n_1}$. MATH1071 HW 45 uses strict $a_k > a_n$ for $n > k$]

## HW2400 012 · `20261121_230357.jpg` · Bolzano–Weierstraß theorem

**Def.** [a theorem] Every bounded sequence has a convergent subsequence.

**P.** Every sequence $(x_n)_{n=1}^{\infty}$ has a monotone subsequence $(x_{n_i})_{i=1}^{\infty}$. Since $(x_n)$ is bounded, $(x_{n_i})$ is bounded. Hence we have a monotone and bounded subsequence, which must therefore converge.

## HW2400 013 · `20261121_230405.jpg` · Cauchy sequences

**Def.** A sequence $(x_n)_{n=1}^{\infty}$ is Cauchy if $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. if $k, l \ge M$, $\abs{x_k - x_l} < \varepsilon$.

**Rem.** The definition $\abs{x_k - x_l} < \varepsilon$ must hold $\forall k, l \ge M$.

**Ex.** Prove $(\frac1n)_{n=1}^{\infty}$ is Cauchy.

**P.** Fix $\varepsilon > 0$. Set $M = \ceil{2/\varepsilon} > 2/\varepsilon$ $\forall k, l \ge M$. Thus,
$$\Bigl\lvert \frac1k - \frac1l \Bigr\rvert \le \Bigl\lvert \frac1k \Bigr\rvert + \Bigl\lvert \frac1l \Bigr\rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
[$\ceil{2/\varepsilon} \ge 2/\varepsilon$, not $>$; with $k, l \ge M$ the bound is $\le$, so $M = \ceil{2/\varepsilon} + 1$ would be needed for strict inequality]

**Ex.** The sequence $((-1)^n)_{n=1}^{\infty}$ is not Cauchy.

**P.** $\forall M \in \N$, take $k \ge M$ to be even, and let $l = k + 1$ be odd. Thus,
$$\abs{(-1)^k - (-1)^l} = \abs{1 - (-1)} = 2 \not< \varepsilon \quad \text{if } \varepsilon \le 2.$$

**Def.** [a theorem] All Cauchy sequences are bounded.

**P.** If $(x_n)$ is Cauchy, then $\exists M \in \N$ s.t. $\forall k, l \ge M$, $\abs{x_k - x_l} < 1$. Thus $\abs{x_k - x_M} < 1$.
By the second triangle inequality, $\abs{x_k} - \abs{x_M} < 1$. Thus $\abs{x_k} < \abs{x_M} + 1$.
Let $B = \max\{\abs{x_1}, \abs{x_2}, \dots, \abs{x_{M-1}}, \abs{x_M} + 1\}$. Then $\abs{x_n} \le B$ $\forall n \in \N$.

## HW2400 014 · `20261121_230409.jpg` · Cauchy iff convergent

**Def.** [a theorem] A sequence is Cauchy iff it is convergent.

**P.** We first prove in the forward direction.
Let $(x_n)$ be a Cauchy sequence. Hence $(x_n)$ is bounded, and has a convergent subsequence $(x_{n_i})$ with limit $L$. We claim that $(x_n)$ also converges to $L$. Fix $\varepsilon > 0$. By definitions,
$\exists M_1$ s.t. $\forall k, l \ge M_1$, $\abs{x_k - x_l} < \varepsilon/2$
$\exists M_2$ s.t. $\forall i > M_2$, $\abs{x_{n_i} - L} < \varepsilon/2$.
Let $M = \max\{M_1, M_2\}$. Thus $\forall n \ge M$,
$$\abs{x_n - L} = \abs{x_n - x_{n_{M+1}} + x_{n_{M+1}} - L} \le \abs{x_n - x_{n_{M+1}}} + \abs{x_{n_{M+1}} - L} < \varepsilon/2 + \varepsilon/2 = \varepsilon.$$
We now prove in the reverse direction.
Assume $\lim_{n \to \infty} x_n = L$. Fix $\varepsilon > 0$. By the definition of the limit, $\exists M \in \N$ s.t. $\forall n \ge M$, $\abs{x_n - L} < \varepsilon/2$. Thus for $k, l \ge M$,
$$\abs{x_k - x_l} = \abs{x_k - L + L - x_l} \le \abs{x_k - L} + \abs{L - x_l} < \varepsilon/2 + \varepsilon/2 = \varepsilon.$$
(Uses Bolzano–Weierstraß, HW 012.)

## HW2400 015 · `20261121_230420.jpg` · Upper and lower limits

**Def.** Given a sequence $(x_n)_{n=1}^{\infty}$, define:
- $a_n := \sup\{x_k : k \ge n\}$
- $b_n := \inf\{x_k : k \ge n\}$
The upper limit of $(x_n)$ is defined by: $\limsup_{n \to \infty} x_n = \lim_{n \to \infty} a_n$.
The lower limit of $(x_n)$ is defined by: $\liminf_{n \to \infty} x_n = \lim_{n \to \infty} b_n$.

**Rem.** Note that $\limsup_{n \to \infty} x_n$ and $\liminf_{n \to \infty} x_n$ may be $\infty$ or $-\infty$ respectively.

**Def.** [a theorem] A bounded sequence converges iff $\limsup_{n \to \infty} x_n = \liminf_{n \to \infty} x_n$. (stated without proof)

**Def.** [a theorem] If a sequence is bounded, then the upper and lower limits exist.

**P.** WLOG, we consider the upper limit. Note that:
$$a_{n+1} \le a_n \iff \{x_k : k \ge n + 1\} \subseteq \{x_k : k \ge n\}$$
Thus $a_n$ is monotone decreasing and bounded, so $a_n$ must converge.
[possible error: "$\iff$" should be "$\Leftarrow$" (the inclusion implies the inequality)]

## HW2400 016 · `20261121_230425.jpg` · Series

**Def.** Given a sequence $(x_n)_{n=1}^{\infty}$, we define a series as $\sum_{n=1}^{\infty} x_n$.

**Def.** We define the $k$th partial sum of the series $\sum_{n=1}^{\infty} x_n$ by $\sum_{n=1}^{k} x_n$.

**Def.** Consider the sequence of partial sums $(S_k)_{k=1}^{\infty}$. If $(S_k)_{k=1}^{\infty}$ converges to some $S \in \R$, we say the series converges and
$$\sum_{n=1}^{\infty} x_n = \lim_{k \to \infty} S_k = \lim_{k \to \infty} \sum_{n=1}^{k} x_n.$$
If $(S_k)_{k=1}^{\infty}$ diverges, then the series diverges.

**Def.** A series $\sum_{n=1}^{\infty} x_n$ is Cauchy iff $(S_k)_{k=1}^{\infty}$ is Cauchy.

**Def.** [a theorem] The series $\sum_{n=1}^{\infty} x_n$ is convergent if it is Cauchy. The series is Cauchy iff $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. if $p, q \ge M$, then $\bigl\lvert \sum_{p+1}^{q} a_k \bigr\rvert < \varepsilon$. [$a_k$ should be $x_k$; $q > p$ is assumed]

**P.** The series $\sum_{n=1}^{\infty} x_n$ converges iff $(S_k)_{k=1}^{\infty}$ does. This sequence converges iff it is Cauchy. Therefore, $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. if $p, q \ge M$, then $\abs{S_q - S_p} < \varepsilon$. Thus, [one crossed-out line]
$$\abs{S_q - S_p} = \Bigl\lvert \sum_{n=1}^{q} x_n - \sum_{n=1}^{p} x_n \Bigr\rvert = \Bigl\lvert \sum_{n=p+1}^{q} x_n \Bigr\rvert < \varepsilon.$$

## HW2400 017 · `20261121_230429.jpg` · Series convergence tests

**Def.** [a theorem] If $\sum_{n=1}^{\infty} x_n$ converges, then $\lim_{n \to \infty} x_n = 0$.

**Rem.** We often use this theorem using the contrapositive: if $\lim_{n \to \infty} x_n \ne 0$, then $\sum_{n=1}^{\infty}$ must diverge.

**P.** As $\sum_{n=1}^{\infty} x_n$ converges, it is Cauchy. Thus $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n \ge M$,
$$\abs{x_{n+1} - 0} = \abs{x_{n+1}} = \Bigl\lvert \sum_{i=n+1}^{n+1} x_i \Bigr\rvert < \varepsilon.$$
Therefore $\forall n \ge M + 1$, $\abs{x_n - 0} < \varepsilon$.

**P.** We present an alternative proof. Let $x_n = S_n - S_{n-1}$. Therefore,
$$\lim_{n \to \infty} x_n = \lim_{n \to \infty}(S_n - S_{n-1}) = \lim_{n \to \infty} S_n - \lim_{n \to \infty} S_{n-1} = 0.$$

**Rem.** This theorem's negation (converse) is false. We will prove this in the following example. [it is the converse, not the negation]

## HW2400 018 · `20261121_230437.jpg` · Series convergence examples

**Def.** [a statement] $\lim_{n \to \infty} x_n = 0 \;\not\Rightarrow\; \sum_{n=1}^{\infty} x_n$ converges. We prove this by examining the harmonic series.

**P.** Consider the harmonic series $\sum_{n=1}^{\infty} \frac1n$. We examine the partial sum $(S_{2^k})_{k=1}^{\infty}$.
- $k = 0$: $S_1 = 1$
- $k = 1$: $S_2 = 1 + (\frac12)$
- $k = 2$: $S_4 = 1 + (\frac12) + (\frac13 + \frac14)$
$$\implies S_{2^k} = 1 + \sum_{i=1}^{k}\Bigl(\sum_{m = 2^{i-1}+1}^{2i} \frac1m\Bigr)$$
[possible error: the inner upper limit should be $2^i$]
Also, $\frac13 + \frac14 > \frac14 + \frac14 = \frac12$, …
$$\implies \sum_{M = 2^{k-1}+1}^{2^k} \frac1M \ge \sum_{M = 2^{k-1}+1}^{2^k} \frac{1}{2^k} = 2^{k-1} \cdot \frac{1}{2^k} = \frac12$$
$$\implies S_{2^k} \ge 1 + \sum_{i=1}^{k} \frac12 = 1 + \frac{k}{2}$$
$\implies (S_{2^k})$ diverges, so $(S_k)$ diverges.
(the subscript is written $S_{2k}$ in places; $S_{2^k}$ is meant.)

## HW2400 019 · `20261121_230440.jpg` · Absolute convergence of series

**Def.** [a theorem] Consider a series $\sum_{n=1}^{\infty} x_n$, where $\forall n > 0$, $x_n \ge 0$. The series converges iff the series of partial sums is bounded above. [read: "the sequence of partial sums"; stated without proof]

**Def.** The series $\sum_{n=1}^{\infty} x_n$ converges absolutely if the series $\sum_{n=1}^{\infty} \abs{x_n}$ converges. If a series converges but does not converge absolutely, then it converges conditionally.

**Def.** [a theorem] If $\sum_{n=1}^{\infty} x_n$ converges absolutely, then it converges.

**P.** The series $\sum_{n=1}^{\infty} \abs{x_n}$ is Cauchy. Therefore, $\forall \varepsilon > 0$, $\exists M \in \N$ s.t. if $p, q \ge M$, then
$$\Bigl\lvert \sum_{i=p+1}^{q} x_i \Bigr\rvert \le \Bigl\lvert \sum_{i=p+1}^{q} \abs{x_i} \Bigr\rvert < \varepsilon$$
Thus $\sum_{n=1}^{\infty} x_n$ is Cauchy.

**Ex.** The series $\sum_{n=1}^{\infty} (-1)^n/n$ converges, but does not converge absolutely. Therefore, the series is conditionally convergent. (no proof given)

## HW2400 020 · `20261121_230446.jpg` · Series comparison test

**Def.** [a theorem] If $0 \le x_n \le y_n$ $\forall n \in \N$ and $\sum_{n=1}^{\infty} y_n$ converges, then $\sum_{n=1}^{\infty} x_n$ converges.

**P.** Consider the sequence of partial sums $(S_k)_{k=1}^{\infty}$. Since $0 \le x_n$, $(S_k)$ is monotone non-decreasing. Also, $S_k \le \sum_{k=1}^{\infty} y_k$ $\forall n \in \N$. Since $\sum_{n=1}^{\infty} y_n$ converges, the partial sums are bounded. Therefore, $\sum_{n=1}^{\infty} x_n$ converges.

**The p-series test**

**Def.** [a theorem] For some $p \in \R$, the series $\sum_{n=1}^{\infty} 1/n^p$ converges for $p > 1$ and diverges for $p \le 1$.

**P.**
- Case 1: $p < 0$. $\lim_{n \to \infty} n^{-p} \ne 0$ so diverges.
- Case 2: $p = 0$. $\lim_{n \to \infty} n^0 = 1 \ne 0$ so diverges.
- Case 3: $p \in (0, 1)$. Diverges by comparison with $\frac1n$.
- Case 4: $p = 1$. The harmonic series diverges.
- Case 5: $p \in (1, 2)$ [blank]
- Case 6: $p > 2$ [blank]
[the convergent cases are not proved in the notes]

## HW2400 021 · `20261121_230449.jpg` · Ratio test

**Def.** [a theorem] Assume $x_n > 0$ $\forall n \in \N$. Then, assume the limit $L = \lim_{n \to \infty} \frac{\abs{x_{n+1}}}{\abs{x_n}}$ exists. Therefore,
- If $L < 1$, then $\sum_{n=1}^{\infty} x_n$ conv. absolutely.
- If $L > 1$, then $\sum_{n=1}^{\infty} x_n$ diverges.
- If $L = 1$, the test is inconclusive.
[the hypothesis "$x_n > 0$" makes the absolute values redundant; presumably $x_n \ne 0$ is meant]

**P.** [blank; the rest of the page is empty] (cf. MATH1071 HW 65 for a proof)

## HW2400 022 · `20261121_230455.jpg` · Root test

**Def.** [a theorem] Let $\sum_{n=1}^{\infty} x_n$ be a series, and let $L = \limsup_{n \to \infty} \abs{x_n}^{1/n}$. Then,
- If $L < 1$, then $\sum_{n=1}^{\infty} x_n$ conv. absolutely.
- If $L > 1$, then $\sum_{n=1}^{\infty} x_n$ diverges
- If $L = 1$, the test is inconclusive.

**P.** [blank]

## HW2400 023 · `20261121_230501.jpg` · Alternating series test

**Def.** [a theorem] Let $(x_n)_{n=1}^{\infty}$ be a sequence such that $\forall n \in \N$, $x_n > 0$ and $x_n \ge x_{n+1}$, and $\lim_{n \to \infty} x_n = 0$. Then, the series $\sum_{n=1}^{\infty} (-1)^n x_n$ converges.

**P.** [blank] (cf. MATH1071 HW 66 for a proof)

## HW2400 024 · `20261121_230507.jpg` · Rearrangement of series

**Def.** [a theorem] Let $\sum_{n=1}^{\infty} x_n$ be an absolutely convergent series converging to $L$. Let $f : \N \to \N$ be a bijection. Then $\sum_{n=1}^{\infty} x_{f(n)}$ is absolutely convergent, and converges to $L$. (stated without proof)

**Rem.** Note that for conditionally convergent series, the theorem does not hold. In particular, the series $\sum_{n=1}^{\infty} (-1)^n/n$ can be rearranged to converge to any $L \in \R$.

## HW2400 025 · `20261121_230514.jpg` · Limits of functions

**Def.** Let $f : S \to \R$ be a function. Assume that $c \in \R$ is a limit / cluster point of $S$. $L \in \R$ is the limit of $f$ as $x$ approaches $c$, or $\lim_{x \to c} f(x) = L$, iff $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $0 < \abs{x - c} < \delta \implies \abs{f(x) - L} < \varepsilon$.

**Ex.** Show $\lim_{x \to 3} \frac{x - 1}{2} = 1$.

**P.** Fix $\varepsilon > 0$. Set $\delta = \varepsilon$. Thus $\forall x$, $0 < \abs{x - 3} < \delta$. Therefore,
$$\Bigl\lvert \frac{x - 1}{2} - 1 \Bigr\rvert = \frac{\abs{x - 3}}{2} < \frac{\varepsilon}{2} < \varepsilon.$$

**Rem.** The function $f$ need not be defined at $c$ for the limit to exist at $c$.

**Ex.** Show $\lim_{x \to c}(mx + b) = mc + b$, for $m, b \in \R$.

**P.** Fix $\varepsilon > 0$. Let $\delta = \varepsilon/\abs{m}$. Then,
$$\abs{(mx + b) - (mc + b)} = \abs{m}\abs{x - c} < \varepsilon \implies \abs{x - c} < \varepsilon/\abs{m} = \delta$$
[possible error: needs $m \ne 0$; the argument runs backwards (from the conclusion to $\delta$)]

**Ex.** Show $\lim_{x \to 4} x^2 = 16$.

**P.** Fix $\varepsilon > 0$. Let $\delta = \min\{1, \varepsilon/9\}$. Then,
$$\abs{x^2 - 16} = \abs{x + 4}\abs{x - 4} \le \abs{x - 4}(\abs{x} + 4) < \varepsilon/9 \cdot 9 = \varepsilon$$
with the side note: $\abs{x - 4} < 1 \implies \abs{x} + 4 < 9$.

## HW2400 026 · `20261121_230518.jpg` · [no title]

**Def.** [a theorem] The limit $L$ of a function $f$ at $c \in \R$ is unique.

**P.** Assume $f$ at $c \in \R$ has two limits $L_1$, $L_2$. Therefore, $\exists \delta_1, \delta_2$ s.t.
$0 < \abs{x - c} < \delta_1 \implies \abs{f(x) - L_1} < \varepsilon/2$
$0 < \abs{x - c} < \delta_2 \implies \abs{f(x) - L_2} < \varepsilon/2$
Let $\delta = \min\{\delta_1, \delta_2\}$. Then,
$$\abs{L_1 - L_2} = \abs{L_1 - f(x) + f(x) - L_2} \le \abs{L_1 - f(x)} + \abs{f(x) - L_2} < \varepsilon/2 + \varepsilon/2 = \varepsilon. \implies L_1 = L_2.$$
[$\varepsilon$ is not fixed; an $x$ with $0 < \abs{x - c} < \delta$ exists because $c$ is a cluster point (not said)]

## HW2400 027 · `20261121_230524.jpg` · Sequential limits

**Def.** We provide an alternative definition of the limit. $\lim_{x \to c} f(x) = L$ iff $\forall$ sequences $(x_n)_{n=1}^{\infty}$ that converge to $c$, the sequences $(f(x_n))_{n=1}^{\infty}$ converge to $L$. [possible error: the sequences must lie in $S \setminus \{c\}$]

**Ex.** Show $\lim_{x \to 3} \frac{x - 1}{2} = 1$.

**P.** Let $(x_n)_{n=1}^{\infty}$ be a sequence such that $\lim_{n \to \infty} x_n = 3$. Thus, $\lim_{n \to \infty} \frac{x_n - 1}{2} = \frac{3 - 1}{2} = 1$.

**Def.** [a theorem] The epsilon-delta and sequential definition of the limit are equivalent.

**P.** We first prove in the forward direction. Fix $\varepsilon > 0$. By $\varepsilon$-$\delta$, $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. $0 < \abs{x - c} < \delta \implies \abs{f(x) - L} < \varepsilon$.
Also, for a sequence $(x_n)$, it converges iff $\forall \bar\varepsilon > 0$, $\exists M \in \N$ s.t. $\forall n \ge M$, $\abs{x_n - c} < \bar\varepsilon$.
Take $\bar\varepsilon = \delta$. Therefore, $\exists M \in \N$ s.t. $\forall n \ge M$, $0 < \abs{x_n - c} < \delta \implies \abs{f(x_n) - L} < \varepsilon$. $\square$

## HW2400 028 · `20261121_230527.jpg` · Sequential limits (cont.)

**P.** We now prove in the reverse direction, using the inverse of the statement. [i.e. by contrapositive]
By $\varepsilon$-$\delta$, $\exists \varepsilon > 0$ s.t. $\forall \delta > 0$, $0 < \abs{x - c} < \delta \implies \abs{f(x) - L} \ge \varepsilon$.
[possible error: the negation is "$\exists \varepsilon > 0$ s.t. $\forall \delta > 0$ $\exists x$ with $0 < \abs{x - c} < \delta$ and $\abs{f(x) - L} \ge \varepsilon$"]
Pick $\delta = \frac1n$ to construct $(x_n)$. Then $\exists \varepsilon > 0$, s.t. $\forall \delta > 0$, $0 < \abs{x_n - c} < 1/n \implies \abs{f(x_n) - L} \ge \varepsilon$.
Since $c - \frac1n < x_n < c + \frac1n$, $x_n \ne c$. Therefore, $\lim_{n \to \infty} x_n = c$ ("$=$" written over a crossed-out symbol).
However, we previously stated $\abs{f(x_n) - L} \ge \varepsilon$, which contradicts the limit. Thus $(f(x_n))_{n=1}^{\infty}$ does not converge to $L$. $\square$

**Ex.** Prove $\lim_{x \to 0} \sin(\frac1x)$ does not exist.

**P.** Let $x_n = \dfrac{1}{\pi n + \frac{\pi}{2}}$. Therefore, $\lim_{n \to \infty} x_n = 0$. Note that:
$$\sin\Bigl(\frac{1}{x_n}\Bigr) = \sin\Bigl(\pi n + \frac{\pi}{2}\Bigr) = (-1)^n.$$
Since $(-1)^n$ diverges, $\sin(\frac{1}{x_n})$ diverges. Therefore, $\lim_{x \to 0} \sin(\frac1x)$ does not exist.
However, if we let $y_n = \frac{1}{\pi n}$, $\sin(\frac{1}{y_n}) = \sin(\pi n) = 0$ and thus converges, so $\lim_{x \to 0} \sin(\frac1x)$ exists. These contradict (different limits), so the limit does not exist.
[the second argument reads as if it were a second proof; one convergent sequence does not show the limit exists]

## HW2400 029 · `20261121_230534.jpg` · Sequential limits (cont.)

**Ex.** Prove that $\lim_{x \to 0} x\sin(\frac1x) = 0$.

**P.** Let $(x_n)$ be a sequence such that $x_n \ne 0$, $\lim_{n \to \infty} x_n = 0$. Therefore,
$$\abs{x_n\sin(\tfrac{1}{x_n}) - 0} = \abs{x_n} \cdot \abs{\sin(\tfrac{1}{x_n})} \le \abs{x_n}$$
Thus as $x_n \to 0 \implies \abs{x_n} \to 0$. Therefore, $(x_n\sin(\frac{1}{x_n}))_{n=1}^{\infty}$. $\square$ [sentence unfinished: "… converges to $0$"]

**Def.** [a theorem] Let $\lim_{x \to c} f(x) = L_1$, $\lim_{x \to c} f(x) = L_2$, and let $f(x) \le g(x)$ $\forall x \in \R$. Then $L_1 \le L_2$.
[possible error: the second limit should be $\lim_{x \to c} g(x) = L_2$]

**P.** Consider the sequence $(x_n)_{n=1}^{\infty}$ which converges to $L$. We have that $f(x_n) \le g(x_n) \implies a_n \le b_n$. Hence, $\implies L_1 \le L_2$.
[possible error: the sequence should converge to $c$, not $L$; $a_n = f(x_n)$, $b_n = g(x_n)$ are not defined; the sequence limit inequality used is not proved in the notes]

**Def.** [a theorem] Let $\lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L$. Assume $f(x) \le g(x) \le h(x)$. Then, $\lim_{x \to c} g(x) = L$.

**P.** Similar to squeeze theorem proof in sequences.

## HW2400 030 · `20261121_230537.jpg` · Continuity

**Def.** Suppose $S \subseteq \R$ and $c \in S$. Then $f : S \to \R$ is continuous at $c$ iff $\forall \varepsilon > 0$, $\exists \delta > 0$ such that $0 < \abs{x - a} < \delta \implies \abs{f(x) - f(a)} < \varepsilon$. Alternatively, $\lim_{x \to a} f(x) = f(a)$. [as in HW 001: $a$ should be $c$]

**Def.** Alternatively, $f : S \to \R$ is continuous at $c$ if for all sequences $(x_n)_{n=1}^{\infty}$, with $\lim_{n \to \infty} x_n = c$, the sequences $(f(x_n))_{n=1}^{\infty}$ converge to $f(c)$.

**Def.** A function $f : S \to \R$ [crossed-out word] is continuous on $S$ iff $f$ is continuous for all $x \in S$.

**Ex.** Prove $f(x) = \sin(x)$, $f : \R \to \R$ is continuous on $\R$.

**P.** We prove $\lim_{\Delta x \to 0} \sin(c + \Delta x) - \sin(c) = 0$.
$$\lim_{\Delta x \to 0} \cdots = \lim_{\Delta x \to 0} 2\sin\Bigl(\frac{\Delta x}{2}\Bigr)\cos\Bigl(\frac{2c + \Delta x}{2}\Bigr)$$
Since $\abs{\cos(x)} \le 1$ and $\abs{\sin x} \le x$, [possible error: $\abs{\sin x} \le \abs{x}$]
$$\Bigl\lvert 2\sin\Bigl(\frac{\Delta x}{2}\Bigr)\cos\Bigl(\frac{2c + \Delta x}{2}\Bigr) \Bigr\rvert \le [\text{crossed out}]\ \Delta x$$
[read: $\le \abs{\Delta x}$]
Therefore as $\Delta x \to 0$, $\sin(c + \Delta x) - \sin(c) \to 0$. Therefore $\sin(x)$ is continuous on $\R$.

## HW2400 031 · `20261121_230542.jpg` · Continuity (cont.)

**Ex.** If $f : \R \to \R$ is a linear combination of polynomials, then $f$ is continuous. [read: "is a polynomial"]

**P.** Let $f(x) = a_dx^d + a_{d-1}x^{d-1} + \dots + a_1x + a_0$. Fix $c \in \R$. Let $(x_n)_{n=1}^{\infty}$ be a sequence such that $\lim_{n \to \infty} x_n = c$. Then,
$$\begin{aligned} f(c) &= a_dc^d + a_{d-1}c^{d-1} + \dots + a_1c + a_0\\ &= a_d(\lim x_n)^d + \dots + a_1\lim x_n + a_0\\ &= \lim(a_dx_n^d + \dots + a_1x_n + a_0) = \lim f(x_n). \end{aligned}$$
Hence $f$ is continuous on $c \in \R$, and thus $f$ is continuous on $\R$.

**Def.** [a theorem] The composition of functions $f : \R \to \R$ and $g : \R \to \R$ is itself continuous. [possible error: $f$ and $g$ must be continuous; stated without proof]

## HW2400 032 · `20261121_230546.jpg` · Continuity implies boundedness

**Def.** [a theorem] Let $f : \R \to \R$ be continuous. (Alternatively, let the domain be $[a, b] \subset \R$) Then $f$ is bounded.
[possible error: the domain must be a closed bounded interval $[a, b]$; a continuous $f : \R \to \R$ need not be bounded]

**P.** We will prove the contrapositive of the statement. Let $f$ be unbounded. Then, $\exists x_n \in [a, b]$ such that $\abs{f(x_n)} \ge n$, $\forall n \in \N$.
Since $x_n \in [a, b]$, $x_n$ is bounded. Therefore, there exists a convergent subsequence $(x_{n_i})$ with limit $L$. Since $x_{n_i} \in [a, b]$, then $L \in [a, b]$, $\forall i$.
However, $\abs{f(x_{n_i})} \ge n_i \ge i$, so the sequence is bounded, and therefore $\lim f(x_{n_i})$ does not exist. [possible error: "unbounded"]
Since $f(L)$ (written over a blacked-out word) is finite, and $f(L) = f(\lim x_{n_i})$.
Therefore, $f$ is not continuous at $x$. [possible error: "at $L$"; the sentence before is incomplete]
(Uses Bolzano–Weierstraß, HW 012; $L \in [a, b]$ because $[a, b]$ is closed, not proved.)

## HW2400 033 · `20261121_230555.jpg` · Extreme value theorem

**Def.** [a theorem] Let $f : [a, b] \to \R$ be continuous. Then $f$ acheives both a minimum and maximum value on $[a, b]$.

**P.** By Bolzano–Weierstraß, $f$ is bounded on $[a, b]$. [possible error: boundedness is the previous theorem (HW 032), which uses Bolzano–Weierstraß] Let $\alpha = \sup(f[a, b])$. We want to show $\exists x_{\max} \in [a, b]$ such that $f(x_{\max}) = \alpha$.
$\forall n > 0$, $\alpha - \frac1n$ is not an upper bound for $f([a, b])$. Therefore, we can choose $x_n \in [a, b]$ such that $f(x_n) > \alpha - \frac1n$.
By Bolzano–Weierstraß, $\exists$ convergent subsequence $(x_{n_k})$ with limit $x_{\max} \in [a, b]$.
Since $f$ is continuous, $f(x_{n_k}) \to f(x_{\max})$. We have therefore: $\alpha - \frac{1}{n_k} \le f(x_{n_k}) \le \alpha$.
By the squeeze theorem, $\lim_{k \to \infty} f(x_{n_k}) = \alpha$, implying that $f(x_{\max}) = \alpha$.
[only the maximum is treated; the minimum follows by applying this to $-f$ (not said)]

## HW2400 034 · `20261121_230559.jpg` · Intermediate value theorem

**Def.** [a theorem] Let $f : [a, b] \to \R$ be continuous. Let $c \in \R$ such that $f(a) < c < f(b)$. Then $\exists x \in (a, b)$ s.t. $f(x) = c$.

**P.** We need only prove the special case where $f(a) < 0$, $f(b) > 0$, $\exists x \in (a, b)$ such that $f(x) = 0$.
Let $A = \{x \in [a, b] : f([a, x]) < 0\}$. $A$ is bounded as $A \subseteq [a, b]$. $A \ne \emptyset$, as $a \in A$. By the least-upper-bound property, $\sup A := \alpha$. We claim $\alpha \in (a, b)$ and $f(\alpha) = 0$.
Suppose by contradiction that $\alpha = a$. Then $\exists \delta > 0$ s.t. $f$ is negative on $[\alpha, \alpha + \delta]$. This implies $a + \delta \in A$, which contradicts $\alpha = a$ being the supremum, so $\alpha \ne a$. Similarly, $\alpha \ne b$.
Suppose for contradiction that $f(\alpha) < 0$. Then $f$ is negative for $[\alpha - \delta, \alpha + \delta]$, for some $\delta > 0$. As $\alpha - \delta \in A$, then $\alpha + \delta \in A$, which contradicts the assumption that $\alpha = \sup A$, so $f(\alpha) \not< 0$. Similarly, $f(\alpha) \not> 0$. Therefore, $f(\alpha) = 0$.
Therefore, $f(\alpha) < 0$ and $\alpha \in (a, b)$. [possible error: should be $f(\alpha) = 0$]
For the general case, let $g(a) = f(a) + c$, let $g(b) = f(b) + c$, $\exists x \in (a, b)$ s.t. $f(x) = c$.
[possible error: the general case uses $g(x) = f(x) - c$ (so $g(a) < 0 < g(b)$), then $g(x) = 0 \iff f(x) = c$; the case $f(a) > c > f(b)$ is not mentioned]

## HW2400 035 · `20261121_230605.jpg` · Intermediate value theorem (cont.) / Uniform continuity

**Ex.** Prove that $f(x) = x^3 - 2x^2 + x - 1$, $f : [1, 2] \to \R$ has a root.

**P.** Observe $f(1) = -1$, $f(2) = 1$. Therefore, by the IVT, $\exists c \in (a, b)$ such that $f(c) = 0$. [$(a, b) = (1, 2)$; checked: $f(1) = -1$, $f(2) = 1$]

**Uniform continuity**

**Def.** Suppose $I$ is an interval on $\R$. Let $f : I \to \R$ be a function. Then $f$ is uniformly continuous on $I$ iff $\forall \varepsilon > 0$, $\exists \delta > 0$ such that $\forall x, y \in I$, if $\abs{x - y} < \delta$, then $\abs{f(x) - f(y)} < \varepsilon$.

**Rem.** In the definition of uniform continuity, $\delta$ is only allowed to depend on $\varepsilon$, and not some point in the interval $I$.
Uniform continuity is a global property (on an interval) while continuity is a local property (on a point).

**Rem.** Uniform continuity implies continuity. However, continuity does not imply uniform continuity.

## HW2400 036 · `20261121_230609.jpg` · Uniform continuity (cont.)

**Rem.** Despite continuity not implying uniform continuity, a function on a closed interval $f : [a, b] \to \R$ that is continuous on $[a, b]$ is uniformly continuous on $[a, b]$. (stated without proof)

**Ex.** Show $f : \R \to \R$, $f(x) = x^2$ is not uniformly continuous.

**P.** Suppose for contradiction that $f$ is u.c. Then $\forall \varepsilon > 0$, $\exists \delta > 0$ s.t. if $\abs{x - y} < \delta$ then $\abs{f(x) - f(y)} < \varepsilon$.
Choose some $x_1 > 0$ s.t. $x_2 = x_1 + \frac12\delta$. Then,
$$\varepsilon > \abs{x_1^2 - x_2^2} = \abs{x_1 + x_2}\abs{x_1 - x_2} = \abs{2x_1 + \tfrac12\delta}\abs{-\tfrac12\delta} = \delta x_1 + \tfrac14\delta^2 \ge \delta x_1$$
which implies $x_1 < \varepsilon/\delta$. If we take some $x > \varepsilon/\delta$, then the above statement is a contradiction. Therefore, $f(x) = x^2$ is not u.c. on $\R$.
[a single fixed $\varepsilon$ (e.g. $\varepsilon = 1$) is meant]

## HW2400 037 · `20261121_230614.jpg` · Uniform continuity (cont.)

**Ex.** Prove that $f : (a, 1) \to \R$, $a > 0$, $f(x) = \frac1x$ is uniformly continuous.

**P.** Let $a < x_1, x_2 < 1$. Then,
$$\abs{f(x_1) - f(x_2)} = \Bigl\lvert \frac{1}{x_1} - \frac{1}{x_2} \Bigr\rvert = \frac{\abs{x_2 - x_1}}{\abs{x_1x_2}} \le \frac{\abs{x_2 - x_1}}{a^2}$$
Hence $\forall \varepsilon > 0$, take $\delta = \frac{1}{a^2}\varepsilon$ [the factor is hard to read: $\frac{1}{a^2}$ or $a^2$]. Then $\forall x_1, x_2$:
$$\abs{x_1 - x_2} < \delta \implies \abs{f(x_1) - f(x_2)} < \frac{\varepsilon}{a^2} < \varepsilon.$$
[possible error: the choice that works is $\delta = a^2\varepsilon$, giving $\abs{f(x_1) - f(x_2)} < \delta/a^2 = \varepsilon$; as written the final chain does not follow (and $\varepsilon/a^2 > \varepsilon$ for $a < 1$)]

**Ex.** Prove that $f : (0, 1) \to \R$, $f(x) = \frac1x$ is not u.c.

**P.** Let $\varepsilon > 0$. Then for $\varepsilon > \abs{1/x - 1/y}$ to hold,
$$\varepsilon > \abs{1/x - 1/y} = \dots = \frac{\abs{y - x}}{xy} \implies \abs{x - y} < xy \cdot \varepsilon.$$
Therefore, to satisfy the definition of uniform continuity, we need $\delta \le xy \cdot \varepsilon$ $\forall x, y \in (0, 1)$. This would imply $\delta \le 0$, so no such $\delta > 0$ exists.
[heuristic: the argument shows what $\delta$ would have to satisfy, not that every $\delta$ fails; no explicit pair $x, y$ is given]

## HW2400 038 · `20261121_230617.jpg` · Lipschitz continuity

**Def.** Suppose $I$ is an interval on $\R$. Let $f : I \to \R$ be a function. Then $f$ is Lipschitz continuous iff $\exists K \in \R$ such that $\forall x, y \in I$, then $\abs{f(x) - f(y)} \le K\abs{x - y}$.

**Rem.** Lipschitz continuity implies uniform continuity, which implies continuity.

**P.** By the definition of Lipschitz continuity, $\abs{f(x) - f(y)} < K\abs{x - y}$. [should be $\le$]
Let $\varepsilon > 0$. Take $\delta = \varepsilon/K$. Thus $\forall x, y \in S$ s.t. $\abs{x - y} < \delta$, then
$$K\abs{x - y} < K\delta = K \cdot \frac{\varepsilon}{K} = \varepsilon.$$
Therefore $f$ is uniformly continuous.
[needs $K > 0$; "$S$" should be $I$]

## HW2400 039 · `20261121_230622.jpg` · The derivative

**Def.** Let $I$ be an interval, let $f : I \to \R$ be a function, and let $c \in I$. If the limit
$$L := \lim_{x \to c} \frac{f(x) - f(c)}{x - c} = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$$
exists, then $f$ is differentiable at $c$, that $L$ is the derivative of $f$ at $c$, and denote $f'(c) = L$.

**Rem.** If $f$ is differentiable at all $c \in I$, then $f$ is said to be differentiable (on $I$), and we obtain the function $f' : I \to \R$.

**Ex.** Find the derivative of $f(x) = x^2$ using first principles.
$$Q_{f,c}(x) = \frac{f(x) - f(c)}{x - c} = \frac{x^2 - c^2}{x - c} = \frac{(x - c)(x + c)}{x - c} = x + c$$
$$\lim_{x \to c} Q_{f,c}(x) = \lim_{x \to c} x + c = 2c.$$

**Ex.** Show $f(x) = \abs{x}$ is not differentiable at $x = 0$.

**P.** $Q_{f,0}(x) = \frac{\abs{x}}{x}$; $x > 0 \implies Q_{f,0}(x) = 1$; $x < 0 \implies Q_{f,0}(x) = -1$. Hence $\lim_{x \to 0} Q_{f,0}(x)$ does not exist.

**Rem.** The function $Q_{f,0}(x)$ is commonly known as the differentiation quotient.

## HW2400 040 · `20261121_230627.jpg` · Properties of the derivative

**Def.** [a theorem] Let the function $f : I \to \R$ be differentiable, at $c \in I$. Then $f$ is continuous [crossed-out word] at $c$.

**P.** We wish to show $\lim_{x \to c} f(x) = f(c)$.
$$\begin{aligned} \lim_{x \to c} f(x) &= \lim_{x \to c}\Bigl(\frac{f(x) - f(c)}{x - c}(x - c) + f(c)\Bigr) = \lim_{x \to c} \frac{f(x) - f(c)}{x - c} \lim_{x \to c}(x - c) + f(c)\\ &= f'(c) \cdot 0 + f(c) = f(c). \end{aligned}$$
(same proof as MATH1071 HW 48)

**Def.** [a theorem] The derivative is linear: given $h(x) = \alpha f(x) + \beta g(x)$ (a "$\pm$" is written over the $+$), where $\alpha \in \R$, $h'(x) = \alpha f'(x) + \beta g'(x)$.

**P.** Let $h(x) = \alpha f(x) + \beta g(x)$. For $x \in I$, $x \ne c$:
$$\frac{h(x) - h(c)}{x - c} = \frac{(\alpha f(x) + \beta g(x)) - (\alpha f(c) + \beta g(c))}{x - c} = \frac{\alpha f(x) - \alpha f(c)}{x - c} + \frac{\beta g(x) - \beta g(c)}{x - c} = \alpha \cdot \frac{f(x) - f(c)}{x - c} + \beta \cdot \frac{g(x) - g(c)}{x - c}$$
Taking the limit on both sides: $h'(x) = \alpha \cdot f'(x) + \beta \cdot g'(x)$.
As $f$ and $g$ are differentiable, $h$ is therefore differentiable.
[the limit is $x \to c$, so the result is $h'(c) = \alpha f'(c) + \beta g'(c)$; $\beta \in \R$ not stated]

## HW2400 041 · `20261121_230633.jpg` · Properties of the derivative (cont.)

**Def.** [a theorem] The product rule. Suppose $f, g : I \to \R$ are differentiable at $c \in I$. Then let $h : I \to \R$ be defined by $h(x) := f(x)g(x)$. Then $h$ is differentiable at $c$, and $h'(c) = f(c)g'(c) + f'(c)g(c)$.

**P.** Let $h(x) = f(x)g(x)$. For $x \in I$, $x \ne c$:
$$\frac{h(x) - h(c)}{x - c} = \frac{f(x)g(x) - f(c)g(c)}{x - c} = \frac{f(x)g(x) - f(x)g(c) + f(x)g(c) - f(c)g(c)}{x - c} = f(x) \cdot \frac{g(x) - g(c)}{x - c} + g(c) \cdot \frac{f(x) - f(c)}{x - c}$$
Taking the limit on both sides:
$$\lim_{x \to c} \frac{h(x) - h(c)}{x - c} = \lim_{x \to c} f(x) \cdot Q_{g,c}(x) + \lim_{x \to c} g(c)Q_{f,c}(x) = f(c) \cdot g'(c) + g(c) \cdot f'(c).$$
As $f$ and $g$ are differentiable, $h$ is therefore differentiable. Thus, $h'(c) = f(c)g'(c) + f'(c)g(c)$.
[$\lim_{x \to c} f(x) = f(c)$ uses continuity of $f$ at $c$ (HW 040), not cited]

**Rem.** As a corollary, we have the quotient rule. Suppose $f, g : I \to \R$ are differentiable at $c \in I$. Let $h : I \to \R$ be defined by $h(x) := f(x)/g(x)$. Then, $h$ is differentiable at $c$, if $g(c) \ne 0$, and
$$h'(c) = \frac{f'(c)g(c) - f(c)g'(c)}{g^2(c)}.$$
(no proof given)

## HW2400 042 · `20261121_230637.jpg` · Properties of the derivative (cont.)

**Def.** [a theorem] The chain rule. Let $I_1$, $I_2$ be intervals on $\R$. Let $g : I_1 \to I_2$ be differentiable at $c \in I_1$, and let $f : I_2 \to \R$ be differentiable at $g(c) \in I_2$. If we define $h : I_1 \to \R$ by $h(x) := (f \circ g)(x) = f(g(x))$, then $h$ is differentiable at $c$, and $h'(c) = f'(g(c)) \cdot g'(c)$.

**P.** For neater notation, let $d := g(c)$. Define $u : I_2 \to \R$ and $v : I_1 \to \R$ by
$$u(y) := \begin{cases} \dfrac{f(y) - f(d)}{y - d} & \text{if } y \ne d\\[4pt] f'(d) & \text{if } y = d\end{cases}\qquad v(x) := \begin{cases} \dfrac{g(x) - g(c)}{x - c} & \text{if } x \ne c\\[4pt] g'(c) & \text{if } x = c\end{cases}$$
(a crossed-out box before $f'(d)$.)
Note that: $f(y) - f(d) = u(y)(y - d)$, $g(x) - g(c) = v(x)(x - c)$. Thus,
$$h(x) - h(c) = f(g(x)) - f(g(c)) = u(g(x))(g(x) - g(c)) = u(g(x))(v(x)(x - c)) \implies \frac{h(x) - h(c)}{x - c} = u(g(x)) \cdot v(x)$$
Computing the limits $\lim_{y \to d} u(y) = f'(d) = f'(g(c))$ and $\lim_{x \to c} v(x) = g'(c)$, as $u$ and $v$ are continuous at $d = g(c)$ and $c$ respectively. Furthermore, $g$ is continuous at $c$.
Thus, the limit on the RHS exists, so $h$ is differentiable at $c$ and $h'(c) = f'(g(c)) \cdot g'(c)$.

## HW2400 043 · `20261121_230645.jpg` · The derivative of sin(x)

**Ex.** Prove that $\frac{\dd}{\dd x}\sin(x) = \cos x$.

**P.** We first prove the following lemmas:
(1) $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
  P. We squeeze between $\cos(x)$ and $1$. [no further detail or figure]
(2) $\lim_{x \to 0} \frac{\cos\theta - 1}{x} = 0$. [$\theta$ and $x$ are mixed; read $\theta = x$]
  P.
$$\lim_{x \to 0} \frac{\cos\theta - 1}{x} = \lim_{x \to 0}\Bigl(\frac{\cos x - 1}{x}\Bigr)\Bigl(\frac{\cos x + 1}{\cos x + 1}\Bigr) = \lim_{x \to 0} \frac{\cos^2 x - 1}{x(\cos x + 1)} = \Bigl(-\lim_{x \to 0} \frac{\sin x}{x}\Bigr)\Bigl(\lim_{x \to 0} \frac{\sin x}{\cos x + 1}\Bigr) = (-1)\Bigl(\frac02\Bigr) = 0$$
Now,
$$\begin{aligned} \frac{\dd}{\dd x}\sin x &= \lim_{h \to 0} \frac{\sin(x + h) - \sin(x)}{h} = \lim_{h \to 0} \frac{\sin x\cos h - \sin h\cos x - \sin(x)}{h}\\ &= \lim_{h \to 0} \frac{\sin h}{h}\cos x + \lim_{h \to 0} \frac{\cos h - 1}{h}\sin x = 1 \cdot \cos x + 0 \cdot \sin x = \cos x. \end{aligned}$$
[possible error: $\sin(x + h) = \sin x\cos h + \cos x\sin h$; the "$-$" in the second expression is a sign slip (the next line uses $+$)]

## HW2400 044 · `20261121_230648.jpg` · Local extrema

**Def.** Let $S \subset \R$ be a set, and let $f : S \to \R$ be a function. The function $f$ has a local (or relative) maximum at $c \in S$ if $\exists \delta > 0$ s.t. $\forall x \in S$ s.t. $\abs{x - c} < \delta$, then $f(x) \le f(c)$. The definition of local minimum is analogous.

**Def.** [a theorem] Let $f : [a, b] \to \R$ be a function differentiable at $c \in [a, b]$, and $c$ is a local extremum of $f$. Then $f'(c) = 0$. [possible error: needs $c \in (a, b)$ (e.g. $f(x) = x$ on $[0, 1]$ has a local maximum at $1$)]

**P.** WLOG, let $c$ be a local maximum. If $c$ is a local minimum, consider the function $-f$.
Therefore, $\abs{x - c} < \delta \implies f(x) - f(c) \le 0$.
Then if $x > c$: $\frac{f(x) - f(c)}{x - c} \le 0$; if $x < c$: $\frac{f(x) - f(c)}{x - c} \ge 0$.
Let sequences $\{x_n\}$ and $\{y_n\}$ be such that $x_n > c$ and $y_n < c$ $\forall n \in \N$, and that $\lim x_n = \lim y_n = c$.
Since $f$ is differentiable on $c$,
$$0 \ge \lim_{n \to \infty} \frac{f(x_n) - f(c)}{x_n - c} = f'(c),\qquad 0 \le \lim_{n \to \infty} \frac{f(y_n) - f(c)}{y_n - c} = f'(c)$$
Hence $f'(c) = 0$.
(cf. MATH1071 HW 49 for the one-sided-limit version.)

## HW2400 045 · `20261121_230659.jpg` · Mean value theorem

(A word before the title is scribbled out.)

**Def.** [a theorem] Suppose $f : I \to \R$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Then, there exists some $c \in (a, b)$ such that $f'(c) = \dfrac{f(b) - f(a)}{b - a}$.

**P.** Consider the function:
$$\varphi(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$$
$$\therefore \varphi(a) = f(a) - f(a) - \frac{f(b) - f(a)}{b - a}(a - a) = 0,\qquad \varphi(b) = f(b) - f(a) - \frac{f(b) - f(a)}{b - a}(b - a) = 0$$
Therefore, applying Rolle's theorem to $\varphi(x)$: $\exists c \in (a, b)$ such that $\varphi'(c) = 0$. Observe that:
$$\varphi'(x) = f'(x) - \frac{f(b) - f(a)}{b - a} \;\therefore\; \varphi'(c) = f'(c) - \frac{f(b) - f(a)}{b - a},\quad 0 = f'(c) - \frac{f(b) - f(a)}{b - a} \implies f'(c) = \frac{f(b) - f(a)}{b - a}$$
(same proof as MATH1071 HW 51; Rolle's theorem is on the next page.)

## HW2400 046 · `20261121_230704.jpg` · Rolle's theorem

**Def.** [a theorem] Suppose $f : I \to \R$ is continuous on $I$ and differentiable on $(a, b)$. Then if $f(a) = f(b)$, there exists some $c \in (a, b)$ such that $f'(c) = 0$. [$I = [a, b]$]

**P.** If $f(x) = f(a)$ for all $x \in (a, b)$, the theorem immediately follows. Assume $f$ is not constant.
WLOG, assume $\exists x_0 \in (a, b)$ s.t. $f(x_0) > f(a)$. If no such $x_0$ exists, $\exists x_1 \in (a, b)$ s.t. $f(x_1) < f(a)$.
By the EVT, $f$ has a maximum $c \in [a, b]$. Since $f(c) \ge f(x_0) > f(a) = f(b)$, $c \ne a$ and $c \ne b$. Thus, $c \in (a, b)$, and $f'(c) = 0$.
(same proof as MATH1071 HW 50.)

## HW2400 047 · `20261121_230711.jpg` · Inverse function theorem: lemmas

**L.** If $f$ is continuous and injective defined on $[a, b]$, and $f'(x_0) = 0$, then $f^{-1}$ is not differentiable on $f(x_0)$.

**P.** Let $x = f^{-1}(f(x)) = (f^{-1} \circ f)(x)$. If $f$ were differentiable, by the chain rule:
$$(f^{-1})'(f(x_0)) \cdot f'(x_0) = 1,\qquad (f^{-1} \circ f)(x_0) \cdot 0 = 1$$
which is a contradiction.
[possible error: "If $f^{-1}$ were differentiable"; the second line should read $(f^{-1})'(f(x_0)) \cdot 0 = 1$ (MATH2400 typed notes Lemma 1 has this)]

**L.** Let $I \subset \R$ (a blot after $I$) be an interval, and let $f : I \to \R$ be continuous and monotone. Then the image of $I$ is an interval.

**P.** Let $y_1, y_2 \in f(I)$. WLOG, assume $y_1 \ne y_2$. WLOG, assume $f$ is increasing. Then, $y_1 < y_2$. Then $\exists x_1 < x_2$: $f(x_1) = y_1$, $f(x_2) = y_2$.
Pick $y$: $f(x_1) < y < f(x_2)$. By the IVT, $\exists x$: $x_1 < x < x_2$ and $f(x) = y$. Hence, $y \in f(I)$.

## HW2400 048 · `20261121_230721.jpg` · Inverse function theorem: lemmas (cont.)

**L.** Let $I \subset \R$ be an interval, and let $f : I \to \R$ be monotone. Then $f$ is invertible on the range of $f$, and $f^{-1} : f(I) \to I$ is monotone and continuous.
[possible error: needs $f$ strictly monotone (the proof uses $s_1 < s_2 \implies f(s_1) < f(s_2)$); continuity of $f^{-1}$ also uses that $f$ is continuous (previous lemma)]

**P.** We first show $f$ is invertible. By 1061, $f$ is invertible $\iff f$ is bijective. $f$ is surjective on $f(I)$, so we need only show $f$ is injective.
Let $s_1 \ne s_2 \in I$. WLOG, assume $s_1 < s_2$. Since $f$ is monotone, $f(s_1) < f(s_2)$.
We now show $f^{-1}$ is monotone. Suppose $t_1, t_2 \in f(I)$. WLOG, assume $t_1 < t_2$. If $f^{-1}(t_1) \ge f^{-1}(t_2)$, then $t_1 \ge t_2$. This is a contradiction, so $f^{-1}(t_1) < f^{-1}(t_2)$.
We now show $f^{-1}$ is continuous. Fix $\varepsilon' > 0$. Let $\varepsilon = \min\{\varepsilon', \frac{b - x}{2}, \frac{x - a}{2}\}$ (a first entry "$\frac{b-a}{2}$" is struck out).
Then $x_0 < x_0 + \varepsilon \le x_0 + \frac{b - x_0}{2} = \frac{b + x_0}{2} < \frac{b + b}{2} = b$. Thus $x_0 < b$. Similarly, $x_0 > a$. Thus the interval $[x_0 - \varepsilon, x_0 + \varepsilon] \in I$, so $f(x_0 \pm \varepsilon)$ exists.
We have therefore shown that $\varepsilon$ is constrained by the size of the interval $I$.
[possible error: "$x_0 + \varepsilon < b$" is shown, not "$x_0 < b$"; "$\in I$" should be "$\subseteq I$"; $x$ and $x_0$ are mixed; continued on HW 049]

## HW2400 049 · `20261121_230727.jpg` · Inverse function theorem: lemmas (cont.)

**P.** We now show $f^{-1}$ is continuous. Let $y_0 \in f(I)$, $x_0 = f^{-1}(y_0)$. Let $\delta_1 = f(x_0 + \varepsilon) - f(x_0)$, $\delta_2 = f(x_0) - f(x_0 - \varepsilon)$. Suppose $t \in f(I)$ and $\abs{t - y_0} < \delta$. Then,
$$-\delta_2 \le -\delta < t - y_0 < \delta \le \delta_1 \implies f(x_0 - \varepsilon) < t < f(x_0 + \varepsilon) \implies x_0 - \varepsilon < f^{-1}(t) < x_0 + \varepsilon \implies \abs{f^{-1}(t) - x_0} < \varepsilon.$$
Thus $f^{-1}$ is continuous.
[$\delta := \min\{\delta_1, \delta_2\}$ is not written; $f$ is assumed increasing]

**L.** Let $I, J \subset \R$ be intervals, and let $f : I \to J$ be bijective (monotone and surjective), and let $f'(x) \ne 0$, and let $f$ be differentiable on $I$. Then $f^{-1}$ is differentiable on $y = f(x)$, and:
$$(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))} = \frac{1}{f'(x)}.$$

**P.** We wish to show that:
$$\lim_{k \to 0} \frac{f^{-1}(y + k) - f^{-1}(y)}{k} = \frac{1}{f'(x)}.$$
Since the inverse is monotone, $h(k) = 0$. Hence, we denote $h(k) = f^{-1}(y + k) - f^{-1}(y)$.
[possible error: the intended statement is "since $f^{-1}$ is continuous, $h(k) \to 0$ as $k \to 0$ (and $h(k) \ne 0$ for $k \ne 0$, since $f^{-1}$ is injective)"]

## HW2400 050 · `20261121_230732.jpg` · Inverse function theorem

**P.** (cont.) We note that:
$$f^{-1}(y) + h(k) = f^{-1}(y + k) \implies f(x + h(k)) = y + k \implies k = f(x + h(k)) - f(x)$$
This implies that:
$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{k \to 0} \frac{f(x + h(k)) - f(x)}{h(k)}$$
implying that:
$$\lim_{k \to 0} \frac{f^{-1}(y + k) - f^{-1}(y)}{k} = \lim_{k \to 0} \frac{h(k)}{f(x + h(k)) - f(x)} = \frac{1}{\lim_{k \to 0} \bigl(f(x + h(k)) - f(x)\bigr)/h(k)} = \frac{1}{f'(x)}.$$

**Def.** [a theorem] Inverse function theorem. Let $f : (a, b) \to \R$ be continuously differentiable. Suppose $x_0 \in (a, b)$ and $f'(x_0) \ne 0$. Then $\exists I \ni x_0$ such that $f|_I$ is invertible. Moreover, $f^{-1} : f(I) \to I$ is differentiable, and
$$(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}.$$

**P.** Suppose $f'(x_0) \ge 0$. [possible error: $f'(x_0) > 0$] Then $f$ is strictly increasing on some interval $I \ni x_0$. As $f$ is diff., $f$ is continuous, so by lemma 2, $f(I)$ is an interval. Hence, since lemma 3 applies, lemma 4 follows.
[lemma 1–4 = the four lemmas of HW 047–049 in order; "strictly increasing on some interval" uses continuity of $f'$ (not argued)]

## HW2400 051 · `20261121_230737.jpg` · Darboux integration

**Def.** We define a partition $P$ of an interval $[a, b]$ by the set $\{x_0, x_1, x_2, \dots, x_n\}$ such that $a = x_0 < x_1 < x_2 < \dots < x_n = b$.

**Rem.** Note that a partition does not need to be evenly spaced.

**Def.** Suppose $P$ is a partition of $[a, b]$. We define
$$m_i = \inf\{f(x) : x_{i-1} \le x \le x_i\},\qquad M_i = \sup\{f(x) : x_{i-1} \le x \le x_i\}$$
Then the lower Darboux sum of $f$ with respect to $P$, denoted by $L(f, P)$ is defined by: $L(f, P) = \sum_{i=1}^{n} m_i(x_i - x_{i-1})$.
The upper Darboux sum of $f$ with respect to $P$, denoted by $U(f, P)$ is defined by: $U(f, P) = \sum_{i=1}^{n} M_i(x_i - x_{i-1})$.

**Def.** [a theorem] Let $m, M \in \R$ be such that $m \le f(x) \le M$, $\forall x \in [a, b]$. Then for every partition $P$ of $[a, b]$,
$$m(b - a) \le L(f, P) \le U(f, P) \le M(b - a).$$

**P.** Let $P$ be a partition. Thus for all $i$, $m \le m_i$ and $M_i \le M$. Also, $m_i \le M_i$, and $\sum(x_i - x_{i-1}) = (b - a)$. Thus,
$$m(b - a) = m\sum(x_i - x_{i-1}) = \sum m(x_i - x_{i-1}) \le \sum m_i(x_i - x_{i-1}) \le \sum M_i(x_i - x_{i-1}) \le \sum M(x_i - x_{i-1}) = M\sum x_i - x_{i-1} = M(b - a).$$

