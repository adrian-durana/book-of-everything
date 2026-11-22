# STAT3001 Mathematical Statistics: transcription, part 1 of 3 (HW 01–28)

_Transcription phase. Nothing here is book text yet. No dates are recorded (the lecture diary's dates and the year of references cited in the notes are omitted); a source is identified only by semester: the course was taken in **Semester 1, 2026**._

## Sources (all three parts)
| Code | Source | Role | Where transcribed |
|---|---|---|---|
| **HW nn** | 56 photos of the handwritten notebook, one page per photo, numbered in shooting order (file name under each heading). Covers the whole course in lecture-note order: multivariate normal → regular exponential family → information and the Cramér–Rao bound → sufficiency, Rao–Blackwell, Lehmann–Scheffé → Jensen, KL divergence, loss and risk → Basu → large-sample theory and MLE asymptotics → EM algorithm → hypothesis testing (NP lemma, GLRT, Wilks, GoF) → multiple testing (FWER, FDR, BH) → PPV → two-sample $t$, Satterthwaite, Tukey. | **Main source** | Parts 1–2, in full |
| **LNn** | Lecturer's typed lecture notes LN1–LN24 (LN19a extra; no LN25 uploaded), 182 pp. LN18 is a book chapter (mixture models, ch. 6, pp. 175–220); LN24 is a scanned journal article on the bootstrap. | Supplement | Part 3: section/page index, figures, content found only here |
| **BN** | *Some Background Notes on Point Estimation* (file `STAT2004 notes.pdf`, 36 pp.), the lecturer's revision notes for STAT2004 material used in this course (lecture diary: "Background Notes"). Not the same file as the STAT2004 chat's PE notes. | Supplement (first third of the course) | Part 3: page index, figures |
| **S1, S2** | Guest lectures 4 and 5 (slides with the lecturer's handwritten annotations): *Introduction to Bayesian Estimation* (13 slides), *MCMC Sampling* (16 slides). | **Only source** for Bayesian estimation and MCMC | Part 3: annotations transcribed, slide index, code |
| **LD** | *Lecture diary* (6 pp.): what was covered in each lecture, examinable/non-examinable notes. | Scope guide | Part 3: scope notes only (dates omitted) |

Page counts: HW 56 pages; LN 182 pp.; BN 36 pp.; S1 13 + S2 16 slides; LD 6 pp.

## Legibility check (HW photos)
All 56 photos were read in order at full resolution, with zoomed crops wherever a symbol was in doubt. Sharpness and exposure are adequate on every photo; a broad diagonal shadow from the phone crosses most pages, but the ink reads through it everywhere. No page is cut off at the text. Photos 01–06 and 08–14 are stored rotated (landscape); they read correctly once rotated.

**Retake suggested (1):**
- **HW 23** (`20261122_011330.jpg`): the final expression of the Rem., $\E[(W-\theta)\,\cdot\,]$, shows no exponent after the bracket. A sharper, unshadowed close-up of that line would settle whether a faint "²" is there or is missing in the notebook (marked `[possible error]` either way; the meaning is clear from the line above).

**Not worth retaking (minor, no content lost):**
- HW 37 (`20261122_011539.jpg`): slightly soft overall; every word reads.
- HW 39 (`20261122_011603.jpg`): the top-right LN number is cut off at the page edge and a finger is visible at the left margin; no writing is covered.

**Unreadable in the notebook itself (a retake won't help):** solid or hatched ink blocks cross out words on HW 04, 11, 18 (old heading), 21, 27 (one or two words), 28 (one word), 33, 38, 40, 48 (the sign before $t$ in the second summary line: should be "$-$"), 49 and 52 (one line). Each is marked `[blot]`/described in place; only HW 48's blot affects content, and it is recoverable from context.

## Conventions
- Wording, structure and labels follow the notes: **Def.**, **Th.**, **P.** (proof), **Ex.**, **Rem.**, **N.** (note). Where a result is labelled "Def." in the margin this is kept and flagged once in brackets.
- The number written at the top right of each notebook page is the **lecture-note number** (LNn) the page is based on, not a page number; it is recorded as "[top-right number …]".
- Maths uses `notation.tex` macros (`\Prob`, `\E`, `\Var`, `\Cov`, `\Normal`, `\ChiSq`, `\iid`, `\vect`, `\mat`, `\T`, `\ind`, `\argmax`, `\MSE`, `\bias`, …). The notes underline vectors; they are set with `\vect`/`\mat`.
- **Information:** the notes write both the Fisher (expected) information and the observed information with one handwritten capital I. They are told apart here as $\mathcal I(\vect\theta)$ (expected) and $I(\vect\theta)$ (observed), following LN3/BN. This is a transcription aid, not a notation decision (see the inventory's notation list).
- Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic re-computed where marked "Checked"); `[blot]` marks crossed-out or unreadable ink. Cross-references "LNn p. k" and "BN p. k" point to the typed notes (index in part 3).

**This part:** multivariate normal, sample variance, regular exponential family and the likelihood equation, observed and expected information, Cramér–Rao bound, sufficiency, Rao–Blackwell, Lehmann–Scheffé, Jensen and KL divergence, loss and risk, Basu's theorem, consistency, ARE, asymptotic efficiency.

---

### HW 01 (`20261122_010855.jpg`): Multivariate normal distributions

**Multivariate normal distributions** [top-right number "1" top right]

**Def.** A random vector $\vect X \in \R^d$ is multivariate normal with mean $\vect\mu \in \R^d$ and covariance $\mat\Sigma \in \R^{d\times d}$, written as
$$\vect X \sim \Normal(\vect\mu, \mat\Sigma)$$
if its p.d.f is
$$f(\vect x) = \frac{1}{(2\pi)^{d/2}\abs{\mat\Sigma}^{1/2}} \exp\Bigl[-\tfrac12(\vect x - \vect\mu)\T \mat\Sigma^{-1}(\vect x - \vect\mu)\Bigr]$$
Note that
$$\vect\mu = \E[\vect X]$$
$$\mat\Sigma = \E\bigl[(\vect X - \vect\mu)(\vect X - \vect\mu)\T\bigr] = \E(\vect X\vect X\T) - \vect\mu\vect\mu\T$$

**Def.** *Affine distributions.* Let $\vect X \sim \Normal(\vect\mu, \mat\Sigma)$. Then for some full row-rank matrix $\mat A \in \R^{m\times d}$ and vector $\vect b \in \R^m$:
$$\vect Y = \mat A\vect X + \vect b \sim \Normal(\mat A\vect\mu + \vect b,\ \mat A\mat\Sigma\mat A\T)$$
[Labelled "Def." in the margin although it is a result. "for some" as written; the result holds for every such $\mat A$, $\vect b$.]

**P.** We have that
$$\E(\vect Y) = \E(\mat A\vect X + \vect b) = \mat A\,\E(\vect X) + \vect b$$
and
$$
\begin{aligned}
\Cov(\vect Y) = \Cov(\mat A\vect X + \vect b)
&= \E\bigl[(\mat A(\vect X - \vect\mu))(\mat A(\vect X - \vect\mu))\T\bigr]\\
&= \E\bigl[\mat A(\vect X - \vect\mu)(\vect X - \vect\mu)\T\mat A\T\bigr]\\
&= \mat A\,\E\bigl[(\vect X - \vect\mu)(\vect X - \vect\mu)\T\bigr]\mat A\T\\
&= \mat A\mat\Sigma\mat A\T
\end{aligned}
$$
by linearity of expectation.
[possible error (gap): the proof only computes the mean and covariance of $\vect Y$; it does not show that $\vect Y$ is normal. LN1 p. 2 proves normality of $\mat C\vect X$ via the MGF.]

*Figure:* none. [A diagonal shadow crosses the page; all text is readable.]

---

### HW 02 (`20261122_010902.jpg`): Multivariate normal: marginal, conditional distributions

**Multivariate normal: marginal, conditional distributions** [top-right number "1" top right]

**Def.** *Marginal distributions.* Partition $\vect X = (\vect X_1, \vect X_2)\T$ such that
$$\begin{pmatrix}\vect X_1\\ \vect X_2\end{pmatrix} \sim \Normal\left(\begin{pmatrix}\vect\mu_1\\ \vect\mu_2\end{pmatrix}, \begin{bmatrix}\mat\Sigma_{11} & \mat\Sigma_{12}\\ \mat\Sigma_{21} & \mat\Sigma_{22}\end{bmatrix}\right)$$
The marginal distribution of $\vect X_1$ is
$$\vect X_1 \sim \Normal(\vect\mu_1, \mat\Sigma_{11})$$

**Rem.** Any subset of a normal vector is also normally distributed.

**Def.** *Conditional distributions.* With the same partitioning, the conditional distribution is
$$\vect X_1 \given \vect X_2 \sim \Normal(\vect\mu_{1|2}, \mat\Sigma_{1|2})$$
where
$$\vect\mu_{1|2} = \vect\mu_1 + \mat\Sigma_{12}\mat\Sigma_{22}^{-1}(\vect x_2 - \vect\mu_2)$$
$$\mat\Sigma_{1|2} = \mat\Sigma_{11} - \mat\Sigma_{12}\mat\Sigma_{22}^{-1}\mat\Sigma_{21}$$
[The conditioning is written $\vect X_1 \given \vect X_2$ (upper case) but the mean uses the value $\vect x_2$. No proof is given.]

**Rem.** For intuition, knowing $\vect X_2 = \vect x_2$ updates our expectation and uncertainty about $\vect X_1$.

**Rem.** The matrix $\mat\Sigma_{1|2}$ is known as the Schur complement of $\mat\Sigma_{11}$.
[possible error: $\mat\Sigma_{11} - \mat\Sigma_{12}\mat\Sigma_{22}^{-1}\mat\Sigma_{21}$ is the Schur complement of $\mat\Sigma_{22}$ in $\mat\Sigma$, not of $\mat\Sigma_{11}$.]

*Figure:* none. [The lower third of the page is blank; faint show-through from the next page.]

---

### HW 03 (`20261122_010910.jpg`): Normal distribution given sample mean (example)

**Normal distribution given sample mean (example)** [top-right number "1"]

**Ex.** Let $\vect X \sim \Normal(\vect\mu, \sigma^2\mat I)$. Find the distribution of $X_i \given \bar x$.

Let
$$W = (X_i, \bar X)\T = \mat A\vect X \qquad \text{where } \mat A \in \R^{2\times n}\text{, first row } \vect e_i\T\text{, second row } (1/n)\,\vect 1_n\T.$$
Then $W \sim \Normal(\vect\mu_W, \mat\Sigma_W)$, where
$$\vect\mu_W = \mu\vect 1_2 \qquad \mat\Sigma_W = \mat A\mat\Sigma\mat A\T = \sigma^2\mat A\mat A\T$$
and the elements of $\mat\Sigma_W$ are given by
$$(\mat\Sigma_W)_{11} = \sigma^2 \qquad (\mat\Sigma_W)_{22} = \sigma^2/n \qquad (\mat\Sigma_W)_{12} = \sigma^2/n$$
It follows that
$$X_i \given \bar x \sim \Normal\bigl(\bar x,\ (1 - 1/n)\sigma^2\bigr)$$
[$\vect\mu_W = \mu\vect 1_2$ assumes every component has the same mean $\mu$ ($\vect\mu = \mu\vect 1_n$); the statement writes the vector $\vect\mu$. The last step applies the conditional formulas of HW 02: $\mu + (\sigma^2/n)(\sigma^2/n)^{-1}(\bar x - \mu) = \bar x$ and $\sigma^2 - (\sigma^2/n)^2/(\sigma^2/n) = (1-1/n)\sigma^2$, not written out. Checked: correct.]

**Rem.** The elements of $\mat\Sigma_W$ are found by:
$$\Var(X_i) = (\mat\Sigma_W)_{11} = \sigma^2$$
$$\Var(\bar X) = (\mat\Sigma_W)_{22} = \sigma^2/n$$
$$
\begin{aligned}
(\mat\Sigma_W)_{12} = (\mat\Sigma_W)_{21} &= \Cov(X_i, \bar X)\\
&= \Cov\Bigl(X_i, \tfrac1n\textstyle\sum_j X_j\Bigr)\\
&= \Cov\bigl(X_i, X_i\cdot\tfrac1n\bigr) + \textstyle\sum_{j\ne i}\Cov\bigl(X_i, \tfrac1n X_j\bigr)\\
&= \tfrac1n\Cov(X_i, X_i) + \tfrac1n\textstyle\sum_{j\ne i}\Cov(X_i, X_j)\\
&= \tfrac1n\Var(X_i) + 0\\
&= \sigma^2/n
\end{aligned}
$$

*Figure:* none.

---

### HW 04 (`20261122_010915.jpg`): Distribution of sample variance $s^2$

**Distribution of sample variance $s^2$** [top-right number "1"]

**Def.** Let $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$. Then the sample variance has distribution
$$\frac{(n-1)s^2}{\sigma^2} \sim \ChiSq{n-1}$$
and is distributed independently of $\bar X$.
[Labelled "Def." in the margin although it is a theorem.]

**P.** Let $\mat B$ be an $n\times n$ orthogonal matrix such that its final row is
$$B_{nj} = \frac{1}{\sqrt n} \qquad \text{for } j = 1,\dots,n$$
Now define the transformed variables $\vect Y = \mat B\vect X$, i.e.
$$Y_i = \textstyle\sum_j B_{ij}X_j \qquad \text{for } i = 1,\dots,n$$
$$\implies Y_n = \textstyle\sum_j B_{nj}X_j = \frac{1}{\sqrt n}\sum_j X_j = \sqrt n\,\bar X$$
First note that by the orthogonality of $\mat B$ we have
$$\Cov(\vect Y) = \mat B\Cov(\vect X)\mat B\T = \mat B\sigma^2\mat I\mat B\T = \sigma^2\mat I$$
and so $Y_i$ are uncorrelated. As $Y_i$ are also jointly normal, $Y_i$ are independent. Thus $\bar X$ is independent of $Y_1,\dots,Y_{n-1}$.
Second note that
$$\vect Y\T\vect Y = (\mat B\vect X)\T\mat B\vect X = \vect X\T\mat B\T\mat B\vect X = \vect X\T\vect X$$
$$\implies \textstyle\sum_i Y_i^2 = \sum_i X_i^2 \qquad \text{(by definition of dot product)}$$
Therefore,
$$
\begin{aligned}
s^2 &= \frac{1}{n-1}\textstyle\sum_j (X_j - \bar X)^2 = \frac{1}{n-1}\Bigl(\sum_j X_j^2 - n\bar X^2\Bigr)\\
&= \frac{1}{n-1}\Bigl(\textstyle\sum_i Y_i^2 - Y_n^2\Bigr) = \frac{1}{n-1}\sum_{i=1}^{n-1} Y_i^2
\end{aligned}
$$
and so $s^2$ is independent of $\bar X$.
[Two hatched blocks cross out text: one before $\sum_j(X_j-\bar X)^2$ and one inside the second bracket; the replacement "$X_j^2 - n\bar X^2$" is written above the second block. The crossed-out text is unreadable and carries no content.]

Finally we have $Y_i \overset{\text{ind.}}{\sim} \Normal(0,\sigma^2)$ which implies $Y_i/\sigma \overset{\text{ind.}}{\sim} \Normal(0,1)$. By Cochran's theorem (beyond scope of course) then
$$\sum_{i=1}^{n-1}\frac{Y_i^2}{\sigma^2} \sim \ChiSq{n-1} \implies \frac{(n-1)s^2}{\sigma^2} \sim \ChiSq{n-1}$$
and so $s^2$ follows a chi-square distribution with $n-1$ d.o.f.
[possible error: $Y_i \sim \Normal(0,\sigma^2)$ holds for $i = 1,\dots,n-1$ only ($\E Y_i = \mu\sqrt n\sum_j B_{ij}B_{nj} = 0$ for $i<n$ by orthogonality to the last row, not shown); $Y_n \sim \Normal(\sqrt n\mu,\sigma^2)$. The last step is the definition of $\ChiSq{n-1}$ as a sum of $n-1$ independent squared standard normals; the appeal to Cochran's theorem is as written. LN1 pp. 4–6 gives the course's proof (Helmert transformation, MGF argument).]

*Figure:* none.

---

### HW 05 (`20261122_010925.jpg`): Log-likelihoods of multivariate normals

**Log-likelihoods of multivariate normals** [top-right number "2"]

**Def.** Let $\vect X \sim \Normal(\vect\mu,\mat\Sigma)$. The log-likelihood of $\vect X$ is
$$\log L(\vect\theta) = -\frac{np}{2}\log(2\pi) - \frac n2\log\abs{\mat\Sigma} - \frac12\textstyle\sum_j(\vect x_j - \vect\mu)\T\mat\Sigma^{-1}(\vect x_j - \vect\mu)$$
[A stray "I" is written in the left margin before "Def.". The sample $\vect x_1,\dots,\vect x_n$ of $p$-dimensional observations is implicit; HW 01 used $d$ for the dimension, here $p$ (as in LN2).]

**Def.** In the univariate case, $X \sim \Normal(\mu,\sigma^2)$ and
$$
\begin{aligned}
\log L(\vect\theta) &= -\frac n2\log(2\pi) - \frac n2\log(\sigma^2) - \frac{1}{2\sigma^2}\textstyle\sum_j(x_j - \mu)^2\\
&= -\frac n2\log(2\pi) - \frac n2\log(\sigma^2) - \textstyle\sum_j\dfrac{x_j^2}{2\sigma^2} + \sum_j\dfrac{x_j\mu}{\sigma^2} - \dfrac{n\mu^2}{\sigma^2}
\end{aligned}
$$
[possible error: the last term should be $-n\mu^2/(2\sigma^2)$. Checked against the zoomed photo: the denominator is $\sigma^2$.]

**Rem.** Note that $\vect\theta$ is the parameter vector of $d = p + \tfrac12 p(p+1)$ dimensions, containing the $p$ elements of $\vect\mu$ and the $\tfrac12 p(p+1)$ elements of $\mat\Sigma$.

*Figure:* none. [Lower half of the page blank.]

---

### HW 06 (`20261122_010937.jpg`): Regular exponential family

**Regular exponential family** [top-right number "2"]

**Def.** Let $\vect X$ have some known distribution, where $\vect X_i \in \R^p$.
Let $\vect\theta \in \R^d$ be the parameter vector.
Let $\vect T(\vect X)$ be a $q$-dimensional statistic, where $q \ge d$.

Then $L(\vect\theta)$ belongs to the $d$-parameter exponential family if it has the form
$$f(\vect x;\vect\theta) = L(\vect\theta) = \frac{b(\vect x)\exp\bigl[\vect c(\vect\theta)\T\vect T(\vect x)\bigr]}{a(\vect\theta)}$$
where
- $a(\vect\theta)$: non-negative, scalar function
- $b(\vect x)$: non-negative, scalar function
- $\vect c(\vect\theta)$: $q\times 1$ vector function; natural / canonical parameter vector.

[possible error (omission): the page is headed "Regular exponential family" but the definition is of the $d$-parameter exponential family; the condition for regularity ($q = d$ and the Jacobian of $\vect c(\vect\theta)$ of full rank, LN3 p. 1) is not stated.]

**Rem.** If $\vect X$ belongs to the regular exponential family, then the statistic $\vect T(\vect x)$ is sufficient. Revision on sufficient statistics is given later.

**Rem.** Functions in the regular exponential family include:
- Normal (univariate and multivariate)
- Bernoulli
- Poisson
- Exponential
- Gamma, Beta

["Functions" as written; distributions are meant.]

*Figure:* none. [Lower third blank.]

---

### HW 07 (`20261122_010955.jpg`): Likelihood equation (scalar)

**Likelihood equation (scalar)** [top-right number "3"]

**Def.** (Scalar case) Suppose $\vect X$ has some distribution belonging to the regular exponential family. Then the MLE $\hat\theta$ satisfies
$$\E[T(\vect X)] = T(\vect x)$$
[Labelled "Def." although it is a theorem. The expectation is evaluated at $\theta = \hat\theta$ (written $\E_{\hat\theta}$ on HW 08, not here).]

**P.** The log-likelihood of a function in the REF is
$$\log L(\theta) = \log b(\vect x) + c(\theta)T(\vect x) - \log a(\theta)$$
Differentiate:
$$\frac{\partial}{\partial\theta}\log L(\theta) = \frac{\partial}{\partial\theta}c(\theta)\,T(\vect x) - \frac{\partial}{\partial\theta}\log a(\theta) \qquad [1]$$
Note that $\partial/\partial\theta\,\log L(\theta)\big|_{\theta=\hat\theta} = 0$ as $\hat\theta$ maximises $L(\theta)$.
Take the expectation on both sides:
$$0 = \frac{\partial}{\partial\theta}c(\theta)\,\E[T(\vect X)] - \frac{\partial}{\partial\theta}\log a(\theta)$$
$$\implies \frac{\partial}{\partial\theta}c(\theta)\,\E[T(\vect X)] = \frac{\partial}{\partial\theta}\log a(\theta) \qquad [2]$$
Now substitute [2] into [1]:
$$
\begin{aligned}
0 &= \frac{\partial}{\partial\theta}c(\theta)\,T(\vect x) - \frac{\partial}{\partial\theta}c(\theta)\,\E[T(\vect X)]\\
&= \frac{\partial}{\partial\theta}c(\theta)\bigl[T(\vect x) - \E[T(\vect X)]\bigr]
\end{aligned}
$$
which implies the result.
["REF" = regular exponential family. "a function in the REF" as written (a distribution is meant).]
[possible error: the expectation step uses $\E\{\partial\log L(\theta)/\partial\theta\} = 0$ for all $\theta$ (LN3 (3)–(7)), not the fact that the score vanishes at $\hat\theta$; the sentence about $\hat\theta$ belongs to the final step, where [1] is set to $0$ at $\theta = \hat\theta$. The conclusion also needs $c'(\hat\theta) \ne 0$ (regularity), not stated.]

*Figure:* none. [Lower third blank.]

---

### HW 08 (`20261122_011054.jpg`): Likelihood equation (vector)

**Likelihood equation (vector)** [top-right number "3"]

**Def.** (Vector case) Suppose $\vect X$ has some distribution belonging to the regular exponential family. Then the MLE $\hat{\vect\theta}$ satisfies
$$\E_{\hat{\vect\theta}}[\vect T(\vect X)] = \vect T(\vect x)$$

**P.** We proceed similarly to the scalar parameter case. The log-likelihood is given by
$$\log L(\vect\theta) = \log b(\vect x) + \vect c(\vect\theta)\T\vect T(\vect x) - \log a(\vect\theta)$$
Differentiate with respect to $\vect\theta$:
$$
\begin{aligned}
\nabla\log L(\vect\theta) &= \nabla\vect c(\vect\theta)\T\,\vect T(\vect x) - \nabla\log a(\vect\theta)\\
&= \mat J(\vect\theta)\,\vect T(\vect x) - \nabla\log a(\vect\theta)
\end{aligned}
$$
where
$$\mat J(\vect\theta) = \nabla\vect c(\vect\theta)\T \qquad \bigl(\mat J(\vect\theta)\bigr)_{uv} = \frac{\partial[\vect c(\vect\theta)]_v}{\partial\theta_u} \qquad u,v = 1,\dots,d$$
Similar to the scalar case, we obtain
$$\frac{\partial\log a(\vect\theta)}{\partial\vect\theta} = \mat J(\vect\theta)\,\E[\vect T(\vect X)]$$
and by substitution and factoring
$$
\begin{aligned}
\vect 0 &= \mat J(\vect\theta)\bigl[\vect T(\vect x) - \E[\vect T(\vect X)]\bigr]\\
&= \vect T(\vect x) - \E[\vect T(\vect X)]
\end{aligned}
$$
as $\mat J(\vect\theta)$ is trivially non-singular.
[possible error: $\mat J(\vect\theta)$ is non-singular by the definition of a *regular* exponential family ($q = d$, Jacobian of full rank, LN3 p. 1), not "trivially"; HW 06 omits that condition.]

*Figure:* none.

---

### HW 09 (`20261122_011100.jpg`): Univariate normal is in regular exponential

**Univariate normal is in regular exponential** [top-right number "2", possibly overwritten]

**N.** It is trivial to show that the univariate normal distribution is part of the regular exponential family, with canonical parameter
$$\vect c(\vect\theta) = \bigl(c_1(\vect\theta), c_2(\vect\theta)\bigr); \qquad c_1(\vect\theta) = \frac{\mu}{\sigma^2}, \quad c_2(\vect\theta) = -\frac{1}{2\sigma^2}$$
and corresponding sufficient statistic
$$\vect T(\vect x) = \bigl(T_1(\vect x), T_2(\vect x)\bigr); \qquad T_1(\vect x) = \textstyle\sum_j x_j, \quad T_2(\vect x) = \sum_j x_j^2$$
with normalising terms
$$a(\vect\theta) = \frac n2\log(2\pi) + \frac n2\log\sigma^2 + \frac{n\mu^2}{2\sigma^2}, \qquad b(\vect x) = 1$$
[possible error: the expression given is $\log a(\vect\theta)$, not $a(\vect\theta)$ (compare HW 05: $\log L = -\log a(\vect\theta) + \dots$).]

**N.** The MLE $\hat{\vect\theta}$ can be found by using the likelihood equation.
$$
\begin{aligned}
\E[T_1(\vect X)] &= T_1(\vect x) & \E[T_2(\vect X)] &= T_2(\vect x)\\
\implies \textstyle\sum_j\E(X_j) &= \textstyle\sum x_j & \textstyle\sum_j\E(X_j^2) &= \textstyle\sum_j x_j^2\\
\implies n\mu &= \textstyle\sum x_j & n(\sigma^2 + \mu^2) &= \textstyle\sum_j x_j^2\\
\implies \hat\mu &= \tfrac1n\textstyle\sum x_j & \hat\sigma^2 &= \tfrac1n\textstyle\sum_j(x_j - \bar x)^2
\end{aligned}
$$
[The two columns are solved side by side; the last step for $\hat\sigma^2$ substitutes $\hat\mu = \bar x$, not shown.]

*Figure:* none. [Lower third blank.]

---

### HW 10 (`20261122_011104.jpg`): Multivariate normal is in regular exponential

**Multivariate normal is in regular exponential** [top-right number "4"]

**N.** It is (much less) trivial to show that the multivariate normal distribution is also part of the regular exponential family, with canonical parameter
$$\vect c(\vect\theta) = \bigl(\vect c_1(\vect\theta), \vect c_2(\vect\theta)\bigr)\T, \qquad \vect c_1(\vect\theta) = \mat\Sigma^{-1}\vect\mu; \quad \vect c_2(\vect\theta) = -\tfrac12\mat\Sigma^{-1}$$
and corresponding sufficient statistics
$$\vect T_1(\vect x) = \textstyle\sum_j\vect x_j, \qquad \vect T_2(\vect x) = \sum_j\vect x_j\vect x_j\T$$
A further derivation is given in the following pages.
[$\vect c_2$ and $\vect T_2$ are matrices; LN4 stacks them with the vec operator. The "following pages" are HW 11–14.]

**N.** The MLE $\hat{\vect\theta}$ can similarly be found using the likelihood equation.
$$
\begin{aligned}
\E[\vect T_1(\vect X)] &= \vect T_1(\vect x) & \E[\vect T_2(\vect X)] &= \vect T_2(\vect x)\\
\implies \textstyle\sum_j\E(\vect X_j) &= \textstyle\sum_j\vect x_j & \textstyle\sum_j\E(\vect X_j\vect X_j\T) &= \textstyle\sum_j\vect x_j\vect x_j\T\\
\implies n\vect\mu &= \textstyle\sum_j\vect x_j & n(\mat\Sigma + \vect\mu\vect\mu\T) &= \textstyle\sum_j\vect x_j\vect x_j\T\\
\implies \hat{\vect\mu} &= \bar{\vect x} & \hat{\mat\Sigma} &= \textstyle\sum_j(\vect x_j\vect x_j\T - n\bar{\vect x}\bar{\vect x}\T)/n\\
&& &= \tfrac1n\textstyle\sum_j(\vect x_j - \bar{\vect x})(\vect x_j - \bar{\vect x})\T
\end{aligned}
$$
[possible error: $n\bar{\vect x}\bar{\vect x}\T$ is written inside the sum; it should be $\hat{\mat\Sigma} = \bigl(\sum_j\vect x_j\vect x_j\T - n\bar{\vect x}\bar{\vect x}\T\bigr)/n$. The final line is correct.]

*Figure:* none. [A pale grey rectangle in the lower half (something under the page or a correction-tape mark) holds no writing; the lower half is otherwise blank.]

---

### HW 11 (`20261122_011111.jpg`): Multivariate normal is in regular exponential (derivation, 1)

**Multivariate normal is in regular exponential** [top-right number "4"]

**N.** We show here that the multivariate normal distribution belongs to the regular exponential family. Recall that
$$\log L(\vect\theta) = -\frac{np}{2}\log(2\pi) - \frac n2\log\abs{\mat\Sigma} - \frac12\textstyle\sum_j(\vect x_j - \vect\mu)\T\mat\Sigma^{-1}(\vect x_j - \vect\mu)$$
Note that the final term is a scalar. Consider this term:
$$
\begin{aligned}
&\textstyle\sum_j(\vect x_j - \vect\mu)\T\mat\Sigma^{-1}(\vect x_j - \vect\mu)\\
&= \textstyle\sum_j\vect x_j\T\mat\Sigma^{-1}\vect x_j + n\vect\mu\T\mat\Sigma^{-1}\vect\mu - \sum_j\vect x_j\T\mat\Sigma^{-1}\vect\mu - \sum_j\vect\mu\T\mat\Sigma^{-1}\vect x_j\\
&= \textstyle\sum_j\vect x_j\T\mat\Sigma^{-1}\vect x_j + n\vect\mu\T\mat\Sigma^{-1}\vect\mu - 2\vect\mu\T\mat\Sigma^{-1}\bigl(\sum_j\vect x_j\bigr)\\
&= \tr\Bigl[\textstyle\sum_j\vect x_j\T\mat\Sigma^{-1}\vect x_j + n\vect\mu\T\mat\Sigma^{-1}\vect\mu - 2\vect\mu\T\mat\Sigma^{-1}\bigl(\sum_j\vect x_j\bigr)\Bigr]\\
&= \tr\Bigl[\Bigl(\textstyle\sum_j\vect x_j\vect x_j\T + n\vect\mu\vect\mu\T - 2\bigl(\sum_j\vect x_j\bigr)\vect\mu\T\Bigr)\mat\Sigma^{-1}\Bigr] \qquad (\tr(\mat A\mat B\mat C) = \tr(\mat C\mat A\mat B))\\
&= -2(\mat\Sigma^{-1}\vect\mu)\T\vect T_1(\vect x) + \tr\bigl[\mat\Sigma^{-1}\vect T_2(\vect x)\bigr] + n\vect\mu\T\mat\Sigma^{-1}\vect\mu
\end{aligned}
$$
[A small ink blot sits on the first $\vect x_j$ in the fifth line.]
where the first term in the expression is given by
$$
\begin{aligned}
\tr\bigl[-2\vect T_1(\vect x)\vect\mu\T\mat\Sigma^{-1}\bigr] &= -2\tr\bigl[\mat\Sigma^{-1}\vect T_1\vect\mu\T\bigr] && \text{cyclic}\\
&= -2\vect\mu\T(\mat\Sigma^{-1}\vect T_1) && \tr[\vect a\vect b\T] = \vect b\T\vect a\\
&= -2\vect T_1\T\mat\Sigma^{-1}\vect\mu && (\mat A\mat B)\T = \mat B\T\mat A\T,\ \mat\Sigma^{-\top} = \mat\Sigma^{-1}\\
&= -2(\mat\Sigma^{-1}\vect\mu)\T\vect T_1
\end{aligned}
$$
[A hatched box crosses out one line between the last two lines (it reads roughly "$-2(\mat\Sigma^{-1}\vect\mu)\T\vect T_1$", rewritten below it). The three justifications are written to the right with braces.]

*Figure:* none.

---

### HW 12 (`20261122_011116.jpg`): Multivariate normal is in regular exponential (derivation, 2)

**Multivariate normal is in regular exponential** [top-right number "4"]

**N.** On substituting the final term we obtain
$$
\begin{aligned}
\log L(\vect\theta) &= -\frac{np}{2}\log(2\pi) - \frac n2\log\abs{\mat\Sigma}\\
&\qquad + (\mat\Sigma^{-1}\vect\mu)\T\vect T_1(\vect x) + \tr\Bigl(\bigl(-\tfrac12\mat\Sigma^{-1}\bigr)\vect T_2(\vect x)\Bigr) - \tfrac12 n\vect\mu\T\mat\Sigma^{-1}\vect\mu\\
&= -\frac{np}{2}\log(2\pi) - \frac n2\log\abs{\mat\Sigma}\\
&\qquad + \vect c_1(\vect\theta)\T\vect T_1(\vect x) + \tr\bigl[\vect c_2(\vect\theta)\T\vect T_2(\vect x)\bigr] - \tfrac12 n\vect\mu\T\mat\Sigma^{-1}\vect\mu
\end{aligned}
$$
Therefore, the multivariate normal distribution has a regular exponential family form, with
$$\vect c_1(\vect\theta) = \mat\Sigma^{-1}\vect\mu \qquad \vect c_2(\vect\theta) = -\tfrac12\mat\Sigma^{-1}$$
$$\vect T_1(\vect x) = \textstyle\sum_j\vect x_j \qquad \vect T_2(\vect x) = \sum_j\vect x_j\vect x_j\T$$
[Checked: $-\tfrac12\times$ the expression from HW 11 gives the line above.]

**Rem.** Note that
$$\tr\bigl[\vect c_2(\vect\theta)\T\vect T_2(\vect x)\bigr] = \bigl(\operatorname{vec}(\vect c_2(\vect\theta))\bigr)\T\operatorname{vec}(\vect T_2(\vect x))$$
where, for $\mat A \in \R^{m\times n}$,
$$\operatorname{vec}(\mat A) = [a_{11},\dots,a_{m1},a_{12},\dots,\dots,a_{1n},\dots,a_{mn}]\T$$

*Figure:* none. [Lower third blank.]

---

### HW 13 (`20261122_011134.jpg`): Fisher and observed information

**Fisher and observed information** [top-right number "3"]

**Def.** Suppose $L(\vect\theta)$ belongs to the regular exponential family. Define the Fisher information $\mathcal I(\vect\theta)$ as the variance of the score statistic:
$$\mathcal I(\vect\theta) = \Var\Bigl[\frac{\partial}{\partial\vect\theta}\log L(\vect\theta)\Bigr] = \E\Bigl[\frac{\partial}{\partial\vect\theta}\log L(\vect\theta)\Bigr]^2$$
Define the observed information $I(\hat{\vect\theta})$ by
$$I(\hat{\vect\theta}) = -\frac{\partial^2\log L(\vect\theta)}{\partial\vect\theta\,\partial\vect\theta\T}\bigg|_{\vect\theta=\hat{\vect\theta}}$$
Then the observed information matrix $I(\hat{\vect\theta})$ at $\vect\theta = \hat{\vect\theta}$ is equal to the Fisher information matrix $\mathcal I(\hat{\vect\theta})$ at $\vect\theta = \hat{\vect\theta}$.
[Notation: the notes write the Fisher and the observed information with the same handwritten capital I; they are told apart here as $\mathcal I$ (Fisher, expected) and $I$ (observed), as in LN3 (17)–(22). "doserved" is written for "observed" in the second sentence. possible error: for vector $\vect\theta$, $\E[\cdot]^2$ should be $\E\bigl[\vect S\vect S\T\bigr]$ with $\vect S$ the score; the square is outside the bracket as written.]

**P.** The score statistic of the REF is given by
$$\frac{\partial}{\partial\vect\theta}\log L(\vect\theta) = \nabla\vect c(\vect\theta)\T\vect T(\vect x) - \nabla\log a(\vect\theta)$$
Differentiate:
$$\frac{\partial^2}{\partial\vect\theta\,\partial\vect\theta\T}\log L(\vect\theta) = \bigl[\nabla\nabla\T\vect c(\vect\theta)\T\bigr]\vect T(\vect x) - \bigl[\nabla\nabla\T\bigr]\log a(\vect\theta)$$
$$\implies I(\hat{\vect\theta}) = -\bigl[\nabla\nabla\T\vect c(\hat{\vect\theta})\T\bigr]\vect T(\vect x) + \bigl[\nabla\nabla\T\bigr]\log a(\hat{\vect\theta}) \qquad [1]$$
[The minus sign in the "Differentiate" line is partly covered by a small ink blot.]
On the other hand, take the expectation:
$$\E\bigl[I(\hat{\vect\theta})\bigr] = \mathcal I(\hat{\vect\theta}) = -\bigl[\nabla\nabla\T\vect c(\hat{\vect\theta})\T\bigr]\E_{\hat{\vect\theta}}[\vect T(\vect X)] + \bigl[\nabla\nabla\T\bigr]\log a(\hat{\vect\theta}) \qquad [2]$$
As $L(\vect\theta)$ belongs to the REF, we have
$$\vect T(\vect x) = \E_{\hat{\vect\theta}}[\vect T(\vect X)]$$
and applying this to [1] and [2] we obtain the result.
[$\E[I(\hat{\vect\theta})]$: the expectation of the observed information evaluated at $\hat{\vect\theta}$ (the notes' shorthand for LN3 (22)); the equality $\E[I(\vect\theta)] = \mathcal I(\vect\theta)$ is result (2) of HW 14.]

*Figure:* none.

---

### HW 14 (`20261122_011139.jpg`): 2004 results under regularity conditions

**2004 results under regularity conditions** [top-right number "3"; "2004" = STAT2004]

**Def.** Under the following regularity conditions:
1. Support of $f$ independent of $\vect\theta$
2. $\Omega$ is an open interval (of $\R$)
3. $\partial/\partial\vect\theta\, f(x;\vect\theta)$ exists for all $\vect\theta$
4. $\mathcal I(\vect\theta) > 0$ for all $\vect\theta$
5. The integral $\int\!\cdots\!\int L(\vect\theta;\vect x)\dd\vect x$ can be differentiated under the integral sign w.r.t. $\vect\theta$.
6. The integral $\int\!\cdots\!\int L(\vect\theta;\vect x)\,T(\vect x)\dd\vect x$ can similarly be differentiated under the integral sign w.r.t. $\vect\theta$.

the following results hold:
1. $\E\Bigl[\dfrac{\partial\log L(\vect\theta)}{\partial\vect\theta}\Bigr] = \vect 0$ (expectation of score statistic is zero)
2. $\mathcal I(\vect\theta) = \E[I(\vect\theta)]$
3. $\Var(T) \ge \dfrac{(g'(\theta))^2}{\mathcal I(\theta)}$ (Cramér–Rao lower bound)

[Labelled "Def." although it states results. possible error (omission): result 3 holds for an unbiased estimator $T$ of $g(\theta)$; neither $T$ nor $g$ is defined on the page (compare BN, Cramér–Rao section).]

**P.** We first prove result (1):
As $L(\vect\theta)$ is a p.d.f. of $\vect x$,
$$\int\!\cdots\!\int L(\vect\theta)\dd\vect x = 1$$
Differentiate (w.r.t. $\vect\theta$):
$$
\begin{aligned}
&\int\!\cdots\!\int\frac{\partial L(\vect\theta)}{\partial\vect\theta}\dd\vect x = 0\\
\implies &\int\!\cdots\!\int\frac{\partial\log L(\vect\theta)}{\partial\vect\theta}L(\vect\theta)\dd\vect x = 0\\
\implies &\E\Bigl[\frac{\partial\log L(\vect\theta)}{\partial\vect\theta}\Bigr] = 0
\end{aligned}
$$

*Figure:* none. [Lower quarter blank.]

---

### HW 15 (`20261122_011145.jpg`): 2004 results under regularity conditions (continued)

**2004 results under regularity conditions** [top-right number "3"]

**P.** We now prove result (2):
Differentiate again (w.r.t. $\theta$):
$$
\begin{aligned}
&\int\!\cdots\!\int\frac{\partial}{\partial\theta}\Bigl[\frac{\partial\log L(\theta)}{\partial\theta}L(\theta)\Bigr]\dd\vect x = 0\\
\implies &\int\!\cdots\!\int\frac{\partial^2\log L(\theta)}{\partial\theta^2}L(\theta) + \Bigl(\frac{\partial\log L(\theta)}{\partial\theta}\Bigr)^2 L(\theta)\dd\vect x = 0\\
\implies &\E\Bigl[\frac{\partial^2\log L(\theta)}{\partial\theta^2}\Bigr] + \E\Bigl[\Bigl(\frac{\partial\log L(\theta)}{\partial\theta}\Bigr)^2\Bigr] = 0\\
\implies &-\E[I(\vect\theta)] + \mathcal I(\theta) = 0
\end{aligned}
$$
[The last step uses $\E[S^2] = \Var(S)$ because $\E S = 0$ by result (1), not stated.]

We finally prove result (3):
Let $T$ be an unbiased estimator of $g(\theta)$. Then,
$$g(\theta) = \E(T) = \int\!\cdots\!\int T\,L(\theta)\dd\vect x$$
Differentiate (w.r.t. $\theta$):
$$
\begin{aligned}
g'(\theta) &= \int\!\cdots\!\int T\,\frac{\partial L(\theta)}{\partial\theta}\dd\vect x\\
&= \int\!\cdots\!\int T\,\frac{\partial\log L(\theta)}{\partial\theta}L(\theta)\dd\vect x\\
&= \E\Bigl[T\,\frac{\partial\log L(\theta)}{\partial\theta}\Bigr]\\
&= \Cov\Bigl(T, \frac{\partial\log L(\theta)}{\partial\theta}\Bigr)
\end{aligned}
$$
by $\Cov(X,Y) = \E[XY] - \E X\,\E Y$, and result (1).
By the Cauchy–Schwartz inequality:
$$
\begin{aligned}
[g'(\theta)]^2 &= \Bigl[\Cov\Bigl(T, \frac{\partial\log L(\theta)}{\partial\theta}\Bigr)\Bigr]^2\\
&\ge \Var[T]\,\Var\bigl[\partial\log L(\theta)/\partial\theta\bigr]\\
&= \Var[T]\,\mathcal I(\theta)
\end{aligned}
$$
[possible error: the inequality is reversed; Cauchy–Schwarz gives $[\Cov(T,S)]^2 \le \Var(T)\Var(S)$, which yields $\Var(T) \ge [g'(\theta)]^2/\mathcal I(\theta)$. "Schwartz" as written.]

*Figure:* none.

---

### HW 16 (`20261122_011152.jpg`): Cramér–Rao lower bound, MVB estimators

**Cramér–Rao lower bound, MVB estimators** [top-right number "5"; a second "7" in the right margin beside the third block]

**Def.** Let $\vect T$ be an unbiased estimator of $\vect g(\vect\theta)$. Let $\vect\theta \in \R^d$ be a parameter vector. Then,
$$\Cov[\vect T] \succeq \vect g'(\vect\theta)\,\mathcal I^{-1}(\vect\theta)\,\vect g'(\vect\theta)\T$$
where $\vect g'(\vect\theta)$ is the Jacobian of $\vect g(\vect\theta)$, and the relation $\succeq$ refers to positive semi-definiteness.
[Labelled "Def."; this is the multivariate Cramér–Rao lower bound (LN5).]

**P.** The proof is beyond the scope of this course. See Bickel & Doksum. [The notes give the year of the reference; omitted here under the no-dates rule.]

**Def.** *Minimum variance bound (MVB) estimators.* Let $T$ be an unbiased estimator of $g(\theta)$. Then $T$ is an MVBE of $g(\theta)$ if its covariance attains equality in the Cramér–Rao lower bound.

**Def.** *CRLB on biased estimators.* Let $T$ be a biased estimator of $\theta$ with bias $b(\theta)$. Then $T$ is an unbiased estimator of
$$g(\theta) = \theta + b(\theta)$$
and so
$$\Var(W) \ge \frac{[g'(\theta)]^2}{\mathcal I(\theta)} = \frac{[1 + b'(\theta)]^2}{\mathcal I(\theta)}$$
which implies
$$\MSE(W) \ge \frac{[1 + b'(\theta)]^2}{\mathcal I(\theta)} + [b(\theta)]^2$$
[possible error: the estimator is called $T$ in the text and $W$ in the two displays. An ink blot sits inside the bracket of $(b'(\theta))$ in the first display.]

*Figure:* none.

---

### HW 17 (`20261122_011158.jpg`): CRLB, MVB estimators (example)

**CRLB, MVB estimators (example)** [top-right number "5"]

**Ex.** Suppose $X \sim \Normal(\mu,\sigma^2)$ where $\mu$ is known. Then $\theta = \sigma^2$.
We can show that the MLE of $\sigma^2$ is (exercise)
$$\hat\sigma^2 = \frac1n\textstyle\sum_j(x_j - \mu)^2$$
We now show it attains the MVB.
As an exercise, we know that
$$\mathcal I(\theta) = \frac{n}{2\sigma^4}$$
The variance of $\hat\sigma^2$ is
$$\Var\Bigl[\frac{n\hat\sigma^2}{\sigma^2}\Bigr] = \frac{n^2}{\sigma^4}\Var[\hat\sigma^2] = 2n \qquad \Bigl(\frac{n\hat\sigma^2}{\sigma^2} \sim \ChiSq{n}\Bigr)$$
which implies $\Var[\hat\sigma^2] = 2\sigma^4/n$. Thus it attains the MVB.

**Ex.** Now suppose $X \sim \Normal(\mu,\sigma^2)$ where now $\mu$ is not known. Then $\vect\theta = (\mu,\sigma^2)\T$.
Consider the estimator $\vect T = (\bar x, s^2)\T$, which is an unbiased estimator of $\vect\theta$. Then,
$$\vect g'(\vect\theta) = \mat I \qquad \mathcal I(\vect\theta) = \diag(n/\sigma^2,\ n/2\sigma^4)$$
and by the CRLB,
$$\Cov(\vect T) \succeq \mathcal I^{-1}(\vect\theta) = \diag(\sigma^2/n,\ 2\sigma^4/n)$$
The variance of $s^2$ is
$$\Var\Bigl[\frac{(n-1)s^2}{\sigma^2}\Bigr] = \frac{(n-1)^2}{\sigma^4}\Var[s^2] = 2(n-1) \qquad \Bigl(\frac{(n-1)s^2}{\sigma^2} \sim \ChiSq{n-1}\Bigr)$$
which implies $\Var[s^2] = 2\sigma^4/(n-1)$.
It follows that $\vect T$ therefore does not attain the CRLB, and thus is not the MVB estimator.
[$\vect g'(\vect\theta) = \mat I$ is the $2\times2$ identity matrix; in the notes it is the same handwritten "I" as the information. The CRLB is written with "≥" here and "⪰" on HW 16. Checked: $2\sigma^4/(n-1) > 2\sigma^4/n$. Compare LN5 pp. 3–5.]

*Figure:* none.

---

### HW 18 (`20261122_011203.jpg`): Sufficiency

**Sufficiency** [top-right number "5"; the heading replaces a crossed-out heading "CRLB, MVB estimators (example)" in a solid ink box at top left]

**Def.** Sufficient statistics contain all information about $\vect\theta$ contained in $\vect x$. No other statistic can provide any additional information about $\vect\theta$.

Mathematically, a statistic is sufficient if the conditional distribution $\vect X \given \vect T(\vect x)$ does not depend on $\vect\theta$.

If $\vect T = \vect H(\vect U)$ is sufficient for $\vect\theta$, then $\vect U$ is also sufficient for $\vect\theta$.

**Def.** A sufficient statistic is minimal sufficient if it is a function of all other sufficient statistics. Minimal sufficient statistics provide the greatest possible reduction of data.

**Def.** A sufficient statistic $T$ is complete if
$$\E(g(T)) = 0 \implies g(T) = 0 \qquad \forall\,\theta \in \Omega$$
A complete statistic is always minimal.
[possible error: the quantifiers are misplaced; the standard form is "$\E_\theta[g(T)] = 0$ for all $\theta \in \Omega$ implies $\Prob_\theta(g(T) = 0) = 1$ for all $\theta$" (BN, completeness). "A complete statistic is always minimal" holds for complete *sufficient* statistics, as the definition's first line intends.]

**Rem.** The sufficient statistic given in a regular exponential family is complete, and therefore minimal.

**Def.** *Fisher–Neyman theorem.* A statistic $T$ is sufficient for $\vect\theta$ iff the p.d.f. of the data $\vect x$ can be factored into
$$f(\vect x;\theta) = h_1[T(\vect x);\theta]\,h_2[\vect x] \qquad \forall\,\vect\theta \in \Omega$$
where $h_1, h_2$ are non-negative functions.

*Figure:* none.

---

### HW 19 (`20261122_011214.jpg`): Rao–Blackwell theorem

**Rao–Blackwell theorem** [no top-right number visible; a stray "Ex" in the left margin belongs to the facing page]

**Th.** *Rao–Blackwell theorem.* Let $U(\vect X_1,\dots,\vect X_n)$ be an unbiased estimator of $\vect\theta$. Suppose that $T(\vect X_1,\dots,\vect X_n)$ is a sufficient statistic for $\theta$. Let
$$W\bigl(T(\vect X_1,\dots,\vect X_n)\bigr) = \E\bigl[U(\vect X_1,\dots,\vect X_n) \given T(\vect X_1,\dots,\vect X_n)\bigr]$$
Then,
1. $U(T(\vect x))$ does not rely on $\theta$ (only on $T$).
2. $W(T(\vect x))$ is an unbiased estimator of $\theta$
3. $\Var[W(T)] < \Var[U]$

[possible error: in (1) the statistic that does not depend on $\theta$ is $W(T(\vect x))$, not $U(T(\vect x))$. In (3) the inequality should be $\le$ (the proof below ends with "$>$" but only $\E[\Var(U \given T)] \ge 0$ is shown; equality holds when $U$ is already a function of $T$).]

**P.** We prove all three statements:
1. The conditional distribution of $\vect X_1,\dots,\vect X_n$, and thus any function of $\vect X_1,\dots,\vect X_n$ given $T(\vect x_1,\dots,\vect x_n)$, does not depend on $\theta$, as $T$ is sufficient for $\theta$.
2. By the tower property,
$$\E[W(T)] = \E\bigl[\E[U(\vect X) \given T(\vect X)]\bigr] = \E[U(\vect X)] = \theta$$
3. By the law of total variance,
$$
\begin{aligned}
\Var[U] &= \Var[\E(U \given T)] + \E[\Var(U \given T)]\\
&= \Var[W(T)] + \E[\Var(U \given T)]\\
&> \Var[W(T)]
\end{aligned}
$$

*Figure:* none.

---

### HW 20 (`20261122_011218.jpg`): UMVUE, Lehmann–Scheffé theorem

**UMVUE, Lehmann–Scheffé theorem** [top-right number blank]

**Def.** The uniform minimum-variance unbiased estimator (UMVUE) is the unique unbiased estimator with the lowest variance of all unbiased estimators, for all parameters $\theta \in \Omega$.

**Rem.** If the MVB estimator exists, it must be the UMVUE. The converse statement does not hold — the variance of the UMVUE may not necessarily attain the Cramér–Rao LB.

**Th.** *Lehmann–Scheffé theorem.* Suppose $T$ is a complete, sufficient statistic for $\theta$. Let $W(T)$ be an unbiased estimator of $\theta$ with finite variance. Then,
1. $W(T)$ is a UMVUE of $\theta$.
2. $W(T)$ is unique.

**P.** By Rao–Blackwell, restrict possible estimators to functions of $T$ alone. We show uniqueness.

Let $Q(T)$ be another unbiased estimator of $\theta$. Then
$$\E[W(T) - Q(T)] = 0 \qquad \forall\,\theta \in \Omega$$
implying that
$$W(T) \equiv Q(T)$$
and so $W(T)$ is unique, with variance not greater than that of any other unbiased estimator. Therefore, $W(T)$ is a UMVUE of $\theta$.
[The step "implying that $W(T) \equiv Q(T)$" uses the completeness of $T$ (HW 18), not named. "Scheffé" is written "Scheffé" in the heading and "Scheffè" in the theorem.]

*Figure:* none.

---

### HW 21 (`20261122_011232(0).jpg`): Jensen's inequality, KL divergence

**Jensen's inequality, KL divergence** [top-right number "6"; the heading follows a crossed-out word in a solid ink box ("Jensen's inequality" written and struck through)]

**Def.** *Jensen's inequality.* Let $h$ be a convex function, and let $X$ have mean $\mu$. Then,
$$\E[h(X)] \ge h(\mu)$$
[A stray "T" in the left margin before "Def." A word between "Jensen's" and "inequality" is crossed out in a solid box.]

**Rem.** A function $h$ is convex if $\forall\,x,y \in \R$, $\forall\,\alpha \in [0,1]$
$$h(\alpha x + (1-\alpha)y) \le \alpha h(x) + (1-\alpha)h(y)$$
If $h$ is twice differentiable with $h''(x) \ge 0$ for all $x$, then $h$ is convex.

**Def.** *Kullback–Leibler (KL) divergence.* Let $f_1, f_2$ be the p.d.f. of two distribution functions. The KL divergence between $f_1$ and $f_2$ is
$$\mathrm{KL}[f_1 \,\|\, f_2] = \delta_{KL} = \int f_1(x)\log\Bigl(\frac{f_1(x)}{f_2(x)}\Bigr)\dd x$$
KL divergence measures how different the distributions $f_1$ and $f_2$ are.

**Def.** KL divergence is non-negative, i.e.
$$\mathrm{KL}[f_1 \,\|\, f_2] \ge 0$$
[Labelled "Def." although it is a result.]

**P.** We have that
$$
\begin{aligned}
\delta_{KL}(F_1,F_2) &= \int f_1(x)\log\Bigl(\frac{f_1(x)}{f_2(x)}\Bigr)\dd x\\
&= -\int f_1(x)\log\Bigl(\frac{f_2(x)}{f_1(x)}\Bigr)\dd x\\
&= -\E_{F_1}\Bigl[\log\Bigl(\frac{f_2(X)}{f_1(X)}\Bigr)\Bigr]\\
&= \E_{F_1}\Bigl[-\log\Bigl(\frac{f_2(X)}{f_1(X)}\Bigr)\Bigr]\\
&\ge -\log\Bigl[\E_{F_1}\Bigl[\frac{f_2(X)}{f_1(X)}\Bigr]\Bigr]
\end{aligned}
$$
by Jensen's inequality. [continued on HW 22]
[Notation switches from $\mathrm{KL}[f_1\|f_2]$ and $\delta_{KL}$ to $\delta_{KL}(F_1,F_2)$ (distribution functions). Jensen is applied to the convex $h(x) = -\log x$ (LN6), not named here.]

*Figure:* none.

---

### HW 22 (`20261122_011244.jpg`): KL divergence

**KL divergence** [top-right number "6"]

**P.** Therefore,
$$
\begin{aligned}
\delta_{KL}(F_1,F_2) &\ge -\log\Bigl[\E_{F_1}\Bigl[\frac{f_2(X)}{f_1(X)}\Bigr]\Bigr]\\
&= -\log\Bigl[\int f_1(x)\cdot\frac{f_2(x)}{f_1(x)}\dd x\Bigr]\\
&= -\log\Bigl[\int f_2(x)\dd x\Bigr]\\
&= -\log 1 = 0
\end{aligned}
$$
which proves the result.

**Rem.** Other useful properties of KL divergence are:
- Not symmetric: $\delta_{KL}(F_1,F_2) \ne \delta_{KL}(F_2,F_1)$
- Non-degenerate: $\delta_{KL}(F_1,F_2) = 0 \implies F_1 = F_2$

["≠" means "not equal in general". Neither property is proved.]

*Figure:* none. [Two-thirds of the page blank; a large shadow covers the lower half but nothing is written there.]

---

### HW 23 (`20261122_011330.jpg`): Loss and risk functions

**Loss and risk functions** [top-right number "7"]

**Def.** Let $W$ be some estimator of $\theta$ and let $\ell(W,\theta)$ denote the loss function in estimating $\theta$ using $W$. The inaccuracy of $W$ is measured by the risk function
$$R(W;\theta) = \E[\ell(W,\theta)]$$

**Rem.** Until now, we have defined the loss function by squared error:
$$\ell(W,\theta) = (W - \theta)^2$$
and (exercise) risk function by mean squared error:
$$R(W;\theta) = \Var(W) + \bias(W)^2 = \E[(W - \theta)^{?}]$$
[The last expression is written $\E[(W-\theta)]$; a square is either missing or too faint to see (checked on a zoomed crop; a photo retake may help). The intended expression is $\E[(W-\theta)^2]$, from the line above.]

*Figure:* none. [Lower half of the page blank.]

---

### HW 24 (`20261122_011334.jpg`): Generalising Rao–Blackwell

**Generalising Rao–Blackwell** [top-right number "7"]

**Th.** *Rao–Blackwell theorem (equivalent definition).* Let $U$ be a (possibly biased) estimator of $\theta$. Let $T$ be a sufficient statistic for $\theta$. Let $U(T) = \E[U \given T]$. Then,
$$\MSE[W] \le \MSE[U]$$
[possible error: the conditional expectation is named $U(T)$ but the conclusion uses $W$; it should read $W(T) = \E[U \given T]$, as in the next theorem.]

**P.** The biases of $U$ and $W$ remain unchanged by the tower property. The variance of $W$ is less than the variance of $U$ by the law of total variance. Thus, the result follows.
["remain unchanged": $W$ has the same bias as $U$. "less than" should be "no greater than" (see HW 19).]

**Th.** *Generalised Rao–Blackwell theorem.* We extend the Rao–Blackwell theorem to any convex loss function. Let $U$ be an estimator of $\theta$. Let $T$ be a sufficient statistic for $\theta$. Define $W(T) = \E[U \given T]$. Then,
$$R(W;\theta) \le R(U;\theta)$$

**P.** By the tower property and Jensen's inequality:
$$
\begin{aligned}
R(U;\theta) &= \E[\ell(U,\theta)]\\
&= \E\bigl[\E[\ell(U,\theta) \given T]\bigr]\\
&\ge \E\bigl[\ell(\E[U \given T],\theta)\bigr]\\
&= R(W;\theta)
\end{aligned}
$$
[The Jensen step is the conditional form of Jensen's inequality for the convex function $\ell(\cdot,\theta)$; HW 21 states only the unconditional form.]

*Figure:* none.

---

### HW 25 (`20261122_011347.jpg`): Basu's theorem

**Basu's theorem** [top-right number "8"]

**Def.** A statistic $V$ is ancillary if its distribution does not depend on $\vect\theta$. Ancillary statistics contain no information about the model parameters.

**Th.** *Basu's theorem.* Let $T$ be a complete sufficient statistic for $\vect\theta$. Let $V$ be an ancillary statistic to $\vect\theta$. Then $T$ and $V$ are independent.

**P.** We work in the case of discrete random variables. For some fixed $V = v$, and some p.d.f. $f$,
$$
\begin{aligned}
\E\bigl[f(v \given T) - f(v)\bigr] &= \E\Bigl[\frac{f(v,T)}{f(T)}\Bigr] - f(v)\\
&= \textstyle\sum_t\dfrac{f(v,t)}{f(t)}f(t) - f(v)\\
&= \textstyle\sum_t f(v,t) - f(v)\\
&= f(v) - f(v) \qquad \forall\,\vect\theta \in \Omega
\end{aligned}
$$
As $T$ is complete sufficient, $f(v \given t)$ does not depend on $\theta$.
As $V$ is ancillary, $f(v)$ does not depend on $\theta$.
It follows that $f(v \given t) \equiv f(v)$, implying that $f(v \given t)$ does not depend on $t$.
Therefore, $V$ is distributed independently of $T$.
[possible error: the roles are mixed. Sufficiency alone gives that $f(v \given t)$ does not depend on $\theta$, so $f(v \given T) - f(v)$ is a statistic; completeness is what turns "expectation $0$ for all $\theta$" into $f(v \given t) \equiv f(v)$ (LN8 p. 1–2). "p.d.f." is used for the discrete p.f.]

*Figure:* none. [Lower third blank.]

---

### HW 26 (`20261122_011354.jpg`): 2004 large sample theory, consistency

**2004 large sample theory, consistency** [top-right number "8"]

**N.** Large sample theory assumes that the sample size $n$ is large. This is useful especially if the distribution of an estimator is complicated or unknown, as we are no longer reliant on knowing the exact model or loss.

We assess the performance of a sequence of estimators $T_n$ as $n \to \infty$. As $n$ increases we expect more information about $\vect\theta$, which improves estimation. While we cannot expect $T_n$ to be close to $\vect\theta$ for every sample, we can aim for closeness with high probability.

**Def.** *Consistency.* A sequence of estimators $T_n$ of $g(\vect\theta)$ is consistent if
$$T_n \xrightarrow{P_\theta} g(\vect\theta) \qquad \text{i.e. } T_n \text{ converges in probability to } g(\vect\theta).$$
That is,
$$\Prob\bigl(\abs{T_n - g(\vect\theta)} \ge \varepsilon\bigr) \to 0 \qquad \text{as } n \to \infty.$$
If $\bias(T_n) \to 0$ and $\Var(T_n) \to 0$, then $T_n$ is consistent.
[The convergence arrow carries "$P_\theta$" (convergence in probability under $\theta$); the book's macro is `\convp`. "for every $\varepsilon > 0$" is not written.]

**P.** We have
$$\Prob\bigl[\abs{T_n - g(\vect\theta)} \ge \varepsilon\bigr] = \int\!\cdots\!\int_{\abs{T_n - g} \ge \varepsilon} f(\vect x;\vect\theta)\dd\vect x$$
On the region of integration, $(T_n - g)^2/\varepsilon^2 \ge 1$. Thus,
$$f(\vect x;\vect\theta) \le f(\vect x;\vect\theta)\cdot\frac{(T_n - g)^2}{\varepsilon^2}$$
Therefore,
$$
\begin{aligned}
\Prob\bigl[\abs{T_n - g(\vect\theta)} \ge \varepsilon\bigr] &\le \int\!\cdots\!\int_{\abs{T_n - g} \ge \varepsilon}\frac{(T_n - g)^2}{\varepsilon^2}f(\vect x;\vect\theta)\dd\vect x\\
&\le \frac{1}{\varepsilon^2}\int\!\cdots\!\int\frac{(T_n - g)^2}{1}f(\vect x;\vect\theta)\dd\vect x\\
&= \frac{1}{\varepsilon^2}\MSE(T_n)
\end{aligned}
$$
which tends to zero as $n \to \infty$, as $\Var(T_n),\ \bias(T_n) \to 0$.
[The last step uses $\MSE = \Var + \bias^2$ (HW 23), not restated. A stray "8" sits in the left margin (facing page number).]

*Figure:* none.

---

### HW 27 (`20261122_011403.jpg`): Asymptotic relative efficiency

**Asymptotic relative efficiency** [top-right number "8"]

**Def.** *ARE (asymptotic relative efficiency).* Let $T_1, T_2$ be estimators of $g(\theta)$, where as $n \to \infty$,
$$\sqrt n\,[T_i - g(\vect\theta)] \xrightarrow{\ \ell\ } \Normal(0,\tau_i^2) \qquad \ast$$
or equivalently,
$$T_i \sim \Normal(g(\theta),\ \tau_i^2/n)$$
Then the ARE of $T_2$ w.r.t. $T_1$ is given by
$$\mathrm{ARE}(T_2) = \tau_1^2/\tau_2^2$$
If the ARE is $x$, [blotted] $T_2$ is $x$ as efficient as $T_1$.
[A small hatched blot precedes "ARE" in the heading, and a solid ink block covers one or two words before "$T_2$ is $x$ as efficient". The second display is approximate for large $n$ ("$\sim$" as written; "$\overset{\cdot}{\sim}$" would be the usual reading).]

**Ex.** Let $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$. Then,
$$\sqrt n(\bar X - \mu) \sim \Normal(0,\sigma^2)$$
$$\sqrt n(\tilde X - \mu) \xrightarrow{\ \ell\ } \Normal(0,\tau^2) \qquad \text{where } \tau^2 = \sigma^2(\phi(0))^{-2}/4 = \frac\pi2\sigma^2$$
Then
$$\mathrm{ARE}(\tilde X) = \sigma^2 \div \frac\pi2\sigma^2 = \frac2\pi = 0.637$$
and so $\tilde X$ is not as efficient as $\bar X$.
[$\tilde X$ = sample median, $\phi$ = standard normal density; neither is defined on the page. Checked: $\phi(0)^{-2}/4 = 2\pi/4 = \pi/2$; $2/\pi = 0.6366$.]

$\ast$ In other words, $\sqrt n[T_i - g(\vect\theta)]$ converges in distribution to $\Normal(0,\tau_i^2)$. The '$\ell$' stands for 'law', an archaic term for distribution.
[The book's macro for this arrow is `\convd`.]

*Figure:* none.

---

### HW 28 (`20261122_011409.jpg`): Asymptotic efficiency

**Asymptotic efficiency** [top-right number "8"]

**N.** In large samples, estimators are ideally consistent as well as asymptotically normal with variance $v(\theta)$. We want estimators that uniformly minimise $v(\theta)$.

**Rem.** Maximum likelihood is a fairly explicit method of obtaining asymptotic efficient estimators.

**Rem.** Large, asymptotically [blotted] optimal estimators need not be unique. The same limiting behaviour can be shared by different sequences. In particular, let $T_n$ be asymptotically optimal and asymptotically normal, i.e.
$$\sqrt n\bigl(T_n - g(\theta)\bigr) \xrightarrow{\ \ell\ } \Normal(0;v(\theta))$$
Then $T_n + R_n$ is also optimal if
$$\sqrt n R_n \xrightarrow{\ p\ } 0$$
[One word after "asymptotically" is covered by a solid ink block. "Large," as written (presumably "large-sample").]

**Def.** *Asymptotic CRLB.* Suppose the estimator [blot] $T$ is asymptotically normal, i.e.
$$\sqrt n\bigl(T - g(\theta)\bigr) \xrightarrow{\ L\ } \Normal(0,v(\theta))$$
Then under certain regularity conditions,
$$v(\theta) \ge \frac{(g'(\theta))^2}{i(\theta)} \qquad \text{where } i(\theta) = \frac{\mathcal I(\theta)}{n}$$
[$i(\theta)$ is the information in one observation (BN, large-sample theory). The regularity conditions are not listed. Stated without proof.]

**Def.** *Asymptotic efficiency.* An estimator $T_n$ is asymptotically efficient if it is asymptotically normal with variance
$$v(\theta) = \frac{(g'(\theta))^2}{i(\theta)}$$
In other words, the asymptotic CRLB holds in equality.

*Figure:* none.

---

