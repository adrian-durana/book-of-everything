# STAT3001 Mathematical Statistics: transcription, part 2 of 3 (HW 29–56)

_Continuation of `claude/notes-stat3001-1.md` (sources, legibility check and conventions are there). Semester 1, 2026; no dates recorded._

**This part:** MLE theory (reasonableness, consistency, asymptotic efficiency, Slutsky-type theorem, delta method, misspecified models), the EM algorithm (formulation, exponential family, GEM, monotonicity, convergence, grouped and truncated data, truncated distributions), hypothesis testing (definitions, Neyman–Pearson lemma, LRT example, GLRT, Wilks' theorem, $t$-test examples, $\chi^2$ goodness of fit), multiple testing (FWER, Bonferroni, FDP, FDR, Benjamini–Hochberg), PPV, two-sample $t$-test, Satterthwaite's approximation, Tukey's studentised range.

---

### HW 29 (`20261122_011415.jpg`): MLE theory: reasonableness

**MLE theory: reasonableness** [top-right number "8"]

**Th.** Suppose $X_1,\dots,X_n$ are i.i.d. and that
1. The p.d.f. $f(\vect x;\vect\theta)$ are distinct with common support.
2. The space $\Omega$ contains an open region containing the true value $\vect\theta_0$ of the parameter $\vect\theta$.

Then for any $\vect\theta \ne \vect\theta_0$, as $n \to \infty$,
$$\Prob_{\vect\theta_0}\bigl[L(\vect\theta_0) > L(\vect\theta)\bigr] \to 1$$

**P.** We first show equivalence in inequalities:
$$
\begin{aligned}
L(\vect\theta_0) > L(\vect\theta) &\iff \frac1n\log\Bigl[\frac{L(\vect\theta)}{L_0(\vect\theta)}\Bigr] < 0\\
&\iff \frac1n\log\prod_j\frac{f(\vect x_j;\vect\theta)}{f(\vect x_j;\vect\theta_0)} < 0\\
&\iff \frac1n\sum_j\log\frac{f(\vect x_j;\vect\theta)}{f(\vect x_j;\vect\theta_0)} < 0
\end{aligned}
$$
We must show this inequality. By the law of large numbers,
$$\frac1n\sum_j\log\frac{f(\vect X_j;\vect\theta)}{f(\vect X_j;\vect\theta_0)} \xrightarrow{\ p\ } \E_{\vect\theta_0}\bigl[\log[f(\vect X;\vect\theta)/f(\vect X;\vect\theta_0)]\bigr]$$
It follows by Jensen's inequality that
$$
\begin{aligned}
\E_{\vect\theta_0}\Bigl[\log\Bigl[\frac{f(\vect X;\vect\theta)}{f(\vect X;\vect\theta_0)}\Bigr]\Bigr] &< \log\E_{\vect\theta_0}\Bigl[\frac{f(\vect X;\vect\theta)}{f(\vect X;\vect\theta_0)}\Bigr]\\
&= \log\int\frac{f(\vect x;\vect\theta)}{f(\vect x;\vect\theta_0)}f(\vect x;\vect\theta_0)\dd x\\
&= \log(1) = 0
\end{aligned}
$$
and the result follows.
[$L_0(\vect\theta)$ in the first line stands for $L(\vect\theta_0)$. The strict inequality in Jensen's inequality needs the ratio to be non-constant, which follows from condition 1 (distinct p.d.f.s); LN8 p. 3–4 says this, the notes do not.]

**Rem.** By this result, while $\vect\theta_0$ may be unknown or even unfindable, the MLE $\hat{\vect\theta}$ should be as close as findable to $\vect\theta_0$, and is hence a reasonable estimator.

**Rem.** This does not show that the MLE $\hat\theta$ is consistent — this is discussed in the following theorem.

*Figure:* none.

---

### HW 30 (`20261122_011420.jpg`): MLE theory: consistency

**MLE theory: consistency** [top-right number "8"]

**Th.** Suppose the conditions in the previous theorem hold. Suppose that $f(\vect x;\vect\theta)$ is differentiable with respect to $\vect\theta$ in the open region containing $\vect\theta_0$. Then with probability tending to one, as $n \to \infty$, the likelihood equation (given below by)
$$\frac{\partial\log L(\vect\theta)}{\partial\vect\theta} = \vect 0$$
has a sequence of roots that tends to $\vect\theta_0$ in probability.

**Rem.** There are three key remarks:
1. While this theorem establishes the existence of a consistent estimator sequence, we are still unsure on which root to choose to obtain said sequence.
2. The existence of a root is not asserted for all $\vect x_S = (\vect x_1\T,\dots,\vect x_n\T)\T$. This does not affect consistency, which only requires $\hat{\vect\theta}$ to be defined on some set $S_n$, the probability of which tends to one as $n \to \infty$.
3. While the likelihood function can have many roots, the consistent sequence of roots is (essentially) unique.

["the likelihood function can have many roots": the likelihood *equation* is meant.]

**P.** The proof is beyond the scope of this course.

*Figure:* none. [Lower 40% blank.]

---

### HW 31 (`20261122_011427.jpg`): MLE theory: asymptotic efficiency

**MLE theory: asymptotic efficiency** [top-right number "8"]

**Th.** Suppose $X_1,\dots,X_n$ are i.i.d. Under certain regularity conditions, any sequence of roots (consistent) $\hat\theta_n$ of the likelihood equation is both asymptotically normal and efficient, i.e.
$$\sqrt n(\hat\theta_n - \theta_0) \xrightarrow{\ \ell\ } \Normal\bigl(0,\ 1/i(\theta_0)\bigr)$$
["any sequence of roots (consistent)": any consistent sequence of roots (LN8 Theorem 5).]

**P.** The proof is beyond the scope of the course. A full outline is provided in the original lecture notes.
[The outline is LN8 pp. 6–8.]

**Rem.** The regularity conditions required are given here.
1. Support of $f$ does not depend on $\theta$.
2. $\Omega$ is an open interval
3. $f$ is thrice continuously differentiable w.r.t. $\theta$
4. The integral $\int\!\cdots\!\int f(x;\theta)\dd x$ can be twice differentiated under the integral sign.
5. $0 < \mathcal I(\theta) < \infty$
6. For any given $\theta_0 \in \Omega$, $\exists$ an open interval of $\theta_0$ and function $M(x)$, such that
$$\abs{\partial^3\log f(x;\theta)/\partial\theta^3} \le M(x)$$
for all $x \in A$, and such that $\E_{\theta_0}[M(X)] < \infty$.

These regularity conditions are identical to those needed for asymptotic efficiency, except to replace all third derivatives with second derivatives.
[$A$ (presumably the common support) is not defined; "for all $\theta$ in the interval" is not written. The last sentence is ambiguous: the conditions above *are* those for asymptotic efficiency; it presumably means the earlier (Cramér–Rao / HW 14) conditions are these with third derivatives replaced by second. Not resolved in the notes; compare LN8 "Regularity Conditions (II)" p. 6.]

*Figure:* none. [Lower third blank.]

---

### HW 32 (`20261122_011433.jpg`): Further theorems concerning asymptotic distributions

**Further theorems concerning asymptotic distributions** [top-right number "8"]

**Th.** If $Y_n \xrightarrow{\ \ell\ } Y$, and $a_n, b_n$ converge in probability to $a, b$, then
$$a_nY_n + b_n \xrightarrow{\ \ell\ } aY + b$$
[A short solid ink bar sits in the left margin above "Th." No name is given (this is Slutsky's theorem; LN8 Theorem 6 gives no name either).]

**P.** The proof is beyond the scope of this course. See Cramér. [The notes give the year of the reference; omitted under the no-dates rule.]

**Th.** *The delta method.* Suppose
$$\sqrt n(T_n - \theta) \xrightarrow{\ \ell\ } \Normal(0,\sigma^2)$$
Let $g$ be differentiable at $\theta$ with $g'(\theta) \ne 0$. Then
$$\sqrt n\bigl[g(T_n) - g(\theta)\bigr] \xrightarrow{\ \ell\ } \Normal\bigl(0,\ \sigma^2 g'(\theta)^2\bigr)$$

**P.** The proof is beyond the scope of this course. The idea behind it is a first-order Taylor expansion:
$$g(T_n) \approx g(\theta) + g'(\theta)(T_n - \theta)$$

*Figure:* none. [Lower 40% blank.]

---

### HW 33 (`20261122_011507.jpg`): MLE theory: estimation under incorrect model

**MLE theory: estimation under incorrect model** [top-right number "8"]

**Rem.** Let $X_1,\dots,X_n$ have true distribution function $f_0(x)$. Suppose that we use the incorrect model
$$\{f(x;\vect\theta) : \vect\theta \in \Omega\}$$
that is, $\hat{\vect\theta}$ maximises the likelihood
$$L(\theta) = \prod_j f(x_j;\vect\theta)$$
As $n \to \infty$:
$$\frac1n\log L(\theta) \xrightarrow{\ \text{a.s.}\ } \E_0[\log f(X;\theta)]$$
where
$$\E_0[\log f(X;\theta)] = \int f_0(x)\log f(x;\theta)\dd x$$
Let $\vect\theta_0$ maximise this value. Then $\vect\theta_0$ minimises the KL divergence between $f_0$ and $f$:
$$\mathrm{KL}[f_0 \,\|\, f] = \int f_0(x)\log\Bigl[\frac{f_0(x)}{f(x;\theta)}\Bigr]\dd x$$
Thus the incorrect MLE $\hat{\vect\theta}$ tends almost surely to $\vect\theta_0$, in terms of KL divergence.
[A hatched block crosses out something before $f_0(x)$ in the numerator. "distribution function $f_0$": a density is meant. The convergence of $\hat{\vect\theta}$ is stated, not proved (LN8 pp. 11–12).]

*Figure:* none. [Lower 40% blank.]

---

### HW 34 (`20261122_011513.jpg`): Introduction to EM algorithm

**Introduction to EM algorithm** [top-right number "10"]

**Def.** *EM algorithm background.* The expectation-maximisation (EM) algorithm is an iterative method to find local maximum likelihood estimates. It is especially useful when working with incomplete-data problems, including but not limited to missing data scenarios, truncated distributions, mixture models and convolutions. The key idea of the EM algorithm is to replace a potentially difficult incomplete-data problem with a simpler complete-data problem. As for the algorithm itself, it alternates between estimating data (E-step) and estimating parameters (M-step). EM is now a standard statistical tool.

**Def.** *EM algorithm formulation.* The EM algorithm is used as an iterative procedure for computing MLEs where maximum likelihood would be (relatively) straightforward if not for the absence of some additional data.

For data, let
- $\vect x \in \mathcal X$ denote complete / augmented data
- $\vect y \in \mathcal Y$ denote additional / unobservable / missing data
- $\vect z$ denote incomplete data

with $f_c(\vect x;\vect\theta)$ denoting the p.d.f. of $\vect X$, and $f$ denoting the incomplete-data p.d.f. of $\vect Y$. It follows that
$$f(\vect y;\vect\theta) = \int_{\mathcal X(\vect y)} f_c(\vect x;\vect\theta)\dd\vect x \qquad \text{where } \mathcal X(\vect y) \subseteq \mathcal X \text{ s.t. } \vect y = \vect y(\vect x)$$
[A curved double arrow joins the $\vect y$ and $\vect z$ lines with the note "swap!": the descriptions are to be exchanged, i.e. $\vect y$ = incomplete (observed) data and $\vect z$ = missing data, which matches the next sentence and LN10 p. 1. Recorded as written, with the author's own correction.]

The EM algorithm solves the incomplete-data likelihood equation indirectly by iterating on the complete-data log likelihood. As this is unobservable, it is replaced by its conditional expectation given $\vect y$, using the current fit for [blot] $\vect\theta$.

*Figure:* none.

---

### HW 35 (`20261122_011526.jpg`): EM Algorithm

**EM Algorithm** [top-right number "10"]

**Def.** *EM algorithm.* Let $\vect\theta^{(0)}$ be the initial value for $\vect\theta$. Then on the first iteration:
- E-step: $Q(\vect\theta;\vect\theta^{(0)}) = \E_{\vect\theta_0}\bigl[\log L_c(\vect\theta) \given \vect y\bigr]$
- M-step: max. $Q(\vect\theta;\vect\theta^{(0)})$ w.r.t. $\vect\theta$ over $\Omega$: choose $\vect\theta^{(1)}$ s.t. $Q(\vect\theta^{(1)};\vect\theta^{(0)}) \ge Q(\vect\theta;\vect\theta^{(0)})$

On the $(k+1)$th iteration:
- E-step: $Q(\vect\theta;\vect\theta^{(k)}) = \E_{\vect\theta^{(k)}}\bigl[\log L_c(\vect\theta) \given \vect y\bigr]$
- M-step: max. $Q(\vect\theta;\vect\theta^{(k)})$ w.r.t. $\vect\theta$ over $\Omega$: choose $\vect\theta^{(k+1)}$ s.t. $Q(\vect\theta^{(k+1)};\vect\theta^{(k)}) \ge Q(\vect\theta;\vect\theta^{(k)})$

Repeat until $L(\vect\theta^{(k+1)}) - L(\vect\theta^{(k)})$ is lower than some tolerance.
[The first E-step's subscript is written $\vect\theta_0$; $\vect\theta^{(0)}$ is meant. A stray mark in the left margin before "Def.". The iteration index is a handwritten $k$ (it can look like $h$). "for all $\vect\theta \in \Omega$" is implied in the M-step inequalities.]

**Rem.** Note it is not necessary to specify the mapping from $\mathcal X$ to $\mathcal Y$, nor the representation of incomplete-data density $f$ in terms of complete-data density $f_c$. It is only necessary that the specification of the complete-data vector $\vect x$ and the conditional density of $\vect X$ given observed-data $\vect y$. The choice of $\vect x$ is not unique, so can be chosen to speed convergence.
["It is only necessary that the specification …": sentence as written (a verb such as "be given" is missing).]

*Figure:* none. [Lower 30% blank.]

---

### HW 36 (`20261122_011531.jpg`): EM algorithm for regular exponential family

**EM algorithm for regular exponential family** [top-right number "10"]

**Def.** The complete-data p.d.f. is from an exponential family if
$$f_c(\vect x;\vect\theta) = b(\vect x)\exp\bigl\{\vect c(\vect\theta)\T\vect t(\vect x)\bigr\}/a(\vect\theta)$$
As the expectation of the score statistic is zero, we have
$$\mat J(\vect\theta)\,\E_{\vect\theta}[\vect t(\vect X)] = \nabla\vect c(\vect\theta)\T\,\E_{\vect\theta}[\vect t(\vect X)] = \frac{\partial\log a(\vect\theta)}{\partial\vect\theta}$$
and so
$$\frac{\partial\log f_c(\vect\theta)}{\partial\vect\theta} = \mat J(\vect\theta)\bigl(\vect t(\vect x) - \E_{\vect\theta}(\vect t(\vect X))\bigr) \qquad [1]$$
We also have that, ignoring terms not involving $\vect\theta$, that
$$Q(\vect\theta;\vect\theta^{(k)}) = \vect c(\vect\theta)\T\vect t^{(k)} - \log a(\vect\theta) \qquad [2]$$
where
$$\vect t^{(k)} = \E_{\vect\theta^{(k)}}\bigl[\vect t(\vect X) \given \vect y\bigr]$$
From differentiating [2] w.r.t. $\vect\theta$, and by [1], it follows that the M-step requires $\vect\theta^{(k+1)}$ to be chosen by solving
$$\mat J(\vect\theta)\bigl[\vect t^{(k)} - \E_{\vect\theta}[\vect t(\vect X)]\bigr] = 0$$
which is equivalent to
$$\E_{\vect\theta}[\vect t(\vect X)] = \vect t^{(k)} \implies \E_{\vect\theta^{(k+1)}}[\vect t(\vect X)] = \vect t^{(k)} \qquad [3]$$
If [3] is solvable for $\vect\theta^{(k+1)}$, then the solution is unique by the convexity of the log-likelihood. If it is not solvable, then the maximiser $\vect\theta^{(k+1)}$ lies on $\partial\Omega$.
[possible error: the complete-data log likelihood of a regular exponential family is *concave* in the natural parameter, which is what gives uniqueness; "convexity" as written (LN10 p. 6: "the complete-data log likelihood is concave"). "is from an exponential family": the result needs the *regular* exponential family, as the heading says. "equivalent to" uses $\mat J(\vect\theta)$ non-singular (HW 08).]

*Figure:* none. [Lower quarter blank.]

---

### HW 37 (`20261122_011539.jpg`): Generalised EM algorithm

**Generalised EM algorithm** [top-right number "10"]

**Def.** *Generalised EM algorithm background.* In practice, the solution to the M-step often exists in closed form. When it does not, finding
$$\vect\theta^{(k+1)} \in \argmax_{\vect\theta} Q(\vect\theta;\vect\theta^{(k)})$$
may be infeasible, or impossible to find a global maximiser.
[A small solid blot precedes $\vect\theta^{(k+1)}$. A stray "De" in the left margin (facing page).]

**Def.** *Generalised EM algorithm.* We modify the M-step such that:
$$\text{M-step: choose } \vect\theta^{(k+1)} \text{ s.t. } Q(\vect\theta^{(k+1)};\vect\theta^{(k)}) \ge Q(\vect\theta^{(k)};\vect\theta^{(k)})$$
In other words, we choose $\vect\theta^{(k+1)}$ to maximise $Q(\vect\theta;\vect\theta^{(k)})$ over its value at $\vect\theta = \vect\theta^{(k)}$, rather than maximising over all $\vect\theta \in \Omega$.
["to maximise … over its value at": i.e. to increase $Q$ above its value at $\vect\theta^{(k)}$.]

**Rem.** There are further extensions to the EM algorithm, namely the ECM (Expectation-Conditional Maximisation) and ECME algorithms. An overview of these algorithms is given in LN11. However, as they are non-examinable, they will not be mentioned in this notebook.
[ECME is not expanded in the notes (LN11 p. 3: Expectation–Conditional Maximization Either).]

*Figure:* none. [Lower 40% blank; the photo is slightly soft but all text reads.]

---

### HW 38 (`20261122_011546.jpg`): Monotonicity of EM algorithm

**Monotonicity of EM algorithm** [top-right number "10"]

**Th.** The incomplete-data likelihood function $L(\vect\theta)$ is not decreased after an EM iteration:
$$L(\vect\theta^{(k+1)}) \ge L(\vect\theta^{(k)})$$

**P.** Let $k$ be the conditional density of $\vect X$ given $\vect Y = \vect y$:
$$k(\vect x \given \vect y;\vect\theta) = f_c(\vect x;\vect\theta)/f(\vect y;\vect\theta)$$
Then the log-likelihood is given by
$$
\begin{aligned}
\log L(\vect\theta) &= \log f(\vect y;\vect\theta)\\
&= \log f_c(\vect x;\vect\theta) - \log k(\vect x \given \vect y;\vect\theta)\\
&= \log L_c(\vect\theta) - \log k(\vect x \given \vect y;\vect\theta)\\
&= \E_{\vect\theta^{(k)}}\bigl[\log L_c(\vect\theta) \given \vect y\bigr] - \E_{\vect\theta^{(k)}}\bigl[\log k(\vect X \given \vect y;\vect\theta) \given \vect y\bigr]
\end{aligned}
$$
[A hatched block crosses out something between "log" and $f_c$ in the second line. The density $k$ and the iteration index $k$ share a letter, as in LN10.]
We have that
$$\log L(\vect\theta^{(k+1)}) - \log L(\vect\theta^{(k)}) = \bigl[Q(\vect\theta^{(k+1)};\vect\theta^{(k)}) - Q(\vect\theta^{(k)};\vect\theta^{(k)})\bigr] - \bigl[H(\vect\theta^{(k+1)};\vect\theta^{(k)}) - H(\vect\theta^{(k)};\vect\theta^{(k)})\bigr]$$
where the first difference is non-negative by definition. Now,
$$
\begin{aligned}
H(\vect\theta;\vect\theta^{(k)}) - H(\vect\theta^{(k)} - \vect\theta^{(k)})
&= \E_{\vect\theta^{(k)}}\Bigl[\log\bigl[k(\vect X \given \vect y;\vect\theta)/k(\vect X \given \vect y;\vect\theta^{(k)})\bigr] \Bigm| \vect y\Bigr]\\
&\le \log\Bigl[\E_{\vect\theta^{(k)}}\bigl[k(\vect X \given \vect y;\vect\theta)/k(\vect X \given \vect y;\vect\theta^{(k)})\bigr] \Bigm| \vect y\Bigr]\\
&= \log\int_{\mathcal X(\vect y)} k(\vect x \given \vect y;\vect\theta)\dd\vect x = 0
\end{aligned}
$$
and so the likelihood $L(\vect\theta)$ monotonically increases.
[$H(\vect\theta;\vect\theta^{(k)}) = \E_{\vect\theta^{(k)}}[\log k(\vect X \given \vect y;\vect\theta) \given \vect y]$ is used but not defined (LN10 (22)). "$H(\vect\theta^{(k)} - \vect\theta^{(k)})$" should be $H(\vect\theta^{(k)};\vect\theta^{(k)})$. In the last line a hatched block crosses out part of the integrand ($k(\vect x \given \vect y;\vect\theta)$ is written above it). A stray "$\$$"-like mark sits in the first $k(\vect X \given \vect y\,;\dots)$. "monotonically increases" means "does not decrease".]

**Rem.** A corollary is the self-consistency of the EM algorithm. If the MLE $\hat{\vect\theta}$ globally maximises $L(\vect\theta)$, $Q(\hat{\vect\theta};\hat{\vect\theta}) \ge Q(\vect\theta;\hat{\vect\theta})$.

*Figure:* none.

---

### HW 39 (`20261122_011603.jpg`): Convergence of EM algorithm

**Convergence of EM algorithm** [top-right number not visible (top-right corner cut off at the page edge)]

**Def.** *EM algorithm convergence.* For a sequence of likelihood values $\{L(\vect\theta^{(k)})\}$ bounded above, it converges monotonically to some $L^*$. This $L^*$ is usually a stationary value, that is,
$$\frac{\partial L(\vect\theta)}{\partial\vect\theta}\bigg|_{\vect\theta=\vect\theta^*} = \vect 0 \implies \frac{\partial\log L(\vect\theta)}{\partial\vect\theta}\bigg|_{\vect\theta=\vect\theta^*} = \vect 0$$
In many practical applications, $L^*$ is a local maximum. If $L(\vect\theta)$ has several stationary points, the convergence of the EM sequence to either a local / global maximum or saddle point depends on the initial iterate $\vect\theta^{(0)}$.
[LN10 writes "or equivalently" between the two conditions; the notes use $\implies$.]

**Def.** *Regularity conditions of Wu.* These conditions ensure that all limit points of any instance of the EM algorithm are local maximisers of $L(\vect\theta)$, and that $L(\vect\theta^{(k)})$ converges monotonically to $L^* = L(\vect\theta^*)$ for some local maximiser $\vect\theta^*$. We have:
1. $\sup_{\vect\theta\in\Omega} Q(\vect\theta;\vect\theta^*) > Q(\vect\theta^*;\vect\theta^*)$
2. $\Omega \subseteq \R^d$
3. $\Omega_{\vect\theta_0} = \{\vect\theta \in \Omega : L(\vect\theta) > L(\vect\theta_0)\}$ is compact
4. $L(\vect\theta)$ is continuous on $\Omega$ and differentiable on $\operatorname{int}(\Omega)$.
5. $\Omega_{\vect\theta_0} \subseteq \operatorname{int}(\Omega)$ $\forall\,\vect\theta_0 \in \Omega$

Additional details are provided in LN10.
[possible error, compare LN10 (34)–(36): condition 1 is required "for any stationary point $\vect\theta^*$ that is not a local maximiser of $L$", which the notes omit; in condition 3 the set is $\{L(\vect\theta) \ge L(\vect\theta_0)\}$ and compactness is required for any $L(\vect\theta_0) > -\infty$. In condition 5 the "$\subseteq$" is written above a small blot. A finger is visible at the left edge of the photo; it covers no writing.]

*Figure:* none. [Lower 20% blank.]

---

### HW 40 (`20261122_011608.jpg`): EM algorithm for grouped and truncated data (background)

**EM algorithm for grouped and truncated data (background)** [top-right number "12"]

**Def.** We consider applying the EM algorithm to continuous data grouped into intervals. Let $W$ have p.d.f. $f(w;\vect\theta)$ where $\vect\theta$ is unknown. Suppose the sample space $\mathcal W$ of $W$ is partitioned into disjoint intervals $\mathcal W_j$. We observe independent samples of $W$, but only the frequencies in each interval $n_j$ are recorded, for $j = 1,\dots,r$ where $r \le v$. For $j > r$, observations may be unknown due to truncation.
[$v$ (the number of intervals, $j = 1,\dots,v$) is not defined on the page (LN12 p. 1).]

The observed data vector $\vect y = (n_1,\dots,n_r)\T$ follows a multinomial distribution with probabilities
$$\frac{P_j(\vect\theta)}{P(\vect\theta)} \qquad \text{where } P_j(\vect\theta) = \int_{\mathcal W_j} f(w;\vect\theta)\dd w, \quad P(\vect\theta) = \textstyle\sum_j^r P_j(\vect\theta)$$
Hence the incomplete-data log-likelihood is
$$\log L(\vect\theta) = \textstyle\sum_j^r n_j\log\bigl[P_j(\vect\theta)/P(\vect\theta)\bigr] + \log\Bigl[n!\Big/\prod_j^r n_j!\Bigr]$$
[$P_j$ and $P$ are written with a blackboard-bold $\mathbb P$ except in the first fraction; they are probabilities of intervals, not the probability measure. $n = \sum_{j=1}^r n_j$ is not defined on the page.]

To apply EM, we introduce missing data:
- $\vect u = (n_{r+1}, n_{r+2},\dots,n_v)\T$: unobserved frequencies (by truncation)
- $\vect w_j = (w_{j1}, w_{j2},\dots,w_{j,n_j})\T$: unobservable indiv. observations within interval $\mathcal W_j$

Thus the complete-data vector is
$$\vect x = (\vect y\T, \vect u\T, \vect w_1\T,\dots,\vect w_v\T)\T$$
and the complete-data log-likelihood is
$$\log L_c(\vect\theta) = \textstyle\sum_j^v\sum_\ell^{n_j}\log f(w_{j\ell};\vect\theta)$$
[A hatched block crosses out something between "$f$" and "$(w_{j\ell};\vect\theta)$".]

To ensure consistency with the observed likelihood, we have that within each interval $\mathcal W_j$ that
$$h_j(w;\vect\theta) = \frac{f(w;\vect\theta)}{P_j(\vect\theta)}$$
Therefore, conditioned on being in $\mathcal W_j$, observations are i.i.d. from $h_j$. The missing frequencies $\vect u$ are given a conditional distribution:
$$d(\vect u \given \vect y;\vect\theta) = c_2\,P(\vect\theta)^n\prod_{j=r+1}^{v}\bigl(P_j(\vect\theta)\bigr)^{n_j}$$
and this defines a prob. function if $c_2 = (m+n-1)!\Big/\Bigl((n-1)!\prod_{j=r+1}^v n_j!\Bigr)$.
[A hatched block crosses out a symbol after the product sign. $m = \sum_{j=r+1}^v n_j$ (the number of truncated observations) is not defined on the page (LN12 p. 2).]

*Figure:* none.

---

### HW 41 (`20261122_011634.jpg`): EM algorithm for grouped and truncated data

**EM algorithm for grouped and truncated data** [top-right number "12"]

**Def.** *E and M steps for grouped and truncated data.* Recall the complete-data log-likelihood for $\vect\theta$:
$$\log L_c(\vect\theta) = \textstyle\sum_j^v\sum_\ell^{n_j}\log f(w_{j\ell};\vect\theta)$$
The expectation of this conditional on $\vect y$ is given by
$$Q(\vect\theta;\vect\theta^{(k)}) = \textstyle\sum_j^v n_j^{(k)}\,Q_j(\vect\theta;\vect\theta^{(k)})$$
where
$$Q_j(\vect\theta;\vect\theta^{(k)}) = \E_{\vect\theta^{(k)}}\bigl[\log f(W;\vect\theta) \given W \in \mathcal W_j\bigr]$$
$$n_j^{(k)} = \begin{cases} n_j & j = 1,\dots,r\\ \E_{\vect\theta^{(k)}}(n_j \given \vect y) & j = r+1,\dots,v\end{cases}
= \begin{cases} n_j & j = 1,\dots,r\\ n\,P_j(\vect\theta^{(k)})/P(\vect\theta^{(k)}) & j = r+1,\dots,v\end{cases}$$
[In the first display the second argument of $Q_j$ is written "$\vect\theta^k$" (no brackets).]

Thus using EM replaces the contribution of each interval by the conditional expectation of the log-density over that interval, rather than using midpoint approximations.
For the M-step, we have that $\vect\theta^{(k+1)}$ is a root of
$$\frac{\partial Q(\vect\theta;\vect\theta^{(k)})}{\partial\vect\theta} = \textstyle\sum_j^v n_j^{(k)}\dfrac{\partial Q_j(\vect\theta;\vect\theta_k)}{\partial\vect\theta}$$
where
$$\frac{\partial Q_j}{\partial\vect\theta} = \E_{\vect\theta^{(k)}}\Bigl[\frac{\partial\log(f(W;\vect\theta))}{\partial\vect\theta} \Bigm| W \in \mathcal W_j\Bigr]$$
[$\vect\theta_k$ in the first display is $\vect\theta^{(k)}$.]

**Def.** *M-step for grouped and truncated normal data.* Suppose that $f(w;\vect\theta) = \phi(w;\mu,\sigma^2)$. Then,
$$Q(\vect\theta;\vect\theta^{(k)}) = -\tfrac12\Bigl(n + \textstyle\sum_{j=r+1}^v n_j^{(k)}\Bigr)\bigl(\log(2\pi) + \log\sigma^2\bigr) - \tfrac12\sigma^{-2}\textstyle\sum_{j=1}^v n_j^{(k)}\,\E_{\vect\theta^{(k)}}\bigl[(W-\mu)^2 \given W \in \mathcal W_j\bigr]$$
and that the maximiser $\vect\theta^{(k+1)}$ is given by
$$\mu^{(k+1)} = \textstyle\sum_{j=1}^v n_j^{(k)}\,\E_{\vect\theta^{(k)}}[W \given W \in \mathcal W_j]\Big/\sum_{j=1}^v n_j^{(k)}$$
$$\sigma^{2\,(k+1)} = \textstyle\sum_{j=1}^v n_j^{(k)}\,\E_{\vect\theta^{(k)}}\bigl[(W - \mu^{(k+1)})^2 \given W \in \mathcal W_j\bigr]\Big/\sum_{j=1}^v n_j^{(k)}$$
[$\phi(w;\mu,\sigma^2)$ = normal density (symbol written as a slashed "Ø"). Compare LN12 §1.3.]

*Figure:* none.

---

### HW 42 (`20261122_011640.jpg`): Distributions of truncated random variables

**Distributions of truncated random variables** [top-right number "13"]

**Th.** Let $V$ be a random variable with density $f$. Suppose $V$ is truncated so that the support is restricted to $R \subseteq \Omega$. Then
$$f(v \given V \in R) = \frac{f(v)\,\ind_{[R]}(v)}{\int_R f(v)\dd v}$$

**P.** Let $A$ denote the set that $V$ is in $R$, and $A_v$ the set that $V = v$. Then,
$$f(v \given V \in R) = \Prob[V = v \given V \in A] = \frac{\Prob[A_v \cap A]}{\Prob[A]}$$
The probability of $A_v \cap A$ is equal to $A_v$ if $v \in A$, and is zero otherwise. Therefore, we have that
$$f(v \given V \in R) = \frac{\Prob[A_v]\,\ind_{[R]}(v)}{\int_R f(v)\dd v}$$
and the result follows.
[possible error: the argument treats the density as a probability ($\Prob[V = v]$), which is valid for a discrete $V$; LN13 p. 1 says it proves the discrete case and that the proof "carries over" to the continuous case, which the notes do not mention. "$V \in A$" should be "$V \in R$" ($A$ is the event), and "equal to $A_v$" means "equal to $\Prob[A_v]$". The dummy variable of integration is the same $v$ as the argument, as written.]

**Def.** The conditional expectation of some function $a$ of $V$ is given by
$$
\begin{aligned}
\E[a(V) \given V \in R] &= \int a(v)\,f(v \given V \in R)\dd v\\
&= \frac{\int a(v)f(v)\ind_{[R]}(v)\dd v}{\int_R f(v)\dd v}\\
&= \frac{\int_R a(v)f(v)\dd v}{\int_R f(v)\dd v}
\end{aligned}
$$
[The function is written "$a$" (first occurrence looks like "$\alpha$"). The indicator is written $\mathbb 1_{[R]}$ (double-struck 1).]

*Figure:* none. [Lower quarter blank.]

---

### HW 43 (`20261122_011654.jpg`): Introduction to hypothesis testing

**Introduction to hypothesis testing** [top-right number "14"]

**Def.** *Hypothesis tests.* A hypothesis test is a decision rule that specifies when to reject the null hypothesis $H_0$ in favour of the alternative hypothesis $H_1$. We can construct many hypothesis tests on the same scenarios.

**Def.** *P-values.* A p-value is the probability that we obtain a test statistic as extreme or more extreme than the observed one, under the null hypothesis $H_0$.

**Def.** *Type I error, significance level.* Type I error is rejecting the null $H_0$ when it is actually true. The probability of a Type I error is
$$\alpha = \Prob(\text{reject } H_0 \given H_0 \text{ true}) = \int_R L(\vect\theta_0;\vect x_S)\dd\vect x_S \qquad \Big\}\ R \text{ is critical region},\ L(\vect\theta;\vect x_S) = \textstyle\prod_i f(x_i;\vect\theta)$$

**Def.** *Type II error, power.* Type II error is accepting (failing to reject) $H_0$ when it is false. The probability of a Type II error is
$$\beta = \Prob(\text{reject } H_1 \given H_1 \text{ true}) = \int_{\bar R} L(\vect\theta_1;\vect x_S)\dd\vect x_S$$
The power of a test is the probability of correctly rejecting $H_0$:
$$\pi = \Prob(\text{reject } H_0 \given H_1 \text{ true}) = 1 - \beta$$
[$\bar R$ = complement of the critical region. $\vect x_S$ is the full sample $(\vect x_1\T,\dots,\vect x_n\T)\T$, as on HW 30. "reject $H_1$" = fail to reject $H_0$.]

*Figure:* none. [Lower quarter blank.]

---

### HW 44 (`20261122_011658.jpg`): Neyman–Pearson lemma

**Neyman–Pearson lemma** [top-right number "14"]

**N.** In practice, we want a test that
- restricts significance level $\alpha$ to some small $\alpha$
- maximises power $\pi = 1 - \beta$.

Such a test exists and is unique, by the Neyman–Pearson lemma.

**Def.** *Likelihood ratio test.* Reject $H_0: \vect\theta = \vect\theta_0$ in favour of $H_1: \vect\theta = \vect\theta_1$ if
$$\frac{L(\vect\theta_1;\vect x_S)}{L(\vect\theta_0;\vect x_S)} > k$$
where the constant $k$ determines $\alpha$.
[The subscript in the numerator is written over a blot; $\vect\theta_1$ is meant. Note the ratio is alternative over null, the reverse of the STAT2004 notes.]

**Def.** *Neyman–Pearson lemma.* Among all tests with significance $\alpha$, the likelihood ratio test has highest power.

**P.** Let $R^*$ be the critical region of any other test of $H_0$ vs. $H_1$ having significance level $\alpha$. We show that the power of this test is always less than the likelihood ratio test.

In this proof we use the properties:
$$R = (R \cap R^*) \cup (R \cap \bar R^*) \qquad R^* = (R^* \cap R) \cup (R^* \cap \bar R)$$
We have:
$$
\begin{aligned}
\pi(R) - \pi(R^*) &= \int_R L(\vect\theta_1;\vect x_S)\dd\vect x_S - \int_{R^*} L(\vect\theta_1;\vect x_S)\dd\vect x_S\\
&= \int_{R\cap\bar R^*} L(\vect\theta_1;\vect x_S)\dd\vect x_S - \int_{\bar R\cap R^*} L(\vect\theta_1;\vect x_S)\dd\vect x_S\\
&> k\int_{R\cap\bar R^*} L(\vect\theta_0;\vect x_S)\dd\vect x_S - k\int_{\bar R\cap R^*} L(\vect\theta_1;\vect x_S)\dd\vect x_S\\
&= \int_R k\,L(\vect\theta_0;\vect x_S)\dd\vect x_S - \int_{R^*} k\,L(\vect\theta_0;\vect x_S)\dd\vect x_S\\
&= k\alpha - k\alpha = 0
\end{aligned}
$$
and the result follows.
[possible error: in the third line the second integrand should be $L(\vect\theta_0;\vect x_S)$ (checked on a zoomed crop: it is written $\vect\theta_1$); the next line has $\vect\theta_0$. The inequality should be "$\ge$" (on $R\cap\bar R^*$, $L_1 > kL_0$; on $\bar R\cap R^*$, $L_1 \le kL_0$), so the conclusion is $\pi(R) \ge \pi(R^*)$, "no less", not "always less … than". "exists and is unique" is as written; uniqueness is not proved.]

*Figure:* none.

---

### HW 45 (`20261122_011718.jpg`): Likelihood ratio test (example)

**Likelihood ratio test (example)** [top-right number "14"]

**Ex.** Suppose $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$, where $\sigma^2$ is known. Suppose we are testing $H_0: \mu = \theta_0$ vs. $H_1: \mu = \theta_1$. The likelihood function for normal data is:
$$L(\theta;\vect x_S) = (2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp\Bigl\{-\frac{1}{2\sigma^2}\textstyle\sum_j(x_j - \theta)^2\Bigr\}$$
and so the LRT statistic is
$$\frac{L(\theta_1;\vect x_S)}{L(\theta_0;\vect x_S)} = \frac{e^{-\frac{1}{2\sigma^2}\sum(x_i-\mu_1)^2}}{e^{-\frac{1}{2\sigma^2}\sum(x_i-\mu_0)^2}} = \exp\Bigl\{\frac{1}{2\sigma^2}\Bigl(\textstyle\sum(x_i-\mu_0)^2 - \sum(x_i-\mu_1)^2\Bigr)\Bigr\}$$
The critical region is equivalent to
$$\theta_1 > \theta_0: \{\vect x_S : \bar x > k\} \quad\text{or}\quad \theta_1 < \theta_0: \{\vect x_S : \bar x < k\}$$
We now find $k$. Suppose $\theta_1 > \theta_0$. Then,
$$
\begin{aligned}
\alpha &= \Prob[\bar X > k \given H_0]\\
&= \Prob\Bigl[\frac{\bar X - \theta_0}{\sigma/\sqrt n} > \frac{k - \theta_0}{\sigma/\sqrt n}\Bigr]\\
&= \Prob\Bigl[Z > \frac{k - \theta_0}{\sigma/\sqrt n}\Bigr]\\
&= \Phi\Bigl(-\frac{k - \theta_0}{\sigma/\sqrt n}\Bigr)
\end{aligned}
$$
and so we have
$$k = \theta_0 - \Phi^{-1}(\alpha)\,\sigma/\sqrt n$$
[The notes switch between $\theta_0,\theta_1$ and $\mu_0,\mu_1$ for the same values, and reuse $k$ for the cut-off on $\bar x$ (a different constant from the $k$ in the LRT). Checked: the formula for $k$ is correct.]

**Rem.** A test is uniformly most powerful if it is most powerful in testing $H_0: \theta = \theta_0$ versus $H_1: \theta = \theta_1$ for all $\theta_1 \in \Omega_{H_1}$. One-sided tests can be UMP, but two-sided tests cannot.

*Figure:* none. [Lower quarter blank.]

---

### HW 46 (`20261122_011722.jpg`): Generalised likelihood ratio test, Wilks' theorem

**Generalised likelihood ratio test, Wilks' theorem** [top-right number "14"]

**Def.** *Generalised likelihood ratio test.* Reject $H_0: \vect\theta = \vect\theta_0$ if
$$\lambda = \frac{\sup_{\vect\theta\in\Omega_{H_0}} L(\vect\theta;\vect x_S)}{\sup_{\vect\theta\in\Omega} L(\vect\theta;\vect x_S)}$$
is sufficiently small. If this ratio $\lambda$ is small, the data is more likely observed under the alternative compared to the null.
[The null is written as a point hypothesis but the numerator takes the supremum over $\Omega_{H_0}$ (general composite null); the denominator is over the full space $\Omega$, as in LN14, not over the alternative only.]

**Def.** *Wilks' theorem.* Suppose $\lambda$ is the GLRT statistic. Then for samplesize large enough
$$-2\log\lambda \sim \ChiSq{d} \qquad d = \dim(\Omega) - \dim(\Omega_{H_0})$$
where we reject $H_0$ when
$$-2\log\lambda > \chi^2_{d,1-\alpha}$$
[Labelled "Def." although it is a theorem. "$\sim$" is approximate (under $H_0$, regularity conditions not stated). $\chi^2_{d,1-\alpha}$ = the $1-\alpha$ quantile of $\ChiSq d$.]

**P.** Suppose that $\theta$ is a scalar parameter. The proof for vector parameters generalises similarly (but not as trivially). We have that
$$\dim\{\Omega_{H_0}\} = 0 \quad\text{and}\quad \dim\{\Omega\} = 1 \implies d = 1$$
and so we must show $-2\log\lambda \sim \ChiSq1$. Expand the log-likelihood using a Taylor expansion:
$$
\begin{aligned}
\log L(\theta_0;\vect x_S) &= \log L(\hat\theta;\vect x_S) + (\theta_0 - \hat\theta)\frac{\partial\log L(\hat\theta;\vect x_S)}{\partial\theta} + \frac12(\theta_0 - \hat\theta)^2\frac{\partial^2\log L(\hat\theta;\vect x_S)}{\partial\theta^2}\\
&= \log L(\hat\theta;\vect x_S) - \frac12(\theta_0 - \hat\theta)^2 I(\theta)
\end{aligned}
$$
and therefore
$$-2\log\lambda = 2\bigl[\log L(\hat\theta;\vect x_S) - \log L(\theta_0;\vect x_S)\bigr] \approx (\hat\theta - \theta_0)^2 I(\hat\theta)$$
which is distributed approximately under $H_0$ as a $\ChiSq1$ variate as
$$\hat\theta \sim \Normal\bigl(\theta_0,\ 1/\mathcal I(\theta)\bigr)$$
[The Taylor expansion is truncated, so the "$=$" signs are "$\approx$"; the first-order term vanishes because the score is $0$ at $\hat\theta$, not stated; the second line writes $I(\theta)$ where $I(\hat\theta)$ (observed information) is meant (next line). The last step also uses $I(\hat\theta)/\mathcal I(\theta_0) \to 1$, not stated; the information symbols are told apart here as on HW 13. Compare LN14 pp. 12–13.]

*Figure:* none.

---

### HW 47 (`20261122_011729.jpg`): Generalised likelihood ratio test (example, two-sided)

**Generalised likelihood ratio test (example)** [top-right number "14"]

**Ex.** Suppose $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$, where now $\sigma^2$ is unknown. Suppose we are testing $H_0: \mu = \mu_0$ vs. $H_1: \mu \ne \mu_0$. The GLRT is given by
$$\lambda = \frac{L(\hat{\hat{\vect\theta}};\vect x_S)}{L(\hat{\vect\theta};\vect x_S)} \qquad \text{where } \hat{\hat{\vect\theta}} \text{ is MLE under } H_0,\ \hat{\vect\theta} \text{ is MLE unconstrained}$$
It can be verified that
$$\hat{\hat\mu} = \mu_0, \quad \hat{\hat\sigma}^2 = \frac1n\textstyle\sum_j(x_j - \mu_0)^2 \qquad\qquad \hat\mu = \bar x, \quad \hat\sigma^2 = \frac1n\sum_j(x_j - \bar x)^2$$
and so
$$
\begin{aligned}
L(\hat{\vect\theta};\vect x_S) &= (2\pi)^{-n/2}(\hat\sigma^2)^{-n/2}e^{-\frac12\sum_i(x_i - \bar x)^2/\hat\sigma^2} = (2\pi)^{-n/2}(\hat\sigma^2)^{-n/2}e^{-n/2}\\
L(\hat{\hat{\vect\theta}};\vect x_S) &= (2\pi)^{-n/2}(\hat{\hat\sigma}^2)^{-n/2}e^{-\frac12\sum_i(x_i - \mu_0)^2/\hat{\hat\sigma}^2} = (2\pi)^{-n/2}(\hat{\hat\sigma}^2)^{-n/2}e^{-n/2}
\end{aligned}
$$
and thus $\lambda = (\hat\sigma^2/\hat{\hat\sigma}^2)^{n/2}$. Now we can express
$$\hat{\hat\sigma}^2 = \frac1n\textstyle\sum_i(x_j - \mu_0)^2 = \frac1n\sum_i(x_j - \bar x + \bar x - \mu_0)^2 = \frac1n\sum_i(x_j - \bar x)^2 + (\bar x - \mu_0)^2 = \hat\sigma^2 + (\bar x - \mu_0)^2$$
and so
$$\lambda = \Bigl(\frac{\hat\sigma^2}{\hat\sigma^2 + (\bar x - \mu_0)^2}\Bigr)^{n/2} = \Bigl(\frac{1}{1 + \frac{(\bar x - \mu_0)^2}{\hat\sigma^2}}\Bigr)^{n/2} = \Bigl(\frac{1}{1 + \frac{(\bar x - \mu_0)^2}{(n-1)s^2/n}}\Bigr)^{n/2} = \Bigl(\frac{1}{1 + t^2/(n-1)}\Bigr)^{n/2}$$
Now $\lambda < C$ implies that $t^2 > k$ for some constants $C, k$. We can compute $k$ exactly by
$$k = t^2_{n-1,1-\alpha/2}$$
[Double hats mark the restricted MLE; in the photo the single and double hats on $\hat\sigma^2$ are small but distinguishable. $t = (\bar x - \mu_0)/(s/\sqrt n)$ is not defined on the page. Summation indices mix $i$ and $j$, as written. The cross term vanishing in the expansion of $\hat{\hat\sigma}^2$ is not shown. Checked: the algebra is correct.]

*Figure:* none.

---

### HW 48 (`20261122_011735.jpg`): Generalised likelihood ratio test (example, one-sided)

**Generalised likelihood ratio test (example)** [top-right number "14"]

**Ex.** Again suppose $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$, where $\sigma^2$ is unknown. Now suppose we are testing $H_0: \mu = \mu_0$ vs. $H_1: \mu > \mu_0$. It follows that
$$\hat\mu = \begin{cases}\bar x & \text{if } \bar x \ge \mu_0\\ \mu_0 & \text{if } \bar x < \mu_0\end{cases}$$
and so
$$\lambda = \begin{cases} 1 & \text{if } \bar x \le \mu_0\\ \Bigl(\dfrac{1}{1 + t^2/(n-1)}\Bigr)^{n/2} & \text{if } \bar x > \mu_0\end{cases}$$
Similarly, $\lambda < C$ implies $t > C^*$, and we can compute $C^*$ by
$$C^* = t_{n-1,1-\alpha}$$
[$\hat\mu$ is the MLE over $\Omega = \{\mu \ge \mu_0\}$ (null and alternative together), not stated.]

**Rem.** To summarise, we have
$$
\begin{aligned}
&\bigl\{\bar X \ge \mu_0 + t^{1-\alpha}_{n-1}\,s/\sqrt n\bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu > \mu_0\\
&\bigl\{\bar X \le \mu_0\ [\text{blot}]\ t^{1-\alpha}_{n-1}\,s/\sqrt n\bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu > \mu_1\\
&\bigl\{\bar X \le \mu_0 - t^{1-\alpha/2}_{n-1}\,s/\sqrt n\ \cup\ \bar X \ge \mu_0 + t^{1-\alpha/2}_{n-1}\,s/\sqrt n\bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu \ne \mu_0
\end{aligned}
$$
[possible error: in the second line the alternative should be $H_1: \mu < \mu_0$; the sign between $\mu_0$ and $t$ is covered by a solid blot and should be "$-$". Quantile notation switches from $t_{n-1,1-\alpha}$ (above) to $t^{1-\alpha}_{n-1}$ (here), same meaning.]

*Figure:* none. [Lower third blank.]

---

### HW 49 (`20261122_011742.jpg`): Goodness-of-fit tests

**Goodness-of-fit tests** [top-right number "14"]

**N.** We use goodness-of-fit tests for categorical data. Suppose we have data categorised into $r$ classes, where $O_j$ denotes the number of observations in class $j$. The null hypothesis $H_0$ is
$$H_0: \theta_j = \theta_{j0} \qquad \Big\}\ \theta_{j0} \text{ is the probability of an observation in class } j$$
[The sentences are written interleaved across the first three lines; the reading order above is the evident one.]

We will show that [blot] the test statistic is
$$T = \sum_{j=1}^r\frac{(o_j - e_j)^2}{e_j} \sim \ChiSq{r-1}$$
The pmf of the data follows a multinomial distribution:
$$\Prob(O_1 = o_1,\dots,O_r = o_r) = \frac{n!}{o_1!\cdots o_r!}\prod_{j=1}^r\theta_j^{o_j}$$
and so the likelihood is
$$L(\vect\theta) = \frac{n!}{o_1!\cdots o_r!}\prod_{j=1}^r\theta_j^{o_j} \qquad \text{such that } \textstyle\sum\theta_j = 1$$
It can be shown that the MLE is given by
$$\hat\theta_j = \frac{o_j}{n}$$
[Small blots sit beside the subscripts $j$ of $\hat\theta_j$ and $o_j$.]
and so the GLRT statistic is
$$\lambda = \prod_{j=1}^r\Bigl(\frac{\theta_{j0}}{\hat\theta_j}\Bigr)^{o_j}$$
Taking the logarithm, we obtain
$$
\begin{aligned}
-2\log\lambda &= -2\sum_{j=1}^r o_j\log\Bigl(\frac{\theta_{j0}}{\hat\theta_j}\Bigr) = -2\sum_{j=1}^r o_j\log\Bigl(\frac{n\theta_{j0}}{o_j}\Bigr) = -2\sum_{j=1}^r o_j\log\Bigl(\frac{e_j}{o_j}\Bigr)
\end{aligned}
$$
Now use the Taylor expansion of $\log(1+x)$. Then,
$$
\begin{aligned}
-2\log\lambda &= -2\sum_{j=1}^r o_j\log\Bigl(1 + \frac{e_j - o_j}{o_j}\Bigr)\\
&= -2\sum_{j=1}^r o_j\Bigl[\frac{e_j - o_j}{o_j}\Bigr] - o_j\Bigl[-\frac12\frac{(e_j - o_j)^2}{o_j^2}\Bigr] + \cdots\\
&\approx \sum_{j=1}^r\frac{(o_j - e_j)^2}{o_j} \approx \sum_{j=1}^r\frac{(o_j - e_j)^2}{e_j}
\end{aligned}
$$
and by Wilks' theorem,
$$\sum_{j=1}^r\frac{(o_j - e_j)^2}{e_j} \sim \ChiSq{r-1}$$
[The first-order term $o_j[(e_j - o_j)/o_j]$ is struck through with an arrow to "$0$" (it sums to $0$ because $\sum e_j = \sum o_j = n$, not stated). $e_j = n\theta_{j0}$ (expected count) is used but not defined; the step $n\theta_{j0} = e_j$ shows it. Counts switch between $O_j$ and $o_j$. The degrees of freedom $r-1$ come from $\dim\Omega - \dim\Omega_{H_0} = (r-1) - 0$, not shown.]

*Figure:* none.

---

### HW 50 (`20261122_011747.jpg`): Multiplicity problem, FWER

**Multiplicity problem, FWER** [top-right number "15"]

**N.** The multiplicity problem occurs when many statistical tests are performed on the data set. Each test has its own chance of a Type I error, and so the probability of making at least one false positive increases as the number of tests grows.

**Def.** *Family-wise error rate (FWER).* Suppose $A_i$ is the event that a Type I error occurs for test $i$. Let $A$ be the event that at least one Type I error occurs for the $n$ tests. Then the FWER is given by
$$\mathrm{FWER} = \Prob(A) = \Prob\Bigl(\textstyle\bigcup_i A_i\Bigr) \le \sum_i\Prob(A_i)$$
If the $n$ tests are independent, then
$$\mathrm{FWER} = 1 - \textstyle\prod_i\bigl(1 - \Prob(A_i)\bigr)$$

**Def.** *Bonferroni correction.* Suppose we want to control FWER to at most $\alpha$. The Bonferroni correction limits the probability of Type I error of each test to at most $\alpha/n$, which ensures that $\mathrm{FWER} \le \alpha$.

**Rem.** Using Bonferroni correction reduces the power of each test significantly, which may lead to missed findings.

**N.** Suppose we have the following table:

| | | Retain null | Reject null | |
|---|---|---|---|---|
| TRUE | Null | $a$ | $b$ (false positive) | $N_0$ |
| | Non-null | $c$ (false negative) | $d$ | $N_1$ |
| | | $N - N_r$ | $N_r$ | $N$ |

[The column group is labelled "PREDICTED" above "Reject null"; the row group is labelled "TRUE". Row totals in the last column, column totals in the last row; no rules are drawn. $N$ is the number of tests here, while the FWER definition above uses $n$.]

Then we can express the FWER by
$$\mathrm{FWER} = \Prob(b \ge 1)$$

*Figure (table):* the 2×2 table above, set as a plain grid with labels "TRUE" (left, rows) and "PREDICTED" (top right, columns).

---

### HW 51 (`20261122_011759.jpg`): Multiplicity problem, FDR

**Multiplicity problem, FDR** [top-right number "16"]

**Def.** *False discovery proportion (FDP).* Refer to the previous table. The false discovery proportion (FDP) is defined as $b/N_r$. It is the proportion of false positives to all tests with rejected nulls.
[Both "N." and "Def." are written in the margin; the sentences are interleaved across lines and read as above. $b/N_r$ is undefined when $N_r = 0$; the Rem. at the foot of the page handles this.]

**Def.** *False discovery rate (FDR).* The false discovery rate (FDR) is the expected value of the FDP:
$$\mathrm{FDR} = \E[\mathrm{FDP}]$$

**Th.** The FDR has two important properties:
1. If all hypotheses are null ($N_0 = N$), then $\mathrm{FDR} = \mathrm{FWER}$
2. If $N_0 < N$, then $\mathrm{FDR} < \mathrm{FWER}$

**P.** We prove the first statement. If $N_0 = N$, if $b > 0$, then FDP is one.
$$
\begin{aligned}
\mathrm{FDR} = \E[\mathrm{FDP}] &= \E\bigl[\E[\mathrm{FDP} \given b]\bigr]\\
&= p_0 \times \E[\mathrm{FDP} \given b = 0] + \textstyle\sum_{i=1}^n p_i \times \E[\mathrm{FDP} \given b = i]\\
&= p_0 \times 0 + \textstyle\sum_{i=1}^n p_i \times 1\\
&= \Prob(b \ge 1) = \mathrm{FWER}
\end{aligned}
$$
For the second statement, if $N_0 < N$, if $b \ge 0$, then $\mathrm{FDP} \le 1$.
$$
\begin{aligned}
\mathrm{FDR} = \E[\mathrm{FDP}] &= \E\bigl[\E[\mathrm{FDP} \given b]\bigr]\\
&= p_0 \times \E[\mathrm{FDP} \given b = 0] + \textstyle\sum_{i=1}^{n_0} p_i \times \E[\mathrm{FDP} \given b = i]\\
&\le p_0 \times 0 + \textstyle\sum_{i=1}^{n_0} p_i \times 1\\
&= \dots = \mathrm{FWER}
\end{aligned}
$$
and the result follows.
[$p_i = \Prob(b = i)$ is not defined. The sums run to $n$ (first proof) and $n_0$ (second); in the table's notation these are $N$ and $N_0$. possible error: the proof of statement 2 shows $\mathrm{FDR} \le \mathrm{FWER}$, not the strict inequality stated.]

**Rem.** We can also (more formally) express the FDR by
$$\mathrm{FDR} = \E[\mathrm{FDP} \given N_r > 0]\,\Prob[N_r > 0]$$

*Figure:* none.

---

### HW 52 (`20261122_011807.jpg`): FDR and Benjamini–Hochberg procedure

**FDR and Benjamini–Hochberg procedure** [top-right number "16"]

**Def.** *The Benjamini–Hochberg (BH) procedure.* The BH procedure controls the FDR at a level $\alpha$ when the p-values following the null distribution are independent and uniformly distributed.
1. Order the p-values: $P_{(1)},\dots,P_{(n)}$
2. Calculate $i_1 = \argmax_i\Bigl\{i : P_{(i)} \le \dfrac{\alpha\times i}{n}\Bigr\}$
3. If $i_1$ exists, reject nulls corresponding to $P_{(1)},\dots,P_{(i_1)}$

[$i_1$ is the *largest* $i$ satisfying the condition (LN16); "argmax" of a set of indices is the notes' shorthand.]

**Def.** *FDR adjustment.* The BH procedure uses the level $\alpha$ to determine tests as significant. To find the minimum $\alpha$-level where a test is rejected, we define the FDR-corrected value by
$$\alpha(i) = \frac{P_{(i)}\,N}{i}$$
[$N$ here = $n$ above (number of tests).]

**Rem.** The FDR-corrected value $\alpha(i)$ is not necessarily monotonic on $P_{(i)}$.
[A solid ink block crosses out one line here; nothing under it is readable.]
To address this, define $\alpha^*(i)$ as the FDR-adjusted value for $P_{(i)}$ where $\alpha^*(i)$ is the smallest $\alpha(k)$ for $k \ge i$.

*Figure:* none. [Lower 40% blank.]

---

### HW 53 (`20261122_011817.jpg`): Errors in testing (PPV)

**Errors in testing (PPV)** [top-right number "17"]

**N.** Taking a high value of the conditional probability $\Prob(A \given B)$ to imply that the conditional probability $\Prob(B \given A)$ to also be high is known as the "fallacy of the transposed conditional". This occurs [blot] in diagnostic testing as well as in criminal trials, where the conditional probability of the evidence given the accused is guilty is taken to imply a high probability of the accused being guilty given the evidence.

**Ex.** Suppose a test $T$ is used to screen for a disease $D$. The null corresponds to not having the disease, while the alternative does correspond to having the disease. The performance of this test can be measured in terms of
$$\text{sensitivity: } 1 - \beta = \Prob(T \text{ positive} \given D \text{ present})$$
$$\text{specificity: } 1 - \alpha = \Prob(T \text{ negative} \given D \text{ absent})$$
The positive predictive value (PPV) is defined to be
$$\mathrm{PPV} = \Prob(D \text{ present} \given T \text{ positive}) = \Prob(\text{True positive} \given T \text{ positive})$$
To calculate the PPV for this scenario, we need to know the prior odds of the disease in the population being screened:
$$R = \frac{p_1}{p_0} = \frac{1 - p_0}{p_0}$$
We calculate the PPV using Bayes' theorem:
$$
\begin{aligned}
\mathrm{PPV} &= \frac{p_1\,\Prob(T \text{ positive} \given D \text{ present})}{p_1\,\Prob(T \text{ positive} \given D \text{ present}) + p_0\,\Prob(T \text{ positive} \given D \text{ absent})}\\
&= \frac{p_1(1-\beta)}{p_1(1-\beta) + p_0\alpha} = \frac{1-\beta}{(1-\beta) + R^{-1}\alpha}
\end{aligned}
$$
Similarly, the negative predictive value (NPV) can be expressed by:
$$\mathrm{NPV} = \Prob(D \text{ absent} \given D \text{ negative}) = \frac{1-\alpha}{(1-\alpha) + R\beta}$$
The sensitivity of the test may be large, but the reverse conditional probability (PPV) is sometimes also mistakenly assumed to be large. This is not usually true.
[$p_1$, $p_0$ = prevalence of the disease and its complement, not defined. possible error: in the NPV, "$D$ negative" should be "$T$ negative". Checked: both formulas are correct. A stray tick in the left margin.]

*Figure:* none.

---

### HW 54 (`20261122_011822.jpg`): Two-sample t-test

**Two-sample t-test** [top-right number "19"]

**Def.** *Two-sample t-test.* Suppose a random sample of size $n_i$ is taken from a class $i$ with distribution $\Normal(\mu_i,\sigma^2)$. The two means $\mu_1$ and $\mu_2$ are unknown, and the variance $\sigma^2$ is shared but unknown. We test
$$H_0: \mu_1 = \mu_2 \quad\text{vs.}\quad H_1: \mu_1 \ne \mu_2$$
The GLRT leads to the two-sample t-test with statistic
$$W = \frac{\bar x_1 - \bar x_2}{s\sqrt{1/n_1 + 1/n_2}} \sim t_{n-2}$$

**P.** The full proof is given in LN19. An overview is given below: The ML estimation of $\vect\theta$ over $\Omega$ gives
$$\hat\mu_i = \bar x_i \quad\text{and}\quad \hat\sigma^2 = \frac{n-2}{n}s^2$$
and the ML estimation of $\vect\theta$ over $\Omega_0$ gives
$$\hat{\hat\mu} = \bar x \quad\text{and}\quad \hat{\hat\sigma}^2 = \sum_{i=1}^2\sum_{j=1}^{n_i}(x_{ij} - \bar x)^2/n$$
The GLRT statistic $\lambda$ is given by
$$
\begin{aligned}
\lambda = \frac{L(\hat{\hat{\vect\theta}})}{L(\hat{\vect\theta})} = \cdots
&= \Bigl(\frac{\hat{\hat\sigma}^2}{\hat\sigma^2}\Bigr)^{-n/2} = \Bigl(\frac{\sum_{i=1}^2\sum_{j=1}^{n_i}(x_{ij} - \bar x)^2}{(n-2)s^2}\Bigr)^{-n/2} = \cdots\\
&= \Bigl(\frac{(n-2)s^2 + \bigl(\frac1{n_1} + \frac1{n_2}\bigr)^{-1}(\bar x_1 - \bar x_2)^2}{(n-2)s^2}\Bigr)^{-n/2}\\
&= \Bigl(\frac{(n-2)s^2}{(n-2)s^2 + \bigl(\frac1{n_1} + \frac1{n_2}\bigr)^{-1}(\bar x_1 - \bar x_2)^2}\Bigr)^{n/2}\\
&= \frac{1}{\Bigl(1 + \frac{1}{n-2}\bigl(\frac{s^2}{n_1} + \frac{s^2}{n_2}\bigr)^{-1}(\bar x_1 - \bar x_2)^2\Bigr)^{n/2}}\\
&= \frac{1}{(1 + w^2/(n-2))^{n/2}}
\end{aligned}
$$
where
$$w = \frac{\bar x_1 - \bar x_2}{s\sqrt{1/n_1 + 1/n_2}}$$
["LN19" is written "LN1a"/"LN19" with the 9 looking like "a"; the full proof is in LN19 (the page number is also "19"). $n = n_1 + n_2$, $s^2$ (pooled variance) and $\bar x$ (grand mean) are not defined on the page. "$\sim t_{n-2}$" holds under $H_0$. The hat on $\hat{\hat\mu}$ is double, as on HW 47. Checked: the algebra is correct.]

*Figure:* none.

---

### HW 55 (`20261122_011830.jpg`): Satterthwaite's approximation

**Satterthwaite's approximation** [top-right number "21"]

**Def.** Suppose $k$ independent mean squares are combined to estimate a variance. We have:
$$W = \sum_{i=1}^k a_iW_i \qquad \text{where } \frac{W_i}{g_i} \sim \frac{\ChiSq{v_i}}{v_i}$$
The constants $g_i = \E[W_i]$ are unknown, and $a_i$ are known. Satterthwaite approximates the distribution of $W$ by
$$\frac{W}{\E(W)} \sim \frac{\ChiSq v}{v}$$
with approximate degrees of freedom
$$v = \frac{(\sum_i a_iw_i)^2}{\sum_i(a_i^2/v_i)w_i^2}$$
where $w_i$ are the observed values of $W_i$.
[Degrees of freedom are written with a handwritten "v" (LN21 uses $\nu$).]

**Def.** We can use Satterthwaite's approximation to approximate the t-statistic degrees of freedom.
$$T = \frac{\bar y_1 - \bar y_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$$
Under the null hypothesis $H_0: \mu_1 = \mu_2$, we have
$$T \sim t_v$$
where
$$v = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{\frac{1}{n_1-1}(s_1^2/n_1)^2 + \frac{1}{n_2-1}(s_2^2/n_2)^2}$$
["$\sim$" is approximate. The two samples are normal with unequal variances (LN21), not stated.]

**Rem.** To derive $v$, we first assume
$$\frac{W}{\E[W]} \sim \frac{\chi^2}{v} \implies \Var\Bigl[\frac{W}{\E[W]}\Bigr] = \Var\Bigl[\frac{\ChiSq v}{v}\Bigr] \implies v = \frac{2\,\E[W]^2}{\Var[W]}$$
Since the $W_i$ are independent,
$$\E[W] = \textstyle\sum_i a_i\E[W_i] = \sum_i a_ig_i$$
$$\Var[W] = \textstyle\sum_i a_i^2\Var[W_i] = 2\sum_i\dfrac{a_i^2}{v_i}g_i^2$$
and substituting gives
$$v = \frac{(\sum_i a_ig_i)^2}{\sum_i(a_i^2/v_i)g_i^2} \approx \frac{(\sum_i a_ig_i)^2}{\sum_i(a_i^2/v_i)w_i^2}$$
[possible error: in the last expression the numerator should also use the observed values, $(\sum_i a_iw_i)^2$, as in the definition above. $\Var(\ChiSq v/v) = 2/v$ and $\Var(W_i) = 2g_i^2/v_i$ are used without being stated.]

*Figure:* none.

---

### HW 56 (`20261122_011836.jpg`): Tukey's studentised range

**Tukey's studentised range** [top-right number "22"]

**Def.** Let $u_1,\dots,u_k$ be an observed random sample with $U_i \sim \Normal(\mu,\sigma^2)$. Let $s^2$ be an independent estimator of $\sigma^2$ such that
$$\frac{vs^2}{\sigma^2} \sim \ChiSq v$$
Define the sample range by
$$R = \max_i u_i - \min_i u_i = u_{(n)} - u_{(1)}$$
Then the Tukey studentised range statistic is
$$T = \frac{R}{s}$$
The distribution of this statistic $T$ (not to be confused with the Student's t-distribution) depends on $k$ and $v$.
[possible error: the sample has size $k$, so the largest order statistic is $u_{(k)}$, not $u_{(n)}$.]

**Def.** Suppose we estimate parameters $\theta_1,\dots,\theta_k$ using
$$\hat\theta_i \sim \Normal(\theta_i,\ c^2\sigma^2)$$
and that $s^2$ satisfies
$$\frac{vs^2}{\sigma^2} \sim \ChiSq v$$
Then a simultaneous (all pairs $i \ne j$) $100(1-\alpha)\%$ confidence interval for all differences $\theta_i - \theta_j$ is
$$(\hat\theta_i - \hat\theta_j) - c\,T_{k,v;1-\alpha}\,s \le \theta_i - \theta_j \le (\hat\theta_i - \hat\theta_j) + c\,T_{k,v;1-\alpha}\,s$$
[$T_{k,v;1-\alpha}$ = the $1-\alpha$ quantile of the studentised range distribution. The $\hat\theta_i$ must be independent and independent of $s^2$ (LN22), not stated.]

**P.** Let $u_i = (\hat\theta_i - \theta_i)/c$. Then $U_i \sim \Normal(0,\sigma^2)$. By the definition of the Tukey statistic,
$$\frac{u_{(n)} - u_{(1)}}{s} \le T_{k,v;1-\alpha} \quad \text{with prob. } 1-\alpha$$
$$\implies \frac{\abs{u_i - u_j}}{s} \le T_{k,v;1-\alpha} \quad \text{with prob. } 1-\alpha$$
Substitute over $u_i$ and $u_j$ and expand the absolute value to obtain
$$-c\,T_{k,v;1-\alpha}\,s \le (\hat\theta_i - \theta_i) - (\hat\theta_j - \theta_j) \le c\,T_{k,v;1-\alpha}\,s$$
and the result follows, with probability $(1-\alpha)$.
[The implication holds for all pairs $i, j$ simultaneously, which is what makes the interval simultaneous; not stated. $u_{(n)}$ again for $u_{(k)}$.]

**Rem.** An extension to linear contrasts is given in LN22.

*Figure:* none. [Lower 10% blank.]

---
