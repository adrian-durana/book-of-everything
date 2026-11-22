# Coverage inventory: STAT2003 Mathematical Probability

_Built 2026-11-18 from 89 photos of the handwritten notes (main reference) and the course notes PDF (21 Feb 2025, 191 pp.). Statuses updated 2026-11-21._

**Sources.** "HW nn" means photo pair nn: two notebook pages, in shooting order. "CN x.y" means a course notes section. **Code:** the course used Python (lecture scripts such as `L21-Uniform2.py`); the book uses **R** for Part III, as decided. **Content rule:** source material only, with corrections.

**Status:** ✅ written, ◻ to do.

---

## Ch 25 Probability spaces (`ch:probability-spaces`)
- ✅ Random experiments, sample space, events (CN 1.1–1.3)
- ✅ (Ω, F, P); F ⊆ 𝒫(Ω); σ-algebra remark for infinite Ω; unfair-coin example (HW 01)
- ✅ Axioms and consequences: P(∅)=0, monotonicity, P(A)≤1, complement, union of two events, with proofs (HW 01–02, CN 1.4)
- ✅ Counting: four urn schemes, balls-in-bins analogy, formulas n^k, nPk, nCk, C(n+k−1,k); dice example (HW 02–03, CN 1.5)
- ✅ Inclusion–exclusion principle; union bound (HW 43, CN 1.5)
- ✅ Conditional probability; P(·|B) satisfies the axioms (HW 03, CN 1.6)
- ✅ Product rule; law of total probability; Bayes' rule (HW 03–04, CN 1.6.1–1.6.2)
- ✅ Independence of events (HW 04, CN 1.6.3)
- ✅ Cable-matching example, P → 1 − 1/e (HW 43)

## Ch 26 Random variables and distribution functions (`ch:random-variables`)
- ✅ Random variable X: Ω → E; {X ∈ A} notation; sum-of-two-dice and coin-flip examples; range; discrete vs continuous (HW 04, CN 2.1)
- ✅ Probability distribution as a description of P(X ∈ A) (HW 04, CN 2.2)
- ✅ CDF definition; properties (proofs of monotonicity and bounds as in CN; limits and right-continuity stated) (HW 05, CN 2.2)
- ✅ P(a<X≤b), P(X=a), P(a≤X≤b) from the CDF (CN 2.2)
- ✅ Discrete distributions, pmf, P(X ∈ B) = Σ f; die and max-of-two-dice examples; pmf from the CDF (corrected) (HW 04, CN 2.2.1)
- ✅ Continuous distributions, pdf, F' = f, density interpretation, P(X=x) = 0; uniform on [0,2] example (HW 05, CN 2.2.2)

## Ch 27 Expectation, variance and moments
- ✅ E X (discrete and continuous); E g(X); f(x)=2x example (HW 06, CN 2.3)
- ✅ Moments, central moments, variance, standard deviation, skewness and kurtosis (HW 06)
- ✅ Linearity of expectation (proof) (HW 07)
- ✅ Var X = E X² − (E X)², Var(aX+b) = a² Var X, SD(aX+b) = |a| SD X (proofs) (HW 07)
- ✅ Markov inequality (general h, indicator proof), Chebyshev inequality (HW 07, 32)

## Ch 28 Generating functions and transforms
- ✅ PGF: definition, pmf from derivatives at 0, moments, variance formula; Poisson PGF (HW 14, CN 2.4)
- ✅ MGF: definition, moments M^{(n)}(0), variance (HW 14, CN 2.4)
- ✅ Sums of independent RVs: G_{X+Y} = G_X G_Y, M_{X+Y} = M_X M_Y (HW 27): placed in Ch 30

## Ch 29 Common distributions
- ✅ i.i.d. Bernoulli trials as the generating model (HW 08)
- ✅ Bernoulli, binomial, geometric (support {1,2,…}), negative binomial, Poisson (Bin(n, λ/n) limit with proof; pmf sums to 1; mean), hypergeometric (→ binomial) (HW 08–11, CN 2.5)
- ✅ Uniform, exponential (memoryless), normal (standardisation, X = μ+σZ, MGF), gamma (Γ function), beta, chi-square = Gamma(n/2, 1/2) (HW 11–13, CN 2.6); Weibull moved to Ch 36
- ✅ Multinomial (HW 21): placed in Ch 30
- ◻ Summary of formulas (CN Appendix C): not used yet

## Ch 30 Multivariate distributions
- ✅ Random vectors; joint pmf/pdf/CDF; marginals; worked 2×3 table (HW 17, 24, CN 4.1)
- ✅ Independence of RVs (HW 19, CN 4.1)
- ✅ E h(X,Y); E[X+Y] = E X + E Y (proof) (HW 18, CN 4.2)
- ✅ Covariance, properties 1–8 (proofs of 5–7), correlation (HW 19, CN 4.2)
- ✅ Expectation vector, covariance matrix (symmetric, PSD: corrected), Cov(X) = E XX^T − μμ^T, Cov(AX) = A Cov(X) A^T (HW 20, 24)
- ◻ Multivariate normal (moved to Ch 32): density derivation, properties, Y = AX via the MGF, marginals, linear combinations, simulation via μ + BX (HW 20, 29–30, CN 5.2); exercises (HW 31)

## Ch 31 Conditional distributions and conditional expectation
- ✅ Conditional pmf/pdf (corrected denominator); table example; discrete-triangle example; conditional CDF limit; product rule and law of total probability for densities; more than two variables (HW 18, CN 4.3)
- ✅ E[X | Y=y], E[X | Y], tower property (proof, continuous case); random sums (corrected: N independent of the X_i) (HW 21, CN 4.4)

## Ch 32 Transformations of random variables
- ◻ Discrete case; examples |X−3| and Bin then X² (HW 22, CN 5.1)
- ◻ Simulation method; CDF method; transformation rule; −ln U ~ Exp(1) (HW 22–23, CN 5.1)
- ◻ Location–scale transforms (HW 22)
- ◻ Order statistics: max/min, r-th order statistic, min of exponentials, max of uniforms, eggs example (HW 25–26)
- ◻ Sums: convolution (proof), Poisson + Poisson, U + Exp(1) (HW 26–27, CN 5.1.1)
- ◻ Linear and general Jacobian transformations; polar coordinates; Cauchy as a ratio of normals (HW 28–29, CN 5.1.2–5.1.3)

## Ch 33 Convergence and limit theorems
- ◻ Convergence in probability, almost surely, in distribution (HW 33)
- ◻ Weak LLN (proof via Chebyshev), strong LLN (statement) (HW 32–33, CN 5.4)
- ◻ CLT statement and MGF-based proof, normal approximation to the binomial (HW 33–34, CN 5.4)

## Ch 34 Discrete-time Markov chains
- ◻ Stochastic processes overview (HW 34); Markov property, time-homogeneity, transition matrix (HW 35, CN 6.1)
- ◻ Chapman–Kolmogorov, P^(n) = P^n; π^(n) = π^(0)P^n; joint distribution (HW 35–36)
- ◻ Examples: stepping stones, spider–fly "hunt", Max the dog (HW 34–38)
- ◻ Limiting and stationary distributions; two-state chain; global balance; random walk on Z⁺; birth–death chains (HW 37–39, CN 6.3)

## Ch 36 Stochastic models and reliability
- ◻ Structure functions: series, parallel, k-out-of-n, coproduct notation, modular decomposition, pivot method, bridge system (HW 39–40, CN 7.2)
- ◻ Monotone systems, minimal path and cut sets (HW 41)
- ◻ Reliability functions: series, parallel (corrected), 2-out-of-3, k-out-of-n (corrected), bridge; bounds via cut sets (HW 41–43, CN 7.3)
- ◻ Non-repairable systems; Christmas-tree example (HW 43–44, CN 7.4)
- ◻ Survival function, E T = ∫R (proof), hazard rate, R = exp(−∫h) (proof), IFR/DFR, Weibull (HW 44–45, CN 7.5)

## Ch 37 Simulation and Monte Carlo methods
- ◻ Pseudorandom numbers, LCGs (HW 15, CN 3.2)
- ◻ Inverse-transform method: generalised inverse F^{-1}(y) = inf{x : F(x) ≥ y}, proof that F^{-1}(U) ~ F, algorithm, f(x)=2x example, discrete version (HW 15, CN 3.3)
- ◻ Acceptance–rejection, basic and general, efficiency 1/C (HW 16, CN 3.4)
- ◻ Generating from common distributions (CN 3.5); simulating Markov chains and random walks (HW 37, CN 6.2)

## Ch 46 Linear models (Part IV): cross-listed
- ◻ Normal linear model Y = Xβ + ε, least squares, σ̂² (HW 32, CN 5.3)

## Not used yet
- CN Appendix A–B (problem sets and solutions).
- CN Appendix C (summary of formulas).

## Corrections to the notes
1. P(X=x) = F(x) − F(x−1) only for integer-valued X; in general it is F(x) − lim_{u↑x} F(u) (HW 04). **Applied in Ch 26.**
2. The geometric support is {1, 2, …} (HW 09). **Applied in Ch 29.**
3. The conditional pmf denominator is f_Y(y) (HW 18). **Applied in Ch 31.**
4. Σ is PSD for all u, with eigenvalues ≥ 0 (HW 20). **Applied in Ch 30.**
5. Eggs example threshold: 65, not 58 (HW 26).
6. Parallel reliability is 1 − Π(1−p_i); the k-out-of-n sum starts at k (HW 42).
7. The CLT MGF proof needs the MGF to exist (HW 34): flag it, don't extend it.
8. The Markov inequality proof in HW 07 covers the continuous case only; HW 32 has the general indicator proof, so use that one. **Applied in Ch 27.**
9. CN §4.3: conditional CDF written F_{Y|X}(y | X); should be (y | x). **Applied in Ch 31.**
10. CN Ex 4.12 (random sums): N must be independent of X_1, X_2, … **Applied in Ch 31.**
