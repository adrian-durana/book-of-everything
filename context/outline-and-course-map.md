# Book of Everything: Chapter Outline and Course Map (v3)

_Last updated: 2026-11-18. Generated from `tools/chapters.py` in the repo, which is the source of truth for the structure. Every chapter has a file `chapters/<part-folder>/<slug>.tex`, labelled `ch:<slug>`._

**Tiers.** Important: Parts III, IV and VI, plus the real analysis and calculus chapters in Part I. Background: the rest of Parts I, II, V and VIII. Important and Background both get full treatment. Nice to have: Part VII, as summary chapters. **Code:** R in Parts III–IV, Python everywhere else.

**v3 change (pilot):** Part III was restructured. Generating functions moved before the new *Common Distributions* chapter, and *Transformations of Random Variables* was split out of *Multivariate Distributions*. All chapters after 28 have shifted by up to two numbers.

**Ingestion order:** STAT2003 (pilot: Ch 26 ✅) → STAT3500 (second pilot, with code: GLMs) → STAT3004 → STAT2004 → STAT3001 → STAT1301 → STAT3006 → STAT3007 → STAT3008 → MATH2401/2400 → MATH1071/1072/2001 → Background tier → Nice to have.

## Part I: Foundations (`foundations/`, Python)
1. Logic and Proof (`ch:logic-and-proof`): MATH1061
2. Sets, Relations and Functions (`ch:sets-relations-functions`): MATH1061
3. Induction, Recursion and Counting (`ch:induction-recursion-counting`): MATH1061
4. Graph Theory (`ch:graph-theory`): MATH1061
5. Number Theory and Algebraic Structures (`ch:number-theory-algebraic-structures`): MATH1061
6. Vectors, Matrices and Linear Systems (`ch:vectors-matrices-linear-systems`): MATH1071
7. Eigenvalues, Diagonalisation and Quadratic Forms (`ch:eigenvalues-diagonalisation`): MATH1071, MATH2001
8. Vector Spaces and Inner Products (`ch:vector-spaces-inner-products`): MATH2001
9. The Real Numbers, Sequences and Series (`ch:real-numbers-sequences-series`): MATH1071, MATH2401, MATH2400
10. Continuity (`ch:continuity`): MATH1071, MATH2401, MATH2400
11. Differentiation (`ch:differentiation`): MATH1071, MATH2401, MATH2400
12. Integration (`ch:integration`): MATH2401, MATH1071, MATH2400
13. Sequences and Series of Functions (`ch:sequences-series-of-functions`): MATH2401, MATH2400
14. Metric Spaces (`ch:metric-spaces`): MATH2401
15. Differential Calculus in Several Variables (`ch:differential-calculus-several-variables`): MATH2401, MATH1072, MATH2001, MATH2400
16. Multiple Integrals and Change of Variables (`ch:multiple-integrals`): MATH2001
17. Vector Calculus (`ch:vector-calculus`): MATH1072, MATH2001

## Part II: Differential Equations (`differential-equations/`, Python)
18. First-Order Ordinary Differential Equations (`ch:first-order-odes`): MATH1072, MATH2010
19. Linear Higher-Order ODEs (`ch:linear-higher-order-odes`): MATH1072, MATH2001
20. Linear Systems of ODEs (`ch:linear-systems-odes`): MATH2010
21. The Laplace Transform (`ch:laplace-transform`): MATH2010
22. Stability and Phase-Plane Analysis (`ch:stability-phase-plane`): MATH2010, MATH1072
23. Fourier Series (`ch:fourier-series`): MATH2011
24. Partial Differential Equations (`ch:pdes`): MATH2011, MATH2001

## Part III: Probability (`probability/`, R)
25. Probability Spaces (`ch:probability-spaces`): STAT2003, STAT1301, MATH1061
26. Random Variables and Distribution Functions (`ch:random-variables`): STAT2003
27. Expectation, Variance and Moments (`ch:expectation-moments`): STAT2003
28. Generating Functions and Transforms (`ch:generating-functions`): STAT2003, STAT3004
29. Common Distributions (`ch:common-distributions`): STAT2003
30. Multivariate Distributions (`ch:multivariate-distributions`): STAT2003
31. Conditional Distributions and Conditional Expectation (`ch:conditional-expectation`): STAT2003
32. Transformations of Random Variables (`ch:transformations`): STAT2003
33. Convergence of Random Variables and Limit Theorems (`ch:limit-theorems`): STAT3004, STAT2003
34. Discrete-Time Markov Chains (`ch:discrete-time-markov-chains`): STAT2003, STAT3004
35. Poisson Processes and Continuous-Time Markov Chains (`ch:poisson-ctmc`): STAT3004
36. Stochastic Models and Reliability (`ch:stochastic-models`): STAT3004, STAT2003
37. Simulation and Monte Carlo Methods (`ch:simulation-monte-carlo`): STAT2003, STAT3004, STAT3500

## Part IV: Statistics (`statistics/`, R)
38. Data, Exploratory Analysis and Study Design (`ch:eda-study-design`): STAT1301
39. Statistical Models and Sampling Distributions (`ch:sampling-distributions`): STAT2004, STAT1301
40. Point Estimation (`ch:point-estimation`): STAT2004, STAT3001
41. Sufficiency, Completeness and the Exponential Family (`ch:sufficiency-exponential-family`): STAT3001
42. Likelihood Theory (`ch:likelihood-theory`): STAT3001, STAT2004
43. Confidence Intervals (`ch:confidence-intervals`): STAT2004, STAT3001, STAT1301
44. Hypothesis Testing (`ch:hypothesis-testing`): STAT3001, STAT2004, STAT1301
45. Categorical Data Analysis (`ch:categorical-data`): STAT1301, STAT2004
46. Linear Models and Regression (`ch:linear-models`): STAT2004, STAT1301
47. Analysis of Variance (`ch:anova`): STAT2004, STAT1301
48. Generalized Linear Models (`ch:glms`): STAT3500, STAT2004
49. Generalized Estimating Equations (`ch:gee`): STAT3500
50. Bayesian Inference (`ch:bayesian-inference`): STAT3500, STAT2004, STAT3001
51. The EM Algorithm and the Bootstrap (`ch:em-bootstrap`): STAT3001
52. Time Series (`ch:time-series`): STAT3500

## Part V: Numerical Methods and Optimisation (`numerics-optimisation/`, Python)
53. Floating-Point Arithmetic, Error and Root-Finding (`ch:floating-point-root-finding`): COSC2500, MATH1072, MATH2400
54. Interpolation, Numerical Differentiation and Quadrature (`ch:interpolation-quadrature`): COSC2500, MATH1071
55. Numerical Methods for ODEs (`ch:numerical-odes`): COSC2500, MATH1072
56. Matrix Types, Norms and Factorisations (`ch:matrix-factorisations`): MATH3204, MATH2001, COSC2500
57. Least Squares and the Singular Value Decomposition (`ch:least-squares-svd`): MATH3204, MATH2001
58. Iterative Methods and Krylov Subspaces (`ch:krylov-methods`): MATH3204
59. Eigenvalue Algorithms (`ch:eigenvalue-algorithms`): MATH3204
60. Randomised Numerical Linear Algebra (`ch:randomised-nla`): MATH3204
61. Convex Analysis (`ch:convex-analysis`): MATH3204
62. Unconstrained Optimisation (`ch:unconstrained-optimisation`): MATH3204
63. Constrained Optimisation and Duality (`ch:constrained-optimisation`): MATH3204
64. Non-Smooth, Stochastic and Derivative-Free Optimisation (`ch:nonsmooth-stochastic-optimisation`): MATH3204
65. Calculus of Variations (`ch:calculus-of-variations`): MATH3404
66. Optimal Control (`ch:optimal-control`): MATH3404
67. Linear Programming (`ch:linear-programming`): MATH3202
68. Integer Programming (`ch:integer-programming`): MATH3202
69. Dynamic Programming (`ch:dynamic-programming`): MATH3202
70. Metaheuristics (`ch:metaheuristics`): MATH3202

## Part VI: Machine Learning (`machine-learning/`, Python)
71. The Statistical Learning Framework (`ch:learning-framework`): STAT3006, STAT3007
72. Nearest Neighbours and Decision Trees (`ch:nearest-neighbours-trees`): STAT3006
73. Linear Methods for Regression and Classification (`ch:linear-methods-ml`): STAT3006
74. Ensembles: Random Forests and Boosting (`ch:ensembles`): STAT3006
75. Kernels and Reproducing Kernel Hilbert Spaces (`ch:kernels-rkhs`): STAT3008
76. Support Vector Machines (`ch:svms`): STAT3008, STAT3006
77. Gaussian Processes (`ch:gaussian-processes`): STAT3008, STAT3006
78. Statistical Learning Theory (`ch:learning-theory`): STAT3008
79. Unsupervised Learning (`ch:unsupervised-learning`): STAT3006
80. Neural Networks (`ch:neural-networks`): STAT3007, STAT3006, STAT3008
81. Training Deep Networks (`ch:training-deep-networks`): STAT3007
82. Deep Architectures (`ch:deep-architectures`): STAT3007
83. Generative Models (`ch:generative-models`): STAT3006, STAT3008
84. Reinforcement Learning (`ch:reinforcement-learning`): STAT3007

## Part VII: Applications (`applications/`, Python)
85. Interest Rates, Annuities and Fixed Income (`ch:interest-annuities-fixed-income`): MATH3090
86. Equities, Forwards, Futures and the Term Structure (`ch:equities-derivatives-term-structure`): MATH3090
87. Microeconomics in Brief (`ch:microeconomics`): ECON1010
88. Macroeconomics in Brief (`ch:macroeconomics`): ECON1020

## Part VIII: Scientific Computing (`scientific-computing/`, Python)
89. Programming in Python (`ch:python-programming`): MATH2504, COSC2500
90. Software Development Practice: git, Unix and Testing (`ch:software-development`): MATH2504
91. Algorithms and Data Structures (`ch:algorithms-data-structures`): MATH2504
92. Symbolic Computation (`ch:symbolic-computation`): MATH2504
93. Simulation and Data Analysis Workflows (`ch:simulation-data-pipelines`): MATH2504

---

## Course → chapter map (generated from `tools/chapters.py`)

| Course | Chapters |
|---|---|
| COSC2500 | 53–56, 89 |
| ECON1010 | 87 |
| ECON1020 | 88 |
| MATH1061 | 1–5, 25 |
| MATH1071 | 6–7, 9–12, 54 |
| MATH1072 | 15, 17–19, 22, 53, 55 |
| MATH2001 | 7–8, 15–17, 19, 24, 56–57 |
| MATH2010 | 18, 20–22 |
| MATH2011 | 23–24 |
| MATH2400 | 9–13, 15, 53 |
| MATH2401 | 9–15 |
| MATH2504 | 89–93 |
| MATH3090 | 85–86 |
| MATH3202 | 67–70 |
| MATH3204 | 56–64 |
| MATH3404 | 65–66 |
| STAT1301 | 25, 38–39, 43–47 |
| STAT2003 | 25–34, 36–37 |
| STAT2004 | 39–40, 42–48, 50 |
| STAT3001 | 40–44, 50–51 |
| STAT3004 | 28, 33–37 |
| STAT3006 | 71–74, 76–77, 79–80, 83 |
| STAT3007 | 71, 80–82, 84 |
| STAT3008 | 75–78, 80, 83 |
| STAT3500 | 37, 48–50, 52 |