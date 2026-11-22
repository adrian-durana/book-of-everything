# Coverage inventory: MATH3404 Optimisation Theory

_Built from 85 photos of the handwritten notes (the only source so far). The textbook the notes follow will be added later as a supplement. The semester the course was taken is not recorded in the material._

**Sources.** "HW nn" means photo nn (one notebook page per photo, in shooting order); the transcription is in `claude/notes-math3404-1.md` (HW 01–19), `-2.md` (HW 20–53) and `-3.md` (HW 54–85). There are no typed notes or slides. **Code:** none in the notes. Part V uses **Python**. **Content rule:** source material only, with corrections.

**Status:** ✅ written, ◻ to do. **↔ merge** = overlaps a chapter that another course also feeds (merge, don't duplicate). Section numbers below are proposals for chapters that have no sections yet; `tools/chapters.py` lists chapters only.

**Target chapters.** HW 02–19 (optimisation in $\R$ and $\R^n$) belong to Part V's optimisation chapters, Ch 62 *Unconstrained Optimisation* and Ch 63 *Constrained Optimisation and Duality* (both led by MATH3204), with the one-variable and Taylor material ↔ Ch 11 and Ch 15. HW 20–53 → **Ch 65 Calculus of Variations**. HW 54–85 → **Ch 66 Optimal Control**. Nothing overlaps the written chapters 25–31 (Probability).

**Note on Ch 62/63.** MATH3204 has not been ingested yet, so the merge into Ch 62–63 can't be planned in detail. These items are listed here so the hub can decide: either merge them into Ch 62–63 when MATH3204 arrives, or open Ch 65 with a short section "Classical optimisation in $\R^n$" (the notes treat it as the course's introduction and lean on it later; e.g. HW 44 "symbolically the same as the Lagrange multiplier method", HW 48 compares the sufficiency conditions).

---

## Ch 11 Differentiation (`ch:differentiation`): ↔ merge (MATH1071, MATH2400, MATH2401)
### §11.3 Extrema and mean value theorems (see `claude/inventory-math1071.md`)
- ◻ Global and local minimum on $I \subseteq \R$; "similar for maxima" (HW 02) ↔ merge (MATH1071 Def 5.2.1). Local-minimum definition has the inclusion reversed (see errors)
- ◻ Th. 1.1 local min ⟹ $f'(\bar x) = 0$, proof via Taylor with the Lagrange remainder, cases $h > 0$, $h < 0$ (HW 02–03) ↔ merge (MATH1071/2400 give two other proofs; pick one)
- ◻ Th. 1.2 first-derivative test for a local minimum; proof "reverse direction, use MVT" (HW 03); Ex. $x^2$ on $(-1, 1)$ (HW 03)
- ◻ Th. 1.3 higher-order derivative test ($f' = \dots = f^{(m-1)} = 0$, $m$ even, $f^{(m)} > 0$), proof via Taylor (HW 04) ↔ merge (MATH1071 second-derivative test is typed only)
- ◻ Def. critical point ($f' = 0$ or $f'$ does not exist) (HW 04)
- ◻ Th. 1.4 sign-change test without differentiability at $\bar x$ (HW 05); Rems: closed intervals (endpoints), piecewise continuous $f$ (HW 05)
- ◻ Method: procedure to find a global minimum on $I$ (stationary points, discontinuities of $f$ or $f'$, endpoints, compare) (HW 05)

## Ch 15 Differential Calculus in Several Variables (`ch:differential-calculus-several-variables`): ↔ merge (MATH2401, MATH1072, MATH2001, MATH2400)
### §15.x Taylor's theorem in several variables
- ◻ Gradient $\nabla f(a)$, Hessian $H_f(a)$ recalled; multivariate Taylor $f(a + \varepsilon h) = f(a) + \varepsilon h\T\nabla f(a) + \frac{\varepsilon^2}{2} h\T H_f(a) h + O(\varepsilon^3)$ (HW 06) ↔ merge (MATH2001 form, which the notes quote in a Rem.)
- ◻ Proof via $g(\varepsilon) = f(a + \varepsilon h)$, one-variable Taylor and the chain rule (HW 09)
### §15.y Extrema in several variables
- ◻ Th. 2.1 local min ⟹ $\nabla f(a) = \vect 0$, "similar to single-variable case" (HW 07); Ex. $x_1^2 + x_2^2$ (HW 07)
- ◻ Th. 2.2 sufficient condition $\nabla f(a) = \vect 0$, $h\T H_f(a) h > 0$, proof via Taylor and the eigenvalue bound (HW 07); Lem. 2.3 quadratic form positive iff eigenvalues positive (HW 07); Cor. 2.4 local max (HW 07)
- ◻ Ex. $x_1^2 - x_2^2$ (saddle: $\det H_f = -4$) (HW 08); exercises $(x_1^2 - 4)^2 + x_2^2$ and $x_1^3 + x_2^3 + 3x_1^2 - 3x_2^2 - 8$ (statements only, no working) (HW 08)
- These may instead go to Ch 62 (optimality conditions) once MATH3204 is in; the hub decides.

## Ch 7 Eigenvalues, Diagonalisation and Quadratic Forms (`ch:eigenvalues-diagonalisation`): ↔ merge (MATH1071, MATH2001)
- ◻ Proof that $h\T H h \ge \min_i \lambda_i$ for $\norm h = 1$ ($H$ symmetric ⟹ orthogonally diagonalisable, $y = Q\T h$) (HW 08). Used in Th. 2.2; the result itself belongs with quadratic forms (link from Ch 15/62)

## Ch 62 Unconstrained Optimisation (`ch:unconstrained-optimisation`): ↔ merge (MATH3204)
- ◻ Problem statement: extrema of $f$ on $K \subseteq \R^n$ (HW 06). The optimality conditions above (Th. 2.1–2.4) are the overlap with MATH3204; see Ch 15 note

## Ch 63 Constrained Optimisation and Duality (`ch:constrained-optimisation`): ↔ merge (MATH3204; MATH1072 for the two-variable Lagrange rule)
### §63.x Equality constraints and Lagrange multipliers
- ◻ Problem: minimise $f$ subject to $g_j(x) = c_j$, $j = 1, \dots, m < n$ (HW 10)
- ◻ Def. Lagrange multiplier (contours parallel, $\nabla f = \lambda\nabla g$, "from MATH1072") (HW 10) ↔ merge (MATH1072)
- ◻ Th. 3.1 Lagrange multiplier theorem, $\nabla(f + \sum\lambda_j g_j) = 0$ at $a$; proof via tangent vectors $h\T\nabla g_j(a) = 0$, splitting $h$ into $(h_1, \dots, h_m)$ and $(h_{m+1}, \dots, h_n)$ (HW 10–11). Missing hypothesis (independent constraint gradients) — see errors
- ◻ Ex. $1 - x_1^2 - x_2^2$ subject to $x_1^2 + x_2 = 1$: two solutions (HW 12)
- ◻ Ex. $x_1^3 + x_2^3 + x_3^3$ subject to two spheres: critical-point equations (HW 13), continued below
### §63.y Second-order conditions: bordered Hessian
- ◻ Lagrangian $L$, Hessian $H_L$; $B = \nabla g$ ($n \times m$); bordered Hessian $\begin{psmallmatrix} H_L & B \\ B\T & O\end{psmallmatrix}$; Def. non-degenerate critical point ($\nabla L = 0$, $\det H \ne 0$) (HW 14)
- ◻ Th. 3.2 local min iff $h\T H_L h \ge 0$ on the tangent space; Cor. local max; Cor. "the equality cannot hold" (HW 15)
- ◻ Proof of Th. 3.2: Step 1 (Taylor of $L$, EVT on the unit tangent set), Step 2 (contradiction via the bordered Hessian) (HW 16–17). Logic needs tidying — see errors
- ◻ Method: the five steps (Lagrangian, critical points, non-degeneracy, tangent space, sign of $h\T H_L h$) (HW 18)
- ◻ Ex. (cont.) at $(1, 0, 2)$: $H_L$, $B$, $H$, $\det H \ne 0$, tangent space $h = (0, \mu, 0)$, $h\T H_L h = -6\mu^2$ ⟹ local max; other critical points left (HW 18–19)

---

## Ch 65 Calculus of Variations (`ch:calculus-of-variations`): new (MATH3404 only)
### §65.1 Functionals and the basic problem
- ◻ Ex. curve between two fixed points; arc length $L[x] = \int\sqrt{1 + \dot x^2}\dd t$ (HW 20) — **Figure 65.a** (curve from $(t_0, \vec x_0)$ to $(t_1, \vec x_1)$) (HW 20)
- ◻ Ex. three motivating problems: isoperimetric, minimum energy, brachistochrone (HW 20) — keep one or two as motivation (STYLE: one motivating example per section)
- ◻ Def. function, functional (HW 21); the problem $\min J[x] = \int_{t_0}^{t_1} f(t, x, \dot x)\dd t$ with fixed endpoints; scalar $x(t)$ only (Rem.); why a notion of closeness is needed (HW 21)
- ◻ Def. admissible curves ($C^2$, end conditions) (HW 22)
- ◻ Def. weak variation, strong variation (HW 22)
- ◻ Def. weak local minimiser, strong local minimiser (HW 22)
### §65.2 The Euler–Lagrange equation
- ◻ Th. 4.1 Euler–Lagrange equation (necessary condition) (HW 23)
- ◻ Def. critical point of $J$; Def. extremals (HW 23)
- ◻ Rem. second form when $f$ has no explicit $t$: $f - \dot x f_{\dot x} = c$ (Beltrami identity; notes spell "Beltrani") (HW 23)
- ◻ Proof of E–L via $F(\varepsilon) = J(x^* + \varepsilon\eta)$, $F'(0) = 0$, integration by parts, choice $\eta = (t - t_0)^3(t - t_1)^3(\ldots)$ (HW 24–25)
- ◻ Proof of the second form (HW 25)
- ◻ Alternative derivation ("fixed endpoint problem"): $0 \le J[y] - J[x^*]$, Taylor, integration by parts, then the lemma (HW 30); supporting lemmas: Taylor (L.), integration by parts (L.) (HW 31). Two proofs of the same result (HW 24–25 and HW 30–31): pick one, or keep the FLCV version as the main proof
- ◻ Lemma: fundamental lemma of the calculus of variations, with proof by a bump function $\eta$ (HW 31)
- ◻ Ex. $\int_1^2 \dot x^2 t^3$, $x(1) = 0$, $x(2) = 3$ ⟹ $x = 4 - 4/t^2$ (HW 26); reused in HW 36, 39, 51
- ◻ Ex. $\int_0^1 (t\dot x + \dot x^2)$ ⟹ $x = -\frac14 t^2 + 2t + 1$ (HW 27)
- ◻ Ex. $\int_0^1 (1 + t^2)\dot x^2$ ⟹ $x = 2\arctan t + \pi/2$ (HW 27)
### §65.3 The brachistochrone
- ◻ Set-up: time functional $T[x] = \frac{1}{\sqrt{2g}}\int_0^a \sqrt{1 + \dot x^2}/\sqrt x\dd t$ from energy/force balance (HW 28) — **Figure 65.b** (brachistochrone, $x$ downwards, $B = (a, b)$, force $mg$) (HW 28)
- ◻ Solution via the second form, $\dot x = \tan\theta$; parametric solution $x = k(1 + \cos 2\theta)$, $t = \ell - k(2\theta + \sin 2\theta)$ (HW 29). The word "cycloid" is not in the notes
### §65.4 Variable endpoints and transversality
- ◻ Def. variable endpoint problem: end on a curve $x = c(t)$, $t_1$ unknown (HW 32) — **Figure 65.c** (variable endpoint on a curve) (HW 32)
- ◻ Def. transversality condition $f + (\dot c - \dot x^*) f_{\dot x} = 0$ at $t_1$; the three conditions (HW 32)
- ◻ Special case 1 ($c$ constant): $f - \dot x^* f_{\dot x} = 0$ — **Figure 65.d** (HW 33)
- ◻ Special case 2 ($t_1$ known, $x(t_1)$ free): $f_{\dot x}(t_1) = 0$, as the limit $\dot c \to \infty$ — **Figure 65.e** (HW 33)
- ◻ Proof of the transversality condition ($\Delta T$, $\varepsilon\eta(t_1) = (\dot c - \dot x^*)\Delta T$, first variation) (HW 34–35)
- ◻ Ex. $\int_1^T \dot x^2 t^3$, end on $c(t) = 2/t^2 - 3$ ⟹ $k = 4$, $T = \sqrt2$ (HW 36)
- ◻ Ex. $\int_0^T (x^2 + \dot x^2)$: (i) $T = 2$, $x(2)$ free ⟹ $\cosh(t - 2)/\cosh 2$; (ii) $x(T) = 2$ ⟹ $x = e^t$, $T = \ln 2$; (iii) $x(0) = 0$, $x(T) = 2$ ⟹ no extremal (HW 37–38)
### §65.5 Corner curves
- ◻ Def. $D_1$ (continuous, piecewise smooth) curves; corner slopes $p_1$, $p_2$ (HW 40)
- ◻ Th. necessary conditions for a $D_1$ minimiser: E–L between corners, $f_{\dot x}$ and $f - \dot x f_{\dot x}$ continuous at corners (HW 40). Stated without proof. (Weierstrass–Erdmann conditions; not named in the notes)
- ◻ Ex. $\int_0^4 x^2(\dot x - 1)^2$, $x(0) = 0$, $x(4) = 2$: smooth extremal fails for $t < 3$; corner curve $x = 0$ then $t - 2$ with $J = 0$ (HW 41)
- ◻ Ex. $\int_0^2 \dot x^2(1 - \dot x)^2$: $x = t/2$ is not a minimiser; corner conditions force slopes $\{0, 1\}$ (HW 42); non-unique minimisers — **Figure 65.f** (two zig-zag paths and a staircase from $(0,0)$ to $(2,1)$) (HW 43)
### §65.6 Isoperimetric problems
- ◻ Problem with an integral constraint $I[x] = c$; Th. $x^*$ is an extremal of $J + \lambda I$ (stated without proof); Rem. three constants; Rem. origin of the name (HW 44) ↔ link (Ch 63 Lagrange multipliers; the notes call it "symbolically the same")
- ◻ Ex. $\int_0^1 \dot x^2$ with $\int_0^1 x = 1$ ⟹ $x = 12t^2 - 10t + 2$ (HW 45)
- ◻ Ex. maximum area under a curve of length $\pi$ from $(0,0)$ to $(2,0)$ ⟹ upper unit semicircle about $(1, 0)$ (HW 46–47)
### §65.7 Sufficient conditions
- ◻ Comparison of necessary/sufficient conditions in $\R^2$ and in the calculus of variations; first and second variations $V_1$, $V_2$ (HW 48) — a two-column table (HW 48) ↔ link (Ch 15 / §63.y)
- ◻ Ex. $\int_0^1 1/\dot x$: $V_2 > 0$ but $x = t$ is not a minimiser (piecewise-linear $y$ with $J = -1/3$) (HW 49)
- ◻ Ex. direct check that $x = 4 - 4/t^2$ minimises $\int_1^2 \dot x^2 t^3$ ($\Delta J = \int \dot\eta^2 t^3 \ge 0$) (HW 39)
- ◻ Def. field of extremals (one-parameter family, simple cover, slope function $p(t, x)$) (HW 50)
- ◻ Ex. fields for $\int_1^2 \dot x^2 t^3$ ($x = \ell - 4/t^2$, $p = 8/t^3$) and for $\int_0^1 \dot x^{2m}$ ($x = t + \ell$, $p = 1$) (HW 51)
- ◻ Def. Hilbert's invariant integral $K[x]$; path independence (asserted); $\Delta J = \int E\dd t$; Def. Weierstrass excess function $E(t, x, \dot x, p)$ (HW 52)
- ◻ Weierstrass conditions for a strong local minimum and for a global minimum (stated without proof) (HW 52–53)
- ◻ Ex. shortest distance between two points is a straight line, via $E \ge 0$ (HW 53)

## Ch 66 Optimal Control (`ch:optimal-control`): new (MATH3404 only)
### §66.1 Examples of control problems
- ◻ Ex. glucose level: $\min\int_0^T u$, $\dot x = -\alpha x + u$ (HW 54)
- ◻ Ex. high-speed train: $m\ddot q = \alpha(t)$, $\abs{\alpha} \le 1$, minimum time to the origin; first-order system form (HW 54–55)
- ◻ Ex. moon landing: $v' = -g + \alpha/m$, $h' = v$, $m' = -k\alpha$; maximise final mass (HW 55)
- Keep one or two (STYLE: one motivating example per section); the glucose and train problems are solved later (HW 60–63)
### §66.2 The general problem and the Pontryagin maximum principle
- ◻ Def. state, control, state equations, cost functional; the general problem (HW 56); two states, piecewise smooth bounded controls (HW 57)
- ◻ Rem. PMP as the analogue of Euler–Lagrange; Rem. fixed $t_1$ needs no $H = 0$ (HW 57)
- ◻ Th. (4.1 in the notes) Pontryagin maximum principle: costate equations, Hamiltonian $H = \psi_0 f_0 + \psi_1 f_1 + \psi_2 f_2$ maximised in $u$, $H = 0$ and $\psi_0 \le 0$ at $t_1$ (stated without proof) (HW 58)
- ◻ Rems: convention $\psi_0 = -1$; cost variable $x_0$ with $\dot x_0 = f_0$; $H = 0$ along an optimal trajectory (stated) (HW 58)
### §66.3 Worked examples
- ◻ Ex. $\dot x_1 = -x_1 + u$, minimise $\frac12\int u^2$: $u = Ae^t$, $x_1 = Be^{-t} + \frac12 Ae^t$, $H = 0$ ⟹ $AB = 0$; cases $(a, b) = (1, 2)$ and $(2, 1)$ (HW 59)
- ◻ Ex. glucose with $0 \le u \le m$: $H$ linear in $u$, switching function $\psi_1 - 1$, no switch; $T$ and $J$ in the cases $a > c$, $a < c$; Rem. minimum-time version gives the same (HW 62–63)
### §66.4 Time-optimal control to the origin (bang-bang)
- ◻ Ex. $\dot x_1 = x_2$, $\dot x_2 = u$: $\psi_2 = B - At$, $u = \frac{K}{m}\operatorname{sgn}\psi_2$, at most one switch; parabolas $x_2^2 = 2u^* x_1 + c$ (HW 60) — **Figure 66.a** (the two families of parabolas) (HW 61)
- ◻ Switching curve $POQ$ and optimal feedback $u^*$ — **Figure 66.b** (switching curve with two optimal paths) (HW 61)
- ◻ Minimum time $t_1 = m(b - 2s)/K$ from the state equations (HW 61)
### §66.5 Time-optimal control of linear systems: real eigenvalues
- ◻ Set-up $\dot{\vect x} = \mat A\vect x + \vect\ell u$, $\abs u \le 1$, $J = t_1 - t_0$; recall of phase-portrait types (stable/unstable node, saddle covered; centre/spiral "not covered" here) (HW 64) ↔ merge (Ch 22, MATH2010: refer to the phase-portrait classification, don't repeat it)
- ◻ Rem. PMP necessary and sufficient for linear time-optimal problems (stated) (HW 64)
- ◻ PMP applied: $H$, costate $\dot{\vect\psi} = -\mat A\T\vect\psi$, $u^* = \operatorname{sgn}(\ell\psi_1 + m\psi_2)$, switching function $S$, equilibria for $u = \pm1$, behaviour (HW 65)
- ◻ Real eigenvalues ⟹ $S = Le^{q_1 t} + Me^{q_2 t}$ has at most one zero (HW 65)
- ◻ Ex. stable node ($\lambda = -1, -5$; equilibria $(\pm3, \pm2)$) — **Figure 66.c** (two node portraits) (HW 66); paths into $O$ — **Figure 66.d** (HW 67); switching curve $P^+OQ^-$ and $u^*$ (HW 67)
- ◻ Ex. unstable node ($\lambda = 1, 5$; equilibria $(-3, 2)$, $(3, -2)$) — **Figure 66.e** (HW 68); paths into $O$ — **Figure 66.f**; finite region of controllability — **Figure 66.g**; $u^*$; larger bound ⟹ larger region (HW 69)
- ◻ Ex. saddle ($\lambda = -2, 4$; equilibria $\pm(1, 2)$) — **Figure 66.h** (two saddle portraits) (HW 70); paths into $O$ and the infinite strip of controllability — **Figure 66.i**; $u^*$ (HW 71)
### §66.6 Time-optimal control of linear systems: complex eigenvalues ("EXT" in the notes)
- ◻ Complex eigenvalues ⟹ $S$ has many zeros; the costate equations must be solved (HW 72)
- ◻ Ex. centre $\dot x_1 = x_2$, $\dot x_2 = -x_1 + u$: $S = k\sin(t + \ell)$, switches $\pi$ apart; $C^\pm$ are circles about $(\pm1, 0)$ (HW 72–73)
- ◻ Switching curve $\Gamma$ of unit semicircles; locus of the previous switch $R$; $u^*$ — **Figures 66.j–l** ($C_1^\pm$ into $O$; construction of $R$; switching curve $\Gamma$) (HW 74)
- ◻ Ex. inward spiral ($\lambda = -k \pm i$): $H$, trajectories, costates, $S = ce^{kt}\sin(t + \gamma)$ (HW 75); arcs $C_1^\pm$, locus of $R$, expansion by $e^{k\pi}$ — **Figures 66.m–n** (HW 76); switching curve and $u^*$ — **Figure 66.o** (HW 77)
- ◻ Ex. outward spiral ($\lambda = k \pm i$): $H$, equilibria $N = (1, 0)$, $M = (-1, 0)$, trajectories — **Figure 66.p** (HW 78); locus of $R$, loops $C_n^+$, shrinking by $e^{k\pi}$ — **Figure 66.q** (HW 79); bounded switching curve, $OP_n \to (1 + e^{-k\pi})/(1 - e^{-k\pi})$, region of control, finitely many switches (HW 80)
### §66.7 Target curves (transversality)
- ◻ Th. (4.3 in the notes) PMP with the end on a curve $g(x_1, x_2) = 0$: $(\psi_1, \psi_2)(t_1)$ perpendicular to the curve (stated without proof) (HW 81) ↔ link (§65.4, transversality in the calculus of variations)
- ◻ Cor. free end state ⟹ $(\psi_1, \psi_2)(t_1) = \vect 0$ (HW 81)
### §66.8 Cost depending on the final state
- ◻ Motivation (drug concentration, pollutant), penalty term $\int u^2$; general problem $J = g(\vect x(t_1)) + \int f_0$ (HW 82)
- ◻ Reduction: cost variable $X_0$, rearranged $H$, pseudo-costates $\lambda_i = \psi_i - \partial g/\partial x_i$, $H'$, end condition $\lambda_i(t_1) = -\partial g/\partial x_i$ (HW 83); summary method (HW 84)
- ◻ Ex. $\dot x = -\alpha x + u$, $J = -x(t_1) + \int_0^{t_1} u^2$ ⟹ $u^* = \frac12 e^{\alpha(t - t_1)}$, $x = \frac{e^{-\alpha t_1}}{2\alpha}\sinh(\alpha t)$ (HW 84–85)

---

## Figures (all to redraw in TikZ; full descriptions in the notes files)
| Fig. | Source | Content |
|---|---|---|
| 65.a | HW 20 | Curve joining two fixed points |
| 65.b | HW 28 | Brachistochrone set-up ($x$ downwards) |
| 65.c | HW 32 | Variable endpoint on a curve $x = c(t)$ with comparison curves |
| 65.d | HW 33 | Special case 1: endpoint on a horizontal line |
| 65.e | HW 33 | Special case 2: endpoint on a vertical line $t = t_1$ |
| 65.f | HW 43 | Non-unique corner minimisers from $(0,0)$ to $(2,1)$ |
| 66.a | HW 61 | Families of parabolas for $u^* = \pm K/m$ |
| 66.b | HW 61 | Switching curve $POQ$ with two optimal paths |
| 66.c–d | HW 66–67 | Stable-node example: portraits for $u^* = \pm1$; paths into $O$ |
| 66.e–g | HW 68–69 | Unstable-node example: portraits; paths into $O$; region of controllability |
| 66.h–i | HW 70–71 | Saddle example: portraits (labels $A$–$D$); paths into $O$ and the strip |
| 66.j–l | HW 74 | Centre example: $C_1^\pm$; construction of $R$; switching curve $\Gamma$ |
| 66.m–o | HW 76–77 | Inward spiral: trajectories; $C_1^\pm$ with $P_1$, $Q$; switching curve |
| 66.p–q | HW 78–79 | Outward spiral: trajectories; switching curve |

Also the two-column comparison table on HW 48 (a table, not a figure). The one-variable and $\R^n$ pages (HW 02–19) have no figures.

## Counts
- **Pages:** 85 (85 photos, one page each; none blank, none duplicated).
- **Labelled blocks in the notes:** 33 Def., 13 Th. (the notes' 1.1–1.4, 2.1–2.2, 3.1–3.2, 4.1 (Euler–Lagrange), corner-curve Th., isoperimetric Th., 4.1 (PMP), 4.3), 4 lemmas (Lem. 2.3 and three "L."), 4 Cor., 19 P. blocks (14 distinct proofs; several run over two pages), 57 Ex. blocks (37 distinct examples, two of them exercises without working), 19 Rem., 25 N.
- **Figures:** 23 (32 individual sketches; several figures are two or three sketches side by side), plus one two-column table (HW 48). All in Ch 65–66; HW 02–19 have none.
- **Inventory items:** 93 bullets above.
- **Code:** none.

## Overlaps with other courses
- **Ch 11** (MATH1071/2400/2401): one-variable extrema, first-derivative and higher-order tests (HW 02–05).
- **Ch 15** (MATH2401/1072/2001/2400): multivariable Taylor series and its proof; gradient/Hessian conditions (HW 06–09).
- **Ch 7** (MATH1071/2001): $h\T H h \ge \lambda_{\min}$ for unit $h$ (HW 08).
- **Ch 62–63** (MATH3204): unconstrained optimality conditions; Lagrange multipliers and the bordered Hessian (HW 06–19). MATH1072 for the two-variable Lagrange rule (HW 10).
- **Ch 22** (MATH2010, see `claude/inventory-math2100.md` §22.b–c): phase-portrait types used in §66.5–66.6 (HW 64).
- **Ch 20** (MATH2010): solution $\vect x = c_1\vect x^{(1)}e^{\lambda_1 t} + c_2\vect x^{(2)}e^{\lambda_2 t}$ recalled (HW 64).
- Chapters 25–31 (written): no overlap.
- MATH3202 (Ch 67–70, same planned chat in `claude/course-chats.md`): no overlap found in these notes.

## Suspected errors in the notes
1. HW 02: local minimum definition has $I \subseteq J$; the $\varepsilon$-neighbourhood $J$ should be inside $I$ (or use $I \cap J$).
2. HW 03: Th. 1.2 writes $f'(x + h)$ for $f'(\bar x + h)$.
3. HW 04: Taylor term $f^{(m-1)}(x)$ should be $f^{(m-1)}(\bar x)$.
4. HW 05: Th. 1.4 (ii) has $\bar x - \varepsilon$; should be $\bar x + \varepsilon$. Continuity at $\bar x$ is needed but not stated.
5. HW 07: Cor. 2.4 needs $h \ne \vect 0$.
6. HW 08: "$Q\T$ is a rotation": orthogonal matrices may be reflections; only length preservation is used (minor). The step $\sum\lambda_i y_i^2 \ge \min\lambda_i$ uses $\sum y_i^2 = 1$, unstated.
7. HW 09: $f(a_1 + \varepsilon h_1, \dots, a_n\varepsilon h_n)$ should have $a_n + \varepsilon h_n$; $\varepsilon \in \R$, not $\R^n$; $h \in \R^n$, not $\Omega$.
8. HW 10–11: Th. 3.1 omits the hypothesis that the $\nabla g_j(a)$ are linearly independent; the proof uses it twice.
9. HW 17: Step 1 shows "$> 0$ sufficient, $\ge 0$ necessary"; the notes say "$> 0$ necessary (and apparently sufficient)". The closing argument states the contradiction as "Thus $\det H(a) = 0$"; it should conclude that no such $h_0$ exists because $\det H(a) \ne 0$. Also $h_0\T g_j$ for $h_0\T\nabla g_j$.
10. HW 18: the final product for $\det H$ is wrong ($\det H = -384$); the conclusion $\det H \ne 0$ stands.
11. HW 24: in the chain-rule line the second derivative is written $\partial f/\partial x$; should be $\partial f/\partial\dot x$. The integrand of $F(\varepsilon)$ drops the $*$ on $x$.
12. HW 25: the dot is missing from $\partial f/\partial\dot x$ in several places; the step "integral $= 0$ ⟹ integrand $= 0$" also needs continuity.
13. HW 26: says the extremal "minimises $J$" before this is shown (it is shown on HW 39). "IVP" is a boundary-value problem.
14. HW 28: $\dd T = \dd s/\sqrt{2g}$ should be $\dd s/\sqrt{2gx}$.
15. HW 29: the last display drops $\ell$; the conditions that fix $\ell$ are not used.
16. HW 31: the bump-function argument gives "$> 0$" only when $m > 0$ near $\alpha$ (should be "$\ne 0$").
17. HW 41: "the integrand is always positive" should be "non-negative".
18. HW 42: $J[y] - J[x^*] = \int -\frac12\dot\eta^2 + \dot\eta^4$; the notes drop the square on the first term.
19. HW 51: $\int_0^1 \dot x^{2m}\dd x$ should be $\dd t$; "$(t, x) \in \R$" should be $\R^2$.
20. HW 55: $\min J = \int_0^T = T$ lacks the integrand, and "subject to" is left blank.
21. HW 56: $\vect f\colon \R^n \times \R \to \R$ should map to $\R^n$; initial time $0$ vs $t_0$.
22. HW 58, HW 81: theorem numbering — the PMP is "4.1" (same as Euler–Lagrange, HW 23) and the target-curve theorem is "4.3"; there is no 4.2.
23. HW 59: case (1) gives $u^* = 0$; should be $u^* = 2e^t$ (the stated $J = 3$ is right).
24. HW 60: the second switch is from $(-)$ to $+$, not "$+$ to $(-)$"; the bound $\abs u \le K/m$ is used without being stated.
25. HW 62: "$m - \alpha = 0$" should be "$m - \alpha a = 0$".
26. HW 65: the costate solution $\vect h(e^{q_1 t} + e^{q_2 t})$ should be $c_1\vect h^{(1)}e^{q_1 t} + c_2\vect h^{(2)}e^{q_2 t}$ (the conclusion for $S$ is right).
27. HW 73: $u^* = -1$ case: $x_2 = -b\cos(t + \beta)$ should be $-b\sin(t + \beta)$.
28. HW 74: final $u^*$: "below $\Gamma$, on $C_1^-$" should be "on $C_1^+$".
29. HW 75: system matrix $(2,1)$ entry should be $-1$ (the Hamiltonian and eigenvalues use $-1$).
30. HW 79: the locus of $R$ for the outward spiral has the wrong exponent signs (should be $x_1 = -1 - 2e^{-k\pi} + e^{-k(\pi - \sigma)}\cos\sigma$, $x_2 = -e^{-k(\pi - \sigma)}\sin\sigma$, consistent with the notes' own $C_2^+$); the sketch draws all arcs above the axis.
31. HW 80: the first sum for $OP_{n+1}$ runs to $\infty$; should run to $n$.
32. HW 83: $H' = -f_0 + \sum\psi_i f_i$ should have $\lambda_i$; "$\lambda_i = -\partial H'/\partial x_i$" should be $\dot\lambda_i$.
33. HW 85: first expression for $x$ has $-e^{\alpha t_1}e^{-\alpha t}$; should be $-\frac{1}{4\alpha}e^{-\alpha t_1}e^{-\alpha t}$ (the final answer is right).

Minor slips (constants renamed between lines, labels as sub- or superscripts, $\Delta T = O(\varepsilon)$ and similar unstated assumptions) are noted in place in the transcription and not repeated here.

## Notation the book doesn't have yet
To go through `NOTATION_REQUESTS.md` in the hub chat.

| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\Hess` (operator) | $H_f(a)$ or $\nabla^2 f(a)$ | Hessian of $f$ | The notes write $H_f$ and $H_L$; Ch 15, 62, 63 will all need one form (MATH3204 likely uses $\nabla^2 f$). |
| `\grad` (optional) | $\nabla f$ | gradient | The notes underline $\nabla$ as a vector operator; one plain form for the book. Could stay raw `\nabla`. |
| `\sgn` (`\DeclareMathOperator`) | $\operatorname{sgn}$ | sign function | Bang-bang controls $u^* = \operatorname{sgn}[\ldots]$ throughout §66.4–66.6. |
| `\Ham` (or plain $H$) | $H$ | Hamiltonian of optimal control | Clashes with the bordered Hessian $H$ (HW 14) and the Hessian $H_f$; fix one letter each. |
| convention, no macro | $\vect\psi$ / $\vect\lambda$ | costate / pseudo-costate vectors | Decide bold; $\lambda$ is also eigenvalues and Lagrange multipliers in the same chapters. |
| convention, no macro | $J[x]$ | functional with square brackets | The notes mix $J[x]$ and $J(x)$; choose one. |
| convention, no macro | $f_x$, $f_{\dot x}$ vs $\partial f/\partial\dot x$ | partial derivatives of the integrand | Both forms appear (HW 30–31 vs HW 23–25). |
| `\Re` / `\Im` (existing LaTeX) | $\operatorname{Re}$, $\operatorname{Im}$ | real/imaginary part | Already used by MATH2100 (HW 64 here); check the book's choice. |

## Code in the notes
None. (Part V uses Python; the hub may later add Python to reproduce the phase-portrait and switching-curve figures, but nothing in the source calls for it.)

## Questions for the hub chat
1. Where does HW 02–19 (optimisation in $\R$ and $\R^n$, Lagrange multipliers, bordered Hessian) go: merged into Ch 11/15/62/63 when MATH3204 arrives, or a short opening section of Ch 65?
2. Which semester was MATH3404 taken (for source identification)?
3. Two proofs of the Euler–Lagrange equation (HW 24–25 and HW 30–31): keep both or one?
4. The time-optimal material (HW 60–80) is long and figure-heavy (about 20 figures). Keep all four linear examples (stable, unstable, saddle) and the three "EXT" complex examples, or trim to one per type?
