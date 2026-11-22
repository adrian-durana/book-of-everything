# STAT3001 Mathematical Statistics: transcription, part 3 of 3 (typed notes, slides, diary)

_Continuation of `claude/notes-stat3001-1.md` (sources and conventions are there). Semester 1, 2026. No dates: the lecture diary's dates and the years in the typed notes' citations are not reproduced._

Typed notes are **not retyped**. For each file: a section/page index, what in it is **not in the handwritten notes** (HW), and a description of every figure detailed enough to redraw. The two guest-lecture slide decks carry the lecturer's **handwritten annotations**, which appear nowhere else; those are transcribed. "↔ HW nn" = the handwritten page that covers the same material.

---

## 1. Scope guide: lecture diary (LD, 6 pp.)

Order of topics (dates omitted): revision of STAT2004 point estimation (BN) → multivariate normal, linear transformations, distribution of $s^2$ (LN1) → ML for univariate and multivariate normal, via direct optimisation and via the regular exponential family (LN2) → **guest lectures: Bayesian estimation, MCMC (S1, S2)** → review of sufficiency, Fisher–Neyman, completeness, minimal sufficiency, CRLB, UMVU, Rao–Blackwell → unbiased estimator of a p.f./p.d.f. at a point (LN9) → regular exponential family and ML (LN3) → observed = estimated Fisher information (LN3); MVN in the REF (LN4) → multivariate CRLB (LN5) → Jensen, KL (LN6); R–B for convex loss (LN7) → Basu (LN8) → theorems underlying ML (LN8) and large-sample theory (BN) → EM: introduction, two-component normal mixture with known common variance, monotonicity proof, mixture fitting, unbounded likelihood for unequal covariance matrices (LN10, LN11) → EM for grouped and truncated data (LN12, LN13) → hypothesis testing (LN14): LRT, **Wald, Wilks and Rao** approaches, $\chi^2$ GoF derivation and df adjustment for estimated parameters → multiple testing, FWER, FDR, BH (LN15, LN16) → errors in testing, PPV, fallacy of the transposed conditional (LN17) → information criteria (LN18 §6.8); **BIC via Laplace's method (LN18 §6.9.2) is stated in LD to be not examinable** → LRT worked examples for means and variances of two classes (LN19, LN19a, LN20) → Satterthwaite (LN21) → Tukey's studentised range (LN22) → bootstrap (LN23), bootstrapping the LRTS for the number of mixture components (LN18 §6.6), bootstrap bias of a classifier's error rate (LN24), bootstrap for regression → **Bayesian statistics from Wasserman, *All of Statistics*, Ch 11 (LN25 — not uploaded)** → review. LN11 (ECM/ECME) is non-examinable per HW 37.

**Content mentioned in LD but in no uploaded source:** the two-component normal mixture EM example and the general mixture-model EM (LD Lectures 16, 18–19; only LN18 touches mixtures), the unbounded mixture likelihood, the df adjustment of the $\chi^2$ GoF statistic for estimated parameters, the bootstrap for regression models, and LN25 (Bayesian statistics). Ask the user whether LN25 exists.

---

## 2. Background Notes on Point Estimation (BN, file `STAT2004 notes.pdf`, 36 pp.)

| Pages | Content | ↔ HW |
|---|---|---|
| 1–2 | Setting: p.f./p.d.f. $f(x;\theta)$, $\theta\in\Omega$; univariate/multivariate; nonparametric index example (normal vs Cauchy); nuisance parameters; $\operatorname{var}(\bar X)$, S.D., S.E.; $\hat\sigma^2$ vs $s^2$; i.i.d. sample | — |
| 2–3 | Closeness of an estimator; **loss function** $\ell(\theta,T)$; risk; no uniformly best estimator (constant-estimator argument); unbiasedness; **median unbiasedness**; bias | HW 23 (loss/risk only) |
| 3–5 | Location estimation: $X_1$ vs $\bar X$; minimising $\sum\abs{x_j-\theta}^a$: $a=2$ mean, $a=1$ sample median ($q_{0.5}$ via order statistics) | — |
| 5–8 | **Method of moments**; Pearson's crab data and two-component normal mixture (Fig 1, p. 8) | — |
| 8–13 | Likelihood function; score $S(\vect x;\theta)$; Fisher (expected) information $\mathcal I(\theta)$; $\E S = 0$ (proof); $\mathcal I = -\E[\partial^2\log L/\partial\theta^2]$; observed information $I(\hat\theta)$; per-observation information $i(\theta)$; regularity conditions; **CRLB with proof** (pp. 10–12, Cauchy–Schwarz) | HW 13–15 |
| 13 | Information for parameter vectors (score vector, information matrix) | HW 16 |
| 14–17 | Maximum likelihood (Fisher); **non-regular example: $\Unif[0,\theta]$**, $L(\theta) = \theta^{-n}I_{[x_{(n)},\infty)}(\theta)$ (p. 15), Fig 2 (p. 16); Fig 3 normal log-likelihood surface (p. 17) | — |
| 18–21 | Regular exponential family; likelihood equation $T = \E_{\hat\theta}T$ (proof); **MVB estimators: attained iff $\partial\log L/\partial\theta = A(\theta)\{T - g(\theta)\}$**, which forces the one-parameter exponential family (pp. 20–21) | HW 06–08, 16 (MVB def only) |
| 22–27 | Sufficiency; $T = H(U)$; minimal sufficiency; completeness ("except perhaps on a set of probability zero"); REF statistic complete; complete ⇒ minimal; **Fisher–Neyman factorisation**; examples: normal $(\bar x, s^2)$ (pp. 24–26), $\Unif[0,\theta]$: $X_{(n)}$ sufficient (p. 26), Bernoulli $\bar X$ (p. 27) | HW 18 (no examples) |
| 28–29 | Rao–Blackwell (Theorem 1, proof); Lehmann–Scheffé (Theorem 2, proof) | HW 19–20 |
| 30–33 | Large-sample theory; consistency (proof via $\MSE/\varepsilon^2$); **example: $\hat\sigma^2$ and $s^2$ consistent** (pp. 32–33) | HW 26 |
| 33–34 | ARE; mean vs median for normal data, $2/\pi$; $\phi(z)$ defined | HW 27 |
| 34–36 | Asymptotic efficiency, asymptotic CRLB with $i(\theta)$; note that asymptotic efficiency does not need unbiasedness; regularity conditions (i)–(v) (p. 36) | HW 28 |

**Figures (BN):**
- **Fig 1 (p. 8)** "Plot of forehead to body length data on 1000 crabs and of the fitted one-component (dashed line) and two-component (solid line) normal mixture models." Histogram of narrow bars over roughly $0.58$–$0.70$ on the horizontal axis (ratio), vertical axis frequency $0$–$100$ (ticks every 10); bars rise from near 0 at the left to a peak of about 95 slightly right of centre and fall faster on the right (left-skewed). Overlaid: a dashed symmetric normal curve peaking at about 85, centred slightly left of the bar peak; a solid curve (two-component mixture) peaking higher (about 90) and further right, with a heavier left shoulder. Data values are not given in the notes, so the bars cannot be reproduced exactly; a redraw needs simulated data or a schematic.
- **Fig 2 (p. 16)** "Likelihood function for the uniform distribution on the interval $[0,\theta]$." Horizontal axis $\theta$ from 0 to 6 (ticks at integers), $x_{(n)}$ marked at 2 by a vertical dashed line; vertical axis $L(\theta)$ from 0 to about $1\times10^{-3}$ (ticks labelled 0e+00, 2e−04, 4e−04, 6e−04, 8e−04). $L = 0$ for $\theta < 2$; a jump at $\theta = 2$ to the maximum (about $1\times10^{-3}$), then a steep convex decay $\theta^{-n}$ to nearly 0 by $\theta \approx 3.5$. ($n$ is not stated; the height $2^{-n}\approx 10^{-3}$ suggests $n = 10$.)
- **Fig 3 (p. 17)** "Log likelihood function for a $N(\mu,\sigma^2)$ distribution." Title "Plot of the Log-Likelihood Function". 3-D wireframe surface: axes "Mu" ($-0.2$ to $0.2$), "Sigma^2" ($0.8$ to $1.6$), vertical "Log-Likelihood" ($-1510$ to $-1440$). A smooth dome with its maximum near $\mu = 0$, $\sigma^2 \approx 1.1$–$1.2$, falling off more steeply towards small $\sigma^2$. Sample data not given; a redraw can use the normal log-likelihood formula with a chosen $n$ and summary statistics.

---

## 3. Lecture notes LN1–LN24

| File | pp. | Content (page) | ↔ HW | Only in LN |
|---|---|---|---|---|
| **LN1** Some standard multivariate results | 6 | $\vect X\sim(\vect\mu,\mat\Sigma)$, $\mat\Sigma$ p.d. symmetric (1); MVN density; subvector marginal and conditional results (2); **example $X_i \given \bar x$** (2–3); "LN4 from STAT2004": distribution of $s^2$ with **Helmert-type orthogonal matrix $\mat B$**, independence from $\bar X$, zero means of $Y_1..Y_{n-1}$ shown (4–6) | HW 01–04 | MGF proof that $\mat C\vect X$ is normal (2); proof that $\E Y_i = 0$ for $i<n$ (6) |
| **LN2** ML for normal distribution | 4 | Likelihood for MVN sample, $d = p + \tfrac12p(p+1)$ (1); univariate normal in REF, $\vect c$, $\vect T$, $a(\vect\theta)$, $b = 1$ (2); ML via $\E T = T$ (2–3); MVN canonical parameter (3) | HW 05, 09–10 | Direct-differentiation check is referred to Tutorial Sheet 1 (not uploaded) |
| **LN3** Likelihood equation: REF | 5 | $d$-parameter exponential family (1); regular: $q = d$, Jacobian full rank (1); $\E\{\partial\log L/\partial\vect\theta\} = \vect 0$ proof (1–2); likelihood equation $T = \E_{\hat\theta}T$ with proof (2–3); **observed information = estimated Fisher information** (3–4) | HW 06–08, 13 | Regularity definition (HW omits it) |
| **LN4** MVN belongs to REF | 3 | Derivation via trace (1–2); vec notation (3) | HW 10–12 | LN4 stacks **rows** for vec; HW 12 stacks **columns** (see errors) |
| **LN5** CRLB for multiparameters | 5 | Multivariate CRLB, $\vect g'(\vect\theta)$ (1); normal, known mean: $\hat\sigma^2$ attains MVB (1–2); unknown mean: $(\bar X, s^2)$ does not (3–4); **covariance of the MLE $(\bar X,\hat\sigma^2)$ vs bound; $\Var\hat\sigma^2 = 2(n-1)\sigma^4/n^2 < 2\sigma^4/(n-1)$** (4–5) | HW 16–17 | MLE comparison (4–5) |
| **LN6** Jensen, KL | 3 | Jensen (1); convex examples $x^2$, $-\log x$ (2); KL distance, non-negativity proof (2–3) | HW 21–22 | — |
| **LN7** R–B for convex loss | 3 | CRLB for MSE of a biased estimator (1–2); R–B with possibly biased $U$ (2); theorem and proof for convex loss (3) | HW 16, 23–24 | — |
| **LN8** More on point estimation | 15 | **Basu's theorem**, example: $\sum(X_j-\bar X)^2$ independent of $\bar X$ (1); proof (1–2); Theorems 3–5 basis for ML: $\Prob[L(\theta_0)>L(\theta)]\to1$ (3–4), consistent root (4–5), asymptotic normality/efficiency with **Regularity Conditions (II)** and proof outline (5–8); Theorem 6 (Slutsky-type, no proof), **Theorem 7** (delta method form) (9–10); ML under incorrect model (11–12); **computation of ML estimates via Newton–Raphson, Fisher scoring, quasi-Newton** (12–15) | HW 25, 29–33 | Basu example (1); Theorem 5 proof outline (6–8); **Newton-type methods (12–15)** |
| **LN9** Estimation of a p.d.f. | 3 | Unbiased estimator of $f(x;\theta)$: conditional p.f. of $X_1$ given sufficient $T$; UMVU if $T$ complete (1); **example: UMVU estimator of the normal density with known variance, $\phi(x;\bar x,(1-1/n)\sigma^2)$** (1–3) | (HW 03 covers the conditional distribution only) | Whole note |
| **LN10** Intro to EM | 10 | EM background, incomplete data (1–3); formulation, E- and M-steps (4–5); REF case (5–6); monotonicity (7–8); self-consistency (8); GEM monotonicity (8); convergence to a stationary value, saddle points, Wu's condition (34) and regularity conditions (35)–(39) (8–10) | HW 34–39 | Closedness of point-to-set maps; differential form $\partial\log L/\partial\Psi = \partial Q/\partial\Psi$ at $\Psi^{(k)}$ (9) |
| **LN11** Extensions of EM | 3 | ECM (Meng–Rubin), formal definition with $S$ CM-steps; ECME (1–3) | HW 37 (mention only) | Whole note; **non-examinable** per HW 37 |
| **LN12** EM for grouped and truncated data | 6 | Setup, multinomial likelihood (1); missing data $\vect u$, $\vect w_j$ (1–2); $d(\vect u\given\vect y)$, $c_2$; negative binomial when $r = v-1$ (2); E-step (3); M-step (3); normal M-step (4); **numerical example: grouped log-normal red blood cell volume data, Table 1 (MLE exact vs midpoint approximation for a two-component mixture), Table 2 (doubly truncated data, observed vs expected)** (4–6) | HW 40–41 | Numerical example and tables (4–6) |
| **LN13** Truncated r.v. | 2 | Truncated p.d.f./p.f. (1); proof, discrete case "carries over" (1); conditional expectation (1); link to the E-step of grouped data (1–2) | HW 42 | E-step link (1–2) |
| **LN14** Introduction to hypothesis testing | 18 | p-value definition; Type I/II, power; NP lemma with proof (1–3); normal-mean MP test (3–4); composite alternatives, **UMP** (4–5); **no UMP for two-sided; unbiased tests, UMPU test $\abs{\bar x-\theta_0}>k$** with **power-function figure** (5–6); GLRT, Wilks (6–7); $t$-test examples two- and one-sided (7–11); derivation of the restricted MLE at the boundary (11); Wilks proof, scalar case (12); **Wald, Wilks and Rao (score) tests** (13–14); $\chi^2$ GoF with MLE derivation via Lagrange-free argument (15–17); **Simpson's paradox: kidney-stone data** (18) | HW 43–49 | UMPU and figure (5–6); Wald/score tests (13–14); MLE of multinomial derivation (16); Simpson's paradox (18) |
| **LN15** Bonferroni (slide) | 1 | Bonferroni's method, FWER $\le\sum\Prob(A_i)$; slide "Methods for dealing with the multiplicity problem" | HW 50 | — |
| **LN16** Testing $N$ hypotheses | 5 | Slide: FDR table, FDR $\sim b/N_r$, FNDR $\sim c/(a+c)$ (1); notation $N, N_0, N_1, N_r, a,b,c,d$ (2); FWER $=\Prob(b\ge1)$; **FDP $:= 0$ when $N_r = 0$**; FDR; two properties (3); FDR conditional form (4); BH procedure (4); FDR-corrected and FDR-adjusted values (Yekutieli–Benjamini) with **worked table of 25 tests, eight smallest P-values** (5) | HW 50–52 | FNDR (1); FDP convention (3); worked table (5) |
| **LN17** Errors in testing | 5 | **Example 1: cancer test 95% accurate, prevalence 0.005, Bayes** (1); Example 2: PPV, sensitivity, specificity, prior odds $R$ (2–3); **PPV numbers: $1-\beta = 1-\alpha = 0.99$, $R = 10^{-3}$ gives 0.09; $R = 10^{-2}$ gives 0.497** (4); series of independent positive tests: PPV → 1 unless $1-\beta<\alpha$; Ioannidis and Jager–Leek discussion (5) | HW 53 | Example 1; numerical PPVs; repeated tests (4–5) |
| **LN18** Assessing the number of components in mixture models (book ch. 6, pp. 175–220) | 46 | §6.1 introduction, order of a mixture, Ex 6.1 skewness adjustment (1–4); §6.2 Hidalgo stamp example (5–9); §6.3 approaches (10–11); §6.4 LRTS, breakdown of regularity, Ex 6.3 (11–12); §6.5 distributional results, simulations (13–17); **§6.6 bootstrapping the LRTS**: implementation, three real data sets, astronomy (18–23); §6.7 effect of estimates on P-values, double bootstrap (24–28); **§6.8 information criteria: bias correction of the log likelihood, AIC, bootstrap-based (EIC), cross-validation, MIR, ICOMP** (28–33); §6.9 Bayesian criteria: Bayes factors, **Laplace's method (not examinable)**, BIC, Laplace–empirical, reversible jump, MML (33–38); §6.10 classification-based criteria CLC, NEC, ICL (38–41); §6.11 empirical comparison (43–46) | — | Whole note. LD: §6.6 and §6.8 covered; §6.9.2 BIC derivation not examinable |
| **LN19** Two-sample $t$-test | 5 | Setup, $\Omega$, $\Omega_{H_0}$ (1–2); MLEs (2); $\lambda$ (3); SS decomposition (4); $\lambda = (1+w^2/(n-2))^{-n/2}$ (5) | HW 54 | Full algebra (3–5) |
| **LN19a** Tests on the variance of one normal population | 7 | (i) MP test of $\sigma_0^2$ vs $\sigma_1^2$, $\mu$ known (1–2); (ii) UMP one-sided (3); (iii) CI for $\sigma^2$ (3); $\mu$ unknown: $\ChiSq{n-1}$ pivot (3–4); (iv) two-sided equal-tails test (4–5); **(v) LRT with $\mu$ unknown: $k_1,k_2$ with $\lambda(k_1)=\lambda(k_2)$, differs from equal tails** (5–6); one-sided LRT agrees with (10) (6–7) | — | **Whole note** |
| **LN20** Tests for homoscedasticity (two classes) | 4 | CI for $\sigma_1^2/\sigma_2^2$ via $F$ (1–2); $F$-test by CI inversion (2); LRT for $\sigma_1^2 = \sigma_2^2$ (2–3); generalisation to $g$ classes and multivariate (**$-2\log\lambda = \sum n_i\log(\abs{\hat{\mat\Sigma}_i}/\abs{\hat{\mat\Sigma}})$**), sensitivity to non-normality (4) | — | **Whole note** |
| **LN21** Satterthwaite's approximation | 2 | $W = \sum a_iW_i$, $\nu$ (1); Welch $t$ (1); derivation (2) | HW 55 | — |
| **LN22** Tukey's studentised range | 6 | Definition (1); simultaneous CIs (1–2); **linear contrasts $\psi = \sum c_i\theta_i$, $\sum c_i = 0$, with $h = \tfrac12\sum\abs{c_i}$, proof** (2–3); **Montgomery Example 3.7: one-way ANOVA, $g=4$, $n=5$, $s^2 = 333.70$, $\nu = 16$** (4); unequal sample sizes (Tukey–Kramer, conservative) (5) | HW 56 | Contrasts, example, unequal $n_i$ (2–5) |
| **LN23** A note on the bootstrap | 3 | Idea; Monte Carlo with known $F$, estimate (1); nonparametric bootstrap from $F_n$, estimate (2); parametric bootstrap $F_{\hat\theta}$ (2); pointer to LN18 §6.6 (3) | — | **Whole note** |
| **LN24** Journal article: Efron's bootstrap approach applied to the error rate of a linear discriminant function (8 pp., scanned) | 8 | Apparent error rate and its bias; bootstrap bias correction; simulation **Tables I–III** comparing bootstrap and parametric corrections for two normal populations | — | **Whole note** (an application; LD: example of bootstrapping the bias of a classifier's error rate) |

**Figures in the LN files:**
- **LN14 p. 6, power functions (no caption).** Horizontal axis $\theta$ with $\theta_0$ marked at the centre; vertical axis labelled "Power function $\Pi(\theta)$" with the value 1 marked by a horizontal dashed line at the top, and $\alpha$ marked on the vertical axis just above the crossing point. Three curves: (a) solid green rising S-curve from 0 (far left) through $\alpha$ at $\theta_0$ to 1 (far right): the one-sided UMP test for $\theta>\theta_0$; (b) its mirror image, solid green falling from 1 to 0 through $\alpha$ at $\theta_0$: the one-sided test for $\theta<\theta_0$; (c) red dash-dotted U-shaped curve with minimum $\alpha$ at $\theta_0$, rising to 1 on both sides, lying below each green curve on that curve's own side; labelled "UMPU test" with an arrow. All three pass through $(\theta_0,\alpha)$. Message: each one-sided test beats the two-sided test on its side and is poor on the other, so no UMP test exists; the UMPU test has power $\ge\alpha$ everywhere.
- **LN14 p. 10, $\lambda(t)$ (no caption).** Horizontal axis $t$ with the vertical axis at $t = 0$; curve labelled $\lambda(t)$: constant at height 1 for $t\le0$ (a horizontal line from the left edge to the axis), then decreasing convexly for $t>0$ towards 0. A dotted horizontal line at height $c$ meets the curve at $t = c^*$, with a dotted vertical drop to the $t$-axis labelled $c^*$. Message: $\lambda < c \iff t > c^*$ for the one-sided $t$-test.
- **LN16 p. 1 (slide), FDR table.** A 2×2 table: rows "TRUE" Null / Non-null, columns "PREDICTED" Retain Null / Reject Null; entries $a$, $b$ (false positive, green), $c$ (false negative, red), $d$; column total under "Reject Null" $N_r$. Below: a cyan box "FDR $\sim b/N_r$" and text "FNDR $\sim c/(a+c)$".
- **LN16 p. 2 (slide)** "Methods for dealing with the Multiplicity Problem": bullet text only (Bonferroni controls FWER, "too strict for typical data sets"; FDR "good for gene expression data").
- **LN18 figures (book plots; underlying data are not in the notes):** Fig 6.1 and 6.2 (p. 4), each a pair: kernel density estimate of a transformed variable (smooth curve with a main mode and a small right bump) and a normal Q–Q plot (points against a straight line, curving away at the ends); Fig 6.3–6.4 (p. 6) and 6.5–6.6 (p. 9): histograms of the Hidalgo stamp thickness data (many narrow bars between about 0.06 and 0.13 mm, several modes) with fitted $g$-component normal mixture densities overlaid ($g = 7, 3$ unrestricted variances; $g = 7, 8$ equal variances); Fig 6.7 (p. 21): three stacked histograms with fitted mixture densities, "acidity data set", "enzyme data set", "galaxy data set"; Fig 6.8 (p. 23): six panels of adaptive-kernel density contour maps of galaxy positions (X and Y in arcmin, about $-40$ to $40$), filled circles for galaxy positions, crosses for mixture-component centres, a scale bar in each panel; Fig 6.9–6.10 (pp. 26–27): line plots of the inverse of the bootstrap estimate of the null distribution of $-2\log\lambda$ (vertical axis) against percentile (horizontal, 0–100), three increasing convex curves ("True", "First Layer", "Second Layer" in solid, dashed, dotted). These are illustrations of an applied case study; redrawing them exactly is not possible without the data.
- **LN24:** journal header images and scanned page images only; Tables I–III are numeric (no plots).
- LN12 Tables 1–2 are numeric tables (reproducible as tables).

---

## 4. Guest lecture 4: Introduction to Bayesian Estimation (S1, 13 slides)

Typed slide text is indexed; the lecturer's **handwritten annotations** (red/green ink on the slides) are transcribed in brackets «…» because they appear nowhere else. Slide numbers are in file order.

**S1.1** Title: STAT3001 Mathematical Statistics, Lecture 4: Introduction to Bayesian Estimation, Semester 1, 2026.

**S1.2 Recap of Estimation.** Typed: MLEs have many desirable properties (under regularity conditions): asymptotically consistent, asymptotically efficient, asymptotically unbiased, asymptotically normal, invariant under transformation of the data, invariant under transformation of the parameter; method of moments estimators; Bayesian estimators.
Annotations: «$x_1, x_2,\dots,x_n \sim f(x;\theta)$», «$\hat\theta = \argmax_\theta f(x;\theta)$»; beside the properties: «$\hat\theta_n \xrightarrow{P} \theta$», «achieves MVB», «$\lim_{n\to\infty}\E(\hat\theta) = \theta$», «$\hat\theta_n \xrightarrow{d} \Normal\bigl(\theta, \frac{1}{\mathcal I(\theta)}\bigr)$». ["Asymptotically unbiased" is underlined.]

**S1.3 Frequentist vs Bayesian approaches.** Typed: Frequentist treats $\theta$ as fixed, estimates $\theta$ based on observed data $\vect x$ only; Bayesian treats $\theta$ as random, makes inference based on the posterior distribution.
*Figure:* two small handwritten flow sketches under a vertical divider. Left (frequentist): «data» with a down arrow to «model». Right (Bayesian): «prior» and «data» side by side, each with an arrow converging on «Model».

**S1.4 Bayesian Estimation.** «Let $x$ be the data and $\theta$ be the parameter of interest.» It has 3 steps:
1. Prior: «Specify our prior belief about $\theta$, using the prior distribution $f(\theta)$.»
2. Data: «Specify the model (likelihood) that characterise how the distribution of $x$ depends on $\theta$. $f(x\given\theta)$»
3. Posterior: «The posterior distribution is given by the Bayes' rule: $f(\theta\given x) = \dfrac{f(x,\theta)}{f(x)} = \dfrac{f(x\given\theta)f(\theta)}{f(x)} \propto \underbrace{f(x\given\theta)}_{\text{likelihood}}\underbrace{f(\theta)}_{\text{prior}}$» [$f(\theta\given x)$ labelled «posterior».]

**S1.5 Coin tosses.** Typed: a coin is tossed $n = 10$ times and we observed $s =$ «3» heads. What do you think about the probability $\theta$ of heads?
«MLE: $\hat\theta = s/n = 3/10 = 0.3$»
1. Prior: «Specify a prior belief about $\theta$: E.g.»
*Figure (three hand-drawn priors on $[0,1]$, side by side):* (a) a peaked, symmetric hump centred at 0.5 with a dashed vertical line at 0.5, axis ticks 0, 0.5, 1, caption «most likely around 0.5, but not exactly sure»; (b) a flat horizontal line over $[0,1]$, boxed in yellow highlighter, caption «no opinion about $\theta$», «$f(\theta) = 1$ for $\theta\in[0,1]$»; (c) a U-shaped curve high at 0 and 1 and low at 0.5, caption «suspect coin is biased».

**S1.6 (continued).**
2. Data: «$f(x\given\theta) = \binom{10}{x}\theta^x(1-\theta)^{10-x}$, $X\given\theta \sim \Bin(n=10, p=\theta)$»
3. Posterior [numbered "2)" on the slide with a "3" written over it]:
«$f(\theta\given x) \propto f(x\given\theta)f(\theta) \propto \binom{10}{x}\theta^x(1-\theta)^{10-x}\times 1 \propto \theta^x(1-\theta)^{10-x} \sim \BetaDist(x+1, 11-x)$»
Side note (green): «$Y\sim\BetaDist(\alpha,\beta)$: $f(y)\propto y^{\alpha-1}(1-y)^{\beta-1}$, $\E(Y) = \frac{\alpha}{\alpha+\beta}$»
«$\E(\theta\given x) = \frac{x+1}{x+1+11-x} = \frac{x+1}{12}$» labelled «posterior mean»; «$x = 3$: $\E(\theta\given x) = 4/12 = 1/3$»; «MLE: $\hat\theta = 3/10 = 0.3$».
Typed: "What does our posterior distribution looks like?"; "Examples of numerical summaries about our posterior belief: posterior mode, posterior mean."

**S1.7 The Beta-Binomial Model.** Typed: tossing a coin $n$ times and observing $s$ heads.
1. Prior: $\theta\sim\BetaDist(\alpha,\beta)$. *Figure:* two hand-drawn symmetric humps on $[0,1]$ centred at 0.5 (dashed vertical line, tick «0.5»): a tall narrow one labelled «Beta(30,30)» and a lower wider one labelled «Beta(3,3)»; note «larger values of $\alpha,\beta$ ⇒ higher confidence». «$f(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$, $\E(\theta) = \frac{\alpha}{\alpha+\beta}$»
2. Data: «$f(x\given\theta) = \binom nx\theta^x(1-\theta)^{n-x}$»
3. Posterior: «$f(\theta\given x)\propto f(x\given\theta)f(\theta) \propto \binom nx\theta^x(1-\theta)^{n-x}\theta^{\alpha-1}(1-\theta)^{\beta-1} \propto \theta^{x+\alpha-1}(1-\theta)^{n+\beta-x-1} \sim \BetaDist(x+\alpha, n+\beta-x)$»; «posterior mean $\E(\theta\given x) = \frac{x+\alpha}{x+\alpha+n+\beta-x} = \frac{x+\alpha}{\alpha+\beta+n}$» [the binomial coefficient is struck through in the third line, being a constant]. Typed: "What does the posterior distribution looks lie?" [sic]

**S1.8 Bayesian Point Estimators.** Typed list with annotations: posterior mean «$\E(\theta\given x)$»; posterior mode «$\argmax_\theta f(\theta\given x)$»; posterior median «$\tilde\theta$ such that $\Prob(\theta\le\tilde\theta\given x) = \tfrac12$»; posterior variance (no annotation).

**S1.9 Interpretation of Hyperparameters.** Typed: $\theta\sim\BetaDist(\alpha,\beta)$; prior mean $\E(\theta) = \alpha/(\alpha+\beta)$; posterior mean $\E(\theta\given\vect x) = (\alpha+x)/(\alpha+\beta+n)$ [circled]; «$\hat\theta = x/n$». "What is the effect of the prior on the posterior mean like?" «It's like observing $\alpha$ successes and $\beta$ failures prior to our observed data.»

**S1.10 Relationship with MLE.** Typed: the posterior mean can be rewritten as $\E(\theta\given\vect x) = \frac{\alpha+x}{\alpha+\beta+n}$. Annotations:
«$= \frac{\alpha}{\alpha+\beta+n} + \frac{x}{\alpha+\beta+n} = \frac{\alpha}{\alpha+\beta+n}\Bigl(\frac{\alpha+\beta}{\alpha+\beta}\Bigr) + \frac{x}{\alpha+\beta+n}\Bigl(\frac nn\Bigr) = \underbrace{\Bigl(\frac{\alpha+\beta}{\alpha+\beta+n}\Bigr)}_{w}\underbrace{\Bigl(\frac{\alpha}{\alpha+\beta}\Bigr)}_{\E(\theta)} + \underbrace{\Bigl(1 - \frac{\alpha+\beta}{\alpha+\beta+n}\Bigr)}_{1-w}\underbrace{\Bigl(\frac xn\Bigr)}_{\hat\theta} = w\,\E(\theta) + (1-w)\hat\theta$»
«$\E(\theta\given x)$ is a weighted average of the prior mean $\E(\theta)$ and the MLE $\hat\theta$.»

**S1.11 Quiz.** Typed: probability $\theta$ of a successful spaceship launch; prior data indicated a $\BetaDist(1,10)$ prior (see plot). What does this reflect about our prior belief on $\theta$? (No annotation; no answer given.)
*Figure:* plot of the $\BetaDist(1,10)$ density on $[0,1]$ (ticks 0, 0.2, …, 1.0; vertical axis 0–10): starts at 10 at $\theta = 0$ and decays convexly to near 0 by about $\theta = 0.4$, flat near 0 thereafter. A clip-art rocket at the lower right (decorative; omit).

---

## 5. Guest lecture 5: MCMC Sampling (S2, 16 slides)

S2 has **no handwritten annotations**; several slides are left blank for in-lecture writing (their content was not captured). Index:

| Slide | Content |
|---|---|
| 1 | Title: Lecture 5, MCMC Sampling, Semester 1, 2026 |
| 2 | Recap of Lecture 4: frequentist vs Bayesian; prior $f(\theta)$, likelihood $f(x\given\theta)$, posterior $f(\theta\given x)$; posterior ∝ data × prior; posterior mean $\E[\theta\given x]$, posterior mode $\argmax_\theta f(\theta\given x)$ |
| 3 | Tricky distributions: can you compute $\E(\vect x)$ if $f(x)\propto x^2e^{-x^2+\sin x}$; $f(x_1,x_2)\propto e^{-x_1x_2-x_1-x_2}$; $f(x_1,x_2)\propto x_2^ae^{-(b-x_1)^2/x_2+bx_1+cx_2}$. Difficult when the posterior is complicated, has no closed form, or is known only up to a normalising constant |
| 4 | The computational problem: $\E[\theta\given\vect x] = \int\theta f(\theta\given\vect x)\dd\theta$, but $f(\vect x)$ is often intractable [space left blank] |
| 5 | Strategy: approximate the posterior via simulation; how to sample from a distribution known up to a constant? Two techniques: Metropolis–Hastings, Gibbs [space left blank] |
| 6 | **Metropolis–Hastings**: aim, construct a Markov chain whose stationary distribution is $f(\theta)$. Start at $\theta^{(0)}$; at iteration $i+1$: propose $\theta^*\sim q(\theta^*\given\theta^{(i)})$; accept with probability $\alpha = \min\Bigl\{1, \dfrac{f(\theta^*)\,q(\theta^{(i)}\given\theta^*)}{f(\theta^{(i)})\,q(\theta^*\given\theta^{(i)})}\Bigr\}$; otherwise stay at $\theta^{(i)}$ |
| 7 | Special case: random-walk MH, "If the proposal model $q(\theta^*\given\theta)$ is symmetric:" [rest left blank — the simplified acceptance ratio is not written] |
| 8 | Example: Beta–binomial model, $x\given\theta\sim\Bin(n,\theta)$, $\theta\sim\BetaDist(\alpha,\beta)$; posterior $f(\theta\given\vect x)\propto\theta^{\alpha+x-1}(1-\theta)^{\beta+n-x-1}$; "Random Walk MH algorithm:" [blank] |
| 9 | R code: random-walk MH for the Beta–binomial example (see Code below) |
| 10 | Exercise: random-walk MH for $f(x)\propto x^2e^{-x^2+\sin x}$ (no solution) |
| 11 | **Gibbs sampling**: aim, samples from $f(\theta_1,\dots,\theta_p)$; start at $\vect\theta^{(0)}$; at iteration $i+1$ sample $\theta_1^{(i+1)}\sim f(\theta_1\given\theta_2^{(i)},\dots,\theta_p^{(i)})$, $\theta_2^{(i+1)}\sim f(\theta_2\given\theta_1^{(i+1)},\theta_3^{(i)},\dots,\theta_p^{(i)})$, …, $\theta_p^{(i+1)}\sim f(\theta_p\given\theta_1^{(i+1)},\dots,\theta_{p-1}^{(i+1)})$; set $\vect\theta^{(i+1)}$ |
| 12 | Example: Gibbs sampler for $f(x_1,x_2)\propto e^{-x_1x_2-x_1-x_2}$ [the full conditionals $X_1\given x_2\sim\Expo(x_2+1)$, $X_2\given x_1\sim\Expo(x_1+1)$ are not written; they are implicit in the code] |
| 13 | R code for slide 12 (see Code below) |
| 14 | Exercise: normal model $x\given\mu,\sigma^2\sim\Normal(\mu,\sigma^2)$, $\mu\sim\Normal(\mu_0,\sigma_0^2)$, $\sigma^2\sim\text{Inv-Gamma}(\alpha_0,\beta_0)$: (1) derive the posterior, (2) Gibbs algorithm, (3) R code for the posterior means (no solution) |
| 15–16 | Blank |

### Code in S2 (R, verbatim)

Slide 9 (random-walk MH, Beta–binomial):
```r
# Data
n <- 10;
x <- 3
a <- 2 #alpha
b <- 2 #beta

# Log posterior (up to constant)
post <- function(theta, n, x, a, b) {
  if(theta <= 0 || theta >= 1) return(-Inf)
  theta^(a + x - 1)*(1-theta)^(b + n - x - 1)
}

# MCMC settings
N      <- 10000
sigma <- 0.1
theta <- numeric(N)
theta[1] <- 0.5
accept <- 0

for(i in 2:N){
  proposal <- rnorm(1, theta[i-1], sigma)
  alpha <- post(proposal, n=n,x=x,a=a,b=b) / post(theta[i-1], n=n,x=x,a=a,b=b)
  if(runif(1) < alpha){
    theta[i] <- proposal
    accept <- accept + 1
  } else {
    theta[i] <- theta[i-1]
  }
}

# results
plot(theta, type="l")
mean(theta)
(a+x)/(a+b+n) #posterior mean
```
[possible error: the comment says "Log posterior" but `post` returns the unnormalised posterior itself (not its log), and the ratio `post/post` is used accordingly; returning `-Inf` outside $(0,1)$ is the log-scale convention. On the density scale it should return `0`. As written, a proposal outside $(0,1)$ gives `alpha = -Inf`, which is never accepted, so the sampler still works.]

Slide 13 (Gibbs sampler):
```r
#density
fx = function(x1,x2) { exp(-(x1*x2+x1+x2)) * (x1>0 & x2>0)}

#plot density surface
library(rgl)
xgrid = seq(0,7,by=0.05)
z = outer(xgrid, xgrid, fx)
persp3d(z,col="red")

#simulation
N = 10^4
x = matrix(0,N,2)
x1=0; x2 = 1              #initial state
for (i in 1:N){
    x1 = rexp(1, x2+1)
    x2 = rexp(1, x1+1)
    x[i, ] = c(x1, x2)
}

#plot of simulated values
plot(x, pch=20, col="blue")
library(MASS)
x.kde = kde2d(x[,1], x[,2], n=50)
contour(x.kde, add=T, lwd=2, col="green")
```
(The plots the code produces are not in the slides.)
