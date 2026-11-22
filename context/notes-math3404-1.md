# MATH3404 Optimisation Theory: transcription, part 1 of 3 (HW 01–19)

_Transcription phase. Nothing here is book text yet. No dates are recorded. The semester in which the course was taken is not given in the material, so it is not recorded here._

## Sources (all three parts)
| Code | Source | Role | Where |
|---|---|---|---|
| **HW nn** | 85 photos of the handwritten notebook, numbered in shooting order (file name under each heading). Each photo is **one** notebook page, shot in portrait (the files carry an EXIF rotation; viewed upright they are single pages). HW 01 is a contents page. | **Main source** | Parts 1–3, in full |
| Textbook | The textbook the notes are based on. | Supplement (context, gap-filling later) | Not yet supplied; to be added later |

There are no typed notes or slides in this upload, so there is no typed-notes index.

**Parts.** 1: HW 01–19 (contents; optimisation in $\R$ and $\R^n$; Lagrange multipliers; bordered Hessian). 2: HW 20–53 (calculus of variations: Euler–Lagrange, brachistochrone, fixed and variable endpoints, transversality, corner curves, isoperimetric problems, sufficiency, fields of extremals, Hilbert's invariant integral, Weierstrass conditions). 3: HW 54–85 (optimal control: examples, the general problem, the Pontryagin maximum principle, time-optimal control of linear systems (real and complex eigenvalues), target curves, cost depending on the final state).

**Page count:** 85 photos = 85 notebook pages, all distinct, none blank (several have a blank lower part).

## Legibility check (all 85 photos, in order)
Every photo was viewed upright at reduced resolution and every doubtful spot was re-checked on a full-resolution crop. **No retakes are needed.** Sharpness and exposure are adequate on every page and no page is cut off. Almost every photo has a broad diagonal shadow from the phone across the page; the ink reads through it everywhere.
- **HW 21** (`20261122_010045.jpg`) is slightly soft over the whole page; every word was confirmed on a full-resolution crop. A retake is optional, not needed.
- Content that cannot be read is in the notebook itself, so a retake won't help: blacked-out (struck-out) words or symbols on many pages, noted where they occur. None of them hides content that the surrounding text needs.
- Ambiguities in the hand (not the photo), resolved from context where they occur: the letters **m and n** look the same throughout (sums and indices in HW 04 and HW 10–15 are read from context); the dot over $x$ in $\partial f/\partial\dot x$ is sometimes missing (HW 24–25, 38), marked "[dot missing]"; $\varepsilon$ vs $c$ (HW 31); "$(-3, 2)$" and "$(3,-2)$" (HW 68); the first symbol of a numerator (HW 35); the last factor of a product (HW 18).

## Conventions
Wording, structure and labels follow the notes: **N.** (= note, the notes' label for running exposition), **Def.**, **Th.** (with the notes' own numbers, e.g. **Th. (2.2)**), **Lem.**/**L.**, **Cor.**, **P.** (= proof), **Ex.**, **Rem.** Maths uses `notation.tex` macros (`\R`, `\N`, `\Z`, `\dd`, `\T`, `\vect`, `\mat`, `\norm`, `\abs`, `\set`, `\argmin`). Vectors underlined in the notes are written `\vect{}` where the notes underline them; the notes mostly leave $a$, $h$, $x$ un-underlined in the $\R^n$ chapter and this is kept. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic and algebra were re-checked where it says "Checked"); `[illegible]` would mark unreadable text (none was needed). "↳" is the notes' own arrow for sub-points. Figures are described in enough detail to redraw in TikZ (axes, labels, points, arrows, dashed/solid). `\cancel{}` marks text struck through in the notes where the strike-through carries meaning.

---

## HW 01 — Contents page
_File `20261122_005619.jpg`. Single page. A broad diagonal shadow crosses the page; everything reads through it._

**MATH3404**

W1,2 : Optimisation in $\R^n$ (Q1)
↳ Classical optimisation in $\R^n$
↳ Optimisation in $\R^n$ with constraints (Lagrange multipliers)

&nbsp;&nbsp;&nbsp;: Calculus of variations
↳ Euler–Lagrange equation
↳ Fixed-endpoint problem
↳ Variable-endpoint problem (transversality)
↳ Corner curves
↳ Isoperimetric problem
↳ Sufficient conditions (fields of extremals, Hilbert's invariant integral, Weierstrass condition)

W8 : Optimal control
↳ Pontryagin maximum principle
↳ Unconstrained fixed endpoint problem
↳ Time-optimal control of linear systems
↳ Uncons. variable endpoint problem
↳ Cost-dependent problem

["W1,2", "W8" are week numbers; the calculus-of-variations line has a colon but no week number. "(Q1)" presumably refers to an assignment or exam question; it is not explained.]

## HW 02 — Introduction: optimisation in $\R$
_File `20261122_005628.jpg`. Header "Introduction: optimisation in $\R$"._

**N.** We wish to solve the following problem:
Let the function $f$ be defined on $I \subseteq \R$. Find the points of $I$ at which (by the EVT) $f$ acheives its maximum and minimum values.

**Def.** *Global minimum*
Let $\bar x \in I$. If $\forall x \in I$, $f(\bar x) \le f(x)$, with equality at $x = \bar x$, then $f$ attains a global minimum at $\bar x$.

**Rem.** We have a similar definition for global maxima.

**Def.** [a blacked-out word] *Local minimum*
Let $\bar x \in I$. If $\forall x \in I \subseteq J$, $f(\bar x) \le f(x)$, with equality at $x = \bar x$, where $I \subseteq J$ is the $\varepsilon$-nbhd $\abs{x - \bar x} < \varepsilon$, then $f$ attains a local minimum at $\bar x$.
[possible error: the inclusion is reversed; the neighbourhood $J = \set{x : \abs{x - \bar x} < \varepsilon}$ should satisfy $J \subseteq I$ (or the condition should be $\forall x \in I \cap J$).]

**Th. (1.1)** Let $f\colon I \to \R$ be $C^2$ in some $\varepsilon$-nbhd of $\bar x \in I$. If $f$ has a local minimum at $\bar x$, then $f'(\bar x) = 0$.

**P.** By def. of local min. $\exists N \subseteq I$:
$$f(\bar x + h) - f(\bar x) \ge 0 \qquad \forall (\bar x + h) \in N$$
with equality at $h = 0$.
Using a Taylor expansion and the Lagrange remainder:
$$f(\bar x + h) = f(\bar x) + h f'(\bar x) + \frac{h^2}{2} f''(\bar x + \theta h) \qquad 0 < \theta < 1$$
which implies
$$h f'(\bar x) + \frac{h^2}{2} f''(\bar x + \theta h) \ge 0$$
where $f''(\bar x + \theta h)$ is bounded.

## HW 03 — Introduction: optimisation in $\R$ (cont.)
_File `20261122_005631.jpg`. Lower half of the page blank._

**P.** [continued] We split into cases. If $h > 0$:
$$f'(\bar x) + \frac{h}{2} f''(\bar x + \theta h) \ge 0$$
As $h \to 0$, we obtain $f'(\bar x) \ge 0$.
If $h < 0$, a similar argument obtains $f'(\bar x) \le 0$.

Hence $f'(\bar x) = 0$ is a necessary condition for a local minimum. $\square$

**Th. (1.2)** Let $f\colon I \to \R$ be $C^1$ in some $\varepsilon$-nbhd of $\bar x \in I$. If $f'(\bar x) = 0$, and $f'(x + h) < 0$ for $h < 0$, and $f'(x + h) > 0$ for $h > 0$, then $f$ attains a local minimum at $\bar x$.
[the notes write $f'(x+h)$; $f'(\bar x + h)$ (for small $\abs h$) is meant]

**P.** Reverse direction of previous theorem – use MVT. $\square$

**Ex.** Let $f(x) = x^2$ be defined on $(-1, 1)$.
As $f'(x) = 2x$ and $\bar x = 0$ satisfies all conditions in the previous theorem, $f$ has a local minimum at $\bar x = 0$.

## HW 04 — Optimisation in $\R$ (cont.): higher-order test; critical points
_File `20261122_005637.jpg`._

**Th. (1.3)** Let $f$ be $C^m$ in some $\varepsilon$-nbhd of $\bar x \in I$. If
$$f'(\bar x) = f''(\bar x) = \dots = f^{(m-1)}(\bar x) = 0, \qquad f^{(m)}(\bar x) \ne 0$$
then $f(\bar x)$ has a local minimum at $\bar x$, provided $m$ is even and $f^{(m)}(\bar x) > 0$.

**P.** The Taylor expansion of $f$ yields
$$f(\bar x + h) = f(\bar x) + h f'(\bar x) + \dots + \frac{h^{m-1}}{(m-1)!} f^{(m-1)}(x) + \frac{h^m}{m!} f^{(m)}(\bar x + \theta h) \qquad 0 < \theta < 1$$
[possible error: $f^{(m-1)}(x)$ should be $f^{(m-1)}(\bar x)$. The hand's "m" and "n" look alike in this proof; read as $m$ throughout.]
This implies
$$f(\bar x + h) - f(\bar x) = \frac{h^m}{m!} f^{(m)}(\bar x + \theta h)$$
As $f^{(m)}$ is continuous near $\bar x$, and $f^{(m)}(\bar x) > 0$, then for small $h$ $f^{(m)}(\bar x + \theta h) > 0$.
Thus $f(\bar x + h) - f(\bar x) > 0$ for small $h$, so $f$ has a local minimum at $\bar x$. $\square$
[the proof does not say where "$m$ even" is used (it makes $h^m > 0$ for $h \ne 0$); not an error, just unstated]

**N.** Our theory (established previously in other undergrad. courses) considers cases where $f'(\bar x)$ exists. However, we must extend our theory to cases where $f$ is not differentiable.

**Def.** *Critical point*
A point where either:
i) $f'(\bar x) = 0$
ii) $f'(x)$ does not exist.

## HW 05 — Critical points in $\R$
_File `20261122_005641.jpg`. Header "Critical points in $\R$"._

**Th. (1.4)** Let $f\colon I \to \R$ be differentiable on $I \setminus \set{\bar x}$.
Consider a deleted-nbhd of $\bar x$. Then $f$ has a local minimum at $\bar x$, provided that
i) $f'(x) < 0$ for $\bar x - \varepsilon < x < \bar x$
ii) $f'(x) > 0$ for $\bar x < x < \bar x - \varepsilon$.
[possible error: (ii) should read $\bar x < x < \bar x + \varepsilon$. Continuity of $f$ at $\bar x$ is also needed but not stated.]

**Rem.** The nature of the interval $I$ is important. If $f$ is defined on a closed interval, the extrema may occur on either endpoint.

**Rem.** We assume that $f$ can be broken into piecewise continuous functions. The isolated points of discontinuity must also be examined.

[No label.] Let $f$ and $f'$ be continuous on $I$ except at a finite number of points. ["on" written above a blacked-out word] The procedure to find a global minimum is:
1) Find any stationary point ($f'(x) = 0$) and use Th. 1.2 to find minima
2) Examine $f$ near every discontinuity of $f$ or $f'$, and compare to find potential minima
3) If $I$ is closed, consider endpoints
4) Compare all points and take minimum of set

## HW 06 — Optimisation in $\R^n$: multivariable Taylor series
_File `20261122_005647.jpg`. Header "[blacked out] Optimisation in $\R^n$"._

**N.** We wish to solve the following problem:
Let the function $f$ be defined on some region $K \subseteq \R^n$. Find the points of $K$ at which $f(x)$ attains its maximum and minimum values.

**Def.** *Local and global minimum*
Defined similarly to the single-variable case.

**Def.** *Multivariable Taylor series*
Let $f$ have continuous first-order and second-order partial derivatives and bounded third-order derivatives.
Recall the gradient (grad, $\nabla$) of $f$:
$$\nabla f(a) = \left(\frac{\partial f}{\partial x_1}(a), \dots, \frac{\partial f}{\partial x_n}(a)\right)\T$$
Recall the Hessian ($H_f$) of $f$:
$$H_f(a) = \left(\frac{\partial^2 f}{\partial x_i \partial x_j}\right)_{n \times n}$$
Let $h \in \R^n$, so $h\T = (h_1, \dots, h_n)$.

**\*** [an asterisk in the margin] Then, the multivariate Taylor series is given by:
$$f(a + \varepsilon h) = f(a) + \varepsilon h\T \nabla f(a) + \frac{\varepsilon^2}{2} h\T H_f(a) h$$
for all $h \in \R^n$, small $\varepsilon$, and error $O(\varepsilon^3)$. [a small blacked-out mark inside the $O(\,)$]

**Rem.** Compare to multivariable Taylor series in MATH2001:
$$f(\vect x) = f(\vect x_0) + \bigl(\nabla f(\vect x_0)\bigr)\T(\vect x - \vect x_0) + \tfrac12 (\vect x - \vect x_0)\T H_f(\vect x_0)(\vect x - \vect x_0) + \cdots$$
[In this page the $\nabla$ is underlined (a vector operator) and in the Remark $\vect x$, $\vect x_0$ are underlined; elsewhere $a$, $h$ are not underlined. Kept as in the notes.]

## HW 07 — Optimisation in $\R^n$: first- and second-order conditions
_File `20261122_005650.jpg`._

**Th. (2.1)** Let $f\colon K \subseteq \R^n \to \R$ have continuous second-order derivatives, and bounded third-order derivatives. Let $a$ be a local min. Then $\nabla f(a) = \vect 0$.

**P.** Similar to single-variable case. $\square$

**Ex.** Consider $f(x_1, x_2) = x_1^2 + x_2^2$. The local minimum (on $\R^2$) is $(0, 0)$, so $\nabla f(0, 0) = \vect 0$.

**Th. (2.2)** Let $f\colon \Omega \subseteq \R^n \to \R$ have continuous second-order derivatives. A sufficient condition for $f$ to have a local minimum at $a \in \Omega$ is that
$$\nabla f(a) = \vect 0 \quad \text{and} \quad h\T H_f(a) h > 0 \quad \forall h \in \R^n \setminus \set{0}$$

**P.** We use the Taylor expansion on $f$:
$$\begin{aligned} f(a + \varepsilon h) - f(a) &= \frac{\varepsilon^2}{2} h\T H_f(a) h + O(\varepsilon^3 \abs{h}^3) \\ &\ge \min\set{\lambda_i} \frac{\varepsilon^2}{2} \abs{h}^2 + O(\varepsilon^3 \abs{h}^3) \\ &> 0 \end{aligned}$$
[an arrow from $\min\set{\lambda_i}$ to the note:] eigenvalue of $H_f(a) > 0$
given that
i) $a + \varepsilon h \in B_\varepsilon(a)$
ii) $\forall h \in \R^n$: $\abs h = 1$ **\*** [asterisk in the notes]
iii) $\abs{\varepsilon} < \varepsilon_0$ for small $\varepsilon_0$. $\square$

**Lem. (2.3)** The quadratic form $h\T H_f h$ is positive iff all of its eigenvalues are positive (and real).
["its eigenvalues" = the eigenvalues of $H_f$]

**Cor. (2.4)** Let $f$ be defined as in (2.2). A sufficient condition for $f$ to have a local max. is that
$$\nabla f(a) = \vect 0 \quad \text{and} \quad h\T H_f(a) h < 0 \quad \forall h \in \R^n$$
[possible error: $h \ne \vect 0$ is needed, as in Th. 2.2.]

## HW 08 — Optimisation in $\R^n$: exercises; proof of the eigenvalue bound
_File `20261122_005943.jpg`. Header "Optimisation in $\R^n$ – exercises"._

**Ex.** Minimise $f(x_1, x_2) = x_1^2 - x_2^2$ on $\R^2$.
$$\nabla f(x_1, x_2) = (2x_1, -2x_2)\T$$
↳ $\nabla f(0, 0) = \vect 0$
$$H_f(x_1, x_2) = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$$
↳ $\det H_f = -4$ and $\dfrac{\partial^2 f}{\partial x_1^2} = 2$, so quadratic form is not positive or negative.
Thus $(0, 0)$ is not maximum or minimum.

**Ex.** Minimise $f(x_1, x_2) = (x_1^2 - 4)^2 + x_2^2$.
[no working]

**Ex.** Find the extrema of $f(x_1, x_2) = x_1^3 + x_2^3 + 3x_1^2 - 3x_2^2 - 8$.
[no working]

**Proof of $h\T H_f(a) h \ge \min\set{\lambda_i}$**

**P.** $H_f$ is real symmetric $\Rightarrow$ $H_f$ is ortho. diagonalisable
↳ $\exists$ ortho. $Q \in \R^{n \times n}$: $H_f = Q A Q\T$, where $A$ is diagonal.

Let $h \in \R^n$: $\norm{h} = 1$. Let $y = Q\T h$. As $Q$ is orthogonal, $Q\T$ is a rotation, and thus $\norm{y} = 1$.
[possible error (minor): an orthogonal matrix need not be a rotation (it may be a reflection); what is used is that it preserves length.]
Now,
$$h\T H_f h = h\T Q A Q\T h = y\T A y = \sum_i \lambda_i y_i^2 \ \ \text{(as $A$ is diagonal)} \ \ge \min\set{\lambda_i} \qquad \square$$
[$A$ here is the diagonal matrix of eigenvalues $\lambda_i$; the last step uses $\sum_i y_i^2 = 1$, not stated.]

## HW 09 — Proof of multivariable Taylor series
_File `20261122_005947.jpg`. Header "Proof of multivariable Taylor series". Lower quarter blank._

**P.** Let $h \in \Omega$: $\abs h = 1$, $x = a + \varepsilon h$ where $\abs\varepsilon < \varepsilon_0$ small.
Define $g(\varepsilon)$ by:
$$g(\varepsilon) = f(a + \varepsilon h) = f(a_1 + \varepsilon h_1, \dots, a_n \varepsilon h_n) \qquad \forall \varepsilon \in \R^n.$$
[possible error: the last argument should be $a_n + \varepsilon h_n$, and $\varepsilon \in \R$ (not $\R^n$). Also $h \in \R^n$ rather than $h \in \Omega$.]

From single variable Taylor series:
$$g(\varepsilon) = g(0) + g'(0)\varepsilon + \tfrac12 g''(0)\varepsilon^2 + \tfrac16 g'''(\theta\varepsilon)\varepsilon^3$$

By the chain rule:
$$\begin{aligned} g'(\varepsilon) &= \frac{\dd}{\dd\varepsilon} f(a + \varepsilon h) \\ &= \frac{\partial f}{\partial x_1}(a + \varepsilon h) \cdot \frac{\dd(a_1 + \varepsilon h_1)}{\dd\varepsilon} + \dots + \frac{\partial f}{\partial x_n}(a + \varepsilon h) \cdots \end{aligned}$$
$$g'(0) = \frac{\partial f}{\partial x_1}(a) \cdot h_1 + \dots + \frac{\partial f}{\partial x_n}(a)\, h_n = h\T \nabla f(a)$$
Similarly,
$$g''(0) = \sum_{i,j} h_i h_j \frac{\partial^2 f}{\partial x_i \partial x_j} = h\T H_f(a) h$$
Hence,
$$g(\varepsilon) = f(a + \varepsilon h) = f(a) + \varepsilon h\T \nabla f(a) + \tfrac12 \varepsilon^2 h\T H_f(a) h + O(\varepsilon^3).$$

## HW 10 — Minimisation in $\R^n$ with constraints: Lagrange multipliers
_File `20261122_005952.jpg`. Header "Minimisation in $\R^n$ (optimisation in $\R^n$) with constraints"._

**N.** We wish to solve the following problem:
Minimise $f(x)$ in $\R^n$ given that $x$ satisfies the equality constraints $g_j(x) = c_j$, where $j = 1, \dots, m < n$ and $c_1, \dots, c_m \in \R$ are known.

**Def.** *Lagrange multiplier*
Given a function to optimise and a constraint equation, the function is optimised when the contours are parallel: i.e. $\nabla f = \lambda \nabla g$. (from MATH1072)
This will be generalised in the following theorem.

**Th. (3.1)** Let $f(x)$ and $g_j(x)$, where $j = 1, \dots, m < n$, is defined on some open $\Omega \subseteq \R^n$, and have continuous second derivatives. Then if $a \in \R^n$ minimises $f$ with constraints $g_j(x)$, then there exists $m$ Lagrange multipliers $\lambda_j \in \R$ such that
$$\nabla\bigl[L(x)\bigr] = \nabla\Bigl[f + \sum_{j=1}^m \lambda_j g_j\Bigr] = 0 \quad \text{at } a.$$
[possible error (missing hypothesis): the theorem and its proof need the constraint gradients $\nabla g_j(a)$ to be linearly independent (after relabelling, the $m \times m$ matrix $(\partial g_j/\partial x_i)_{i,j \le m}$ invertible); the proof uses this when it "chooses" the $\lambda_j$ and when it solves for $h_1, \dots, h_m$ (HW 11), but it is never stated. $L$ is not defined separately.]

**P.** Consider the constraint equations $g_j(x) = c_j$.
Let $x = a + \varepsilon h$, where $\abs h = 1$ and $\varepsilon$ is small.
Using Taylor's expansion in $\varepsilon$:
$$g_j(a + \varepsilon h) = g_j(a) + \varepsilon h\T \nabla g_j(a) + \cdots = c_j$$
↳ $h\T \nabla g_j(a) = 0$ for $j = 1, \dots, m$. **\***

Similarly using Taylor's expansion for $f(a + \varepsilon h) \ge f(a)$ (as $a$ is a local minimum):
$$h\T \nabla f(a) = 0 \qquad \forall h: h\T \nabla g_j(a) = 0,\ j = 1, \dots, m.$$

**\*** i.e. $h$ is a tangent vector to $g_j$.

## HW 11 — Optimisation in $\R^n$ with constraints (proof of 3.1, cont.)
_File `20261122_010000.jpg`. Header "Optimisation in $\R^n$ with constraints (proof of ~~[struck-out word, probably "Lagrange mult."]~~)" with "3.1." written above the struck-out word. A blacked-out box to the right of the first display._

**P.** [continued] Therefore, for any choice of $\lambda_1, \dots, \lambda_m \in \R$:
$$h\T\Bigl[\nabla f(a) + \sum_{j=1}^m \lambda_j \nabla g_j(a)\Bigr] = 0.$$
Reorganising sums, this implies that at $x = a$:
$$\sum_{i=1}^m h_i\Bigl(\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i}\Bigr) + \sum_{i=m+1}^n h_i\Bigl(\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i}\Bigr) = 0.$$
for all $h$: $h\T \nabla g_j(a) = 0$, $j = 1, \dots, m$.
[a bracket-arrow in the left margin joins this line to the line "$\Leftrightarrow h\T \nabla g_j(a) = 0$" further down]

Choose $\lambda_1, \dots, \lambda_m$ such that the $m$ equations
$$\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i} = 0 \qquad \leftarrow \text{for } i = 1, \dots, m$$
are satisfied. This reduces our equation to:
$$\sum_{i=m+1}^n h_i\Bigl(\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i}\Bigr) = 0.$$
For any $(h_{m+1}, \dots, h_n) \in \R^{n-m}$, $\exists h_1, \dots, h_m$:
$$\sum_{i=1}^m h_i \frac{\partial g_j}{\partial x_i} = -\sum_{i=m+1}^n h_i \frac{\partial g_j}{\partial x_i} \ \Leftrightarrow\ h\T \nabla g_j(a) = 0 \text{ for } j = 1, \dots, m.$$
Thus as we can choose $h_{m+1}, \dots, h_n$ we have
$$\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i} = 0 \qquad \leftarrow \text{for } i = m+1, \dots, n$$
Combining our marked statements, there exists $\lambda_1, \dots, \lambda_m$ such that:
$$\frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i} = 0$$
for $i = 1, \dots, n$ at $x = a$. This implies that
$$\nabla\Bigl(f + \sum_{j=1}^m \lambda_j g_j\Bigr) = 0.$$
at a local minimum $a$. $\square$
[In this hand "m" and "n" are hard to tell apart; the upper limits are read as $m$ for sums over $j$ and as $m$ or $n$ for sums over $i$ as the argument requires. In the second display the inner $\partial g_j$ is written $\partial g_i$ in places.]

## HW 12 — Optimisation in $\R^n$ with constraints: examples
_File `20261122_010005.jpg`. Header "Optimisation in $\R^n$ with constraints – examples". Bottom fifth blank._

**Ex.** Minimise $f(x) = 1 - x_1^2 - x_2^2$ subject to $g(x) = x_1^2 + x_2 - 1 = 0$.

We use theorem (3.1) with $n = 2$, $m = 1$.
There exists a Lagrange multiplier $\lambda$ such that $\nabla(f + \lambda g) = 0$.
This implies:
$$\begin{pmatrix} \partial L/\partial x_1 \\ \partial L/\partial x_2 \end{pmatrix} = \begin{pmatrix} -2x_1 + 2\lambda x_1 \\ -2x_2 + \lambda \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
As there are three unknowns, we need another equation (i.e. the constraint itself).
Thus we have the following system:
$$\begin{cases} -2x_1 + 2\lambda x_1 = 0 & \text{(i)} \\ -2x_2 + \lambda = 0 & \text{(ii)} \\ x_1^2 + x_2 - 1 = 0 & \text{(iii)} \end{cases}$$
From (i): $x_1 = 0$ or $\lambda = 1$ ↘
If $x_1 = 0$: $x_2 = 1$ (iii) and $\lambda = 2$ (ii)
If $\lambda = 1$: $x_2 = 1/2$ (ii) and $x_1 = \pm\frac{1}{\sqrt2}$ (iii)

Thus we have two solutions:
↳ $x_1 = 0$, $x_2 = 1$, $\lambda = 2$
↳ $x_1 = \pm\frac{1}{\sqrt2}$, $x_2 = 1/2$, $\lambda = 1$
[Checked. The notes do not say which of these is the minimum (continued on HW 13?).]

## HW 13 — Optimisation in $\R^n$ with constraints: examples (two constraints)
_File `20261122_010009.jpg`. Header "Optimisation in $\R^n$ with constraints – examples". Bottom fifth blank._

**Ex.** Find the local extrema of $f(x) = x_1^3 + x_2^3 + x_3^3$
where
$$g_1(x) = x_1^2 + x_2^2 + x_3^2 - 5 = 0, \qquad g_2(x) = x_1^2 + x_2^2 + x_3^2 - 2x_1 - 3 = 0$$
Use theorem (3.1) with $n = 3$, $m = 2$. [written "$n = 3$, $n = 2$"; the second is $m$]
$$\begin{aligned} L(x) &= f + \lambda_1 g_1 + \lambda_2 g_2 \\ &= x_1^3 + x_2^3 + x_3^3 + \lambda_1(x_1^2 + x_2^2 + x_3^2 - 5) + \lambda_2(x_1^2 + x_2^2 + x_3^2 - 2x_1 - 3) \end{aligned}$$
$$\begin{aligned} \frac{\partial L}{\partial x_1} &= 3x_1^2 + 2\lambda_1 x_1 + 2\lambda_2(x_1 - 1) = 0 && \text{(i)} \\ \frac{\partial L}{\partial x_2} &= 3x_2^2 + 2\lambda_1 x_2 + 2\lambda_2 x_2 = 0 && \text{(ii)} \\ \frac{\partial L}{\partial x_3} &= 3x_3^2 + 2\lambda_1 x_3 + 2\lambda_2 x_3 = 0 && \text{(iii)} \end{aligned}$$
where the other two equations are $g_1, g_2 = 0$.

From $g_1 - g_2$, we obtain $x_1 = 1$. Substituting into (i), we obtain $\lambda_1 = -3/2$.
From (ii): $x_2 = 0$ or $3x_2 + 2\lambda_1 + 2\lambda_2 = 0$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(iii): $x_3 = 0$ or $3x_3 + 2\lambda_1 + 2\lambda_2 = 0$
If $x_2 = 0$, $x_1 = 1$ $\Rightarrow$ $x_3 = \pm 2$ $\quad (g_1)$
If $x_3 = 0$, $x_1 = 1$ $\Rightarrow$ $x_2 = \pm 2$ $\quad (g_2)$
If $x_2 \ne 0$, $x_3 \ne 0$ $\Rightarrow$ $x_2 = x_3$ $\quad$ (ii, iii)
[Checked. The second line cites $(g_2)$; $g_1$ (or $g_2$) gives the same. The example stops here: the case $x_2 = x_3$ is not finished and the extrema are not classified.]

## HW 14 — Optimisation in $\R^n$ with constraints: non-degeneracy, bordered Hessian
_File `20261122_010015.jpg`. Header "Optimisation in $\R^n$ with constraints – non-degeneracy"._

**Def.** How do we distinguish between maxima and minima?
Suppose we are minimising $f(x_1, \dots, x_n)$ subject to
$$g_1(x_1, \dots, x_n) = c_1, \quad \dots, \quad g_m(x_1, \dots, x_n) = c_m$$
The Lagrangian is:
$$L = f + \lambda_1 g_1 + \dots + \lambda_m g_m.$$
Suppose $a$ is a critical point. Then $\nabla L(a) = 0$.

Let $H_L$ be the Hessian matrix of $L$. Thus $H_L$ involves $\lambda_1, \dots, \lambda_m$ as well as $a_1, \dots, a_n$.
Note that at a minimum (crit. point) $a$, we have
$$h\T H_L h \ge 0 \qquad \forall h \ne 0 : h\T \nabla g_j = 0 \ \forall j$$

Define the matrix $B$ by $\nabla g$:
$$B = \nabla g = \begin{bmatrix} \partial g_1/\partial x_1 & \cdots & \partial g_m/\partial x_1 \\ \vdots & \ddots & \vdots \\ \partial g_1/\partial x_n & \cdots & \partial g_m/\partial x_n \end{bmatrix}_{n \times m}$$
and thus define the bordered Hessian by:
$$H = \begin{bmatrix} H_L & B \\ B\T & O \end{bmatrix}_{(n+m) \times (n+m)} \quad \text{at } x = a.$$
where $O$ is an $m \times m$ zero matrix.

A point $a$ where $\nabla L = 0$ and $\det H \ne 0$ is called a *non-degenerate critical point*.

## HW 15 — Optimisation in $\R^n$ with constraints: distinguishing maxima and minima
_File `20261122_010018.jpg`. Header "Optimisation in $\R^n$ with constraints – dis. max and min." Lower half blank._

**Th. (3.2)** Let $a$ be a non-degenerate critical point of $f$ subject to $g_j(x) = c_j$, $j = 1, \dots, m$. Then $a$ is a local minimum of $f$ (subject to constraints $g_j$) iff:
$$h\T H_L h \ge 0 \qquad \forall h: h\T \nabla g_j(a) = 0,\ j = 1, \dots, m.$$

**Cor.** The point $a$ is a local maximum of $f$ (subject to constraints $g_j$) iff $h\T H_L h \le 0$ $\forall h: h\T \nabla g_j(a) = 0$.

**Cor.** The inequality does not need to be strict (?) but we will show (Proof, part 2) that the equality cannot hold.
[The "(?)" is in the notes. The "Proof, part 2" referred to is on HW 16–17.]

## HW 16 — Optimisation in $\R^n$ with constraints (proof of 3.2), step 1
_File `20261122_010022.jpg`. Header "Optimisation in $\R^n$ with constraints (proof of 3.2)"._

**P.** We split the proof into two steps.

<u>Step 1:</u> we first show/prove in the forward direction.
Suppose that $a$ is a local minimum. Then
$$f(a + \varepsilon h) \ge f(a) \qquad \forall h: \abs h = 1,\ \forall \varepsilon: \abs\varepsilon \le \varepsilon_0.$$
with constraint $g_j(a + \varepsilon h) = c_j$, $j = 1, \dots, m$.
As $g_j$ is constant, this implies that
$$L(a + \varepsilon h) \overset{?}{\ge} L(a) \quad \text{[blacked-out text]} \quad \forall h: \abs h = 1,\ \forall \varepsilon: \cdots$$
[the "?" is written above the "$\ge$" in the notes]
We now apply Taylor's expansion:
$$f(a + \varepsilon h) - f(a) = L(a + \varepsilon h) - L(a) = \varepsilon h\T \nabla L(a) + \tfrac12 \varepsilon^2 h\T H_L(a) h + O(\varepsilon^3)$$
As $g_j(a + \varepsilon h) = c_j$, an equivalent constraint is $h\T \nabla g_j(a) = 0$ (see proof in 3.1)
$$= \cancel{\varepsilon h\T}\, \vect 0 + \tfrac12 \varepsilon^2 h\T H_L(a) h + O(\varepsilon^3)$$
[the "$\varepsilon h\T$" in front of the underlined $0$ is struck through]
for all $h \in \R^n$: $\abs h = 1$ and $h\T \nabla g_j(a) = 0$ for $j = 1, \dots, m$. **\***
[Left-margin brackets with arrows: one joins "As $g_j$ is constant …" to the Taylor line; another joins the Taylor line to "for all $h \in \R^n$ …".]

Note that if $h\T H_L(a) h > 0$, $\forall h: \norm h = 1$, $h\T \nabla g_j(a) = 0$, as this set is a closed set, by the EVT $\exists h_0$: $\abs{h_0} = 1$, $h_0\T \nabla g_j(a) = 0$ such that
$$h_0\T H_L(a) h_0 = \min\set{h\T H_L(a) h} > 0.$$
Thus
$$\cancel{\varepsilon h\T \nabla L(a)} + \tfrac12 \varepsilon^2 h\T H_L(a) h + O(\varepsilon^3) \ge \tfrac12 \varepsilon^2 h_0\T H_L(a) h_0 + O(\varepsilon^3) > 0.$$
[the first term is struck through in the notes]

**\*** In order for $a$ to give $f(x)$ a minimum, we require $h\T H_L h \ge 0$ at $a$, $\forall$ [the sentence ends here]
[The set used with the EVT is closed and bounded (the unit sphere intersected with a subspace); the notes say only "closed".]

## HW 17 — Optimisation in $\R^n$ with constraints (proof of 3.2), step 2
_File `20261122_010027.jpg`. Header "Optimisation in $\R^n$ with constraints (proof of 3.2)"._

**P.** [continued] We have shown that $h\T H_L h > 0$ is necessary (and apparently sufficient) for a local minimum in Step 1.
We must now show no $h_0$: $\abs{h_0} = 1$, $h_0\T \nabla g_j(a) = 0$, $j = 1, \dots, m$ exist such that $h_0\T H_L(a) h_0 = 0$. [a hooked arrow from "$h_0$" to the note "$h_0 \ne 0$"]
[possible error: Step 1 shows that $h\T H_L h > 0$ (on the tangent space) is *sufficient*, and that $h\T H_L h \ge 0$ is *necessary*; "necessary (and apparently sufficient)" has these the wrong way round.]

<u>Step 2:</u> We prove the equality does not hold by contradiction.
Let $A = H_L(a)$, and
$$B = \nabla g(a) = \Bigl(\frac{\partial g_j}{\partial x_i}\Bigr)_{n \times m} = (\nabla g_1, \dots, \nabla g_m)$$
[the last entry is written $\nabla g_n$]
By the assumption made ($h\T H_L h \ge 0$, $\forall h: h\T \nabla g_j(a) = 0$), $h_0$ minimises $h\T A h = \sum_{i,j=1}^n h_i A_{ij} h_j$, given conditions above.

The condition $h\T \nabla g_j(a) = 0 \Rightarrow h\T B = 0 \Rightarrow B\T h = 0$.

By theorem 3.1, we can formulate this using Lagrangian multipliers $\mu_1, \dots, \mu_m$ such that $h_0$ satisfies
$$\nabla_h\bigl(h\T A h + h\T B \mu\bigr) = 0, \quad B\T h = 0, \quad \mu\T = (\mu_1, \dots, \mu_m)$$
$$↳ \ \nabla_h\Bigl(\sum_{i,j=1}^n h_i A_{ij} h_j + h_i \nabla_i g_j \mu_j\Bigr) = 0, \quad B\T h = 0$$
**\*\*** [double asterisk in the notes]
implying that
$$\begin{cases} 2Ah + B\mu = 0 \\ B\T h = 0 \end{cases}$$
which is equivalent to (in matrix form)
$$\underbrace{\begin{pmatrix} A & B \\ B\T & 0 \end{pmatrix}}_{H(a)} \begin{pmatrix} 2h \\ \mu \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
[a long arrow labelled "equivalent to $h_0 H_L(a) h_0$" points from the right of the matrix equation back to $H(a)$. The first block row of the product is $2Ah + B\mu$, so the vector should be $(h, \mu)$ with $\mu$ rescaled, or the equation $2Ah + B\mu$ written as $A(2h) + B\mu$; as written it is consistent.]
If $\det(H(a)) \ne 0$, then $2h = 0$ and $\mu = 0$, implying that $h_0 = 0$. This is a contradiction, as $\abs h = 1$. Thus $\det(H(a)) = 0$.
Thus $\nexists h_0 \ne 0$: $h_0\T g_j(a) = 0$ s.t. $h_0\T H_L(a) h_0 = 0$.
Hence, at last, $h\T H_L h > 0$ is needed (?) for a local min. $\square$
[possible error: the logic of the last lines is muddled. The contradiction shows that a minimiser $h_0$ with $h_0\T H_L h_0 = 0$ forces $\det H(a) = 0$, contradicting non-degeneracy ($\det H(a) \ne 0$); so no such $h_0$ exists. "Thus $\det(H(a)) = 0$" states the contradiction as a conclusion. Also $h_0\T g_j(a)$ should be $h_0\T \nabla g_j(a)$. The "(?)" is in the notes. The Lagrange step ignores the constraint $\abs h = 1$; this is harmless here because the minimum value is $0$, but it is not said.]

## HW 18 — Optimisation in $\R^n$ with constraints: method and worked example
_File `20261122_010032.jpg`. Header "Optimisation in $\R^n$ with constraints – example", with an asterisk in the top right corner._

**N.** Recall that to solve constrained problems we must:
(1) Construct Lagrangian $L = f + \sum_{i=1}^m \lambda_i g_i$
(2) Find critical points $a$, where $\nabla L = 0$.
(3) Check non-degeneracy of bordered Hessian $H = \begin{bmatrix} H_L & B \\ B\T & O \end{bmatrix}$, i.e. $\det(H) \ne 0$
(4) Find $h$ in tangent space.
(5) Check sign of $h\T H_L h$.

**Ex.** We return to the previous example where $f(x) = x_1^3 + x_2^3 + x_3^3$, …
Steps (1) and (2) have been completed. We start with (3).
The Hessian of $L$ is given by:
$$H_L = \begin{pmatrix} 6x_1 + 2\lambda_1 + 2\lambda_2 & 0 & 0 \\ 0 & 6x_2 + 2\lambda_1 + 2\lambda_2 & 0 \\ 0 & 0 & 6x_3 + 2\lambda_1 + 2\lambda_2 \end{pmatrix}$$
and $B$ is given by:
$$B = (\nabla g_1\ \nabla g_2) = \begin{pmatrix} 2x_1 & 2x_1 - 2 \\ 2x_2 & 2x_2 \\ 2x_3 & 2x_3 \end{pmatrix}$$
We now check for each critical point that [blacked-out mark] $\det H \ne 0$.
Checking $\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$: $\lambda_1 = \lambda_2 = -3/2$.
$$H_L = \begin{bmatrix} 0 & 0 & 0 \\ 0 & -6 & 0 \\ 0 & 0 & 6 \end{bmatrix}, \qquad B = \begin{bmatrix} 2 & 0 \\ 0 & 0 \\ 4 & 4 \end{bmatrix}$$
$$H = \begin{bmatrix} 0 & 0 & 0 & 2 & 0 \\ 0 & -6 & 0 & 0 & 0 \\ 0 & 0 & 6 & 4 & 4 \\ 2 & 0 & 4 & 0 & 0 \\ 0 & 0 & 4 & 0 & 0 \end{bmatrix}$$
$$\det H = -2\begin{vmatrix} 0 & -6 & 0 & 0 \\ 0 & 0 & 6 & 4 \\ 2 & 0 & 4 & 0 \\ 0 & 0 & 4 & 0 \end{vmatrix} = -2 \times -(-6) \times \begin{vmatrix} 0 & 6 & 4 \\ 2 & 4 & 0 \\ 0 & 4 & 0 \end{vmatrix} = -2 \times 6 \times (-4) \times (-2) \times (-16) \ne 0.$$
[Checked: $H_L$, $B$, $H$ and the two cofactor expansions are right. possible error: the $3 \times 3$ determinant is $32$, so $\det H = -2 \times 6 \times 32 = -384$; the product on the last line (whose last factor reads "$(-16)$", possibly "$(-1 \cdot 6)$") does not equal this. The conclusion $\det H \ne 0$ is right. In $H_L$ the middle entry may read "$6x_2 + 2\lambda_1 - 2\lambda_2$"; the sign is unclear in the hand and $+$ is correct.]

## HW 19 — Optimisation in $\R^n$ with constraints: worked example (cont.)
_File `20261122_010035.jpg`. Header "Optimisation in $\R^n$ with constraints – example", asterisk in the top right corner. Lower 40% blank._

**Ex.** [continued] We must now find $h$ in the tangent space (4).
i.e. find $h$ such that $h\T \nabla g_1 = 0$, $h\T \nabla g_2 = 0$.
Thus,
$$(h_1\ h_2\ h_3)\begin{pmatrix} 2 \\ 0 \\ 4 \end{pmatrix} = 0, \qquad (h_1\ h_2\ h_3)\begin{pmatrix} 0 \\ 0 \\ 4 \end{pmatrix} = 0$$
which implies $h_1 = h_3 = 0$, and thus $h_2 = \mu \in \R$.
Hence $h\T = (0, \mu, 0)$ for $\mu \in \R$.

Finally we check the sign of $h\T H_L h$ (5).
$$(0, \mu, 0)\begin{pmatrix} 0 & 0 & 0 \\ 0 & -6 & 0 \\ 0 & 0 & 6 \end{pmatrix}\begin{pmatrix} 0 \\ \mu \\ 0 \end{pmatrix} = -6\mu^2 < 0$$
Thus $a = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}$ is a local maximum.
We repeat this procedure for the remaining critical points.
[Checked. "$< 0$" needs $\mu \ne 0$. The remaining critical points are not done in the notes.]

