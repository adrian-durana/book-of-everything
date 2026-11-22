# STAT3004 Probability Models & Stochastic Processes: transcription, part 2 of 3 (HW 17–32)

_Transcription phase. Sources, legibility check and conventions: see `claude/notes-stat3004-1.md`._

**This part:** simple random variables and the construction of expectation, Jensen, Borel-measurable functions and LOTUS (with proof), modes of convergence with examples, characteristic functions and Lévy's continuity theorem, limits and expectations (counterexample, MCT, Fatou, reverse Fatou, DCT), weak and strong LLN, a.s. convergence via Borel–Cantelli, CLT. HW 32 is the last handwritten page.

---

### HW 17 (`20261122_012105.jpg`): Expectation (1)

**Expectation**

**Def.** Simple random variable
A random variable $X$ is simple if it takes finitely many values.
Alternatively,
$$X(\vect\omega) = \sum_{i=1}^n b_i\, I_{A_i}(\omega) \qquad \text{for constants } a_i \in \R \text{ and events } A_i \in \mathcal F \text{ partitioning } \mathcal F.$$
[possible error: (i) the coefficients are $b_i$ in the formula but "$a_i$" in the text; (ii) the $A_i$ partition $\Omega$, not $\mathcal F$ (CN Def 1.2.12). The $\omega$ on the left is underlined, on the right not.]

*Figure (a simple function):* a horizontal axis with tick marks dividing it into consecutive intervals labelled $A_1$, $A_2$, …, $A_n$ below (with "…" between $A_2$ and $A_n$); the symbol "$\mathcal F$" is written to the right of the axis [presumably meaning the axis represents the sample space]. Above each interval a short flat bar (a thin rectangle) at a different height: above $A_1$ at height $b_1$, above $A_2$ at height $b_2$, …, above $A_n$ at height $b_n$, each height marked by a double-headed vertical arrow from the axis to the bar labelled $b_1$, $b_2$, $b_n$. Between $A_2$ and $A_n$ three more bars at assorted heights (one high, two middling) stand for the intermediate values.

**Th.** Simple function approximation theorem
Any non-negative random variable can be expressed as the pointwise limit of some (non-decreasing) sequence of (non-negative) [one word crossed out] simple random variables. Alternatively, there exist simple random variables
$$0 \le X_1 \le X_2 \le \cdots \quad \text{such that} \quad X_n(\omega) \uparrow X(\omega) \quad \forall \omega \in \Omega.$$
["decreasing" is written above a crossed-out word after "non-". Stated without proof (CN Prop 1.2.14, also without proof).]

**Ex.** An explicit choice is the sum with $n^{\text{th}}$ element given by
$$X_n := \begin{cases} k/2^n & \dfrac{k}{2^n} \le X \le \dfrac{k+1}{2^n} \quad (\text{if } k \le n2^n)\\[6pt] n & \text{otherwise}\end{cases}$$
which truncates $X$ at level $n$ and discretises the remaining range into steps of size $2^{-n}$.
[possible error: the upper inequality should be strict, $k/2^n \le X < (k+1)/2^n$, and the range is $k = 0, \dots, n2^n - 1$ (CN Rem 1.2.15: $X_n = \sum_{k=0}^{n2^n-1} \frac{k}{2^n}\ind\{k/2^n \le X < (k+1)/2^n\} + n\ind\{X \ge n\}$). With "$\le$" at both ends the cases overlap at dyadic points.]

**Rem.** Note that $I_A(\omega)$ is itself a random variable, as $I_A^{-1}(\{1\}) = A \in \mathcal F$.

**Def.** General random variable
Suppose $X$ is a random variable. Then
$$X^+ := \max(X, 0) \quad\text{and}\quad X^- := \max(-X, 0)$$
are both non-negative random variables, with
$$X = X^+ - X^-, \qquad \abs{X} = X^+ + X^-$$

---

### HW 18 (`20261122_012110.jpg`): Expectation (2)

**Expectation**

**Def.** Expectation of indicator function
Given $(\Omega, \mathcal F, \Prob)$, let $X = I_A$. Then $\E[X] := \Prob(A)$
[Not a separate definition in CN (it is the case $k=1$ of Def 1.2.17).]

**Def.** Expectation of simple random variable
Let $X$ be a simple random variable. Then
$$\E[X] = \E\Bigl[\sum_i b_i I_{A_i}\Bigr] := \sum_i b_i \Prob(A_i)$$

**Def.** Expectation of non-negative random variable
Let $X \ge 0$ be a random variable. Define
$$\E[X] := \sup\{\E[s] : s \text{ simple},\ 0 \le s \le X\} \in [0, \infty]$$
Equivalently, if
$$\begin{cases} X_n \to X & \text{pointwise}\\ X_n \le X_{n+1} \end{cases}$$
then $\E[X] = \lim_{n\to\infty}\E[X_n]$.
[The $X_n$ are meant to be simple and non-negative (CN Def 1.2.20); the notes leave this to context.]

*Figure (approximating $X$ from below by simple functions):* a horizontal segment labelled "$\Omega$" below. Above it a smooth wavy curve labelled "$X$" at its right end (rising, dipping in the middle, rising again at the right). Under the curve two staircase (piecewise-constant) functions drawn with horizontal and vertical segments: a coarse one with a few wide steps lying well below the curve, labelled "$s$" at its right end, and a finer one with many narrow steps hugging the curve from just below. Both stay below the curve everywhere.

**Def.** Expectation of general random variable
Let $X$ be some general random variable, decomposed into $X = X^+ - X^-$.
If not both $\E[X^+]$ and $\E[X^-]$ are infinite, define
$$\E[X] := \E[X^+] - \E[X^-] \in [-\infty, \infty]$$

**Rem.** We also write the expectation as
$$\E[X] = \int_\Omega X \dd\Prob$$
(i.e. the Lebesgue integral of $X$ w.r.t. $\Prob$)

[CN Def 1.2.20 also defines "integrable" ($\E\abs X < \infty$); the notes don't.]

---

### HW 19 (`20261122_012116.jpg`): Expectation (3)

**Expectation**

**Th.** Properties of expectation
For constants $a, b \in \R$ and random variables $X, Y$ on a common probability space $(\Omega, \mathcal F, \Prob)$, we have
- (a) Linearity: $\E[aX + bY] = a\E X + b\E Y$
- (b) Monotone: $\underset{\text{(a.s.)}}{X \le Y} \implies \E[X] \le \E[Y]$
- (c) Jensen's inequality: let $\varphi$ be a convex function. Then $\varphi(\E[X]) \le \E[\varphi(X)]$

[The convex function is written with a glyph resembling "$\gamma$"/"$r$" everywhere except the first symbol of the proof's display, where it is a clear $\varphi$; transcribed as $\varphi$ throughout. CN Prop 1.2.28 assumes $X, Y$ integrable and has (c) $\abs{\E X} \le \E\abs X$ instead; Jensen is CN Thm 1.2.30 (with $X$ and $\varphi(X)$ integrable). The notes omit the integrability assumptions. Linearity and monotonicity are not proved in either source (CN Rem 1.2.29 sketches them).]

**P.** [of (c)] Since $\varphi$ is convex, there exists some $c \in \R$ such that
$$\varphi(x) \ge \varphi(\E[X]) + c(x - \E[X]) \qquad \forall x \in \R$$
Substitute $x = X(\omega)$, take expectations of both sides, and use the properties of linearity and monotonicity above:
$$\E[\varphi(X)] \ge \varphi(\E[X]) + c(\E[X] - \E[X])$$
and the result follows.

[The lower half of the page is blank.]

*Figure:* none.

---

### HW 20 (`20261122_012121.jpg`): Change of variables / LOTUS (1)

**Change of variables / LOTUS**

**Def.** Borel measurable function
A function $g : \R \to \R$ is Borel measurable if
$$g^{-1}(B) = \{x \in \R : g(x) \in B\} \in \mathcal B(\R) \qquad \forall B \in \mathcal B(\R)$$

*Figure (preimage under $g$):* two short diagonal lines (lower left to upper right), each labelled "$\R$" at its top. On the left line, a small marked segment (between two cross ticks) labelled "$g^{-1}(B)$" below it, with a hollow point $x$ in it. On the right line a marked segment labelled "$B$", with a point labelled "$g(x)$" above it. A curved arrow goes from the left line (from $x$) to the right line (to $g(x)$). A brace on the right: "Special case of random variable for $\mathcal B(\R)$" [i.e. $\Omega = \R$, $\mathcal F = \mathcal B(\R)$].
[Not a separate definition in CN (CN Thm 1.2.23 just says "Borel measurable").]

**Th.** Let $X : \Omega \to \R$ be a random variable on some $(\Omega, \mathcal F)$.
Let $g : \R \to \R$ be Borel-measurable. Then $g(X) : \Omega \to \R$ is a random variable.

*Figure (composition):* left, a rectangle labelled "$\Omega$" containing a hollow point $\omega$. Middle, a diagonal line labelled "$\R$" with a marked segment labelled "$g^{-1}(B)$" above it and a point labelled "$X(\omega)$" below it. Right, another diagonal line labelled "$\R$" with a marked segment labelled "$B$" above and a point labelled "$g(X(\omega))$" below. Curved arrows: rectangle → middle line (into $g^{-1}(B)$), middle line → right line (into $B$).

**P.** To show this, take $B \in \mathcal B(\R)$. As $g$ is Borel-measurable,
$$g^{-1}(B) \in \mathcal B(\R) \qquad (g^{-1}(B) \text{ is a Borel set})$$
and as $X$ is a random variable,
$$\{X \in g^{-1}(B)\} \in \mathcal F \implies \{g(X) \in B\} \in \mathcal F$$
which is equivalent to $g(X)$ being a random variable.
[Theorem and proof are not in CN (CN uses $g(X)$ in LOTUS without comment).]

**Th.** Change of variables / LOTUS
Let $X$ be a random variable on $(\Omega, \mathcal F, \Prob)$ with distribution $\mu_X$ on $(\R, \mathcal B(\R))$, and let $g : \R \to \R$ be Borel measurable. Then
$$\E[g(X)] = \int_\R g(x)\,\mu_X(\dd x)$$
[CN Thm 1.2.23 adds when the two sides are defined (both or neither; $g \ge 0$ or $g(X)$ integrable). ↔ STAT2003 LOTUS (Ch 27).]

---

### HW 21 (`20261122_012142.jpg`): LOTUS (proof) (1)

**LOTUS (proof)**

**Rem.** Motivation for LOTUS
Formally, the expectation of a Borel-measurable function of a random variable $X$ is defined by:
$$\E[g(X)] = \underbrace{\int_\Omega g(x) \dd\Prob}_{\text{hard to use}} = \underbrace{\int_\R g(x)\,\mu_X(\dd x)}_{\text{LOTUS, easy}}$$
where $\mu_X$ is the distribution measure of $X$:
$$\mu_X(B) = \Prob(X \in B)$$
For continuous random variables:
$$\mu_X(B) = \int_B \mu_X(\dd x), \qquad \mu_X(\dd x) = f(x)\dd x$$
For discrete random variables:
$$\mu_X(B) = \sum_{x_i \in B}\Prob(X = x_i), \qquad \mu_X(\dd x) = \sum_{x_i \in B}\Prob(X = x_i)\,\delta_{x_i}(\dd x)$$
where $\delta_{x_i}(\dd x)$ is the Dirac measure.
[possible error: the integrand over $\Omega$ should be $g(X(\omega))$, i.e. $\int_\Omega g(X)\dd\Prob$; and in the discrete $\mu_X(\dd x)$ the sum should run over all atoms $x_i$, not $x_i \in B$. The density and Dirac forms are in the notes only; CN Rem 1.2.24 gives the equivalent $\E[g(X)] = \int g\,f_X \dd x$ and $\sum_i g(x_i)p_i$.]

**P.** We prove LOTUS in increasing generality, starting with (I) indicator functions, (II) simple random variables, (III) non-negative random variables, and finally (IV) general random variables.

(I) Suppose $g(x) = I_B(x)$, $B \in \mathcal B(\R)$.
LHS: $\E[g(X)] = \E[I_B(X)] = \Prob(X \in B) = \mu_X(B)$
RHS: $\displaystyle \int_\R g(x)\,\mu_X(\dd x) = \int_B \mu_X(\dd x) = \mu_X(B)$
and so the two expressions are equivalent.

(II) Suppose $g(x) = \sum_{n=1}^N a_n I_{B_n}(x)$, $B_n \in \mathcal B(\R)$. Then,
$$
\begin{aligned}
\E[g(X)] &= \E\Bigl[\sum_{n=1}^N a_n I_{B_n}(X)\Bigr]\\
&= \sum_{n=1}^N a_n \E[I_{B_n}(X)] && \text{(linearity of expectation)}\\
&= \sum_{n=1}^N a_n \int_\R I_{B_n}(x)\,\mu_X(\dd x) && \text{(I)}\\
&= \int_\R \sum_{n=1}^N a_n I_{B_n}(x)\,\mu_X(\dd x) && \text{(linearity of integrals)}
\end{aligned}
$$
[continued on HW 22]
[The coefficients are written "$\alpha_n$"/"$a_n$" (a looped a); transcribed $a_n$. The $B_n$ are not said to partition $\R$ (CN Step 2 takes a partition). Throughout the proof the argument of $I_B$ is written "$(x)$" inside $\E[\cdot]$ where $X$ is meant; normalised to $X$ above.]

---

### HW 22 (`20261122_012146.jpg`): LOTUS (proof) (2)

**LOTUS (proof)**

**P.** (c) [= continued]
(II) Continuing from the previous page:
$$
\begin{aligned}
\E[g(X)] &= \int_\R \sum_{n=1}^N a_n I_{B_n}(x)\,\mu_X(\dd x)\\
&= \int_\R g(x)\,\mu_X(\dd x)
\end{aligned}
$$
and so the two expressions are equivalent.
[A short vertical stroke stands before the first $\E$ (a continuation mark).]

(III) Suppose $g \ge 0$. Let $g_n \uparrow g$ be an increasing sequence of simple RVs.
Then by monotone convergence,
$$
\begin{aligned}
&\E\bigl[\lim_{n\to\infty} g_n(X)\bigr] = \int_\R \lim_{n\to\infty} g_n(x)\,\mu_X(\dd x) && \text{(II)}\\
\iff\ &\E[g(X)] = \int_\R g(x)\,\mu_X(\dd x) && \text{(monotone convergence)}
\end{aligned}
$$
and so the two expressions are equivalent.
[possible error: (i) the $g_n$ are simple Borel functions on $\R$, not random variables; (ii) the step is compressed: (II) gives $\E[g_n(X)] = \int g_n \dd\mu_X$ for each $n$, and the MCT is then applied on both sides to pass to the limit (CN Step 3). As written, (II) is cited for an identity that already has the limit inside.]

(IV) Suppose $g$ is a general random variable. Then
$$g = g^+ - g^- = \max(g, 0) - \max(-g, 0)$$
and so
$$
\begin{aligned}
\text{LHS:}\quad \E[g(X)] &= \E[g^+(X)] - \E[g^-(X)] && \text{(linearity of expectation)}\\
&= \int_\R g^+(x)\,\mu_X(\dd x) - \int g^-(x)\,\mu_X(\dd x) && \text{(III)}\\
&= \int_\R \bigl(g^+(x) - g^-(x)\bigr)\,\mu_X(\dd x) && \text{(linearity of integral)}\\
\text{RHS:}\quad &= \int_\R g(x)\,\mu_X(\dd x)
\end{aligned}
$$
and so the two expressions are equivalent.
This concludes the proof.
[possible error: "$g$ is a general random variable" should be "a general Borel function"; the step needs $g(X)$ integrable (CN Step 4).]

*Figure:* none.

---

### HW 23 (`20261122_012204.jpg`): Convergence (1)

**Convergence**

**Def.** Convergence (sequences in $\R$)
Given $(x_n)_{n=1}^\infty$, $\lim_{n\to\infty} x_n = x$ iff
$$\forall \varepsilon > 0,\ \exists N \in \N : \forall n \ge N,\ \abs{x_n - x} < \varepsilon$$
[Not in CN.]

**Def.** Convergence (sequences of random variables)
Random variables have multiple modes of convergence. We will list these in decreasing order of strength.
(Let $X_1, \dots$ be RVs on $(\Omega, \mathcal F, \Prob)$) [a bracketed side note at the right]

**Def.** Pointwise convergence (sure convergence)
$(X_n)_{n=1}^\infty$ converges pointwise if
$$\forall \omega \in \Omega, \quad \lim_{n\to\infty} X_n(\omega) = X(\omega)$$
This is the notion of pointwise convergence of a sequence of functions, extended to a sequence of random variables.
[Not a named mode in CN §1.3.2.]

**Def.** Almost-sure convergence
$(X_n)_{n=1}^\infty$ converges almost surely if
$$\Prob\bigl(\lim_{n\to\infty} X_n = X\bigr) = 1$$
and we write $X_n \convas X$.

**Def.** Convergence in probability
$(X_n)_{n=1}^\infty$ converges in probability if
$$\forall \varepsilon > 0, \quad \lim_{n\to\infty}\Prob(\abs{X_n - X} \ge \varepsilon) = 0$$
and we write $X_n \xrightarrow{\Prob} X$.
[CN Def 1.3.5 uses $> \varepsilon$; the two are equivalent. Notation: the notes write $\xrightarrow{\Prob}$; the book's macro is $\convp$.]

**Def.** Convergence in mean ($L^p$ norm)
Let $X, X_1, \dots$ be random variables such that $\E[\abs{X_n}^p] < \infty$ and $\E[\abs X^p] < \infty$. Then $(X_n)_{n=1}^\infty$ converges in the $p^{\text{th}}$ mean if
$$\lim_{n\to\infty}\E[\abs{X_n - X}^p] = 0$$
and we write $X_n \xrightarrow{L^p} X$. If $p < q$, then $L^q \implies L^p$ convergence.
[CN Def 1.3.5 has $p \ge 1$ and doesn't state the finiteness assumptions; CN Rem 1.3.8 proves $L^q \Rightarrow L^p$ via Jensen. The notes give no proof.]

*Figure:* none.

---

### HW 24 (`20261122_012210.jpg`): Convergence (2)

**Convergence**

**Def.** Convergence in distribution (weak convergence, convergence in law)
Let $X, X_1, \dots$ be random variables with cdf $F, F_1, \dots$.
Then $(X_n)_{n=1}^\infty$ converges in distribution if
$$\lim_{n\to\infty} F_n(x) = F(x) \qquad \forall x \in \R \text{ where } F \text{ is continuous}$$
and we write $X_n \convd X$, or $X_n \xrightarrow{w} X$, or $X_n \Rightarrow X$.

**Th.** Comparing modes of convergence
$$
\begin{array}{ccccccc}
 & & & & & L^p & \\
 & & & & \swarrow\!\!\!\swarrow & & \searrow\!\!\!\searrow\\
\text{pointwise} & \Rightarrow & \text{a.s.} & \Rightarrow & \Prob & \Rightarrow & d/w
\end{array}
$$
*Figure (implication diagram):* the chain "pointwise ⇒ a.s. ⇒ $\Prob$ ⇒ d/w" on one line, with "$L^p$" above, between $\Prob$ and d/w; a double arrow ⇙ from $L^p$ down-left to $\Prob$ and a double arrow ⇘ from $L^p$ down-right to d/w. ["$\Prob$" = in probability; "d/w" = in distribution / weak.]

We will not prove each implication, but examples are provided below.
[CN Prop 1.3.7 states the same implications (without pointwise) and that none reverses in general; no proofs except $L^q \Rightarrow L^p$.]

**Ex.** Suppose $X_n \sim \Bern(1/n)$, $X = 0$. Then
(1) $X_n \xrightarrow{\Prob} X$ as
$$\underset{\substack{\rotatebox{90}{$\le$}\\ 0}}{\Prob(\abs{X_n - X} \ge \varepsilon)} = \Prob(X_n \ge \varepsilon) = \begin{cases} 0 & \varepsilon > 1\\ 1/n & 0 < \varepsilon \le 1\end{cases} \to 0$$
[Under "$\abs{X_n - X}$" the notes write "$\ge 0$" and under "$X$" "$= 0$" (vertical annotations).]

(2) $X_n \overset{\text{a.s.}}{\not\to} X$ as
$$\Prob(X_n = 1) =: \Prob(A_n) = \frac1n \implies \sum_{n=1}^\infty \Prob(A_n) = \sum_{n=1}^\infty \frac1n \to \infty$$
$$\implies \underset{\text{(Borel–Cantelli)}}{\Prob(A_n \text{ i.o.}) = 1} \implies \underset{\text{(definition of i.o.)}}{\limsup_{n\to\infty} X_n = 1 \text{ w.p. } 1} \implies X_n \not\to 0$$
[possible error: Borel–Cantelli II needs the $X_n$ (the events $A_n$) to be independent; the example doesn't say so. Not in CN.]

---

### HW 25 (`20261122_012221.jpg`): Convergence (3)

**Convergence**

**Ex.** Suppose $X \sim \Normal(0,1)$, $X_n = -X$ $\forall n \in \N$. Then
(1) $X_n \convd X$ as
$$X_n = -X \sim \Normal(0,1) \implies F_n \to F \text{ trivially}$$
(2) $X_n \overset{\Prob}{\not\to} X$ as
$$\forall \varepsilon > 0, \quad \Prob(\abs{X_n - X} \ge \varepsilon) = \Prob(\abs X \ge \varepsilon/2) \not\to 0$$
[Under "$X_n$" is written "$= -X$" and under "$\Prob(\abs X \ge \varepsilon/2)$" a "$> 0$" (vertical annotations). Not in CN.]

**Ex.** Let $U \sim \Unif[0,1]$. Suppose $X_n = \sqrt n\, I_{\{0 \le U \le 1/n\}}$, $X = 0$. Then
(1) $X_n \xrightarrow{\Prob} X$ as
$$
\begin{aligned}
\forall \varepsilon > 0, \quad \Prob(\abs{X_n - X} \ge \varepsilon) &= \Prob\bigl(\sqrt n\, I_{\{0 \le U \le 1/n\}} \ge \varepsilon\bigr) && \Big\}\ 0 \text{ if } U > 1/n\\
&\le \Prob(0 \le U \le 1/n) \to 0 && \Big\}\ 1/n \to 0
\end{aligned}
$$
(2) $X_n \overset{L^2}{\not\to} X$ as
$$\E[\abs{X_n - X}^2] = \E\bigl[n\, I_{\{0 \le U \le 1/n\}}\bigr] = n\,\Prob(0 \le U \le 1/n) = 1 \not\to 0$$
[Vertical annotations "$\ge 0$" and "$= 0$" under $\abs{X_n - X}$ and $X$, as on HW 24. Checked: correct. CN Rem 1.3.8 describes this kind of example in words only ($X_n = c_n \ind_{E_n}$ on $[0,1]$), for "$L^1 \not\Rightarrow L^2$"; this explicit $X_n$ is in the notes only.]

[The lower third of the page is blank.]

*Figure:* none.

---

### HW 26 (`20261122_012226.jpg`): Lévy's continuity theorem

**Lévy's continuity theorem**

**Def.** Characteristic function
Let $X$ be a random variable. Then the characteristic function is (equivalent to) the Fourier transform of the p.d.f. of $X$:
$$\varphi_X(t) = \E[e^{itX}]$$
An important property of $\varphi_X$ is that it determines the distribution of $X$ uniquely.
[Stated without proof, as in CN Rem 1.3.12.]

**Th.** Lévy's continuity theorem
Let $X, X_1, \dots$ be random variables with characteristic functions $\varphi, \varphi_1, \dots$. Then,
- (1) If $X_n \convd X$, $\varphi_n \to \varphi$ pointwise.
- (2) If $\varphi_n \to \varphi$ pointwise and $\varphi(t)$ is continuous at $t = 0$, [blotted] $X_n \convd X$.

[The blot before "$X_n$" in (2) covers one word (presumably "then"). possible error: in (2), $\varphi$ is only a pointwise limit, not assumed to be the characteristic function of a given $X$; the theorem's conclusion is that $\varphi$ is the characteristic function of some $X$ and $X_n \convd X$ (CN Thm 1.3.10). Stated without proof in both sources.]

**Rem.** Lévy's continuity theorem gives a purely analytic criterion for the probabilistic notion of convergence in distribution. This theorem also is useful in the classical proof of the central limit theorem.

**Ex.** Suppose $X_n \sim \Unif[-n, n]$. Then
$$
\varphi_n = \E[e^{itX_n}] = \frac{1}{2n}\int_{-n}^{n} e^{itx}\dd x
= \begin{cases} \dfrac{\sin(nt)}{nt} & t \ne 0\\[4pt] 1 & t = 0\end{cases}
\;\to\; \begin{cases} 0 & t \ne 0\\ 1 & t = 0\end{cases}
$$
and so the limit $\varphi$ is not continuous at $t = 0$.
Hence we cannot use Lévy's continuity theorem in this example.
["$\sin(nt)$": the $t$ is written like "+". Checked: correct. CN Rem 1.3.11 makes the same point with $X_n \sim \Normal(0, n)$ instead; this example is in the notes only.]

*Figure:* none.

---

### HW 27 (`20261122_012236.jpg`): Limits and expectations

**Limits and expectations**

**N.** Let $\{X_n\}_{n=1}^\infty$ be a sequence of random variables on $(\Omega, \mathcal F, \Prob)$ converging pointwise to $X$. Does it hold that
$$\E[X] = \E\bigl[\lim_{n\to\infty} X_n\bigr] \overset{?}{=} \lim_{n\to\infty}\E[X_n]\ ?$$
In general, this identity does NOT hold. A counterexample is given below.

**Ex.** Let $(\Omega, \mathcal F, \Prob) = ([0,1], \mathcal B[0,1], \lambda)$.
Suppose $X_n = n e^{-n\omega}$ for $\omega \in [0,1]$, $n \in \N$. Then
$$X(\omega) = \lim_{n\to\infty} X_n(\omega) = \begin{cases} 0 & 0 < \omega \le 1\\ \infty & \omega = 0\end{cases}$$
and the expectation of $X$ is
$$\E[X] = \E\bigl[\lim_{n\to\infty} X_n\bigr] = 0 \times \overset{1}{\Prob((0,1])} + \infty \times \overset{0}{\Prob(\{0\})} = 0$$
However, if we calculate individual expectations before taking limits:
$$\E[X_n] = \int_\Omega X_n \dd\Prob \overset{\ast}{=} \int_0^1 n e^{-n\omega}\dd\omega = 1 - e^{-n}$$
and taking the limit:
$$\lim_{n\to\infty}\E[X_n] = 1 - \lim_{n\to\infty} e^{-n} = 1 \ne \E[X].$$
Hence the limit of the expectation is not generally the expectation of the limit.
[The small "1" and "0" are written above $\Prob((0,1])$ and $\Prob(\{0\})$. The product $\infty \times 0$ is taken as $0$ (not stated). Checked: correct. Not in CN.]

**Rem.** ($\ast$) We justify why these two integrals are equivalent.
$$
\begin{aligned}
\int_\Omega X(\omega)\dd\Prob(\omega) &= \int_\Omega X \dd\Prob = \int_0^1 X \dd\Prob && \Big\}\ \text{integral w.r.t. probability}\\
\int_\Omega X(\omega)\dd\omega &= \int_0^1 X \dd\omega && \Big\}\ \text{integral w.r.t. length (ordinary)}
\end{aligned}
$$
Here, $\Prob = \lambda$, and so $\dd\Prob = \dd\lambda$. Conventionally, when integrating over a variable e.g. $\omega$ we write $\dd\omega$ in place of $\dd\lambda$.

[a hatched blot in the margin, then:]
**N.** Sufficient conditions on swapping limits and expectations.
For us to swap limits and expectations, there are two main conditions:
- (1) Monotone convergence theorem
- (2) Dominated convergence theorem

A sequence of random variable must satisfy one (or can satisfy both) to swap operations.
[The margin label before "N." is crossed out. The last sentence overstates it slightly (these are sufficient conditions, as the heading says); kept as written. The course guide §2.3 has the same point as a table (MCT, Fatou, DCT).]

*Figure:* none.

---

### HW 28 (`20261122_012240.jpg`): Limits and expectations: monotone convergence

**Limits and expectations: monotone convergence**

**Th.** Monotone convergence (MCT)
Let $\{X_n\}_{n=1}^\infty$ be a positive, monotone increasing sequence of random variables.
Let $X_n \convas X$. Then $\E[X_n] \to \E[X]$.

**Ex.** Suppose $Y_1, \dots$ is a sequence of non-negative random variables. Define:
$$X_n := \sum_{i=1}^n Y_i \quad \rightsquigarrow \quad \begin{cases} X_n \ge 0\\ X_n \le X_{n+1}\end{cases} \quad \forall n \in \N$$
By monotone convergence theorem,
$$
\begin{aligned}
&(1)\quad \lim_{n\to\infty} X_n = \lim_{n\to\infty}\sum_{i=1}^n Y_i := \sum_{i=1}^\infty Y_i \quad \text{exists}\\
&(2)\quad \lim_{n\to\infty}\E[X_n] = \lim_{n\to\infty}\E\Bigl[\sum_{i=1}^n Y_i\Bigr] = \lim_{n\to\infty}\sum_{i=1}^n \E[Y_i] \quad \text{exists}\\
&\qquad\qquad\qquad\ \ = \E\bigl[\lim_{n\to\infty} X_n\bigr] = \E\Bigl[\sum_{i=1}^\infty Y_i\Bigr] \quad \text{by MCT}
\end{aligned}
$$
[A "$\|$" (vertical equals sign) under $\lim\sum_{i=1}^n \E[Y_i]$ links it to "$\sum_{i=1}^\infty \E[Y_i]$" written beneath, so the conclusion is $\E[\sum_{i=1}^\infty Y_i] = \sum_{i=1}^\infty \E[Y_i]$. "(1) … exists" (in $[0,\infty]$) follows from monotonicity, not from the MCT; kept as written. Not in CN.]

**P.** An extended proof is given in the online supplementary notes.
[CN Thm 1.3.1 gives a proof sketch.]

[The lower half of the page is blank.]

*Figure:* none.

---

### HW 29 (`20261122_012249.jpg`): Limits and expectations: dominated convergence (1)

**Limits and expectations: dominated convergence**

**Th.** Fatou's lemma
Let $X_1, \dots$ be a sequence of non-negative random variables. Define
$$X(\omega) = \liminf_{n\to\infty} X_n(\omega)$$
Then
$$\E[X] \equiv \E\bigl[\liminf_{n\to\infty} X_n\bigr] \le \liminf_{n\to\infty}\E[X_n]$$

**P.** Let $Y_n = \inf_{k\ge n} X_k \ge 0$. Then $Y_n \uparrow \liminf_{n\to\infty} X_n$, so by MCT, $\E[Y_n] \to \E[\liminf_{n\to\infty} X_n]$. Since $Y_n \le X_k$ $\forall k \ge n$, we have that $\E[Y_n] \le \inf_{k\ge n}\E[X_k]$, so
$$\E\bigl[\liminf_{n\to\infty} X_n\bigr] = \lim_{n\to\infty}\E[Y_n] \le \liminf_{n}\ \inf_{k \ge n}\E[X_k] = \liminf_{n\to\infty}\E[X_n]$$
[In the last display the middle term is written "$\liminf_n \inf_{k\ge n}$" with the inf as a subscript "$k \ge n$" under liminf; CN has $\lim_n \inf_{k\ge n}\E[X_k]$.]

**Th.** Reverse Fatou's lemma
Let $X_1, \dots$ be a sequence of arbitrary random variables.
Let $Y$ be some non-negative random variable with $\E[Y] < \infty$ such that $X_n \le Y$ for all $n$, almost surely for $\omega \in \Omega$. Then define
$$X(\omega) = \limsup_{n\to\infty} X_n(\omega)$$
Then
$$\limsup_{n\to\infty}\E[X_n] \le [\text{blotted}]\ \E\bigl[\limsup_{n\to\infty} X_n\bigr] \equiv \E[X]$$
[A hatched blot (crossed-out symbol) between "$\le$" and "$\E$".]

**P.** Apply Fatou's lemma to the non-negative sequence $Y - X_n$:
$$\E\bigl[\liminf_{n\to\infty}(Y - X_n)\bigr] \le \liminf_{n\to\infty}\E[Y - X_n]$$
As $\E[Y] < \infty$, we have
$$\liminf_{n\to\infty}\E[Y - X_n] = \E[Y] - \limsup_{n\to\infty}\E[X_n]$$
Also note that $\liminf_{n\to\infty}(Y - X_n) = Y - \limsup_{n\to\infty} X_n$.
[a full line crossed out with hatching]
It follows that
$$\E[Y] - \E\bigl[\limsup_{n\to\infty} X_n\bigr] \le \E[Y] - \limsup_{n\to\infty}\E[X_n]$$
and the result follows.

*Figure:* none.

---

### HW 30 (`20261122_012254.jpg`): Limits and expectations: dominated convergence (2)

**Limits and expectations: dominated convergence**

**Th.** Dominated convergence (DCT)
Let $\{X_n\}_{n=1}^\infty$ be a sequence of random variables. Let $Y \ge 0$ be a random variable with finite expectation such that $\abs{X_n} \le Y$ almost surely.
Let $X_n \convas X$. Then $\E[X_n] \to \E[X]$.

**P.** Apply Fatou's lemma to the non-negative sequences $g + X_n \ge 0$ and $g - X_n \ge 0$:
$$
\begin{aligned}
(1)\quad \E[Y] + \E[X] &= \E\bigl[\liminf_{n\to\infty}(Y + X_n)\bigr]\\
&\le \liminf_{n\to\infty}\E[Y + X_n] = \E[Y] + \liminf_{n\to\infty}\E[X_n]\\
(2)\quad \E[Y] - \E[X] &= \E\bigl[\liminf_{n\to\infty}(Y - X_n)\bigr]\\
&\le \liminf_{n\to\infty}\E[Y - X_n] = \E[Y] - \limsup_{n\to\infty}\E[X_n]
\end{aligned}
$$
(1) gives $\E[X] \le \liminf_{n\to\infty}\E[X_n]$.
(2) gives $\limsup_{n\to\infty}\E[X_n] \le \E[X]$.
Hence $\liminf_{n\to\infty}\E[X_n] = \limsup_{n\to\infty}\E[X_n]$, that is, $\E[X_n] \to \E[X]$.
[possible error: the proof's first line says "$g + X_n$" and "$g - X_n$" (CN's name for the dominating variable) where the theorem calls it $Y$. In the last line the two "$\E[X_n]$" are written below hatched blots that cover the originals. CN Thm 1.3.4 also concludes that $X_n$, $X$ are integrable; and the chain "$\liminf = \limsup$" should end "$= \E[X]$".]

[The lower half of the page is blank.]

*Figure:* none.

---

### HW 31 (`20261122_012304.jpg`): Law of large numbers

**Law of large numbers**

**Th.** Weak law of large numbers
Let $X_1, \dots$ be i.i.d. with expectation $\mu$ and variance $\sigma^2 < \infty$.
Let $\bar X_n := \frac1n\sum_i X_i$. Then $\bar X_n \xrightarrow{\Prob} \mu$.

**P.** By independence, $\Var(\bar X_n) = \sigma^2/n$. By Chebyshev's inequality,
$$\Prob(\abs{\bar X_n - \mu} > \varepsilon) \le \frac{\Var(\bar X_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0$$
for all $\varepsilon > 0$, as $n \to \infty$.
[Chebyshev's inequality is not stated in the notes; it is CN Thm 1.3.15 (with Markov, Thm 1.3.14), both with proofs. ↔ STAT2003 (Ch 27, Ch 33).]

**Th.** Strong law of large numbers
Let $X_1, \dots$ be i.i.d. with expectation $\mu$ and variance $\sigma^2 < \infty$.
Let $\bar X_n := \frac1n\sum_i X_i$. Then $\bar X_n \convas \mu$.
[CN Thm 1.3.18 needs only $\E\abs{X_1} < \infty$; the notes' hypothesis (finite variance) is stronger, and the next paragraph mentions the $\E\abs X < \infty$ case.]

**P.** We demonstrate a proof idea under the additional condition of a finite fourth moment $\E[X^4] < \infty$. A moment computation shows that $\E[(\bar X_n - \mu)^4] = O(n^{-2})$, and so by Markov's inequality
$$\Prob(\abs{\bar X_n - \mu} > \varepsilon) \le \E[(\bar X_n - \mu)^4]/\varepsilon^4 = O(n^{-2})$$
By the following convergence theorem, we have $\bar X_n \convas \mu$.
The general proof ($\E[X] < \infty$ only) requires a more delicate truncation argument due to Kolmogorov, which we state without proof.
[The moment computation is not shown in either source. "$\E[X] < \infty$" should be $\E\abs{X_1} < \infty$ (CN Rem 1.3.21). The step $\sum_n n^{-2} < \infty$ is left implicit (CN states it).]

**Th.** Almost-sure convergence theorems
Let $X_1, \dots$ be random variables on $(\Omega, \mathcal F, \Prob)$, and for $\varepsilon > 0$ let $A_n(\varepsilon) = \{\abs{X_n - X} > \varepsilon\}$. Then
- (1) $\displaystyle \sum_{n=1}^\infty \Prob(A_n(\varepsilon)) < \infty \implies X_n \convas X$
- (2) $\displaystyle X_n \text{ ind.},\ \sum_{n=1}^\infty \Prob(A_n(\varepsilon)) = \infty \implies X_n \overset{\text{a.s.}}{\not\to} X$

[possible error: (1) needs the sum finite for every $\varepsilon > 0$; (2) needs it infinite for some $\varepsilon > 0$ (CN Thm 1.3.19). $X$ is not introduced in the hypothesis ("$X_1, \dots$" only).]

**P.** Both statements follow from the respective Borel–Cantelli lemmas, applied to the events $A_n(\varepsilon)$. Expressing the event $\{\lim_{n\to\infty} X_n = X\}$ in terms of limsup / liminf of the $A_n(\varepsilon)$ is the key step in relating almost sure convergence back to the infinitely-often language used for Borel–Cantelli.

*Figure:* none.

---

### HW 32 (`20261122_012309.jpg`): Central limit theorem

**Central limit theorem**

**Th.** Central limit theorem
Let $X_1, \dots$ be iid. with finite expectation $\mu$ and finite variance $\sigma^2$.
Let $S_n := \sum_i X_i$. Then
$$\frac{S_n - n\mu}{\sigma\sqrt n} \convd \Normal(0,1)$$
or equivalently, letting $\bar X_n := \frac1n\sum_i X_i$,
$$\sqrt n(\bar X_n - \mu) \convd \Normal(0, \sigma^2)$$
[No proof in the notes; CN Lecture theorem 1.3.22 gives a proof sketch via characteristic functions and Lévy's theorem, and requires $\sigma^2 \in (0,\infty)$ (the notes don't exclude $\sigma = 0$). ↔ STAT2003 CLT (Ch 33). The second form is in the notes only.]

[The rest of the page (about two thirds) is blank. This is the last handwritten page.]

*Figure:* none.

---
