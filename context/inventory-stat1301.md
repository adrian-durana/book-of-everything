# Coverage inventory: STAT1301 Advanced Analysis of Scientific Data

_Built 2026-11-18._

**Sources.** Two versions of the course notes:
- **CN26**, dated 22 July 2026 (269 pp.). This is the **primary** source.
- **CN24**, dated 15 July 2024 (261 pp.).

The two are about 96% identical word for word. CN26 moves "Statistical Studies" into Ch 1 (§1.2) and "Statistical Modeling" into Ch 4 (§4.1), renumbers Ch 1, and adds **Appendix B (answers to exercises)**. No content appears only in CN24 apart from text that moved. Section numbers below are CN26's.

**Code:** R throughout (the course is R-based; Part IV uses R). **Content rule:** source material only, with corrections. Status: ✅ written, ◻ to do, ↔ merge into an existing STAT2003 entry (don't duplicate).

---

## Part III (probability): mostly overlaps STAT2003
### Ch 25 Probability spaces
- ↔ Random experiments; coin tossing with simulation (Fig 1.1–1.2) (§1.3)
- ↔ Sample space, events, set laws (Thm 1.1), Venn diagrams (§1.4, Def 1.1–1.2)
- ↔ Probability measure, properties (Def 1.3, Thm 1.2)
- ↔ Counting: Thm 1.3–1.5, urn and tree diagrams (§1.5)
- ↔ Conditional probability, independence, product rule (Def 1.4–1.5, Thm 1.6; Examples 1.4–1.6)
- ↔ Law of total probability, Bayes' rule (Thm 1.7–1.8); quality-control example (Ex 1.7) (§1.7)

### Ch 26 Random variables and distribution functions
- ✅ Discrete vs continuous (countable; intervals with P(X=c)=0); CDF (Def 1.6); P(a<X≤b) (§1.8)
- ✅ pmf (Def 1.7), P(X ∈ B) = Σ f; sum-of-two-dice table (Ex 1.8)
- ✅ pdf (Def 1.8), X ~ f notation, P(X ∈ B) = ∫_B f, F' = f, density interpretation; random point in [0,2] (Ex 1.9)
- ✅ Quantiles and percentiles, quantile function (Def 1.9)

### Ch 27 Expectation, variance and moments
- ↔ Expectation, discrete and continuous (Def 1.10–1.11); expected payout example (Ex 1.10)
- ↔ E g(X) (Thm 1.9); die example E X² (Ex 1.11); properties (Thm 1.10); variance (Def 1.12) and its properties (§1.9)

### Ch 29 Common distributions
- ↔ Bernoulli (Def 2.1, Thm 2.1); binomial (Def 2.2, Thm 2.2); uniform (Def 2.3, Thm 2.3)
- ↔ Normal (Def 2.4, Thm 2.4), standardisation (Thm 2.5, Ex 2.1); R functions (`dnorm`, `pnorm`, `qnorm`, `rnorm`, …) (§2.2–2.5)

### Ch 30 Multivariate distributions
- ↔ Joint CDF, pmf, pdf (Def 3.1–3.3); three-dice box example (Ex 3.1)
- ↔ Independence (Def 3.4, Ex 3.2); bivariate standard normal (Ex 3.3)
- ↔ Expectation properties (Thm 3.1); covariance (Def 3.5, Thm 3.2); variance of linear combinations (Thm 3.3); binomial mean and variance via sums (Ex 3.4)
- ↔ Linear combinations of normals are normal (Thm 3.6)

### Ch 33 Limit theorems
- ↔ LLN (Thm 3.4), CLT (Thm 3.5) with R illustrations (§3.5)

### Ch 37 Simulation
- ↔ Simulating random variables in R (§2.6)

## Part IV (statistics): STAT1301 is the first source for most of these
### Ch 38 Data, exploratory analysis and study design
- ◻ Statistics and the steps for a statistical study; biased-coin example (Ex 1.1) (§1.1–1.2)
- ◻ Data, sampling from a population, villagers example (Ex 4.4); designed experiment: Alice's caffeine data (§4.2–4.4)
- ◻ Descriptive statistics: data as a spreadsheet, variable types, summary statistics, categorical variables, quantitative variables, one categorical plus one quantitative, pairs of quantitative variables; R plotting (Ch 5)
- ◻ Randomisation and blocking (§8.4)

### Ch 39 Statistical models and sampling distributions
- ◻ Statistical modelling: one-sample normal, two-sample binomial, two-sample normal models (Ex 4.1–4.3); remark on modelling (Rem 4.1) (§4.1)
- ◻ Standardised mean and Student t-distribution (Thm 6.2)

### Ch 40 Point estimation
- ◻ Estimates and estimators; biased coin (Ex 6.1); iid normal sample (Ex 6.2); method of moments (Ex 6.3) (§6.2)

### Ch 43 Confidence intervals
- ◻ Definition (Def 6.1); approximate CI for μ (Thm 6.1, oil company Ex 6.4)
- ◻ Normal data, one sample: exact CI for μ (Thm 6.3, water drop Ex 6.5); Thm 6.4 (variance; check); aspirin (Ex 6.6)
- ◻ Normal data, two samples (Thm 6.5, human movement Ex 6.7)
- ◻ Binomial one and two samples (opinion poll Ex 6.8–6.9, nightmares Ex 6.10–6.11) (§6.3)

### Ch 44 Hypothesis testing
- ◻ Steps for a statistical test; blood pressure (Ex 7.1); biased coin revisited (Ex 7.2) (§7.1)
- ◻ One-sample t-test, p-values, `t.test` (§7.2)
- ◻ Type-I and Type-II errors, power; simulating the power, `power.t.test` (Ex 7.3) (§7.3)
- ◻ One-sample test for proportions; market research (Ex 7.4–7.6, Rem 7.1) (§7.4)
- ◻ Two-sample t-test, paired data (Ex 7.7–7.8) (§7.5)
- ◻ Two-sample test for proportions: ABC viewers (Ex 7.9–7.10) (§7.6)
- ◻ Multiple comparisons (§8.5)

### Ch 45 Categorical data analysis (chi-squared tests)
- ◻ Multinomial distribution (Def 11.1), army recruits (Ex 11.1); ↔ also Ch 29
- ◻ Goodness of fit with known parameters (Thm 11.1, Rem 11.1–11.2, simulation Ex 11.2, frizzled chickens Ex 11.3)
- ◻ Unknown parameters (Thm 11.2); testing independence in contingency tables (ESP belief Ex 11.4) (§11.2–11.3)

### Ch 46 Linear models and regression
- ◻ Simple linear regression (Def 9.1); least-squares estimates (Thm 9.1); properties of estimators (Thm 9.2); hypothesis tests; `lm`; confidence and prediction intervals; validating assumptions (§9.2)
- ◻ Multiple linear regression (Def 9.2), analysis and validation (§9.3)
- ◻ Normal linear model (Def 10.1); SLR and one-factor ANOVA as special cases (Ex 10.1–10.2); estimation and testing; residual analysis; transformations of data (Ch 10)

### Ch 47 Analysis of variance
- ◻ Single-factor ANOVA: model (Def 8.1), estimation, F-test, worked example (§8.2)
- ◻ Two-factor ANOVA: model (Def 8.2), estimation, testing, worked example (§8.3)

## Not yet placed
- **Appendix A: R tutorial** (installing; vectors and data frames, component selection, lists, linear algebra, flow control, functions, graphics, reading and writing data, workspace and packages). _Proposed home: a new Part VIII chapter, "Programming in R"._
- **End-of-chapter exercises (§1.10, 2.7, 3.6, 4.5, 5.9, 6.4, 7.7, 8.6, 9.4, 10.6, 11.4) and answers (CN26 App B):** a pool for worked examples.
- **References** (Kroese & Chan 2014, etc.).

## Corrections
_None found yet. Record them here while drafting._
