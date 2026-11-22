# MATH3202 Operations Research & Mathematical Planning: transcription, part 2 of 2 (HW 41–80)

_Transcription phase. Sources, legibility check and conventions: see `claude/notes-math3202-1.md`. No dates are recorded: the three worked past exams are called **Past exam I** (HW 58–69), **II** (HW 70–73, 80) and **III** (HW 74–79), in the order they appear._

**This part:** dynamic programming (components, Bellman equation, deterministic and stochastic examples), shortest paths and resource constrained shortest paths, complexity and metaheuristics (simulated annealing), and worked past-exam questions on the revised simplex algorithm, sensitivity, IP modelling and DP.

---

### HW 41 (`20261122_005110.jpg`): Dynamic programming (2)

**Dynamic programming**

**Def.** We break a dynamic programming problem up into:

- <u>Stages</u>: often indexed by $t$ (time stages)
- <u>State space</u>: discrete $s \in S$
- <u>Action space</u>: discrete $a \in A$ (or $A_t$: can depend on stage)
- <u>Transition function</u>: $s_{t+1} = s^M(s_t, a_t)$ $\quad\Big\}$ recursive
- <u>Contribution function</u>: Immediate cost of making action $a_t$ at state $s_t$ at stage $t$.
  ~~[hatched]~~ $C_t(s_t, a_t)$
  i.e. short-term return
- <u>Value function</u>: Similar to objective function.
  Bellman equation:
  $$V_t(s_t) = \min_{a_t\in A}\{C_t(s_t, a_t) + V_{t+1}(s_{t+1})\}$$
  A caret "^" under the "+" with the note "can be any operation".

  In an additive model, $V_{\text{base}}(s_{\text{base}}) = 0$.
  In a multiplicative model, $V_{\text{base}}(s_{\text{base}}) = 1$.

[The superscript of $s^M$ is a capital M ("model"). The headings are written as labels in the left column (no underline on "Value function"). A few characters before $C_t(s_t, a_t)$ are hatched out. The base value of 0 / 1 is stated without the condition that the base stage has no further contribution.]

*Figure:* none.

---

### HW 42 (`20261122_005118.jpg`): Dynamic programming: inventory problem

**Dynamic programming: inventory problem**

**Ex.**
- <u>Stages</u> $t$ months
- <u>State space</u> $0 \le s_t \le 4$ inventory
- <u>Action space</u> $0 \le a_t \le 5$ production
- <u>Transition function</u> $s_{t+1} = s_t + a_t - d_t$ [underbrace on $d_t$: "demand"]
- <u>Contribution function</u>
  $$C_t(a_t) = \begin{cases}0 + 0.5s_{t+1} & \text{if } a_t = 0\\ 3 + 1a_t + 0.5s_{t+1} & \text{if } a_t > 0\end{cases}$$
- <u>Value function</u>
  $$V_t(s_t) = \min_{0\le a_t\le 5}\{C_t(a_t) + V_{t+1}(s_t + a_t - d_t)\}$$
  $\updownarrow$ We can also use
  $$\max\{0, d_t - s_t\} \le a_t \le \min\{5, 4 + d_t - s_t\}$$

[Reading of the costs (not written): set-up cost 3, unit cost 1, holding cost 0.5 per unit carried. The tighter action range keeps $0 \le s_{t+1} \le 4$. The demands $d_t$, the number of months and the base case are not given. A small stray mark ("=:") at the top right.]

*Figure:* none.

---

### HW 43 (`20261122_005126.jpg`): Dynamic programming: minimal studying

**Dynamic programming: minimal studying**

**Ex.**
- <u>Stages</u> $t \in \{1,2,3\}$ subjects
- <u>State</u> $s_t$ hours remaining
- <u>Action</u> $a_t$ hours for subject $t$
- <u>Data</u> $p_{t,h}$ probability of passing subject $t$ with $h$ hours
- <u>Value function</u> We want $V_1(4)$.
  i.e. pass one subject, four hours remaining

  Base case: $V_4(s_4) = 1$
  $$V_t(s_t) = \min_{0\le a_t\le s_t}\bigl\{\underbrace{(1 - p_{t,(a_t)})}_{\Prob \text{ of failing subject } t}\cdot\underbrace{V_{t+1}(s_t - a_t)}_{\Prob \text{ of failing remaining } t}\bigr\}$$

We want to minimise the probability that we fail all three subjects.

[The $p_{t,(a_t)}$ is written above a solid blacked-out box inside the bracket (the original symbol is hidden; the replacement above it is clear). The underbraces are written as corner brackets with the labels below. "i.e. pass one subject, four hours remaining" is as written: $V_1(4)$ is the minimum probability of failing all subjects starting at subject 1 with 4 hours. A multiplicative model (base case 1, HW 41). The table $p_{t,h}$ is not given.]

*Figure:* none.

---

### HW 44 (`20261122_005134.jpg`): Dynamic programming: non-linear objective

**Dynamic programming: non-linear objective**

**Ex.**
- <u>Stages</u> $t$ variables
- <u>State</u> $s_t$ amount of total available for stages $t, \dots, 3$
- <u>Action</u> $x_t$ value
- <u>Data</u>
  - $d = [5, 1, 2]$ coefficients
  - $w = [3, 2, 1]$ constraint LHS
  - total $= 6$ RHS
- <u>Value function</u> $V_t(s_t)$ max value from variables $x_t, \dots, x_0$, if we have $s_t$ available.
  $$= \max_{0\le x_t\le\lfloor s_t/w_t\rfloor}\{(x_t + d_t)\times V_{t+1}(s_t - w_tx_t)\}$$
  $$
  \begin{aligned}
  V_3(s_3) &= \max_{0\le x_3\le s_3}(x_3 + 2)\\
  V_2(s_2) &= \max_{0\le x_2\le\lfloor s_2/2\rfloor}[(x_2 + 1)\cdot V_3(s_2 - 2x_2)]\\
  V_1(s_1) &= \max_{0\le x_1\le\lfloor s_1/3\rfloor}\{(x_1 + 5)\cdot V_2(s_1 - 3x_1)\}
  \end{aligned}
  $$
  We want $V_1(6)$.

**Q.** Maximise $(x_1 + 5)(x_2 + 1)(x_3 + 2)$ subject to $3x_1 + 2x_2 + x_3 \le 6$ where $x_1, x_2, x_3 \in \Z^+$.

[The data vector $w$ is written with a letter that looks like "u"/"υ"; the recursion uses $w_t$. possible error: "$x_t, \dots, x_0$" should be "$x_t, \dots, x_3$" (the stages run 1 to 3). The "2" in $V_3(s_3) = \max(x_3 + 2)$ is written over another digit. $\Z^+$ here must include 0 (the recursion allows $x_t = 0$). No numerical answer is given.]

*Figure:* none.

---

### HW 45 (`20261122_005138.jpg`): Dynamic programming: democracy

**Dynamic programming: democracy**

**Ex.**
- <u>Stages</u> LGAs $j = 1, \dots, n \in L$
- <u>State</u> $s_j$ number of representatives available for $j, \dots, n$
- <u>Action</u> $a_j$ number of representatives to allocate to LGA $j$
- <u>Data</u> $P_j$ population of $j \in L$; $\quad d_j = \dfrac{100P_j}{\sum P_j}$ target reps. for LGA $j$
- <u>Value function</u> $V_j(s_j)$ minimum max. discrepancy if we have $s_j$ reps for LGAs $j, \dots, n$

Base: $V_{50}(s_{50}) = \abs{s_{50} - d_{50}}$

Obj: $V_1(100)$

General case:
$$V_j(s_j) = \min_{0\le a_j\le s_j}\bigl\{\max\{\abs{a_j - d_j}, V_{j+1}(s_j - a_j)\}\bigr\}$$

[LGA = local government area (not expanded in the notes). There are $n = 50$ LGAs and 100 representatives (from the base case and objective). A min–max model: the "operation" of HW 41 is max.]

*Figure:* none.

---

### HW 46 (`20261122_005146.jpg`): Stochastic DP: chess strategy

**Stochastic DP: chess strategy**

**Ex.**
- <u>Stages</u> games $j$
- <u>Action</u> bold; conservative
- <u>State</u> $s_j$ points at start of game $j$
- <u>Value f.</u> $V_j(s_j)$ = max. probability of winning match if we start game $j$ with $s_j$ points

We want $V_1(0)$.

Base case
$$V_3(s_3) = \begin{cases}.45 & \text{if } s_3 = 1\\ 1 & \text{if } s_3 > 1\\ 0 & \text{if } s_3 < 1\end{cases} \qquad s_3 \text{ may not occur!}$$

In general,
$$V_j(s_j) = \max\begin{cases}.55V_{j+1}(s_j) + .45V_{j+1}(s_j + 1) & \text{b.}\\ .1V_{j+1}(s_j) + .9V_{j+1}(s_j + \tfrac12) & \text{c.}\end{cases}$$
["b." = bold, "c." = conservative (right margin). Under the second line "end." with two small arrows pointing down at the values below.]

First game:
$$V_1(0) = \max\begin{cases}.55\,\underset{.2025}{V_2(0)} + .45\,\underset{.945}{V_2(1)} = 0.5366\\ .1V_2(0) + .9\,\underset{.45}{V_2(\tfrac12)} = 0.4253\end{cases}$$

Second game:
- (lost first) $V_2(0) = \max\begin{cases}.55V_3(0) + .45V_3(1) = 0.2025\\ .1V_3(0) + .9V_3(\tfrac12) = 0\end{cases}$
- (draw first) $V_2(\tfrac12) = \max\begin{cases}.55V_3(\tfrac12) + .45V_3(\tfrac32) = 0.45\\ .1V_3(\tfrac12) + .9V_3(1) = 0.405\end{cases}$
- (win first) $V_2(1) = \max\begin{cases}.55V_3(1) + .45V_3(2) = 0.6975\\ .1\,\underset{.45}{V_3(1)} + .9\,\underset{1}{V_3(\tfrac32)} = 0.945\end{cases}$

**Rem.** Start with base → first game → second game → use values from game 3 and work backwards with values.
| Ans: 1) bold; 2) W: cons. L: bold; 3) bold

[The small numbers written above or below a value term (shown here with \underset) are the values substituted. Setting (inferred from the numbers, not stated): two-game match, bold play wins (1 point) w.p. 0.45 and loses w.p. 0.55; conservative play draws (½ point) w.p. 0.9 and loses w.p. 0.1; a tie after two games goes to a sudden-death game played boldly ($V_3(1) = .45$). The "+1" in the general bold line is written over a blot. Checked: every value is correct ($V_1(0) = 0.536625$, $0.42525$). The "Ans" is: game 1 bold; game 2 conservative if won (W), bold if lost (L); game 3 bold. The value $V_2(\tfrac12) = 0.45$ means bold after a draw, not listed in "Ans".]

*Figure:* none.

---

### HW 47 (`20261122_005149.jpg`): Stochastic DP: betting strategy

**Stochastic DP: betting strategy**

**Ex.**
- <u>Stages</u> games $j$
- <u>Action</u> $b_j$ amount to bet in game $j$
- <u>State</u> $s_j$ money at start of game $j$
- <u>Value f.</u>
  $$V_j(s_j) = \max_{0\le b_j\le s_j}\left\{\begin{aligned}&.6V_{j+1}(s_j - b_j)\\ &+ .4V_{j+1}(s_j + b_j)\end{aligned}\right\}$$

We want $V_1(2)$.

Base case
$$V_4(s_4) = \begin{cases}1 & \text{if } s_4 \ge 5\\ 0 & \text{if } s_4 < 5\end{cases}$$

- First game: $V_1(2) = \max\{\cdots\} = (\underset{p}{0.256}, \underset{b_j}{2})$
- Second game: $V_2(4) = \cdots = (\underset{p}{0.64}, \underset{b_j}{1})$
- Third game: $V_3(3) = \cdots =$ [blank]
- $\phantom{\text{Third game: }} V_3(5) = \cdots =$ [blank]

[The pairs are (probability $p$, optimal bet $b_j$). The "4" in $V_4(s_4)$ is written over another digit. The third-game values are left blank. Checked by recomputing (win w.p. 0.4, target 5 after three games): $V_2(4) = 0.64$ with $b = 1$ and $V_1(2) = 0.256$ with $b = 2$ are correct. The rest of the page is blank.]

*Figure:* none.

---

### HW 48 (`20261122_005155.jpg`): Stochastic DP: transcontinental drive

**Stochastic DP: transcontinental drive**

**Ex.**
- <u>Sets</u> $N$ nodes; $A$ arcs; $A_n^{\to}$ arcs leaving a node $n$; $A_n^{\leftarrow}$ [no description]
- <u>Data</u> $f_a, t_a, c_a$ from, to, cost for $a \in A$
- <u>State</u> $n$ node
- <u>Stage</u> Unnecessary, has ordering / acyclic (Stage is to present cyclic behaviour)

$$V(n) = \begin{cases}0 & \text{if } n = \text{LA}\\ \min_{a\in A_n^{\to}} c_a + V(t_a)\end{cases}$$

distance to 4:
$$d_4 = \min\begin{cases}d_1 + c_{14} = 1230\\ d_2 + c_{24} = 1480\\ d_3 + c_{34} = 1280\end{cases}$$

**N.** Forward labelling problem
- ↳ some ordering of nodes required
- ↳ used for shortest path problems e.g. maps
- ↳ every deterministic DP can be turned into a forward labelling problem

[The arc-set symbols are $A_n$ with a small right arrow (leaving) and left arrow (presumably entering) above the subscript. "present" is presumably "prevent" ("stage is to prevent cyclic behaviour"). The third value reads 1280 (the middle digit could be a 3: ambiguous in the notebook). The node data and $d_1, d_2, d_3$, $c_{i4}$ are not given, and the minimum $d_4$ is not stated. possible error: the title says "Stochastic DP" but the problem is deterministic (no probabilities); LA is the destination (Los Angeles, not expanded). $V(n)$ (backward, cost-to-go) and $d_n$ (forward, distance from the start) are two different recursions on the same page.]

*Figure:* none.

---

### HW 49 (`20261122_005159.jpg`): Stochastic DP: web-building

**Stochastic DP: web-building**

**Rem.** Based on a real paper, does not involve money!

**Ex.**
- <u>State</u> $s_t$ weight at start of day $t$
- <u>Stages</u> $t$ days
- <u>Action</u> $w_t$ size of web to build
- <u>Value fn.</u> $V_t(s_t)$ = maximum probability of reaching 80mg by day 10, if we start day $t$ with weight $s_t$

We want $V_1(35)$

Base case:
$$V_{11}(s_{11}) = \begin{cases}1 & \text{if } s_{11} \ge 80\\ 0, & \text{otherwise}\end{cases}, \qquad V_t(s_t) = 0 \text{ if } s_t < 25, \qquad V_t(s_t) = 1 \text{ if } s_t \ge 80$$
[A bracket in the right margin with an arrow ← pointing at the first line groups the three lines as base cases. A small blot after the "1" in the last line.]

General case:
$$V_t(s_t) = \max_{w_t}\left\{\begin{aligned}&\lambda_{w_t}V_{t+1}(\overbrace{s_t + 6 - \alpha(w_t, s_t)}^{s_{t+1}})(1 - \beta_{w_t})\\ &+ (1 - \lambda_{w_t})V_{t+1}(\underbrace{s_t - \alpha(w_t, s_t)}_{s_{t+1}})(1 - \beta_{w_t})\\ &+ \beta_{w_t}\cdot 0\end{aligned}\right.$$

[Not defined on the page (reading from the recursion): $\lambda_{w}$ = probability of catching food with web size $w$ (gain 6 mg), $\alpha(w, s)$ = weight used up building web $w$ at weight $s$, $\beta_w$ = probability of being eaten (value 0). In the first two lines the $\beta$ in $(1 - \beta_{w_t})$ is written like "ρ"/"β"; read as $\beta$, as in the third line. The weights 25 (death threshold) and 80 (target) are not explained. "by day 10" with base case at day 11 is as written.]

*Figure:* none.

---

### HW 50 (`20261122_005205.jpg`): Stochastic dynamic programming theory (1)

**Stochastic dynamic programming theory**

**Def.** We provide a recap on deterministic DP:
- <u>State</u> $S$, discrete state space
- <u>Action</u> $A$, discrete action space
- <u>Stages</u> $t$ often corresponds to time
- <u>Transition function</u> $s_{t+1} = s^M(s_t, a_t)$: the state we are in at stage $t+1$ depends on previous state + action
- <u>Contribution function</u> $C_t(s_t, a_t)$: the immediate cost (or value) of making decision $a_t$ in state $s_t$
- <u>Value function</u> $V_t(s_t) = \min_{a_t}\{C_t(s_t, a_t) + V_{t+1}(s_{t+1})\}$: total cost (or value) of making all the best decisions, from chosen $t$ to the end

[Repeats HW 41. Pink sticky tab at the bottom right; hides nothing.]

*Figure:* none.

---

### HW 51 (`20261122_005210.jpg`): Stochastic dynamic programming theory (2)

**Stochastic dynamic programming theory**

**Def.** We also provide a recap on stochastic DP:
- <u>Outcome</u> $\Omega$, discrete outcome space, can depend on state, stage, action
- <u>Prob.</u> $p_t(\omega_t, s_t, a_t)$: probability $p_t$ of outcome $\omega_t \in \Omega_t(s_t, a_t)$
  $$\sum_{\omega_t} p_t(\omega_t, s_t, a_t) = 1.$$
- <u>Transition function</u> $s_{t+1} = s^M(s_t, a_t, \omega_t)$: can now depend on outcome $\omega_t$
- <u>Value function</u>
  $$V_t(s_t) = \min_{a_t}\Bigl\{C_t(s_t, a_t) + \sum_{\omega_t} p_t(\omega_t, s_t, a_t)V_{t+1}(s_{t+1})\Bigr\}.$$

[$\omega_t$ is written like "w". In the value function $s_{t+1} = s^M(s_t, a_t, \omega_t)$ depends on $\omega_t$ (not written inside the sum).]

*Figure:* none.

---

### HW 52 (`20261122_005216.jpg`): Resource constrained shortest paths (1)

**Resource constrained shortest paths**

**Def.** Suppose we have a cyclic network.
We use a forward labelling procedure.
- ↳ Label ≈ state
- ↳ We 'extend' [blot] a label to future 'states' / labels
- ↳ Runs forward, not usually backward

RCSP, without resources, simplifies down to Dijkstra's path-finding algorithm.

**Def.** Resource constrained shortest paths
- $R$ set of resources
- $N$ set of nodes
- $A_i$ set of nodes connected to node $i$
- $d_{ij}$ length of arc from $i$ to $j$, $\ge 0$
- $U_{ij}$ vector of resource consumption on arc from $i$ to $j$. Can be negative (i.e. can replenish resources)
- $L_i$ set of labels for node $i$
- $(i, s, V, \text{done})$ data stored with a label:
  - $i_l$ node
  - $s_l$ relevant path length
  - $V_l$ vector of resource levels
  - $\text{done}_l$ Boolean flag

["cyclic" as written (the method allows cycles, unlike HW 48's acyclic case). RCSP = resource constrained shortest path.]

*Figure:* none.

---

### HW 53 (`20261122_005222.jpg`): Resource constrained shortest paths (2)

**Resource constrained shortest paths**

**Def.** The algorithm is defined as follows:
Start at the origin O with initial vector of resources $V_0$.
- (1) Set $L_0 = \{(0, 0, V_0, \text{false})\}$, $L_i = \emptyset$
- (2) Choose label $l$ such that $s_l = \min\{s_l : \text{done}_l = \text{false}\}$
- (3) If $i_l = D$ (destination) then stop.
- (4) Set $\text{done}_l = \text{true}$
- (5) For all $j \in A_{i_l}$ such that $V_l - U_{ij} \ge 0$ (resource constraint),
  AddLabel$\{j, s_l + d_{ij}, V_l - U_{ij}, \text{false}\}$ (create new label at node $j$)
- (6) Repeat from step (2).

**Rem.** An exponential number of labels will be created if we are not careful with how we add labels.
Thus, with AddLabel, it must remove any dominated label.

**Def.** Label $l_1$ dominates label $l_2$ iff:
- ↳ $i_{l_1} = i_{l_2}$ (go to same node)
- $\phantom{↳}$ $s_{l_1} \le s_{l_2}$ (cheaper to go there / less path length)
- $\phantom{↳}$ $V_{l_1} \ge V_{l_2}$ (more of every resource left)

One label dominating another implies a separate path to the same node that is no longer, and consumes no more of every resource.

**Rem.** In the case that there is no resources, this algorithm reduces to Dijkstra's shortest path algorithm.

[In (2) the minimum is over all labels $l'$ with $\text{done}_{l'} = \text{false}$ (same letter used for both). In (5) $U_{ij}$ means $U_{i_l j}$. $L_i = \emptyset$ is for $i \ne 0$. "(4) Set done$_l$ − true": the "=" is faint.]

*Figure:* none.

---

### HW 54 (`20261122_005230.jpg`): Remarks on RCSP

**Remarks on RCSP**

**Rem.** Sometimes resource constrained shortest paths are expressed in terms of resources accumulating and reaching some maximum. It is important to quickly find the next label.

A good example would the shortest path between two points travelling on a restricted / finite number of arcs.

**Ex.** For example, finding the fastest possible journey from A to B through a public transport network with fewer than N changes, costing less than \$M.

**Def.** Here are some requirements for RCSP:
- (1) The set of feasible decisions for a given label (i.e. arcs – how to move forward from the label)
- (2) How the values on the new label (cost, etc.) depend on the current label and decision made
- (3) Dominance criteria among labels
- (4) A processing order for labels, which ensures that we will not have infinite loops.

**Rem.** For a more efficient algorithm, consider the A* search algorithm.

Labels
$$l = (c_l, r_l, i_l, \text{path}_l)$$
cost so far, resource usage, node, path to label $l$.

Augment to be
$$l = (c^*_l, c_l, r_l, i_l, \text{path}_l)$$
where $c^*_l$ is a lower bound estimate of min. cost.

["would the shortest path" as written ("would be"). The "Rem." label at the top reads "Rem." (first letter unclear). The label tuple here differs from HW 52's $(i, s, V, \text{done})$; both as written. How $c^*_l$ is used (order labels by $c^*_l$) is not written.]

*Figure:* none.

---

### HW 55 (`20261122_005235.jpg`): Metaheuristics

**Metaheuristics**

**Rem.** Our LP, IP and DP models have been used to find exact solutions. However, there are many IP and DP models that cannot be solved in reasonable time. Metaheuristics can help with this.

**Def.** Types of metaheuristics:
- ↳ Simulated annealing
- ↳ Genetic algorithms
- ↳ Misc. (see PowerPoint)

**Def.** Consider an optimisation problem consisting of a large finite number of feasible solutions

[The sentence stops there; the rest of the page is blank. "see PowerPoint" refers to lecture slides not supplied.]

*Figure:* none.

---

### HW 56 (`20261122_005241.jpg`): Complexity

**Complexity**

**Def.**
- P: class of problems solvable in polynomial time
- NP: class of problems where objective can be evaluated in polynomial

A Millennium Prize problem is $\mathrm{P} \overset{?}{=} \mathrm{NP}$.

- <u>NP hard</u>: as hard as any problem in NP.
- Exact alg.: can make work on bigger problems
- Heuristic alg.: can make give better solutions

**Def.** Heuristic algorithms require
- ↳ some way of generating an initial algorithm
- ↳ some formal definition of a neighbourhood
- ↳ some rule for picking a neighbour

[possible error: NP is the class of (decision) problems whose solutions can be *verified* in polynomial time; "objective can be evaluated in polynomial [time]" is a loose version, and "time" is missing. "initial algorithm" should presumably be "initial solution". The "Exact alg."/"Heuristic alg." lines are as written (presumably: the goal of research is to make exact algorithms work on bigger problems and heuristics give better solutions). A few stray dots near the bottom.]

*Figure:* none.

---

### HW 57 (`20261122_005244.jpg`): Simulated annealing

**Simulated annealing**

**Def.**
```
s = s_0                 initial solution
e = E(s)                initial objective
s_b = s, e_b = e        keep track of current best solution + objective

for k ∈ {1, …, k_max}:
    s' = random-neighbour(s)
    e' = E(s')
    if e' < e_b:
        s_b = s, e_b = e
    if P(e, e', temp(e)) > random()
        s = s', e = e'
(where temp(e) = exp((e − e')/Tα^k))
```
In LaTeX: acceptance if $\Prob(e, e', \mathrm{temp}(e)) > \mathrm{random}()$, where $\mathrm{temp}(e) = \exp\bigl((e - e')/T\alpha^k\bigr)$.

[Pseudocode as written (indentation as on the page). The exponent of $\alpha$ is written over a blot with a small "k" above it; read as $\alpha^k$. $T$ and $\alpha$ (initial temperature and cooling factor) are not defined. possible error: inside "if $e' < e_b$" the update should be $s_b = s'$, $e_b = e'$ (the new point), not $s, e$. possible error: the formula labelled "temp(e)" is the acceptance probability $P(e, e', T_k) = \exp((e - e')/T_k)$ with temperature $T_k = T\alpha^k$; as written the names are mixed up. Minimisation is assumed ($e' < e_b$ is better).]

**Ex.** Consider the travelling salesman problem.

*Figure (six cities):* six small hollow circles, each labelled with a number, roughly on a hexagon: 1 at the far left (middle height); 2 upper-left and 6 lower-left (same horizontal position, about a third of the way across); 3 upper-right and 5 lower-right (same horizontal position, about two-thirds across); 4 at the far right (middle height, slightly above 5). Approximate coordinates: 1 $(0, 0.5)$, 2 $(0.3, 0.9)$, 6 $(0.3, 0.1)$, 3 $(0.75, 0.9)$, 5 $(0.75, 0.1)$, 4 $(1, 0.55)$. No edges drawn.

One path can be $1, 2, 5, 4, 3, 6$; [5 and 3 marked with brackets below] can swap → $1, 2, 3, 4, 5, 6$ [3 and 5 marked with brackets above].

Simulated annealing is used to find a solution.

[The swap of two cities in the tour is the neighbourhood move (not named as such).]

---

### HW 58 (`20261122_005302.jpg`): Past exam I (Q1a) (1)

**[Past exam I] (Q1a)** [The heading gives the exam's year; omitted under the no-dates rule. Three past exams are worked in the notes; they are called I, II and III here, in the order they appear (I is the most recent). I: HW 58–69; II: HW 70–73 and 80; III: HW 74–79.]

**Question 1.**

Maximise $z = 2x_1 + x_2$, subject to:
$$2x_1 + 3x_2 + x_3 = 10, \qquad 4x_1 + x_2 + x_4 = 10, \qquad x_1 + 4x_2 + x_5 = 13$$

Assume we have a current basis of $x_1, x_3, x_5$.
You may use the following equations:
$$\begin{bmatrix}2&1&0\\4&0&0\\1&0&1\end{bmatrix}\begin{bmatrix}0&\tfrac14&0\\1&-\tfrac12&0\\0&-\tfrac14&1\end{bmatrix} = \mat I, \qquad \begin{bmatrix}2&3&0\\4&1&0\\1&4&1\end{bmatrix}\begin{bmatrix}-\tfrac1{10}&\tfrac3{10}&0\\\tfrac25&-\tfrac15&0\\-\tfrac32&\tfrac12&1\end{bmatrix} = \mat I$$

**(a)** What is the basic feasible solution at this stage? What is the objective value?

Express constraints as $\mat A\vect x = \vect b$:
$$\mat A = \begin{bmatrix}2&3&1&0&0\\4&1&0&1&0\\1&4&0&0&1\end{bmatrix}, \qquad \vect b = \begin{bmatrix}10\\10\\13\end{bmatrix}$$

[Non-negativity is not written in the question. Checked: both products equal $\mat I$. The first $x$ in "$4x_1$" is written like "$x_4$". A blue sticky tab at the top right hides nothing.]

*Figure:* none.

---

### HW 59 (`20261122_005305.jpg`): Past exam I (Q1a) (2)

**[Past exam I] (Q1a)**

Restrict to the basis $\{1,3,5\}$.
The submatrix $\mat B$ (given by 1st, 3rd, 5th columns of $\mat A$) can be found and inverted with the first hint:
$$\mat B = \begin{bmatrix}2&1&0\\4&0&0\\1&0&1\end{bmatrix} \to \mat B^{-1} = \begin{bmatrix}0&\tfrac14&0\\1&-\tfrac12&0\\0&-\tfrac14&1\end{bmatrix}$$

We can now find the basic feasible solution by using the formula below:
$$\vect x^B = \mat B^{-1}\vect b = \begin{bmatrix}0&\tfrac14&0\\1&-\tfrac12&0\\0&-\tfrac14&1\end{bmatrix}\begin{bmatrix}10\\10\\13\end{bmatrix} = \begin{bmatrix}2.5\\5\\10.5\end{bmatrix}$$

We now return to the objective function $z = \vect c\T\vect x$.
Restrict $\vect c$ to the basis $\{1,3,5\}$ to find $\vect c^B$:
$$\vect c = \begin{bmatrix}2\\1\\0\\0\\0\end{bmatrix} \to \vect c^B = \begin{bmatrix}2\\0\\0\end{bmatrix}$$

The current objective value is given by $z^B = (\vect c^B)\T\vect x^B$.
$$z^B = [2\ 0\ 0]\begin{bmatrix}2.5\\5\\10.5\end{bmatrix} = 5.$$

[Checked: correct.]

*Figure:* none.

---

### HW 60 (`20261122_005311.jpg`): Past exam I (Q1b) (1)

**[Past exam I] (Q1b)**

**(b)** For the next step of the revised simplex algorithm, what is the entering and leaving variable?

First compute the dual variables:
$$\vect y = (\mat B^{-1})\T\vect c^B = \begin{bmatrix}0&1&0\\\tfrac14&-\tfrac12&-\tfrac14\\0&0&1\end{bmatrix}\begin{bmatrix}2\\0\\0\end{bmatrix} = \begin{bmatrix}0\\\tfrac12\\0\end{bmatrix}$$

Then compute the reduced costs of the two non-basic variables. This is given by [blot] $c'_j = c_j - \vect y\T\vect p^j$, where $\vect p^j$ is the $j$th column of matrix $\mat A$.
$$c'_2 = c_2 - \vect y\T\vect p^2 = 1 - [0\ 0.5\ 0]\begin{bmatrix}3\\1\\4\end{bmatrix} = 0.5 \qquad c'_4 = c_4 - \vect y\T\vect p^4 = 0 - [0\ 0.5\ 0]\begin{bmatrix}0\\1\\0\end{bmatrix} = -0.5$$

The <u>only</u> (normally highest) variable with a positive reduced cost is $x_2$, so $x_2$ enters the basis.

The entering variable is therefore $x_2$.

[Checked: correct.]

*Figure:* none.

---

### HW 61 (`20261122_005314.jpg`): Past exam I (Q1b) (2)

**[Past exam I] (Q1b)**

We now must find which variable leaves the basis, using the ratio test. We first compute $\vect\alpha^2 = \mat B^{-1}\vect p^2$, as we chose $j^* = 2$:
$$\vect\alpha^2 = \begin{bmatrix}0&\tfrac14&0\\1&-\tfrac12&0\\0&-\tfrac14&1\end{bmatrix}\begin{bmatrix}3\\1\\4\end{bmatrix} = \begin{bmatrix}0.25\\2.5\\3.75\end{bmatrix}$$

Now apply the ratio test on the (original) basic variables:
$$\frac{x_1}{\alpha^2_1} = \frac{2.5}{0.25} = 10, \qquad \frac{x_3}{\alpha^2_3} = \frac{5}{2.5} = 2, \qquad \frac{x_5}{\alpha^2_5} = \frac{10.5}{3.75} = 2.8$$

Of the basic variables, $x_3$ attains the minimum value, so $x_3$ leaves the basis.

The leaving variable is therefore $x_3$.

[Checked: correct. The components of $\vect\alpha^2$ are indexed by variable number ($\alpha^2_1, \alpha^2_3, \alpha^2_5$), not by position.]

*Figure:* none.

---

### HW 62 (`20261122_005319.jpg`): Past exam I (Q1c) (1)

**[Past exam I] (Q1c)**

**(c)** What is the new objective value? Verify that the new solution is optimal.

Similarly to in (a), but we update information:
Note that the basis $S = \{1, 2, 5\}$.
$$\mat B = \begin{bmatrix}2&3&0\\4&1&0\\1&4&1\end{bmatrix} \to \mat B^{-1} = \begin{bmatrix}-\tfrac1{10}&\tfrac3{10}&0\\\tfrac25&-\tfrac15&0\\-\tfrac32&\tfrac12&1\end{bmatrix}, \qquad \vect c^B = \begin{bmatrix}2\\1\\0\end{bmatrix}$$
Note the second hint provided $\mat B^{-1}$.

Now use $\vect x^B = \mat B^{-1}\vect b$ for the basic feasible solution, and $z^B = (\vect c^B)\T\vect x^B$ for the new objective value.
$$\vect x^B = \begin{bmatrix}-\tfrac1{10}&\tfrac3{10}&0\\\tfrac25&-\tfrac15&0\\-\tfrac32&\tfrac12&1\end{bmatrix}\begin{bmatrix}10\\10\\13\end{bmatrix} = \begin{bmatrix}2\\2\\3\end{bmatrix}, \qquad z^B = [2\ 1\ 0]\begin{bmatrix}2\\2\\3\end{bmatrix} = 6$$

[Checked: correct.]

*Figure:* none.

---

### HW 63 (`20261122_005323.jpg`): Past exam I (Q1c) (2)

**[Past exam I] (Q1c)**

We use a procedure similarly to in (b) to determine if the solution is optimal. First compute the dual variables:
$$\vect y = (\mat B^{-1})\T\vect c^B = \begin{bmatrix}-\tfrac1{10}&\tfrac25&-\tfrac32\\\tfrac3{10}&-\tfrac15&\tfrac12\\0&0&1\end{bmatrix}\begin{bmatrix}2\\1\\0\end{bmatrix} = \begin{bmatrix}0.2\\0.4\\0\end{bmatrix}$$

Then compute the reduced costs of the non-basic variables.
$$c'_3 = c_3 - \vect y\T\vect p^3 = 0 - [0.2\ 0.4\ 0]\begin{bmatrix}1\\0\\0\end{bmatrix} = -0.2 \qquad c'_4 = c_4 - \vect y\T\vect p^4 = 0 - [0.2\ 0.4\ 0]\begin{bmatrix}0\\1\\0\end{bmatrix} = -0.4$$

As there are no positive reduced costs, the current solution is therefore optimal. The optimal solution and objective value are therefore:
$$\vect x = \begin{bmatrix}2\\2\\0\\0\\3\end{bmatrix}, \qquad z = \vect c\T\vect x = 6$$

[Checked: correct. A small blot under the first line of $c'_3$.]

*Figure:* none.

---

### HW 64 (`20261122_005335.jpg`): Past exam I (Q1d)

**[Past exam I] (Q1d)**

**(d)** Assuming no other changes, what value does the objective coefficient of $x_3$ have to increase by so that $x_3$ is nonzero in the optimal solution?

As $x_3$ is a non-basic variable, its reduced cost needs to become positive for it to be non-zero in the optimal solution. If the cost vector is perturbed by $\Delta$ in the third position, then:
$$\vect c^\Delta = \vect c + \Delta\vect e^3$$

Thus the reduced cost of $x_3$ is given by: (* perturbed)
$$c^{\Delta\prime}_3 = (c_3 + \Delta) - \vect y\T\vect p^3 = c_3 - \vect y\T\vect p^3 + \Delta = c'_3 + \Delta$$

Solving for a positive perturbed reduced cost:
$$c^{\Delta\prime}_3 > 0 \Rightarrow c'_3 + \Delta > 0 \Rightarrow \Delta > -c'_3 \Rightarrow \Delta > 0.2 \quad \text{by (c)}$$

Thus the obj. coeff. of $x_3$ must increase for more than 0.2 in order for $x_3$ to be non-zero in the optimal solution.

Alternatively, in the final iteration of the RSA in (c), the reduced cost of $x_3$ was $c'_3 = -\tfrac15$. Thus the obj. coeff. of $x_3$ must increase by at least $\tfrac15$ so that $x_3$ is non-zero in the optimal solution.

[The asterisk in "(* perturbed)" sits above "reduced". The two conclusions differ: "more than 0.2" vs "at least $\tfrac15$" (at exactly 0.2 there is a tie, and $x_3$ need not enter). Recorded as written.]

*Figure:* none.

---

### HW 65 (`20261122_005340.jpg`): Past exam I (Q1e)

**[Past exam I] (Q1e)**

**(e)** If the RHS of the second constraint is changed to $10 + \delta$ for some small value of $\delta > 0$, what will happen to the value of $z$?

Suppose the second constraint is perturbed by some small $\delta > 0$. Assume that $\delta$ is sufficiently small such that there are no changes to which variables are basic / non-basic. Then the constraint RHS vector $\vect b$ is perturbed as follows:
$$\vect b^\delta = \vect b + \delta\vect e^2$$

The objective value $z$ is likewise perturbed:
$$
\begin{aligned}
z^\delta &= \vect y\T\vect b^\delta = \vect y\T(\vect b + \delta\vect e^2) = \vect y\T\vect b + \delta\vect y\T\vect e^2\\
&= \vect y\T\vect b + \delta y_2 = \vect y\T\vect b + 0.4\delta \quad \text{by (c)}\\
&= z^B + 0.4\delta
\end{aligned}
$$

Hence if the RHS of the second constraint increases by $\delta$, then the objective value increases by $0.4\delta$.

[Checked: correct ($y_2 = 0.4$).]

*Figure:* none.

---

### HW 66 (`20261122_005346.jpg`): Past exam I (Q2a)

**[Past exam I] (Q2a)**

**Question 2.**

Linear and integer programming
See 'Smart Minds Chess School' example.

**(a)**
<u>Sets</u>
- $C$ classes; $\quad I^s \subseteq I$ senior inst.
- $T$ time slots; $\quad C_t \subseteq C$ classes at time $t$, known
- $I$ instructors

<u>Data</u>
- $n_c$ number of instructors required for class $c \in C$
- $v_{ic}$ teaching value of instructor $i \in I$ for class $c \in C$

<u>Vars</u> $x_{ic} = \begin{cases}1 & \text{instructor } i \text{ assigned to class } c\\ 0 & \text{else}\end{cases}$

<u>Obj</u> Maximise $\sum_{i\in I}\sum_{c\in C} v_{ic}x_{ic}$ (max. sum of teaching values of assignments)

<u>Constraints</u>
$$
\begin{aligned}
\sum_{c\in C_t} x_{ic} &\le 1, && \forall i \in I, \forall t \in T && \Big\}\ \text{one time slot, one class, per instr. max.}\\
\sum_{i\in I} x_{ic} &\ge n_c && \forall c \in C && \Big\}\ \text{required \# of instr. per class}\\
\sum_{i\in I^s} x_{ic} &\ge 1 && \forall c \in C && \Big\}\ \text{senior instructor per class min.}
\end{aligned}
$$

[The question's text (the 'Smart Minds Chess School' example) is not in the notes. A yellow sticky tab at the top right hides nothing.]

*Figure:* none.

---

### HW 67 (`20261122_005349.jpg`): Past exam I (Q2b)

**[Past exam I] (Q2b)**

**(b)** We append any required additions:

<u>Constraints</u>
$$\sum_{c\in C} x_{i_1c} - \sum_{c\in C} x_{i_2c} \le 2, \qquad \forall i_1 \in I, \forall i_2 \in I$$

This additional constraint corresponds to the maximum difference between instructors being at most two hours.

["two hours" assumes each class is one hour (not stated). The rest of the page is blank (lowest sharpness score of all photos, from the empty paper; the writing is readable).]

*Figure:* none.

---

### HW 68 (`20261122_005357.jpg`): Past exam I (Q3a)

**Question 3.**

Dynamic programming
See 'Electrigrid' example.

**(a)**
<u>Data</u>
- $d_t$ forecast daily electricity demand (MWh)
- $b$ battery capacity (MWh)
- $c(x)$ cost per MWh

- <u>Stages</u> $t$ days $1 \le t \le T$
- <u>State</u> $s_t$ amount of electricity stored in battery (MWh)
- <u>Actions</u> $a_t$ electricity bought for day $t$
- <u>Contribution</u> $c(a_t)$ cost of electricity bought
- <u>Transition</u> $s_{t+1} = s^M(s_t) = s_t + a_t - d_t$
- <u>Value fn.</u>
  $$V_t(s_t) = \min\{c(a_t) + V_{t+1}(s_t + a_t - d_t)\}$$
  over
  - $a_t \ge 0$ (electricity bought is non-negative)
  - $a_t \ge d_t - s_t$ (meeting demand)
  - $a_t \le b + d_t - s_t$ (less than battery capacity)

Base: $V_{T+1}(s_{T+1}) = 0$ (no costs after day $T$)
Obj: $V_1(0)$

[This page has no "Exam" heading (it continues HW 66–67). In the contribution, the argument $a_t$ is written over a blot with "a" above it. $s^M(s_t)$ omits $a_t$ (HW 41: $s^M(s_t, a_t)$). "$c(x)$ cost per MWh" vs "$c(a_t)$ cost of electricity bought": $c$ is presumably the cost of buying $x$ MWh. The pointer to the 'Electrigrid' example (HW 22, an LP) is as written. Pink sticky tab at the top right hides nothing.]

*Figure:* none.

---

### HW 69 (`20261122_005401.jpg`): Past exam I (Q3b)

**[Past exam I] (Q3b)**

**(b)** We modify / append any required additions:

<u>Data</u>
- $p_t$ probability of extra demand
- $h_t$ higher daily electricity demand

<u>Value fn.</u>
$$V_t(s_t) = \min\left\{\begin{aligned}&c(a_t) +\\ &p_t\cdot V_{t+1}(s_t + a_t - h_t) +\\ &(1 - p_t)\cdot V_{t+1}(\min\{s_t + a_t - d_t, b\})\end{aligned}\right\}$$
[An arrow ↑ with "*" points at the $\min\{\cdot, b\}$.]

over
- $a_t \ge 0$
- $a_t \ge h_t - s_t$
- $a_t \le b + h_t - s_t$ $\quad$ (replace $d_t$ with $h_t$, to meet demand in case of $p_t$)

\* Note that with an increased demand (and thus an increase in $a_t$), there is a chance that we purchase more electricity than can be stored.

[The base case and objective are as in (a) (HW 68). Electricity beyond capacity $b$ is discarded by the $\min$ (presumably; not said).]

*Figure:* none.

---

### HW 70 (`20261122_005407.jpg`): Past exam II (Q2a)

**[Past exam II] (Q2a)** [year omitted]

**Question 2.**

Linear and integer programming
See 'BMC' example.

**(a)**
<u>Sets</u>
- $S$ Stores
- $W$ Warehouses

<u>Data</u>
- $d_s$ demand from store $s \in S$
- $c_w$ cost of establishing warehouse $w \in W$
- $a_{ws}$ cost of supplying store $s \in S$ from warehouse $w \in W$
- $b_w$ capacity of warehouse $w \in W$

<u>Vars</u>
- $x_w \in \{0,1\}$ if established at $w \in W$
- $y_{w,s} \in \{0,1\}$ if store $s \in S$ is supplied by warehouse $w \in W$

<u>Obj</u> Minimise $\sum_{w\in W} c_wx_w + \sum_{s\in S}\sum_{w\in W} a_{ws}y_{ws}$

<u>Cons</u>
$$
\begin{aligned}
\sum_{s\in S} y_{ws}d_s &\le b_w && \forall w \in W && \Big\}\ \text{warehouse capacity}\\
\sum_{w\in W} y_{ws} &\ge 1 && \forall s \in S && \Big\}\ \text{all stores supplied}\\
y_{ws} &\le x_w && \forall w \in W, \forall s \in S && \Big\}\ \text{connect variables}
\end{aligned}
$$

[The 'BMC' example is not in the notes. Yellow sticky tab at the top right hides nothing.]

*Figure:* none.

---

### HW 71 (`20261122_005411.jpg`): Past exam II (Q2b)

**[Past exam II] (Q2b)**

**(b)** We append any required additions:

<u>Sets</u> $S^c \subseteq S$ chain stores [the symbol is written below a blacked-out one]

<u>Data</u> $k$ minimum number of unique warehouses supplying chain stores

<u>Vars</u> $z_w \in \{0,1\}$ if $w \in W$ is supplying a chain store

<u>Cons</u>
$$
\begin{aligned}
\sum_{s\in S^c} y_{ws} &\le 2 && \forall w \in W && \Big\}\ \text{no more than two chain stores supplied by same warehouse}\\
\sum_{w\in W} z_w &\ge k && && \Big\}\ k \text{ constraint}\\
\sum_{s\in S} y_{ws} &\ge z_w && && \Big\}\ \text{connect variables}
\end{aligned}
$$

[Blots: in the first constraint, the subscript of $y$ and the index line under the sum are partly blacked out (rewritten as $y_{ws}$, $s \in S^c$). "$\forall w \in W$" is written like "$\forall v \in U$". Beside the last constraint is a vertical hooked arrow (┐ down to ↓) pointing at a fully cross-hatched box below it (crossed-out content). possible error: the connecting constraint should sum over chain stores, $\sum_{s\in S^c} y_{ws} \ge z_w$ ($\forall w \in W$), since $z_w$ means "supplies a chain store".]

*Figure:* none.

---

### HW 72 (`20261122_005416.jpg`): Past exam II (Q3a)

**[Past exam II] (Q3a)**

**Question 3.**

Dynamic programming
See 'Running' example.

**(a)**
- <u>Data</u> $p_f = \dfrac{1}{2 + f}$ probability of winning a race with fatigue $f$
- <u>Stage</u> $t$ races done
- <u>State</u> $f$ fatigue score
- <u>Action</u> $a \in \{0,1\}$ if race
- <u>Value fn.</u> $V_t(f)$ is the expected number of races won after $t$ races with fatigue score $f$.

Base: $V_T(f) = 0$
Obj: $V_0(0)$
$$V_t(f) = \max\begin{cases}\dfrac{1}{2+f} + V_{t+1}(f + 3) & \text{if race}\\ V_{t+1}(\max\{0, f - 4\}) & \text{if rest}\end{cases}$$

["expected number of races won after $t$ races" means won in the remaining races, after $t$ are done. The fatigue rules (+3 for racing, −4 for resting, floor 0) are read from the recursion. Pink sticky tab top right.]

*Figure:* none.

---

### HW 73 (`20261122_005421.jpg`): Past exam II (Q3b)

**[Past exam II] (Q3b)**

**(b)** Suppose she starts a season of four races with fatigue score 0. Which races should she enter? What is her expected number of wins?

*Figure (decision tree):* a binary tree drawn top-down, each node a value expression with its value in square brackets beneath.
- Root: $V_0(0)$ $[\tfrac{12}{10}]$.
- Root's left child: $\tfrac12 + V_1(3)$ $[\tfrac12 + \tfrac7{10}]$; right child: $V_1(0)$ $[1]$. A small arrow ↗ under the root points back up from the left branch (the chosen branch).
- Children of $\tfrac12 + V_1(3)$: left $\tfrac15 + V_2(6)$ $[\tfrac9{20}]$, right $V_2(0)$ $[\tfrac7{10}]$; an arrow ↖ under the node points back up from the right child (chosen).
- Children of $V_1(0)$: left $\tfrac12 + V_2(3)$ $[1]$, right $V_2(0)$ $[\tfrac7{10}]$; an arrow ↗ points back up from the left child (chosen).
In each pair the left edge is "race" and the right edge "rest" (not labelled on the page).

Thus we have three cases:
$$
\begin{aligned}
V_2(0) &= \max\{\tfrac12 + V_3(3), V_3(0)\} = \max\{\tfrac12 + \tfrac15, \tfrac12\} = \tfrac7{10}\\
V_2(3) &= \max\{\tfrac15 + V_3(6), V_3(0)\} = \max\{\tfrac15 + \tfrac18, \tfrac12\} = \tfrac12\\
V_2(6) &= \max\{\tfrac18 + V_3(9), V_3(2)\} = \max\{\tfrac18 + \tfrac1{11}, \tfrac14\} = \tfrac14
\end{aligned}
$$
from the assumption that you may as well run the last race.
Now work up the 'tree' to find the solution.
Thus she should enter the first race, rest the second race, and run the two remaining races.
This gives $12/10 = 1.2$ expected wins.

Note we could have assumed to run on 0 fatigue.

[In $V_2(0)$ the first term is written "$V_z(3)$" over a correction; $V_3(3)$ is meant. Checked: all values correct ($V_3(f) = 1/(2+f)$; $V_1(3) = \max\{9/20, 7/10\} = 7/10$; $V_1(0) = \max\{1, 7/10\} = 1$; $V_0(0) = \max\{6/5, 1\} = 1.2$). Part (c) is on HW 80.]

---

### HW 74 (`20261122_005429.jpg`): Past exam III (Q2a)

**[Past exam III] (Q2a)** [year omitted]

**Question 2.**

Linear and integer programming
See 'Grid Ball' example.

**(a)**
<u>Sets</u>
- $C$ cities; $\quad S_p \subseteq S$ squares that player $p$ can play
- $P$ players; $\quad P_c \subseteq P$ players from city $c$
- $S$ squares

<u>Data</u>
- $r_p$ rating (1–100) of player $p \in P$
- $a_p$ cost of player $p \in P$
- $b$ total budget
- minCity minimum number of cities represented in one team
- maxCity maximum number of players from one city in team

<u>Vars</u>
- $x_{ps} \in \{0,1\}$ if player $p$ plays in square $s$
- $y_c \in \{0,1\}$ if city $c$ rep. in team

<u>Obj</u> Maximise $\sum_{p\in P}\sum_{s\in S} x_{ps}r_p$ (max. total rating)

<u>Cons</u>
$$
\begin{aligned}
\sum_{p\in P} x_{ps} &= 1 && \forall s \in S && \text{(one player per square)}\\
\sum_{s\in S\setminus S_p} x_{ps} &= 0 && \forall p \in P && \text{(players cannot play in some squares)}\\
\sum_{p\in P}\sum_{s\in S} x_{ps}a_p &\le b && && \text{(within budget)}
\end{aligned}
$$
[continued on HW 75]

[No constraint that a player fills at most one square is written ($\sum_s x_{ps} \le 1$). Yellow sticky tab top right.]

*Figure:* none.

---

### HW 75 (`20261122_005435(0).jpg`) and HW 76 (`20261122_005435.jpg`): Past exam III (Q2b)

[HW 75 and HW 76 are two shots of the same page (same second, slightly different framing); both are fully legible. Transcribed once.]

**[Past exam III] (Q2b)**

<u>Cons</u> [continuing (a)]
$$
\begin{aligned}
\sum_{c\in C} y_c &\ge \text{minCity} && \text{(minCity constraint)}\\
\sum_{p\in P_c}\sum_{s\in S} x_{ps} &\le \text{maxCity}, \quad \forall c \in C && \text{(maxCity constraint)}\\
\sum_{p\in P_c}\sum_{s\in S} x_{ps} &\ge y_c \quad \forall c \in C && \text{(link } x_{ps} \text{ and } y_c)
\end{aligned}
$$

**(b)** We modify/append any additions:

<u>Sets</u> $A \subset S\times S$ set of all pairs of adj. squares

<u>Vars</u> $z_{(a,b)c} \in \{0,1\}$ if bonus rating from pair $(a,b) \in A$ from city $c$

<u>Obj</u> Maximise $\sum_{p\in P}\sum_{s\in S} x_{ps}r_p + \sum_{c\in C}\sum_{(a,b)\in A} z_{(a,b)c}$

<u>Cons</u> We want to do
$$\sum_{p\in P_c} x_{p,a}\sum_{p\in P_c} x_{p,b} = z_{(a,b),c}.$$
However, this is not linear. Thus we do the logically equivalent alternative:
$$
\begin{aligned}
z_{(a,b)c} &\le \sum_{p\in P_c}(x_{p,a})\\
z_{(a,b)c} &\le \sum_{p\in P_c}(x_{p,b})\\
z_{(a,b)c} &\ge \sum_{p\in P_c} x_{p,a} + \sum_{p\in P_c} x_{p,b} - 1 \qquad \forall c \in C.
\end{aligned}
$$

[The (a) constraints continue at the top under "Cons" before part (b) starts. The size of the bonus is not given (the objective adds $z$ with weight 1). The range "$\forall (a,b) \in A$" is not written on the last three constraints. The first sum's subscript is written "$x_{p,a}$" with an "a" that can look like "c"; $a$ is meant.]

*Figure:* none.

---

### HW 77 (`20261122_005441.jpg`): Past exam III (Q3a)

**[Past exam III] (Q3a)**

**Question 3.**

Dynamic programming
See 'Farmer' example.

**(a)**
- <u>Data</u> $p_t$ profit per sheep, sold in year $t$
- <u>Stages</u> $t$ years $1 \le t \le T$
- <u>State</u> $s_t$ number of sheep at start of year $t \in T$
- <u>Action</u> $a_t$ number of sheep to sell in year $t \in T$
- <u>Value fn</u>
  $$V_t(s_t) = \max\{[\text{blot}]\ a_tp_t + V_{t+1}(2(s_t - a_t))\}$$
  over $0 \le a_t \le s_t$

Base: $V_T(s_T) = s_Tp_T$ [the $s$ written above a blacked-out letter]
Obj: $V_1(k)$

[The flock doubles each year ($2(s_t - a_t)$), read from the recursion. $k$ (initial number of sheep) is not defined. Pink sticky tab top right.]

*Figure:* none.

---

### HW 78 (`20261122_005445.jpg`): Past exam III (Q3b) (1)

**[Past exam III] (Q3b)**

**(b)** This is a wholly separate problem to in (a).

<u>Data</u>
- $m_s$ expected profit in given year, given state $s$ of soil $\{700, 400\}$
- $c$ cost of applying fertiliser for one year
- $P_{sa}$ probability of good / poor quality given state, action

- <u>Stages</u> $t$ years $1 \le t \le T$
- <u>State</u> $s_t$ soil condition $\{\text{good}, \text{poor}\}$
- <u>Action</u> $a_t$ apply fertiliser or not $\{\text{True}, \text{False}\}$
- <u>Value fn</u> $V_t(s_t)$: max profit from year $t$ to $T$, given soil quality $s_t$ at start of year $t$.

$$V_t(s_t) = \max\begin{cases}[\text{hatched}]\ m_s + P_{\text{good,no}}V_{t+1}(\text{good}) + P_{\text{poor,no}}V_{t+1}(\text{poor}) & \text{if False}\\ m_s + P_{\text{good,yes}}V_{t+1}(\text{good}) + P_{\text{poor,yes}}V_{t+1}(\text{poor}) - c & \text{if True}\end{cases}$$

Base: $V_T(s_T) = \max\begin{cases}m_s & \text{if True}\\ m_s - c & \text{if False}\end{cases} = m_s$ (False)

Obj: $V_1(s_1)$

[possible error: in the base case the labels are swapped: $m_s$ is "if False" (no fertiliser) and $m_s - c$ "if True"; the conclusion "$= m_s$ (False)" matches the corrected labels. A small "?" sits after "if True". The transition probabilities $P_{\text{good,no}}$ etc. also depend on the current state $s_t$ (subscript omitted); their values are only on HW 79.]

*Figure:* none.

---

### HW 79 (`20261122_005452.jpg`): Past exam III (Q3b) (2)

**[Past exam III] (Q3b, continued)**

**(b)** Suppose there are two years before the gardener retires. Should he fertilise his garden?

There are only two years; 1 and $2 = T$.
Thus,
$$V_2(\text{good}) = 700, \qquad V_2(\text{poor}) = 400$$
[An arrow ↙ from "$2 = T$" points at these values.]

If $s_1 = $ good:
$$
\begin{aligned}
V_1(\text{good}) &= \max\begin{cases}700 + 0.4V_2(\text{good}) + 0.6V_2(\text{poor}) & \text{F}\\ 700 - 150 + 0.2V_2(\text{poor}) + 0.8V_2(\text{good}) & \text{T}\end{cases}\\
&= \max\begin{cases}700 + 0.4(700) + 0.6(400) & \text{F}\\ 700 - 150 + 0.2(400) + 0.8(700) & \text{T}\end{cases} = \max\begin{Bmatrix}1220\\1190\end{Bmatrix} = 1220 \text{ F}
\end{aligned}
$$

If $s_1 = $ bad:
$$
\begin{aligned}
V_1(\text{bad}) &= \max\begin{cases}400 + 0.1V_2(\text{good}) + 0.9V_2(\text{poor}) & \text{F}\\ 400 - 150 + 0.6V_2(\text{good}) + 0.4V_2(\text{poor}) & \text{T}\end{cases}\\
&= \max\begin{cases}400 + 0.1(700) + 0.9(400) & \text{F}\\ 400 - 150 + 0.6(700) + 0.4(400) & \text{T}\end{cases} = \max\begin{Bmatrix}830\\830\end{Bmatrix} = 830 \sim
\end{aligned}
$$
[Under $V_1(\text{bad})$: "↕ poor" (bad = poor).]

Therefore, if the soil quality is good, he should not fertilise. If the soil quality is poor, the action does not matter.
On his second year he should not fertilise.

[Data used: $c = 150$; transition probabilities (to good / to poor): good & no fertiliser 0.4 / 0.6, good & fertiliser 0.8 / 0.2, poor & no 0.1 / 0.9, poor & fertiliser 0.6 / 0.4. Checked: all four totals are correct. "$\sim$" after 830 marks the tie.]

*Figure:* none.

---

### HW 80 (`20261122_005459.jpg`): Past exam II (Q3c)

**[Past exam II] (Q3c)** [follows HW 73; photographed last]

**(c)** This is a related, but separate problem to in (a).

- <u>Extra state</u> $w$ number of wins
- <u>Value function</u> $V_t(f, w)$: max. prob. of finishing season with 3 wins given $w$ wins, $f$ fatigue after $t$ races

Base: $V_T(f, w) = \begin{cases}1 & \text{if } w \ge 3\\ 0 & \text{if not}\end{cases}$ $\quad$ (or) $V_t(f, 3) = 1$

Obj: $V_0(0, 0)$

$$V_t(f, w) = \max\begin{cases}\dfrac{1}{2+f}\bigl(0.5V_{t+1}(f+3, w+1) + 0.5V_{t+1}(f+2, w+1)\bigr)\\ \quad + \bigl(1 - \tfrac{1}{2+f}\bigr)\bigl(0.5V_{t+1}(f+3, w) + 0.5V_{t+1}(f+2, w)\bigr) & \text{run}\\ V_{t+1}(\max\{0, f-4\}, w) & \text{rest}\end{cases}$$

Note that when she runs, there are two separate events: the probability of winning $\left(\tfrac{1}{2+f}\right)$ and the probability of decreased fatigue (0.5). We thus have four terms to sum over, and four different value function possibilities.

[The labels "run" and "rest" are in the left margin with small tick marks pointing at the two branches. The $f$ in the base case $V_T(f, w)$ looks like "3" (same glyph as the other $f$'s on the page). In part (c) racing raises fatigue by 3 or 2 with probability 0.5 each ("decreased fatigue" = the +2 case), read from the formula; the question text is not in the notes.]

*Figure:* none.

---
