# Coverage inventory: STAT3004 Probability Models & Stochastic Processes

_Built in the transcription phase from 32 photos of the handwritten notes (Topic 1 only), the typed lecture notes (99 pp., Topics 1–6) and the course guide (33 pp., derived from the lecture notes). Transcriptions: `claude/notes-stat3004-1.md` (HW 01–16), `-2.md` (HW 17–32), `-3.md` (CN and CG index, figures, "only here" lists)._

**Sources.** "HW nn" = handwritten page nn (one page per photo, shooting order). "CN x.y.z" = typed lecture notes item (Definition/Theorem/… number) or § with page. "CG p" = course guide page. **Lead source:** HW for Topic 1 (CN as supplement); CN for Topics 2–6. **Code:** the notes contain no code, only pseudocode algorithms; the book uses **R** for Part III. **Content rule:** source material only, with corrections.

**Status:** all ◻ (to do). **↔ merge** = overlaps a chapter already written (Ch 25–31) or another course's material; the item is merged into that home, not duplicated. **Fig.** references are to the figure descriptions in the notes files.

---

## Ch 2 Sets, Relations and Functions (`ch:sets-relations-functions`) ↔ merge MATH1061
- ◻ ↔ Universal set, examples of finite and infinite sample spaces (coin, die, two dice as a $6\times6$ grid, $[0,1]$, $\R$) (HW 01; CN 1.1.1)
- ◻ ↔ Subset; union, intersection, complement, set difference; empty set (HW 01; CN Def 1.1.1–1.1.2)
- ◻ ↔ Countable unions and intersections; finite versions (HW 01; CN Def 1.1.3)
- ◻ ↔ De Morgan's laws, countable form (HW 02; CN Prop 1.1.4, proof left as exercise in both)
- ◻ ↔ Disjoint, mutually disjoint, $\bigsqcup$ notation; partition (finite or countable) (HW 02; CN Def 1.1.6–1.1.7)
- ◻ Increasing/decreasing sequences of sets and their limits, $A_n\uparrow A$ (HW 02; CN Def 1.1.8) — may sit in Ch 25 instead, next to continuity of $\Prob$
- ◻ ↔ Power set, $\abs{\powerset(\Omega)} = 2^n$ with the two proof sketches (indicator bijection; induction); Ex $\powerset(\{0,1,2\})$ (HW 02; CN Prop 1.1.10, Rem 1.1.11)

## Ch 9 The Real Numbers, Sequences and Series (`ch:real-numbers-sequences-series`) ↔ merge MATH2401/MATH1071
- ◻ ↔ Convergence of a real sequence (ε–N) (HW 23)
- ◻ ↔ limsup and liminf of real sequences; $\liminf \le \limsup$ (HW 09; HW uses them in Fatou)
- ◻ ↔ Little-o and big-O notation, their relationship (CN Rem 5.3.6–5.3.8) — or Ch 11

## Ch 25 Probability Spaces (`ch:probability-spaces`) ↔ merge STAT2003 (σ-algebra remark, axioms, consequences, union bound already written)
- ◻ Algebra (field) of sets; examples on $\{H,T\}$ (enlarging a collection to an algebra); closed under intersections (commutative-square figure) (HW 03; CN Def 1.1.12)
- ◻ Algebras too small: Bernoulli trials, "success eventually" $=\bigcup A_n$ (HW 03; HW only)
- ◻ Monotone class (HW 03; CN Def 1.1.13); σ-algebra ⇒ monotone class, converse fails: $\{\emptyset,\R\}\cup\{(-\infty,x]\}$ (CN Rem 1.1.16)
- ◻ σ-algebra (σ-field); closed under countable intersections, $\emptyset\in\mathcal F$ (HW 04; CN Def 1.1.14, Rem 1.1.15) ↔ STAT2003 σ-algebra remark (Ch 25)
- ◻ Thm σ-algebra ⇔ algebra + monotone class, with proof (HW 04; CN Prop 1.1.17)
- ◻ Examples: trivial σ-algebra, $\powerset(\Omega)$ (largest; too large to be consistent), two coin flips with the "flips agree" σ-algebra (HW 04; CN Ex 1.1.18, Prop 1.1.19)
- ◻ Intersection of σ-algebras is a σ-algebra, **proof only in HW** (HW 04; CN Prop 1.1.21–1.1.22, Rem 1.1.23)
- ◻ Generated σ-algebra $\sigma(\mathcal A)$, smallest containing $\mathcal A$; Ex $\sigma(\{\{H\}\})$ (HW 05; CN Def 1.1.24)
- ◻ Monotone Class Theorem (starred, statement only) (CN Thm 1.1.25)
- ◻ Borel σ-algebra $\mathcal B(\R)$: open sets, closed half-lines, open half-lines (single countable limit); contains intervals and points (no proof; CG gives the constructions); $\abs{\mathcal B(\R)} = \abs{\R} < \abs{\powerset(\R)}$ (HW 05 only, no proof) (HW 05; CN Def 1.1.26, Rem 1.1.27, Prop 1.1.28, Rem 1.1.32; CG 4)
- ◻ Borel σ-algebra on the extended real line (CN Def 1.1.29)
- ◻ Trace σ-algebra; Ex $\Omega = \{0,1,2\}$, $I = \{0,1\}$ gives $\powerset(I)$; $\mathcal B([0,1])$ (HW 06; CN Def 1.1.30, Ex 1.1.31)
- ◻ Measurable space (HW 06; CN Def 1.1.33)
- ◻ ↔ Probability measure (Kolmogorov axioms), probability space (HW 07; CN Def 1.1.34; Ex 1.1.35 $\abs A/4$)
- ◻ ↔ Consequences: $\Prob(\emptyset) = 0$, complement, monotonicity, inclusion–exclusion for two sets (HW), finite subadditivity (CN), with CN's proofs; Boole's inequality (HW 07; CN Prop 1.1.36, Thm 1.1.37, Rem 1.1.38) ↔ STAT2003 consequences and union bound
- ◻ Continuity from below and above, with proof (HW 07; CN Thm 1.1.39) ↔ STAT2003 (if Ch 25 already states continuity, merge)
- ◻ Lebesgue measure: picking a point in $[0,1]$ (number-line figure, HW 08), $\lambda((a,b]) = b-a$, why not all of $\powerset([0,1])$ (partition argument sketched in HW 08 without construction; CN Rem 1.1.40); uniform probability space $([0,1],\mathcal B([0,1]),\lambda)$ (HW 08; CN §1.1.5, Ex 1.1.41)
- ◻ limsup/liminf of events, $\{A_n \text{ i.o.}\}$, $\{A_n \text{ a.b.f.m.}\}$, membership characterisation, a.b.f.m. ⊆ i.o. with example, theorem "i.o. = limsup" with two-inclusion proof (HW 09–10; CN Def 1.1.42)
- ◻ Properties: $\liminf A_n = (\limsup A_n^c)^c$; monotone sequences; $\Prob(\limsup A_n) \ge \limsup\Prob(A_n)$, $\Prob(\liminf A_n) \le \liminf\Prob(A_n)$ (HW 10, stated as exercise; CN Rem 1.1.43 has the first only)
- ◻ Borel–Cantelli I with proof (HW: continuity from above; CN: Boole) and Ex $\Prob(A_n) = 1/n^2$ (HW 11; CN Lemma 1.1.44; CG 5)
- ◻ Borel–Cantelli II with proof ($1-x\le e^{-x}$) and Ex $\Prob(A_n) = 1/n$ (HW 12; CN Lemma 1.1.45); remarks on dropping independence and on $\Prob(A_n^c \text{ i.o.})$ (CN Rem 1.1.46–1.1.47)
- ◻ ↔ Laws of total probability and total expectation conditional on an event $C$ (CN Lecture rem 3.2.5) ↔ STAT2003 Ch 25, Ch 31

## Ch 26 Random Variables and Distribution Functions (`ch:random-variables`) ↔ merge STAT2003
- ◻ ↔ Random variable as an $\mathcal F/\mathcal B(\R)$-measurable map, preimage; need not be invertible; $\Prob$ not needed (map figure) (HW 13; CN Def 1.2.1) ↔ STAT2003 $X:\Omega\to E$
- ◻ Ex indicator $I_{[0,p]}$ on $[0,1]$: four-case measurability check (figure); not measurable for a small $\mathcal F$, measurable for $\sigma([0,p])$ (HW 13; HW only)
- ◻ $X$ is a random variable iff $\{X\le x\}\in\mathcal F$ for all $x$ (HW 13; CN Prop 1.2.2, reason in Rem 1.2.3)
- ◻ Indicator is a random variable (HW 17; CN Def 1.2.11)
- ◻ ↔ Distribution (law) $\mu_X$ as a probability measure on $(\R,\mathcal B(\R))$ (HW 14; CN Def 1.2.5) ↔ STAT2003 "probability distribution"
- ◻ ↔ cdf; Ex cdf of $I_{[0,p]}$ under Lebesgue measure; properties (monotone, right-continuous, limits) with CN proof (HW 14; CN Def 1.2.6, Prop 1.2.7) ↔ STAT2003 CDF properties (merge the proof)
- ◻ Lebesgue decomposition of a cdf (discrete, absolutely continuous, singular; Cantor function) (CN Rem 1.2.8)
- ◻ Borel-measurable function $g$ (figure); $g(X)$ is a random variable, with proof (figure) (HW 20; HW only for the theorem)

## Ch 27 Expectation, Variance and Moments (`ch:expectation-moments`) ↔ merge STAT2003
- ◻ Simple random variable (canonical partition form; Rem 1.2.13 on non-partition forms) (figure) (HW 17; CN Def 1.2.12)
- ◻ Simple approximation theorem; explicit dyadic sequence (HW 17; CN Prop 1.2.14, Rem 1.2.15)
- ◻ $X^+$, $X^-$, $\abs X = X^++X^-$ (HW 17; CN Def 1.2.16)
- ◻ Construction of $\E$: indicator, simple, non-negative (sup; limit along any approximating sequence; figure of staircases under $X$), general; integrable; $\int_\Omega X\dd\Prob$ (HW 18; CN Def 1.2.17, 1.2.20, Rem 1.2.21–1.2.22) ↔ STAT2003 discrete/continuous definitions (book: present both, measure-theoretic one as the general case)
- ◻ Linearity for simple r.v.s (CN Prop 1.2.18, Rem 1.2.19)
- ◻ ↔ Properties: linearity, monotonicity (a.s.), $\abs{\E X}\le\E\abs X$ (HW 19; CN Prop 1.2.28, Rem 1.2.29) ↔ STAT2003 linearity proof
- ◻ Almost surely (CN Def 1.2.26, Rem 1.2.27)
- ◻ Jensen's inequality with proof; instances $x^2$, $\abs x$, $e^x$ (HW 19; CN Thm 1.2.30, Rem 1.2.31)
- ◻ ↔ LOTUS $\E g(X) = \int g\dd\mu_X$; motivation (hard vs easy integral; density and Dirac forms, HW 21); four-step proof (HW 21–22; CN Thm 1.2.23 and proof); Stieltjes, density and pmf forms (CN Rem 1.2.24–1.2.25) ↔ STAT2003 LOTUS (Ch 27)
- ◻ ↔ Markov and Chebyshev inequalities with proofs (CN Thm 1.3.14–1.3.15) ↔ STAT2003 (already in Ch 27; merge)
- ◻ Pareto ($\alpha = 1$): finite a.s., infinite mean (CN Lecture ex 3.2.8; CG 7 trap)
- ◻ Limits and expectations: question $\E\lim X_n = \lim\E X_n$?; counterexample $X_n = ne^{-n\omega}$ with the remark on $\dd\Prob = \dd\lambda = \dd\omega$; sufficient conditions MCT/DCT (HW 27; CG 6 table) — **placement question: here or Ch 33**
- ◻ MCT (statement; CN proof sketch) and the series example $\E\sum Y_i = \sum\E Y_i$ (HW 28; CN Thm 1.3.1)
- ◻ Fatou's lemma with proof; reverse Fatou with proof (HW 29; CN Lemma 1.3.2–1.3.3)
- ◻ DCT with proof (HW 30; CN Thm 1.3.4)

## Ch 28 Generating Functions and Transforms (`ch:generating-functions`) ↔ merge STAT2003
- ◻ ↔ pgf on $[-1,1]$; properties: $G(1)=1$, $G(0)=p_0$, bounds, monotone and convex on $[0,1]$, smooth, continuous (with proof); $0^0=1$; pmf from derivatives; $\mu = G'(1)$ via MCT (CN Def 2.1.1, Prop 2.1.3, Lecture rem 2.1.4–2.1.5, Rem 2.1.6) ↔ STAT2003 PGF (merge; add the convexity/continuity facts)
- ◻ ↔ pgf of independent sums, iid sums $G^r$ (CN Prop 2.1.7, Rem 2.1.8, Rem 3.1.9) ↔ STAT2003 (placed in Ch 30)
- ◻ ↔ Examples: Poisson pgf; geometric pgf in both conventions (CN Ex 2.1.9–2.1.10) ↔ Ch 29
- ◻ Three transforms: characteristic function, mgf, pgf; $M_X(s) = G_X(e^s)$, $\varphi_X(t) = G_X(e^{it})$ (CN Lecture rem 2.1.2)
- ◻ Characteristic function $\varphi_X(t) = \E e^{itX}$ (Fourier transform), meaning of $\E e^{itX}$ via Euler; determines the law; product rule for independent sums (HW 26; CN Rem 1.3.9, 1.3.12)
- ◻ Bernoulli increments: $S_n\sim\Bin(n,p)$ via pgfs (CN Ex 3.1.10) ↔ STAT2003 binomial

## Ch 29 Common Distributions (`ch:common-distributions`) ↔ merge STAT2003
- ◻ ↔ Geometric "failures from 0" convention alongside the book's $\{1,2,\dots\}$ convention (CN Ex 2.1.10)
- ◻ ↔ Memoryless property of $\Expo(\lambda)$ with proof (CN Lemma 5.3.3, Rem 5.3.4) ↔ STAT2003 (already in Ch 29)
- ◻ ↔ $T_n \sim \GammaDist(n,\lambda)$ (Erlang) as a sum of exponentials; Gamma tail (CN Lemma 5.3.1, Lecture rem 5.3.2) ↔ STAT2003 gamma
- ◻ Bernoulli process (CN Def 5.1.1, Rem 5.1.2) ↔ STAT2003 "i.i.d. Bernoulli trials" (Ch 29)

## Ch 30 Multivariate Distributions (`ch:multivariate-distributions`) ↔ merge STAT2003
- ◻ Random vector as an $\mathcal F/\mathcal B(\R^d)$-measurable map; $\mathcal B(\R^d)$ from products of half-lines; criterion $\{X_1\le x_1,\dots\}\in\mathcal F$ (HW) or components are random variables (CN) (HW 15; CN Def 1.2.4)
- ◻ Ex $\vect X = (I_{[0,p]}(\omega_1), I_{[0,p]}(\omega_2))$ on $[0,1]^2$: measurability by cases (unit-square figure), joint pmf, Bernoulli marginals, independence (HW 15–16; HW only)
- ◻ ↔ Joint distribution and joint cdf of $(X_1,X_2)$; marginal cdfs as limits (CN Def 1.2.9, Rem 1.2.10) ↔ STAT2003 joint CDF
- ◻ ↔ Covariance, correlation, bilinearity (CN Def 3.1.3, Rem 3.1.4) ↔ STAT2003 covariance

## Ch 32 Transformations of Random Variables (`ch:transformations`) ↔ merge STAT2003
- ◻ ↔ Order statistics of iid uniforms: joint density $n!/t^n$ (CN Prop 5.5.1) ↔ STAT2003 order statistics
- ◻ ↔ Competing exponentials: $\min\sim\Expo(\sum a_i)$, $\Prob(I=i) = a_i/a$, independent of the min (CN Lemma 6.11.1) ↔ STAT2003 min of exponentials

## Ch 33 Convergence of Random Variables and Limit Theorems (`ch:limit-theorems`) ↔ merge STAT2003 (◻ there: modes, WLLN, SLLN, CLT)
- ◻ Modes listed by strength: pointwise (sure), a.s., in probability, in $L^p$, in distribution (weak, in law); notations (HW 23–24; CN Def 1.3.5, Rem 1.3.6) ↔ STAT2003 HW 33
- ◻ Implications diagram (pointwise ⇒ a.s. ⇒ $\Prob$ ⇒ d; $L^p$ ⇒ $\Prob$; $L^p$ ⇒ d) (figure), none reversible; $L^q \Rightarrow L^p$ with Jensen proof (HW 24; CN Prop 1.3.7, Rem 1.3.8; CG 6)
- ◻ Counterexamples: $\Bern(1/n)$ converges in probability, not a.s.; $X_n = -X$ with $X\sim\Normal(0,1)$ converges in distribution, not in probability; $\sqrt n\,I_{\{U\le1/n\}}$ converges in probability, not in $L^2$ (HW 24–25; HW only; CN Rem 1.3.8 hints at the last)
- ◻ Lévy's continuity theorem (statement), purely analytic criterion; examples $\Unif[-n,n]$ (HW) and $\Normal(0,n)$ (CN) where the limit is discontinuous at 0 (HW 26; CN Thm 1.3.10, Rem 1.3.11, 1.3.13)
- ◻ ↔ WLLN with Chebyshev proof (HW 31; CN Thm 1.3.16); Khinchin remark (CN Rem 1.3.17) ↔ STAT2003 WLLN proof (merge)
- ◻ ↔ SLLN (statement), fourth-moment proof idea; Kolmogorov's general proof not given (HW 31; CN Thm 1.3.18, Rem 1.3.21) ↔ STAT2003 SLLN statement
- ◻ a.s. convergence via Borel–Cantelli: summable ⇒ a.s.; independent, non-summable ⇒ not a.s. (HW 31; CN Thm 1.3.19, Rem 1.3.20)
- ◻ ↔ CLT, two forms; proof sketch via characteristic functions and Lévy (CN); role of the first two moments (HW 32; CN Lecture thm 1.3.22, Lecture rem 1.3.23; CG 7) ↔ STAT2003 CLT with MGF proof (keep both proofs? hub question)
- ◻ Random walk long-run behaviour: $S_n/n \to\mu$ a.s., drift to ±∞, CLT for $S_n$ (CN Lecture prop 3.1.7) — or Ch 34 with the random walks

## Ch 34 Discrete-Time Markov Chains (`ch:discrete-time-markov-chains`) ↔ merge STAT2003 (◻ there: Markov property, CK, examples, limiting/stationary, two-state chain, global balance, RW on $\Z^+$, birth–death chains)
**Random walks (CN Topic 3; placement question: opening sections of Ch 34, or Ch 36)**
- ◻ Random walk, independent increments; moments $\E S_n$, $\Var S_n$, $\Cov(S_n,S_{n+k}) = n\sigma^2$, $\Corr = \sqrt{n/(n+k)}$ with proof (CN Def 3.1.1, Rem 3.1.2, Prop 3.1.5, Rem 3.1.6); boundary case $\mu=0$ (CN Lecture rem 3.1.8)
- ◻ Examples: Bernoulli increments (binomial), normal increments (CN Ex 3.1.10, 3.1.12, Rem 3.1.13, Exercise 3.1.11)
- ◻ SSRW, hitting times; symmetry lemma; difference equation; recurrence theorem with proof (CN Def 3.2.1–3.2.3, Lemma 3.2.4, 3.2.6, Thm 3.2.7); first-step analysis recipe (CG 11)
- ◻ Expected hitting time is infinite (CN Thm 3.2.9, Rem 3.2.10; CG 11–12)
- ◻ Gambler's ruin: absorption a.s. with finite mean (CN Lemma 3.3.2); ruin/win probabilities (Thm 3.3.4); escape probability $b\to\infty$ (Cor 3.3.6); expected duration (Thm 3.3.8); $\E\tau_0$ (Cor 3.3.9); connection to SSRW (Rem 3.3.10); worked numbers $p = 0.4$, $x = 5$, $b = 10$ (CG 12, Fig. CG3)
**Markov chains**
- ◻ ↔ Markov process (general); classification table by time and state space (CN Def 4.1.1, §4.1.2 table, Rem 4.1.2)
- ◻ ↔ DTMC, one-step and $n$-step transition probabilities (time-inhomogeneous first), product formula, joint pmf, marginals (CN Def 4.1.3–4.1.5, Lecture prop 4.1.6, Prop 4.1.7, Lecture cor 4.1.8) ↔ STAT2003 HW 35
- ◻ ↔ Time-homogeneity, stochastic matrix; Chapman–Kolmogorov; $\pi^{(n)} = \pi^{(0)}P^n$; weather-chain example (CN Def 4.1.9, Rem 4.1.10, Thm 4.1.11, Prop 4.1.12, Lecture ex 4.1.13; CG 13–15) ↔ STAT2003 HW 35–36
- ◻ Spectral method: left/right eigenvectors, biorthogonality, $P^n = \sum\lambda_i^n v_iu_i$, limiting distribution when 1 is simple and dominant; 3-cycle vs perturbed 3-cycle (CN §4.2.1–4.2.3, Lecture ex 4.2.7; CG 15) ↔ Ch 7 eigenvalues/diagonalisation (MATH1071, MATH2001)
- ◻ Gershgorin's circle theorem with proof; stochastic-matrix corollary (CN Thm 4.2.8, Cor 4.2.9, Rem 4.2.10) ↔ Ch 7 / Ch 59 (MATH3204) — state where first needed
- ◻ ↔ Stationary distribution; limiting ⇒ stationary; worked $3\times3$ example (CN Def 4.2.11, Rem 4.2.12, Lecture ex 4.2.13; CG 18) ↔ STAT2003 HW 37–39
- ◻ Three ways to specify a chain; sample paths (CN Lecture ex 4.2.16, Fig. A, Fig. B) — simulation algorithm goes to Ch 37
- ◻ ↔ Two-state chain, complete analysis: structural cases, spectral decomposition, closed form of $P^n$, projector trick, limiting behaviour (CN §4.3, Lecture ex 4.3.1, Lecture rem 4.3.2; CG 15–16, Fig. CG4) ↔ STAT2003 two-state chain
- ◻ Motivating examples (six-state, seven-state with Fig. C) (CN Ex 4.4.1, Lecture ex 4.4.2; CG 17)
- ◻ $\Prob_x$, $\E_x$; hitting times; return probabilities $f_{xy}$; recurrent/transient; two-state recurrent example; number of visits; $\sum p^{(n)}_{yy}$ criterion (CN Def 4.4.3–4.4.6, Lecture ex 4.4.7, Prop 4.4.8, Rem 4.4.9)
- ◻ Leads to, communicates, classes; recurrence is a class property (Lemmas 4.5.2, 4.5.4, 4.5.5, Thm 4.5.6, proofs) (CN §4.5.1–4.5.2)
- ◻ Irreducible, closed, absorbing; classification examples (Fig. D); block decomposition theorem with proof; finite closed classes are recurrent (Fig. E); subtleties on infinite spaces (CN Def 4.5.8–4.5.10, Ex 4.5.11–4.5.19)
- ◻ Hitting probabilities and expected hitting times by first-step analysis (CG 17 recipe; CN uses it via Topic 3)
- ◻ Periodicity: period, class property, self-loop ⇒ aperiodic (CN Def 4.6.1, Lemma 4.6.2, Ex 4.6.3; CG 17 trap)
- ◻ ↔ Global and local balance; local ⇒ global; doubly stochastic ⇒ uniform; deterministic 3-cycle; random walk on a graph; reflected walk on $\{0,1,\dots\}$; branching process as a DTMC; gambler's ruin as a DTMC (Fig. F) (CN §4.7; CG 18–19) ↔ STAT2003 global balance, RW on $\Z^+$
- ◻ Time reversal, reversibility = detailed balance; Kolmogorov's cycle condition (statement, idea) (CN §4.8)
- ◻ Mean return time, positive/null recurrence, ergodic theorem ($\pi_x = 1/m_x$; convergence for aperiodic chains), equivalences (CN §4.9; CG 19 table)

## Ch 35 Poisson Processes and Continuous-Time Markov Chains (`ch:poisson-ctmc`) — new (STAT3004 only)
**Poisson processes (CN Topic 5)**
- ◻ Counting process; arrival and inter-arrival times; duality $\{N(t)\ge n\} = \{T_n\le t\}$; discrete-time counting example (CN §5.2.1; CG 21–22, Fig. CG5, symbol table)
- ◻ Poisson process (counting definition), stationary and independent increments; Ex PP(2): one interval, disjoint intervals; overlapping intervals computed in full (CN Def 5.2.6, Rem 5.2.7, Ex 5.2.8, Rem 5.2.9, Lecture ex 5.2.10; CG 23–24, Fig. CG6)
- ◻ Equivalent characterisations: exponential inter-arrival times (with proof sketch), memorylessness, restart at a fixed time; infinitesimal description and its converse (difference-differential equations) (CN §5.3; CG 22–23)
- ◻ Bernoulli process limit: discretised approximation, binomial → Poisson (CN §5.4; CG 21 "one picture", discrete→continuous table) ↔ STAT2003 Poisson limit of binomial (Ch 29)
- ◻ Conditional uniformity of arrival times given $N(t) = n$ (CN Claim 5.5.2, Rem 5.5.3; CG 24)
- ◻ Waiting-time recipes (CG 24)
- ◻ Non-homogeneous Poisson process: Bernoulli approximation, definition via $\Lambda$, gaps not exponential/independent (example $\lambda(s) = \lambda s$), joint density of $(A_1,A_2)$, examples $\lambda = 2+s$ and $e^s$ (CN §5.7; CG 25)
- ◻ Spatial Poisson process (PRM): definition, trees-in-a-forest example, non-homogeneous PRM and $\E N(A) = \int_A\lambda$ examples (CN §5.8, Def 5.8.1, 5.8.11, Ex 5.8.3, 5.8.13, Lecture ex 5.8.14; CG 25–26)
- ◻ Superposition, thinning (homogeneous and non-homogeneous) (CN Prop 5.8.4–5.8.5, Lecture prop 5.8.6, Rem 5.8.7; CG 26)
**CTMCs (CN Topic 6)**
- ◻ CTMC and the Markov property; transition functions; time-homogeneity; finite-dimensional distributions; standard transition functions; Chapman–Kolmogorov $P_{s+t} = P_sP_t$; non-homogeneous remark (CN §6.1)
- ◻ Holding times are exponential (proof via Cauchy's functional equation); absorbing/stable/instantaneous states (CN §6.2)
- ◻ Jump chain $K$, $K_{xx}=0$; holding time independent of next state; structure theorem; two-state chain (Fig. H); sample path (CG Fig. CG7) (CN §6.3.1, Ex 6.3.5; CG 27)
- ◻ Explosion: exploding chain $q_x = 2^x$ (MCT); regular/honest; bounded rates ⇒ regular; general criterion; standing assumptions (CN §6.3.3; CG 32)
- ◻ Examples: Poisson process as a CTMC (Fig. G), M/M/1 via competing clocks (Fig. CG8) (CN §6.4; CG 27–28)
- ◻ Small-time analysis, $Q$-matrix, properties, model primitives, Q-matrices of the examples; writing down $Q$ recipe (CN §6.5; CG 27–28)
- ◻ Kolmogorov backward and forward equations (proofs), when forward fails; $P_t = e^{tQ}$ for finite $E$; two-state chain via the series (CN §6.6; CG 29) ↔ Ch 20 (matrix exponential, MATH2010)
- ◻ Marginal, limiting and stationary distributions; mass escaping; limiting ⇒ stationary (CN §6.7)
- ◻ Spectral decomposition of $P_t$; Gershgorin for $Q$ (eigenvalues 0 or negative real part); convergence rate; no periodicity; multiplicity of 0 = number of closed classes; transition rate graph; Poisson and two-state examples (CN §6.8)
- ◻ $\pi Q = 0$, balance equations; $Q = D(K-I)$; $\pi \leftrightarrow \nu$ ($\pi_x\propto\nu_x/q_x$); fraction of jumps vs fraction of time; examples where normalisation fails in each direction (CN §6.9; CG 30–31)
- ◻ Classification: hitting/return times, recurrence via the jump chain, positive/null recurrence, communication, no periodicity, closed classes; repair problem (Fig. I) with its stationary distribution; convergence to equilibrium (sketch) (CN §6.10; CG 29–31)
- ◻ Queues: competing exponentials (↔ Ch 32), M/M/∞, M/M/c, M/M/c/K; queue table (CN §6.11; CG 32 table)
- ◻ Local balance, time reversal, reversibility, KCC for $Q$ and $K$, tree-like graphs (CN §6.12; CG 30)
- ◻ ↔ Birth–death processes: definition (Fig. J), stationary distribution (6.12)–(6.13), existence criterion $S<\infty$; M/M/1, M/M/∞, M/M/c, M/M/c/K (CN §6.13; CG 31–32) ↔ STAT2003 birth–death **chains** (Ch 34)
- ◻ Wrap-up: three descriptions of a CTMC; DTMC vs CTMC table; course summary and unifying themes (CN §6.14–6.15; CG 33) — use for chapter/part introductions only

## Ch 36 Stochastic Models and Reliability (`ch:stochastic-models`) — branching processes (placement question)
- ◻ Branching process (Galton–Watson): definition, family-tree figure (CG Fig. CG1); extinction is permanent (CN Def 2.2.1, Rem 2.2.2–2.2.3; CG 8)
- ◻ Mean $\mu^n$ (tower property) and variance (law of total variance) with proofs; behaviour as $n\to\infty$ (CN Prop 2.2.4–2.2.5, §2.2.3; CG 8–9) ↔ Ch 31 (tower property, total variance)
- ◻ Extinction probability: $\eta = \lim\Prob(S_n=0)$; subcritical via Markov; η smallest root of $G(z) = z$ with proof; fixed-point iteration; trichotomy with proof idea; geometric offspring, $p = \frac13$ case (CN §2.3; CG 9, Fig. CG2, recipe "finding η")

## Ch 37 Simulation and Monte Carlo Methods (`ch:simulation-monte-carlo`) ↔ merge STAT2003 (simulating Markov chains and random walks)
- ◻ ↔ Simulating a DTMC by inverse-cdf sampling (CN Prop 4.2.15; CG 14) ↔ STAT2003 HW 37
- ◻ Simulating a Poisson process: sequential (gap by gap), fixed-count / order statistics (CN Alg 5.6.1–5.6.2; CG 25)
- ◻ Thinning for an NHPP; efficiency (CN Alg 5.8.8, Rem 5.8.9)
- ◻ Simulating a homogeneous and a non-homogeneous PRM (CN Alg 5.8.10, 5.8.12)
- ◻ Forward simulation of a CTMC (CN Alg 6.3.6; CG 27)

## Other chapters touched (merge pointers only)
- Ch 3 Induction, Recursion and Counting (MATH1061): linear difference equations as used in the gambler's ruin (homogeneous and inhomogeneous, CN §3.3) ↔ merge — or keep in Ch 34.
- Ch 7 Eigenvalues (MATH1071/2001): left/right eigenvectors, biorthogonality, spectral decomposition (CN §4.2.1) ↔ merge.
- Ch 12 Integration (MATH2401): the Lebesgue integral is only named here ($\int_\Omega X\dd\Prob$); no merge needed.
- Ch 20 Linear Systems of ODEs (MATH2010): matrix exponential $e^{tQ}$ (CN Thm 6.6.7) ↔ merge.

## Not used yet
- CN §6.15 course summary and CG checklists (exam-oriented; candidates for chapter introductions or not at all).
- CN Exercise 1.1.20, 3.1.11 and the "good exercise" remarks (exercises, not content).
- Companion text (Rosenthal) reference; the "online supplementary notes" (HW 28) and "supplementary optional-reading notes" (CN Rem 1.2.24) — not supplied.

---

## Suspected errors in the notes (kept in place in the transcriptions)
**Handwritten notes**
1. HW 02 partition: "every $\omega$ belongs to only one $A_n \in \Omega$": should be $A_n \subseteq \Omega$.
2. HW 04 proof that $\bigcap_i\mathcal F_i$ is a σ-algebra, step (ii): "Let $A\in\mathcal F$" should be "Let $A\in\bigcap_i\mathcal F_i$".
3. HW 05 $(-\infty,a) = \bigcup_n(-\infty,a-\frac1n)$: should use closed half-lines $(-\infty,a-\frac1n]$ (CN Rem 1.1.27), otherwise it doesn't show the two classes generate each other.
4. HW 07 continuity proof: summation/union indices mix $n$ and $k$ ($\bigcup_{n=1}^\infty B_k$, $\sum_{n=1}^n\Prob(B_k)$).
5. HW 08 "countable additivity is only satisfied if $\mathcal F = \mathcal B([0,1])$" overstates the point (λ cannot be extended to all of $\powerset([0,1])$).
6. HW 09 real limsup/liminf: inner sup/inf act on $x_n$ instead of $x_m$; liminf of events written $\bigcup_{n=1}\bigcap_{n=n}$ (should be $\bigcup_{m}\bigcap_{n\ge m}$); **$\omega\in\{A_n\text{ a.b.f.m.}\} \iff \abs{\{n:\omega\in A_n\}}<\infty$ should be $\omega\notin A_n$**; theorem writes $\bigcup_{m\ge n}A_n$ for $A_m$.
7. HW 10 proof of i.o. = limsup: "$\forall n$" dropped in the second equivalence; $A_n$/$A_m$ mixed.
8. HW 13 "$X^{-1}(\{-1\}) = [0,p]$": should be $\{1\}$ (possibly a stray stroke).
9. HW 15 random-vector example: "Else: $x_1,x_2<0$" should be "$x_1<0$ or $x_2<0$".
10. HW 17 simple random variable: coefficients $b_i$ vs "constants $a_i$"; "$A_i$ partitioning $\mathcal F$" should be $\Omega$. Dyadic approximation: should be $k/2^n \le X < (k+1)/2^n$, $k<n2^n$ (CN Rem 1.2.15).
11. HW 19 properties of expectation and Jensen: integrability assumptions omitted (CN Prop 1.2.28, Thm 1.2.30).
12. HW 21 $\int_\Omega g(x)\dd\Prob$ should be $\int_\Omega g(X)\dd\Prob$; the discrete $\mu_X(\dd x)$ sums over $x_i\in B$ (should be all atoms).
13. HW 22 LOTUS step (III): $g_n$ are simple Borel functions, not random variables; the step citing (II) already has the limit inside (MCT must be applied on both sides, CN Step 3). Step (IV): $g$ is a Borel function, not a random variable; needs $g(X)$ integrable.
14. HW 24 $\Bern(1/n)$ example: Borel–Cantelli II needs independence, not stated.
15. HW 26 Lévy part (2): $\varphi$ is only a pointwise limit; the conclusion includes that $\varphi$ is a characteristic function (CN Thm 1.3.10).
16. HW 28 MCT example: existence of $\lim X_n$ follows from monotonicity, not from the MCT. Minor.
17. HW 30 DCT proof writes $g\pm X_n$ (CN's name) for $Y\pm X_n$; the final chain omits "$=\E[X]$".
18. HW 31 SLLN hypothesis uses finite variance (CN: $\E\abs{X_1}<\infty$); "general proof ($\E[X]<\infty$ only)" should be $\E\abs X<\infty$; a.s.-convergence theorem: (1) needs every $\varepsilon>0$, (2) some $\varepsilon>0$ and independent events (CN Thm 1.3.19).
19. HW 32 CLT: $\sigma^2>0$ needed (CN: $\sigma^2\in(0,\infty)$).
20. HW 27 "a sequence must satisfy one [of MCT, DCT] to swap operations": they are sufficient, not necessary (the heading says so). Minor.

**Typed notes (CN)**
21. Ex 4.4.1 (p44): "from 4, with probability $\frac23$ the chain leaves for $\{1\}$ or $\{5,6\}$ and never comes back" implies a return with probability $\frac13$; the remaining step goes to the closed class $\{2,3\}$, so $f_{44}=0$. Conclusion (transient) right.
22. Ex 4.7.9 (p52): branching process written $Z_n$ (Topic 2 uses $S_n$); pmf first written informally ("Binomial$(x,p)\cdot2$-type sum").
23. Notation clash in Topic 1: $g$ is both the Borel function (LOTUS) and the dominating variable (DCT).
24. Cross-references to separate topic files ("lecture_notes.tex", "MON/DOM notes", "DTMC notes") — cite chapters instead.

**Course guide (CG)**
25. p5: "Independent events with $\Prob(A_n)=1/n^2$ … (BC I)": BC I needs no independence. Conclusion right.

## Notation the book doesn't have yet (proposals for `NOTATION_REQUESTS.md`, via the hub)
| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\F` (or `\sigalg`) | $\mathcal F$ | the σ-algebra of a probability space | used on almost every page of Topic 1 and in Ch 25; one macro keeps it consistent with STAT2003 |
| `\Borel` | $\mathcal B$ | Borel σ-algebra, `\Borel(\R)`, `\Borel(\R^d)`, `\Borel([0,1])` | Topic 1 throughout |
| `\gensig` (or plain `\sigma(\mathcal A)`) | $\sigma(\mathcal A)$ | generated σ-algebra | decide whether a macro is wanted |
| `\Leb` | $\lambda$ (or $\mathrm{Leb}$) | Lebesgue measure | **clash**: $\lambda$ is also the Poisson/exponential rate in Ch 29, 35; suggest $\mathrm{Leb}$ or $\lambda$ with a remark |
| `\law` | $\mu_X$ | distribution (law) of $X$ | HW 14, LOTUS; fix the letter |
| `\io`, `\abfm` | $\text{i.o.}$, $\text{a.b.f.m.}$ | infinitely often / all but finitely many | Borel–Cantelli, a.s. convergence |
| `\convLp{p}` | $\xrightarrow{L^p}$ | convergence in $L^p$ (mean) | completes `\convp`, `\convd`, `\convas`; HW 23 |
| `\convw` (optional) | $\xrightarrow{w}$ / $\Rightarrow$ | weak convergence | the notes list it as an alternative; may be mentioned once only |
| `\cf` (or `\charfn`) | $\varphi$ | characteristic function $\varphi_X(t)=\E e^{itX}$ | matches `\pgf`, `\mgf` |
| `\eR` | $\bar{\R}$ | extended real line $[-\infty,\infty]$ | CN Def 1.1.29, $\E X\in[-\infty,\infty]$ |
| `\PP` | $\mathrm{PP}$ | Poisson process $N\sim\mathrm{PP}(\lambda)$ | Ch 35 |
| `\DTMC`, `\CTMC` | $\mathrm{DTMC}(P,\pi^{(0)})$, $\mathrm{CTMC}(\pi^{(0)},Q)$ | chain with given primitives | Ch 34–35 (check STAT2003's Ch 34 usage first) |
| `\GeomZero` (or a stated convention) | $\Geom_0(p)$ | geometric on $\{0,1,\dots\}$ (failures) | CN uses both conventions; book's `\Geom` is on $\{1,2,\dots\}$ |
| `\Pareto` | $\mathrm{Pareto}$ | Pareto distribution | CN Lecture ex 3.2.8 (one example; optional) |
| `\bigO`, `\littleo` | $O$, $o$ | Landau symbols | CN Rem 5.3.6–5.3.8, small-time analysis in Ch 35 |
| `\Prob_x`, `\E_x` (convention, no macro) | $\Prob_x$, $\E_x$ | chain started at $x$ | Ch 34–35; record as a convention |
| — | $\ind_A$ for $I_A$ | indicator | the notes write $I_A$; the book already has `\ind` (convert) |
| — | $\pgf$ for $G$ | pgf | the notes write $G$; the book already has `\pgf` (convert) |

Fixed conventions to record: row-vector distributions acting on the left ($\pi^{(0)}P^n$, $\pi Q = 0$); $p^{(n)}_{xy}$; $f_{xy}$ (return/hitting probability); $m_x$ (mean return time); $d(x)$ (period); $T_n$ (arrival times) and $A_n$ (gaps), which clash with events $A_n$ in Ch 25 — the hub may want a different letter for gaps.

## Code in the notes
- **None.** No R, Python or other code in HW, CN or CG.
- Pseudocode algorithms to implement in R for Ch 37 (and their examples): DTMC simulation (CN Prop 4.2.15, with the sample paths of Lecture ex 4.2.16), Poisson process simulation (Alg 5.6.1 sequential, 5.6.2 order statistics), NHPP thinning (Alg 5.8.8), homogeneous PRM (Alg 5.8.10), non-homogeneous PRM thinning (Alg 5.8.12), CTMC forward simulation (Alg 6.3.6).
- Figures that show single random realisations (CN Fig. B; CG Fig. CG7) can be redrawn from the exact points given, or regenerated in R with a fixed seed.

## Questions for the hub chat
1. **Branching processes** have no chapter in `tools/chapters.py`. Proposal: a section of Ch 36 (Stochastic models), with the pgf review merged into Ch 28. Alternative: Ch 28 as an application of pgfs.
2. **Random walks and the gambler's ruin** (CN Topic 3): opening sections of Ch 34 (they reappear there as DTMC examples), or Ch 36?
3. **MCT/Fatou/DCT and "limits and expectations"**: Ch 27 (needed early, e.g. $\mu = G'(1)$ in Ch 28) or Ch 33?
4. **Measure-theoretic layer vs STAT2003 Ch 25–27**: STAT2003's chapters are already written at an elementary level. Merge Topic 1 into them as new sections (σ-algebras, Borel sets, Lebesgue measure, measurable maps, construction of $\E$), or add a separate "measure-theoretic probability" section at the end of each? Ch 25 currently has only a σ-algebra remark.
5. **Two CLT proofs** (STAT2003 via MGFs, STAT3004 via characteristic functions and Lévy): keep both?
6. **Lebesgue measure symbol** $\lambda$ vs rates $\lambda$ (see notation table).
7. **Ch 35 queueing**: queues (M/M/1, M/M/∞, M/M/c, M/M/c/K) stay in Ch 35 with birth–death processes, or move to Ch 36?
8. **Course guide** is itself derived from CN; treat it as a secondary source (recipes and a few figures only)? Its "How to answer it" recipes read as exam advice; include them as remarks/methods or leave them out?
