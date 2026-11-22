# Coverage inventory: STAT3001 Mathematical Statistics

_Built in the transcription phase from 56 photos of the handwritten notes (main source), the lecturer's typed lecture notes LN1–LN24, the Background Notes on Point Estimation, two guest-lecture slide decks and the lecture diary. Course taken Semester 1, 2026. Nothing is written yet._

**Sources.** Transcriptions and indexes: `claude/notes-stat3001-1.md` (HW 01–28, sources, legibility), `-2.md` (HW 29–56), `-3.md` (typed notes, slides, diary).
- **HW nn**: handwritten page nn (56 pages, whole course). **Main source.**
- **LNn p. k**: typed lecture note n (LN1–LN24, LN19a; 182 pp.). Supplement; the only source for several topics (marked **LN only**).
- **BN p. k**: *Background Notes on Point Estimation* (36 pp.). Supplement for Ch 40–42.
- **S1.k, S2.k**: guest lectures on Bayesian estimation and MCMC (slide k). Only source for those topics.
- **LD**: lecture diary (scope; non-examinable flags).

**Code:** the course's code is R (S2 only). Part IV uses R, so it carries over. **Content rule:** source material only, with corrections. **Status:** ◻ to do (nothing drafted). **↔** = merge with an entry from another course or an existing chapter rather than add new. **Main-source rule (user):** HW is the main source; LN/BN supplement it.

---

## Part III cross-listings

### Ch 27 Expectation, variance and moments (`ch:expectation-moments`) — ✅ written (STAT2003)
- ◻ **Jensen's inequality** $\E h(X)\ge h(\E X)$ for convex $h$; convexity definition; $h''\ge0$ criterion; examples $x^2$, $-\log x$ (HW 21; LN6 pp. 1–2). Not proved in the course. ↔ add to Ch 27 (new item in a written chapter) or open Ch 42 with it — hub to decide

### Ch 30 Multivariate distributions (`ch:multivariate-distributions`) — ✅ written (STAT2003); MVN moved to Ch 32
- ↔ $\vect\mu = \E\vect X$, $\mat\Sigma = \E(\vect X\vect X\T) - \vect\mu\vect\mu\T$; $\mat\Sigma$ p.d. symmetric (HW 01; LN1 p. 1) — already in Ch 30
- ↔ $\Cov(X_i,\bar X) = \sigma^2/n$ computation (HW 03 Rem.; LN9 p. 3) — example for covariance properties

### Ch 31 Conditional distributions (`ch:conditional-expectation`) — ✅ written (STAT2003)
- ◻ **Truncated random variable**: $f(v\given V\in R) = f(v)\ind_{[R]}(v)/\int_Rf$, proof (discrete case), conditional expectation of $a(V)$ (HW 42; LN13 p. 1) ↔ conditional pmf/pdf; could instead sit with EM in Ch 51

### Ch 32 Transformations of random variables (`ch:transformations`) — MVN material ↔ STAT2003 ◻ entry, STAT2004 Ch 32 entry
- ◻ MVN definition and density (HW 01; LN1 p. 2) ↔ STAT2003 HW 20, 29–30
- ◻ **Affine transformation** $\mat A\vect X+\vect b\sim\Normal(\mat A\vect\mu+\vect b,\mat A\mat\Sigma\mat A\T)$, full row rank; proof of mean and covariance (HW 01); normality via MGF (LN1 p. 2, **LN only**) ↔ STAT2003 Y = AX via MGF
- ◻ **Marginals and conditionals of a partitioned MVN**, Schur complement remark, interpretation (HW 02; LN1 p. 2). Stated without proof
- ◻ Example: $X_i\given\bar x\sim\Normal(\bar x,(1-1/n)\sigma^2)$ via $\vect W = \mat A\vect X$ (HW 03; LN1 pp. 2–3)
- ◻ **$(n-1)s^2/\sigma^2\sim\ChiSq{n-1}$ and $s^2\indep\bar X$**: orthogonal matrix with last row $1/\sqrt n$ (HW 04; LN1 pp. 4–6, Helmert-type, with $\E Y_i = 0$ shown) ↔ STAT2004 entry ("Fisher's lemma", R L01 proof) — three proofs now exist; hub to choose. _Could open Ch 39 instead (STAT2004 note)._

### Ch 33 Convergence and limit theorems (`ch:limit-theorems`) ↔ STAT3004, STAT2003, STAT2004
- ◻ Convergence in law notation "$\xrightarrow{\ell}$", "law" as archaic for distribution (HW 27) → use `\convd`
- ◻ **Slutsky-type theorem**: $Y_n\convd Y$, $a_n\convp a$, $b_n\convp b\implies a_nY_n+b_n\convd aY+b$ (HW 32; LN8 Theorem 6 p. 9). Not proved (Cramér reference)
- ◻ **Delta method** $\sqrt n[g(T_n)-g(\theta)]\convd\Normal(0,\sigma^2g'(\theta)^2)$, Taylor idea (HW 32; LN8 Theorem 7 pp. 9–10) ↔ STAT2004 R L05–L06 (scalar and multivariate)

### Ch 37 Simulation and Monte Carlo (`ch:simulation-monte-carlo`) ↔ STAT2003, STAT3004, STAT3500
- ◻ **Metropolis–Hastings**: aim, algorithm, acceptance probability (S2.6); random-walk special case (S2.7, ratio not written) ↔ STAT3500/STAT3004 (check their inventories for MCMC)
- ◻ **Gibbs sampling** algorithm (S2.11); example $f(x_1,x_2)\propto e^{-x_1x_2-x_1-x_2}$ with exponential full conditionals (S2.12–13)
- ◻ Motivation: posteriors known up to a constant; "tricky distributions" (S2.3–5)
- ◻ Exercises: RW-MH for $x^2e^{-x^2+\sin x}$ (S2.10); normal–inverse-gamma Gibbs (S2.14) — no solutions
- ◻ Code: RW-MH Beta–binomial; Gibbs sampler with `rgl::persp3d`, `MASS::kde2d` (S2.9, S2.13) — goes in the computing section
- ◻ Bootstrap as Monte Carlo (LN23 pp. 1–2) — see Ch 51

---

## Part IV

### Ch 39 Statistical models and sampling distributions (`ch:sampling-distributions`) ↔ STAT2004, STAT1301
- ◻ Setting: $f(x;\vect\theta)$, $\vect\theta\in\Omega$, univariate/multivariate, nonparametric index example (normal vs Cauchy), nuisance parameters, S.D. vs S.E. (BN pp. 1–2)
- ↔ Distribution of $s^2$ — see Ch 32

### Ch 40 Point estimation (`ch:point-estimation`) ↔ STAT2004 (PE main for this chapter)
- ◻ Loss function, risk $R(W;\theta) = \E\ell(W,\theta)$; squared-error loss gives MSE $=\Var+\bias^2$ (HW 23; BN pp. 2–3) ↔ STAT2004 MSE entry
- ◻ No uniformly best estimator; **median unbiasedness** (BN p. 3, **BN only**)
- ◻ Location estimation: $\sum\abs{x_j-\theta}^a$, mean ($a=2$) and median ($a=1$) (BN pp. 3–5, **BN only**)
- ◻ Method of moments; Pearson's crab data, Fig 1 (BN pp. 5–8) ↔ STAT2004 MoM entry
- ◻ Consistency: definition, bias and variance → 0 ⇒ consistent, proof via $\MSE/\varepsilon^2$ (HW 26; BN pp. 30–31) ↔ STAT2004 (PE §5.1, same proof); example $\hat\sigma^2$, $s^2$ consistent (BN pp. 32–33)
- ◻ **ARE**; median vs mean $2/\pi = 0.637$ (HW 27; BN pp. 33–34) ↔ STAT2004 PE §5.2 (duplicate; merge)
- ◻ **Unbiased (UMVU) estimator of a p.f./p.d.f. at a point** via the conditional distribution of $X_1$ given a complete sufficient $T$; normal density with known variance $\phi(x;\bar x,(1-1/n)\sigma^2)$ (LN9 pp. 1–3, **LN only**; LD) — fits after Rao–Blackwell in Ch 41

### Ch 41 Sufficiency, completeness and the exponential family (`ch:sufficiency-exponential-family`) — **STAT3001 primary** ↔ STAT2004 (PE §3.3–4.2)
- ◻ **$d$-parameter exponential family** $L = b(\vect x)\exp\{\vect c(\vect\theta)\T\vect T(\vect x)\}/a(\vect\theta)$; natural parameter; members listed (HW 06; LN3 p. 1); **regular** ($q=d$, Jacobian full rank) (LN3 p. 1 — missing from HW)
- ◻ **Likelihood equation in the REF: $\E_{\hat\theta}\vect T(\vect X) = \vect T(\vect x)$**, scalar proof (HW 07) and vector proof with Jacobian $\mat J(\vect\theta)$ (HW 08; LN3 pp. 2–3; BN pp. 18–19) ↔ STAT2004 PE §3.3
- ◻ Examples: univariate normal in REF, MLEs via $\E T = T$ (HW 05, 09; LN2 pp. 1–3); **multivariate normal in REF** via trace identity, vec remark, MLEs $\bar{\vect x}$ and $\frac1n\sum(\vect x_j-\bar{\vect x})(\vect x_j-\bar{\vect x})\T$ (HW 10–12; LN2 p. 3; LN4 pp. 1–3); MVN log-likelihood, $d = p+\tfrac12p(p+1)$ (HW 05)
- ◻ **Observed information = estimated Fisher information** at $\hat\theta$ in the REF, proof (HW 13; LN3 pp. 3–4; BN p. 19) ↔ STAT2004 PE §3.3 — could sit in Ch 42
- ◻ Sufficiency (conditional definition), $T = H(U)$, minimal sufficiency, completeness, complete ⇒ minimal, REF statistic complete (HW 18; BN pp. 22–23) ↔ STAT2004 PE §4.1
- ◻ **Fisher–Neyman factorisation** (HW 18; BN p. 23), no proof; examples normal $(\bar x,s^2)$, $\Unif[0,\theta]$ ($X_{(n)}$), Bernoulli (BN pp. 24–27) ↔ STAT2004
- ◻ **Rao–Blackwell theorem**, three statements with proof (HW 19; BN p. 28) ↔ STAT2004
- ◻ UMVUE definition; MVB ⇒ UMVUE, converse fails (HW 20)
- ◻ **Lehmann–Scheffé theorem**, proof (HW 20; BN p. 29) ↔ STAT2004
- ◻ **Rao–Blackwell for MSE** (possibly biased $U$) and **generalised R–B for convex loss**, proof via tower property and conditional Jensen (HW 24; LN7 pp. 2–3)
- ◻ **Ancillary statistic; Basu's theorem**, proof (discrete case) (HW 25; LN8 pp. 1–2); example $\sum(X_j-\bar X)^2\indep\bar X$ (LN8 p. 1, **LN only**) ↔ Ch 32 $s^2\indep\bar X$
- ◻ UMVU density estimator (LN9) — see Ch 40 entry

### Ch 42 Likelihood theory (`ch:likelihood-theory`) — **STAT3001 primary** ↔ STAT2004 (PE §3.2, §5.3; R L04–L06)
- ◻ Likelihood, score, Fisher information $\mathcal I(\theta) = \Var(\text{score})$, observed information $I(\hat\theta)$ (HW 13; BN pp. 8–9)
- ◻ Regularity conditions (list of 6) and three results: $\E(\text{score}) = 0$, $\mathcal I = \E I$, CRLB; proofs (HW 14–15; BN pp. 9–12; LN3 pp. 1–2) ↔ STAT2004 (lists differ again: merge HW 14, HW 31, BN p. 36, LN8 "Regularity Conditions (II)")
- ◻ **Multivariate CRLB** $\Cov\vect T\succeq\vect g'\mathcal I^{-1}\vect g'{}\T$ (HW 16; LN5 p. 1), not proved (Bickel & Doksum)
- ◻ MVB estimator definition (HW 16); **necessary and sufficient condition for attaining the MVB** (score linear in $T$) and link to the one-parameter exponential family (BN pp. 20–21, **BN only**; LD lecture 35)
- ◻ CRLB for biased estimators, MSE bound (HW 16; LN7 pp. 1–2) ↔ STAT2004 PE §3.2 Ex
- ◻ Examples: normal known mean, $\hat\sigma^2$ attains MVB; unknown mean, $(\bar X,s^2)$ does not (HW 17; LN5 pp. 1–4); MLE $(\bar X,\hat\sigma^2)$ covariance vs bound (LN5 pp. 4–5, **LN only**)
- ◻ **Kullback–Leibler divergence**, non-negativity proof via Jensen, asymmetry, $\delta_{KL}=0\implies F_1=F_2$ (HW 21–22; LN6 pp. 2–3)
- ◻ Large-sample motivation (HW 26)
- ◻ Asymptotic efficiency: non-uniqueness ($T_n+R_n$ with $\sqrt nR_n\convp0$), **asymptotic CRLB**, asymptotically efficient estimators (HW 28; BN pp. 34–36) ↔ STAT2004 PE §5.3
- ◻ **MLE theory**: $\Prob_{\theta_0}[L(\theta_0)>L(\theta)]\to1$ with proof (HW 29; LN8 Theorem 3 pp. 3–4) ↔ STAT2004 R L05 p5 sketch; **consistent root of the likelihood equation**, three remarks, no proof (HW 30; LN8 Theorem 4 pp. 4–5); **asymptotic normality and efficiency of the MLE** $\sqrt n(\hat\theta_n-\theta_0)\convd\Normal(0,1/i(\theta_0))$, regularity conditions, proof outline only in LN (HW 31; LN8 Theorem 5 pp. 5–8) ↔ STAT2004 R L05 p6
- ◻ **MLE under an incorrect model**: $\hat\theta\to\theta_0$ minimising $\mathrm{KL}[f_0\|f_\theta]$ (HW 33; LN8 pp. 11–12)
- ◻ **Computing MLEs: Newton–Raphson, Fisher scoring, quasi-Newton**; convergence remarks (LN8 pp. 12–15, **LN only**) ↔ Ch 62 Unconstrained optimisation (MATH3204), STAT2004 IRLS (Ch 48)
- ◻ Non-regular example: $\Unif[0,\theta]$ likelihood, Fig 2; normal log-likelihood surface, Fig 3 (BN pp. 14–17) ↔ STAT2004 R L03 uniform figures
- ◻ **Information criteria in model selection**: bias correction of the log likelihood, **AIC**, bootstrap-based EIC, cross-validation-based, MIR, ICOMP (LN18 §6.8 pp. 28–33, **LN only**); Bayesian criteria: Bayes factor, **BIC** (Laplace derivation §6.9.2 **non-examinable** per LD), Laplace–empirical, reversible jump, MML (LN18 §6.9); classification-based CLC, NEC, ICL (LN18 §6.10) — hub to decide scope (LD covered §6.8 and BIC); could instead go to Ch 71 (learning framework) ↔ STAT3006

### Ch 43 Confidence intervals (`ch:confidence-intervals`) ↔ STAT2004 (HW main), STAT1301
- ◻ CI for $\sigma^2$ with $\mu$ known and unknown (LN19a (iii) pp. 3–4) ↔ STAT2004 HW 04
- ◻ CI for $\sigma_1^2/\sigma_2^2$ via $F$ (LN20 pp. 1–2) ↔ STAT2004 CN §6.2.2
- ◻ **Tukey simultaneous CIs** for all $\theta_i-\theta_j$, proof (HW 56; LN22 pp. 1–2); **linear contrasts** with $h = \tfrac12\sum\abs{c_i}$, proof (LN22 pp. 2–3, **LN only**); Montgomery Ex 3.7 (LN22 p. 4); unequal $n_i$ (LN22 p. 5) — or Ch 47 ↔ STAT2004 CN §10.1.6, STAT1301 §8.5

### Ch 44 Hypothesis testing (`ch:hypothesis-testing`) — **STAT3001 primary** ↔ STAT2004 (HW main), STAT1301
- ◻ Hypothesis test as a decision rule; p-value ("as or more extreme"); Type I error, significance level as $\int_RL(\theta_0)$; Type II error, power $\pi = 1-\beta$ (HW 43; LN14 p. 1) ↔ STAT2004 HW 07–12
- ◻ **Neyman–Pearson lemma with proof** (critical-region decomposition) (HW 44; LN14 pp. 1–3) ↔ STAT2004 HW 14 (statement only, "proof in STAT2904") — STAT3001 supplies the proof
- ◻ Normal-mean MP test, $k = \theta_0-\Phi^{-1}(\alpha)\sigma/\sqrt n$ (HW 45; LN14 pp. 3–4) ↔ STAT2004 HW 13–15
- ◻ UMP definition; one-sided UMP, two-sided not UMP (HW 45; LN14 pp. 4–6); **unbiased tests and the UMPU test**, power-function figure (LN14 pp. 5–6, **LN only**)
- ◻ **GLRT** (sup over $\Omega_{H_0}$ / sup over $\Omega$) and **Wilks' theorem** $-2\log\lambda\approx\ChiSq d$, scalar proof by Taylor expansion (HW 46; LN14 pp. 6–7, 12) ↔ STAT2004 HW 22
- ◻ GLRT examples: one-sample $t$-test two-sided (HW 47; LN14 pp. 7–9) and one-sided with boundary MLE, $\lambda(t)$ figure (HW 48; LN14 pp. 10–11); summary of three $t$ critical regions (HW 48) ↔ STAT2004 HW 16
- ◻ **Wald, Wilks and Rao (score) tests** (LN14 pp. 13–14, **LN only**; LD lecture 23)
- ◻ **Two-sample pooled $t$-test from the GLRT** (HW 54; LN19 pp. 1–5) ↔ STAT2004 HW 23–25
- ◻ **Tests on one normal variance**: MP, UMP, equal-tails two-sided test, LRT with unequal tails ($\lambda(k_1)=\lambda(k_2)$), one-sided LRT (LN19a pp. 1–7, **LN only**) ↔ STAT2004 CN §7.2.2
- ◻ **Homoscedasticity**: $F$-test by CI inversion; LRT for two classes; $g$-class multivariate form $\sum n_i\log(\abs{\hat{\mat\Sigma}_i}/\abs{\hat{\mat\Sigma}})$; sensitivity to non-normality (LN20 pp. 1–4, **LN only**) ↔ STAT2004 CN §7.3.2
- ◻ **Satterthwaite's approximation** and Welch's $t$ df, derivation (HW 55; LN21 pp. 1–2)
- ◻ **Multiple testing**: multiplicity problem; **FWER**, union bound, independent case; **Bonferroni** (HW 50; LN15) ↔ STAT2004 HW 40, STAT1301 §8.5; outcome table $a,b,c,d,N_0,N_1,N_r$ and FWER $=\Prob(b\ge1)$ (HW 50; LN16 pp. 1–3); **FDP** (with FDP $:=0$ when $N_r=0$, LN16 p. 3), **FDR**, two properties with proof (HW 51; LN16 p. 3); FDR conditional form (HW 51; LN16 p. 4); FNDR (LN16 p. 1, **LN only**); **Benjamini–Hochberg** procedure, FDR-corrected and FDR-adjusted values (HW 52; LN16 pp. 4–5); worked table of 25 tests (LN16 p. 5, **LN only**)
- ◻ **Errors in testing: PPV**, sensitivity, specificity, prior odds, Bayes; NPV; fallacy of the transposed conditional (HW 53; LN17 pp. 2–3) ↔ Ch 25 Bayes' rule; cancer-test Example 1 (LN17 p. 1); numerical PPVs 0.09 and 0.497 (LN17 p. 4); repeated positive tests, Ioannidis discussion (LN17 p. 5) — **LN only**

### Ch 45 Categorical data analysis (`ch:categorical-data`) ↔ STAT2004 (HW 26–33), STAT1301 Ch 11
- ◻ **$\chi^2$ goodness of fit via the GLRT**: multinomial likelihood, MLE $o_j/n$ (derivation LN14 p. 16), $-2\log\lambda$, Taylor expansion of $\log(1+x)$, $\sum(o_j-e_j)^2/e_j\approx\ChiSq{r-1}$ (HW 49; LN14 pp. 15–17) ↔ STAT2004 HW 26–28 (same derivation; merge)
- ◻ df adjustment when parameters are estimated (LD lecture 24; **no uploaded source**) ↔ STAT2004 CN Thm 8.2
- ◻ **Simpson's paradox**, kidney-stone data table (LN14 p. 18, **LN only**) ↔ STAT1301

### Ch 47 Analysis of variance (`ch:anova`) ↔ STAT2004, STAT1301
- ◻ Tukey's studentised range: definition, distribution depends on $k,\nu$ (HW 56; LN22 p. 1) — CIs in Ch 43 entry; ANOVA example (LN22 p. 4) ↔ STAT2004 CN §10.1.6, STAT1301 §8.5

### Ch 50 Bayesian inference (`ch:bayesian-inference`) ↔ STAT3500 (primary), STAT2004
- ◻ Recap of MLE properties with annotations (S1.2); frequentist vs Bayesian, flow sketch figure (S1.3)
- ◻ Three steps: prior, likelihood, posterior ∝ likelihood × prior (S1.4) ↔ STAT2004 A W7L3
- ◻ Coin example, $n=10$, $s=3$: three hand-drawn priors figure; uniform prior → $\BetaDist(x+1,11-x)$, posterior mean $1/3$ vs MLE $0.3$ (S1.5–6) ↔ STAT2004 Skittles example
- ◻ **Beta–binomial model**: prior figure Beta(30,30) vs Beta(3,3); posterior $\BetaDist(x+\alpha,n+\beta-x)$ (S1.7)
- ◻ Bayesian point estimators: posterior mean, mode, median, variance (S1.8)
- ◻ Interpretation of hyperparameters as pseudo-observations (S1.9); **posterior mean = $w\,\E\theta+(1-w)\hat\theta$** (S1.10)
- ◻ Quiz: $\BetaDist(1,10)$ prior, plot (S1.11)
- ◻ LN25 (Wasserman Ch 11) covered in lectures but **not uploaded**

### Ch 51 The EM algorithm and the bootstrap (`ch:em-bootstrap`) — **STAT3001 only**
- ◻ EM background: incomplete data (missing, truncated, mixtures, convolutions), key idea (HW 34; LN10 pp. 1–3)
- ◻ Formulation: complete data $\vect x$, observed $\vect y$, $f(\vect y;\vect\theta) = \int_{\mathcal X(\vect y)}f_c$ (HW 34, with the author's "swap!" correction; LN10 p. 4)
- ◻ **E- and M-steps**, $Q(\vect\theta;\vect\theta^{(k)})$, stopping rule; specification remark (HW 35; LN10 pp. 4–5)
- ◻ **EM for the regular exponential family**: M-step solves $\E_{\vect\theta}\vect t(\vect X) = \vect t^{(k)}$ (HW 36; LN10 pp. 5–6)
- ◻ **Generalised EM** (HW 37; LN10 pp. 5, 8); ECM/ECME non-examinable (HW 37; LN11) — omit or one remark
- ◻ **Monotonicity** $L(\vect\theta^{(k+1)})\ge L(\vect\theta^{(k)})$, proof via $Q-H$ and Jensen; self-consistency (HW 38; LN10 pp. 7–8)
- ◻ **Convergence**: to a stationary value, saddle points, dependence on $\vect\theta^{(0)}$; Wu's condition and regularity conditions (HW 39; LN10 pp. 8–10)
- ◻ **Grouped and truncated data**: multinomial observed likelihood, missing $\vect u$, $\vect w_j$, $h_j$, $d(\vect u\given\vect y)$, $c_2$ (HW 40; LN12 pp. 1–2); E- and M-steps, $n_j^{(k)}$, normal M-step (HW 41; LN12 pp. 3–4); truncated distributions (HW 42; LN13) ↔ Ch 31 entry
- ◻ Numerical example: red blood cell volumes, Tables 1–2 (LN12 pp. 4–6, **LN only**)
- ◻ Mixture-model EM (two-component normal, known variance; unbounded likelihood with unequal covariances): LD lectures 16–20 only, **no uploaded source** ↔ Ch 79 (STAT3006 mixtures)
- ◻ **Bootstrap**: idea, Monte Carlo with known $F$, nonparametric ($F_n$, resampling) and parametric ($F_{\hat\theta}$) bootstrap estimates (LN23 pp. 1–2, **LN only**) ↔ Ch 37
- ◻ **Bootstrapping the LRTS for the number of mixture components**, implementation, examples, double bootstrap (LN18 §6.6–6.7 pp. 18–28, **LN only**; figures 6.7–6.10 need data not supplied)
- ◻ Bootstrap bias correction of the apparent error rate of a linear discriminant (LN24, **LN only**) ↔ Ch 73 (classification)
- ◻ Bootstrap for regression models: LD lecture 31 only, **no uploaded source**
- ◻ Other LN18 material (§6.1–6.5, §6.10–6.11): assessing the number of components — mostly beyond the course's examinable scope; hub to decide (↔ Ch 79)

### Ch 90 Programming in R (`ch:r-programming`)
- R functions used in S2: `rnorm`, `runif`, `rexp`, `numeric`, `matrix`, `outer`, `seq`, `plot`, `mean`, `rgl::persp3d`, `MASS::kde2d`, `contour`.

---

## Figures (all to redraw in TikZ/pgfplots)
| Source | Figure | Target |
|---|---|---|
| S1.3 | Frequentist "data → model" vs Bayesian "prior, data → model" flow sketches | Ch 50 |
| S1.5 | Three priors on $[0,1]$: peaked at 0.5, flat, U-shaped | Ch 50 |
| S1.7 | $\BetaDist(30,30)$ vs $\BetaDist(3,3)$ densities | Ch 50 |
| S1.11 | $\BetaDist(1,10)$ density | Ch 50 |
| LN14 p. 6 | Power functions: two one-sided UMP tests and the UMPU test through $(\theta_0,\alpha)$ | Ch 44 |
| LN14 p. 10 | $\lambda(t)$ for the one-sided $t$-test with threshold $c$, $c^*$ | Ch 44 |
| LN16 p. 1 | FDR outcome table (also HW 50 table) | Ch 44 (table) |
| BN p. 8, Fig 1 | Crab-ratio histogram with one- and two-component normal fits (data not supplied) | Ch 40 |
| BN p. 16, Fig 2 | $\Unif[0,\theta]$ likelihood, $x_{(n)} = 2$ | Ch 42 |
| BN p. 17, Fig 3 | Normal log-likelihood surface over $(\mu,\sigma^2)$ | Ch 42 |
| LN18 Figs 6.1–6.10 | Kernel densities, Q–Q plots, stamp/acidity/enzyme/galaxy histograms with mixture fits, galaxy contour maps, bootstrap percentile plots (data not supplied) | Ch 51 (if kept) |
| HW | No figures in the handwritten notes; only tables (HW 50 outcome table) | — |

---

## Not used / out of scope
- LN11 (ECM, ECME): non-examinable per HW 37.
- LN18 §6.9.2 (Laplace's method, BIC derivation): not examinable per LD.
- LD's administrative remarks; references' publication years (no dates rule).
- LN24's journal front matter.

## Suspected errors in the notes
_Kept in the transcriptions; to be corrected when drafting._

**Handwritten notes (HW)**
1. HW 01: "Def." for a result; the proof shows only mean and covariance, not normality (LN1 p. 2 has the MGF argument).
2. HW 02: $\mat\Sigma_{11}-\mat\Sigma_{12}\mat\Sigma_{22}^{-1}\mat\Sigma_{21}$ is the Schur complement of $\mat\Sigma_{22}$, not $\mat\Sigma_{11}$.
3. HW 03: statement writes $\Normal(\vect\mu,\sigma^2\mat I)$ but uses a common mean $\mu$.
4. HW 04: $Y_i\sim\Normal(0,\sigma^2)$ only for $i<n$; zero mean not shown; "Cochran's theorem" where the definition of $\ChiSq{n-1}$ suffices.
5. HW 05: last term of the univariate log-likelihood should be $-n\mu^2/(2\sigma^2)$.
6. HW 06: heading says "regular" but the regularity condition ($q=d$, full-rank Jacobian) is missing.
7. HW 07: the expectation step uses $\E(\text{score}) = 0$, not the vanishing of the score at $\hat\theta$; needs $c'(\hat\theta)\ne0$.
8. HW 08: $\mat J$ non-singular by the definition of *regular*, not "trivially".
9. HW 09 (and LN2 p. 2): the expression given for $a(\vect\theta)$ is $\log a(\vect\theta)$.
10. HW 10: $n\bar{\vect x}\bar{\vect x}\T$ placed inside the sum.
11. HW 12 vs LN4 p. 3: vec stacks columns (HW) vs rows (LN4); pick one.
12. HW 13: Fisher information for a vector written $\E[\cdot]^2$; should be $\E[\vect S\vect S\T]$; one symbol for observed and expected information.
13. HW 14: CRLB stated without defining $T$ (unbiased for $g(\theta)$).
14. HW 15: Cauchy–Schwarz inequality reversed ("$\ge$" should be "$\le$") (same slip as STAT2004 PE §3.2).
15. HW 16: estimator called $T$ then $W$.
16. HW 18: completeness quantifiers (for all $\theta$; $g(T)=0$ with probability 1); "complete ⇒ minimal" needs sufficiency.
17. HW 19: statement 1 should be about $W(T)$, not $U(T)$; statement 3 should be "$\le$".
18. HW 23: $\E[(W-\theta)^2]$ written without the square (retake requested).
19. HW 24: $U(T)=\E[U\given T]$ should be $W(T)$; "less than" should be "no greater than".
20. HW 25: Basu proof attributes "does not depend on $\theta$" to completeness; it is sufficiency, and completeness gives $f(v\given t)\equiv f(v)$.
21. HW 31: regularity remark's final sentence ambiguous; $A$ undefined; "for all $\theta$ in the interval" missing.
22. HW 35: first E-step subscript $\vect\theta_0$ for $\vect\theta^{(0)}$.
23. HW 36: "convexity of the log-likelihood" should be concavity; "exponential family" should be regular exponential family.
24. HW 38: $H$ not defined; $H(\vect\theta^{(k)}-\vect\theta^{(k)})$ for $H(\vect\theta^{(k)};\vect\theta^{(k)})$.
25. HW 39: Wu's condition 1 needs "for any stationary point that is not a local maximiser"; condition 3 should use $\ge$ and "for any $L(\vect\theta_0)>-\infty$" (LN10 (34)–(36)).
26. HW 42: proof treats a density as a probability (discrete case only, as LN13 says); "$V\in A$" for "$V\in R$".
27. HW 44: NP proof's third line has $L(\vect\theta_1)$ for $L(\vect\theta_0)$ in the second integral; inequality should be "$\ge$" and the conclusion "no less than"; "exists and is unique" unproved.
28. HW 45: $\theta$ and $\mu$ subscripts mixed; $k$ reused.
29. HW 46: Taylor-expansion "=" should be "≈"; $I(\theta)$ for $I(\hat\theta)$; $I(\hat\theta)/\mathcal I(\theta_0)\to1$ unstated.
30. HW 48: second summary line should read $H_1:\mu<\mu_0$ and "$\mu_0 - t$" (sign blotted).
31. HW 51: FDR property 2 stated as strict "$<$" but proved as "$\le$"; $p_i$ undefined.
32. HW 53: NPV written $\Prob(D\text{ absent}\given D\text{ negative})$; should be "$T$ negative".
33. HW 55: final approximation's numerator should be $(\sum a_iw_i)^2$.
34. HW 56: $u_{(n)}$ for $u_{(k)}$; independence assumptions unstated.

**Typed sources**
35. LN2 p. 2: $a(\vect\theta)$ given as its logarithm (as HW 09).
36. S2.9 code: comment "Log posterior" but `post` returns the posterior (not its log); `return(-Inf)` is the log-scale convention (should be `0` on the density scale; the sampler still works).
37. S1.6: step numbered "2)" for the posterior (overwritten "3"); "looks lie" [sic] on S1.7.

## Notation the book doesn't have yet
(Overlaps the STAT2004 requests; listed here so the hub can decide them together.)

| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\Info`, `\ObsInfo`, `\info` | $\mathcal I(\theta)$, $I(\theta)$ (or $J$), $i(\theta)$ | expected (Fisher) information, observed information, per-observation information | HW, LN3 and BN use one handwritten symbol for both expected and observed; STAT2004 request already open |
| `\ParSpace` | $\Omega$ or $\Theta$ | parameter space | HW/LN/BN use $\Omega$ (clashes with sample space in Part III); STAT2004 request open |
| `\score` | $S(\vect x;\theta)$ or $U(\theta)$ | score statistic | BN writes $S$; STAT2004 R L writes $U$ |
| `\psdge` (or use `\succeq`) | $\succeq$ | Loewner order (PSD difference) | Multivariate CRLB (HW 16, LN5) |
| `\vecop` (operator) | $\operatorname{vec}$ | vectorisation | HW 12, LN4; also fix the stacking convention |
| `\KL` | $\mathrm{KL}[f_1\,\|\,f_2]$ or $\delta_{KL}(F_1,F_2)$ | Kullback–Leibler divergence | HW 21–22, 33, LN6, LN8; also used in Part VI (STAT3006–3008) |
| `\hatr`/convention for restricted MLE | $\hat{\hat{\vect\theta}}$ vs $\tilde{\vect\theta}$ | MLE under $H_0$ | HW 47, 54, LN14, LN19 use double hats |
| `\GLR` | $\lambda$ or $\Lambda$ | (generalised) likelihood ratio | STAT3001 uses $\lambda$ (and LRT ratio alternative/null, HW 44); STAT2004 uses $\Lambda$/$\Omega$ with null/alternative — ratio direction differs too |
| `\InvGamma` | $\mathrm{Inv\text{-}Gamma}(\alpha,\beta)$ | inverse-gamma distribution | S2.14 |
| `\FDR`, `\FWER`, `\FDP`, `\PPV` (operators) | upright abbreviations | multiple-testing quantities | HW 50–53 |
| `\quant` convention | $t_{n-1;1-\alpha}$ vs $t^{1-\alpha}_{n-1}$, $\chi^2_{d;1-\alpha}$, $T_{k,\nu;1-\alpha}$ | quantiles | HW mixes two forms on one page (HW 48); STAT2004 request open |
| `\Tukey` or plain | $T_{k,\nu;1-\alpha}$ | studentised range quantile | HW 56, LN22 |

Also: the book's `\convd`/`\convp` replace the notes' "$\xrightarrow{\ell}$", "$\xrightarrow{L}$", "$\xrightarrow{P_\theta}$".

## Code in the notes
| Where | Language | What it does |
|---|---|---|
| S2.9 | R | Random-walk Metropolis–Hastings for the Beta–binomial posterior ($n=10$, $x=3$, $\alpha=\beta=2$, $N=10\,000$, proposal sd 0.1); trace plot; MCMC mean vs exact posterior mean $(a+x)/(a+b+n)$ |
| S2.13 | R | Gibbs sampler for $f(x_1,x_2)\propto e^{-x_1x_2-x_1-x_2}$ with exponential full conditionals; 3-D density surface (`rgl::persp3d`); scatter of draws with a 2-D kernel density contour (`MASS::kde2d`) |
| S2.10, S2.14 | — | Exercises asking for R code (no solutions) |
| HW, LN, BN | — | No code |
