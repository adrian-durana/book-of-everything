# MATH3404 Optimisation Theory: transcription, part 3 of 3 (HW 54–85)

_Optimal control. Sources, legibility check and conventions: see `claude/notes-math3404-1.md`. No dates are recorded. "EXT" in some page headers is the notes' own label (extension material)._

---

## HW 54 — Introduction: optimal control
_File `20261122_010347.jpg`. Header "Introduction: optimal control"._

**N.** We begin by considering the following problems:

**Ex.** *Level of glucose in bloodstream*
The level of glucose in the bloodstream $x(t)$ is metabolised at a rate $\alpha x(t)$.
We wish to control the level of glucose from $x = a$ at time $0$ to $x = c$ at time $T$ by infusing at a rate $u(t)$.
We also wish to minimise the total amount given.
Therefore, we
$$\min J = \int_0^T u(t) \dd t$$
subject to the differential equation constraint
$$\dot x = -\alpha x + u(t)$$

**Ex.** *High speed train*
Imagine a train powered by two engines (one per side).
Denote
$q(t)$: position at time $t$
$v(t)$: velocity at time $t$
$\alpha(t)$: thrust/force from engine at time $t$, $-1 \le \alpha(t) \le 1$.
We wish to control the thrust of the engine so that we arrive at the origin $O$ with zero velocity at a minimum time.

From Newton's second law, $m\ddot q(t) = \alpha(t)$
We also know $\dot q(t) = v(t)$. We can express these ODEs as a system of first-order ODEs:
$$\vect x(t) = \begin{pmatrix} q(t) \\ \dot q(t) \end{pmatrix} \Rightarrow \vect x'(t) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} q(t) \\ \dot q(t) \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \end{pmatrix}\frac{\alpha(t)}{m}$$
$$\vect x(0) = \begin{pmatrix} q_0 \\ \dot q_0 \end{pmatrix}, \qquad \vect x(T) = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
[$\vect x$ is underlined in the notes. The same Greek-looking letter $\alpha$ is used for the glucose rate constant and the train's thrust; in the train example it may be a cursive "a".]

## HW 55 — Introduction: optimal control (cont.); landing on the moon
_File `20261122_010351.jpg`. Header "Introduction: optimal control"._

**Ex.** (continued) Therefore, we
$$\min J = \int_0^T = T$$
subject to
[the integrand ($1 \dd t$) is missing, and nothing is written after "subject to" (the state equations of HW 54 are meant)]

**Ex.** *Landing on the moon*
Suppose we are landing a spacecraft on the lunar surface.
Denote
$h(t)$: height at time $t$
$v(t)$: velocity at time $t$
$\alpha(t)$: thrust/force at time $t$, $0 \le \alpha(t) \le 1$
We wish to control thrust so that we land at the origin $O$ (with zero velocity) with minimal fuel usage (i.e. max mass).

From Newton's second law, $m\ddot h(t) = -gm + \alpha(t)$.
We therefore have the following ODEs:
$$\begin{cases} v'(t) = -g + \frac1m\alpha(t) \\ h'(t) = v(t) \\ m'(t) = -k\alpha(t) \end{cases}$$
[an arrow points at the last equation from the note:] thrust inversely proportional to mass change
To maximise mass, we therefore
$$\max J = \int_{t_0}^T -K\alpha(t) \dd t + m(t_0)$$
[the constant is written $k$ in the ODE and $K$ in $J$. "inversely proportional" is the notes' wording; the equation says the mass decreases at a rate proportional to the thrust.]

## HW 56 — General optimal control: the problem
_File `20261122_010356.jpg`. Header "General optimal control". Bottom fifth blank._

**Def.** We define the optimal control problem as follows:

First define the following functions:

| | |
|---|---|
| $\vect x(t)\colon \R \to \R^n$ | state function (unknown) |
| → $\vect x(0) = \vect x_0$ | initial state (known) |
| → $\vect x(t_1) = \vect x_1$ | target state (known) [with "$t_1$ unknown" written above "known"] |
| $u(t)\colon \R \to \R$, $u \in \mathcal U$ | control function (unknown) |
| $\vect f(\vect x, u)\colon \R^n \times \R \to \R$ $\ (\dot{\vect x} = \vect f(\vect x, u))$ | state equations (diff. eq. constraint) |
| $J = \displaystyle\int_{t_0}^{t_1} f_0(\vect x, u) \dd t$ | cost functional |

[$\vect x$, $\vect f$ underlined in the notes; the $\vect f$ has a small blacked-out subscript (probably an "$i$"). The codomain of $\vect f$ should be $\R^n$ (or the componentwise $f_i$ map to $\R$). The initial time is $0$ in the second line and $t_0$ in $J$.]

We now define the general problem.
We are given the state equations, the initial state, the target state (unspecified time), the cost functional and the set of admissible control functions $u(t) \in \mathcal U$.
We wish to find the control $u^*$ and corresponding path $\vect x^*$ (which transfers the system from $\vect x_0$ to $\vect x_1$) such that the cost function $J$ is minimised, subject to the constraint state DEs.

## HW 57 — General optimal control: two states
_File `20261122_010400.jpg`. Header "General optimal control". Lower quarter blank._

**Def.** In this course we will only work with $n = 1$ or $2$ states.
If we consider 2 states, we have constraints
$$\dot x_1 = f_1(x_1, x_2, u), \qquad \dot x_2 = f_2(x_1, x_2, u)$$
and we wish to go from $(x_1^0, x_2^0)$ at $t = t_0$ to $(x_1^1, x_2^1)$ at $t = t_1$ using <u>piecewise smooth</u> and <u>bounded</u> admissible control functions $u(t)$ such that
$$J = \int_{t_0}^{t_1} f_0(x_1, x_2, u) \dd t \quad \text{is minimised.}$$

**Rem.** We now wish to find necessary (and later, sufficient) conditions for minimising $J$. A necessary condition for optimal control (analogous to the Euler–Lagrange) is the PMP (Pontryagin maximum principle).

**Rem.** If the final time $t_1$ is fixed and known, the endpoint conditions are sufficient to solve the problem.
(We do not need to set, for example, $H = 0$ using PMP)

## HW 58 — Pontryagin maximum principle
_File `20261122_010407.jpg`. Header "Pontryagin maximum principle". Bottom eighth blank._

**Th. (4.1)** Let $u^*(t)$ be an admissible control with corresponding path $\vect x^*(t)$ that takes the system from $(t_0, \vect x_0)$ to $(t_1, \vect x_1)$ at some unspecified time $t_1$.
Then for $u^*$ and $\vect x^*$ to be optimal, it is necessary that:
(1) $\exists$ a non-zero vector $\vect\psi = (\psi_0, \psi_1, \psi_2)$ such that
$$\dot\psi_i = -\partial H/\partial x_i$$
These are the costate equations.
(2) $\exists$ a scalar function
$$H(\vect\psi, \vect x, u) = \psi_0 f_0 + \psi_1 f_1 + \psi_2 f_2$$
such that
(i) $\forall t \in [t_0, t_1]$, $H$ attains its maximum (w.r.t. $u$) at $u = u^*(t)$
(ii) $H(\vect\psi^*, \vect x^*, u^*) = 0$ and $\psi_0 \le 0$ at $t = t_1$
[Not proved in the notes. The number (4.1) repeats the Euler–Lagrange theorem's number (HW 23). $\vect\psi$, $\vect x$ underlined in the notes; $\psi_0$ is written with a slightly different glyph ($\varphi_0$) in places.]

**Rem.** Conventionally, we set $\psi_0 = -1$. Therefore the Hamiltonian $H$ is
$$H(\vect\psi, \vect x, u) = -f_0 + \psi_1 f_1 + \psi_2 f_2$$

**Rem.** We define $x_0$ to be the solution of
$$\dot x_0 = f_0(x_1, x_2, u), \qquad x_0(t_0) = 0$$
That is, $x_0(t)$ measures the 'cost' incurred up to $t$.

**Rem.** We can actually show $H = 0$ at each $t$ on an optimal trajectory.
[not shown in the notes]

## HW 59 — Optimal control example (minimum energy, one state)
_File `20261122_010411.jpg`. Header "Optimal control example"._

**Ex.** Let $\dot x_1 = -x_1 + u$. Control the system from $x_1 = a$ ($t = 0$) to $x_1 = b$ ($t = t_1$) such that $\frac12\int_0^{t_1} u^2 \dd t$ is minimised.

Note that $f_0(x_1, x_2, u) = \frac12 u^2$, $f_1(x_1, x_2, u) = -x_1 + u$.
Thus,
$$H = -\tfrac12 u^2 + \psi_1(-x_1 + u)$$
$$\dot\psi_1 = -\partial H/\partial x_1 = \psi_1 \Rightarrow \psi_1 = Ae^t$$
Now maximise $H$ w.r.t. $u$:
$$\frac{\partial H}{\partial u} = -u + \psi_1 \quad \text{and} \quad \frac{\partial^2 H}{\partial u^2} = -1 \Rightarrow H \text{ maximised by } u = \psi_1 = Ae^t$$
The corresponding solution for $x$ is:
$$\dot x_1 = f_1(x_1, x_2, u) = -x_1 + Ae^t \Rightarrow x_1(t) = Be^{-t} + \tfrac12 Ae^t$$
Apply end conditions:
$$x_1(0) = a = B + \tfrac12 A \quad \text{and} \quad x_1(t_1) = b = Be^{-t_1} + \tfrac12 Ae^{t_1}$$
$$\Rightarrow B = \frac{ae^{t_1} - b}{e^{t_1} - e^{-t_1}}, \qquad \frac{A}{2} = \frac{b - ae^{-t_1}}{e^{t_1} - e^{-t_1}}$$
Now find time $t_1$ (use the condition that $H = 0$ for any $t$ on an optimal path). Substituting $u$, $\psi_1$, $x_1$ into $H = 0$, we obtain $AB = 0$. Note $t$ should cancel.
[Checked.]

**Rem.** Further examine cases where (1) $a = 1$, $b = 2$; (2) $a = 2$, $b = 1$.
(1) $A = 0$: $e^{-t_1} = 2$ ↯ so $B = 0$, $t_1 = \ln 2$, $u^* = 0$, $x_1^* = e^t$, $J = 3$
(2) $B = 0$: $e^{t_1} = 1/2$ ↯ so $A = 0$, $t_1 = \ln 2$, $u^* = 0$, $x_1^* = 2e^{-t}$, $J = 0$
[possible error: in case (1), $B = 0$ gives $A = 2$ and $u^* = \psi_1 = 2e^t$, not $u^* = 0$ ($u^* = 0$ would give $J = 0$). The rest of case (1) ($t_1 = \ln 2$, $x_1^* = e^t$, $J = 3$) and all of case (2) are right. ↯ marks a contradiction.]

Thus we have shown it 'costs less' for the system to go from $x_0 = 2$ to $x_1 = 1$, compared to $x_0 = 1$, $x_1 = 2$. ["$x_0 = 2$" is written above a blacked-out box]
In fact, if no control is imposed on the system, the behaviour is $\dot x_1 = -x_1$, and thus tends to the origin. Thus it will not move from e.g. $x_0 = 1$ to $x_1 = 2$ unless forced by a large enough control.
[Here "$x_0$", "$x_1$" mean the start and end values $a$, $b$, clashing with the state $x_1$ and the cost variable $x_0$.]

## HW 60 — Optimal control example (time-optimal control to the origin)
_File `20261122_010418.jpg`. Header "Optimal control example"._

**Ex.** Consider the system $\{\dot x_1 = x_2,\ \dot x_2 = u\}$ and controlling it from an initial point $(a, b)$ at $t = 0$ to the origin in as short a time as possible.

**Rem.** This is a simple example of a class of problems known as 'the problem of time control to the origin'.

**Ex.** (continued) The cost is $t_1$, and so we minimise
$$J = \int_0^{t_1} f_0(x_1, x_2, u) \dd t = \int_0^{t_1} \dd t = t_1$$
Thus $f_0(x_1, x_2, u) = 1$, $f_1(x_1, x_2, u) = x_2$, $f_2(x_1, x_2, u) = u$ and we have $H = -1 + \psi_1 x_2 + \psi_2 u$ with
$$\dot\psi_1 = \frac{-\partial H}{\partial x_1} = 0, \quad \dot\psi_2 = \frac{-\partial H}{\partial x_2} = -\psi_1 \Rightarrow \psi_1 = A,\ \psi_2 = B - At$$
We now need to maximise $H$ w.r.t. $u$. We must bound $u$ to find some sort of an 'optimal solution'.
The max. value of $H$ if $\psi_2 > 0$ is $u = K/m$. If $\psi_2 < 0$, the max. value of $H$ is $u = -K/m$. Thus the value of $u$ is
$$u(t) = \tfrac{K}{m}\operatorname{sgn}[\psi_2(t)]$$
– the control <u>switches</u> from $K/m$ to $-K/m$ when $\psi_2$ goes from $+$ to $(-)$, and also <u>switches</u> from $-K/m$ to $K/m$ when $\psi_2$ goes from $+$ to $(-)$.
[possible error: the second switch is when $\psi_2$ goes from $(-)$ to $+$. The bound $\abs u \le K/m$ is used but not stated; $K$ and $m$ (from the train example, HW 54) are not defined here. "The max. value of $H$ … is $u = \dots$" means "is attained at".]
However, as $\psi_2 = B - At$ can only switch sign once, there is only ever one switch. By the PMP, the time-optimal control is amongst this class of controls.

The solution for $x_1, x_2$ is as follows. Let $u^*(t) = \frac{K}{m}\operatorname{sgn}[\psi_2(t)]$. Note $u^*$ is constant except at switches. Then we have
$$\dot x_1 = x_2, \quad \dot x_2 = u^*, \quad u^* = \pm K/m$$
$$\Rightarrow \frac{\dd x_2}{\dd x_1} = \frac{u^*}{x_2} \Rightarrow x_2^2 = 2u^* x_1 + \text{constant}$$

## HW 61 — Optimal control example (time-optimal, cont.): parabolas, switching curve, minimum time
_File `20261122_010423.jpg`. Header "Optimal control example"._

**Ex.** To each of the allowed values of $u^*$ there corresponds a family of parabolas:

*Figure (two phase-plane families, side by side; axes unlabelled, horizontal $x_1$, vertical $x_2$).*
- Left, labelled $u^* = -K/m$: three nested parabolas opening to the **left** (vertex on the horizontal axis, arms going up-left and down-left), the outermost with its vertex just right of the vertical axis, the others with vertices further left. Each carries an arrowhead on its lower arm pointing down-left (motion downwards, $x_2$ decreasing).
- Right, labelled $u^* = K/m$: three nested parabolas opening to the **right** (vertex on the horizontal axis, arms going up-right and down-right), the outermost with its vertex just left of the vertical axis. Each carries an arrowhead on its upper arm pointing up-right (motion upwards, $x_2$ increasing).

Thus we construct the minimum time path by following the trajectory until it cuts one of the parabolic arcs that head towards $O$ – these are the only routes to $O$.

*Figure (switching curve $POQ$ and two optimal paths).* Axes $x_1$ (horizontal, arrow right) and $x_2$ (vertical, arrow up), origin $O$ marked with a dot.
- The switching curve: arc $PO$ comes from $P$ at the far upper left and descends to $O$ (upper-left half of a left-opening parabola through $O$), with an arrow pointing into $O$; arc $OQ$ leaves $O$ and runs down to $Q$ at the lower right (lower-right half of a right-opening parabola through $O$), with an arrow on it pointing back up towards $O$.
- Path 1 (from above the switching curve): starts at the upper left above $P$, runs right across the $x_2$-axis through the point $R$ (just right of the $x_2$-axis, with a dotted horizontal line from $R$ out to the right), bends down (arrow down) and crosses the $x_1$-axis on the right, then meets $OQ$ and follows it up into $O$.
- Path 2 (from below): starts at the lower right below $Q$, runs left through the point $S$ (just left of the $x_2$-axis, with a dotted horizontal line from $S$ out to the left), bends up (arrow up) across the $x_1$-axis on the left, then meets $PO$ and follows it down into $O$.
[the labels $R$ and $S$ are not used in the text; $s$ in the text below is the value of $x_2$ at the switch]

The optimal control is
$$u^* = \begin{cases} -K/m & \text{above } POQ, \text{ on } OP \\ K/m & \text{below } POQ, \text{ on } OQ \end{cases}$$
$POQ$ is the switching curve.

The minimum time $t_1$ could be determined by $H = 0$. As we have three unknowns $(A, B, t_1)$ we would have to apply it at three times ($t = 0$, the switch $t = \eta$, $t = t_1$). This is tedious.
We can instead find $t_1$ directly using the state equations.
Consider WLOG that $(a, b)$ is above the switching curve.
$$\begin{aligned} \dot x_2 = -K/m &\Rightarrow x_2 = -\tfrac{K}{m}t + b && 0 \le t \le \eta \\ x_2 = s &\Rightarrow \eta = m(b - s)/K && t = \eta \\ \dot x_2 = K/m &\Rightarrow x_2 = \tfrac{K}{m}t + \text{const.} && t > \eta \\ &\Rightarrow \phantom{x_2} = \tfrac{K}{m}t - b + 2s \end{aligned}$$
At $t = t_1$, $x_2 = 0$, so $t_1 = m(b - 2s)/K$.
We determine $s$ by finding the intersection of the path through $(a, b)$, and $OQ$.
[Checked.]

## HW 62 — Optimal control example (glucose problem, bounded control)
_File `20261122_010430.jpg`. Header "Optimal control example"._

**Ex.** Consider the glucose problem posed earlier. In particular, we have $\dot x_1 = -\alpha x_1 + u$, and where $0 \le u(t) \le m$.
The level is to be controlled from $x_1 = a$ ($t = 0$) to $x_1 = c$ ($t = T$) such that we minimise $J = \int_0^T u \dd t$.

Note that $a, c \ge 0$ and $m \ge \alpha c$, for the system to be controllable. Then
$$H = -u + \psi_1(-\alpha x_1 + u) = -\alpha x_1\psi_1 + u(\psi_1 - 1).$$
As $H$ is linear in $u$, and $0 \le u \le m$, the max. of $H$ w.r.t. $u$ is
$$u = \bar u = \begin{cases} 0 & \psi_1 < 1 \\ m & \psi_1 > 1 \end{cases} \qquad \text{Note } \dot\psi_1 = -\frac{\partial H}{\partial x_1} = \alpha\psi_1 \Rightarrow \psi_1 = Ae^{\alpha t}$$
As $\alpha > 0$, it follows that $e^{\alpha t} > 0$, so the switching function $\psi_1 - 1 = Ae^{\alpha t} - 1$ can only have a zero (in $t > 0$) if $0 < A < 1$.
For $A \ge 1$, it is $> 0$ $\forall t > 0$, giving $\bar u = m$.
For $A \le 0$, it is $< 0$ $\forall t > 0$, giving $\bar u = 0$.
In all three cases, the control that maximises $H$ is piecewise constant, so at $t = 0$ we have either $\bar u = 0$ or $\bar u = m$.
We can now rule out the possibility there is a switch:
→ If $u(0) = 0$, $H_{t=0} = -\alpha aA = 0 \Rightarrow A = 0 \Rightarrow \psi_1 - 1 = -1$ $\forall t > 0$ ✓
→ If $u(0) = m$, $H_{t=0} = -m + A(m - \alpha a) = 0 \Rightarrow A = m/(m - \alpha a)$ [the "0" in $u(0)$ is written over a blacked-out character]
&nbsp;&nbsp;&nbsp;&nbsp;Note that $m - \alpha a = 0$ leads to $m = 0$ ↯.
&nbsp;&nbsp;&nbsp;&nbsp;Thus either $m < a\alpha \Rightarrow A < 0$ or $m > a\alpha \Rightarrow A > 1$. ✓
[the first line of the note reads "$m - \alpha = 0$"; $m - \alpha a$ is meant. The case $u(0) = 0$ also needs $a \ne 0$. The ✓ ticks are in the notes.]
Hence $\bar u = 0$ or $\bar u = m$ $\forall t$. The state equation
$$\dot x_1 = -\alpha x_1 + \bar u \Rightarrow x_1 = Be^{-\alpha t} + \bar u/\alpha$$
Applying end conditions, we obtain
$$a = B + \bar u/\alpha, \qquad c = Be^{-\alpha T} + \bar u/\alpha$$
[Checked. In "$m < a\alpha \Rightarrow A < 0$" the case $A < 0$ contradicts $\bar u(0) = m$ ($\psi_1 < 1$); the notes leave this implicit.]

## HW 63 — Optimal control example (glucose problem, cont.)
_File `20261122_010433.jpg`. Header "Optimal control example". Lower 40% blank._

**Ex.** (continued) There are two cases:
(1) $a > c$: Here we must decrease glucose.
The control $\bar u = m$ gives $T < 0$, and thus cannot transfer the level to $x_1 = c$. [a blacked-out character after "$T$"]
The control $\bar u = 0$ gives $T = \frac1\alpha\ln(a/c) > 0$.
(2) $a < c$: Here we must increase glucose.
The control $\bar u = 0$ gives $T < 0$.
The control $\bar u = m$ gives a finite positive value to $T$, as $m \ge \alpha c \ge \alpha a$. This gives
$$T = \frac1\alpha\ln\Bigl(\frac{m - \alpha a}{m - \alpha c}\Bigr) \Rightarrow J = \frac{m}{\alpha}\ln\Bigl(\frac{m - \alpha a}{m - \alpha c}\Bigr).$$
The optimal strategy is therefore to (obviously) put in $u = 0$ if $a > c$ and put in $u = m$ if $a < c$.
[Checked. A finite $T$ needs $m > \alpha c$ strictly.]

**Rem.** The minimum time problem for this system results in the same solution. ["time" is written above a blacked-out word]

## HW 64 — Time-optimal control of linear systems: set-up
_File `20261122_010440.jpg`. Header "Time-optimal control of linear systems"._

**Def.** For time-optimal control of linear systems, we constrain a single control $\abs{u(t)} \le 1$ where $u$ is piecewise continuous.
The system is governed by a pair of linear DEs
$$\dot x_1 = ax_1 + bx_2 + \ell u, \quad \dot x_2 = cx_1 + dx_2 + mu \quad \Rightarrow \quad \dot{\vect x} = \mat A\vect x + \vect\ell u$$
We control the system from $\vect x_0 = \vect x(t_0)$ to $\vect x_1 = \vect x(t_1)$ by an admissible control $u$ while minimising
$$J = \int_{t_0}^{t_1} 1 \dd t = t_1 - t_0$$
The solutions to this problem involve phase-plane analysis (as in MATH2010/MATH2100)
[$\vect x$ and $\vect\ell = (\ell, m)\T$ are underlined in the notes; $\mat A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is implied. Here $m$ is a coefficient, not the mass of the earlier examples.]

**Rem.** Recall that given a system $\dot{\vect x} = \mat A\vect x$, the solution is given by $\vect x = c_1\vect x^{(1)}e^{\lambda_1 t} + c_2\vect x^{(2)}e^{\lambda_2 t}$, where $\lambda_1, \lambda_2$ are the eigenvalues of $\mat A$ and $\vect x^{(1)}$, $\vect x^{(2)}$ are the corresponding eigenvectors.
Then,
(1) Real, non-zero eigenvalues
&nbsp;&nbsp;&nbsp;(i) $\lambda_i < 0$: stable node
&nbsp;&nbsp;&nbsp;(ii) $\lambda_i > 0$: unstable node
&nbsp;&nbsp;&nbsp;(iii) $\lambda_{(1)} > 0$, $\lambda_{(2)} < 0$: saddle [a blacked-out box before "(iii)"]
&nbsp;&nbsp;&nbsp;$\Bigr\}$ we will cover
(2) Imaginary eigenvalues
&nbsp;&nbsp;&nbsp;(i) $\operatorname{Re}(\lambda_i) = 0$: centre
&nbsp;&nbsp;&nbsp;(ii) $\operatorname{Re}(\lambda_i) \ne 0$: spiral
&nbsp;&nbsp;&nbsp;$\Bigr\}$ we will NOT cover
["Imaginary" means complex (non-real) here.]

**Rem.** We can show that PMP is both necessary and sufficient for linear time-optimal control problems.
[not shown in the notes]

## HW 65 — Time-optimal control of linear systems: applying the PMP; real eigenvalues
_File `20261122_010445.jpg`. Header "Time-optimal control of linear systems"._

**Def.** We apply PMP to this problem:
(1) <u>Find $H$:</u>
$$\begin{aligned} H &= \sum \psi_i f_i \\ &= -1 + \psi_1(ax_1 + bx_2 + \ell u) + \psi_2(cx_1 + dx_2 + mu) \\ &= -1 + \psi_1(ax_1 + bx_2) + \psi_2(cx_1 + dx_2) + u(\ell\psi_1 + m\psi_2) \end{aligned}$$
<u>Costate equations:</u>
$$\dot\psi_1 = -\partial H/\partial x_1 = -a\psi_1 - c\psi_2, \quad \dot\psi_2 = -\partial H/\partial x_2 = -b\psi_1 - d\psi_2 \quad \Rightarrow \quad \dot{\vect\psi} = -\mat A\T\vect\psi$$
(2) <u>Maximise $H$:</u>
$H$ is linear in $u$, so $u^* = \pm1$ (depending on the sign of $\ell\psi_1 + m\psi_2$): $u^* = \operatorname{sgn}[\ell\psi_1 + m\psi_2]$.
$u^*$ is piecewise cts. and switches at the zeros of $\ell\psi_1 + m\psi_2$. Thus,
<u>Switching fn:</u> $S = \ell\psi_1 + m\psi_2$.
Between two zeros of $S$, $u^*$ is constant:
$$\dot{\vect x} = \mat A\vect x + u^*\vect\ell \quad \text{where } u^* = \pm1.$$
If $\det\mat A \ne 0$, the trajectories have a singularity at the solution of
$$\begin{aligned} ax_1 + bx_2 + \ell = 0 &\quad \text{and} \quad cx_1 + dx_2 + m = 0 && (u = 1) \\ ax_1 + bx_2 - \ell = 0 &\quad \text{and} \quad cx_1 + dx_2 - m = 0 && (u = -1) \end{aligned}$$
(3) <u>Behaviour:</u>
Behaviour is governed by the matrix $\mat A$, translated to the equilibrium point.

**Def.** *System with real eigenvalues*
Note that if $\mat A$ has real $\lambda_i$, $-\mat A\T$ also has real $\lambda_i$.
The solution of the costate equations is
$$\vect\psi = \vect h(e^{q_1 t} + e^{q_2 t}) \quad \text{where $q_i$ are e.values, $\vect h$ is e.vector}$$
Thus the switching function is
$$S = \ell\psi_1 + m\psi_2 = Le^{q_1 t} + Me^{q_2 t} \qquad \leftarrow \text{has at most one zero}$$
[possible error: the general costate solution is $\vect\psi = c_1\vect h^{(1)}e^{q_1 t} + c_2\vect h^{(2)}e^{q_2 t}$, with an eigenvector (and a constant) for each eigenvalue $q_i$ of $-\mat A\T$; one vector $\vect h$ times $(e^{q_1 t} + e^{q_2 t})$ is not the general solution. The conclusion $S = Le^{q_1 t} + Me^{q_2 t}$ is right. The multiplier of $\psi_1$ in the last line of $H$ is written like "$1\psi_1$"; it is $\ell\psi_1$.]

## HW 66 — Time-optimal control of linear systems (example: stable node)
_File `20261122_010452.jpg`. Header "Time-optimal control of linear systems (ex. stable)"._

**Ex.** Solve the problem of time-optimal control to the origin for the system $\dot x_1 = -3x_1 + 2x_2 + 5u$, $\dot x_2 = 2x_1 - 3x_2$, $\abs u \le 1$.

We have $f_0 = 1$, $f_1 = -3x_1 + 2x_2 + 5u$, $f_2 = 2x_1 - 3x_2$.
Then
$$\begin{aligned} H &= -1 + \psi_1(-3x_1 + 2x_2 + 5u) + \psi_2(2x_1 - 3x_2) \\ &= -1 + \psi_1(-3x_1 + 2x_2) + \psi_2(2x_1 - 3x_2) + u(5\psi_1) \end{aligned}$$
The costate equations are
$$\dot\psi_1 = -\partial H/\partial x_1 = 3\psi_1 - 2\psi_2, \quad \dot\psi_2 = -\partial H/\partial x_2 = -2\psi_1 + 3\psi_2 \quad \Rightarrow \quad \dot{\vect\psi} = \begin{pmatrix} 3 & -2 \\ -2 & 3 \end{pmatrix}\vec\psi$$
$H$ is maximised w.r.t. $u$ when $u^* = \operatorname{sgn}[5\psi_1] = \pm1$
Thus the corresponding solutions of the state equations are the trajectories of the linear system
$$\dot{\vect x} = \begin{pmatrix} -3 & 2 \\ 2 & -3 \end{pmatrix}\vect x + \begin{pmatrix} 5 \\ 0 \end{pmatrix}u^* \qquad u^* = \pm1$$
The eigenvalues of $\mat A$ are $\lambda_1 = -1$, $\lambda_2 = -5$. These are real, so there is at most one switch. These are also both negative, so we have a stable node at eq. point.
The eq. points are given by:
$$u^* = 1: \ \begin{cases} -3x_1 + 2x_2 + 5 = 0 \\ 2x_1 - 3x_2 = 0 \end{cases} \Rightarrow x_1 = 3,\ x_2 = 2 \qquad u^* = -1: \ \begin{cases} -3x_1 + 2x_2 - 5 = 0 \\ 2x_1 - 3x_2 = 0 \end{cases} \Rightarrow x_1 = -3,\ x_2 = -2$$
The eigenvectors are given by $\vect x^{(1)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $\vect x^{(2)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
[Checked.]

Let $C^+$ be a typical path for $u^* = 1$, and $C^-$ for $u^* = -1$.

*Figure (two phase portraits side by side, axes unlabelled; horizontal $x_1$, vertical $x_2$).*
- Left, labelled $u^* = 1$: the equilibrium $(3, 2)$ is a dot in the first quadrant. Two solid lines through it: one of slope $1$ (eigenvector $(1, 1)$) running from the upper right down through the dot and on past the origin region into the third quadrant, with arrowheads pointing towards the dot from both ends; one of slope $-1$ (eigenvector $(1, -1)$) from the upper left to the lower right through the dot, again with arrowheads pointing in. Many short dashed curves converge on the dot from all directions (stable node).
- Right, labelled $u^* = -1$: the same picture centred on the equilibrium $(-3, -2)$, a dot in the third quadrant: solid lines of slopes $1$ and $-1$ through it with inward arrowheads, and dashed curves converging on it.

## HW 67 — Time-optimal control of linear systems (stable example, cont.): switching curve
_File `20261122_010457.jpg`. Header "Time-optimal control of linear systems (ex. stable)"._

**Ex.** (continued) To reach the origin at minimum time, the phase point $(x_1, x_2)$ must either travel along a $C^+$ or $C^-$ path, and can only switch at most once.
There is only two paths that go to the origin.
The slope of the curves at $O$ is $\dd x_2/\dd x_1 = 0/5u^* = 0$.

*Figure (the two paths into $O$; two small phase-plane sketches, axes unlabelled).*
- Left, labelled $u^* = 1$: the equilibrium $P = (3, 2)$ in the first quadrant at the crossing of two dashed lines (slopes $1$ and $-1$, the eigendirections). A solid curve comes from $P_+$ at the upper left (second quadrant), with an arrow pointing down-right, and reaches $O$ tangent to the $x_1$-axis; it continues as a short curve heading up-right towards $P$ (the $C^+$ path through $O$ ends at the stable node $P$).
- Right, labelled $u^* = -1$: the equilibrium $Q = (-3, -2)$ in the third quadrant at the crossing of two dashed lines (slopes $1$ and $-1$). A solid curve comes from $Q_-$ at the lower right (fourth quadrant), with an arrow pointing up-left, and reaches $O$ tangent to the $x_1$-axis, continuing towards $Q$.

If the initial state of the system lies at $P_+O$ or $Q_-O$, then the optimal control sequence is simply $\{1\}$ or $\{-1\}$ respectively.
If the initial state is above $P_+OQ_-$, we cannot go on a $+$ path (this goes to $P$), so we go on a $-$ path until $P_+O$ is reached, then switch, i.e.
$$u^* = \begin{cases} -1 & \text{until reaches } P_+O \\ 1 & \text{afterwards} \end{cases}$$
If the initial state is below $P_+OQ_-$, we cannot go on a $-$ path (this goes to $Q$), so we go on a $+$ path until $Q_-O$ is reached, then switch, i.e.
$$u^* = \begin{cases} 1 & \text{until reaches } Q_-O \\ -1 & \text{afterwards} \end{cases}$$
Thus the optimal control is
$$u^* = \begin{cases} 1 & \text{below } P^+OQ^-, \text{ on } P^+O \\ -1 & \text{above } P^+OQ^-, \text{ on } Q^-O \end{cases}$$
[The labels are written $P_+$, $Q_-$ (subscripts) in the text and $P^+$, $Q^-$ (superscripts) in the last display. "$0/5u^*$": at $O$, $\dot x_2 = 0$ and $\dot x_1 = 5u^*$.]

## HW 68 — Time-optimal control of linear systems (example: unstable node)
_File `20261122_010503.jpg`. Header "Time-optimal control of linear systems (ex. unstable)"._

**Ex.** Solve the problem of time-optimal control to the origin for the system $\dot x_1 = 3x_1 + 2x_2 + 5u$, $\dot x_2 = 2x_1 + 3x_2$, $\abs u \le 1$.

We have the system
$$\dot{\vect x} = \begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix}\vect x + u\begin{pmatrix} 5 \\ 0 \end{pmatrix}$$
The Hamiltonian $H$ is
$$H = -1 + \psi_1(3x_1 + 2x_2) + \psi_2(2x_1 + 3x_2) + u(5\psi_1)$$
and the costate equations are
$$\dot{\vect\psi} = -\mat A\T\vect\psi = \begin{pmatrix} -3 & -2 \\ -2 & -3 \end{pmatrix}\vect\psi$$
$H$ is maximised w.r.t. $u$ by $u^* = \operatorname{sgn}[5\psi_1] = \pm1$.

Therefore, the optimal trajectories satisfy
$$\dot{\vect x} = \begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix}\vect x + u^*\begin{pmatrix} 5 \\ 0 \end{pmatrix} \qquad u = \pm1$$
The eigenvalues of $\mat A$ are $\lambda_1 = 1$, $\lambda_2 = 5$. These are both real, so there is at most one switch. ["is" written above a blacked-out word] They are also both positive, so we have an unstable node.
The eigenvectors of $\mat A$ are $\vect x^{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, $\vect x^{(2)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
The eq. points are $(-3, 2)$ for $u^* = 1$, $(3, -2)$ for $u^* = -1$.
[Checked. ambiguous: the first point's minus sign merges with the bracket, and the "3" of the second could be read as "5" (the hand, not the photo); the values given are the correct ones and match the figure.]

Let $C^+$ be a path for $u^* = 1$, and $C^-$ for $u^* = -1$.

*Figure (two phase portraits, axes unlabelled).*
- Left ($u^* = 1$, not labelled on the figure): the equilibrium $(-3, 2)$, a dot in the second quadrant. Two solid lines through it with arrowheads pointing **away** from it: slope $-1$ (eigenvector $(1, -1)$) from upper left to lower right, passing near the origin and ending in the fourth quadrant; slope $1$ (eigenvector $(1, 1)$) from lower left to upper right. Dashed curves radiate outwards from the dot (unstable node).
- Right ($u^* = -1$): the same picture about the equilibrium $(3, -2)$ in the fourth quadrant: solid slope $-1$ line from the second quadrant through the origin region down to lower right, solid slope $1$ line, arrowheads outwards, dashed curves radiating out.

## HW 69 — Time-optimal control of linear systems (unstable example, cont.): region of controllability
_File `20261122_010507.jpg`. Header "Time-optimal control of linear systems (ex. unstable)"._

**Ex.** Thus the two paths that go to the origin are

*Figure (the two paths into $O$, two small sketches, axes unlabelled).* In both, $P$ is an open circle in the second quadrant (the equilibrium $(-3, 2)$) and $Q$ an open circle in the fourth quadrant (the equilibrium $(3, -2)$).
- Left: a solid curve leaves $P$, bends down and runs into $O$ tangent to the $x_1$-axis, with an arrow pointing towards $O$; a dashed curve continues from $O$ down to $Q$ (the rest of that trajectory).
- Right: a solid curve leaves $Q$, bends up and runs into $O$ tangent to the $x_1$-axis from the right, with an arrow towards $O$; a dashed curve joins $P$ to $O$.

Note that states that lie only on either $PO$ or $OQ$ go to $O$.
Consider an initial state above $POQ$. Then choosing $u^* = 1$ drives the state to infinity, as the $C^+$ path cannot intersect $QO$. Choosing $u^* = -1$ drives that state to $O$ only if the trajectory intersects $PO$. ["to" written above a blacked-out word] A similar situation occurs for an initial state below $POQ$.

Thus, for most initial states, the trajectory will not get to the origin under any control. We have a small, finite region of controllability as below:

*Figure (region of controllability).* Axes unlabelled. $P$ (open circle, upper left, second quadrant) and $Q$ (open circle, lower right, fourth quadrant). Solid: a curve from $P$ down to $O$, arriving tangent to the $x_1$-axis with an arrow towards $O$, and a curve from $Q$ up to $O$ with an arrow (up-left) towards $O$; together they form $POQ$. Dashed/dotted: an upper arc from $P$ running right, just above the solid curve, to the $x_2$-axis and on into the first quadrant, with small arrowheads pointing back up-left towards $P$; and a lower arc leaving $P$ downwards on the left, crossing the $x_1$-axis and running right along the bottom to $Q$, with small arrowheads pointing right towards $Q$. The region enclosed between the dashed arcs, around $POQ$, is the region of controllability.

[a blacked-out box] The region is bounded by the path on $C^+$ from $P$ to $Q$, and the $C^-$ path from $Q$ to $P$.

A larger bound for $\abs u$ gives a larger region of controllability.
$$u^* = \begin{cases} -1 & \text{above } POQ, \text{ on } QO \\ 1 & \text{below } POQ, \text{ on } PO \end{cases}$$
[The region figure is a rough sketch and the dashed arcs do not clearly join up; it can be redrawn from the sentence above it (boundary: the $C^+$ trajectory from $P$ to $Q$ and the $C^-$ trajectory from $Q$ to $P$).]

## HW 70 — Time-optimal control of linear systems (example: saddle)
_File `20261122_010521.jpg`. Header "Time-optimal control of linear systems (ex. saddle)"._

**Ex.** Solve the problem of time-optimal control to the origin for the system $\dot x_1 = x_1 + 3x_2 - 7u$, $\dot x_2 = 3x_1 + x_2 - 5u$, $\abs u \le 1$.

We have the system
$$\dot{\vect x} = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}\vect x + \begin{pmatrix} -7 \\ -5 \end{pmatrix}u$$
The Hamiltonian $H$ is
$$H = -1 + \psi_1(x_1 + 3x_2) + \psi_2(3x_1 + x_2) + u(-7\psi_1 - 5\psi_2)$$
$H$ is maximised w.r.t. $u$ if $u^* = \operatorname{sgn}[-7\psi_1 - 5\psi_2] = \pm1$
The optimal trajectories thus satisfy
$$\dot{\vect x} = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}\vect x + u\begin{pmatrix} -7 \\ -5 \end{pmatrix} \qquad u = \pm1$$
The eigenvalues of $\mat A$ are $\lambda_1 = -2$, $\lambda_2 = 4$.
The signs alternate, so we have a saddle point.
The eigenvectors of $\mat A$ are $\vect x^{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, $\vect x^{(2)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
The equilibrium points are given by:
$$u^* = 1: \ \begin{cases} x_1 + 3x_2 - 7 = 0 \\ 3x_1 + x_2 - 5 = 0 \end{cases} \Rightarrow x_1 = 1,\ x_2 = 2 \qquad u^* = -1: \ \begin{cases} x_1 + 3x_2 + 7 = 0 \\ 3x_1 + x_2 + 5 = 0 \end{cases} \Rightarrow x_1 = -1,\ x_2 = -2$$
[Checked.]

Thus the $C^+$ paths ($u^* = 1$) and $C^-$ paths ($u^* = -1$) are

*Figure (two saddle phase portraits, axes unlabelled).*
- Left ($C^+$): the saddle $(1, 2)$, a dot in the first quadrant. Through it, a solid line of slope $-1$ (stable direction $(1, -1)$) from the point labelled $A$ at the upper left to the point labelled $B$ at the lower right (crossing the $x_1$-axis right of the origin), with arrowheads pointing towards the saddle from both ends; and a solid line of slope $1$ (unstable direction $(1, 1)$) from the third quadrant up through the saddle to the upper right, with an arrowhead pointing away (up-right). In each of the four sectors a hyperbola-like curve with an arrow: they come in along the stable line and leave along the unstable line.
- Right ($C^-$): the same picture about the saddle $(-1, -2)$ in the third quadrant, with the stable line labelled $C$ at its upper-left end and $D$ at its lower-right end.

Note that any path $C^+$ above $A$ [the sentence stops here]

## HW 71 — Time-optimal control of linear systems (saddle example, cont.): infinite strip
_File `20261122_010524.jpg`. Header "Time-optimal control of linear systems (ex. saddle)". Lower 20% blank._

**Ex.** The two paths that go to the origin are

*Figure (paths into $O$ for the saddle example; two sketches, axes unlabelled).*
- Left: an S-shaped solid curve from $Q^-$ at the upper left (second quadrant) down across the $x_1$-axis, dipping below it in the third quadrant, rising through $O$, over a hump above the axis in the first quadrant, and down across the axis to $P_+$ at the lower right (fourth quadrant). Dot $P$ (the $u^* = 1$ saddle $(1,2)$) above the hump; dot $Q$ (the $u^* = -1$ saddle $(-1,-2)$) below the dip. The left half ($Q^-O$) is a $C^-$ path and the right half ($OP_+$) a $C^+$ path.
- Right: the same S-curve (ends labelled $Q^-$ and $P^+$) with two parallel dashed lines of slope $-1$ added, one through $P$ and one through $Q$ (the stable eigendirections of the two saddles), bounding a diagonal strip that contains the S-curve; a few dotted curves inside the strip near $O$ show other trajectories.

Note again that only states on $P_+OQ_-$ go to the origin.
Minimum time to the origin is attained by $\{1\}$ or $\{-1\}$.

Consider the control sequence $\{-1, 1\}$. Then a $C^-$ path will have to intersect $P^+O$ for it to go to the origin. This is similar for $\{1, -1\}$.

We can see that an initial state must be 'within an infinite corridor' for the trajectories to reach either $P^+O$ or $Q^-O$. Mathematically, the region of controllability is an infinite strip. Outside, control to $O$ is impossible.
$$u^* = \begin{cases} -1 & \text{below } Q^-OP^+,\ \text{on } Q^-O \\ 1 & \text{above } Q^-OP^+,\ \text{on } P^+O \end{cases}$$
[The labels switch between subscripts and superscripts as in the notes. "Minimum time to the origin is attained by $\{1\}$ or $\{-1\}$" refers to initial states on $P_+O$ or $Q_-O$.]

## HW 72 — EXT: time control of linear complex systems
_File `20261122_010541.jpg`. Header "EXT: Time control of linear complex systems"._

**N.** Note that if the system matrix $\mat A$ has complex eigenvalues, then so will the costate matrix $-\mat A\T$.
The controls which maximise $H$ are still piecewise constant $u^* = \pm1$ according to $\operatorname{sgn}[L\psi_1 + M\psi_2]$, but now our expression $L\psi_1 + M\psi_2$ can attain many zeroes.

When a system has complex eigenvalues, the system's uncontrolled (i.e. $u = 0$) [blacked-out word] behaviour is oscillatory. The optimal control will use these oscillations to drive the system to the origin.

When we worked with real eigenvalues, we did not need to solve the costate equations, as we had a lemma that stated there was only at most one switch.
However, with complex eigenvalues, we must find $\psi_1, \psi_2$ so we can determine exactly how $L\psi_1 + M\psi_2$ behaves.
["EXT" presumably marks extension material. $L, M$ here are the coefficients $\ell, m$ of HW 64–65.]

**Ex.** Solve the problem of time-optimal control to the origin for the system $\dot x_1 = x_2$, $\dot x_2 = -x_1 + u$, $\abs u \le 1$.

We have the system
$$\dot{\vect x} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\vect x + \begin{pmatrix} 0 \\ 1 \end{pmatrix}u$$
The Hamiltonian $H$ is
$$H = -1 + \psi_1 x_2 - \psi_2 x_1 + u\psi_2$$
which is maximised w.r.t. $u$ if $u^* = \operatorname{sgn}[\psi_2] = \pm1$.
[the sign before $\psi_2 x_1$ is written over a blacked-out mark; $-$ is correct]

The costate equations are:
$$\dot\psi_1 = -\partial H/\partial x_1 = \psi_2, \quad \dot\psi_2 = -\partial H/\partial x_2 = -\psi_1 \quad \Rightarrow \quad \ddot\psi_2 + \psi_2 = 0 \quad \Rightarrow \quad \lambda = \pm i$$

## HW 73 — EXT: time-optimal control of complex linear systems (example: centre)
_File `20261122_010544.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. centre)"._

**Ex.** (continued) This implies $S = \psi_2 = k\sin(t + \ell)$ where $k, \ell \in \R$.
The zeroes of $S$ are at $t = n\pi - \ell$ for $n \in \N$.

We now work with the state equations
$$\dot x_1 = x_2, \qquad \dot x_2 = -x_1 + u^*, \qquad u^* = \pm1$$
<u>Case 1:</u> $u^* = 1$
Make the substitution $\varepsilon = x_1 - 1$.
Then $\dot\varepsilon = x_2$ and $\dot x_2 = -\varepsilon$, and thus $\ddot\varepsilon + \varepsilon = 0$.
The solution is $\varepsilon = a\cos(t + \alpha)$, $a, \alpha \in \R$.
The family of trajectories is
$$x_1 - 1 = a\cos(t + \alpha), \quad x_2 = -a\sin(t + \alpha) \quad \Rightarrow \quad (x_1 - 1)^2 + x_2^2 = a^2 \quad \leftarrow C^+$$
<u>Case 2:</u> $u^* = -1$
Make the substitution $\varepsilon = x_1 + 1$.
Then $\dot\varepsilon = x_2$ and $\dot x_2 = -\varepsilon$, and thus $\ddot\varepsilon + \varepsilon = 0$.
The solution is $\varepsilon = b\cos(t + \beta)$, $b, \beta \in \R$.
The family of trajectories is
$$x_1 + 1 = b\cos(t + \beta), \quad x_2 = -b\cos(t + \beta) \quad \Rightarrow \quad (x_1 + 1)^2 + x_2^2 = b^2 \quad \leftarrow C^-$$
[possible error: $x_2 = \dot\varepsilon = -b\sin(t + \beta)$; the notes have $\cos$. The circle equation is right. $n \in \Z$ would be needed for all zeros.]

The optimal path to the origin must therefore consist of alternate arcs of $C^+$ and $C^-$ with the points/switches during/on the zeros of $S$. Thus the switches are at $t = n\pi - \ell$ (the switches are $\pi$ apart in time).
During this time a point on any $C^+$ or $C^-$ trajectory sweeps out a circular arc.

## HW 74 — EXT: time-optimal control of complex linear systems (centre, cont.): switching curve
_File `20261122_010550.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. centre)"._

**Ex.**

*Figure (the arcs $C_1^\pm$ into the origin).* Axes (unlabelled) with dots at $(-1, 0)$ and $(1, 0)$. $C_1^-$: the upper semicircle of radius 1 centred at $(-1, 0)$, from $(-2, 0)$ over the top to $O$, with an arrow pointing right (clockwise motion), labelled $C_1^-$. $C_1^+$: the lower semicircle of radius 1 centred at $(1, 0)$, from $(2, 0)$ under the axis to $O$, with an arrow pointing left (clockwise), labelled $C_1^+$.

The origin can be directly reached on either $C_1^+$ or $C_1^-$.
If the initial state lies on $C_1^+$ or $C_1^-$, simply stay on it.
Any other initial state must eventually take it onto a $C^-$ path that intersects $C_1^+$, or $C^+$ path → $C_1^-$.

Consider a path that switches onto $C_1^+$ at some point $Q$.
In $\tau - \pi \le t \le \tau$, it must have been on some $C^-$ through $Q$, where the previous switch is at some point $R$.
We construct a switching curve by determining the locus of $R$.

*Figure (locating the previous switch $R$).* Axes; points on the $x_1$-axis labelled $L$ (about $(-3, 0)$), $M$ (about $(-1, 0)$) and $N$ (about $(1, 0)$). The lower semicircle $C_1^+$ centred at $N$, with the point $Q$ on it (below the axis, just right of the $x_2$-axis) and a radius drawn from $N$ to $Q$. An upper semicircle of radius 1 centred at $L$, with the point $R$ on it and a radius drawn from $L$ to $R$. A straight segment from $R$ through $M$ to $Q$ ($R$ and $Q$ are symmetric about $M$). A dotted arc from $R$ over the top, clockwise, round to $Q$ (half a turn of the $C^-$ circle centred at $M$), with an arrowhead.

Thus the previous switch $R$ lies on the top half of the circle of radius 1 centered at $L$. Similarly, optimal paths switching onto $C_1^-$ must have had their previous switch on the lower half of the circle of radius 1 centred at $(3, 0)$. ["have" written above "had"]
Continuing this logic ad infinitum we obtain the switching curve:

*Figure (switching curve $\Gamma$).* The $x_1$-axis with ticks labelled $-4$, $-2$, $2$ (and $4$ implied). To the left of the origin, a row of upper semicircles of radius 1 standing on the axis (centred at $-1, -3, -5, -7$), each with an arrow pointing right along its top (clockwise). To the right of the origin, a row of lower semicircles of radius 1 hanging from the axis (centred at $1, 3, 5, 7$), each with an arrow pointing left along its bottom. The chain is labelled $\Gamma$ at its right end. A dotted circle (an example trajectory) is drawn around the origin region, roughly from $x_1 \approx -2.5$ to $2.5$ and mostly below the axis, with a short solid arrow on its lower-right arc.

$$u^* = \begin{cases} -1 & \text{above } \Gamma,\ \text{on } C_1^- \\ 1 & \text{below } \Gamma,\ \text{on } C_1^- \end{cases}$$
[possible error: the second line should read "on $C_1^+$" (on $C_1^-$ the control is $-1$).]

## HW 75 — EXT: time-optimal control of complex linear systems (example: spiral in)
_File `20261122_010555.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral in)"._

**Ex.** Solve the problem of time-optimal control to the origin for
$$\begin{pmatrix} \dot x_1 \\ \dot x_2 \end{pmatrix} = \begin{pmatrix} -k & 1 \\ 1 & -k \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} k \\ 1 \end{pmatrix}u \qquad \abs u \le 1$$
[possible error: the $(2,1)$ entry should be $-1$: the Hamiltonian below has $\psi_2(-x_1 - kx_2 + u)$, and the eigenvalues $-k \pm i$ need $\begin{pmatrix} -k & 1 \\ -1 & -k \end{pmatrix}$. The "$+$" before the control vector is written over a blacked-out mark.]

The Hamiltonian $H$ is
$$H = -1 + \psi_1(-kx_1 + x_2 + ku) + \psi_2(-x_1 - kx_2 + u)$$
which is maximised w.r.t. $u$ if $u^* = \operatorname{sgn}[k\psi_1 + \psi_2] = \pm1$.

Note that the eigenvalues of $\mat A$ are $\lambda = -k \pm i$.
The corresponding trajectories are clockwise spirals w/ equations
$$x_1 = u^* + ae^{-kt}\cos(t + \alpha), \qquad x_2 = -ae^{-kt}\sin(t + \alpha)$$
(Trajectories are found by solving above system with $u^* = 1$ and $u^* = -1$, finding crit. point $(t_1, t_2)$ and subbing into sol.)
[the critical point is $(x_1, x_2) = (u^*, 0)$; "$(t_1, t_2)$" is the notes' wording]

The costate equations are:
$$\dot\psi_1 = k\psi_1 + \psi_2, \quad \dot\psi_2 = -\psi_1 + k\psi_2 \quad \Rightarrow \quad \psi_1 = be^{kt}\cos(t + \beta), \quad \psi_2 = -be^{kt}\sin(t + \beta)$$
and so $S = ce^{kt}\sin(t + \gamma)$ (as linear combinations of cosine and sine functions give a sinusoidal curve) and has zeros at $t = -\gamma \pm n\pi$. (Therefore, the time interval between switches is $\pi$)
[Checked (with the corrected matrix).]

Similarly to the purely imaginary eigenvalue case / centre case, the optimal path to the origin must therefore consist of alternate arcs of $C^+$ and $C^-$ paths.
However, as these are spirals, the switching curve is going to be rather complicated.

Example trajectories for $C^+$ and $C^-$ are given in the next page.

## HW 76 — EXT: time-optimal control of complex linear systems (spiral in, cont.)
_File `20261122_010602.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral in)"._

**Ex.**

*Figure (one spiral trajectory for each control; two sketches, axes unlabelled).*
- Left, labelled $C_1^+$ (top) and $u^* = 1$ (bottom): the critical point $N$ is a tick on the positive $x_1$-axis close to the origin. A spiral winds once round $N$, clockwise and inwards: it starts as an arc entering from the lower left of the origin region, passes up and over $N$, round the right side, under the axis and back up, ending near the origin. A polar annotation at $N$: a short radius labelled $r$ with its angle $\theta$ marked.
- Right, labelled $C_1^-$ and $u^* = -1$: the mirror picture about $M$, a tick on the negative $x_1$-axis close to the origin, with the same $r$/$\theta$ annotation; the spiral winds round $M$ and passes through the origin region on its right.

The two paths to the origin is given here. WLOG translate time $t$ so that $P_1O$ reaches the origin at $t = 0$. If $S = 0$ at $t = 0$ then the previous switch was at $t = -\pi$ at $P_1$. If $S \ne 0$ the previous switch must have been on some $Q$ on $C_1^+$.

*Figure (the arcs $C_1^\pm$ into the origin).* Axes; ticks $M$ on the negative and $N$ on the positive $x_1$-axis, and the point $P_1$ further right on the positive $x_1$-axis. $C_1^-$: an arc rising from the lower left (left of $M$), over the top with an arrow pointing right, and down into $O$. $C_1^+$: an arc leaving $P_1$ downwards, through the point $Q$ (below the axis on the right), curving under the axis with an arrow pointing left, and up into $O$. The two arcs meet at $O$ in an S-shape (the $C_1^-$ arc continues slightly below the axis and the $C_1^+$ arc slightly above).

The arc $C_1^+$ can be described in terms of the parameter $\sigma$:
$$x_1 = 1 - e^{-k\sigma}\cos\sigma, \quad x_2 = e^{-k\sigma}\sin\sigma, \quad \sigma \in [-\pi, 0]$$
and the arc $C^-$ is simply $C^+$ translated to $M$ and rotated by $\pi$.

Tracing back through an angle $\pi$ along the $C^-$ curve through $Q$ we reach the previous switch point $R$.
We can show the locus of $R$ is given parametrically by
$$x_1 = -1 - 2e^{k\pi} + e^{k(\pi - \sigma)}\cos\sigma, \quad x_2 = -e^{k(\pi - \sigma)}\sin\sigma, \quad \sigma \in [-\pi, 0]$$
[Checked: $R - M = -e^{k\pi}(Q - M)$ with $M = (-1, 0)$.]

Note that $C_2^-$ is 'similar' to $C_1^+$ and expands by a factor $e^{k\pi}$. This repeats ad infinitum to obtain the switching curve $\Gamma$.

## HW 77 — EXT: time-optimal control of complex linear systems (spiral in, cont.): switching curve
_File `20261122_010607.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral in)". Lower half blank._

**Ex.** The switching curve $\Gamma$ is

*Figure (switching curve $\Gamma$ for the inward spiral).* Axes (unlabelled). Left of the origin, a chain of arcs standing on the $x_1$-axis above it, getting larger away from the origin (three arcs: a small one next to the origin, a medium one, and a large one furthest left). Right of the origin, a chain of arcs hanging below the $x_1$-axis, also getting larger away from the origin (three arcs: two small ones, then a large shallow one on the far right whose right end rises back up towards the axis). No arrows or labels on the figure.

The optimal control is therefore
$$u^* = \begin{cases} -1 & \text{above } \Gamma,\ \text{on } C_1^- \\ 1 & \text{below } \Gamma,\ \text{on } C_1^+ \end{cases}$$

## HW 78 — EXT: time-optimal control of complex linear systems (example: spiral out)
_File `20261122_010614.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral out)"._

**Ex.** Solve the problem of time-optimal control to the origin for
$$\begin{pmatrix} \dot x_1 \\ \dot x_2 \end{pmatrix} = \begin{pmatrix} k & 1 \\ -1 & k \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} -k \\ 1 \end{pmatrix}u \qquad \abs u \le 1,\ k > 0$$
The Hamiltonian $H$ is
$$H = -1 + \psi_1(kx_1 + x_2 - ku) + \psi_2(-x_1 + kx_2 + u)$$
which is maximised w.r.t. $u$ if $u^* = \operatorname{sgn}[-k\psi_1 + \psi_2] = \pm1$

Similarly to the previous example, $S = ce^{-kt}\sin(t + \gamma)$ has zeros at $t = -\gamma \pm n\pi$.

The eigenvalues of $\mat A$ are $\lambda = k \pm i$.
<u>$u^* = 1$:</u>
$$\begin{cases} \dot x_1 = kx_1 + x_2 - ku \\ \dot x_2 = -x_1 + kx_2 + u \end{cases} \quad \text{crit. point } N = (1, 0)$$
$$\Rightarrow x_1 - 1 = ae^{kt}\cos(t + \alpha) \Rightarrow x_2 = -ae^{kt}\sin(t + \alpha)$$
<u>$u^* = -1$:</u>
$$\begin{cases} \dot x_1 = kx_1 + x_2 + ku \\ \dot x_2 = -x_1 + kx_2 - u \end{cases} \quad \text{crit. point } M = (-1, 0)$$
$$\Rightarrow x_1 + 1 = ae^{kt}\cos(t + \alpha) \Rightarrow x_2 = -ae^{kt}\sin(t + \alpha)$$
[Checked. In the $u^* = -1$ block the $u$ has already been replaced by $-1$ ($+ku$, $-u$ should be $+k$, $-1$); the "$a$" in the last line looks like "$u$".]

*Figure (outward spirals; two sketches, axes unlabelled).*
- Left, labelled $C_1^+$ (top) and $u^* = 1$ (bottom): $N$ a tick on the positive $x_1$-axis; a spiral winding clockwise and outwards round $N$, about one and a half turns, passing to the left of the origin, with arrowheads (pointing up on the left side, down on the right side). The same $r$/$\theta$ polar annotation at $N$.
- Right, labelled $C_1^-$ and $u^* = -1$: the mirror picture round $M$ on the negative $x_1$-axis, spiralling clockwise outwards and passing to the right of the origin, with arrowheads.

## HW 79 — EXT: time-optimal control of complex linear systems (spiral out, cont.): switching curve
_File `20261122_010618.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral out)"._

**Ex.** The trajectories are clockwise spirals.
We construct the switching curve in a similar way to the inward spiral. Again the optimal path consists of alternate arcs of $C^+$ and $C^-$ paths.
Translate time $t$ so that $P_1O$ reaches the origin at $t = 0$.
If $S = 0$ at $t = 0$ then the previous switch was at $t = -\pi$ at $P_1$.
If $S \ne 0$ then the previous switch must have been on some $Q$ on $C_1^+$.

Tracing back by $\pi$ along the $C^-$ curve through $Q$ we reach the previous switch point $R$.
We can show the locus of $R$ is given parametrically by
$$x_1 = -1 - 2e^{k\pi} + e^{k(\pi + \sigma)}\cos\sigma, \quad x_2 = e^{k(\pi + \sigma)}\sin\sigma, \quad \sigma \in [-\pi, 0].$$
[possible error: with $C_1^+$ as below ($x_1 = 1 - e^{k\sigma}\cos\sigma$, $x_2 = e^{k\sigma}\sin\sigma$) and $R - M = -e^{-k\pi}(Q - M)$, $M = (-1, 0)$, the locus is $x_1 = -1 - 2e^{-k\pi} + e^{-k(\pi - \sigma)}\cos\sigma$, $x_2 = -e^{-k(\pi - \sigma)}\sin\sigma$. That is minus the notes' own $C_2^+$ below, which is consistent; the formula as written looks copied from the inward spiral (HW 76) with the signs of the exponents changed.]
Continuing this ad infinitum to obtain the switching curve $\Gamma$.
(Note the curve shrinks by a factor $e^{k\pi}$)

*Figure (switching curve for the outward spiral).* Axes (unlabelled). On each side of the origin, three arcs standing on the $x_1$-axis **above** it, the largest next to the origin and each further one smaller (shrinking away from the origin), with "$\cdots$" at both ends of the chain. The sketch is symmetric about the $x_2$-axis.
[By the symmetry used in the text (as in HW 74 and HW 77) the arcs for $x_1 > 0$ should hang below the axis; the sketch draws them above. The figure has no labels.]

Does the switching curve disappear? To answer this we need only examine the switching curve for $x_1 > 0$ (due to symmetry)

The loops are represented parametrically by:
$$\begin{aligned} C_1^+&: \ x_1 = 1 - e^{k\sigma}\cos\sigma, \quad x_2 = e^{k\sigma}\sin\sigma \\ C_2^+&: \ x_1 = 1 + 2e^{-k\pi} - e^{-k(\pi - \sigma)}\cos\sigma, \quad x_2 = e^{-k(\pi - \sigma)}\sin\sigma \\ &\ \ \vdots \\ C_{n+1}^+&: \ x_1 = 1 + 2\sum_{i=1}^n e^{-pk\pi} - e^{-k(n\pi - \sigma)}\cos\sigma, \quad x_2 = e^{-k(n\pi - \sigma)}\sin\sigma \end{aligned}$$
[the summation index is written $i$ below the sum and $p$ in the summand]
The distance between $P_n$ and $P_{n+1}$ is
$$e^{-nk\pi}(1 + e^{-k\pi}) \to 0$$
[Checked ($P_{n+1}$ is the point $\sigma = -\pi$ of $C_{n+1}^+$).]

## HW 80 — EXT: time-optimal control of complex linear systems (spiral out, cont.): region of control
_File `20261122_010624.jpg`. Header "EXT: Time-optimal control of complex linear systems (ex. spiral out)"._

**Ex.** Therefore, this distance $OP_{n+1}$ converges:
$$\begin{aligned} OP_{n+1} &= 1 + 2\sum_{p=1}^\infty e^{-pk\pi} + e^{-nk\pi} \\ &\to 1 + 2\sum_{p=1}^\infty e^{-pk\pi} \\ &= \frac{1 + e^{-k\pi}}{1 - e^{-k\pi}} \qquad \text{as } n \to \infty \end{aligned}$$
and similarly for $OQ_{n+1}$.
[the first sum should run to $n$, not $\infty$; the limit is right]

While there are an infinite number of arcs, the switching curve is thus bounded. Inside the region of control,
$$u^* = \begin{cases} -1 & \text{above } \Gamma \text{ and on } C_1^- \\ +1 & \text{below } \Gamma \text{ and on } C_1^+ \end{cases}$$

The region of control can be found by letting
↳ $t = 0$ at limit point $P$
$$\Rightarrow x_1 = 1 + ae^{kt}\cos t, \quad x_2 = -ae^{kt}\sin t$$
↳ $t = \pi$ at limit point $Q$
$$\Rightarrow x_1 = 1 - 2/(1 - e^{-k\pi}), \quad x_2 = 0$$
$P$ and $Q$ alternate – neither can be controlled to the origin.
[Checked: $a = 2e^{-k\pi}/(1 - e^{-k\pi})$ and $Q = -P$. The region of control is the region inside the $C^+$/$C^-$ arcs through $P$ and $Q$; the notes do not say so in words.]

In the region of control the system can still be controlled optimally to the origin with a finite number of switches. For any given initial state, we only need calculate the number $m$ of the loop on which the first switch takes place, and then construct the switching curve for $n \le m$.

## HW 81 — Optimal control to target curves
_File `20261122_010630.jpg`. Header "Optimal control to target curves"._

**N.** What if the ending point $\vect x_1$ at $t = t_1$ is not fixed, but instead lies on a given curve $C$?
Then, in a similar fashion to the calculus of variations, we must implement a transversality condition.

**Th. (4.3)** Let $u^*(t)$ be an admissible control that transfers the system from $\vect x_0$ at time $t_0$ to a point on some curve $C\colon g(x_1, x_2) = 0$ at time $t_1$.
Then for $u^*$ and $\vect x^*$ to be optimal, it is necessary that there exists:
↳ A non-trivial $\vect\psi = (\psi_0, \psi_1, \psi_2)$ such that $\dot\psi_i = -\partial H/\partial x_i$
↳ A scalar function $H(\vect\psi, \vect x, u) = \psi_0 f_0 + \psi_1 f_1 + \psi_2 f_2$
such that
↳ $H$ attains its maximum (w.r.t. $u$) at $u = u^*$ for all $t_0 \le t \le t_1$
↳ $H(\vect\psi^*, \vect x^*, u^*) = 0$
↳ $\begin{pmatrix} \psi_1(t_1) \\ \psi_2(t_1) \end{pmatrix}$ is perpendicular to the tangent of $C$ at $\vect x^*(t_1)$
[Not proved in the notes. There is no Th. 4.2 in the notes (the PMP is numbered 4.1, like the Euler–Lagrange theorem).]

**Cor.** If the state $\vect x_1$ at $t = t_1$ is completely unspecified, the transversality condition becomes
$$\begin{pmatrix} \psi_1(t_1) \\ \psi_2(t_1) \end{pmatrix} = \vect 0$$

## HW 82 — Problems where cost depends on $\vect x(t_1)$
_File `20261122_010638.jpg`. Header "Problems where cost depends on $\vect x(t_1)$"._

**N.** There are situations where the appropriate form for the cost functional is not an integral, but instead some function of the final state of the system.
For example:
↳ Maximising the concentration of a drug in a medical control problem
↳ Minimising the quantity of some pollutant by-product in an industrial process

**N.** If we wished to have a control without explicit constraints, but want to ensure the optimal control took sensible (i.e. not infinite) values, we could include a <u>penalty term</u> like:
$$\int_{t_0}^{t_1} u^2 \dd t \qquad \text{in the cost functional [blacked-out words]}$$
such that (for example)
$$J = -x_1(t_1) + \int_{t_0}^{t_1} u^2 \dd t$$

**N.** We express the general problem as follows:
Control the system $\dot{\vect x} = \vect f(\vect x, u)$ during $t_0 \le t \le t_1$ from a given initial state $\vect x_0$ such that
$$J = g(\vect x(t_1)) + \int_{t_0}^{t_1} f_0(\vect x, u) \dd t$$
is minimised. Find the optimal control $u^*$.

We must transform this problem so that we can apply the PMP.
[$u$ is underlined in "$\vect f(\vect x, \underline u)$" here only.]

## HW 83 — Problems where cost depends on $\vect x(t_1)$ (cont.): pseudo-costate variables
_File `20261122_010643(0).jpg`. Header "Problems where cost depends on $\vect x(t_1)$"._

**N.** (continued)
We introduce a new cost variable $X_0$, where
$$\dot X_0 = \sum_{i=1}^n \frac{\partial g}{\partial x_i} f_i + f_0 = \sum_{i=1}^n \frac{\partial g}{\partial x_i}\dot x_i + f_0$$
so that
$$X_0(t_1) = g(\vect x(t_1)) - g(\vect x(t_0)) + \int_{t_0}^{t_1} f_0 \dd t = J - g(\vect x(t_0))$$
[the second "=" is written over a blacked-out mark]
As $\vect x_0 = \vect x(t_0)$ is given, the quantity $g(\vect x(t_0))$ is known and constant, and thus minimising $J$ is equivalent to minimising $X_0(t_1)$.
We now apply PMP:
$$H = \psi_0\Bigl(f_0 + \sum_{i=1}^n \frac{\partial g}{\partial x_i} f_i\Bigr) + \sum_{i=1}^n \psi_i f_i$$
[the last subscript inside the bracket is written over a blacked-out mark]
We could proceed by setting $\psi_0 = -1$ and solving the problem with the costate equations (this is hard!)
Instead we can rearrange $H$:
$$H = -f_0 + \sum_{i=1}^n\Bigl(\psi_i - \frac{\partial g}{\partial x_i}\Bigr) f_i$$
and introduce 'pseudo-costate' variables
$$\lambda_i = \psi_i - \partial g/\partial x_i$$
$$H = -f_0 + \sum \psi_i f_i =: H' \quad \ast$$
[possible error: with the pseudo-costates, $H = -f_0 + \sum \lambda_i f_i =: H'$ (HW 84 uses $\lambda_j$); the line has $\psi_i$.]
We can show that
$$\lambda_i = \frac{-\partial H'}{\partial x_i} \qquad \text{(and so $\lambda_i$ acts just like a co-state variables)}$$
[possible error: this should be $\dot\lambda_i = -\partial H'/\partial x_i$ (the dot is missing; HW 84 uses $\dot\lambda$). "We can show" — not shown.]
As $\vect x_1$ is free we use the transversality condition
$$\psi_i(t_1) = 0 \Rightarrow \lambda_i(t_1) = \left.-\frac{\partial g}{\partial x_i}\right|_{t_1}$$
[$X_0$ here is a capital X; the notes elsewhere use $x_0$ for the cost variable (HW 58) and $\vect x_0$ for the initial state.]

## HW 84 — Problems where cost depends on $\vect x(t_1)$: summary and example
_File `20261122_010659.jpg`. Header "Problems where cost depends on $\vect x(t_1)$"._

**N.** As a summary, to solve this general problem:
↳ Write $H' = -f_0 + \sum \lambda_j f_j$
↳ Maximise $H'$ w.r.t. $u'$ [$u$ is meant]
↳ Apply end conditions $\vect x_0 = \vect x(t_0)$, $\lambda_i(t_1) = -\partial g/\partial x_i|_{t_1}$

**Ex.** Consider the system $\dot x = -\alpha x + u$ controlled from $x = 0$ at $t = 0$ to some $x(t_1)$ at $t = t_1$. ["$x = 0$" written above a blacked-out box]
Find the optimal control that minimises
$$J = -x(t_1) + \int_0^{t_1} u^2 \dd t$$
We have
$$H' = -u^2 + \lambda(-\alpha x + u)$$
with costate equations
$$\dot\lambda = -\partial H/\partial x = \alpha\lambda \Rightarrow \lambda = Ae^{\alpha t}$$
To maximise $H$ w.r.t. $u$,
$$\frac{\partial H}{\partial u} = -2u + \lambda = 0 \Rightarrow u^* = \frac{\lambda}{2}$$
and so $u^* = \frac12 Ae^{\alpha t}$.
Thus the optimal state equation is
$$\dot x = -\alpha x + u^* = -\alpha x + \tfrac12 Ae^{\alpha t} \Rightarrow x = Be^{-\alpha t} + Ae^{\alpha t}/4\alpha$$
[Checked.]

## HW 85 — Problems where cost depends on $\vect x(t_1)$: example (cont.)
_File `20261122_010703.jpg`. Header "Problems where cost depends on $\vect x(t_1)$". Lower fifth blank._

**Ex.** (continued)
We now consider the end conditions:
(1) $x(0) = 0$
$$0 = B + \frac{1}{4\alpha}A \Rightarrow B = -A/4\alpha$$
(2) $g(x(t_1)) = -x(t_1)$ so $g(x) = -x$
$$\Rightarrow \lambda(t_1) = -\frac{\partial g}{\partial x} = 1 \Rightarrow Ae^{\alpha t_1} = 1 \Rightarrow A = e^{-\alpha t_1}$$
[the "1" is written above a blacked-out box]
Hence
$$u^* = \tfrac12 e^{-\alpha t_1}e^{\alpha t} = \tfrac12 e^{\alpha(t - t_1)}$$
and
$$x = -e^{\alpha t_1}e^{-\alpha t} + \frac{1}{4\alpha}e^{\alpha(t - t_1)} = \frac{e^{-\alpha t_1}}{2\alpha}\Bigl[\frac{e^{\alpha t} - e^{-\alpha t}}{2}\Bigr] = \frac{e^{-\alpha t_1}}{2\alpha}\sinh(\alpha t)$$
[possible error: the first term should be $-\frac{1}{4\alpha}e^{-\alpha t_1}e^{-\alpha t}$ ($B = -e^{-\alpha t_1}/4\alpha$); the next two lines are right.]
