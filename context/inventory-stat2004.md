# Coverage inventory: STAT2004 Statistical Modelling & Analysis

_Built in the transcription phase from 51 photos of the handwritten notes, the typed *Notes on Point Estimation*, the course notes, and the later iteration's lectures and exercise sheets. Nothing is written yet._

**Sources.** Transcriptions and indexes: `claude/notes-stat2004-1.md` … `-4.md`.
- **HW nn**: handwritten page nn (51 pages, second half of the course: CIs → linear models). **Main source for the second half.**
- **PE §x**: *Notes on Point Estimation* (typed, 28 pp.). **Main source for the first half** (estimation).
- **CN §x / Ex / Thm / Fig**: the lecturer's course notes (146 pp.). Supplement for the whole course; the only source for simple linear regression (CN Ch 9), randomised block designs and several tests.
- **R Lnn pk**: later iteration, first-half lectures (estimation, likelihood, regression, logistic regression). **A WwLl pk**: later iteration, second-half lectures (parallel to HW). Supplements.
- **AC w / Tut w**: later iteration's applied-class and tutorial exercises (example pool).

**Code:** the course used R (CN has none; HW and A lectures quote R calls and live "R DEMO"s; R L and AC solutions use `optim`, `lm`, `glm`, `boxcox`). Part IV uses R, so this carries over directly. **Content rule:** source material only, with corrections. **Status:** ◻ to do (nothing drafted). **↔** = merge with an entry from another course or an existing chapter rather than add new.

**Main-source rule (from the user):** first half (Ch 39–42 material) follows PE, supplemented by CN and R L01–L06; second half (Ch 43–47) follows HW, supplemented by CN and A W7–W13. The regression and GLM material of R L07–L12 has no handwritten counterpart and is supplementary only.

---

## Part III cross-listings

### Ch 29 Common distributions (`ch:common-distributions`)
- ↔ Discrete and continuous distributions, CN §2.4–2.5.6 with Figs 2.3–2.10 (already covered by STAT2003; figures only if useful)
- ◻ $F$-distribution: density, moments, $F_{m_1,m_2}$ as a ratio of independent $\chi^2$/df (CN §2.5.7, Thm 2.2, Fig 2.11)
- ◻ $t$-distribution: density, moments, $Z/\sqrt{V/m}\sim t_m$ (CN §2.5.8, Thm 2.3, Fig 2.12; A W7L1-2 p6 figure $\Normal(0,1)$, $t_2$, $t_{30}$)
- ↔ Chi-squared as $\GammaDist(k/2,1/2)$; $\E Q = k$, $\Var Q = 2k$, MGF $(1-2t)^{-k/2}$ (PE §1.3, R L01 p3–4; STAT2003 Ch 29)

### Ch 30 Multivariate distributions (`ch:multivariate-distributions`)
- ↔ Joint distributions, independence, expectation, covariance properties (Table 3.1), multinomial (CN §3.1–3.2, Def 3.1–3.5, Figs 3.1–3.3) — STAT2003/STAT1301 already written
- ↔ $\vect\mu_{\mat A\vect Z} = \mat A\vect\mu$, $\Sigma = \mat A\Sigma_Z\mat A\T$ (CN Thm 3.7; R L07 p3 "STAT2003 claim 45")

### Ch 32 Transformations of random variables (`ch:transformations`)
- ◻ Linear transformation of densities $f_{\vect X}(\vect x) = f_{\vect Z}(\mat A^{-1}\vect x)/\abs{\mat A}$, Fig 3.4 (CN §3.3) ↔ STAT2003 HW 28
- ◻ $X_1^2+\dots+X_n^2\sim\ChiSq n$ for iid $\Normal(0,1)$ (CN Thm 3.6) ↔ STAT2003
- ◻ Jointly normal: bivariate normal, uncorrelated ⇒ independent, **Fisher's lemma** (orthogonal $\mat B$), linear combinations, ball-bearings example (CN §3.4, Thm 3.8–3.10, Ex 3.9–3.11) ↔ STAT2003 MVN entries
- ◻ **$\bar X\indep S^2$ for normal samples** (proof via MVN and zero covariance: R L01 p2–3) and **$(n-1)S^2/\sigma^2\sim\ChiSq{n-1}$** (MGF proof: R L01 p3–4); stated without proof in PE §1.3, CN Thm 6.2, HW 03 ("WHY?"), A W7L1-2 p5–6. _Could instead open Ch 39; hub to decide._

### Ch 33 Limit theorems (`ch:limit-theorems`)
- ↔ WLLN, CLT, normal approximation to the binomial (Fig 3.5–3.6), multinomial CLT Thm 3.14 (CN §3.5) — STAT2003/STAT3004
- ◻ Continuous mapping theorem for $\convp$ (R L02 p4), example: odds $\hat p/(1-\hat p)$ consistent
- ◻ Delta method, scalar and multivariate (R L05 p6, R L06 p3; AC 7 Q1(b)); could sit in Ch 42 instead

### Ch 37 Simulation (`ch:simulation-monte-carlo`)
- ◻ Simulation studies of estimators (bias, variance, MSE scaled by $n$; AC 2 Q4) and of CI coverage (Tut 9 Ex 1); simulating bivariate normal regression data (CN §9.3) — examples only

---

## Part IV

### Ch 38 Data, exploratory analysis and study design (`ch:eda-study-design`)
- ◻ Milk-carton data analysis: histogram Fig 4.1, summary statistics (CN Ex 4.1) ↔ STAT1301 Ch 5 descriptive statistics
- ◻ Data fabrication (too little variability; Fisher on Mendel, p-value 0.9996) (HW 29, A W10L3 p2)
- ◻ **Pseudo-replication**: two designs for comparing fertilisers, figure (HW 29, A W10L3 p3 figure) ↔ STAT1301 §8.4 randomisation and blocking
- ◻ Numbers as category labels warning (A W11L1-2 p5)

### Ch 39 Statistical models and sampling distributions (`ch:sampling-distributions`)
- ◻ Statistical inference framing; modelling process flow chart Fig 4.2 (CN §4.2, Rem 4.1; PE §1) ↔ STAT1301 §4.1
- ◻ Random sample, iid; statistic; sampling distribution; common statistics (R L01 p1; PE §1.1) ↔ STAT1301
- ◻ Statistical model $\mathcal F$; parametric model $\{f(\cdot;\theta):\theta\in\Theta\}$, parameter space; identifiability (R L01 p5; PE §1.1)
- ◻ Sampling distribution of $\bar X$: $\E\bar X = \mu$, $\Var\bar X = \sigma^2/n$; normal case (R L01 p1; PE §1.2)
- ◻ Sample variance and $\chi^2$ (PE §1.3) — proofs per Ch 32 entry
- ◻ $t$ statistic: $(\bar X-\mu)/(S/\sqrt n)\sim t_{n-1}$ (CN Thm 6.1 with proof; A W7L1-2 p6) ↔ STAT1301 Thm 6.2
- ◻ Two-sample pooled $t$ (CN Thm 6.3) and variance ratio $F$ (CN Thm 6.4 with proof)

### Ch 40 Point estimation (`ch:point-estimation`) — **PE main source**
- ◻ Estimate vs estimator; statistic (PE §1.1; CN §5.1, Ex 5.1–5.2, Rem 5.1–5.2; R L01 p5) ↔ STAT1301 §6.2
- ◻ Method of moments: definition (PE §2); general mean/variance (PE §2, CN Ex 5.3); Bernoulli (CN Ex 5.4, R L01 p6); normal (R L01 p6); geometric $1/\bar X$ (R L01 p6); **zero-inflated Poisson** and whether the estimates lie in $\Theta$ (R L01 p6–7); **sample correlation as a MoM estimator** (CN Ex 5.5); exercises AC 2 Q2, Q5 ↔ STAT1301 Ex 6.3
- ◻ Maximum likelihood: water-bottle motivation (PE §3); likelihood definition and interpretation (PE §3.1; CN Def 5.1, Rem 5.3–5.4, Ex 5.6–5.9; R L03 p1, Bernoulli likelihood figure); log-likelihood (PE Rem); MLE definition (PE §3.1; CN Def 5.2, Fig 5.1; R L03 p2); likelihood equations (PE Thm)
- ◻ Finding MLEs: calculus facts (R L03 p2); exponential (R L03 p2–3); Poisson and **non-existence when $s=0$** (R L03 p3, figure); **non-uniqueness** (Laplace location, R L03 p4); **multiple local maxima** (Cauchy, R L03 p5); uniform $[0,\theta]$ (PE §3.1; R L03 p5–6, two figures); binomial (CN §5.3.1); normal two-parameter via profiling (CN §5.3.2, Rem 5.7; R L03 p6–7); Bernoulli (R L04 p1); Weibull likelihood with no closed form (R L04 p1); exercises AC 3
- ◻ Invariance: MLE of $g(\theta)$ is $g(\hat\theta)$ (PE §3.1 Def; CN Def 5.3, Rem 5.6; R L03 p7 proof for one-to-one $g$; induced likelihood for general $g$, MLE of $\sigma$, R L03 p8)
- ◻ Bias, unbiasedness; $X_1$ vs $\bar X$ (PE §1.2; CN Ex 5.10; R L02 p1); $\hat\sigma^2$ bias $-\sigma^2/n$ (R L02 p1, CN Ex 5.10, PE §5.1) ↔ STAT1301
- ◻ MSE; MSE = Var + bias² (proof) (PE §1.2; CN Ex 5.10; R L02 p1–2); bias–variance trade-off; "more efficient" (CN §5.4); **MSE of $S^2$ vs $\hat\sigma^2$** (R L02 p2); exercises AC 2 Q1–2
- ◻ Consistency: definition (PE §5.1; R L02 p3); Bias → 0 and Var → 0 ⇒ consistent (PE §5.1 proof; R L02 p3 via Markov); examples Bernoulli (R L02 p3), $\hat\sigma^2$ (PE §5.1); continuous mapping (see Ch 33); exercises AC 2 Q4, AC 3 Q3
- ◻ Comparing estimators asymptotically: ARE, median vs mean $2/\pi$ (PE §5.2)
- ◻ Code (computing section): simulation study of $1/\bar X$ (AC 2 Q4); `optim` for the ZIP MLE (AC 3 Q5)

### Ch 41 Sufficiency, completeness and the exponential family (`ch:sufficiency-exponential-family`) — PE only; ↔ STAT3001 (primary)
- ◻ Exponential family, regular family, normal example (PE §3.3); MLE solves $\E T(\vect X) = T(\vect x)$ (PE §3.3 Thm, proof, normal example); observed = expected information at $\hat\theta$ (PE §3.3 Thm, proof)
- ◻ Sufficiency, minimal sufficiency, completeness; remarks; Bernoulli example (PE §4.1)
- ◻ Regular exponential family ⇒ complete sufficient (PE §4.1 Thm, no proof)
- ◻ Fisher–Neyman factorisation (no proof); normal example (PE §4.1); sufficiency of $\bar X$ for $\mu$ noted in CN Ex 5.9 and A W9L1-2 p2
- ◻ Rao–Blackwell (proof), UMVU, MVB ⇒ UMVU, Lehmann–Scheffé (proof), Bernoulli example (PE §4.2)
- ◻ MVB estimators and the exponential family (PE §3.4, Thm with proof, $\Normal(\theta,1)$ example) — could sit in Ch 42 beside the CRLB

### Ch 42 Likelihood theory (`ch:likelihood-theory`) — PE main; ↔ STAT3001
- ◻ Regularity conditions (PE §3.2 list; R L05 p4 list from CB — the two lists differ, merge)
- ◻ Score; $\E U = 0$ (PE §3.2 proof; R L04 p2); Fisher information $I(\theta) = \Var U$ (PE §3.2; R L04 p2); $I = -\E\ell''$ (PE §3.2 proof; R L05 p1); observed information $J$ (R L05 p1; PE uses the same symbol $I$); iid case $I = n\,i(\theta)$ (R L05 p1); Bernoulli score, $I$, $i$, $J$ (R L05 p2)
- ◻ **Cramér–Rao lower bound** with proof (PE §3.2; R L05 p3); bound for biased estimators (PE §3.2 Ex); attainment, Bernoulli (R L05 p4; PE §4.2 Ex); MVB (see Ch 41); exercise AC 4 Q1(d)
- ◻ Consistency of the MLE (R L05 p4 statement; p5 proof sketch via LLN and Jensen)
- ◻ Asymptotic normality and efficiency: asymptotic variance with counterexample $Z+Y/n$, $Y\sim t_2$ (R L05 p5); asymptotic normality definition, non-uniqueness remark (PE §5.3); asymptotic CRLB, asymptotic efficiency (PE §5.3); **asymptotic normality of the MLE with delta method, proof sketch** (R L05 p6); $\hat\theta\approx\Normal(\theta_0,1/(n\,i(\theta_0)))$; example: Poisson $e^{-\lambda}$, MLE vs unbiased $\bar Y$ vs CRLB (R L05 p7); exercises AC 4 Q1–2 (boundary cases where it fails)
- ◻ Multiparameter: score vector, information matrix (PSD), observed information matrix, $\sqrt n(\hat{\vect\theta}-\vect\theta_0)\convd\Normal(\vect 0, i^{-1})$ (R L06 p1); normal $(\mu,\sigma^2)$ information (R L06 p2); multivariate delta method, MLE of $\sigma$ (R L06 p3); exercises AC 4 Q3, Q5
- ◻ Profile likelihood (R L03 p6 mention; Box–Cox profile, R L10 p1)
- ◻ Code: standard errors from the Hessian with `optim` (AC 4 Q4)

### Ch 43 Confidence intervals (`ch:confidence-intervals`) — **HW main source**; ↔ STAT1301 Ch 6, STAT3001
- ◻ Margin of error and level of confidence; CI for $p$ recalled (HW 01; A W7L1-2 p1–2 with Skittles demo)
- ◻ **Pivot variables**: definition, standardisation example, 95% CI for $\mu$ ($\sigma$ known), what is random (HW 02; A W7L1-2 p3–5, figure; CN §6 intro, Ex 6.2)
- ◻ General CI definition, exact and **conservative** CIs; remarks (HW 06; A W7L3 p3–4; CN Def 6.1, Rem 6.1–6.2)
- ◻ Normal one sample: $\mu$ with $\sigma^2$ unknown via $t$ (HW 03; CN §6.1.1, Thm 6.1, Ex 6.3; A W7L1-2 p5–7 incl. `qt`) ↔ STAT1301 Thm 6.3
- ◻ Normal one sample: $\sigma^2$ and $\sigma$, multiplicative margins, aspirin example (HW 04; CN §6.1.2, Thm 6.2, Ex 6.4; A W7L1-2 p8–10 with $\chi^2$ figures and `qchisq`) ↔ STAT1301 Thm 6.4, Ex 6.6
- ◻ No exact pivots for discrete data, $\Bin(5,0.4)$ illustration (A W7L1-2 p10–11)
- ◻ Binomial one sample: asymptotic pivot, CI, rule of thumb 10 successes/failures (HW 05; CN §6.3, Ex 6.7–6.8; A W7L3 p1–2) ↔ STAT1301 §6.3
- ◻ Normal two samples: $\mu_1-\mu_2$ pooled (CN §6.2.1, Thm 6.3, Ex 6.5); $\sigma_1^2/\sigma_2^2$ (CN §6.2.2, Thm 6.4, Ex 6.6) ↔ STAT1301 Thm 6.5
- ◻ Binomial two samples (CN §6.4, Ex 6.9–6.10) ↔ STAT1301 Ex 6.10–6.11
- ◻ Duality with tests; CIs by inverting tests (HW 21; A W9L3 p2–3)
- ◻ Interpretation; frequentist vs Bayesian "philosophy corner" (A W7L1-2 p10; A W7L3 p4)
- ◻ Code: `qt`, `qchisq`; $t$-interval robustness simulation (Tut 9 Ex 1); exponential pivot exercise (Tut 8 Ex 1)

### Ch 44 Hypothesis testing (`ch:hypothesis-testing`) — **HW main source**; ↔ STAT1301 Ch 7, STAT3001
- ◻ Tests as decision rules; LDL-cholesterol motivating example with candidate rules (HW 07; A W8L1-2 p3–4); CN motivating examples (Ex 7.1 blood pressure, Ex 7.2 tennis)
- ◻ Null and alternative hypotheses; simple, one-sided, two-sided; gravity example (HW 08; CN §7.1.1; A W8L1-2 p5)
- ◻ Test statistics (MoM/MLE starting points) and critical regions (HW 09; CN §7.1.2–7.1.3; A W8L1-2 p6–7)
- ◻ Type I error and significance level; LDL computations 7.8%, 1%, 17.2% (HW 10; CN §7.1.5; A W8L1-2 p8–10, A W8L3 p1–2, figures)
- ◻ Type II error, power, power curve; LDL power 11.9%, 76.1% (HW 11–12; CN Def 7.1; A W8L3 p2–4, figures)
- ◻ Neyman–Pearson paradigm; field conventions for $\alpha$ (HW 13; A W8L3 p4)
- ◻ **Likelihood ratio test**; **Neyman–Pearson lemma** (statement only; "proof in STAT2904") (HW 13–14; A W8L3 p5–6)
- ◻ LRT for a normal mean ⇒ $\{\bar X\ge d\}$, number-line figure; setting $d$; UMP; left-sided and two-sided cases; two-sided not UMP (HW 14–15; A W9L1-2 p1–4, figures)
- ◻ $t$-tests from the LRT with unknown variance; $z$-test (HW 16; CN §7.2.1, Rem 7.3; A W9L1-2 p5) ↔ STAT1301 §7.2
- ◻ **Poisson LRT** (calls per hour), exact cut-off with `qpois`/`ppois`, comparison with a blind $t$-test, robustness (HW 17–18; A W9L1-2 p6–9)
- ◻ Design before data (Fisher's "post-mortem" remark) (A W9L1-2 p9; A W9L3 p1)
- ◻ p-values: definitions for the three alternatives; Poisson example p = 0.02; evidence scale figure; misinterpretations (HW 19–20; CN §7.1.4, Rem 7.1; A W9L1-2 p10–11, A W9L3 p1–2)
- ◻ 8 steps of a test (CN §7.1.6) ↔ STAT1301 §7.1
- ◻ Duality of tests and CIs (HW 21; A W9L3 p2–3) — cross-reference Ch 43
- ◻ **Generalised likelihood ratio test**: definition, $\Theta_0\subset\Theta$ figure (HW 22; A W9L3 p4–5, figures)
- ◻ GLRT for two normal means: parameter-plane figure, SS decomposition, two-sample $z$-test and pooled $t$-test (HW 23–25; A W9L3 p5–6, A W10L1-2 p1–4, figures) ↔ STAT1301 §7.5
- ◻ CN-only tests: $\sigma^2$ (§7.2.2, Ex 7.12); $F$-test for equal variances (§7.3.2, Ex 7.15); paired samples (§7.4); binomial one sample (§7.5, Ex 7.16, Rem 7.5–7.6) and two samples (§7.6, Ex 7.17–7.18); sign test (§7.7, Ex 7.19–7.20) ↔ STAT1301 §7.4–7.6
- ◻ Multiple comparisons in general ↔ STAT1301 §8.5 (Bonferroni appears in Ch 47 entry)
- ◻ Code: `pnorm`, `qpois`, `ppois`, `qchisq`, `pchisq`; exercises Tut 9 Ex 2–4

### Ch 45 Categorical data analysis (`ch:categorical-data`) — HW main; ↔ STAT1301 Ch 11
- ◻ Multinomial model for $k$ categories, $k-1$ free parameters (HW 26; A W10L1-2 p5–6; CN Thm 8.1 setting) ↔ Ch 30 multinomial
- ◻ **GLRT for a simple multinomial null**: $-\log\Lambda = \sum O_k\log(O_k/E_k)$ (HW 26–27; A W10L1-2 p7–8)
- ◻ Why Pearson's $\chi^2$ (four reasons; asymptotic equivalence to $-2\log\Lambda$) (HW 28; A W10L1-2 p9)
- ◻ GoF with known parameters: Thm 8.1, rule of thumb (CN §8.1, Rem 8.1–8.2, frizzled chickens Ex 8.2; army recruits Ex 8.1) ↔ STAT1301 Thm 11.1
- ◻ **Mendel example** ($-2\log\Lambda = 0.618$, $\chi^2 = 0.604$, p ≈ 0.9; $\chi^2_3$ figures) (A W10L1-2 p10–11, A W10L3 p1)
- ◻ "Consistent with" vs "supports" the null; Pythagoras and black-swan examples (HW 28; A W10L1-2 p12)
- ◻ GoF with estimated parameters: Thm 8.2 ($k-1-r$ df), village housing (CN §8.2, Ex 8.3, Table 8.1) ↔ STAT1301 Thm 11.2
- ◻ Tests of independence and **homogeneity** (HW 30; A W10L3 p4–7, A W11L1-2 p1); ESP example (CN §8.3, Ex 8.4) ↔ STAT1301 Ex 11.4
- ◻ Operating-system example: expected counts, $\chi^2 = 9.66$ on 4 df, p = 0.047 (HW 31–32; A W10L3 p5–7, A W11L1-2 p1–2)
- ◻ Caveats and rule of thumb (HW 32; A W11L1-2 p3) — rules differ between sources; see errors
- ◻ **Fisher's exact test**: three steps, alternative tables with the same margins (HW 33; A W11L1-2 p3–4)
- ◻ Code: `qchisq`, `pchisq`; Fisher test "R DEMO" (code not supplied)

### Ch 46 Linear models and regression (`ch:linear-models`) — HW for the general linear model; CN for simple linear regression; R L07–L10 supplementary; ↔ STAT1301 Ch 9–10, STAT2003 HW 32
- ◻ Simple linear regression, least squares: father–son heights (Fig 9.1, Table 9.1, regression effect), sales vs advertising (Ex 9.1–9.2, Fig 9.2), other fitting criteria (Rem 9.1), **regression through the origin** (Rem 9.2) (CN §9 intro–9.1) ↔ STAT1301 Def 9.1, Thm 9.1
- ◻ Non-linear relationships: polynomial fits and transformations, melanoma example (CN §9.1.1, Ex 9.3, Figs 9.3–9.5)
- ◻ Regression model with normal errors, Fig 9.6; MLE = LS; Thm 9.1 (unbiasedness, proof); Thm 9.2 (distributions); unbiased $S^2$; Thm 9.3 ($t_{n-2}$); Cor 9.1 CI for $\beta_1$; test $\beta_1=0$; oxygen/heart-rate Ex 9.4 (Table 9.4, Fig 9.7) (CN §9.2–9.2.1) ↔ STAT1301 Thm 9.2
- ◻ Residuals and fitted values; CI for $\beta_0+\beta_1x$; prediction interval (CN §9.2.2–9.2.4, Ex 9.5–9.6) ↔ STAT1301 §9.2
- ◻ Regression via the bivariate normal; simulation (CN §9.3, Ex 9.7)
- ◻ **General linear model** $\vect Y = \mat X\vect\beta+\vect\varepsilon$; design matrix; "linear in the parameters"; polynomial (jump vs height) and BMI examples (HW 45, 51; A W12L1-2 p5–7, A W12L3) ↔ STAT1301 Def 10.1
- ◻ Conditional likelihood given covariates (R L07 p1)
- ◻ Least squares / MLE: normal equations, $\hat{\vect\beta} = (\mat X\T\mat X)^{-1}\mat X\T\vect y$, full column rank (HW 48; R L07 p2 with minimisation proof); $\hat\sigma^2_{\text{MLE}}$ and unbiased $\hat\sigma^2$ (R L07 p3; HW 50)
- ◻ Properties: unbiased, $\Cov\hat{\vect\beta} = \sigma^2(\mat X\T\mat X)^{-1}$, normality (R L07 p3–4 with proofs) ↔ STAT2003 HW 32
- ◻ **QR decomposition** route: RSS, $\hat{\vect\beta} = \mat R^{-1}\vect f$, $\lVert\vect r\rVert^2/\sigma^2\sim\ChiSq{n-p}$, $t$-statistics for $\beta_j$ (R L07 p4–6) ↔ Ch 56–57 (MATH3204 QR)
- ◻ **Gauss–Markov theorem** with proof (R L10 p2)
- ◻ Hat matrix: projection, idempotent, trace $p$, symmetric, $\mat H\mat X = \mat X$; fitted values and residuals, their covariances (R L08 p1–2; HW 48 mentions it, see errors)
- ◻ Diagnostics: standardised residuals, leverage ($2p/n$), influence, Cook's distance ($4/(n-p)$) (R L08 p2–3); studentised residuals and Bonferroni outlier cut-off (R L09 p1–2); residual plots, added-variable and partial-residual plots, interactions (R L09 p2); **collinearity**: condition number, VIFs (R L09 p3); changes of scale (R L09 p4); exercises AC 5–6
- ◻ Transforming the response; log-normal mean and variance; **Box–Cox** with profile likelihood (R L09 p4, R L10 p1); exercise AC 6 Q3
- ◻ **General linear hypothesis $\mat R\vect\beta = \vect 0$**; restriction matrices; universal $F$-test $\frac{(RSS_0-RSS_1)/r}{RSS_1/df_1}\sim F_{r,df_1}$; GLRT derivation; $F$-table (HW 46–50; A W12L3, A W13L1)
- ◻ One-way and two-way ANOVA as linear models: design matrices (HW 45, 47; A W12L1-2 p6, A W12L3) — cross-reference Ch 47
- ◻ Code: `lm`, `influence.measures`-type diagnostics, `boxcox` (AC 5–6 solutions); "R DEMO"s (jump distance, tooth growth) not supplied

### Ch 47 Analysis of variance (`ch:anova`) — HW main; ↔ STAT1301 Ch 8
- ◻ One-way layout and motivation (group-means figure) (HW 34; A W11L1-2 p5, figure; CN §10 intro, Ex 10.1 heart rate, Table 10.1, Fig 10.1) ↔ STAT1301 Def 8.1
- ◻ **Derivation of the $F$-test via the GLRT**: likelihood, MLEs under $H_0$ and $H_1$, $SS_{\text{total}} = SS_{\text{groups}}+SS_{\text{resid}}$, $\Lambda = \exp(-SS_{\text{groups}}/2\sigma^2)$, $\chi^2$ distributions, pooled variance, independence, $F_{J-1,N-J}$, df interpretation (HW 34–37; A W11L1-2 p6–10) — CN Thm 10.1, Cor 10.1 state it without proof ↔ STAT1301 §8.2
- ◻ ANOVA table; movie-genre example (HW 38–39; A W11L3 p1–3; CN Rem 10.1–10.2, Exercise 10.1, corn Ex 10.3)
- ◻ Post-hoc comparisons, Bonferroni correction (HW 40; A W11L3 p3–4); Tukey intervals (CN §10.1.6, Ex 10.6) ↔ STAT1301 §8.5
- ◻ Contrasts: definition, thriller vs horror, $SS_C$ and its $F$-test, corn example (HW 41; A W11L3 p5; CN §10.1.5, Ex 10.4–10.5)
- ◻ Parametrisations: mean, **sum** and **contrast** (R default), family-heights analogy table (HW 41–42; A W11L3 p5–6, A W12L1-2 p1–2)
- ◻ **Two-way ANOVA**: model with interactions, parameter counts, sum and contrast constraints, interpretation of main and interaction effects, test interactions first; tooth growth as a $2\times3$ design (HW 43–44; A W12L1-2 p3–5) ↔ STAT1301 Def 8.2, §8.3
- ◻ Randomised block design: model, Thm 10.2, Cor 10.2, Minitab output, contrasts and Tukey, paired $t$-test as a block design (tyres) (CN §10.2, Ex 10.7–10.9, Rem 10.3–10.5) ↔ STAT1301 §8.4
- ◻ Code: `lm` for ANOVA; "R DEMO" tooth growth (not supplied)

### Ch 48 Generalized linear models (`ch:glms`) — R L11–L12 only; ↔ STAT3500 (primary)
- ◻ Logistic regression: Bernoulli responses, logit link, inverse logit, odds and the $e^{\beta_1}$ interpretation (R L11 p1–2)
- ◻ Likelihood, score, likelihood equations; observed = expected information $\mat X\T\mat W\mat X$ (R L11 p2–3)
- ◻ **IRLS** derivation (R L12 p1)
- ◻ Asymptotic standard errors; predictions and their standard errors (delta method) (R L11 p4)
- ◻ Diagnostics: raw residuals, binned residual plots, leverage $\mat W^{1/2}\mat X(\mat X\T\mat W\mat X)^{-1}\mat X\T\mat W^{1/2}$ (R L11 p5)
- ◻ Retrospective (case–control) sampling changes only the intercept (R L12 p2)
- ◻ Exercises: Challenger O-rings, kyphosis, wells (AC 7 with `glm` code and a binned residual plot)

### Ch 50 Bayesian inference (`ch:bayesian-inference`) — A W7–W8 only; ↔ STAT3500, STAT3001
- ◻ Prior beliefs as Beta distributions (four priors, figures); posterior ∝ likelihood × prior; Beta–binomial updating with the Skittles data (A W7L3 p4–7, A W8L1-2 p1, figures)
- ◻ Credible intervals with `qbeta`; interpretation vs confidence intervals (A W8L1-2 p2–3)
- ◻ Exercise: $\BetaDist(0.5,0.5)$ prior (Tut 8 Ex 2)

### Ch 90 Programming in R (`ch:r-programming`)
- No dedicated R material in STAT2004. R calls used: `qt`, `qchisq`, `pchisq`, `pnorm`, `qpois`, `ppois`, `qbeta`, `rpois`, `rgeom`, `optim`, `lm`, `glm`, `MASS::boxcox`, `read.csv`, `write.table` (see Code below).

---

## Not used / out of scope
- `Cheatsheet.pdf` and `Lab08-State Machines.pdf` are CSSE2010 material (digital logic, AVR assembly), uploaded inside `STAT2004_Ross.zip` by mistake. Not in the book plan.
- Course announcements, assignment references ("A4", "Ass 3"), "R DEMO" placeholders.
- CN references to "Supplement 5" and a missing appendix section.

## Suspected errors in the notes
_Kept in the transcriptions; to be corrected when drafting._

**Handwritten notes (HW)**
1. HW 01: standard error written $\sqrt{p(1-p)/n}$; the computable one is $\sqrt{\hat p(1-\hat p)/n}$.
2. HW 03: last line's denominators are blotted; the bounds are $\bar X\pm t^{(1-\alpha/2)}_{n-1}S/\sqrt n$.
3. HW 05: $z_{\alpha/2}$ used both as the lower quantile and as the positive critical value on one page.
4. HW 06: $T_i(\vect x)$ inside $\Prob$; should be $T_i(\vect X)$.
5. HW 08: "composite" used only for one-sided alternatives (two-sided is composite too).
6. HW 09: "$\max(\bar X)$" should be $\max(\vect X) = X_{(n)}$; two-sided region mixes $c$ and $c_2$.
7. HW 11: example should read $H_1:\mu>0$.
8. HW 15: "most powerful because it does not depend on $\mu_1$" — independence of $\mu_1$ gives *uniformly* most powerful.
9. HW 16: two-sided region drops bars ($X$ for $\bar X$); "approx." where the distribution is exact.
10. HW 17: side note "$\lambda^x/x! = e^x$" means $\sum\lambda^x/x! = e^\lambda$; "large $\sum x_i$ (i.e. increased sample size)" is wrong ($n$ fixed).
11. HW 20: p-value definition incomplete; "prob. of sample is 0.02" should be "probability of a total at least 132".
12. HW 21: quantile superscripts mixed; acceptance region has $\mu_0$ in the middle instead of $\bar X$.
13. HW 23: cross term and a missing square in the SS decomposition.
14. HW 24: "$\mu_0\ne\mu_1$" should be $\mu_1\ne\mu_2$; bars dropped.
15. HW 26: $x_n$ for $x_k$ in the multinomial pmf; $n$ missing from Multinomial$(p_1,\dots,p_k)$.
16. HW 27–28: GLRT statistic written $\Omega$ (clashes with PE's parameter space); df of $-2\log\Omega$ blotted with "$n-1$" beneath, should be $k-1$.
17. HW 32: last term uses 3.60 for 3.66 (total 9.66 correct); rule of thumb mixes thresholds 10 and 5 (CN Rem 8.1: $np_i\ge5$).
18. HW 33 (and A W11L1-2 p4): tables with fixed margins are not equally likely under $H_0$ (hypergeometric probabilities); "simulations of all tables" mixes enumeration and simulation.
19. HW 35: inner sum of the cross term should be $\sum_i(Y_{ji}-\bar Y_{j\cdot})$.
20. HW 39 (and A W11L3 p3): $SS_{\text{groups}}$ computes to 5533.8, not 5466.63 ($F = 1.53$, p = 0.18; conclusion unchanged).
21. A W11L3 p3 (HW 40 same example): post-hoc p-value 0.018 is one-sided; two-sided 0.036 (Bonferroni 0.54).
22. HW 43: interaction written $\gamma_{jk}$ and $\delta_{jk}$.
23. HW 48: derivative missing a factor 2; "hat matrix" given as $(\mat X\T\mat X)^{-1}\mat X\T$ (that maps $\vect y$ to $\hat{\vect\beta}$; $\mat H = \mat X(\mat X\T\mat X)^{-1}\mat X\T$); "$\mat X\T$ has full rank" should be "$\mat X$ has full column rank".

**PE** (details in notes part 3)
24. §1.3 $\ChiSq k$ vs $n$ terms; lower-case data in a distributional statement.
25. §3 water bottle: $\Normal(\mu,0.1)$ then $\Normal(\mu,0.01)$.
26. §3.1 uniform example: MLE is $x_{(n)}$, not $x_{(1)}$; "not bounded" lead-in.
27. §3.2: CRLB proof's Cauchy–Schwarz inequality reversed; observed and expected information share a symbol; condition 4 uses $I$ before defining it.
28. §3.3 proof mixes $\theta$ and $\hat\theta$ when taking expectations; divides by $c'(\theta)$ silently.
29. §4.1: completeness needs "with probability 1"; "not minimal as not complete" is a non sequitur; $T = X_n+\sum_{j<n}X_j$ (no $1/(n-1)$).
30. §4.2: bracket in the tower property; equality condition is "iff"; completeness used silently in Lehmann–Scheffé.
31. §5.1 proof's integration region; §5.2 "methods for computing estimators" should be "comparing".

**CN**
32. §2.5.5: gamma $\lambda$ called "scale" (it is the rate). Fig 2.3 "p.d.f." for a pmf. Ch 2 title.
33. Thm 3.9: $Z_1,\dots,Z_n$ vs $(Z_1,\dots,Z_p)$.
34. Ex 10.4: text says variety 5, hypothesis is about variety 3.

**Later-iteration lectures**
35. R L07 p5: $\Cov(\mat Q\T\vect Y)$ written $\mat Q\Cov(\vect Y)\mat Q\T$ (value unchanged).
36. A W7L3 p4: prior labelled "around 70–70" for $\BetaDist(3,7)$ (mean 0.3).
37. A W9L1-2 p5: "approx" for exact normal/$t$ distributions.
38. A W10L1-2 p9: Pearson's statistic described as the "first-order" Taylor term of $-2\log\Lambda$ (it is the leading, second-order term).
39. A W10L3 p7: expected counts from rounded proportions (12.42 vs 12.51); corrected in A W11L1-2 p2.
40. A W11L1-2 p3: rule of thumb "80% of cells ≥ 10, all ≥ 5" differs from HW 32 and CN Rem 8.1.

## Notation the book doesn't have yet
| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\tdist{m}` | $t_m$ | Student $t$ with $m$ df | Used throughout Ch 39, 43–47; parallels `\ChiSq` |
| `\Fdist{m_1}{m_2}` | $F_{m_1,m_2}$ | $F$-distribution | ANOVA, variance ratio, linear-model $F$-test |
| `\quant{q}{\alpha}` or a fixed convention | e.g. $z_{1-\alpha/2}$, $t_{n-1;1-\alpha/2}$, $\chi^2_{m;\alpha}$ | quantile of order $\alpha$ | Sources use four conventions: $z_{\alpha/2}$ (HW 01, 05), $z^{(1-\alpha)}$, $t^{(1-\alpha/2)}_{(n-1)}$ (HW, A), $t_{n-2;1-\alpha/2}$, $\chi^2_{m;\alpha}$ (CN); needs one book-wide rule |
| `\lik`, `\loglik` | $L(\theta)$ or $\mathcal L(\theta)$; $\ell(\theta)$ | likelihood, log-likelihood | PE uses $L$, R L uses $\mathcal L$, $\ell$; HW uses $L(\theta\given\vect x)$; Ch 40–42, 44–48 |
| `\score` | $U(\theta)$ (or $S$) | score function | PE writes $S(\vect x;\theta)$, R L writes $U$ |
| `\Info`, `\info`, `\ObsInfo` | $I(\theta)$, $i(\theta)$, $J(\theta)$ | expected (Fisher) information, per-observation information, observed information | PE uses $I$ for both expected and observed; needs distinct symbols |
| `\ParSpace` | $\Theta$ | parameter space | PE uses $\Omega$, which clashes with the sample space $\Omega$ in Part III; R L, A and CN use $\Theta$ |
| `\approxdist` | $\overset{\text{approx}}{\sim}$ or $\mathrel{\dot\sim}$ | approximately distributed as | HW "app. ~", A "approx ~"; used for CLT-based pivots, $\chi^2$ GoF, MLE asymptotics |
| `\LR` / `\GLR` | $\Lambda$ | (generalised) likelihood ratio statistic | HW writes $\Omega$ (clash), A writes $\Lambda$ |
| `\SS`, `\MS`, `\RSS` (operators) | $\mathrm{SS}_{\text{groups}}$, $\mathrm{MS}$, $\mathrm{RSS}$ | sums of squares, mean squares, residual SS | Ch 46–47; consistent upright subscripted names |
| `\hatmat` | $\mat H$ | hat (influence) matrix | Ch 46, 48; to keep $\mat H$ reserved |
| `\logit` (operator) | $\operatorname{logit}$ | log-odds | Ch 48 |
| `\Tbar`-style dot notation | $\bar Y_{j\cdot}$, $\bar Y_{\cdot\cdot}$ | group and grand means | Confirm the dot convention (`\cdot`) book-wide for Ch 45–47 |
| `\IG` | $\mathrm{IG}(\mu,\lambda)$ | inverse Gaussian | Only in AC 4 Q5; low priority |
| `\ZIP` | $\mathrm{ZIP}(\pi,\lambda)$ | zero-inflated Poisson | R L01, AC 3–4; optional |

Also check: `\NegBin` in the book counts trials until the $k$-th success, but AC 2 Q5 uses the failures parametrisation on $\{0,1,2,\dots\}$; `\Geom` support $\{1,2,\dots\}$ matches AC 3–4.

## Code in the notes
| Where | Language | What it does |
|---|---|---|
| HW 17, 20; A W9L1-2 p8, p11 | R | `qpois(0.95, 109.5)`, `1 - ppois(127, 109.5)`, `1 - ppois(131, 109.5)`: Poisson LRT cut-off, size and p-value |
| A W7L1-2 p7, p9 | R | `qt(0.985, 41)`; `qchisq(0.025, 24)`, `qchisq(0.975, 24)`: CI quantiles |
| A W8L1-2 p2 | R | `qbeta(0.025, 25, 26)` etc.: credible intervals |
| A W8L1-2 p9–10, W8L3 | R | `1 - pnorm(1.417)` etc.: Type I error and power |
| A W10L3 p1; A W11L1-2 p2 | R | `qchisq(0.95, 3)`; `1 - pchisq(9.66, 4)` |
| A W8L3 p4, W11L1-2 p4, W12L1-2 p3, p5, W12L3, W13L1; HW 43–44, 51 | R (not supplied) | "R DEMO": power curve; Fisher's exact test; tooth growth one- and two-way ANOVA with `lm`; jump-distance polynomial models |
| AC 2 Q4 (solution) | R | Simulation study of the geometric MoM estimator ($B = 10\,000$; uses `rgeom` + 1) |
| AC 3 Q5, AC 4 Q4 (solutions) | R | ZIP log-likelihood, `optim`, Hessian-based standard errors on `fish.csv` |
| AC 5 Q4, AC 6 Q3–4 (solutions) | R | `lm` on `faraway::sat` and `trees`; Cook's distance, leverage, studentised residuals, VIFs; `MASS::boxcox` |
| AC 7 (solution) | R | `glm(..., family = binomial)` for Challenger, kyphosis, wells; `vcov`; binned residual plots |
| Tut 9 Ex 1 | R | `rpois`, `write.table`, `read.csv`, `qt`: $t$-interval for Poisson data and a 1000-sample coverage simulation |
| CN Ex 10.3, 10.8 | Minitab output | ANOVA tables (no code) |
