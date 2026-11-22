# MATH3202 Operations Research & Mathematical Planning: transcription, part 1 of 2 (HW 01–40)

_Transcription phase. Nothing here is book text yet. No dates are recorded: the past-exam headings on HW 58–80 give exam years, which are replaced by "Past exam I/II/III"; the photo file names are camera timestamps and are kept only as file identifiers._

## Sources (both parts)
| Code | Source | Role | Where transcribed |
|---|---|---|---|
| **HW nn** | 80 photos of the handwritten notes (`math3202.zip`), one notebook page per photo, numbered in shooting order (file name under each heading). HW 75 and HW 76 are two shots of the same page, so there are **79 distinct pages**. | **Only source** | Part 1: HW 01–40 (linear and integer programming). Part 2: HW 41–80 (dynamic programming, shortest paths, metaheuristics, past exams). |

No typed notes or slides were supplied. The notes mention lecture "PowerPoint" slides (HW 55), Gurobi (HW 03), the practicals (Practical 2–4) and named exam examples ('Smart Minds Chess School', 'BMC', 'Grid Ball', 'Running', 'Farmer'), none of which is included.

**Topics by page.** LP models HW 01–05; standard form and BFS 05–08; revised simplex 09–13; duality 14–19, 21; sensitivity 20; practicals 22–24, 29; LP modelling tips 25; integer programming (branch and bound, binary modelling, assignment and network models) 26–28, 30–39; dynamic programming 40–51; resource constrained shortest paths 52–54; metaheuristics and complexity 55–57; past exams 58–80.

## Legibility check (all 80 photos)
All photos were read in order at full resolution (4000 × 3000, rotated upright); every doubtful spot was re-checked on a zoomed crop. Every photo has a broad diagonal shadow, but the ink is readable through it everywhere; none is blurred or too dark.

**Retake needed (1):**
- **HW 20 (`20261122_004854.jpg`)**, Sensitivity analysis: the right edge of the page is cut off. The margin note at the bottom right runs off the photo: only "…, $\vect y \ge \vect 0$ ho" is visible (presumably "holds", not assumed). Retake with the full right margin.

**Duplicate (no action needed):** HW 75 (`20261122_005435(0).jpg`) and HW 76 (`20261122_005435.jpg`) are the same page (Past exam III Q2b), both fully legible.

**Unreadable content that is in the notebook itself** (hatched or blacked-out cross-outs; a retake won't help, and in every case the replacement or surrounding text is clear): HW 05 (blot before "$\ge 0$"), 25 (word before the first "Min."), 26 (text before "$z = 47.25$"), 27 (whole boxed block and a title word crossed out; partly readable, see the page), 33 (blot before $\Lambda_a$), 37 (word before "$t \in T$"), 38 (boxed data line, a word, a symbol), 41 (characters before $C_t(s_t, a_t)$), 43 (symbol under $p_{t,(a_t)}$), 49 (blot after "1"), 52 (blot after "extend"), 57 (exponent of $\alpha$, "k" written above), 60 (blot before $c'_j$), 68 (blot under $a_t$), 71 (blots in the first constraint; a cross-hatched box), 77 (two blots), 78 (word before $m_s$).

**Genuinely ambiguous glyphs** (in the notebook; resolved in brackets where they occur): HW 05 the "=" before 40 is faint (looks like "−"); HW 30 a subscript written as 1 and 2 on top of each other; HW 44 the data vector letter ($w$ vs $u$) and an overwritten digit; HW 47 the "4" in $V_4$ written over another digit; HW 48 "1280" (middle digit could be 3); HW 73 "$V_z(3)$" (correction, $V_3$ meant); HW 75 "$x_{p,a}$" (the $a$ can look like $c$); HW 80 the letter $f$ looks like "3" in the base case.

## Conventions
Wording, structure and labels (Def., Thm., P. = proof, Ex., Rem., N. = note, Q. = question) follow the notes; most pages are modelling examples laid out under the headings Sets / Data / Variables / Objective / Constraints (LP, IP) or Stages / State / Action / Transition / Contribution / Value function / Base / Obj (DP), which are kept. "↳" marks the notes' hooked-arrow bullets. Maths uses `notation.tex` macros: underlined vectors in the notes are written `\vect`, matrices `\mat`, transposes `\T`. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic re-computed where marked "Checked"); "[blot]", "[hatched]" mark crossed-out text. Figures are described in enough detail to redraw in TikZ; only four pages have figures (HW 26 implied tree, 31, 57, 73).

**This part:** linear programming (models, standard form, basic feasible solutions, the revised simplex algorithm, duality, complementary slackness, sensitivity) and integer programming (branch and bound, binary and big-M modelling, assignment and network models), plus the opening dynamic programming page (HW 40).

---

### HW 01 (`20261122_004720.jpg`): An introduction to linear programming

**An introduction to linear programming**

**Ex.** Farmer Jones' problem

<u>Sets</u>
$$C = \{\text{chocolate}, \text{plain}\}, \qquad I = \{\text{eggs}, \text{time}, \text{milk}\}$$

<u>Data</u>
- $a_i$ = Availability of ingredient $i \in I$
- $p_c$ = Price of cake $c \in C$
- $u_{ic}$ = Amount of ingredient $i \in I$, in cake $c \in C$.

<u>Vars</u>
↳ short for <u>Variables</u>, or <u>Decision Variables</u>
- $x_c$ = Number of cakes $c \in C$ to bake

<u>Objective</u>
↳ maximise profit $= \sum_{c \in C} p_c x_c$ subject to constraints.

<u>Constraints</u>
↳
$$\sum_{c\in C} u_{ic} x_c \le a_i, \quad \forall i \in I \qquad\qquad x_c \in \Z^+, \quad \forall c \in C$$
A double arrow ⇑ points up at "$x_c \in \Z^+$" from the note "Answer restricted to integers!"

["$\Z^+$" is written as a blackboard Z with superscript +. The objective is called "profit" here and "Revenue" on HW 02.]

*Figure:* none.

---

### HW 02 (`20261122_004724.jpg`): Introduction to linear programming: Farmer Jones

**Introduction to linear programming: Farmer Jones**

**Ex.** Adding values to the problem

<u>Data</u>
- $a_i$ : 30 eggs, 480 min., 5L
- $p_c$ : \$4, \$2
- $u_{ic}$ : [two columns, chocolate on the left, plain on the right, separated by "vs."]

| | chocolate | | plain |
|---|---|---|---|
| eggs | 4 eggs | vs. | 1 egg |
| time | 20 min. | | 50 min. |
| milk | 0.25 L | | 0.2 L |

[The row labels eggs/time/milk are not written; the order of the numbers is eggs, time, milk in both columns. The left column is chocolate and the right plain, as the constraints below confirm.]

<u>Constraints</u>
↳
$$
\begin{aligned}
\text{Eggs:}\quad & 4x_{\text{choc}} + x_{\text{plain}} \le 30\\
\text{Milk:}\quad & 0.25x_{\text{choc}} + 0.2x_{\text{plain}} \le 5\\
\text{Time:}\quad & 20x_{\text{choc}} + 50x_{\text{plain}} \le 480
\end{aligned}
$$

<u>Objective</u>
↳ Revenue $= \sum_{c\in C} p_c x_c = 4x_{\text{choc}} + 2x_{\text{plain}}$

**N.** This problem is a type of integer programming, a subtype of linear programming.
We use the <u>simplex</u> method to solve this problem.

[possible error: integer programming is usually described as linear programming with an integrality restriction (the LP relaxation drops it), and the simplex method alone solves the LP relaxation, not the integer problem; the notes' later pages (HW 44 onwards: branch and bound) treat integer programs separately. Recorded as written.]

*Figure:* none.

---

### HW 03 (`20261122_004729.jpg`): Introduction to linear programming: subsistence

**Introduction to linear programming: subsistence**

**Ex.** The cost of subsistence problem

<u>Sets</u>
$$F = \{\text{almonds}, \dots, \text{white rice}\} \ \text{; 30}, \qquad N = \{\text{energy}, \dots, \text{sodium}\} \ \text{; 13}$$
[Margin notes: $F$ has 30 foods, $N$ has 13 nutrients.]

<u>Data</u>
- $p_f$ = Price of food $\in F$ per 100g
- $a_{nf}$ = Amount of nutrients $\in N$ per 100g of food $\in F$
- $\alpha_n$ = Amount of nutrients $\in N$, min.
- $\beta_n$ = Amount of nutrients $\in N$, max.

<u>Variables</u> $x_f$ = Amount of food $\in F$ to consume

<u>Objective</u>
↳ minimise price $= \sum_{f\in F} p_f x_f$ subject to constraints.

<u>Constraints</u>
↳
$$\left.\begin{aligned} \sum_{n\in N} a_{nf} x_f &\ge \alpha_n\\ \sum_{n\in N} a_{nf} x_f &\le \beta_n \end{aligned}\right\}\ \begin{aligned}&\text{if no max. for nutrients}\\ &\text{if max.}\end{aligned}$$

This problem was solved in Gurobi.

[possible error: the sums should run over foods, $\sum_{f\in F} a_{nf}x_f \ge \alpha_n$ (and $\le \beta_n$) for each $n \in N$; as written they sum over $n$ with $f$ free. The margin text by the brace reads "if no max. for nutrients / if max.": the $\le \beta_n$ constraint applies only to nutrients that have a maximum. No non-negativity constraint is written.]

*Figure:* none.

---

### HW 04 (`20261122_004734.jpg`): Linear programming: WordLock

**Linear programming: WordLock**

**Ex.** Is WordLock maximally efficient?

<u>Sets</u>
- $L = \{A, B, \dots, Z\}$ ; 26 letters
- $W = \{\text{ABET}, \dots, \text{ZOOM}\}$ ; 1537 four letter [words]
- $D = \{0, 1, 2, 3\}$ ; 4 dials

<u>Data</u> Dictionary of words

<u>Variables</u>
$$x_{dl} = \begin{cases} 1 & \text{if } l \text{ is on dial } d \in D\\ 0 & \text{if not}\end{cases}
\qquad
y_w = \begin{cases} 1 & \text{if } w \in W \text{ can be spelled}\\ 0 & \text{if not}\end{cases}$$
[Above the $l$ in "if $l$ is on dial" is written "$l \in L$" vertically (L, then a rotated ∈).]

<u>Objective</u>
↳ ~~minimise~~ Maximise number of words $\sum_{w\in W} y_w$ subject to constraints
["minimise" is struck through.]

<u>Constraints</u>
↳
$$\sum_{l\in L} x_{dl} = 10 \quad ; \text{10 letters per dial} \in D$$
$$x_{0A} + x_{1B} + x_{2E} + x_{3T} \ge 4y_{(\text{ABET})}$$
$$\vdots \quad ; \text{for each word}$$

<u>Refine</u>
↳
$$x_{0F} + x_{1U} + x_{2C} + x_{3K} \le 3y_{(\text{FUCK})}$$
to remove 'FUCK'

[possible error: the refining constraint has $3y_{(\cdot)}$ on the right; to forbid the word whatever $y$ is, the right-hand side would be the constant 3 (with $y = 1$, as written, it does exclude the word, but with $y = 0$ it also forces all four letters off their dials, which over-restricts). Recorded as written. The "1537" count and the letter/word data are not given beyond this page.]

*Figure:* none.

---

### HW 05 (`20261122_004740.jpg`): Linear programming: woodcarving

**Linear programming: woodcarving**

**Ex.** Giapetto's woodcarving

- $x_1$: number of soldiers / week
- $x_2$: number of trains / week

We maximise $z = 3x_1 + 2x_2$ subject to:
$$
\begin{aligned}
2x_1 + x_2 &\le 100 && \text{; finishing}\\
x_1 + x_2 &\le 80 && \text{; carpentry}\\
x_1 &\le 40 && \text{; max. soldiers}\\
x_1, x_2 &\ge 0
\end{aligned}
$$
[A small blot before the last "$\ge$"; reads correctly without it. "Giapetto" as spelled in the notes.]

**Ex.** Giapetto in standard form

We add slack variables:
Maximise $z = 3x_1 + 2x_2$ subject to:
$$
\begin{aligned}
2x_1 + x_2 + x_3 &= 100\\
x_1 + x_2 + x_4 &= 80\\
x_1 + x_5 &= 40\\
x_1, x_2, x_3, x_4, x_5 &\ge 0
\end{aligned}
$$
[The "=" before 40 is faint (its upper bar is barely visible, so it can look like "−"); read as "=". "slach" as written.]

*Figure:* none.

---

### HW 06 (`20261122_004743.jpg`): Standard form of linear programming

**Standard form of linear programming**

**Def.** We find $\vect x$ that maximises $z = \vect c\T \vect x$ subject to:
- ↳ $\mat A\vect x \le \vect b \Rightarrow \mat A\vect x = \vect b$
- ↳ $\vect x \ge \vect 0$

where:
- ↳ $\vect c, \vect x$ are vectors of size $n$ (the number of variables)
- ↳ $\vect b$ is a vector of size $m$ (the number of constraints)

[Vectors are underlined in the notes ($\underline{x}$, $\underline{c}$, $\underline{b}$); transcribed with `\vect`. Matrices ($A$, later $B$, $N$) are not underlined; transcribed with `\mat` for consistency with `notation.tex`. "$\mat A\vect x \le \vect b \Rightarrow \mat A\vect x = \vect b$" means the inequality form is converted to the equality form by slack variables (next remark).]

**Rem.** To turn the constraint inequality to an equality, we introduce slack variables:
- ↳ $\vect a\T\vect x \le b \Rightarrow \vect a\T\vect x + s = b$
- ↳ $\vect a\T\vect x \ge b \Rightarrow \vect a\T\vect x - s = b$

$\quad, \ s \ge 0$

**Rem.** If we want to minimise $z = \vect c\T\vect x$, simply maximise $-\vect c\T\vect x$.

**Improving on a basic feasible solution**
[A second heading, mid-page. This part uses notation defined on HW 07–08.]

**Def.** For the objective value to increase, we need $j^*$ so that $(c_{j^*} - \vect y\T\vect p^{j^*}) > 0$.

To improve the basic feasible solution, we:
- ↳ Increase $x_{j^*}$ by $\lambda$ until one of the basic variables (e.g. $x_r$) becomes 0.
- ↳ Replace $x_r$ by $x_{j^*}$ in the basis.
- ↳ Repeat.

[A pale blue rectangle covers the bottom-left corner of the photo (beside the last list); it is outside the writing and hides nothing. The $\vect y$ in $\vect y\T\vect p^{j^*}$ is not underlined here but is a vector (defined on HW 08 as $\vect y = (\mat B^{-1})\T\vect c^B$).]

*Figure:* none.

---

### HW 07 (`20261122_004749.jpg`): Basic feasible solution

**Basic feasible solution**

**Def.** Assume we have a set of $m$ linearly independent variables $S = \{i_1, i_2, \dots, i_m\}$.
$S$ usually corresponds to the slack variables.

Let $\mat B$ be the invertible $m\times m$ sub-matrix of $\mat A$ corresponding to the columns of variables in $S$. $\mat B$ is the basis.

We denote basic variables ($\vect x^B$) as the variables corresponding to $S$ (and $\mat B$).

The other variables are non-basic, and are all zero. Their columns in $\mat A$ can be denoted as $\mat N$, with non-basic variables denoted by $\vect x^N$.

[possible error: "linearly independent variables" — it is the columns of $\mat A$ indexed by $S$ that are linearly independent (which is what makes $\mat B$ invertible).]

**Def.** Therefore,
- ↳ we maximise $z = \begin{bmatrix}\vect c^B\\ \vect c^N\end{bmatrix}\T \begin{bmatrix}\vect x^B\\ \vect x^N\end{bmatrix}$
- ↳ subject to: $[\mat B \mid \mat N]\begin{bmatrix}\vect x^B\\ \vect x^N\end{bmatrix} = \vect b$

Since $\vect x^N = \vect 0$,
$$\Rightarrow \mat B\vect x^B = \vect b \Rightarrow \vect x^B = \mat B^{-1}\vect b.$$

If $\mat B$ is invertible and $\vect x^B \ge \vect 0$, we have a basic feasible solution.

The objective can be calculated by:
$$z^B = (\vect c^B)\T\vect x^B = (\vect c^B)\T\mat B^{-1}\vect b$$
[The $z$ in $z^B$ is double-underlined/bold in the notes. The superscripts $B$, $N$ are written as plain capitals.]

*Figure:* none.

---

### HW 08 (`20261122_004753.jpg`): BFS: what if a non-basic variable increases?

**BFS: what if a non-basic variable increases?**

**Def.** Consider the non-basic variable $x_{j^*}$.
What if $x_{j^*}$ is increased to $\lambda$?

Let $\vect p^{j^*}$ be the column of $\mat A$ corresponding to $x_{j^*}$.

We calculate $\vect\alpha^{j^*}$ — the amount by which the basic variables need to change such that the solution remains feasible, for every unit change in $x_{j^*}$.

Therefore,
$$
\begin{aligned}
\mat A\vect x = \vect b
&\Rightarrow [\mat B\ \ \vect p^{j^*}]\begin{bmatrix}\vect x^B - \lambda\vect\alpha^{j^*}\\ \lambda\end{bmatrix} = \vect b\\
&\Rightarrow \mat B\vect x^B - \lambda\mat B\vect\alpha^{j^*} + \lambda\vect p^{j^*} = \vect b\\
&\Rightarrow \vect b + \lambda(-\mat B\vect\alpha^{j^*} + \vect p^{j^*}) = \vect b\\
&\Rightarrow \mat B\vect\alpha^{j^*} = \vect p^{j^*} \Rightarrow \vect\alpha^{j^*} = \mat B^{-1}\vect p^{j^*}
\end{aligned}
$$
[The symbol written $\underline{\alpha}^{j^*}$ is an underlined alpha (it can look like "a" or "d"); read as $\vect\alpha^{j^*}$.]

Let $\vect y = (\mat B^{-1})\T\vect c^B$. Thus,
$$
\begin{aligned}
z &= \begin{bmatrix}\vect c^B\\ c_{j^*}\end{bmatrix}\T\begin{bmatrix}\vect x^B - \lambda\vect\alpha^{j^*}\\ \lambda\end{bmatrix}\\
&= \vect c^{B\top}\vect x^B - \lambda\vect c^{B\top}\vect\alpha^{j^*} + \lambda c_{j^*}\\
&= z^B - \lambda\vect c^{B\top}(\mat B^{-1}\vect p^{j^*}) + \lambda c_{j^*}\\
&= z^B - \lambda\vect y\T\vect p^{j^*} + \lambda c_{j^*}\\
&= z^B + \lambda(c_{j^*} - \vect y\T\vect p^{j^*})
\end{aligned}
$$
[In the first line of $z$ the transpose sign is missing (written $\begin{bmatrix}\vect c^B\\ c_{j^*}\end{bmatrix}\begin{bmatrix}\cdots\end{bmatrix}$); the next line shows the transpose is meant. Checked: the algebra is correct.]

**Rem.** To increase $z$, we need $j^*$ such that $(c_{j^*} - \vect y\T\vect p^{j^*}) > 0$.

*Figure:* none.

---

### HW 09 (`20261122_004758.jpg`): The revised simplex algorithm (1)

**The revised simplex algorithm**

**Initialisation:**
- ↳ Given an initial set of basic variables $S$, with basis $\mat B$, from $\mat B^{-1}$ calculate $\vect x^B$ and $z^B$.
  - ↳↳ We usually set $S$ as the slack variables, so that $\mat B = \mat B^{-1} = \mat I$.

**Step 1: Price:**
- ↳ Determine the entering variable $x_{j^*}$ with column in $\mat A$ of $\vect p^{j^*}$.
  - ↳↳ Compute the dual variables $\vect y = (\mat B^{-1})\T\vect c^B$ (or alternatively, $\vect y\T = (\vect c^B)\T\mat B^{-1}$)
  - ↳↳ Compute the 'reduced cost': $c'_j = c_j - \vect y\T\vect p^j$
  - ↳↳ Choose $j^*$ such that $c'_{j^*} > 0$. Choose the most positive $j^*$.
  - ↳↳ If there are no $c'_{j^*} > 0$, then stop with the optimal solution.

**Step 2: Ratio test:**
- ↳ Determine the leaving variable $x_r$ with associated column in $\mat A$ of $\vect p^r$.
  - ↳↳ Compute the direction in which $\vect\alpha^{j^*} = \mat B^{-1}\vect p^{j^*}$. As we increase $x_{j^*}$, then the other variables reduce by $\vect\alpha^{j^*}$.
  - ↳↳ Choose $x_r$ which achieves
    $$\theta = \min_{k\in S}\Bigl\{\frac{x^B_k}{\alpha^{j^*}_k} : \alpha^{j^*}_k > 0\Bigr\}$$
  - ↳↳ If there are no $x_r$, then stop with an unbounded solution.

["Choose the most positive $j^*$" means the $j^*$ with the most positive reduced cost. "the other variables reduce by $\vect\alpha^{j^*}$" means by $\vect\alpha^{j^*}$ per unit increase (HW 08).]

*Figure:* none.

---

### HW 10 (`20261122_004801.jpg`): The revised simplex algorithm (2)

**The revised simplex algorithm**

**Step 3: Update:**
- ↳ Let $S = S \cup \{j^*\} \setminus \{r\}$
- ↳ From the new basis $\mat B$, calculate $\mat B^{-1}$, $\vect x^B = \mat B^{-1}\vect b$ and $z^B = (\vect c^B)\T\vect x^B$
- ↳ Repeat from Step 1.

[The rest of the page is blank. This photo has the lowest sharpness score of the first batch because most of it is empty paper; the writing is sharp.]

*Figure:* none.

---

### HW 11 (`20261122_004806.jpg`): The revised simplex algorithm: Giapetto (1)

**The revised simplex algorithm: Giapetto**

**Ex.** Consider Giapetto's woodworking problem:
We maximise $z = 3x_1 + 2x_2$ subject to
$$
\begin{aligned}
2x_1 + x_2 + x_3 &= 100\\
x_1 + x_2 + x_4 &= 80\\
x_1 + x_5 &= 40\\
x_1, x_2, x_3, x_4, x_5 &\ge 0
\end{aligned}
$$

Therefore,
- ↳ $\mat A = \begin{bmatrix} 2 & 1 & 1 & 0 & 0\\ 1 & 1 & 0 & 1 & 0\\ 1 & 0 & 0 & 0 & 1\end{bmatrix}$ [an overbrace labelled "$B$" spans the last three columns]
- ↳ $\vect b = \begin{pmatrix}100\\80\\40\end{pmatrix}$, $\quad \vect c = (3, 2, \underbrace{0, 0, 0}_{(\vect c^B)\T})\T$
- ↳ $S = \{3, 4, 5\}$
- ↳ $\vect x^B = \begin{pmatrix}100\\80\\40\end{pmatrix} \Rightarrow z^B = 0.$

**Iteration 1:** $S = \{3,4,5\}$
- (1) Price:
  - (a) Compute $\vect y = (\mat B^{-1})\T\vect c^B = (0,0,0)$
  - (b) Reduced costs: $c'_j = c_j - \vect y\T\vect p^j$
    ↳ $c'_1 = 3$, $c'_2 = 2$
  - (c) Entering variable is $x_1$, $\vect p_1 = (2,1,1)\T$
- (2) Ratio:
  - (a) $\vect\alpha^1 = \mat B^{-1}\vect p^1 = (2,1,1)\T$
  - (b) $\vect x^B = (100, 80, 40)\T$
    $\theta = \min_{k\in S}\{x^B_k/\alpha^{j^*}_k : \alpha^{j^*}_k > 0\} = 40$
    $\Rightarrow$ Exiting variable is $x_5$.
- (3) Update [continued on HW 12]

[The column is written $\vect p_1$ (subscript) in (c) and $\vect p^1$ (superscript) in (a); same object. Checked: $\theta = \min\{100/2, 80/1, 40/1\} = 40$, attained by $x_5$.]

*Figure:* none.

---

### HW 12 (`20261122_004809.jpg`): The revised simplex algorithm: Giapetto (2)

**The revised simplex algorithm: Giapetto**

**Ex.** Iteration 1:
- (3) Update:
  $S = \{1,3,4\}$, $\mat B = \begin{bmatrix}2&1&0\\1&0&1\\1&0&0\end{bmatrix}$,
  $\mat B^{-1} = \begin{bmatrix}0&0&1\\1&0&-2\\0&1&-1\end{bmatrix}$, $\vect x^B = \begin{pmatrix}40\\20\\40\end{pmatrix}$, $z^B = 120$

**Iteration 2:** $S = \{1,3,4\}$
- (1) Price:
  - (a) Compute $\vect y\T = \vect c^{B\top}\mat B^{-1} = (3,0,0)\begin{pmatrix}0&0&1\\1&0&-2\\0&1&-1\end{pmatrix} = (0,0,3)$
  - (b) Reduced costs: $c'_j = c_j - \vect y\T\vect p^j$
    ↳ $c'_2 = 2$, $c'_5 = -3$
  - (c) Entering variable is $x_2$, $\vect p_2 = (1,1,0)\T$
- (2) Ratio:
  - (a) $\vect\alpha^2 = \mat B^{-1}\vect p^2 = \cdots = (0,1,1)\T$
  - (b) $\vect x^B = (40, 20, 40)\T$
    $\theta = \min_{k\in S}\{x^B_k/\alpha^{j^*}_k : \alpha^{j^*}_k > 0\} = 20$
    $\Rightarrow$ Exiting variable is $x_3$.
- (3) Update:
  $S = \{1,2,4\}$, $\mat B = \begin{bmatrix}2&1&0\\1&1&1\\1&0&0\end{bmatrix}$,
  $\mat B^{-1} = \begin{bmatrix}0&0&1\\1&0&-2\\-1&1&1\end{bmatrix}$, $\vect x^B = \begin{pmatrix}40\\20\\20\end{pmatrix}$, $z^B = (160)$

[Checked: both $\mat B^{-1}$ are correct (computed), as are $\vect x^B$, $z^B$, $\vect y$, the reduced costs, $\vect\alpha^2$ and $\theta$. The basic variables are listed in the order of $S$. $z^B = 160$ is written in round brackets.]

*Figure:* none.

---

### HW 13 (`20261122_004815.jpg`): The revised simplex algorithm: Giapetto (3)

**The revised simplex algorithm: Giapetto**

**Ex.** Iteration 3: $S = \{1,2,4\}$
- (1) Price:
  - (a) Compute $\vect y\T = (\vect c^B)\T\mat B^{-1} = \cdots = (2, 0, -1)$
  - (b) Reduced costs: $c'_j = c_j - \vect y\T\vect p^j$.
    ↳ $c'_3 = -2$, $c_5 = 1$
  - (c) Entering variable is $x_5$, $\vect p_5 = (0,0,1)\T$
- (2) Ratio:
  - (a) $\vect\alpha^5 = \mat B^{-1}\vect p^5 = (1,-2,1)\T$
  - (b) $\vect x^B = (40,20,20)\T$
    $\theta = \min_{k\in S}\{x^B_k/\alpha^{j^*}_k : \alpha^{j^*}_k > 0\} = 20$
    $\Rightarrow$ Exiting variable is $x_4$.
- (3) Update:
  $S = \{1,2,5\}$, $\mat B = \begin{bmatrix}2&1&0\\1&1&0\\1&0&1\end{bmatrix}$,
  $\mat B^{-1} = \begin{bmatrix}1&-1&0\\-1&2&0\\-1&1&1\end{bmatrix}$, $\vect x^B = \begin{pmatrix}20\\60\\20\end{pmatrix}$, $z^B = 180$

**Iteration 4:** $S = \{1,2,5\}$
- (1) Price:
  - (a) Compute $\vect y\T = (\vect c^B)\T\mat B^{-1} = \cdots = (1,1,0)$
  - (b) Reduced costs: $c'_j = c_j - \vect y\T\vect p^j$.
    ↳ $c'_3 = -1$, $c'_4 = -1$.
  - (c) No entering variable – stop.

Therefore, $x_1 = 20$, $x_2 = 60$, $z^B = 180$.

["$c_5 = 1$" is missing its prime ($c'_5 = 1$ is meant). Checked: every value on the page is correct, including $\mat B^{-1}$ and $\theta = \min\{40/1, 20/1\} = 20$ (attained by $x_4$).]

*Figure:* none.

---

### HW 14 (`20261122_004818.jpg`): Revisiting Farmer Jones

**Revisiting Farmer Jones**

**Ex.** Consider if Farmer Jones had to purchase his ingredients (eggs, milk, time).

Let
- $y_1$ : \$ / egg
- $y_2$ : \$ / minute
- $y_3$ : \$ / L milk.

We minimise $30y_1 + 480y_2 + 5y_3$ $\Big\}$ values of ingredients to purchase

subject to:
$$
\begin{aligned}
4y_1 + 20y_2 + .25y_3 &\ge 4 && \} \text{ choc}\\
y_1 + 50y_2 + .2y_3 &\ge 2 && \} \text{ plain}\\
y_1, y_2, y_3 &\ge 0
\end{aligned}
$$

This is an example of a dual problem.

[Checked against HW 02: these are the dual constraints of the Farmer Jones LP (relaxation). The lower half of the page is blank.]

*Figure:* none.

---

### HW 15 (`20261122_004823.jpg`): Duality

**Duality**

**Def.** Consider the standard form of a linear programming problem:

<u>Primal</u>: maximise $\vect c\T\vect x$ subject to $\mat A\vect x \le \vect b$, $\vect x \ge \vect 0$.

We denote the 'original' problem as the primal problem, with $\vect x$ as the primal variables.
The primal has an associated 'dual' problem, with $\vect y$ as the dual variables, denoted by:

<u>Dual</u>: minimise $\vect b\T\vect y$ subject to $\mat A\T\vect y \ge \vect c$, $\vect y \ge \vect 0$.

**Def.** The dual of the dual is the primal.
We can show this as follows:

<u>Dual (−)</u>: maximise $-\vect b\T\vect y$ subject to $-\mat A\T\vect y \ge \vect c$, $\vect y \ge \vect 0$.

<u>Dual of Dual (−)</u>: minimise $-\vect c\T\vect z$ subject to $-\mat A\vect z \ge -\vect b$, $\vect z \ge \vect 0$.

<u>Dual of Dual</u>: maximise $\vect c\T\vect z$ subject to $\mat A\vect z \le \vect b$, $\vect z \ge \vect 0$.

[possible error: in Dual (−) the constraint should be $-\mat A\T\vect y \le -\vect c$ (multiplying $\mat A\T\vect y \ge \vect c$ by $-1$ flips the inequality and negates $\vect c$); the next line is consistent with that corrected form. "The dual of the dual is the primal" is labelled "Def." but is a result.]

*Figure:* none.

---

### HW 16 (`20261122_004827.jpg`): The weak duality theorem

**The weak duality theorem**

**Def.** For each feasible solution $\vect x$ of the primal, and each feasible solution $\vect y$ of the dual,
$$\vect y\T\vect b \ge \vect x\T\vect c \iff \vect b\T\vect y \ge \vect c\T\vect x$$

In other words,
- ↳ Each feasible solution $\vect x$ of the primal, the objective value is a <u>lower-bound</u> on the objective value of the dual.
- ↳ For each feasible solution $\vect y$ of the dual, the objective value is an <u>upper-bound</u> on the objective value of the primal.

**P.** Consider the primal: $\mat A\vect x \le \vect b \Rightarrow \vect y\T\mat A\vect x \le \vect y\T\vect b$

Now consider the dual: $\mat A\T\vect y \ge \vect c \Rightarrow \vect x\T\mat A\T\vect y \ge \vect x\T\vect c$

Since $\vect y\T\mat A\vect x = \vect x\T\mat A\T\vect y$: $\quad \vect y\T\vect b \ge \cdots \ge \vect x\T\vect c$. $\square$

**P.** An alternative proof is given here.
$$
\begin{aligned}
\vect c\T\vect x &= \vect x\T\vect c && \text{(since it is a scalar product)}\\
&\le \vect x\T(\mat A\T\vect y) && \text{(by dual constraint, } \vect x \ge \vect 0)\\
&= (\mat A\vect x)\T\vect y && \text{(transpose property)}\\
&\le \vect b\T\vect y && \text{(by dual constraint, } \vect y \ge \vect 0) \qquad \square
\end{aligned}
$$

[The theorem is labelled "Def." (the heading calls it a theorem). In the first proof, multiplying by $\vect y\T$ and $\vect x\T$ keeps the inequalities because $\vect y \ge \vect 0$ and $\vect x \ge \vect 0$; this is not said there but is said in the alternative proof. possible error: the last justification should be "by primal constraint ($\mat A\vect x \le \vect b$), $\vect y \ge \vect 0$", not "dual constraint".]

*Figure:* none.

---

### HW 17 (`20261122_004834.jpg`): The strong duality theorem

**The strong duality theorem**

**Def.** If one of either the primal or dual problems has an optimal solution, then the other also has an optimal solution. Additionally,
$$\max_{\vect x}(\vect c\T\vect x) = \min_{\vect y}(\vect b\T\vect y)$$

This implies that if the primal is unbounded (from above), then the dual has no feasible solution, and if the dual is unbounded (from below), the primal has no feasible solution.

[Labelled "Def."; it is a theorem (heading). Stated without proof on this page; HW 18 gives the argument through the revised simplex algorithm. The "unbounded ⇒ infeasible" consequence follows from weak duality (HW 16), not from the equality; recorded as written. The lower half of the page is blank.]

*Figure:* none.

---

### HW 18 (`20261122_004839.jpg`): Duality in the revised simplex algorithm

**Duality in the revised simplex algorithm**

**Def.** Recall that in the RSA, we introduced the (dual) variables $\vect y\T = \vect c^{B\top}\mat B^{-1}$.
Assuming the algorithm has terminated, we then analyse the reduced costs $c'_j = c_j - \vect y\T\vect p^j$.
Note that:
- ↳ The reduced costs of all basic variables are 0.
  $\vect c^{B\top} - \vect y\T\mat B = \vect c^{B\top} - \vect c^{B\top}\mat B^{-1}\mat B = \vect 0$
- ↳ Other reduced costs $\le 0$, since RSA terminated.
  $\vect c\T - \vect y\T\mat A \le \vect 0 \Rightarrow \mat A\T\vect y \ge \vect c$
- ↳ If $\exists j$ s.t. $y_j < 0$, the slack variable corresponding to constraint $j$ would have a positive reduced cost, and thus the RSA would not have terminated. Thus, $\vect y \ge \vect 0$.
- ↳ $\vect y\T\vect b = (\vect c^{B\top}\mat B^{-1})\vect b = \vect c^{B\top}\vect x^B = z^B$

Therefore, the revised simplex algorithm has generated feasible solutions to the primal and dual problems, which have the same objective value.

As a reminder,
- <u>Primal</u> obj: $z^B$
- <u>Dual</u> obj: $\vect y\T\vect b$

As the solutions are both equal and feasible, the solution of the revised simplex algorithm is optimal.

**Rem.** We have not proved that the RSA always terminates finitely (in finite steps, with no loop).

[RSA = revised simplex algorithm. The step "slack of constraint $j$ has reduced cost $0 - y_j$" (its column is $\vect e^j$ and its cost 0) is implicit. The "optimal" conclusion uses weak duality (HW 16), not named here.]

*Figure:* none.

---

### HW 19 (`20261122_004850.jpg`): Complementary slackness

**Complementary slackness**

**Def.** Variables in either the primal or dual problem are complementary to constraints in the other.
In other words,
$$\underbrace{\begin{aligned}&\#\text{ constraints}\\ &\#\text{ variables}\end{aligned}}_{\text{primal}} \ \begin{aligned}&=\\&=\end{aligned}\ \underbrace{\begin{aligned}&\#\text{ variables}\\ &\#\text{ constraints}\end{aligned}}_{\text{dual}}$$

A constraint has slack if it is not binding, or in other words, if the equality does not hold.
- ↳ For inequality constraints, the slack variable is positive.
- ↳ For variables constrained to be non-negative, the variable is positive.

**Def.** Assume the primal (P) has an optimal solution $\vect x^*$, and the dual (D) has an optimal solution $\vect y^*$.
- (1) If $x^*_j > 0$, then constraint $j$ in D is binding.
- (2) If $j$ in D is not binding, then $x^*_j = 0$.
- (3) If $y^*_i > 0$, then constraint $i$ in P is binding.
- (4) If $i$ in P is not binding, then $y^*_i = 0$.

i.e.
$$\text{Dual var} = 0 \Leftarrow \text{Slack} > 0, \qquad \text{Dual var} > 0 \Rightarrow \text{Slack} = 0$$

**Rem.** The name 'Complementary Slackness' is because the theorem asserts that there cannot be slack in both a constraint and the associated dual variable.

[The second "Def." is the complementary slackness theorem (the remark calls it "the theorem"); no proof is given. (2) and (4) are the contrapositives of (1) and (3).]

*Figure:* none.

---

### HW 20 (`20261122_004854.jpg`): Sensitivity analysis

**Sensitivity analysis**

**Def.** When we have the solution to a linear program, we are often interested in the sensitivity of the solution.
We ask the following questions:
- ↳ What's the impact of varying the RHS of constraints by a small amount? Over what range will this hold? (1)
- ↳ How much can the coefficients be varied (of the objective function) while keeping the optimal solution? (2)

**Rem.** The questions (1) and (2) are duals of each other.

**(1)** Let $\vect e^j$ be the zero vector, with 1 in position $j$.
Let the RHS become $\vect b + \Delta\vect e^j$.

<u>Objective</u>: $z^\Delta = \vect y^{*\top}(\vect b + \Delta\vect e^j) = \vect y^{*\top}\vect b + \vect y^{*\top}\Delta\vect e^j = z^* + \Delta y^*_j$

<u>Range</u>: $\vect x^{B\Delta} = \mat B^{-1}(\vect b + \Delta\vect e^j) = \vect x^B + \Delta\mat B^{-1}\vect e^j$

The dual variable indicates the amount by which the objective function changes, for changes in the RHS.
The range for $\Delta$ is so that $\vect x \ge \vect 0$ holds.

**(2)** Let $\vect c$ become $\vect c + \Delta\vect e^j$. For variables,

<u>Non-basic</u>: solution stays optimal while $c'_j = c_j - \vect y\T\vect p^j < 0$

<u>Basic</u>: $\vect y^\Delta = \mat B^{-1\top}(\vect c^B + \Delta\vect e^j) = \vect y + \Delta\mat B^{-1\top}\vect e^j$

*Figure (bracket arrow):* in the right margin, a vertical line joins two left-pointing arrows: the top one points at the line "…so that $\vect x \ge \vect 0$ holds", the bottom one at the line "$= \vect y + \Delta\mat B^{-1\top}\vect e^j$". Under the bottom arrow: "…, $\vect y \ge \vect 0$ ho[lds]" — **the text runs off the right edge of the photo** (only "ho" is visible). It pairs the two range conditions: $\vect x \ge \vect 0$ for (1) and $\vect y \ge \vect 0$ for (2).

[In (2) Non-basic, the condition uses the changed cost $c_j + \Delta$; the formula is written with $c_j$. In (2) Basic, "$\vect e^j$" is the unit vector in the position of $x_j$ within the basis. "$\le 0$" would match HW 09's stopping rule; the page has "$< 0$". Recorded as written.]

---

### HW 21 (`20261122_004906.jpg`): Economic interpretation of duality

**Economic interpretation of duality**

**Ex.** Consider the Farmer Jones problem:
We maximise $z = 4x_1 + 2x_2$ subject to
$$
\begin{aligned}
4x_1 + 1x_2 &\le 30 && ]\ \text{eggs } (y_1)\\
20x_1 + 50x_2 &\le 480 && ]\ \text{time } (y_2)\\
.25x_1 + .2x_2 &\le 5 && ]\ \text{milk } (y_3)\\
x_1, x_2 &\ge 0
\end{aligned}
$$

Now consider a farmer that has no ingredients, and wants to purchase the entire stock from Farmer Jones.
The farmer offers a price of $\vect y$ (a unit of ingredient $i$ for $y_i$). For the offer to be accepted by Farmer Jones, $\mat A\T\vect y \ge \vect c$, since if otherwise, Farmer Jones would rather create more profit producing cakes.

Therefore, the optimisation problem for the second farmer is:
We minimise $z = 30y_1 + 480y_2 + 5y_3$ subject to
$$
\begin{aligned}
4y_1 + 20y_2 + .25y_3 &\ge 4 && ]\ \text{chocolate } (x_1)\\
1y_1 + 50y_2 + .2y_3 &\ge 2 && ]\ \text{plain } (x_2)\\
y_1, y_2, y_3 &\ge 0
\end{aligned}
$$

The second optimisation problem is the dual of Farmer Jones' problem.

["Jonas"/"Jones" both appear; Jones is meant. Constraint order here is eggs, time, milk (HW 02 had eggs, milk, time). Checked: consistent with HW 14.]

*Figure:* none.

---

### HW 22 (`20261122_004910.jpg`): Practical 2: Electrigrid

**Practical 2: Electrigrid**

**Ex.**
<u>Sets</u>
- $N$: nodes
- $G$: generators, $G \subseteq N$
- $E$: transmission lines

<u>Data</u>
- $d_n$ demand (MW) at node $n \in N$
- $a_g$ available capacity (MW) of $g \in G$
- $c_g$ cost (\$/MWh) of $g \in G$
- $l_e$ length (km) of line $e \in E$
- $f_e$ 'from' node, for $e \in E$
- $t_e$ 'to' node, for $e \in E$
- $h$ hours running, $g \in G$

<u>Vars</u>
- $x_n$ electricity produced (MW) by $n \in N$
- $y_e$ flow (MW) on line $e \in E$

<u>Obj</u> Minimise $\sum_{g\in G} h c_g x_g$ subject to constraints

<u>Constraints</u>
- Production: $x_n \le a_n$; $\ x_n = 0$ $\quad \forall n \in N$
- Flow balance: $x_n + \sum_{e\in E} y_e = d_n + \sum_{e\in E} y_e$ such that $t_e = n$, $f_e = n$
- Modified f.b.: $x_n + \sum_{e\in E}(1 - \text{loss}\cdot l_e)y_e = \cdots$
- Non-neg.: $x_n \ge 0\ \forall n \in N$; $\ y_e \ge 0\ \forall e \in E$

[The subscript of $l_e$ is written as a dot ("$l_\bullet$"); $e$ is meant. "such that $t_e = n$, $f_e = n$" attaches to the two sums in order: the left sum is over lines into $n$ ($t_e = n$), the right over lines out of $n$ ($f_e = n$). possible error: Production should read $x_n \le a_n$ for $n \in G$ and $x_n = 0$ for $n \in N \setminus G$; as written both carry "$\forall n \in N$" ($a_n$ is only defined for generators). "loss" (loss per km) is not defined in the data list. The modified flow balance is left unfinished ("$= \cdots$").]

*Figure:* none.

---

### HW 23 (`20261122_004916.jpg`): Practical 3: Oil Blending (1)

**Practical 3: Oil Blending**

**Ex.**
<u>Sets</u>
- $I$: oils
- $T$: month

<u>Data</u>
- $v_i$: $\begin{cases}\text{true if } i \in I \text{ is vegetable}\\ \text{false if otherwise}\end{cases}$
- $h_i$: hardness of oil $i \in I$
- $c_{it}$: cost (\$/tonne) of oil $i \in I$ in given month $t \in T$
- MaxVeg, MinVeg: max processing (tonnes) of each type
- MaxH, MinH : max hardness limit $i \in I$
- $p$: price (\$/tonne) of final blend
- (b) $\Big\{$ storecost : cost of storage (\$/tonne/mo.); storemax : max storage (tonne) per month; initial : amount (tonne) of oil initially

<u>Vars</u>
- $x_i$: tonnes of oil $i \in I$ to blend
- $s_{it}$: tonnes of oil $i \in I$ in storage at end of month $t \in T$
- $y_{it}$: … to purchase in $t \in T$

<u>Obj</u> Maximise $p\sum_{i\in I} x_i - \sum_{i\in I} c_i x_i$

(b) $\Big\{$ Maximise $p\sum_{i\in I}\sum_{t\in T} x_{it} - \sum_{i\in I}\sum_{t\in T} c_{it}y_{it} - \text{storecost}\cdot\sum_{i\in I}\sum_{t\in T} s_{it}$

["(b)" marks the additions for part (b) of the practical (multi-month version with storage). possible error: "MaxVeg, MinVeg" should be "MaxVeg, MaxNonVeg" (HW 24 uses MaxNonVeg; both are maxima of each type). "MaxH, MinH: max hardness limit" is as written (max and min hardness of the blend). The single-month objective uses $c_i$ and $x_i$; part (b) uses $x_{it}$ and $c_{it}$. "$y_{it}$: …" means tonnes of oil $i$.]

*Figure:* none.

---

### HW 24 (`20261122_004920.jpg`): Practical 3: Oil Blending (2)

**Practical 3: Oil Blending**

**Ex.** <u>Constraints</u>

Processing limits:
$$\sum_{i\in I \text{ s.t. } v_i} x_{it} \le \text{MaxVeg} \quad \forall t\in T, \qquad \sum_{i\in I \text{ s.t. not } v_i} x_{it} \le \text{MaxNonVeg} \quad \forall t \in T$$

Hardness limits:
$$\sum_{i\in I}(h_i - \text{maxH})x_{it} \le 0 \quad \forall t \in T, \qquad \sum_{i\in I}(\text{minH} - h_i)x_{it} \le 0 \quad \forall t \in T$$

Non-negativity: $x_{it} \ge 0$, $s_{it} \ge 0$, $y_{it} \ge 0$ $\quad \forall i \in I, \forall t \in T$

Storage limits:
$$s_{it} \le \text{storemax}, \qquad s_{i5} \ge \text{initial}$$
$$s_{it} = s_{i,t-1} + y_{it} - x_{it}, \qquad s_{i0} = \text{initial} + y_{i0} - x_{i0}$$

[The storage variable is written as a capital-looking "S" in places; same as $s_{it}$ on HW 23. "$s_{i5}$" is clearly a 5: presumably the last month (months indexed 0–5), so the final stock must be at least the initial stock; the month range is not given. Indexing is inconsistent: $s_{i0}$ is defined by the balance with "initial" playing $s_{i,-1}$. The hardness limits are the linearised forms of $\text{minH} \le \sum_i h_i x_{it}/\sum_i x_{it} \le \text{maxH}$ (that form is not written).]

*Figure:* none.

---

### HW 25 (`20261122_004937.jpg`): LP: minimising absolute error

**LP: minimising absolute error**

**Ex.**
<u>Sets</u> $I$ observations

<u>Data</u> $(x_i, y_i)$ points for $i \in I$

<u>Variables</u>
- $\bar x_i$ distance between data point and point on line $\quad\times$
- $b_0, b_1$ intercept and slope variables
- $z_i$ absolute error for point $i \in I$

<u>Objective</u>
- ~~[blotted]~~ Min. $\sum_{i\in I}\abs{y_i - (b_0 + b_1x_i)}$ $\quad\times$
- Min. $\sum_{i\in I} z_i$

<u>Constraints</u>
$$e_i = y_i - (b_0 + b_1x_1), \qquad z_i \ge e_i,\quad z_i \ge -e_i \qquad \forall i \in I$$

**Rem.** Tip: can I model my solution in a linear, matrix form?
Strict inequalities are not allowed.
Hardest part of solution is vars.

**Rem.** You cannot have 'if' in a constraint.

[The "×" marks in the right margin reject the first attempt: the variable $\bar x_i$ and the absolute-value objective (not linear) are crossed off, replaced by $z_i$ and $\min\sum z_i$. A word before "Min." in the first objective is hatched out. possible error: $b_1x_1$ in the constraint should be $b_1x_i$. $e_i$ is not listed as a variable (it can be read as shorthand for the expression).]

*Figure:* none.

---

### HW 26 (`20261122_004940.jpg`): Integer programming: Telfa

**Integer programming: Telfa**

**Ex.** Telfa Pty. Ltd.
- $x_1$ tables to create
- $x_2$ chairs to create

We maximise $z = 8x_1 + 5x_2$ subject to:
$$
\left.\begin{aligned}
x_1 + x_2 &\le 6\\
9x_1 + 5x_2 &\le 45\\
x_1, x_2 &\ge 0
\end{aligned}\right\}\ \text{linear relaxation problem}
\qquad x_1, x_2 \in \Z
$$
[The brace "linear relaxation problem" covers the first three lines (the LP without $x_1, x_2 \in \Z$).]

The solution of the linear relaxation problem is:
↳ [hatched-out text] $z = 47.25$, $x_1 = 3.75$, $x_2 = 2.25$

We split into 'branches':
- ↳ If $x_1 \le 3$, $z = 39$, $x_1 = 3$, $x_2 = 3$
  - ↳ non-optimal, $z$ is higher in other branch
- ↳ If $x_1 \ge 4$, $z = 41$, $x_1 = 4$, $x_2 = 1.8$
  - ↳ If $x_2 \le 1$, $z = 40.\bar5$, $x_1 = 4.\bar4$, $x_2 = 1$
    - ↳ If $x_1 \le 4$, $z = 37$, $x_1 = 4$, $x_2 = 1$
    - ↳ If $x_1 \ge 5$, $z = 40$, $x_1 = 5$, $x_2 = 0$ ✓
  - ↳ If $x_2 \ge 2$, infeasible

We stop with optimal $x_1 = 5$, $x_2 = 0$ for $z = 40$.

This method is called branch-and-bound.

[possible error: the LP relaxation value is $z = 8(3.75) + 5(2.25) = 41.25$, not $47.25$ (the point $x_1 = 3.75$, $x_2 = 2.25$ is correct). Checked: every branch value is correct. The indentation shows the tree: $x_2 \le 1$ and $x_2 \ge 2$ are both children of $x_1 \ge 4$; $x_1 \le 4$ and $x_1 \ge 5$ are children of $x_2 \le 1$. The $x_1 \le 3$ branch gives an integer solution with $z = 39$, below the incumbent 40 found later. An empty "↳" sits under the $x_1 \le 3$ line.]

*Figure (for TikZ, implied by the list):* a branch-and-bound tree. Root: LP relaxation ($z = 41.25$ [47.25 in notes], $x = (3.75, 2.25)$). Children: $x_1 \le 3$ ($z = 39$, $(3,3)$, integer) and $x_1 \ge 4$ ($z = 41$, $(4, 1.8)$). Children of $x_1 \ge 4$: $x_2 \le 1$ ($z = 40.\bar5$, $(4.\bar4, 1)$) and $x_2 \ge 2$ (infeasible). Children of $x_2 \le 1$: $x_1 \le 4$ ($z = 37$, $(4,1)$) and $x_1 \ge 5$ ($z = 40$, $(5,0)$, optimal ✓). [The notes draw no tree; this records the structure of the indented list.]

---

### HW 27 (`20261122_004948.jpg`): Integer programming: Set Covering

**Integer programming: ~~[hatched]~~ Set Covering**

[A boxed block on the upper left is fully cross-hatched (crossed out). Under the hatching can be read: "Cloth Co.", "$x_1$ shirts to create", "$x_2$ shorts to create", "$x_3$ pants to create", "We maximise $z =$". It is an abandoned start of the Cloth Co. example (done on HW 28). A hatched word in the title (presumably "Cloth Co.") precedes "Set Covering".]

**Ex.**
<u>Sets</u> $C$ towns

<u>Data</u>
- $t_c$ travel time between cities $\times$
- $n_c$ set of neighbouring towns (can use adj. matrix)

<u>Variables</u>
$$x_c = \begin{cases}1 & \text{if station built in } c \in C\\ 0 & \text{if not}\end{cases}$$

<u>Objective</u> Minimise $\sum_c x_c$

<u>Constraints</u>
$$\sum_{c\in n_c} x_i \ge 1 \qquad \forall c \in C$$
Note that we use data in the sum, not elements in a set. This is allowed.

[The "×" after "travel time between cities" marks it as not used (replaced by $n_c$). possible error: the sum index and summand disagree; $\sum_{i\in n_c} x_i \ge 1$ is meant (a station in some neighbour of $c$; whether $c \in n_c$ is not said). A yellow sticky tab at the bottom right hides nothing.]

*Figure:* none (the hatched box is crossed-out text).

---

### HW 28 (`20261122_004952.jpg`): Integer programming: Cloth Co.

**Integer programming: Cloth Co.**

**Ex.**
<u>Sets</u>
- $C$ clothes
- $R$ resources

<u>Data</u>
- $a_r$ availability of $r \in R$
- $u_{cr}$ usage of $r \in R$ to produce $c \in C$
- $p_c$ profit (price−cost) of $c \in C$
- $m_c$ machine rental cost of $c \in C$

<u>Variables</u>
- $x_c$ number of clothes $c \in C$ to make
- $y_c = \begin{cases}1 & \text{if machine rented}\\ 0 & \text{if not}\end{cases}$

<u>Objective</u> Maximise $\sum_{c\in C} x_cp_c - \sum_{c\in C} y_cm_c$

<u>Constraints</u>
$$
\begin{aligned}
\sum_{c\in C} u_{cr}x_c &\le a_r && \forall r \in R\\
x_c &\le M_cy_c && \Big\}\ \text{big M constraint, e.g. } M_1 = 40\\
x_c &\ge 0 && \forall c \in C\\
x_c &\in \Z
\end{aligned}
$$

[$M_c$ is not in the data list; "e.g. $M_1 = 40$" is an example value. $y_c \in \{0,1\}$ is given only by the case definition.]

*Figure:* none.

---

### HW 29 (`20261122_004957.jpg`): Practical 4: Portfolio Management

**Practical 4: Portfolio Management**

**Ex.**
<u>Sets</u> $P$ products (markets)

<u>Data</u>
- $r_p$ % return for each product
- $C$ Capital

<u>Variables</u> $x_p$ \$ invested in each product

<u>Objective</u> Max $\sum_{p\in P} x_pr_p$

<u>Constraints</u> $\sum_{p\in P} x_p \le C$
$$
\begin{array}{ll}
(1) & x_1 + x_2 \le 30\,000\\
(2) & x_3 + x_4 \le 30\,000\\
(3) & x_5 + x_6 \le 20\,000\\
(4) & x_7 + x_8 \ge 20\,000\\
(5) & x_9 + x_{10} \ge 25\,000\\
(6) & x_9 \ge 0.4x_{10}\\
(7) & x_1 + x_7 \le 50\,000\\
(8) & x_3 + x_8 \le 40\,000\\
& x_p \ge 0
\end{array}
$$

[The meaning of products 1–10 and of constraints (1)–(8) is not given (the practical's statement is not in the notes). The value of $C$ is not given.]

*Figure:* none.

---

### HW 30 (`20261122_005000.jpg`): Integer programming: piecewise functions

**Integer programming: piecewise functions**

**Ex.** Ewing Petroleum

<u>Sets</u>
- $I$ oils
- $J$ blends

<u>Data</u> [empty]

<u>Variables</u>
- $x_{ij}$ Amount of oil $i \in \{1,2\}$ in blend $j \in \{1,2\}$
- $y$ Additional oil purchased

<u>Objective</u> Max $1.2(x_{11} + x_{21}) + 1.4(x_{12} + x_{22}) - 2.5y_1 - 2y_2 - 1.5y_3$

<u>Constraints</u>
$$
\begin{aligned}
x_{11} + x_{12} &\le 500 + y && 0 \le y \le 1500\\
x_{21} + x_{22} &\le 1000\\
x_{11} &\ge 0.5(x_{11} + x_{21}) && x_{ij} \ge 0\\
x_{12} &\ge 0.6(x_{12} + x_{22})
\end{aligned}
$$

Let
- $z_2 \in \{0,1\}$ : 1 if $y_1 = 500$, $0 \le y_2 \le 500$
- $z_3 \in \{0,1\}$ : 1 if $y_2 = 500$, $0 \le y_3 \le 500$

from $z_2$: $\quad y_2 \le 500z_2$, $\quad y_1 \ge 500z_{[1/2]}$
from $z_3$: $\quad y_3 \le 500z_3$, $\quad y_2 \ge 500z_2$
$$\Rightarrow z_3 \le z_2$$

The function (piecewise) is convex.

[$y = y_1 + y_2 + y_3$ (three price tiers of 500 each, at 2.5, 2 and 1.5 per unit) is implied but not written. In "$y_1 \ge 500z_{[1/2]}$" the subscript is written over: a 1 and a 2 on top of each other (ambiguous glyph in the notebook; a retake won't help). possible error: it should be $y_1 \ge 500z_2$ (from $z_2$), and the last line should be $y_2 \ge 500z_3$ (from $z_3$), not $500z_2$; the conclusion $z_3 \le z_2$ follows from the corrected pair. "Convex": the purchase cost has decreasing unit prices (concave cost), so its negative in the maximisation is convex, which is why binaries are needed; the notes don't say which function is meant.]

*Figure:* none.

---

### HW 31 (`20261122_005006.jpg`): Integer programming: noughts and crosses

**Integer programming: noughts and crosses**

**Ex.**

*Figure (3×3 board):* a noughts-and-crosses grid (two vertical and two horizontal lines, no outer border) with the squares numbered row by row: top row 0, 1, 2; middle 3, 4, 5; bottom 6, 7, 8. An arrow "→" from the grid to the Sets.

<u>Sets</u>
$$S = \{0, 1, \dots, 7, 8\}, \qquad L = \{(0,1,2), (3,4,5), \dots, (2,4,6)\}$$

<u>Variables</u>
- $x_i \in \{0,1\}$ $\forall i \in S$: 1 if square $i$ is "X", 0 if square $i$ is "O"
- $y_l \in \{0,1\}$ $\forall l \in L$: 1 if line $l$ is "on"

<u>Objective</u> Min $\sum_{l\in L} y_l$

<u>Constraints</u>
Idea: if $\sum_{i\in L_l} x_i = 3 \Rightarrow y_l = 1$; $\ = 0 \Rightarrow y_l = 1$
↳↳
$$1 - y_l \le \sum_{i\in L_l} x_i \le 2 + y_l \qquad \forall l \in L$$

[$L$ has the 8 lines (rows, columns, diagonals); only three are listed. $L_l$ denotes the squares in line $l$. A line is "on" if it is all X or all O. The problem being solved (presumably: fill the board with a fixed number of X's so that the fewest lines are complete) is not stated; no constraint on the number of X's is written.]

---

### HW 32 (`20261122_005010.jpg`): Integer programming: concrete

**Integer programming: concrete**

**Ex.**
<u>Sets</u> $N$ index set of things
- $i$ batching plants
- $j$ jobs

<u>Data</u> $d_{ij}$ distance between

<u>Variables</u> $x_{ij}$ $\begin{cases}1 & \text{if job } j \text{ is served by plant } i\\ 0\end{cases}$

<u>Objective</u> Min $\sum_{i\in N}\sum_{j\in N} d_{ij}x_{ij}$

<u>Constraints</u>
$$\left.\begin{aligned}\sum_{j\in N} x_{ij} &= 1\\ \sum_{i\in N} x_{ij} &= 1\end{aligned}\right\}\ \text{Equalities, so dual variables can be negative}$$
An arrow ↖ points at the constraints from the note "50 plants, 50 jobs ensures 1–1 allocation."

Linear assignment problem
- ↳ often sparse
- ↳ total unimodular (determinant ±1)
  - ↳ invertible square sub-matrices are invertible over $\Z$.
    ↳ often in problems w/ two constraints.

None of the transport 'lines' intersect in the optimal solutions – if lines intersect distance is not minimal.

[The constraints' "for all" ranges ($\forall i$, $\forall j$) are not written. possible error: total unimodularity means every square sub-matrix has determinant $0$ or $\pm1$ (not that the determinant is $\pm1$); what follows (integer inverses, hence integral LP solutions) is as written. "two constraints" presumably means two families of constraints (each variable in exactly two constraints). The non-crossing remark is stated without proof.]

*Figure:* none.

---

### HW 33 (`20261122_005020.jpg`): Integer programming: Bananagrams

**Integer programming: Bananagrams**

**Ex.**
<u>Sets</u>
- $W$ set of words
- $A$ set of letters

<u>Data</u>
- $\Lambda_a$ # of $a$ in tiles
- $\delta_{wa}$ # times $a$ appears in word $w$

<u>Variables</u> $x_w \in \{0,1\}$: 1 if word $w \in W$ is used

<u>Objective</u> min. $\sum_{w\in W} x_w$

<u>Constraints</u>
$$\sum_{w\in W}\delta_{wa}x_w = \Lambda_a + y_a$$

Let $y_a$ be the number of $a$ intersections.
$$0 \le y_a \le \Lambda_a, \qquad \sum_{a\in A} y_a = \sum_{w\in W} x_w - 1$$

We leave out space constraints.

**Q.** Bananagrams is a word game played with 144 letter tiles, with the distribution of letters closely matching English usage. The game is played by arranging tiles into a grid of connected letters.
What is the smallest number of connected words that uses all 144 tiles?

[A small blot before $\Lambda_a$ in the data list. The data symbol is a capital Lambda ($\Lambda$); the count symbol is a delta ($\delta_{wa}$). "$\forall a \in A$" is not written on the first constraint. The question ("Q.") is written after the model.]

*Figure:* none.

---

### HW 34 (`20261122_005026.jpg`): Integer programming: cargo balancing

**Integer programming: cargo balancing**

**Ex.**
<u>Sets</u>
- $C$ compartments $\{A, B, C, D\}$
- $P$ packages

<u>Data</u>
- $m_p$ mass of package $p \in P$
- maxmass max mass per $c \in C$
- minpack min packages per $c \in C$

<u>Vars</u> $x_{cp} = \begin{cases}1 & \text{if we put } p \in P \text{ in } c \in C\\ 0\end{cases}$

<u>Objective</u> None!

<u>Constraints</u>
$$
\begin{aligned}
\sum_{p\in P} x_{cp} &\ge \text{minpack}\\
\sum_{p\in P} m_px_{cp} &\le \text{maxmass}\\
\sum_{c\in C} x_{cp} &= 1\\
\sum_{p\in P} m_px_{Ap} &= \sum_{p\in P} m_px_{Dp}\\
\sum_{p\in P} m_px_{Bp} &= \sum_{p\in P} m_px_{Cp}
\end{aligned}
$$

[The ranges ($\forall c \in C$ for the first two, $\forall p \in P$ for the third) are not written. The sum in the second line reads "$p \in D$"; $p \in P$ is meant. The last two lines balance compartments A with D and B with C.]

*Figure:* none.

---

### HW 35 (`20261122_005029.jpg`): Integer programming: Pilots

**Integer programming: Pilots**

**Ex.**
<u>Sets</u> $T$ month

<u>Data</u>
- $d_t$ pilot needed per $t \in T$
- hcost cost of hiring pilot $\big]$
- fcost cost of firing pilot $\big]$ numerical
- salary salary $\big]$
- ini initial number of pilots

<u>Vars</u>
- $s_t$ pilots in month $t \in T$
- $x_t$ hire pilots in month $t \in T$
- $y_t$ fire pilots in month $t \in T$

<u>Obj</u> min. $\sum_{t\in T} 8000s_t + 10000x_t + 5000y_t$

<u>Constraints</u>
$$s_t = s_{t-1} + x_t - y_t, \qquad s_0 = \text{ini} + x_0 - y_0, \qquad s_t \ge d_t$$

Introduce variable: $z_t = \begin{cases}1\\0\end{cases}$
$$z_t + z_{t-1} \le 1, \qquad y_t \le 60z_t \qquad \forall t \in T, t > 0$$

["numerical" (brace over hcost, fcost, salary) means these are given as numbers; the objective uses salary = 8000, hcost = 10000, fcost = 5000. The meaning of $z_t$ is not written; from the constraints, $z_t = 1$ allows firing (at most 60) in month $t$, and firing is not allowed in two consecutive months. Recorded as an inference, not in the notes.]

*Figure:* none.

---

### HW 36 (`20261122_005035.jpg`): Integer programming: storm

**Integer programming: storm**

**Ex.**
<u>Sets</u>
- $B$ boats
- $P$ ports

<u>Data</u>
- $t_{bp}$ time for $b \in B$ to reach $p \in P$
- $c_p$ max capacity of port

<u>Vars</u> $x_{bp}$ $\begin{cases}1 & \text{if } b \in B \text{ to } p \in P\\ 0 & \text{if not}\end{cases}$

<u>Objective</u> min. $\sum_{b\in B}\sum_{p\in P} x_{bp}t_{bp}$

<u>Constraints</u>
$$\sum_{b\in B} x_{bp} \le c_p \quad \forall p \in P, \qquad \sum_{p\in P} x_{bp} = 1 \quad \forall b \in B$$

[The lower half of the page is blank (low sharpness score; the writing is readable).]

*Figure:* none.

---

### HW 37 (`20261122_005039.jpg`): Integer programming: pure fresh juice

**Integer programming: pure fresh juice**

**Ex.**
<u>Sets</u>
- $T$ quarters
- $J$ juices
- $F$ fruits

<u>Data</u>
- $b_{jf}$ proportion of juice $j \in J$ made from $f \in F$
- $s_{jt}$ max sales of juice $j \in J$ in quarter $t \in T$
- $p$ sell price (\$/L)
- $c_f$ cost of fruit $f \in F$ (\$/kL)
- $a_t$ availability of FCOJ (kL) in $t \in T$

<u>Vars</u> $x_{jt}$ amount of juice $j \in J$ in [hatched] $t \in T$

<u>Objective</u>
$$\max \sum_{j\in J}\sum_{t\in T} px_{jt} - \sum_{j\in J}\sum_{t\in T}\sum_{f\in F} c_fb_{jf}x_{jt} - \sum_{f\in F\setminus\{0\}}\sum_{t\in T}\ [\text{unfinished}]$$

<u>Constraints</u>
FCOJ import:
$$\sum_{j\in J} b_{j0}x_{jt} \le a_t \quad \forall t \in T$$
$$x_{jt} \le s_{jt} \quad \forall j \in J, \forall t \in T, \qquad x_{jt} \ge 0$$
$$\sum_{j\in J} b_{jf}x_{jt} \le 10y_{ft} \qquad \text{where } y_{ft} \text{ is truckloads of fruit}$$

[FCOJ (frozen concentrated orange juice, not expanded in the notes) is fruit $f = 0$. The third objective term stops after the two sums (presumably the truckload cost of $y_{ft}$, whose cost is not in the data list). Units are mixed (\$/L sale price, \$/kL fruit cost) as written. A word before "$t \in T$" in Vars is hatched out (presumably "quarter").]

*Figure:* none.

---

### HW 38 (`20261122_005046.jpg`): Integer programming: Sudoku

**Integer programming: Sudoku**

**Ex.**
<u>Sets</u>
- $N$ digits $\{1, \dots, 9\}$
- $L$ tiles

<u>Data</u> ~~[boxed and hatched out: "$S$ digit in tiles"]~~ Set of initial placement ~~[hatched]~~ $(r,c,n)$

<u>Vars</u> $x_{rcn} = \begin{cases}1 & \text{if number } n \text{ in tile } (r,c)\\ 0 & \text{if not}\end{cases}$

<u>Objective</u> [blank]

<u>Constraints</u> Each digit once per row:
$$\sum_{c\in C} x_{rcn} = 1 \qquad \forall r \in R, \forall n \in N$$
$$\sum_{r\in R} x_{rcn} = 1 \qquad \leftarrow \text{column}$$
$$[\text{blank}] \qquad \leftarrow \text{block}$$
$$\sum_{n\in N} x_{rcn} = 1 \qquad \forall c \in C, \forall r \in R$$
$$x_{rcn} = 1 \qquad \forall (r,c,n) \in S$$

[Crossed-out (hatched) content: the first data entry (a boxed line, partly readable as "$S$ … digit in tiles"), a word after "placement" and a symbol above "$r \in R$" in the column sum. The block constraint is not written (only its label and arrow). $R$ and $C$ (rows, columns) are not defined; the data set of initial placements is called $S$ in the last constraint. The column constraint's range ($\forall c \in C, \forall n \in N$) is not written. No objective (a feasibility problem, like HW 34).]

*Figure:* none.

---

### HW 39 (`20261122_005053.jpg`): Integer programming: coal line maintenance

**Integer programming: coal line maintenance**

**Ex.**
<u>Sets</u>
- $N$ nodes $\qquad$ $T$ weeks
- $A$ arcs $\qquad$ $M \subset A$ arcs w. maintenance

<u>Data</u>
- $u_a$ max throughput of arc $\in A$
- $f_a$ from node of arc $\in A$
- $t_a$ to node
- [under a bracket labelled "2"] $e_a$ effort for mainten. $a \in A$; $\ l_t$ labour avail. at $t \in T$

<u>Vars</u>
- $x_{at}$ coal flow on each arc $a \in A$ at week $t \in T$.
- $y_{at} = \begin{cases}1 & \text{if } a \in M \text{ maintained at } t \in T.\\ 0\end{cases}$

<u>Obj.</u> $\max x_0 \to \max\sum_t x_{0t}$

<u>Constraints</u>
$$\sum_{a\in A:\ f_a = n} x_{at} = \sum_{a\in A:\ t_a = n} x_{at} \qquad \forall n \in N, \forall t \in T$$
$$0 \le x_a \le u_a$$
[bracket labelled "2" over the next three]
$$\hookrightarrow\ x_{at} \le (1 - y_{at})u_a \qquad \forall a \in M, \forall t \in T$$
$$\sum_{a\in A} e_ay_{at} \le l_t \qquad \forall t \in T$$
$$\sum_{t\in T} y_{at} = 1 \qquad \forall a \in M$$
[bracket labelled "3b" over the next three; the first and last are also under an underbrace labelled "3a: stockpile bypass"]
$$y_{S4,0} = 0, \qquad y_{S4,t} = \sum_{t'=0}^{t-1} y_{S3,t'} \quad \forall t \in T,\ t > 0 \ [\text{with "}t'\text{?" written above the } t], \qquad y_{STS,0} = 1$$

3c. left as exercise, generalisation of 3b.

[The labels 2, 3a, 3b, 3c refer to parts of the practical/assignment, whose statement is not in the notes; S3, S4 and STS are arc names from that network (not defined here). "$x_0$" is the flow on arc 0 (presumably the output arc). The flow-balance constraint as written has no source/sink exception. Above the $t$ in "$t > 0$" the notes have a small "$t'$?", the writer's own query. Which labels cover which lines: "2" spans $x_{at} \le (1-y_{at})u_a$ to $\sum_t y_{at} = 1$; "3b" spans the three $y_S$ lines; "3a" is under $y_{STS,0} = 1$ only, as drawn.]

*Figure:* none.

---

### HW 40 (`20261122_005101.jpg`): Dynamic programming

**Dynamic programming**

**Def.** Dynamic programming works by simplifying a complex decision by breaking it down into a sequence of decision steps over time.

We use the principle of optimality: the optimal solution to a dynamic optimisation problem can be found by combining the optimal solutions to its subproblems.

Our base case is: $V_{t_{\max}}(s) = $ function of $s$.

Our goal is: $V_0(s_0)$ if initial index is 0.

Stochastic dynamic programming: has no fixed state in the future, but a distribution of states.

[$V_t(s)$ (value function at stage $t$, state $s$) is not defined on this page; it is used from HW 41 on. A pink sticky tab at the bottom right hides nothing.]

*Figure:* none.

---

