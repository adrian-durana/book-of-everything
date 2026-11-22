# Progress log

_Chapter status and corrections. The per-course inventories (`claude/inventory-<course>.md`) hold the topic → chapter mapping; this file records what is done. Updated 2026-11-21._

## Chapters written
| Ch | Title | Sources merged | Status |
|---|---|---|---|
| 25 | Probability Spaces | STAT2003 (HW, CN 1), STAT1301 (§1.3–1.7) | approved; standardised to STYLE.md (2026-11-21) |
| 26 | Random Variables and Distribution Functions | STAT2003 (HW, CN 2.1–2.2), STAT1301 (§1.8) | approved; standardised (2026-11-21) |
| 27 | Expectation, Variance and Moments | STAT2003 (HW, CN 2.3), STAT1301 (§1.9) | approved; standardised (2026-11-21) |
| 28 | Generating Functions and Transforms | STAT2003 (HW, CN 2.4) | approved; standardised (2026-11-21) |
| 29 | Common Distributions | STAT2003 (HW, CN 2.5–2.6), STAT1301 (§2.1–2.5, Table 2.1) | approved; standardised (2026-11-21) |
| 30 | Multivariate Distributions | STAT2003 (HW, CN 4.1–4.2), STAT1301 (§3.1–3.4) | approved (2026-11-21); standardised |
| 31 | Conditional Distributions and Conditional Expectation | STAT2003 (HW 18, 21, CN 4.3–4.4); no STAT1301 content | drafted under STYLE.md (2026-11-21). Awaiting user review |

**Next:** after Ch 31 review → 32 Transformations, including the multivariate normal (CN 5.1–5.2, HW 22–31, STAT1301 Thm 3.6) → 33 Limit theorems (CN 5.4, HW 32–34, STAT1301 §3.5) → 34 Markov chains (CN 6, HW 34–39) → 36 Reliability (CN 7, HW 39–45) → 37 Simulation (CN 3, HW 15–16, STAT1301 §2.6). Then the STAT1301 Part IV chapters (38–40, 43–47), plus the STAT2003 normal linear model in 46.

## Decisions
- Box style: keep the current style (option A: left bar with tint). (2026-11-20)
- Bold vectors and matrices: `\bm` (via `\vect`, `\mat`). (2026-11-20)
- Writing and layout preferences from the author's reviews are kept in `STYLE.md`, section "Writing and layout preferences", grouped by topic (tone, content and structure, naming, italics, lists, proofs, equations, figures, tables, boxes, notation). Every piece of review feedback is recorded there as a general rule and applied to all chapters, including future ones and course chats.
- Notation set in review: 𝔼(X) (𝔼X only where brackets clutter), PGF 𝒢 (`\pgf`), MGF ℳ (`\mgf`), Ber, Poi, 𝒩 (may revert), Gamma (rate; scale form mentioned), Beta, ℝ⁺/ℝ⁻, 𝒫(Ω).
- Code goes only in a chapter's computing section; applied in Ch 29 only so far (other chapters keep their code, per STYLE.md).
- Ch 31 convention: condition X on Y (as in the handwritten notes); the course notes condition Y on X. The triangle example keeps the notes' Y given X.

## Round-2 rules (2026-11-18, from the user)
1. Rename and rearrange section and subsection titles as content is added.
2. Every image in the typed or handwritten notes is redrawn in TikZ/pgfplots.
3. One (at most two) motivating examples per section or subsection.
4. Writing style follows the handwritten notes (typed notes where they explain better; STAT2003/STAT1301 typed style for courses without handwritten notes).
5. "Builds on" box text is plain, not italic. Long maths in examples goes on its own display line.

## Source material removed under rule 3 (can be restored later)
- Ch 25: control-chart, machine-lifetime (with lifetime table) and aeroplane examples (CN §1.1); the extra sample-space and event example lists; the 13-card probability example; the drawing-balls product-rule example; the five "more counting examples" (CN §1.5).
- Ch 25 (user feedback, 2026-11-20): system-reliability events example with the three-systems figure (CN §1.2; the systems reappear in Ch 36); area-measure triangle figure (analogy kept in prose); set-laws theorem box (laws now mentioned in prose, De Morgan kept as a display).
- Ch 26: two of the four background examples of random variables.
- Ch 27: the sum-of-two-dice "fair game" calculation (CN §2.3). The max-of-two-dice version (STAT1301) is kept as the interpretation.
- Ch 30: box with different dice and box with ordinary dice (joint pmf examples, CN §4.1); uniform random numbers with histograms (CN §4.1, Fig 4.2).
- Ch 31: nothing removed (two examples in §31.1: the HW table and the CN triangle).

## Placement decisions made while drafting
- Sums of independent RVs via PGF/MGF (Poisson + Poisson, sum of exponentials → gamma) → Ch 30, as in CN §4.2. Ch 32 covers sums by convolution (HW 26–27).
- Multivariate normal → Ch 32 (it is derived with the transformation rule).
- Weibull distribution → Ch 36 (it appears in the reliability notes).
- STAT1301 §2.6 (simulating random variables in R) → Ch 37.
- Multinomial distribution → Ch 30; also used in Ch 45 (chi-squared tests).
- CN Python code is converted to R in Part III.
- Figure data from simulations or tables is generated in R and stored in `figures/data/*.dat` in the repo.
- Course exercises (STAT1301 end-of-chapter, STAT2003 Appendix A–B) are not included yet.

## Corrections made to sources
| Source | Error | Fix | Ch |
|---|---|---|---|
| STAT2003 HW p.7 | P(X=x) = F(x) − F(x−1) "since discrete" | Only for integer-valued X; in general F(x) − lim_{u↑x}F(u) | 26 |
| STAT2003 HW p.17 | Geometric support {0,1,…} | {1,2,…} | 29 |
| STAT2003 HW p.34 (pair 18) | Conditional pmf denominator P(X=x) = f_X(x) | P(Y=y) = f_Y(y) | 31 |
| STAT2003 HW p.39 | Σ PSD "for u ≥ 0", eigenvalues "positive" | For all u; eigenvalues ≥ 0 | 30 |
| STAT2003 CN §1.5 | Lists "(ordered, with replacement)" twice | Fourth case is (unordered, with replacement) | 25 |
| STAT2003 CN §2.4 | pmf-from-PGF formula stated for x = 1, 2, … | Holds for x = 0, 1, 2, … | 28 |
| STAT2003 CN §2.5.5 | Non-red balls counted as "N − x" | N − r | 29 |
| STAT2003 CN §4.3 | Conditional CDF written F_{Y\|X}(y \| X) | F_{Y\|X}(y \| x) (lower-case x) | 31 |
| STAT2003 CN §4.4, Ex 4.12 | Random sums: N not assumed independent of the X_i | N independent of X_1, X_2, … (needed for E(S_N \| N) = Nμ) | 31 |
| STAT1301 §1.3 | R code `sample(c(0,1), n=100, replace=T)` | `size = 100` | 25 |
| STAT1301 §2.5 | Output shown as "[1] [1] 0.001349898" | Typo; value 0.001349898 | 29 |

_Pending corrections: eggs threshold 65 (Ch 32), parallel and k-out-of-n reliability (Ch 36), CLT MGF caveat (Ch 33), STAT1301 `rnorm(10e4)` = 100,000 draws (Ch 37)._
