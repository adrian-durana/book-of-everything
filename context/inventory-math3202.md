# Coverage inventory: MATH3202 Operations Research & Mathematical Planning

_Built from 80 photos of the handwritten notes (one notebook page per photo; HW 75 and HW 76 are two shots of the same page, so 79 distinct pages). No typed notes or slides were supplied (the notes refer to lecture "PowerPoint" slides on HW 55 and to named exam examples that are not included). Transcription: `claude/notes-math3202-1.md` (HW 01–40) and `claude/notes-math3202-2.md` (HW 41–80)._

**Sources.** "HW nn" means photo nn in shooting order (file names are listed in the notes). The last 23 pages (HW 58–80) are worked past-exam questions; their headings give the exam years, which are omitted here. They are called **Exam I** (HW 58–69), **Exam II** (HW 70–73, 80) and **Exam III** (HW 74–79). **Code:** the notes contain no code, only one pseudocode block (simulated annealing, HW 57); practicals were solved in Gurobi (HW 03). Part V uses **Python**. **Content rule:** source material only, with corrections.

**Status:** ✅ written, ◻ to do. Section numbers below are proposals (the chapters are empty so far). Every item is ◻.

**Character of the material.** Most pages are modelling examples in a fixed template (Sets / Data / Variables / Objective / Constraints for LP and IP; Stages / State / Action / Transition / Contribution / Value function / Base / Objective for DP). Theory is thin and mostly stated without proof (exceptions: dual of the dual, weak duality, the RSA optimality argument, the BFS improvement derivation). Under the "one motivating example, two at most" rule, most examples will be cut or moved to exercises; the inventory lists them all so the hub can choose.

---

## Ch 67 Linear Programming (`ch:linear-programming`)

### 67.1 Linear programming models
- ◻ Modelling template: sets, data, (decision) variables, objective, constraints; "Vars" short for variables / decision variables (HW 01)
- ◻ Ex. Farmer Jones' cakes: general model (HW 01), with numbers (HW 02); integrality "answer restricted to integers!" (HW 01) — **motivating example** (reused by the dual on HW 14, 21)
- ◻ N. "integer programming, a subtype of linear programming … simplex method" (HW 02) [flagged]
- ◻ Ex. cost of subsistence (diet) problem: 30 foods, 13 nutrients, min/max nutrient bounds; solved in Gurobi (HW 03) [sum index flagged]
- ◻ Ex. Giapetto's woodcarving (soldiers, trains; finishing, carpentry, max soldiers) (HW 05)
- ◻ Ex. Practical 2: Electrigrid — generators, transmission lines, flow balance, modified flow balance with line losses (HW 22) [production constraint flagged] ↔ also a network-flow model (68.4)
- ◻ Ex. Practical 3: Oil blending — vegetable/non-vegetable processing limits, linearised hardness limits; part (b) multi-month with purchase, storage, storage cost (HW 23–24)
- ◻ Ex. LP for minimising absolute error (least absolute deviations line fit): $z_i \ge e_i$, $z_i \ge -e_i$; rejected first attempts crossed out (HW 25) ↔ Ch 46 Linear models (regression, if least squares is there; LAD is new)
- ◻ Rem. modelling tips: linear matrix form, no strict inequalities, "hardest part is vars", no 'if' in a constraint (HW 25)
- ◻ Ex. Practical 4: Portfolio management, 10 products, constraints (1)–(8) without context (HW 29)

### 67.2 Standard form
- ◻ Def. standard form: maximise $\vect c\T\vect x$ s.t. $\mat A\vect x \le \vect b$ ($\Rightarrow \mat A\vect x = \vect b$), $\vect x \ge \vect 0$; sizes $n$, $m$ (HW 06)
- ◻ Rem. slack (and surplus) variables: $\vect a\T\vect x \le b \Rightarrow \vect a\T\vect x + s = b$, $\ge$ case with $-s$ (HW 06)
- ◻ Rem. minimise $\vect c\T\vect x$ = maximise $-\vect c\T\vect x$ (HW 06)
- ◻ Ex. Giapetto in standard form (HW 05)

### 67.3 Basic feasible solutions
- ◻ Def. basis: $m$ variables $S$ with invertible $\mat B$, basic variables $\vect x^B$, non-basic $\vect x^N = \vect 0$, $[\mat B \mid \mat N]$; $\vect x^B = \mat B^{-1}\vect b$; BFS if $\vect x^B \ge \vect 0$; $z^B = (\vect c^B)\T\mat B^{-1}\vect b$ (HW 07) ["linearly independent variables" flagged] ↔ Ch 6 (matrix inverse, MATH1071)
- ◻ Derivation: increasing a non-basic $x_{j^*}$ by $\lambda$; $\vect\alpha^{j^*} = \mat B^{-1}\vect p^{j^*}$; $\vect y = (\mat B^{-1})\T\vect c^B$; $z = z^B + \lambda(c_{j^*} - \vect y\T\vect p^{j^*})$ (HW 08)
- ◻ Improving a BFS: need $c_{j^*} - \vect y\T\vect p^{j^*} > 0$; increase until a basic variable hits 0, swap, repeat (HW 06, HW 08 Rem.)

### 67.4 The revised simplex algorithm
- ◻ Algorithm: initialisation (slack basis, $\mat B = \mat B^{-1} = \mat I$); Step 1 price (dual variables, reduced costs $c'_j = c_j - \vect y\T\vect p^j$, most positive, optimality stop); Step 2 ratio test ($\theta = \min\{x^B_k/\alpha^{j^*}_k : \alpha^{j^*}_k > 0\}$, unbounded stop); Step 3 update (HW 09–10)
- ◻ Ex. Giapetto by the RSA, four iterations, optimum $x_1 = 20$, $x_2 = 60$, $z = 180$ (HW 11–13) [all values checked] — **worked example**
- ◻ Ex. Exam I Q1(a)–(c): BFS from a given basis, entering $x_2$, leaving $x_3$, new BFS, optimality check, $z = 6$ (HW 58–63) [all values checked] — second worked example or exercise
- ◻ Rem. finite termination (no cycling) not proved (HW 18)

### 67.5 Duality
- ◻ Ex. Farmer Jones buying his ingredients: the dual LP (HW 14) — **motivating example**
- ◻ Def. primal (max $\vect c\T\vect x$, $\mat A\vect x \le \vect b$, $\vect x \ge \vect 0$) and dual (min $\vect b\T\vect y$, $\mat A\T\vect y \ge \vect c$, $\vect y \ge \vect 0$) (HW 15)
- ◻ Thm. the dual of the dual is the primal, with derivation (HW 15) [Dual (−) constraint flagged; labelled Def.]
- ◻ Thm. weak duality $\vect b\T\vect y \ge \vect c\T\vect x$; two proofs; lower/upper bound reading (HW 16) [labelled Def.; justification flagged]
- ◻ Thm. strong duality (stated without proof as such) and the unbounded ⇒ infeasible consequences (HW 17)
- ◻ Duality in the RSA: at termination $\vect y$ is dual feasible ($\mat A\T\vect y \ge \vect c$, $\vect y \ge \vect 0$ via slack reduced costs) and $\vect y\T\vect b = z^B$, hence optimal (HW 18) — this is the course's argument for strong duality
- ◻ Def. complementarity of variables and constraints (# constraints/variables table); slack, binding (HW 19)
- ◻ Thm. complementary slackness (1)–(4), "dual var > 0 ⇒ slack = 0"; Rem. on the name (HW 19) [stated without proof]
- ◻ Ex. economic interpretation: a second farmer buying Farmer Jones' stock; dual prices (HW 21)
- ↔ **merge Ch 63 Constrained Optimisation and Duality (MATH3204)**: LP duality, weak/strong duality and complementary slackness are the LP case of Lagrangian duality/KKT if MATH3204 covers them. Decide which chapter owns LP duality.

### 67.6 Sensitivity analysis
- ◻ Def. the two questions (RHS changes and their range; objective coefficient ranges); Rem. they are duals of each other (HW 20)
- ◻ RHS: $z^\Delta = z^* + \Delta y^*_j$, range from $\vect x^B + \Delta\mat B^{-1}\vect e^j \ge \vect 0$; dual variables as shadow prices (HW 20)
- ◻ Objective coefficients: non-basic ($c'_j < 0$), basic ($\vect y^\Delta = \vect y + \Delta\mat B^{-\top}\vect e^j$, keep $\vect y \ge \vect 0$) (HW 20) [margin note cut off: retake]
- ◻ Ex. Exam I Q1(d): increase in $c_3$ needed for $x_3$ to enter, $\Delta > 0.2$ (HW 64) ["more than" vs "at least" flagged]
- ◻ Ex. Exam I Q1(e): RHS $10 + \delta$ gives $z + 0.4\delta$ (HW 65) [checked]

---

## Ch 68 Integer Programming (`ch:integer-programming`)

### 68.1 Integer programs and the LP relaxation
- ◻ Integrality constraints $x \in \Z^+$, $x \in \Z$ (HW 01, 26, 28) [notation: see end]
- ◻ Def. linear relaxation problem (HW 26)
- ◻ Rem. many IP (and DP) models cannot be solved in reasonable time (HW 55) ↔ Ch 70

### 68.2 Branch and bound
- ◻ Ex. Telfa (tables, chairs): LP relaxation, branching on $x_1 \le 3$ / $x_1 \ge 4$, $x_2 \le 1$ / $x_2 \ge 2$, $x_1 \le 4$ / $x_1 \ge 5$; optimum $(5, 0)$, $z = 40$; "This method is called branch-and-bound" (HW 26) [relaxation value 47.25 flagged, should be 41.25] — **motivating example**; **Figure** (branch-and-bound tree, implied by the indented list; to draw)
- The general algorithm (bounding, pruning, incumbent) is **not** written in the notes.

### 68.3 Binary variables and logical constraints
- ◻ Ex. WordLock: letters on dials $x_{dl}$, spellable words $y_w$, word constraints $\ge 4y_w$; "refine" to exclude a word (HW 04) [refinement flagged]
- ◻ Ex. set covering: stations in towns, neighbour sets $n_c$, $\sum x \ge 1$; "data in the sum" remark (HW 27) [index flagged]
- ◻ Ex. Cloth Co.: fixed machine-rental cost, **big-M constraint** $x_c \le M_cy_c$ (HW 28) — motivating example for big-M
- ◻ Ex. Ewing Petroleum: **piecewise-linear cost** with tier binaries $z_2, z_3$, $z_3 \le z_2$; "the function (piecewise) is convex" (HW 30) [two subscripts flagged] ↔ Ch 61 Convex analysis (convexity remark only)
- ◻ Ex. noughts and crosses: lines "on" iff all equal, $1 - y_l \le \sum x_i \le 2 + y_l$ (HW 31)
- ◻ Ex. Bananagrams: fewest words using all 144 tiles; intersections $y_a$; Q. statement (HW 33)
- ◻ Ex. Pilots: hiring/firing with no firing in consecutive months, $z_t + z_{t-1} \le 1$, $y_t \le 60z_t$ (HW 35)
- ◻ Ex. Exam III Q2(b): **linearising a product** of binaries ($z \le \cdot$, $z \le \cdot$, $z \ge \cdot + \cdot - 1$), "logically equivalent alternative" (HW 75–76)
- ◻ Ex. Exam II Q2(b): chain stores, at most two per warehouse, at least $k$ warehouses, linking $z_w$ (HW 71) [sum range flagged]

### 68.4 Assignment, transportation and network models
- ◻ Ex. concrete: plants to jobs, **linear assignment problem**; equalities ⇒ duals can be negative; sparse; **total unimodularity** (integral inverses); optimal transport lines don't cross (HW 32) [TU definition flagged]
- ◻ Ex. storm: boats to ports with capacities (HW 36)
- ◻ Ex. cargo balancing: feasibility problem, "Objective: None!" (HW 34)
- ◻ Ex. Sudoku as an IP: $x_{rcn}$, row/column/cell/initial-placement constraints; block constraint not written (HW 38)
- ◻ Ex. coal line maintenance: flow conservation on arcs, maintenance binaries, labour limits, stockpile bypass (parts 2, 3a, 3b; 3c "exercise") (HW 39)
- ◻ Ex. Electrigrid (HW 22) as a network-flow LP ↔ 67.1
- ◻ Ex. Exam I Q2(a)–(b): chess-school instructor assignment, senior-instructor and balance constraints (HW 66–67)
- ◻ Ex. Exam II Q2(a): warehouse location (facility location) with capacities (HW 70)
- ◻ Ex. Exam III Q2(a): Grid Ball team selection (squares, budget, min/max cities) (HW 74–75)

### 68.5 Multi-period models
- ◻ Ex. pure fresh juice: quarters, FCOJ imports, truckloads $y_{ft}$ (HW 37) [objective unfinished]
- ◻ Oil blending (b) and Pilots are also multi-period (HW 23–24, 35) ↔ 67.1, 68.3

---

## Ch 69 Dynamic Programming (`ch:dynamic-programming`)

### 69.1 The principle of optimality and the Bellman equation
- ◻ Def. DP breaks a decision into a sequence of steps over time; principle of optimality; base case $V_{t_{\max}}(s)$; goal $V_0(s_0)$ (HW 40)
- ◻ Def. components: stages, state space, action space ($A_t$), transition $s_{t+1} = s^M(s_t, a_t)$, contribution $C_t(s_t, a_t)$, value function; **Bellman equation** $V_t(s_t) = \min_{a_t}\{C_t + V_{t+1}(s_{t+1})\}$, "+ can be any operation"; additive base 0, multiplicative base 1 (HW 41)
- ◻ Recap of deterministic DP (HW 50) — duplicate of HW 41, use for wording only
- ↔ **Ch 66 Optimal Control (MATH3404)** if it has the dynamic programming principle / HJB; **Ch 84 Reinforcement Learning (STAT3007)** (Bellman equation, MDPs). Decide where the Bellman equation is introduced.

### 69.2 Deterministic examples
- ◻ Ex. inventory problem: set-up cost, holding cost, tighter action range (HW 42) — **motivating example** (additive)
- ◻ Ex. minimal studying: minimise probability of failing all subjects, multiplicative model (HW 43)
- ◻ Ex. non-linear objective: max $(x_1+5)(x_2+1)(x_3+2)$ s.t. $3x_1 + 2x_2 + x_3 \le 6$ by DP; Q. (HW 44) [index flagged; no numerical answer]
- ◻ Ex. democracy: allocating 100 representatives to 50 LGAs, min–max discrepancy (HW 45)
- ◻ Ex. Exam I Q3(a): electricity purchase with battery (HW 68)
- ◻ Ex. Exam II Q3(a)–(b): racing with fatigue, decision tree, optimal policy, 1.2 expected wins (HW 72–73) [checked] — **Figure** (decision tree)
- ◻ Ex. Exam III Q3(a): selling sheep, flock doubles (HW 77)

### 69.3 Stochastic dynamic programming
- ◻ Def. stochastic DP: distribution of future states (HW 40); outcome space $\Omega_t(s_t, a_t)$, probabilities $p_t(\omega_t, s_t, a_t)$ summing to 1, transition $s^M(s_t, a_t, \omega_t)$, expected Bellman equation (HW 51) ↔ Ch 34 DTMCs (transition probabilities), Ch 27 (expectation), Ch 84 (MDPs)
- ◻ Ex. chess strategy (bold/conservative), all values computed, policy (HW 46) [checked] — **motivating example**
- ◻ Ex. betting strategy: reach 5 in three bets, $V_1(2) = 0.256$ with $b = 2$ (HW 47) [checked; third game blank]
- ◻ Ex. web-building spider ("based on a real paper"): max probability of reaching 80 mg (HW 49)
- ◻ Ex. Exam I Q3(b): random high demand (HW 69)
- ◻ Ex. Exam II Q3(c): augmented state (fatigue, wins), four-outcome recursion (HW 80)
- ◻ Ex. Exam III Q3(b): fertiliser and soil quality, two-year computation (1220 vs 1190; 830 tie) (HW 78–79) [checked; base-case labels flagged]

### 69.4 Shortest paths and labelling algorithms
- ◻ Ex. transcontinental drive: no stages needed for acyclic networks, $V(n) = \min_a c_a + V(t_a)$, forward distances $d_4$ (HW 48) [title "Stochastic" flagged]
- ◻ N. forward labelling: needs a node ordering, shortest paths, every deterministic DP can be turned into one (HW 48)
- ◻ Def. resource constrained shortest paths (RCSP): cyclic networks, labels ≈ states, data $(i, s, V, \text{done})$ (HW 52)
- ◻ Algorithm: RCSP labelling algorithm, steps (1)–(6) (HW 53)
- ◻ Def. label dominance; Rem. remove dominated labels (exponential growth otherwise) (HW 53)
- ◻ Rem. with no resources, reduces to **Dijkstra's algorithm** (HW 52, 53) ↔ Ch 4 Graph theory (MATH1061) and Ch 91 Algorithms (MATH2504), if Dijkstra is there
- ◻ Rem. RCSP with accumulating resources; Ex. public-transport journey with < N changes and < \$M; Def. four requirements (feasible decisions, label update, dominance, processing order) (HW 54)
- ◻ Rem. **A\* search**: labels $(c^*_l, c_l, r_l, i_l, \text{path}_l)$ with a lower-bound estimate (HW 54) ↔ Ch 91

---

## Ch 70 Metaheuristics (`ch:metaheuristics`)

### 70.1 Why heuristics: complexity
- ◻ Rem. exact LP/IP/DP vs problems not solvable in reasonable time (HW 55)
- ◻ Def. P, NP, NP-hard; P vs NP as a Millennium Prize problem; exact vs heuristic algorithms (HW 56) [NP definition flagged] ↔ Ch 91 Algorithms and Data Structures (MATH2504), if complexity is covered there
- ◻ Def. setting: optimisation problem with a large finite number of feasible solutions (HW 55, sentence unfinished)

### 70.2 Local search ingredients
- ◻ Def. heuristic algorithms require an initial solution, a neighbourhood and a rule for picking a neighbour (HW 56) ["initial algorithm" flagged]

### 70.3 Simulated annealing
- ◻ Algorithm: simulated annealing pseudocode with best-so-far tracking, acceptance $\exp((e - e')/T\alpha^k)$ against `random()` (HW 57) [two items flagged] ↔ Ch 64 (stochastic/derivative-free optimisation, MATH3204) and Ch 37 (uniform random numbers)
- ◻ Ex. travelling salesman, six cities, swap neighbourhood $1,2,5,4,3,6 \to 1,2,3,4,5,6$ (HW 57) — **Figure** (six cities on a hexagon)

### 70.4 Other metaheuristics
- ◻ Genetic algorithms; "Misc. (see PowerPoint)" (HW 55): **named only, no content in the notes.** The chapter will be very short unless the slides are supplied.

---

## Figures (for TikZ)
1. Branch-and-bound tree for Telfa (HW 26; implied by the indented list, not drawn in the notes).
2. Noughts-and-crosses board with squares numbered 0–8 (HW 31).
3. Decision tree for the racing problem, values in brackets (HW 73).
4. Six TSP cities on a hexagon (HW 57).
5. Sensitivity margin bracket on HW 20 (annotation, not a figure; no TikZ needed).
No other page has a figure.

## Overlaps with other courses (↔ merge)
- **Ch 63 Constrained Optimisation and Duality (MATH3204):** LP duality, weak/strong duality, complementary slackness, dual variables as sensitivities (67.5–67.6).
- **Ch 61 Convex Analysis (MATH3204):** convexity of the piecewise cost (HW 30), one remark.
- **Ch 64 Non-Smooth, Stochastic and Derivative-Free Optimisation (MATH3204):** simulated annealing (70.3), if MATH3204 covers it.
- **Ch 66 Optimal Control (MATH3404)** and **Ch 84 Reinforcement Learning (STAT3007):** Bellman equation, stochastic DP / MDPs (69.1, 69.3).
- **Ch 34 Discrete-Time Markov Chains (STAT2003, STAT3004):** transition probabilities in stochastic DP (light).
- **Ch 4 Graph Theory (MATH1061)** and **Ch 91 Algorithms and Data Structures (MATH2504):** Dijkstra, A\*, shortest paths, P/NP (69.4, 70.1).
- **Ch 6 Vectors, Matrices and Linear Systems (MATH1071):** matrix inverse and partitioned matrices used in the RSA; total unimodularity (HW 32) is new.
- **Ch 46 Linear Models and Regression (STAT2004, STAT1301):** LAD line fitting as an LP (HW 25), cross-reference only.
- No overlap with written Chapters 25–31.

## Suspected errors in the notes
1. HW 02: "integer programming, a subtype of linear programming … simplex method" — the simplex method solves the LP relaxation; integer programs need branch and bound (HW 26).
2. HW 03: nutrient constraints sum over $n \in N$; should be $\sum_{f\in F} a_{nf}x_f \ge \alpha_n$ (and $\le \beta_n$) for each $n$.
3. HW 04: WordLock refinement $\le 3y_{(\cdot)}$; the constant 3 excludes the word without forcing letters off dials when $y = 0$.
4. HW 07: "linearly independent variables" — the columns of $\mat A$ indexed by $S$ are linearly independent.
5. HW 13: "$c_5 = 1$" should be $c'_5 = 1$ (typo).
6. HW 15: Dual (−) constraint should be $-\mat A\T\vect y \le -\vect c$. Also the "dual of the dual" (HW 15), weak duality (HW 16), strong duality (HW 17) and complementary slackness (HW 19) are labelled "Def." but are theorems.
7. HW 16: last step of the alternative proof uses the primal constraint, not the dual one; the first proof needs $\vect x, \vect y \ge \vect 0$ (unstated).
8. HW 17: "unbounded ⇒ other infeasible" follows from weak duality, not from the equality stated.
9. HW 20: non-basic optimality condition uses $c_j$ instead of the perturbed $c_j + \Delta$; "$< 0$" vs "$\le 0$" (HW 09).
10. HW 22: production constraints should be $x_n \le a_n$ for $n \in G$ and $x_n = 0$ for $n \notin G$.
11. HW 23: "MaxVeg, MinVeg" should be "MaxVeg, MaxNonVeg" (HW 24 uses MaxNonVeg).
12. HW 25: $b_1x_1$ should be $b_1x_i$.
13. HW 26: LP relaxation value is $z = 41.25$, not $47.25$.
14. HW 27: set-covering constraint should be $\sum_{i\in n_c} x_i \ge 1$.
15. HW 30: "from $z_2$": $y_1 \ge 500z_2$ (subscript overwritten); "from $z_3$": $y_2 \ge 500z_3$ (written $500z_2$).
16. HW 32: total unimodularity means every square sub-matrix has determinant $0$ or $\pm1$, not "determinant $\pm1$".
17. HW 44: "$x_t, \dots, x_0$" should be "$x_t, \dots, x_3$".
18. HW 48: titled "Stochastic DP" but deterministic.
19. HW 56: NP described as "objective can be evaluated in polynomial [time]" (verification of solutions is meant); "initial algorithm" should be "initial solution".
20. HW 57: best-so-far update should store $s', e'$; the formula called temp$(e)$ is the acceptance probability with temperature $T\alpha^k$.
21. HW 64: "more than 0.2" and "at least $\tfrac15$" disagree at the boundary.
22. HW 71: chain-store linking constraint should sum over $S^c$.
23. HW 78: base-case labels "if True"/"if False" are swapped.

All numerical worked examples were recomputed: Giapetto RSA (HW 11–13), Telfa branches (HW 26, except item 13), chess (HW 46), betting (HW 47), Exam I Q1 (HW 58–65), racing (HW 73) and soil (HW 79) are correct.

## Notation the book doesn't have yet
| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\Znn` | $\Z_{\ge 0}$ | non-negative integers | The notes write $\Z^+$ for integer variables that may be 0 (HW 01, 44). STYLE.md uses $\R^{+}$ for positive reals, so $\Z^+$ would read as $\{1, 2, \dots\}$ (= $\N$). Needs one convention. |
| `\cpP`, `\cpNP` | $\mathrm{P}$, $\mathrm{NP}$ | complexity classes | HW 56. Upright to avoid clashing with $\Prob$ and with a variable $P$. |
| (decision) | $\vect x^B$, $\vect x^N$, $\mat B$, $\mat N$, $\vect c^B$ | basic / non-basic parts | Superscripts $B$, $N$ (HW 07). $\mat N$ clashes with $\N$ only visually; propose keeping the notes' form. |
| (decision) | $\vect p^j$, $\vect\alpha^j$, $\vect e^j$ | column $j$ of $\mat A$, direction, unit vector | The notes index columns by **superscripts** ($\vect p^{j^*}$, $\vect e^j$; HW 08, 20, 64). If the book writes unit vectors as $\vect e_j$ elsewhere, convert. |
| (decision) | $c'_j$ | reduced cost | HW 09; fine as is unless MATH3204 uses $\bar c_j$. |
| (decision) | $A^{\to}_n$, $A^{\leftarrow}_n$ | arcs leaving / entering node $n$ | HW 48 (also $f_a$, $t_a$ for from/to nodes, HW 22, 39). Graph-theory chapter (MATH1061) may already fix a convention. |
| (decision) | $s^M(s_t, a_t, \omega_t)$, $C_t$, $V_t$ | DP transition, contribution, value | HW 41, 51. Should match Ch 66/84 if those use the Bellman equation. |

## Code in the notes
- **None as runnable code.** HW 57 has simulated-annealing **pseudocode** (Python-like: `for k in {1, …, k_max}`, `random-neighbour(s)`, `random()`); it maps directly to a Python snippet for Ch 70's computing section.
- HW 03 says the subsistence problem "was solved in Gurobi" (the practicals used a solver; no code or language is recorded). Part V is Python, so a `gurobipy` or `scipy.optimize.linprog` / `milp` version would be new material: not to be added in this phase.

## Not in the notes (for the hub's information)
- Lecture slides ("PowerPoint", HW 55): genetic algorithms and other metaheuristics.
- The statements of the named exam examples ('Smart Minds Chess School', 'BMC', 'Grid Ball', 'Running', 'Farmer', 'Electrigrid' in DP form) and of the practicals' numeric data.
- Tableau simplex, phase I / big-M for finding an initial BFS, degeneracy/cycling rules, and a general branch-and-bound statement: none are in the notes.
