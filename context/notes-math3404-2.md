# MATH3404 Optimisation Theory: transcription, part 2 of 3 (HW 20–53)

_Calculus of variations. Sources, legibility check and conventions: see `claude/notes-math3404-1.md`. No dates are recorded._

---

## HW 20 — Introduction: calculus of variations
_File `20261122_010041.jpg`. Header "Introduction: calculus of variations"._

**Ex.** Consider the following example:

*Figure (a curve between two fixed points).* Axes: vertical axis $x$ (arrow up), horizontal axis $t$ (arrow right); the vertical axis is drawn a little in from the left, and the horizontal axis crosses it about a third of the way up. A small open circle in the first quadrant, close above the $t$-axis, labelled $(t_0, \vec x_0)$ below it. From it a smooth curve rises to a local maximum, dips to a local minimum (still above the start height), then rises steeply to a second open circle at the upper right, labelled $(t_1, \vec x_1)$. Below the $t$-axis: "$\vec x = \vec x(t) = (x_1(t), x_2(t))$".
[the subscript of the right endpoint's $t$ is written like a "g"/"2"; it is $t_1$ as in the text below. The figure uses arrow vectors $\vec x$, the text below plain $x$.]

Let $x(t)$ represent the equation of a plane curve.
Let $(t_0, \vec x_0)$ and $(t_1, \vec x_1)$ be two fixed points on the plane.
Recall the arclength of a curve:
$$L[x] = \int_{t_0}^{t_1} \sqrt{1 + \Bigl(\frac{\dd x}{\dd t}\Bigr)^2} \dd t$$

**Ex.** There are many different types of optimisation problems involving integrals of a family of curves:
(1) Classical isoperimetric problem:
What curve (closed, length $\ell$) surrounds the greatest (maximised) area?
(2) Minimising energy:
What curve minimises the energy needed for moving some $P$ from $A$ to $B$?
(3) Brachistochrone problem:
A particle $P$ slides down a curve from $A$ to $B$ under gravity. What curve minimises the time needed?

## HW 21 — Introduction: calculus of variations (cont.): functionals, the basic problem
_File `20261122_010045.jpg`. The photo is slightly soft overall, but every word reads (checked on full-resolution crops)._

**Def.** For the purposes of this course, a function is a mapping from some $U \subseteq \R^n$ to some $V \subseteq \R^m$.
A functional maps from some function $f$ (or some space of functions) to some $\Omega \subseteq \R^n$ (typically $\R$)

**N.** We wish to solve the following problem:
Find the curve $x(t)$ which joins the fixed point $(t_0, x_0)$ to $(t_1, x_1)$ that gives the functional
$$J[x] = \int_{t_0}^{t_1} f(t, x, \dot x) \dd t$$
a minimum value.

**Rem.** We will only cover cases where $x(t)$ is a scalar function, as solutions can be easily found using ODEs.

**N.** In other words, our problem asks us to find a curve $x^*(t)$ which satisfies $J[x] \ge J[x^*]$.
While this condition is necessary and sufficient, it gives us no clues on how to find this $x^*(t)$.
To find a necessary condition, we must make more assumptions.
We must also define a notion of 'closeness' for curves.

**N.** We will first cover solution to curves with both fixed end points.

## HW 22 — Admissible curves, variation curves and minimisers
_File `20261122_010050.jpg`. Header "Admissible curves, variation curves and minimisers"._

**Def.** The class of admissable curves are curves that are twice continuously differentiable and satisfy the end-point conditions $x(t_0) = x_0$ and $x(t_1) = x_1$.

**N.** We can now define our problem in terms of admissible curves. However, we still lack a definition of 'closeness' for curves.

**Def.** *A weak variation.*
Let $x^*(t)$ be a differentiable curve and let $x(t)$ be admissable. If $\exists$ small $\varepsilon_1 > 0$ and $\varepsilon_2 > 0$ such that
$$\abs{x^*(t) - x(t)} < \varepsilon_1 \quad \text{and} \quad \abs{\dot x^*(t) - \dot x(t)} < \varepsilon_2$$
for all $t_0 \le t \le t_1$, then $x(t)$ is a weak variation of $x^*(t)$.

**Def.** *A strong variation.*
Let $x^*(t)$, $x(t)$ be defined as above. If $\exists$ small $\varepsilon > 0$ such that $\abs{x^*(t) - x(t)} < \varepsilon$ for all $t_0 \le t \le t_1$, then $x(t)$ is a strong variation of $x^*(t)$.

**N.** We can now define what it means for a curve to be minimised.

**Def.** *Weak local minimiser*
A curve $x^*(t)\colon [t_0, t_1] \to \R$ is a weak local minimiser of a functional $J$ if $\exists$ small $\varepsilon_1, \varepsilon_2 > 0$ such that
$$J(x^*) \le J(x)$$
for all [blacked-out mark] $x(t)$ curves satisfying the boundary conditions and $\abs{x^*(t) - x(t)} < \varepsilon_1$ and $\abs{\dot x^*(t) - \dot x(t)} < \varepsilon_2$.

**Def.** *Strong local minimiser*
Similar definition to weak local minimisers, but with respect to strong variations.

## HW 23 — The Euler–Lagrange equation
_File `20261122_010054.jpg`. Header "The Euler–Lagrange equation", asterisk in the top right corner. Lower fifth blank._

**Th. (4.1)** *Euler–Lagrange* [the "Th." label is written over a blacked-out box]
Let $x^*(t)$ be a minimising curve of $J[x]$, such that $x(t)$ are admissible. Then it is necessary that
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = 0$$
at each point of $x^*(t)$.

**Def.** *Critical points of $J[x]$*
The function $x^*(t)$ is a critical point of
$$J[x] = \int_{t_0}^{t_1} f(t, x, \dot x) \dd t, \quad x(t_0) = x_0,\ x(t_1) = x_1$$
if it satisfies the Euler–Lagrange equation.

**Def.** The solutions of the Euler–Lagrange equation are called extremals.

**Rem.** If the integrand $f(t, x, \dot x)$ does not depend on $t$, then we have the second form of the Euler–Lagrange:
$$f - \dot x\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = c \qquad c \in \R$$
This is called also the Beltrani identity. [spelt "Beltrani"; usually "Beltrami"]

## HW 24 — Proving the Euler–Lagrange equation
_File `20261122_010058.jpg`. Header "Proving the Euler–Lagrange equation"._

**P.** Let $\eta\colon [t_0, t_1] \to \R$ be a $C^2$-function of continuous partial derivatives, such that $\eta(t_0) = \eta(t_1) = 0$.
Let $x(t) = x^* + \varepsilon\eta(t)$, $\varepsilon \in \R$. For all $\varepsilon \in \R$, let
$$F(\varepsilon) = J(x^* + \varepsilon\eta) = \int_{t_0}^{t_1} f(t, x + \varepsilon\eta, \dot x + \varepsilon\dot\eta) \dd t$$
[the arguments should be $x^* + \varepsilon\eta$, $\dot x^* + \varepsilon\dot\eta$; the notes drop the $*$ inside $f$ here and in the next display]
As $x^*$ is a weak local min of $J[x]$,
$$\exists \varepsilon_0: \quad \abs{x(t) - x^*(t)} = \abs{\varepsilon\eta(t)} \le \varepsilon_1, \quad \abs{\dot x(t) - \dot x^*(t)} = \abs{\varepsilon\eta'(t)} \le \varepsilon_2 \qquad \forall \varepsilon \le \varepsilon_0$$
Take $F(0)$. Then,
$$F(0) = J(x^*) \le J(x). \Rightarrow F'(0) = 0.$$
$$\begin{aligned} \left.\frac{\dd F(\varepsilon)}{\dd\varepsilon}\right|_{\varepsilon=0} &= F'(0) = \frac{\dd}{\dd\varepsilon} F(\varepsilon) = 0 \\ &= \frac{\dd}{\dd\varepsilon}\int_{t_0}^{t_1} f(t, x + \varepsilon\eta, \dot x + \varepsilon\dot\eta) \dd t\,\Big|_{\varepsilon=0} \\ &= \int_{t_0}^{t_1} \frac{\dd}{\dd\varepsilon} f(t, x + \varepsilon\eta, \dot x + \varepsilon\dot\eta) \dd t\,\Big|_{\varepsilon=0} \\ &= \int_{t_0}^{t_1} \Bigl[\frac{\partial f}{\partial x}\frac{\dd(\varepsilon\eta)}{\dd\varepsilon} + \frac{\partial f}{\partial x}\frac{\dd(\varepsilon\dot\eta)}{\dd\varepsilon}\Bigr]_{\varepsilon=0} \dd t \\ &= \int_{t_0}^{t_1} \frac{\partial f}{\partial x}\bigl(t, x^*(t), \dot x^*(t)\bigr)\eta(t) + \frac{\partial f}{\partial \dot x}\bigl(t, x^*(t), \dot x^*(t)\bigr)\dot\eta(t) \dd t \end{aligned}$$
[possible error: in the fourth line the second partial derivative should be $\partial f/\partial \dot x$ (written $\partial f/\partial x$); the next line has it right. The first derivative in that line is written with a curly $\partial\varepsilon$ in the denominator.]
Integrating by parts obtains:
$$\begin{aligned} \int_{t_0}^{t_1} \frac{\partial f}{\partial \dot x}\bigl(t, x^*(t), \dot x^*(t)\bigr)\frac{\dd\eta}{\dd t} \dd t &= \int_{t_0}^{t_1} \Bigl(\frac{\partial f}{\partial \dot x}\eta\Bigr)' \dd t - \int_{t_0}^{t_1} \frac{\dd}{\dd t}\frac{\partial f}{\partial \dot x}\,\eta \dd t \\ &= \underbrace{\frac{\partial f}{\partial \dot x}\eta(t)\Big|_{t_0}^{t_1}}_{=\,0} - \int_{t_0}^{t_1} \frac{\dd}{\dd t}\frac{\partial f}{\partial \dot x}\,\eta(t) \dd t \end{aligned}$$
[the "$= 0$" is written vertically under the boundary term]

## HW 25 — Proving the Euler–Lagrange equation (cont.); the second form
_File `20261122_010101.jpg`. Header "Proving the Euler–Lagrange equation"._

**P.** [continued; the first line begins with a long blacked-out phrase] We obtain:
$$\int_{t_0}^{t_1}\Bigl[\frac{\partial f}{\partial x}\bigl(t, x^*(t), \dot x^*(t)\bigr)\eta(t) - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\bigl(t, x^*(t), \dot x^*(t)\bigr)\Bigr)\eta(t)\Bigr] \dd t = 0$$
[dot missing: the second $\partial f/\partial \dot x$ is written $\partial f/\partial x$]
for all $\eta(t) \in C^2$ such that $\eta(t_0) = \eta(t_1) = 0$.

Choose $\eta(t) = (t - t_0)^3 (t - t_1)^3 \Bigl(\dfrac{\partial f}{\partial x} - \dfrac{\dd}{\dd t}\Bigl(\dfrac{\partial f}{\partial \dot x}\Bigr)\Bigr)$. Then,
$$\Rightarrow \int_{t_0}^{t_1}\Bigl[\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl[\frac{\partial f}{\partial \dot x}\Bigr]\Bigr]^2 (t - t_0)^3 (t_1 - t)^3 \dd t = 0$$
$$\Rightarrow \frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = 0. \quad \ast$$
[the integrand has $(t_1 - t)^3$ where $\eta$ has $(t - t_1)^3$; this changes only the sign, and the integral is still $0$]
Thus
$$\frac{\partial f}{\partial x}(t, x^*, \dot x^*) - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\Bigr) = 0$$
[dot missing in the second derivative, as above]

**P.** To prove the second form, where $f(x, \dot x)$:
$$\begin{aligned} \frac{\dd}{\dd t}\Bigl(f - \dot x\frac{\partial f}{\partial \dot x}\Bigr) &= \frac{\dd}{\dd t}\Bigl(f(x, \dot x) - \dot x\frac{\partial f}{\partial \dot x}\Bigr) \\ &= \frac{\partial f}{\partial x}\dot x + \frac{\partial f}{\partial \dot x}\ddot x - \ddot x\frac{\partial f}{\partial \dot x} - \dot x\frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) && \text{chain rule} \\ &= \dot x\Bigl[\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr)\Bigr] && \text{E–L first form} \\ &= 0 \end{aligned}$$
[dot missing in the last $\partial f/\partial \dot x$ of the third line]

**\*** This is because
(1) $(t - t_0)^3 (t - t_1)^3 < 0$ on $(t_0, t_1)$
(2) $\Bigl[\dfrac{\partial f}{\partial x} - \dfrac{\dd}{\dd t}\Bigl[\dfrac{\partial f}{\partial \dot x}\Bigr]\Bigr]^2 \ge 0$ trivially
so the integral is $0$ iff E–L equation holds.
[the step from "integral $= 0$" to "integrand $= 0$" also uses continuity of the integrand; not stated]

## HW 26 — Euler–Lagrange equation: examples
_File `20261122_010106.jpg`. Header "Euler–Lagrange equation – examples". Bottom quarter blank._

**Ex.** Find the extremal of
$$J[x] = \int_1^2 \dot x^2 t^3 \dd t \quad \text{where } x(1) = 0,\ x(2) = 3$$
Let $f(t, x, \dot x) = \dot x^2 t^3$.
Then $\dfrac{\partial f}{\partial x} = 0$ and $\dfrac{\partial f}{\partial \dot x} = 2\dot x t^3$.
By the Euler–Lagrange equation,
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl[\frac{\partial f}{\partial \dot x}\Bigr] = 0$$
↳ $0 - \dfrac{\dd}{\dd t}(2\dot x t^3) = 0$
↳ $2 \cdot \dfrac{\dd x}{\dd t} \cdot t^3 = k \in \R$
↳ $\dfrac{\dd x}{\dd t} = \dfrac{k}{2t^3}$
where the solution to the ODE is
$$x = \frac{K}{t^2} + c$$
Solving the IVP we obtain $x = 4 - \dfrac{4}{t^2}$.
This solution is a curve joining $(1, 0)$ and $(2, 3)$ which minimises $J[x]$.
[Checked ($K = -k/4$ absorbs the constant; the boundary conditions give $K = -4$, $c = 4$). "IVP" here is a boundary-value problem. The claim that it *minimises* $J$ is not shown (the E–L equation is only necessary).]

## HW 27 — Euler–Lagrange equation: examples (cont.)
_File `20261122_010111.jpg`. Header "Euler–Lagrange equation – examples"._

**Ex.** Find the extremal of
$$J[x] = \int_0^1 (t\dot x + \dot x^2) \dd t \quad \text{where } x(0) = 1,\ x(1) = 2.75$$
By first Euler–Lagrange equation:
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = 0$$
↳ $0 - \dfrac{\dd}{\dd t}(t + 2\dot x) = 0$
↳ $t + 2\dot x = c$
&nbsp;&nbsp;&nbsp;&nbsp;$\dot x = c - \frac12 t$
&nbsp;&nbsp;&nbsp;&nbsp;$x = -\frac14 t^2 + ct + d$
From initial conditions:
$$x = -\tfrac14 t^2 + 2t + 1$$
[Checked (the constant $c$ is renamed from line to line: $\dot x = c/2 - t/2$ strictly).]

**Ex.** Find the extremal of
$$J[x] = \int_0^1 (1 + t^2)\dot x^2 \dd t \quad \text{where } x(0) = \pi/2,\ x(1) = \pi$$
By Euler–Lagrange equation:
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl[\frac{\partial f}{\partial \dot x}\Bigr] = 0$$
↳ $0 - \dfrac{\dd}{\dd t}\bigl[2(1 + t^2)\dot x\bigr] = 0$
↳ $\dot x(1 + t^2) = c$
&nbsp;&nbsp;&nbsp;&nbsp;$x = c\arctan t + d$
From initial conditions:
$$x = 2\arctan t + \pi/2$$
[Checked.]

## HW 28 — The brachistochrone problem: setting up the functional
_File `20261122_010123.jpg`. Header "The brachistrochrone problem" [sic]._

**Ex.** Consider the brachistochrone problem.

*Figure (brachistochrone set-up, $x$ measured downwards).* A horizontal axis along the top, arrow to the right, labelled $t$; a vertical axis down the left side, arrow pointing **down**, labelled $x$ at the bottom. The start point $A$ is a small open circle at the origin (top-left corner, unlabelled). A curve falls steeply from the origin and flattens out, concave up, ending at a small open circle at the lower right labelled $B = (a, b)$ (the curve is nearly horizontal on arrival). A point on the curve about a third of the way along has a dashed horizontal line to the $x$-axis, where it is labelled $x(t)$, and a dashed vertical line up to the $t$-axis, labelled $t$ beside it. At that point a short arrow points straight down, labelled $F = mg$.

Let $T = T[x(t)]$ be the time at position $(t, x)$.
The arc-length and velocity at some $(t, x)$ is given by:
$$s(t) = \int_0^t \sqrt{1 + \dot x^2(t)} \dd t, \qquad v = \frac{\dd s}{\dd T}$$
We model the force acting on the object:
$$F = ma = m\frac{\dd v}{\dd T} = mg\cos\theta = mg\frac{\dd x}{\dd s}$$
$$\Rightarrow \frac{\dd^2 s}{\dd T^2} = g\frac{\dd x}{\dd s} \ \Rightarrow\ \frac{\dd s}{\dd T}\frac{\dd^2 s}{\dd T^2} = g\frac{\dd x}{\dd s}\frac{\dd s}{\dd T}$$
We then integrate both sides by $T$ using the chain rule:
<u>LHS:</u> $\displaystyle\int_0^T \frac{\dd s}{\dd T}\frac{\dd^2 s}{\dd T^2} \dd T = \int_0^T \frac{\dd}{\dd T}\Bigl[\frac12\Bigl(\frac{\dd s}{\dd T}\Bigr)^2\Bigr] \dd T$
<u>RHS:</u> $\displaystyle\int_0^T g\frac{\dd x}{\dd s}\frac{\dd s}{\dd T} \dd T = \int_0^T g\frac{\dd x}{\dd T} \dd T$
Note that $T(A) = 0$ and $x(0) = 0$. Then,
$$\frac12\Bigl(\frac{\dd s}{\dd T}\Bigr)^2 = gx \Rightarrow v = \sqrt{2gx}, \quad \dd T = \frac{\dd s}{\sqrt{2g}}$$
[possible error: $\dd T = \dd s / v = \dd s/\sqrt{2gx}$; the $x$ is missing under the root. The next display has it.]
The time $T[x]$ on $x(t)$ from $A$ to $B$ is thus:
$$T[x] = \int_A^B \dd T = \int_A^B \frac{\dd s}{v}\cdot\frac{\dd t}{\dd t} = \frac{1}{\sqrt{2g}}\int_0^a \frac{1}{\sqrt x}\frac{\dd s}{\dd t} \dd t = \frac{1}{\sqrt{2g}}\int_0^a \frac{\sqrt{1 + \dot x^2}}{\sqrt x} \dd t$$
[In this example $t$ is the horizontal coordinate and $T$ is time; the "T" is written in a curly hand that can look like "E" or "τ" (e.g. $v = \dd s/\dd T$). $\theta$ is the angle of the curve to the vertical; it is not marked in the figure. The initial speed $0$ at $A$ is used but not stated.]

## HW 29 — The brachistochrone problem: solution (cycloid)
_File `20261122_010127.jpg`. Header "The brachistochrone problem"._

**Ex.** [continued] We must therefore minimise (find the extremal) of
$$J[x] = \int \frac{\sqrt{1 + \dot x^2}}{\sqrt x} \dd t \qquad t(\theta_0) = 0,\ t(\theta_1) = a; \quad x(\theta_0) = 0,\ x(\theta_1) = b$$
We use the second form of the Euler–Lagrange equation:
$$f - \dot x\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = c$$
$$\Bigl(\frac{1 + \dot x^2}{x}\Bigr)^{1/2} - \dot x \times \frac{\dot x}{\bigl(x(1 + \dot x^2)\bigr)^{1/2}} = c$$
$$\bigl(x(1 + \dot x^2)\bigr)^{-1/2}\bigl((1 + \dot x^2) - \dot x^2\bigr) = c$$
and thus we obtain $x(1 + \dot x^2) = c$.
[the constant is renamed: strictly $x(1 + \dot x^2) = 1/c^2$]
We use a trig. substitution $\dot x = \tan\theta$. Thus
$$(1 + \dot x^2) = (1 + \tan^2\theta) = \sec^2\theta$$
which implies <u>$x = c\cos^2\theta$</u>.
We now have $x$ in terms of $\theta$. We must find $t$ in terms of $\theta$.
We differentiate $x = c\cos^2\theta$ w.r.t. $t$:
$$\dot x = \frac{\dd}{\dd\theta}(c\cos^2\theta)\,\dd\theta/\dd t = -2c\cos\theta\sin\theta\,\dot\theta = -\sin 2\theta\, c\dot\theta$$
[the bracket is written "$(\cos\theta)$"; the result shows $c\cos^2\theta$ is meant]
↳ $\tan\theta = -2c\cos\theta\sin\theta\,\dot\theta$
↳ $1 = -2c\dot\theta\cos^2\theta = -c\dot\theta(\cos 2\theta + 1)$
which is a first order separable ODE for $\dot\theta$.
Solving this we obtain
$$t = -c\bigl(\theta + \tfrac12\sin 2\theta\bigr) + K$$
Finally, let $k = c/2$, $\ell = K$, and noting that $x = c\cos^2\theta = \frac{c}{2}(1 + \cos 2\theta)$, we obtain
$$\begin{cases} x = k(1 + \cos 2\theta) \\ t = \ell - k(2\theta + \sin 2\theta) \end{cases}$$
where $\ell, k$ are found from initial conditions:
$$\begin{cases} x = b = k(1 + \cos 2\theta_1) \\ t = a = -k(2\theta_1 + \sin 2\theta_1) \end{cases}\Bigg|_{\theta = \theta_1}$$
[Checked up to the last display. possible error: the last line drops $\ell$ ($t = a = \ell - k(2\theta_1 + \sin 2\theta_1)$); the conditions $t(\theta_0) = 0$, $x(\theta_0) = 0$ that fix $\ell$ are not used. The word "cycloid" does not appear in the notes.]

## HW 30 — Fixed endpoint problem: derivation of the Euler–Lagrange equation
_File `20261122_010137.jpg`. Header "Fixed endpoint problem"._

**Def.** In a general fixed endpoint problem, we minimise
$$J[x] = \int_{t_0}^{t_1} f(t, x, \dot x) \dd t, \qquad (t_0, x(t_0)),\ (t_1, x(t_1)) \text{ fixed}$$
Let $y = x^*(t) + \varepsilon\eta(t)$ be a weak variation satisfying the fixed endpoints. We will show that if $x^*(t)$ is a minimising curve, then the Euler–Lagrange equation follows.

**P.** Consider
$$\begin{aligned} 0 &\le J[y] - J[x^*] \\ &= -\int_{t_0}^{t_1} f(t, x^*, \dot x^*) \dd t + \int_{t_0}^{t_1} f(t, x^* + \varepsilon\eta, \dot x^* + \varepsilon\dot\eta) \dd t \\ &= \int_{t_0}^{t_1} f(t, x^* + \varepsilon\eta, \dot x^* + \varepsilon\dot\eta) - f(t, x^*, \dot x^*) \dd t \\ &= \int_{t_0}^{t_1} \bigl(f_x(t, x^*, \dot x^*)\varepsilon\eta + f_{\dot x}(t, x^*, \dot x^*)\varepsilon\dot\eta\bigr) \dd t + O(\varepsilon^2) && \text{Taylor's theorem} \\ &= \int_{t_0}^{t_1} \Bigl(f_x(t, x^*, \dot x^*) - \frac{\dd}{\dd t} f_{\dot x}(t, x^*, \dot x^*)\Bigr)\varepsilon\eta \dd t + \bigl[f_{\dot x}(t, x^*, \dot x^*)\varepsilon\eta\bigr]_{t_0}^{t_1} + O(\varepsilon^2) && \text{Integration by parts} \\ &= \int_{t_0}^{t_1} \Bigl(f_x(t, x^*, \dot x^*) - \frac{\dd}{\dd t} f_{\dot x}(t, x^*, \dot x^*)\Bigr)\varepsilon\eta \dd t + O(\varepsilon^2) \end{aligned}$$
[The labels "Taylor's theorem" and "Integration by parts" are written in the left margin with braces spanning the lines. A small blacked-out mark sits before $\varepsilon\dot\eta$ in the Taylor line. The boundary term vanishes because $\eta(t_0) = \eta(t_1) = 0$; this is not written.]
This implies from the following lemma that
$$f_x(t, x^*, \dot x^*) - \frac{\dd}{\dd t} f_{\dot x}(t, x^*, \dot x^*) = 0$$

## HW 31 — Fixed endpoint problem: lemmas; fundamental lemma of the calculus of variations
_File `20261122_010142.jpg`. Header "Fixed endpoint problem". "L." = lemma._

**L.** By Taylor's theorem,
$$f(t, x^* + \varepsilon\eta, \dot x^* + \varepsilon\dot\eta) - f(t, x^*, \dot x^*) = f_x(t, x^*, \dot x^*)\varepsilon\eta + f_{\dot x}(t, x^*, \dot x^*)\varepsilon\dot\eta + O(\varepsilon^2)$$

**L.** By integration by parts,
$$\int_{t_0}^{t_1} u\dot v \dd t = [uv]_{t_0}^{t_1} - \int_{t_0}^{t_1} \dot u v \dd t$$
We set $u = f_{\dot x}(t, x^*, \dot x^*)$ and $\dot v = \varepsilon\dot\eta$.
Thus $\dot u = \frac{\dd}{\dd t} f_{\dot x}(t, x^*, \dot x^*)$ and $v = \varepsilon\eta$.
We obtain
$$\int_{t_0}^{t_1} f_{\dot x}(t, x^*, \dot x^*)\varepsilon\dot\eta \dd t = \bigl[f_{\dot x}(t, x^*, \dot x^*)\varepsilon\eta\bigr]_{t_0}^{t_1} - \int_{t_0}^{t_1} \frac{\dd}{\dd t} f_{\dot x}(t, x^*, \dot x^*)\varepsilon\eta \dd t$$
[the dots on $\dot v$ and on $\dot\eta$ in the integrand are faint; read from context]

**L.** If $m(t)\colon [t_0, t_1] \to \R$ is continuous and satisfies
$$\int_{t_0}^{t_1} m(t)\eta(t) = 0 \qquad \forall \eta \in C^2: \eta(t_0) = \eta(t_1) = 0$$
then $m(t) = 0$ $\forall t \in [t_0, t_1]$.
**\*** *Fundamental lemma of calculus of variations* [written beside the statement]

**P.** Suppose $\exists \alpha \in (t_0, t_1)$ s.t. $m(\alpha) \ne 0$. As $m$ is continuous, choose some $\varepsilon > 0$ s.t. $m(t) > 0$ or $m(t) < 0$ in some nbhd. of $\alpha$. Choose
$$\eta(t) = \begin{cases} (t - \alpha + \varepsilon)^3(\alpha + \varepsilon - t)^3 & \forall t \in [\alpha - \varepsilon, \alpha + \varepsilon] \\ 0 & \forall t \in [t_0, \alpha - \varepsilon) \cup (\alpha + \varepsilon, t_1] \end{cases}$$
Then
$$\int_{t_0}^{t_1} m(t)\eta(t) \dd t = \int_{\alpha - \varepsilon}^{\alpha + \varepsilon} m(t)\eta(t) \dd t > 0$$
which is impossible. Thus $m(t) = 0$.
[The hand switches between "$\alpha$" and "$a$" for the same point; written $\alpha$ throughout. "$\varepsilon > 0$" is written like "$c > 0$". "$> 0$" covers the case $m > 0$ near $\alpha$ ($< 0$ otherwise); the integral should be $\ne 0$. The step from $(t_0, t_1)$ to $[t_0, t_1]$ (continuity at the endpoints) is not stated.]

## HW 32 — Variable endpoint problem: transversality condition
_File `20261122_010148.jpg`. Header "Variable endpoint problem"._

**Def.** We now consider a variable endpoint problem.
We minimise
$$J[x] = \int_{t_0}^{t_1} f(t, x, \dot x) \dd t$$
subject to a fixed starting point $(t_0, x(t_0))$ and a variable endpoint $(t_1, x(t_1))$, where the coordinate $x$ lies on some given curve $x = c(t)$, $t_1$ unknown.

*Figure (variable endpoint on a curve).* Axes: vertical $x$ (arrow up) at the left, horizontal $t$ (arrow right) along the bottom. A small open circle in the lower middle-left labelled $(t_0, x_0)$ below it. A solid curve from it rises, flattens into a hump, dips slightly and ends at a small open circle labelled $(t_1, x(t_1))$ on the target curve. The target curve $x = c(t)$ is drawn at the right: it starts high, comes down almost vertically, then bends to the right and down to just above the $t$-axis, where it is labelled $x = c(t)$. Two dashed comparison curves leave $(t_0, x_0)$: one above the solid curve (higher hump, ending on the target curve above the solid endpoint) and one nearly horizontal below it, running to the target curve lower down. A short dashed segment also sits under the solid curve's hump.

In this case, the Euler–Lagrange equation will give an infinite number of solutions.
To reduce the number of candidate points, we add more necessary conditions using a transversality condition.

**Def.** The transversality condition is given by:
$$f(t_1) + \bigl(\dot c(t_1) - \dot x^*(t_1)\bigr)\frac{\partial f}{\partial \dot x}(t_1) = 0$$
[$f(t_1)$ means $f\bigl(t_1, x^*(t_1), \dot x^*(t_1)\bigr)$. Not derived in the notes.]

Thus to find extremals of $J[x]$ with a variable endpoint, we require three conditions:
↳ $x(t_0) = x_0$, $(t_0, x_0)$ known
↳ $x(t_1) = c(t_1)$
↳ Transversality condition

## HW 33 — Variable endpoint problem: two special cases
_File `20261122_010154.jpg`. Header "Variable endpoint problem"._

**Def.** There are two 'special cases' in the variable endpoint problem:
↳ Fixed, constant $x(t_1) = c(t)$
↳ Known $t_1$, unknown $x(t_1)$

**Def.** Special case 1: if $c(t)$ is constant, then the transversality condition is given by:
$$f(t_1) - \dot x^*(t_1)\frac{\partial f}{\partial \dot x}(t_1) = 0$$
Here is an illustration:

*Figure (special case 1: endpoint on a horizontal line).* Axes: vertical axis (arrow up, unlabelled) at the left, horizontal axis (arrow right, unlabelled) at the bottom. A horizontal solid line about two-thirds of the way up, labelled $x = c(t) = c$ at its right end. A small open circle at lower left labelled $(t_0, x_0)$. A solid curve rises from it, levels off in a gentle S and rises again to meet the horizontal line at an open circle labelled $(t_1, c)$ above it. Two dashed comparison curves from $(t_0, x_0)$: one above, rising close under the line and meeting it a little left of $(t_1, c)$; one below, running nearly flat then rising to meet the line to the right of $(t_1, c)$.

**Def.** Special case 2: if $t$ is known, then the transversality condition is given by:
$$\lim_{\dot c(t_1) \to \infty} \frac{1}{\dot c(t_1)} f(t_1) + \Bigl(1 - \frac{\dot x^*(t_1)}{\dot c(t_1)}\Bigr)\frac{\partial f}{\partial \dot x}(t_1) = 0$$
which implies
$$\left.\frac{\partial f}{\partial \dot x}\right|_{t_1} = 0$$
[i.e. the transversality condition divided by $\dot c(t_1)$, with the target curve a vertical line, $\dot c \to \infty$; the "$t$" in "if $t$ is known" is $t_1$]
Here is an illustration:

*Figure (special case 2: endpoint on a vertical line, $x(t_1)$ free).* Axes: vertical $x$ (arrow up) at the left, horizontal $t$ (arrow right) at the bottom. A vertical solid line at the right, crossing the $t$-axis where it is labelled $t = t_1$ below. A small open circle at lower left labelled $(t_0, x_0)$. A solid curve rises from it, runs across in a gentle wave (up, flat, dip, up) and meets the vertical line at an open circle labelled $(t_1, x(t_1)$ free$)$. Dashed comparison curves from $(t_0, x_0)$: one rising to a high arch then coming down to meet the vertical line below the solid endpoint; one wavy just above/around the solid curve; and one horizontal dashed line low down running to the vertical line.

## HW 34 — Proving the transversality condition
_File `20261122_010201.jpg`. Header "Proving the transversality condition"._

**N.** Let $x^*(t)$ be a minimising curve that intersects $c(t)$ at $t = t_1$. Let $y = x^*(t) + \varepsilon\eta(t)$ be a weak variation with start point $(t_0, x(t_0))$ and endpoint on the curve at $t = t_1 + \Delta T$. Then the transversality condition follows.

**P.** We begin with:
$$y(t_1 + \Delta T) = x^*(t_1 + \Delta T) + \varepsilon\eta(t_1 + \Delta T) = x^*(t_1) + \Delta T\,\dot x^*(t_1) + \varepsilon\eta(t_1) + O(\varepsilon^2)$$
and
$$y(t_1 + \Delta T) = c(t_1 + \Delta T) = c(t_1) + \Delta T\,\dot c(t_1) + O(\varepsilon^2)$$
Thus
$$x^*(t_1) + \Delta T\,\dot x^*(t_1) + \varepsilon\eta(t_1) = c(t_1) + \Delta T\,\dot c(t_1)$$
and since $x^*(t_1) = c(t_1)$, we have:
$$\varepsilon\eta(t_1) = \bigl(\dot c(t_1) - \dot x^*(t_1)\bigr)\Delta T$$
[$\Delta T = O(\varepsilon)$ is assumed in the $O(\varepsilon^2)$ terms but not stated]

Now consider the variation in $J$:
$$\begin{aligned} \Delta J = J[y] - J[x^*] &= \int_{t_0}^{t_1 + \Delta T} f(t, x^* + \varepsilon\eta, \dot x^* + \varepsilon\dot\eta) \dd t - \int_{t_0}^{t_1} \cdots \dd t \\ &= \int_{t_1}^{t_1 + \Delta T} f(t, x^* + \varepsilon\eta, \dot x^* + \varepsilon\dot\eta) \dd t \\ &\quad + \int_{t_0}^{t_1}\Bigl(\frac{\partial f}{\partial x}(t, x^*, \dot x^*)\varepsilon\eta + \frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\dot\eta\Bigr) \dd t + O(\varepsilon^2) \end{aligned}$$
[a note "$f(t, x^*, \dot x^*)$" above the second integral, with two short strokes pointing down at its "$\cdots$"]

## HW 35 — Proving the transversality condition (cont.)
_File `20261122_010205.jpg`. Header "Proving the transversality condition"._

**P.** [continued] Note that:
$$\begin{aligned} &\int_{t_0}^{t_1}\Bigl(\frac{\partial f}{\partial x}(t, x^*, \dot x^*)\varepsilon\eta + \frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\dot\eta\Bigr) \dd t \\ &= \int_{t_0}^{t_1} \frac{\partial f}{\partial x}(t, x^*, \dot x^*)\varepsilon\eta \dd t + \Bigl[\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\eta\Bigr]_{t_0}^{t_1} - \int_{t_0}^{t_1} \frac{\dd}{\dd t}\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\eta \dd t \\ &= \int_{t_0}^{t_1}\Bigl(\frac{\partial f}{\partial x}(t, x^*, \dot x^*) - \frac{\dd}{\dd t}\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\Bigr)\varepsilon\eta \dd t + \Bigl[\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\eta\Bigr]_{t_0}^{t_1} \end{aligned}$$
Thus:
$$\begin{aligned} \Delta J &= f(t_1, x^*, \dot x^*)\Delta T + \int_{t_0}^{t_1}\Bigl(\frac{\partial f}{\partial x}(t, x^*, \dot x^*) - \frac{\dd}{\dd t}\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\Bigr)\varepsilon\eta \dd t + \Bigl[\frac{\partial f}{\partial \dot x}(t, x^*, \dot x^*)\varepsilon\eta\Bigr]_{t_0}^{t_1} + O(\varepsilon^2) \\ &= f(t_1, x^*, \dot x^*)\Delta T + f_{\dot x}(t_1, x^*, \dot x^*)\varepsilon\eta(t_1) + O(\varepsilon^2) \end{aligned}$$
by the fact $x^*$ is an extremal (and thus satisfies E–L) and that $\eta(t_0) = 0$. Using the first result we obtained:
$$\Delta J = \Delta T\bigl(f(t_1, x^*, \dot x^*) + (\dot c(t_1) - \dot x^*(t_1)) f_{\dot x}\bigr)$$
[the first integral $\int_{t_1}^{t_1+\Delta T} f \dd t$ is replaced by $f(t_1, x^*, \dot x^*)\Delta T$ without comment (to first order)]

Given that the extremal minimises (or, is a critical point) of $J$, the first variation $\dd\Delta J/\dd\varepsilon = 0$.
The transversality condition [blacked-out mark] follows:
$$0 = \frac{\eta(t_1)}{\dot c(t_1) - \dot x^*(t_1)}\Bigl(f(t_1, \cdots) + \bigl(\dot c(t_1) - \dot x^*(t_1)\bigr) f_{\dot x}\Bigr)$$
$$\Rightarrow f(t_1) + \bigl(\dot c(t_1) - \dot x(t_1)\bigr)\frac{\partial f}{\partial \dot x}(t_1) = 0.$$
[ambiguous: the numerator starts with a mark like "×" or "x" before $\eta(t_1)$ (the hand, not the photo); from $\Delta T = \varepsilon\eta(t_1)/(\dot c - \dot x^*)$ the derivative in $\varepsilon$ gives just $\eta(t_1)$, so it is read as a multiplication sign. The last line drops the $*$ on $\dot x$.]

## HW 36 — Variable endpoint problem: example
_File `20261122_010211.jpg`. Header "Variable endpoint problem – examples". Bottom quarter blank._

**Ex.** Find the extremal of
$$\int_1^T \dot x^2 t^3 \dd t \qquad x(1) = 0,\ T > 1, \qquad x(T) \text{ lies on } c(t) = \frac{2}{t^2} - 3.$$
We know from previously that extremals have the form $x = k/t^2 + c$.
From the initial condition $x(1)$ we thus have:
$$x = k/t^2 - k$$
We apply the transversality condition:
$$f(t_1) + \bigl(\dot c(t_1) - \dot x^*(t_1)\bigr)\frac{\partial f}{\partial \dot x}(t_1) = 0$$
where $f(t) = \dot x^2 t^3$, $t_1 = T$. Thus,
$$\dot x(T)^2 T^3 + 2\dot x(T) T^3\bigl(-4/T^3 + 2k/T^3\bigr) = 0$$
$$\Rightarrow -\frac{2k}{T^3}T^3 + 2T^3\bigl(-4/T^3 + 2k/T^3\bigr) = 0$$
$$\Rightarrow 2k - 8 = 0 \Rightarrow k = 4.$$
We now determine $T$:
$$c(T) = 2/T^2 - 3 = 4/T^2 - 4 = x(T) \Rightarrow T = \pm\sqrt2 \Rightarrow T = \sqrt2 > 1$$
Thus $x^*(t)$ meets $c(t)$ at $(T, x(T)) = (\sqrt2, -2)$.
[Checked. The second line divides by $\dot x(T) = -2k/T^3$ without saying so ($k \ne 0$); the constant $c$ of the extremal clashes with the curve $c(t)$, as in the notes.]

## HW 37 — Variable endpoint problem: examples (cont.), case (i)
_File `20261122_010215.jpg`. Header "Variable endpoint problem – examples". A blacked-out word sits on its own line before "We use"._

**Ex.** Find the extremal of
$$\int_0^T (x^2 + \dot x^2) \dd t \quad \text{where (i) } x(0) = 1,\ T = 2; \quad \text{(ii) } x(0) = 1,\ x(T) = 2; \quad \text{(iii) } x(0) = 0,\ x(T) = 2$$
We use the Euler–Lagrange equation:
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial \dot x}\Bigr) = 0, \qquad 2x - \frac{\dd}{\dd t}(2\dot x) = 0$$
so we have $\ddot x - x = 0$. The solution to this ODE is
$$x(t) = Ae^t + Be^{-t}$$
For (i):
The t.c. is $\dfrac{\partial f}{\partial \dot x}(T) = 0 \Rightarrow 2\dot x(T) = 0 \Rightarrow \dot x(2) = 0$
This implies that $B = Ae^4$. Hence,
$$\begin{aligned} x(t) &= Ae^t + Ae^4 e^{-t} \\ &= \frac{1}{1 + e^4}e^t + \frac{e^4}{1 + e^4}e^{-t} \qquad \text{(from } A + B = 1\text{)} \\ &= \frac{e^{-2}}{e^{-2} + e^2}e^t + \frac{e^2}{e^{-2} + e^2}e^{-t} \\ &= \frac{e^{t-2} + e^{-(t-2)}}{e^{-2} + e^2} \\ &= \frac{\cosh(t - 2)}{\cosh(2)} \end{aligned}$$
[Checked. "t.c." = transversality condition (special case 2, HW 33).]

## HW 38 — Variable endpoint problem: examples (cont.), cases (ii) and (iii)
_File `20261122_010220.jpg`. Header "Variable endpoint problem – examples". Lower quarter blank._

**Ex.** For (ii):
The t.c. is
$$f(T) - \dot x(T)\frac{\partial f}{\partial \dot x}(T) = 0$$
$$\Rightarrow (Ae^T + Be^{-T})^2 + (Ae^T - Be^{-T})^2 - 2(Ae^T - Be^{-T})^2 = 0$$
$$\Rightarrow 2AB + 2AB = 0 \Rightarrow AB = 0$$
Thus by the null factor law, either
$$x = e^t \quad \text{or} \quad x = e^{-t} \qquad \text{(from } A + B = 1\text{)}$$
However, as $x(T) = 2$, $x = e^{-t}$ is unattainable as $t > 0$.
Thus, the extremal is $x(t) = e^t$, with $(T, x(T)) = (\ln 2, 2)$.
[Checked (special case 1, HW 33, with $c = 2$).]

For (iii):
From the initial condition we have $A + B = 0$.
The t.c. is
$$f(T) - \dot x(T)\frac{\partial f}{\partial \dot x}(T) = 0 \Rightarrow AB = 0 \quad \text{from (ii)}$$
This is a problem, as $A = 0$, $B = 0$, so $x = 0$ is the extremal. This does not intersect $x = 2$ for any $T$, so an extremal (under our current conditions) does not exist. ["an" is written above a blacked-out word]
[the dot on $\partial \dot x$ in the (iii) t.c. is missing in the hand]

## HW 39 — Minimising curves
_File `20261122_010224.jpg`. Header "Minimising curves." Lower quarter blank._

**N.** The Euler–Lagrange equation does not actually find a minimum of a functional. Instead, we examine extremals (which may be maxima or minima).

**Ex.** Return to the previous example
$$J[x] = \int_1^2 \dot x^2 t^3 \dd t, \quad x(1) = 0,\ x(2) = 3$$
This functional has an extremal
$$x^*(t) = 4 - 4/t^2$$
Let $y(t) = x^* + \eta(t)$ be a variation, where $\eta \in C^1$, $\eta(1) = \eta(2) = 0$, but $\eta$ is not necessarily small. Then,
$$\begin{aligned} \Delta J = J[y] - J[x^*] &= \int_1^2 t^3(8/t^3 + \dot\eta)^2 \dd t - \int_1^2 t^3(8/t^3)^2 \dd t \\ &= \int_1^2 16\dot\eta + \dot\eta^2 t^3 \dd t \\ &= [16\eta]_1^2 + \int_1^2 \dot\eta^2 t^3 \dd t \\ &= 0 + \int_1^2 \dot\eta^2 t^3 \dd t \ge 0 \end{aligned}$$
So the extremal $x^*(t)$ is a minimising curve.
[Checked.]

## HW 40 — Corner curves: $D_1$ curves and the corner conditions
_File `20261122_010229.jpg`. Header "Corner curves". Lower quarter blank._

**N.** Up until this point, we have found smooth extremals. However, sometimes the minimising curve is not smooth ($C_1$) but is in the collection of $D_1$ curves.

**Def.** We define $D_1$ as the set of continuous, piecewise smooth curves. Alternatively, piecewise smooth means continuously differentiable except for a finite number of corners (i.e. jumps in the derivative).

**Rem.** At some corner $(t, x^*(t))$ we denote the left-hand slope by $\dot x^*(t^-) = p_1$ and the right-hand slope by $\dot x^*(t^+) = p_2$.

**Th.** For a $D_1$ curve to be a minimising curve for a fixed end-point problem, the following conditions are necessary:
(1) The Euler–Lagrange equation is satisfied between corners, and between a corner and an endpoint.
(2) $\partial f/\partial \dot x$ is continuous at a corner.
(3) $f - \dot x\dfrac{\partial f}{\partial \dot x}$ is continuous at a corner.
[Not proved in the notes. (2) and (3) are the Weierstrass–Erdmann corner conditions, but the notes do not name them.]

## HW 41 — Corner curves: example where the smooth extremal fails
_File `20261122_010236.jpg`. No header (the page starts with the example)._

**Ex.** Find a minimising curve for
$$J[x] = \int_0^4 x^2(\dot x - 1)^2 \dd t \qquad x(0) = 0,\ x(4) = 2.$$
We use the Beltrani identity:
$$f - \dot x\frac{\partial f}{\partial \dot x} = c$$
$$\Rightarrow x^2(\dot x - 1)^2 - \dot x \cdot 2(\dot x - 1)x^2 = c$$
$$-x^2(\dot x^2 - 1) = c$$
$$\Rightarrow \dot x^2 = \frac{-c + x^2}{x^2} \Rightarrow \dot x = \frac{\sqrt{x^2 - c}}{x}$$
We solve this differential equation:
$$\int \frac{x}{\sqrt{x^2 - c}} \dd x = t + k$$
$$\Rightarrow \sqrt{x^2 - c} = t + k \Rightarrow x^2 - c = (t + k)^2$$
From the initial condition $x(0) = 0$ we obtain $-c = k^2$.
From $x(4) = 2$ we obtain
$$4 + k^2 = (4 + k)^2 \Rightarrow k = -3/2$$
Therefore $x^2 = t^2 - 3t \Rightarrow (t - 3/2)^2 - x^2 = 9/4$
Note there is no solution for $t < 3$!
[Checked. The constant is written "$k$" and "$h$" interchangeably in the hand; written $k$. Only the positive root of $\dot x$ is taken.]

Common sense tells us there must be a minimising curve: the integrand is always positive, so a curve that achieves $J[x] = 0$ will be the minimising curve.
[the integrand is non-negative, not positive]

We can show
$$x = \begin{cases} 0 & 0 \le t \le 2 \\ t - 2 & 2 \le t \le 4 \end{cases}$$
satisfies the three conditions for corner curves and that $J[x] = 0$, and is thus a minimising curve.
[Checked.]

## HW 42 — Corner curves: examples
_File `20261122_010242.jpg`. Header "Corner curves – examples"._

**Ex.** Minimise
$$\int_0^2 \dot x^2(1 - \dot x)^2 \dd t \quad \text{with } x(0) = 0,\ x(2) = 1$$
The Euler–Lagrange equation is
$$0 - \frac{\dd}{\dd t}\bigl(2\dot x(1 - \dot x)^2 - 2\dot x^2(1 - \dot x)\bigr) = 0$$
Let $g(u) = 2u(1 - u)^2 - 2u^2(1 - u)$.
Then $\frac{\dd}{\dd t} g(\dot x) = g'(\dot x)\ddot x = 0$ so either $g'(\dot x) = 0$ or $\ddot x = 0$.
Both cases (exercise) results in $\dot x = c$, so the extremals are given by $x = kt + \ell$.
Thus the extremal for the endpoints is $x = \frac12 t$.
This is not a minimising curve – let $y = x^*(t) + \eta(t)$:
$$J[y] - J[x^*] = \int_0^2 \bigl(\tfrac12 + \dot\eta\bigr)^2\bigl(\tfrac12 - \dot\eta\bigr)^2 \dd t - \int_0^2 \tfrac14 \cdot \tfrac14 \dd t = \dots = \int_0^2 -\tfrac12\dot\eta(t) + \dot\eta(t)^4 \dd t$$
[possible error: the integrand is $(\frac14 - \dot\eta^2)^2 - \frac1{16} = -\frac12\dot\eta^2 + \dot\eta^4$; the square on the first $\dot\eta$ is missing.]
which is neither $> 0$ or $< 0$ for all $\eta(t)$.
We thus look for a $D_1$ curve that satisfies the corner conditions and the E–L equation between corners.
Thus $\dot x = c$, so every segment of the curve is linear.
For the corner conditions: $\dfrac{\partial f}{\partial \dot x}$, $f - \dot x\dfrac{\partial f}{\partial \dot x}$ cont. at corner.

i.e. if $p_1, p_2$ are slopes on either side of a corner then
$$g(\dot x) := \dot x(1 - \dot x)(1 - 2\dot x) \quad \text{and} \quad h(\dot x) := \dot x^2(1 - \dot x)(3\dot x - 1)$$
$$\Rightarrow g(p_1) = g(p_2) \quad \text{and} \quad h(p_1) = h(p_2).$$
The only values that satisfy both are either:
$$p_1 = 0,\ p_2 = 1 \quad \text{or} \quad p_1 = 1,\ p_2 = 0.$$
[Checked: $g = \frac12 f_{\dot x}$ and $h = f - \dot x f_{\dot x}$. The name $g$ is reused (first for $f_{\dot x}$, then for half of it). "The only values" excludes the trivial $p_1 = p_2$.]

## HW 43 — Corner curves: examples (cont.)
_File `20261122_010245.jpg`. Header "Corner curves – examples". Lower half blank._

**Ex.** Both of these curves are suitable minimising curves as $J = 0$. We graph the curves below:

*Figure (non-unique minimising corner curves from $(0,0)$ to $(2,1)$).* Axes: vertical $x$ (arrow up) at the left, horizontal $t$ (arrow right) at the bottom; the point labelled $(0, 0)$ is drawn as a small open circle a little above and to the right of the axes' corner (not to scale), and $(2, 1)$ as an open circle at the upper right. Three paths join them, each made of horizontal pieces (slope 0) and diagonal pieces (slope 1):
- dashed, "flat then up": horizontal from $(0,0)$ to $(1,0)$, then diagonal to $(2,1)$;
- dashed, "up then flat": diagonal from $(0,0)$ to $(1,1)$, then horizontal to $(2,1)$;
- dotted staircase between them: a short horizontal piece, a diagonal, a horizontal piece at about one-third height, a diagonal, a horizontal piece at about two-thirds height, and a final diagonal into $(2,1)$.
The two dashed paths form a parallelogram; the dotted staircase lies inside it.

In fact, any such combination of lines is a minimising curve as long as the endpoints are satisfied.

Note that therefore the minimising curve is not unique.

## HW 44 — Isoperimetric problems
_File `20261122_010252.jpg`. Header "Isoperimetric problems"._

**N.** We wish to solve the following problem: minimise
$$J[x] = \int_{t_0}^{t_1} f(t, x, \dot x) \dd t$$
with $x(t_0) = x_0$, $x(t_1) = x_1$, subject to the constraint
$$I[x] = \int_{t_0}^{t_1} g(t, x, \dot x) \dd t = c$$
[the "$[x]$" of $I[x]$ is written above the $I$]
This problem (and the solution) is symbollically the same as the Lagrange multiplier method.

**Th.** For $x = x^*(t)$ to be a solution to the constrained problem, it is necessary that $x^*$ is an extremal of
$$J[x] + \lambda I[x] = \int_{t_0}^{t_1}\bigl\{f(t, x, \dot x) + \lambda g(t, x, \dot x)\bigr\} \dd t$$
for some constant $\lambda$.
[Not proved in the notes.]

**Rem.** The Euler–Lagrange equation on the Lagrangian provides a DE and three constants. ["constants" is written above the struck-out word "constraints"] Two constants are found from the endpoints, while the constraint gives the final extra constant.

**Rem.** The name 'isoperimetric' is given to such a problem for historical reasons – the first of such a problem to be considered was to find the curve that maximises an enclosed area given a fixed length (i.e. perimeter).

## HW 45 — Isoperimetric problems: example
_File `20261122_010255.jpg`. Header "Isoperimetric [blacked-out word] problems – example". Lower third blank._

**Ex.** Minimise
$$J[x] = \int_0^1 \dot x^2 \dd t, \quad \text{where } x(0) = 2,\ x(1) = 4$$
subject to $\int_0^1 x \dd t = 1$.

The Lagrangian $J + \lambda I$ is given by
$$\int_0^1 \dot x^2 + \lambda x \dd t$$
By the Euler–Lagrange equation:
$$\lambda - \frac{\dd}{\dd t}(2\dot x) = 0$$
which implies $\ddot x = \lambda/2$, implying $x = \frac{\lambda}{4}t^2 + kt + \ell$.
From the endpoint conditions:
$$\ell = 2, \quad k = 2 - \lambda/4$$
$$\Rightarrow x = \tfrac{\lambda}{4}t^2 + (2 - \lambda/4)t + 2$$
Finally, substituting into the constraint:
$$\Rightarrow \lambda = 48 \Rightarrow x = 12t^2 - 10t + 2$$
[Checked.]

## HW 46 — Isoperimetric problems: example (maximum area under a curve of given length)
_File `20261122_010303.jpg`. Header "Isoperimetric problems – example"._

**Ex.** Consider the problem of finding, among the set of curves of length $\pi$ joining $(0, 0)$ to $(2, 0)$, the curve which encloses the maximum area between itself and the $t$-axis.
In other words, maximise
$$J[x] = \int_0^2 x \dd t \quad \text{where } x(0) = 0,\ x(2) = 0$$
given
$$I[x] = \int_0^2 (1 + \dot x^2)^{1/2} \dd t = \pi.$$

We first find the extremals of the Lagrangian.
$$x + \lambda(1 + \dot x^2)^{1/2} - \frac{\lambda\dot x^2}{(1 + \dot x^2)^{1/2}} = k$$
[i.e. the second form (Beltrami identity) applied to $x + \lambda(1 + \dot x^2)^{1/2}$; not said in the notes]
We now use a parametric substitution $\dot x = \tan\theta$.
This expression simplifies to $x + \lambda\cos\theta = k$.
Differentiate and equate with $\dot x = \tan\theta$ to obtain $\theta$ i.t.o. $t$:
$$\begin{aligned} \dot x - \lambda\sin\theta \times \dot\theta &= 0 \\ \Rightarrow \tan\theta &= \lambda\sin\theta\,\dot\theta \\ \Rightarrow \lambda\dot\theta &= \sec\theta \end{aligned} \qquad \text{→ The solution to this ODE is } \lambda\sin\theta = t + c.$$
Thus we have the following system:
$$\lambda\sin\theta = t + c, \qquad x + \lambda\cos\theta = k$$
which is the parametric form of a circle.

If $\theta_0, \theta_1$ are the values of $\theta$ at $(0, 0)$ and $(2, 0)$, the end condition give:
$$\begin{aligned} k &= \lambda\cos\theta_0 = \lambda\cos\theta_1 && (\ast 1) \\ c &= \lambda\sin\theta_1 - 2 = \lambda\sin\theta_0 && (\ast 2) \end{aligned}$$
The integration constraint: [with the note "from $\dd t = \lambda\cos\theta \dd\theta$" and two strokes pointing to the change of variable]
$$\int_0^2 (1 + \dot x^2)^{1/2} \dd t = \int_0^2 \sec\theta \dd t \Rightarrow \int_{\theta_0}^{\theta_1} \lambda \dd\theta = \pi$$
$$\Rightarrow \lambda(\theta_1 - \theta_0) = \pi \qquad (\ast 3)$$
[Checked.]

## HW 47 — Isoperimetric problems: example (cont.)
_File `20261122_010307.jpg`. Header "Isoperimetric problems – example". Lower 40% blank._

**Ex.** (continued)
From \*1, $\theta_0 = \pm\theta_1$ (as $\cos\theta$ is even)
From \*3, $\theta_0 = -\theta_1$
Thus $\theta_1 = \pi/2\lambda$.
From \*2, we have $1/\lambda = \sin(\pi/2\lambda)$.
This equation has two solutions $\lambda = 1$, $\lambda = -1$.

If $\lambda = 1$: solution in 4th quadrant
If $\lambda = -1$: solution in 1st quadrant.
The max. area is given by $\lambda = -1$, for which
$$\theta_1 = -\theta_0 = -\pi/2, \quad k = 0, \quad c = -1.$$

This gives the top half of the circle centered at $(1, 0)$, through $(0, 0)$ and $(2, 0)$.
[Checked: $x = \cos\theta$, $t - 1 = -\sin\theta$, so $(t - 1)^2 + x^2 = 1$. "Two solutions" means the two used here; the notes do not discuss other roots of $1/\lambda = \sin(\pi/2\lambda)$.]

## HW 48 — Sufficiency conditions: comparison with calculus in $\R^2$
_File `20261122_010312.jpg`. Header "Sufficiency conditions". The page is laid out in two columns, left "calculus in $\R^2$", right "calculus of variations"._

**N.** Compare the conditions required for minimisation for calculus in $\R^2$ compared to calculus of variations.

| | Calculus in $\R^2$ | Calculus of variations |
|---|---|---|
| <u>Necessary:</u> | $\nabla f(x^*) = 0$ where $x^* \in \R^2$ (critical point) | $\dfrac{\partial f}{\partial x} - \dfrac{\dd}{\dd t}\Bigl(\dfrac{\partial f}{\partial \dot x}\Bigr) = 0$ where $x^* \in C^1$ (extremal) |
| <u>Sufficient:</u> | Let $y = x^* + \varepsilon\eta$ where $x^*, \eta, y \in \R^2$ | Let $y = x^* + \varepsilon\eta$ where $x^*, \eta, y \in C^1$ |
| | $0 \le f(y) - f(x^*) = \varepsilon V_1 + \varepsilon^2 V_2 + \cdots$ | $0 \le J[y] - J[x^*] = \varepsilon V_1 + \varepsilon^2 V_2$ |
| | where $V_1 = \nabla f(x^*)\eta$, $V_2 = \frac12\eta\T H\eta$ | where $V_1 = \int_{t_0}^{t_1} \eta\Bigl(\dfrac{\partial f}{\partial x} - \dfrac{\dd}{\dd t}\Bigl(\dfrac{\partial f}{\partial \dot x}\Bigr)\Bigr) \dd t$, $V_2 = \frac12\int_{t_0}^{t_1} \eta^2 f_{xx} + 2\dot\eta\eta f_{x\dot x} + \dot\eta^2 f_{\dot x\dot x} \dd t$ |
| | Then $V_1 = 0$, $V_2 > 0$ <u>IS</u> sufficient for a minimum. | Then $V_1 = 0$, $V_2 > 0$ <u>IS NOT</u> sufficient for a minimum. |

[In both columns the "$>$" in "$V_2 > 0$" is written above a blacked-out symbol (probably an overwritten "$\ge$"). $V_1 = \nabla f(x^*)\eta$ is $\nabla f(x^*)\T\eta$. The right column omits "$+ \cdots$".]

We can see that while the vanishing of the first variation $V_1$ are necessary conditions for both problems, showing $V_2 > 0$ is not sufficient for finding minima. [the "$>$" again above a blacked-out symbol]
This can be shown in the following example.

## HW 49 — Sufficiency conditions: example where $V_2 > 0$ but the extremal is not a minimiser
_File `20261122_010318.jpg`. Header "Sufficiency conditions"._

**Ex.** Minimise
$$J[x] = \int_0^1 \frac{1}{\dot x} \dd t \quad \text{where } x(0) = 0,\ x(1) = 1$$
We can show the extremal is $x^* = t$, $J[x^*] = 1$.
Consider $y = x^* + \varepsilon\eta = t + \varepsilon\eta$, with $\eta(0) = \eta(1) = 0$.
$$\begin{aligned} \Delta J = J[y] - J[t] &= \int_0^1 \frac{1}{1 + \varepsilon\dot\eta} - 1 \dd t \\ &= \int_0^1 (-\varepsilon\dot\eta + \varepsilon^2\dot\eta^2 - \varepsilon^3\dot\eta^3 + \cdots) \dd t && \Bigl\}\ \tfrac{1}{1+x} = 1 - x + x^2 - x^3 + \cdots \\ &= -\varepsilon\cancel{\int_0^1 \dot\eta \dd t} + \varepsilon^2\int_0^1 \dot\eta^2 \dd t - O(\varepsilon^3) > 0 \end{aligned}$$
[the first integral is struck through with an arrow to "0"]
Thus the second variation is positive. However, consider
$$y = \begin{cases} 3t & 0 \le t \le 1/2 \\ -t + 2 & 1/2 \le t \le 1 \end{cases}$$
which has $J[y] = -1/3$.
(Rem: note this is not a $D_1$ min. curve, as corner conditions not satisfied. We can create many curves with $J < 1$.)

Therefore, although $V_2 > 0$, $x = t$ is not a minimising curve.
[Checked: $J[y] = \frac16 - \frac12 = -\frac13$.]

**N.** We must therefore adopt a subtler approach, using the concepts of the Hilbert integral and a field of extremals.

## HW 50 — Fields of extremals
_File `20261122_010325.jpg`. Header "Fields of extremals"._

**N.** In order to find sufficient conditions for a minimum we must return to the inequality $\Delta J = J[y] - J[x^*] > 0$ for all curves $y$ that satisfy the end conditions.
In previous examples we showed by direct calculation of $\Delta J$ that $\Delta J > 0$. However, in general, $\Delta J$ is the integral of some complicated function involving both $\eta$ and $\dot\eta$, we will not be able to make a general statement about the sign. ["and" written above the line]
What we must do is express $\Delta J$ in some new form where it is easier to ascertain. To do this we must examine the below.

**Def.** *Field of extremals*
Recall that the general solution of the Euler–Lagrange equation relies on two end conditions; the solution is a two-parameter family of curves.
(e.g. general extremal: $x = kt + \ell$ where $k = 1$, $\ell = 0$, $x$ goes through $(0, 0)$, $(1, 1)$)
Consider a one-parameter family of curves. This family gives a simple cover to the plane; through each point passes a unique member of the family.
(e.g. family $x = t + \ell$ OR $x = kt$)
We choose the family which is most convenient or well-behaved.
[$x = kt$ does not give a simple cover at $t = 0$ (every member passes through the origin); the notes do not comment.]

**Def.** As only one member of the family passes through each point, there is a unique value for the slope $p(t, x)$ at each point $(t, x)$.
Therefore, for a field of extremals there is a slope function $p(t, x)$ that satisfies
$$\frac{\partial f(t, x, p)}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial p}(t, x, p)\Bigr) = 0 \qquad \text{at each } (t, x).$$

## HW 51 — Fields of extremals: examples
_File `20261122_010329.jpg`. Header "Fields of extremals"._

**Ex.** Find a field of extremals for
$$J[x] = \int_1^2 \dot x^2 t^3 \dd t \quad \text{where } x(1) = 0,\ x(2) = 3$$
The general solution is $x = k/t^2 + \ell$, and the extremal satisfying the end conditions is $x = -4/t^2 + 4$.
A one-parameter family of extremals is thus $x = \ell - 4/t^2$.
For $t > 0$ this gives a simple cover of the half plane, and therefore is an extremal field with slope function
$$p(t, x) = 8/t^3.$$
Now $f(t, x, p) = p^2 t^3$, $\partial f/\partial x = 0$, $\partial f/\partial p = 2pt^3$. Hence,
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial p}\Bigr) = 0 - \frac{\dd}{\dd t}(2pt^3) = -\frac{\dd}{\dd t}(16) = 0$$
[Checked.]

**Ex.** Find a field of extremals for
$$J[x] = \int_0^1 \dot x^{2m} \dd x \quad \text{where } m \in \N,\ x(0) = 1,\ x(1) = 2$$
[$\dd x$ should be $\dd t$]
The Euler–Lagrange equation is $\frac{\dd}{\dd t}(2m\dot x^{2m-1}) = 0$, implying that $\dot x = c$, implying that $x^* = kt + \ell$.
By the initial conditions we have $\ell = 1$, $k = 1$.
Let $p(t, x) = \dot x_\ell(t) = 1$ be the slope of the extremal field $x = t + \ell$. Then
$$f(t, x, p) = p^{2m} = 1, \qquad \frac{\partial f}{\partial p} = 2mp^{2m-1} = 2m$$
which obviously satisfies the equation
$$\frac{\partial f}{\partial x} - \frac{\dd}{\dd t}\Bigl(\frac{\partial f}{\partial p}\Bigr) = 0 \qquad \forall (t, x) \in \R.$$
[$(t, x) \in \R^2$ is meant]

## HW 52 — Hilbert's invariant integral; Weierstrass excess function
_File `20261122_010336.jpg`. Header "Hilbert's invariant integral"._

**Def.** Suppose we have an extremal $x^*(t)$ which we denote $C^*$. Let $x(t)$, or $C$, be any other curve joining the endpoints and covered by the field. The only restriction on $C$ is that the following integral is defined along it:
$$K[x] = \int_{t_0}^{t_1}\Bigl(f(t, x, p) + (\dot x - p)\frac{\partial f}{\partial p}(t, x, p)\Bigr) \dd t$$
Note that if $C = C^*$, $\dot x = p$ and $K[x^*] = J[x^*]$.
Let
$$u(t, x) = f(t, x, p) - p\frac{\partial f}{\partial p}(t, x, p), \qquad v(t, x) = \frac{\partial f}{\partial p}(t, x, p) \qquad \Bigr\}\ \text{note $p$ depends on $t, x$.}$$
Then
$$K[x] = \int_C u \dd t + v \dd x \qquad \Bigr\}\ \text{line integral, independent of $C$ as } \partial u/\partial x - \partial v/\partial t = 0$$
[the path-independence ($\partial u/\partial x = \partial v/\partial t$) is asserted, not shown]
We can therefore express $\Delta J$ by
$$\begin{aligned} \Delta J &= J[x] - J[x^*] \\ &= J[x] - K[x^*] && (J[x^*] = K[x^*] \text{ at } x^*) \\ &= J[x] - K[x] && \text{(path-independence)} \\ &= \int_{t_0}^{t_1} \underbrace{\Bigl(f(t, x, \dot x) - f(t, x, p) - (\dot x - p)\frac{\partial f}{\partial p}(t, x, p)\Bigr)}_{E(t, x, \dot x, p),\ \text{Weierstrass excess function}} \dd t \end{aligned}$$

**Def.** We therefore have a sufficient condition for a strong minimum of $J[x]$, called the Weierstrass conditions.

## HW 53 — Hilbert's invariant integral (Weierstrass conditions); example: shortest distance
_File `20261122_010342.jpg`. Header "Hilbert's invariant integral (Weierstrass conditions)"._

**Def.** *Weierstrass conditions (strong local minimum)*
For the extremal $C^*$ to give a strong local minimum to $J[x]$, it is sufficient that
(1) $C^*$ is a member of a field of extremals
(2) $E(t, x, \dot x, p) \ge 0$ for all $(t, x)$ 'close' to $C^*$, and any arbitrary value of $\dot x$.

**Def.** *Weierstrass conditions (global minimum)*
For the extremal $C^*$ to give a global [written above a blacked-out word] minimum to $J[x]$, it is sufficient that
(1) $C^*$ is a member of a field of extremals where the field covers $\R^2$ (the whole $t$-$x$ plane)
(2) $E(t, x, \dot x, p) \ge 0$ for all $t, x \in \R^2$.

**Ex.** Show the shortest distance between two points is a line.
i.e. minimise
$$\int_0^1 (1 + \dot x^2)^{1/2} \dd t \qquad x(0) = 0,\ x(1) = 1$$
The solution/extremal is $x = kt + \ell$, $k = 1$, $\ell = 0 \Rightarrow x = t$.
First, embed $x = t$ in a field of extremals.
(We can choose $x = t + \ell$, $p(t, x) = 1$ or $x = kt$, $p(t, x) = x/t$)
Now
$$\begin{aligned} E(t, x, \dot x, p) &= f(t, x, \dot x) - f(t, x, p) - (\dot x - p)\frac{\partial f}{\partial p}(t, x, p) \\ &= (1 + \dot x^2)^{1/2} - (1 + p^2)^{1/2} - p(\dot x - p)(1 + p^2)^{-1/2} \\ &= (1 + \dot x^2)^{1/2} - (1 + p\dot x)(1 + p^2)^{-1/2} \end{aligned}$$
Now consider some $(t, x)$ in the region covered by a field. Note $p(t, x)$ has a numerical value. We must show $E \ge 0$ for all $\dot x$ at such a point $(t, x)$.
↳ If $(1 + p\dot x) \le 0$, then $E > 0$
↳ If $(1 + p\dot x) > 0$, let $G = (1 + \dot x^2)^{1/2} + (1 + p\dot x)(1 + p^2)^{-1/2}$
$$\Rightarrow EG = \frac{(\dot x - p)^2}{1 + p^2} \ge 0 \Rightarrow E \ge 0$$
Thus $x^* = t$ is a minimising curve.
[Checked. $G > 0$ is used but not stated.]

