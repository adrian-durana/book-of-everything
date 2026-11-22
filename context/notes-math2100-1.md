# MATH2100 Applied Mathematical Analysis (MATH2010 ODEs + MATH2011 PDEs): transcription, part 1 of 5 (HW 01–26)
 
_Transcription phase. Nothing here is book text yet. No dates are recorded; the sources are identified only by the semester of the workbooks (Semester 2, 2025)._
 
## Sources (all five parts)
| Code | Source | Role | Where |
|---|---|---|---|
| **HW nn** | 100 photos of the handwritten notebook, numbered in shooting order (file name under each heading). Each photo is a two-page spread (left and right page), except HW 01 and HW 45 (single contents pages, photographed sideways). HW 01–44 = MATH2010 half (ODEs: systems, phase plane, stability, nonlinear systems, Laplace transforms); HW 45–100 = MATH2011 half (PDEs: Fourier series, vector calculus, the big three PDEs, d'Alembert, Fourier's method, infinite domains, harmonic functions). HW 98 is a duplicate of HW 97. | **Main source** | Parts 1–4, in full |
| **CN-ODE** | *MATH2010-MATH2100-MATH7100 Analysis of Ordinary Differential Equations*, lecture workbook, 119 pp. Printed page = PDF page. | Supplement | Part 5: index, figures, content found only here |
| **CN-PDE** | *MATH2011 & the PDE section of MATH2100/7100*, lecture workbook, 155 pp. Printed page = PDF page − 1. | Supplement | Part 5 |
 
"CN §x.y" in parts 1–2 means CN-ODE, in parts 3–4 CN-PDE. The workbooks leave most derivations and examples as empty boxes; the handwritten notes are the filled-in lectures, so they are the more complete source almost everywhere.
 
**Parts.** 1: HW 01–26 (systems of ODEs, phase plane, stability, nonlinear systems). 2: HW 27–44 (Laplace transforms). 3: HW 45–68 (intro to PDEs, Fourier series, vector calculus, derivation of the big three). 4: HW 69–100 (wave equation, Fourier's method, inhomogeneous problems, Laplace's equation in a rectangle, heat equation on infinite domains, method of images, harmonic functions, point sources, potential theory). 5: typed-notes index.
 
Page counts: HW 100 photos = 197 notebook pages (98 spreads + 2 single pages; HW 98 duplicates HW 97, so 195 distinct pages, a few of them blank); CN-ODE 119 pp.; CN-PDE 155 pp.
 
## Legibility check (all 100 photos, in order)
Every photo was read at full resolution (rotated, split into left and right pages and contrast-normalised; doubtful spots re-checked on full-resolution crops). **No retakes are needed.** Sharpness and exposure are fine on all pages; many photos have a broad shadow or a bright patch across one page, but the ink reads through it everywhere. No page is cut off.
- **HW 98** (`20261122_001209.jpg`) is a second shot of the same spread as HW 97. Nothing is missing; it can be deleted.
- Orientation only (not a retake issue): HW 01 and HW 45 are single pages shot sideways; HW 17 (`20261121_235557.jpg`) is upside down.
- **HW 87** (`20261122_000942.jpg`): the left page curves into the gutter; the line ends there are soft but were read from a crop ("localised at $t = 0$").
Content that cannot be read is in the notebook itself (a retake won't help): blacked-out words (struck-out text) on many pages, noted where they occur; HW 23 smudged subscripts in the general Jacobian; HW 77 a blacked-out part of a denominator. Each is marked in place. Small ambiguities in the hand ("3"/"5" on HW 34, "h"/"k" on HW 86, a squiggle on HW 92) are resolved in brackets where they occur.
## Conventions
Wording, structure and labels follow the notes: **Def.**, **Ex.**, **Rem.**, **P.** (= proof), **N.** (= note, the notes' label for running exposition). Maths uses `notation.tex` macros (`\vect`, `\mat`, `\T`, `\tr`, `\dd`, `\R`, `\C`, `\N`, `\Z`, …). Vectors underlined in the notes are written `\vect{}`; unit vectors $\vec\imath, \vec\jmath, \vec k$ as in the notes. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic was re-checked where it says "Checked"); `[illegible]` marks unreadable text. Crossed-out text is noted only where it carries meaning. Figures are described in enough detail to redraw in TikZ (axes, labels, points, shading, arrows).
 
---
 
## HW 01 — Contents page (MATH2010 half)
_File `20261121_235333.jpg`. Single page, photographed sideways. A bright light patch crosses the lower right, but everything is readable._
 
**MATH2100**
**Applied Math. Analysis**
 
| No. | Title |
|---|---|
| 1 | Intro to MATH2010 (ODEs) |
| 2 | Differential Equations |
| 2.1 | Intro to systems, classifying |
| 2.2 | Solving systems of two coupled 1st-order ODEs |
| 2.3 | Existence and uniqueness for 1-st-order systems |
| 2.4 | Phase Planes for homo. const. linear systems |
| 2.5 | Critical points, stability |
| 2.6 | Non-homo linear systems |
| 2.7 | Non-linear systems |
| 3 | Laplace Transforms |
| 3.1 | Finding Laplace transforms |
| 3.2 | LTs of derivatives, solving simple linear const. cases and systems |
| 3.3 | Finding inverse Laplace transforms using partial fractions |
| 3.4 | Second shifting theorem |
| 3.5 | Convolution theorem |
 
[This mirrors the CN (MATH2010) table of contents, chapters 1–3.]
 
## HW 02 — Introduction to ODEs; introduction to systems of ODEs
_File `20261121_235343.jpg`. Two-page spread. Left page header "Introduction to ODEs", right page header "Introduction to systems of ODEs"; both carry the section number 1._
 
**Left page.**
 
**Def.** An ordinary differential equation (ODE) involves only one independent variable.
 
**Ex.** The ODE for a mass spring system:
$$m\frac{\dd^2 x}{\dd t^2} = -kx - c\frac{\dd x}{\dd t}$$
Note that the equation only involves a function $x(t)$ of a single variable $t$.
 
**Def.** The ODE half of this course covers two parts:
↳ Systems of ODEs
↳ Laplace transforms
We first cover systems of ODEs.
 
**Right page.**
 
**Ex.** We model the spread of an infectious disease:
$$\begin{cases} \dfrac{\dd I}{\dd t} = f(I, S) \\[2mm] \dfrac{\dd S}{\dd t} = g(I, S) \end{cases} \qquad \text{where } I: \#\text{ infected},\quad S: \#\text{ susceptible}$$
 
**Ex.** Consider the electrical circuit:
 
*Figure (series LRC circuit).* A rectangular loop. Top side, left to right: an arrow pointing right labelled $I(t)$ (current direction), then a zig-zag resistor labelled $R$. Right side: a capacitor (two short parallel horizontal plates, the gap drawn horizontally) labelled $C$, with $Q(t)$ written to its left. Bottom side: a battery/voltage source (two short vertical plates of unequal length) labelled $E(t)$ below it, near the bottom-left corner. Left side: a coil (inductor) labelled $L$. Legend to the right: R: resist., L: inductor, C: capacitor, $I(t)$: current, $Q(t)$: charge, $E(t)$: voltage applied.
 
Kirchhoff's law states that the voltage drop across the inductor plus the voltage drop across the resistor plus the voltage drop across the capacitor equals the applied voltage.
$$L\frac{\dd I(t)}{\dd t} + RI(t) + \frac{Q(t)}{C} = E(t)$$
As charge is related to current – $I(t) = \dfrac{\dd Q}{\dd t}$:
$$L\frac{\dd^2 Q}{\dd t^2} + R\frac{\dd Q}{\dd t} + \frac{Q}{C} = E(t)$$
or, to rewrite:
$$\frac{\dd^2 Q}{\dd t^2} = \frac{E(t)}{L} - \frac{Q}{CL} - \frac{R}{L}\frac{\dd Q}{\dd t}.$$
 
## HW 03 — Introduction to systems of ODEs (cont.): the LC circuit, phase space
_File `20261121_235351.jpg`. Two-page spread, both pages headed "Introduction to systems of ODEs", section 1._
 
**Left page.**
 
**Ex.** This second-order ODE can be written as a system of two first-order ODEs:
$$\begin{cases} \dfrac{\dd Q}{\dd t} = I \\[2mm] \dfrac{\dd I}{\dd t} = \dfrac{\dd^2 Q}{\dd t^2} = -\dfrac{Q}{CL} - \dfrac{R}{L} I + \dfrac{E(t)}{L} \end{cases}$$
or, in matrix form, by:
$$\frac{\dd}{\dd t}\begin{bmatrix} Q \\ I \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -\frac{1}{CL} & -\frac{R}{L} \end{bmatrix}\begin{bmatrix} Q \\ I \end{bmatrix} + \begin{bmatrix} 0 \\ \frac{E(t)}{L} \end{bmatrix}$$
 
**Ex.** Take an electrical circuit with $R = 0$, $L = 1$, $C = 1$ and $E(t) = 0$. Then:
$$\frac{\dd^2 Q}{\dd t^2} + Q = 0$$
↳ $\lambda^2 e^{\lambda t} + e^{\lambda t} = 0$
↳ $e^{\lambda t}(\lambda^2 + 1) = 0$
$\Rightarrow \lambda = \pm i$
Thus, $Q(t) = c_1 e^{it} + c_2 e^{-it}$ where $c_1, c_2 \in \C$.
 
**Right page.**
 
**Ex.** In this case, if $c_2 = \bar{c}_1$, then
$$Q(t) = A\cos t + B\sin t \quad \text{where } A, B \in \R$$
If $Q(0) = 0$, the solution of the IVP is
$$Q(0) = A\cos 0 + B\sin 0 = A = 0 \ \Rightarrow\ Q(t) = B\sin(t)$$
Thus the solution is
$$\begin{pmatrix} Q(t) \\ I(t) \end{pmatrix} = \begin{pmatrix} B\sin t \\ B\cos t \end{pmatrix}$$
We can deduce that the charge and current oscillate out of phase with each other.
 
**Rem.** The solution curves are circles in $(Q, I)$ space. To show this, consider $Q^2 + I^2$.
However, the full 3D space $(t, Q, I) = (t, c_2\sin t, c_2\cos t)$ is hard to work with.
[possible error: the amplitude is called $B$ two lines earlier and $c_2$ here.]
The $(Q(t), I(t))$ space is called *phase space*.
In 2D phase space, there are six qualitatively different linear systems.
 
## HW 04 — Introduction (Laplace part); systems of first-order ODEs
_File `20261121_235405.jpg`. Left page "Introduction to systems of ODEs" (section 1), right page "Systems of first-order ODEs" (section 2.1)._
 
**Left page.**
 
**Def.** The second part of the ODE half of the course concerns Laplace transforms. In Laplace transforms we will solve systems that are time-dependent.
 
**Ex.** Consider the previous circuit example with a variable applied voltage; in particular, a voltage that has suddenly switched off. Assume that this voltage is off at time $t = h$.
$$E(t) = \begin{cases} E_0 & 0 \le t < h \\ 0 & h \le t \end{cases}$$
Then for some circuits, the result is oscillatory behaviour.
 
**Rem.** Laplace transforms are useful as they can be used to solve equations with discontinuous terms.
 
**Right page.**
 
**Ex.** Systems of first-order ODEs arise naturally. Consider the Lotka–Volterra (predator–prey) model.
$$\begin{cases} \dfrac{\dd r}{\dd t} = a r(t) - b r(t) f(t) \\[2mm] \dfrac{\dd f}{\dd t} = -\ell f(t) + k r(t) f(t) \end{cases}$$
These equations are coupled – we cannot solve either independently.
 
**Ex.** Consider a mass–spring–damper system.
$$m\ddot{x} = -kx - c\dot{x}$$
As $\dfrac{\dd p}{\dd t} = m\ddot{x} = -kx - c\dot{x}$ (linear momentum), we can convert into a system of first order ODEs:
$$\begin{cases} \dot{x} = \dfrac{p}{m} \\[2mm] \dot{p} = -kx - \dfrac{cp}{m} \end{cases} \qquad \text{or} \qquad \frac{\dd}{\dd t}\begin{pmatrix} x \\ p \end{pmatrix} = \begin{bmatrix} 0 & \frac{1}{m} \\ -k & -\frac{c}{m} \end{bmatrix}\begin{bmatrix} x \\ p \end{bmatrix}$$
 
## HW 05 — Converting $n$th-order ODEs to $n$-systems; classifying ODEs
_File `20261121_235411.jpg`. Left page "Converting $n$th order to $n$-systems", right page "Classifying ODEs"; both section 2.1._
 
**Left page.**
 
**Ex.** Consider $\ddot{y} + \dot{y} - 2y = 0$.
Let $y_1 = y$, $y_2 = \dot{y}$.
Then $\dot{y}_1 = \dot{y} = y_2$, $\dot{y}_2 = \ddot{y} = 2y - \dot{y}$
$$\Rightarrow \begin{cases} \dot{y}_1 = y_2 \\ \dot{y}_2 = 2y_1 - y_2 \end{cases}$$
 
**Def.** Any $n$-th order ODE in the form
$$\frac{\dd^n y}{\dd t^n} = F\left(t, y, \frac{\dd y}{\dd t}, \frac{\dd^2 y}{\dd t^2}, \dots, \frac{\dd^{(n-1)} y}{\dd t^{(n-1)}}\right)$$
can be written as a system of $n$ first-order ODEs:
Let $y_1 = y$, $y_2 = \dot{y}$, …, $y_n = y^{(n-1)}$. Then
$$\begin{cases} \dd y_1/\dd t = y_2 \\ \dd y_2/\dd t = y_3 \\ \quad\vdots \\ \dd y_{n-1}/\dd t = y_n \\ \dd y_n/\dd t = F(t, y_1, y_2, \dots, y_n) \end{cases}$$
 
**Right page.**
 
**Def.** A differential equation is either:
↳ Ordinary (one variable)
↳ Partial (more variables)
ODEs are either:
↳ Linear ⟶ [a bracket from "Linear" points to] ↳ Homogenous / ↳ Non-homogenous
↳ Non-linear
 
**Def.** An ODE is *linear* if it is linear in the unknown ($y$) and its derivatives. It need not be linear in the ind. var. ($t$).
 
**Def.** The *order* of an ODE refers to the order of its highest derivative.
 
**Def.** An ODE is *homogenous* if:
↳ if $y(t)$ is a solution, $cy(t)$ is also, $c \in \R$.
 
## HW 06 — Examples of homogeneous ODEs; superposition principle; revision of known ODE methods
_File `20261121_235416.jpg`. Left page "Examples of homogenous ODEs", right page "Superposition principle"; both section 2.1._
 
**Left page.**
 
**Ex.** $L[y(t)] = \dfrac{\dd^2 y}{\dd t^2} + 2\dfrac{\dd y}{\dd t} - \cos(5t)\,y = 0$ is homo.
We must show $L[y(t)] \Rightarrow L[c(y(t))] = 0\ \forall c$
$$L[cy(t)] = \frac{\dd^2}{\dd t^2}(cy) + 2\frac{\dd}{\dd t}(cy) - \cos(5t)(cy) = c\left[\frac{\dd^2 y}{\dd t^2} + 2\frac{\dd y}{\dd t} - \cos(5t)\,y\right] = 0$$
[a small filled-in (blacked-out) box follows the first line; nothing readable under it. "$L[y(t)] \Rightarrow$" reads as "$L[y(t)] = 0 \Rightarrow$".]
 
**Ex.** $L[y(t)] = \dfrac{\dd^2 y}{\dd t^2} - e^t\dfrac{\dd y}{\dd t} + \cos 5t \cdot y - t^5 = 0$ is not.
$$\begin{aligned} L[y(t)] &= 0 \\ L[cy(t)] &= \frac{\dd^2}{\dd t^2}(cy) - e^t\frac{\dd}{\dd t}(cy) + \cos 5t\,(cy) - t^5 \\ &= c\left(\frac{\dd^2 y}{\dd t^2} - e^t\frac{\dd y}{\dd t} + y\cos 5t\right) - t^5 \\ &= -t^5 \ne 0. \end{aligned}$$
[possible error: since $L[y] = 0$, the bracket equals $t^5$, so $L[cy] = ct^5 - t^5 = (c-1)t^5$, which is $\ne 0$ for $c \ne 1$; the last line treats the bracket as $0$.]
 
**Ex.** $\dfrac{\dd^3 u}{\dd x^3} = \sin x\, u(x) + 5$ is inhomogenous.
 
**Right page.**
 
**Def.** Linear, homogenous ODEs obey this principle. Linear combinations of solutions are also solutions.
$$y_1(t),\ y_2(t) \text{ sol.} \Rightarrow c_1(y_1(t)) + c_2(y_2(t))$$
This principle also works for systems.
$$\begin{pmatrix} y_{1a} \\ y_{1b} \end{pmatrix}, \begin{pmatrix} y_{2a} \\ y_{2b} \end{pmatrix} \text{ sol.} \Rightarrow c_1\begin{pmatrix} y_{1a} \\ y_{1b} \end{pmatrix} + c_2\begin{pmatrix} y_{2a} \\ y_{2b} \end{pmatrix}$$
[the conclusion "is also a sol." is implied, not written]
 
**Revision: ODE equations known**
 
**Def.** Linear first-order – $\dot{y} = q(x) - p(x)y$
↳ solve with integrating factor $e^{\int p(x)\dd x}$.
↳ $I(x)\dot{y} + I(x)p(x)y = I(x)q(x)$
  $\dfrac{\dd}{\dd x}\bigl(I(x)\,y\bigr) =$ [nothing written after "="]
[the notes write $\dot y$ for $\dd y/\dd x$ here]
 
Linear second-order, homogenous – $\ddot{y} = -qy - p\dot{y}$
↳ Real roots:
  ↳ Unique roots $\lambda_1, \lambda_2$: $c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$
  ↳ Repeated roots $\lambda_1 = \lambda_2$: $c_1 e^{\lambda_1 t} + c_2 t e^{\lambda_2 t}$
↳↳ Complex roots $\lambda = \alpha \pm i\beta$: $e^{\alpha t}\bigl(A\cos(\beta t) + B\sin(\beta t)\bigr)$
 
## HW 07 — Solving systems of two coupled first-order ODEs; homogeneous case with constant coefficients
_File `20261121_235423.jpg`. Left page "Solving systems of two coupled 1st-order ODEs", right page "Homogenous case – constant coefficients"; both section 2.2. Vectors are underlined in the notes; written here as `\vect{}`._
 
**Left page.**
 
**Def.** Any 2nd-order linear ODE can be written as a system of two coupled 1st-order ODEs.
$$\frac{\dd^2 y}{\dd t^2} + p(t)\frac{\dd y}{\dd t} + q(t)y(t) = r(t)$$
Let $y_1 = y$, $y_2 = \dot{y}$.
Then, $\dot{y}_1 = \dot{y} = y_2$,
$\dot{y}_2 = \ddot{y} = -q(t)y(t) - p(t)\dfrac{\dd y}{\dd t} - r(t)$
[possible error: from the ODE, $\ddot y = -q(t)y - p(t)\dot y + r(t)$; the next display has $+r(t)$.]
Hence:
$$\begin{cases} \dfrac{\dd y_1}{\dd t} = y_2 \\[2mm] \dfrac{\dd y_2}{\dd t} = -q(t)\,y_1 - p(t)\,y_2 + r(t) \end{cases}$$
[the $y_1$ is written above a blacked-out box]
or:
$$\frac{\dd}{\dd t}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} + \begin{pmatrix} 0 \\ r \end{pmatrix}, \qquad \frac{\dd \vect{y}}{\dd t} = \mat{A}(t)\vect{y} + \vect{R}(t)$$
If $\vect{R}(t) = \vect{0}$, the system is homogenous.
If $\vect{R}(t) \ne \vect{0}$, the system is inhomogenous.
 
**Right page.**
 
**Def.** Suppose that $\dot{\vect{y}} = \mat{A}\vect{y}$ with
$$\mat{A} = \begin{pmatrix} 0 & 1 \\ -q & -p \end{pmatrix} \quad \text{being constant.}$$
Recall the solution for homo. 2nd-order ODEs:
$\ddot{y} + p\dot{y} + qy = 0$, let $y = e^{\lambda t}$.
↳ $\lambda^2 e^{\lambda t} + p\lambda e^{\lambda t} + qe^{\lambda t} = 0$
$e^{\lambda t}(\lambda^2 + p\lambda + q) = 0$
which provides the auxillary equation:
$$\lambda^2 + \lambda p + q = 0$$
Given two roots $\lambda_1, \lambda_2$, the general solution to the ODE is $y = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$.
There are four cases:
↳ Real roots
  ↳ Unique roots $\lambda_1, \lambda_2$ ($\lambda_1 \ne \lambda_2$) [an arrow runs from this line up to the general solution above]
  ↳ Equal roots $\lambda_1, \lambda_2$ ($\lambda_1 = \lambda_2$)
↳ Complex roots
  ↳ Non-zero real part ($\alpha \pm i\beta$)
  ↳ Imaginary roots $\lambda_1, \lambda_2$ ($\pm i\beta$)
 
## HW 08 — Homogeneous case, constant coefficients: eigenvalue method; first example
_File `20261121_235429.jpg`. Left page "Homogenous case – constant coefficients", right page "Example on homo. case, cons. coeff."; both section 2.2._
 
**Left page.**
 
**Def.** For a system $\dot{\vect{y}} = \mat{A}\vect{y}$, try $\vect{y} = \vect{x}e^{\lambda t}$, where $\vect{x} = \begin{pmatrix} u \\ v \end{pmatrix} \in \R^2 \setminus \{0\}$ and $\lambda \in \R$.
Then,
$$\vect{y} = \begin{pmatrix} ue^{\lambda t} \\ ve^{\lambda t} \end{pmatrix} \Rightarrow \dot{\vect{y}} = \begin{pmatrix} u\lambda e^{\lambda t} \\ v\lambda e^{\lambda t} \end{pmatrix}$$
so
$$\dot{\vect{y}} = \begin{pmatrix} u \\ v \end{pmatrix}\lambda e^{\lambda t} = \mat{A}\begin{pmatrix} u \\ v \end{pmatrix}e^{\lambda t}.$$
This provides the eigenvalue equation for $\mat{A}$:
$$\mat{A}\vect{x} = \lambda\vect{x}$$
If there are two unique eigenvectors $\lambda_1, \lambda_2$ with eigenvectors $\vect{x}_1$ and $\vect{x}_2$, then the general solution to the matrix equation is:
$$\vect{y} = c_1\vect{x}_1 e^{\lambda_1 t} + c_2\vect{x}_2 e^{\lambda_2 t}$$
[possible error: "two unique eigenvectors $\lambda_1, \lambda_2$" should read "two distinct eigenvalues".]
 
**Rem.** Recall we solve the eigenvalue equation by $\det(\mat{A} - \lambda\mat{I}) = 0$.
 
**Right page.**
 
**Ex.** Consider the 2nd-order ODE $\ddot{y} + 2\dot{y} - 15y = 0$. As a system, we have:
$$\begin{cases} \dot{y}_1 = y_2 \\ \dot{y}_2 = 15y_1 - 2y_2 \end{cases} \Rightarrow \frac{\dd}{\dd t}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 15 & -2 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$$
Now let $\vect{y} = \vect{x}e^{\lambda t} \Rightarrow \dot{\vect{y}} = \lambda\vect{x}e^{\lambda t} = \mat{A}\vect{x}e^{\lambda t}$ [an arrow links the two right-hand sides]
Thus we have $\lambda\vect{x} = \mat{A}\vect{x}$.
We solve the eigenvalue equation:
$$\left|\begin{pmatrix} 0 & 1 \\ 15 & -2 \end{pmatrix} - \begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix}\right| = \begin{vmatrix} -\lambda & 1 \\ 15 & -2-\lambda \end{vmatrix} = 0$$
↳ $\lambda^2 + 2\lambda - 15 = 0 \to \lambda_1 = 3,\ \lambda_2 = -5$
$(\lambda - 3)(\lambda + 5) = 0$
If $\lambda_1 = 3$: $\begin{pmatrix} -3 & 1 \\ 15 & -5 \end{pmatrix}\begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ ↳ $v = 3u \to$ if $u = 1$, $v = 3$ ↳ $\vect{x}_1 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$
If $\lambda_2 = -5$: $\begin{pmatrix} 5 & 1 \\ 15 & 3 \end{pmatrix}\begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ ↳ $v = -5u \to$ if $u = 1$, $v = -5$ ↳ $\vect{x}_2 = \begin{pmatrix} 1 \\ -5 \end{pmatrix}$
Thus the general solution is:
$$\vect{y} = c_1\begin{pmatrix} 1 \\ 3 \end{pmatrix}e^{3t} + c_2\begin{pmatrix} 1 \\ -5 \end{pmatrix}e^{-5t}.$$
 
## HW 09 — Fundamental matrix and Wronskian; summary for $2 \times 2$ constant-coefficient systems; IVP example
_File `20261121_235442.jpg`. Left page "Homo. case, const. coeff. – fundamental matrix", right page "Summary on solving sys. of 2 coupled lin. const. coeff."; both section 2.2._
 
**Left page.**
 
**Ex.** Consider the previous example. The solution to the matrix equation is:
$$\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = c_1\begin{pmatrix} 1 \\ 3 \end{pmatrix}e^{3t} + c_2\begin{pmatrix} 1 \\ -5 \end{pmatrix}e^{-5t}$$
or in matrix form by:
$$\vect{y} = \begin{pmatrix} e^{3t} & e^{-5t} \\ 3e^{3t} & -5e^{-5t} \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$
 
**Def.** More generally, the solution is given by:
$$\vect{y} = \begin{pmatrix} y_1^{(1)} & y_1^{(2)} \\ y_2^{(1)} & y_2^{(2)} \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$
This matrix is called the *fundamental matrix*. The determinant is called the *Wronskian* $W$.
 
**Rem.** If the Wronskian is non-zero, then $\vect{y}_1$ and $\vect{y}_2$ are linearly independent and the general solution to the matrix equation is given by: $\vect{y} = c_1\vect{y}_1 + c_2\vect{y}_2$.
 
**Right page.**
 
**Def.** To solve $\dot{\vect{y}} = \mat{A}\vect{y}$ (where $\mat{A} \in M_{2\times 2}$, $\vect{y} = \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$):
↳ Solve for eigenvalues $\lambda_i$, eigenvectors $\vect{x}_i$ of $\mat{A}$
↳ Both $\vect{y}_1 = \vect{x}_1 e^{\lambda_1 t}$ and $\vect{y}_2 = \vect{x}_2 e^{\lambda_2 t}$ are solutions to the system.
↳ General solution is $\vect{y} = c_1\vect{x}_1 e^{\lambda_1 t} + c_2\vect{x}_2 e^{\lambda_2 t}$ given $\vect{y}_1, \vect{y}_2$ are linearly independent.
 
**Ex.** Solve $\ddot{y} - 3\dot{y} - 4y = 0$, $y(0) = 4$, $\dot{y}(0) = 6$.
$$\begin{cases} \dot{y}_1 = y_2 \\ \dot{y}_2 = 4y_1 + 3y_2 \end{cases} \Rightarrow \begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \Rightarrow \lambda_1 = -1,\ \lambda_2 = 4;\quad \vect{x}_{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix},\ \vect{x}_{(2)} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$$
Thus $\vect{y}_{(1)} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-t}$, $\vect{y}_{(2)} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}e^{4t}$.
Solving for initial values:
$$\vect{y}(0) = \begin{pmatrix} 1 & 1 \\ -1 & 4 \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix} \ \hookrightarrow\ \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ -1 & 4 \end{pmatrix}^{-1}\begin{pmatrix} 4 \\ 6 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}$$
[the final solution $\vect y$ is not written out]
 
## HW 10 — Homogeneous case, constant coefficients: complex eigenvalues
_File `20261121_235448.jpg`. Both pages "Homo. case, const. coeff – complex eig.", section 2.2._
 
**Left page.**
 
**Def.** We run into a problem when the eigenvalues are complex. We usually want a real solution.
 
**Ex.** Take $\ddot{y} + 4y = 0$. Thus,
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$$
The eigenvalues of $\mat{A}$ are given by $\det(\mat{A} - \lambda\mat{I}) = \lambda^2 + 4 = 0$.
↳ $\lambda = \pm 2i$
↳ $\begin{pmatrix} -2i & 1 \\ -4 & -2i \end{pmatrix}\begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ for $\lambda_1 = 2i$ $\Rightarrow -2iu + v = 0$, if $u = 1$, $v = 2i$, $\vect{x}_1 = \begin{pmatrix} 1 \\ 2i \end{pmatrix}$
↳ $\begin{pmatrix} 2i & 1 \\ -4 & 2i \end{pmatrix}\begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ for $\lambda_2 = -2i$ $\Rightarrow 2iu + v = 0$, …, $\vect{x}_2 = \begin{pmatrix} 1 \\ -2i \end{pmatrix}$.
Note that as the eigenvalues are complex conjugates of each other, the eigenvectors are also complex conjugates of each other.
The (complex) solution is thus:
$$\vect{y}_{(1)} = \begin{pmatrix} 1 \\ 2i \end{pmatrix}e^{2it} = \begin{pmatrix} \cos 2t \\ -2\sin 2t \end{pmatrix} + i\begin{pmatrix} \sin 2t \\ 2\cos 2t \end{pmatrix}$$
$$\vect{y}_{(2)} = \begin{pmatrix} 1 \\ -2i \end{pmatrix}e^{-2it} = \begin{pmatrix} \cos 2t \\ -2\sin 2t \end{pmatrix} - i\begin{pmatrix} \sin 2t \\ 2\cos 2t \end{pmatrix} = \vect{y}_1^r - i\vect{y}_1^c$$
 
**Right page.**
 
**Ex.** Continuing from the previous page:
$$\vect{y} = c_1\begin{pmatrix} 1 \\ 2i \end{pmatrix}e^{2it} + c_2\begin{pmatrix} 1 \\ -2i \end{pmatrix}e^{-2it}, \qquad c_1, c_2 \in \C.$$
For a real solution, $c_1$ and $c_2$ must be complex conjugates. Thus $c_1\vect{y}_1$ and $c_2\vect{y}_2$ are complex conjugates of each other, so their sum is real.
Let $c_1 = a + ib$, $c_2 = a - ib$. The general solution in real form is thus:
$$\vect{y} = (a + ib)(\vect{y}_1^r + i\vect{y}_1^c) + (a - ib)(\vect{y}_1^r \pm i\vect{y}_1^c) = \dots = 2a\vect{y}_1^r - 2b\vect{y}_1^c.$$
[ambiguous: the sign inside the second bracket could be $+$ or $-$ (the handwriting is unclear, not the photo). It must be $-$ for the result to hold (it is $\vect y_{(2)}$ from the left page).]
Thus for a real solution we need only find the real and imaginary parts of $\vect{y}_1$:
$$\vect{y}_{\text{real}}(t) = A\vect{y}_1^r + B\vect{y}_1^c, \qquad A, B \in \R$$
Back to our example:
$$\vect{y}_{\text{real}}(t) = d_1\begin{pmatrix} \cos 2t \\ -2\sin 2t \end{pmatrix} + d_2\begin{pmatrix} \sin 2t \\ 2\cos 2t \end{pmatrix}$$
for $d_1, d_2 \in \R$.
 
## HW 11 — Theory of first-order systems: IVPs, existence and uniqueness
_File `20261121_235458.jpg`. Both pages "Theory of first-order systems", section 2.3._
 
**Left page.**
 
**Def.** Take an $n$-dim. system:
$$\begin{cases} \dot{y}_1 = f_1(t, y_1, \dots, y_n) \\ \dot{y}_2 = f_2(t, y_1, \dots, y_n) \\ \dot{y}_n = f_n(t, y_1, \dots, y_n) \end{cases}$$
This can be re-written as $\dot{\vect{y}} = \vect{f}(t, \vect{y})$ where $\vect{y}, \vect{f}$ are $n$-dim., and $f_i(t, y_1, \dots, y_n)$ are not necessarily linear in $t$ or $y_i$.
For an IVP there is an initial condition: $\vect{y}(t_0) = \vect{K}$.
Thus an IVP is written as:
$$\dot{\vect{y}} = \vect{f}(t, \vect{y}), \qquad \vect{y}(t_0) = \vect{K}$$
 
**Def.** Existence and uniqueness.
For existence, let $f_i$ be continuous in some neighbourhood containing $(t_0, K_1, \dots, K_n)$. Then the IVP has at least one solution on some interval $(t_0 - \alpha, t_0 + \alpha)$.
For uniqueness, let $f_i$ be continuous with all continuous partial derivatives (w.r.t. $y_i$) in some neighbourhood containing $(t_0, K_1, \dots, K_n)$. Then the IVP has a UNIQUE solution on some interval $(t_0 - \alpha, t_0 + \alpha)$.
 
**Right page.**
 
**Ex.** Solutions may not exist for all time. Let $\dot{y} = y^2$.
As $f(t, y) = y^2$, $\dfrac{\partial f}{\partial y} = 2y$, which is continuous.
Solving for $y$:
$$y(t) = \frac{-1}{t + c} \to y(0) = \frac{-1}{c} \quad \text{which may not exist if } c = 0.$$
 
**Ex.** If $f_i$ are not continuous at $(t_0, y_i(0))$, existence/uniqueness is not guaranteed.
Let $\dd y/\dd t = 2y/t = f(t, y)$. Note that $f$ is not cont. at $t = 0$.
 
**Ex.** If $\partial f_i/\partial y_i$ are not continuous at $(t_0, y_i(0))$, ~~existence~~/uniqueness is not guaranteed. ["existence" is struck through]
Let
$$\begin{cases} y(0) = 0 & \to \text{cont. } \forall y \ge 0 \\ \dot{y} = \sqrt{y} = f(t, y) & \searrow\ \dfrac{\partial f}{\partial y} = \dfrac{1}{2\sqrt{y}} \text{ cont. } \forall y > 0. \end{cases}$$
Sol: (1) $y(t) = \dfrac{t^2}{4}$; (2) $y(t) = 0$.
 
## HW 12 — Introduction to phase spaces
_File `20261121_235508.jpg`. Both pages "Intro to phase spaces", section 2.4._
 
**Left page.**
 
**Def.** We have (currently) a vague idea of the behaviour we can expect from linear, constant-coeff. ODEs as they have exponential solutions. We expect:
↳ Exp. decay e.g. $e^{-3t}$
↳ Exp. growth e.g. $e^{2t}$
↳ Regular oscillatory behaviour e.g. $\sin(t)$
↳ Growing/decaying oscill. behaviour e.g. $e^t\sin(t)$
However in a 2D system there are always two fundamental solutions which can exhibit different behaviour. Ideally we would consider 3D space $(t, y_1, y_2)$ but this is complicated.
Hence we consider $(y_1(t), y_2(t))$ coordinates in $(y_1, y_2)$ space, known as *phase space*.
 
**Ex.** The linear pendulum (see 3B1B) is a good model. [3B1B: the YouTube channel 3Blue1Brown]
$$\ddot{\theta} = -g/\ell \cdot \theta.$$
Let $g/\ell = 9$. We can show (exercise) that we obtain
$$\vect{y} = \begin{pmatrix} \cos 3t \\ -3\sin 3t \end{pmatrix} + i\begin{pmatrix} \sin 3t \\ 3\cos 3t \end{pmatrix}$$
so $y_1^2 + \frac{1}{9}y_2^2 = 1$ (if $A = 1$, $B = 0$, or vice versa).
It can be shown that the general solution is given by $y_1^2 + \frac{1}{9}y_2^2 = c^2$ for some $c \in \R$.
 
**Right page.**
 
**Def.** In a phase space, each initial condition gives a (unique) curve, called a *trajectory*. Trajectories represent solutions to the ODE in phase space. This is called the *phase portrait* of a system.
 
**Ex.** In the linear pendulum example, the phase portrait is simply a lot of ellipses given by $y_1^2 + \frac{1}{9}y_2^2 = c^2$.
 
**Def.** Phase plane representations cannot provide all information (e.g. how fast you move along a phase curve). Direction of increasing time is given by an arrow.
 
**Rem.** Two trajectory curves cannot cross as this violates uniqueness – at the (hypothetical) point of intersection there are two solutions.
 
**Def.** A system $\dot{\vect{y}} = \mat{A}\vect{y}$ has a trivial solution $\vect{y}(t_0) = \vect{0}$. In other words, if $y_1(t_0) = 0$ and $y_2(t_0) = 0$ then $y_1(t) = y_2(t) = 0\ \forall t$. The trivial trajectory is very easy to plot!
 
*Figure (trivial trajectory).* Plain axes: a horizontal axis with an arrowhead pointing right and a vertical axis with an arrowhead pointing up, unlabelled; a small cross/dot marks the origin (the trivial trajectory is the single point $\vect 0$).
 
## HW 13 — Velocity vectors, direction fields and nullclines; summary of the six phase portraits
_File `20261121_235516.jpg`. Left page "Intro to phase spaces", right page "Summary on phase portraits"; both section 2.4. The lower half of both pages is blank._
 
**Left page.**
 
**Def.** Consider the vector equation $\dfrac{\dd\vect{y}}{\dd t} = \vect{f}(\vect{y})$ where $\vect{y}\T = (y_1, y_2)$. Then $\vect{f}(\vect{y})$ evaluated at $(y_1, y_2)$ represents the *velocity vector* at $(y_1, y_2)$.
The characteristics of a velocity vector:
↳ Direction: direction of flow
↳ Length: speed
We define the *direction field* as the field of these velocity vectors. Direction field are useful as we can use them to analyse ODEs without solving them.
 
**Def.** The slope of a vector in a direction field is given by
$$\frac{\dd y_2}{\dd y_1} = \frac{f_2(y_1, y_2)}{f_1(y_1, y_2)} = \frac{\dot{y}_2}{\dot{y}_1}$$
A *nulleline* is a line/curve where the slope is either $0$ or $\infty$. [spelt "nulleline"; the CN term is "nullcline"]
 
**Right page.**
 
**Def.** In this course we will study six qualitatively different phase portraits.
↳ Four are concerned with REAL eigenvalues
  ↳ Saddle (one $\lambda_i > 0$, one $\lambda_i < 0$)
  ↳ Improper nodes (both $\lambda_i$ $(+)$ or $(-)$)
  ↳ Proper nodes ($\lambda_i$ equal, l.i. eigenvectors)
  ↳ Degenerate nodes ($\lambda_i$ equal, one eigenvector)
↳ Two are concerned with COMPLEX eigenvalues
  ↳ Spiral/focus ($\lambda_i$ complex, either $(-)$ real part stable or $(+)$ real part unstable)
  ↳ Centre ($\lambda_i$ purely imaginary)
 
## HW 14 — Real phase portraits; improper stable nodes
_File `20261121_235523.jpg`. Left page "Real phase portraits", right page "Improper stable nodes"; both section 2.4._
 
**Left page.**
 
**Def.** Let $\dot{\vect{y}} = \mat{A}\vect{y}$. If the eigenvalues of $\mat{A}$ are real and distinct, recall the solution is in the form
$$\vect{y} = c_1\vect{x}^{(1)}e^{\lambda_1 t} + c_2\vect{x}^{(2)}e^{\lambda_2 t}$$
In this case, there are always two straight lines in the phase space where it is easy to find the direction of the flow.
 
**Ex.** Let $\mat{A} = \begin{pmatrix} -2 & 0 \\ 1 & -1 \end{pmatrix}$. Then the general solution is given by
$$\vect{y} = c_1\begin{pmatrix} 1 \\ -1 \end{pmatrix}e^{-2t} + c_2\begin{pmatrix} 0 \\ 1 \end{pmatrix}e^{-t}$$
Note that if either $c_1, c_2$ are zero, the trajectory is a straight line (as $y_1$ is just a multiple of $y_2$).
i.e. If $c_2 = 0$ then $y_1 = c_1 e^{-2t}$, $y_2 = -c_1 e^{-2t}$ so $y_1 = -y_2$.
If $c_1 = 0$ then $y_1 = 0$, $y_2 = c_2 e^{-?t}$. [the exponent's coefficient is overwritten and unreadable (handwriting, not the photo); from the solution it is $e^{-t}$]
Note we have five different trajectories.
↳ Origin ↳ $y_1 = 0$, $y_2 > 0$
↳ $y_2 = -y_1$ where $y_1 > 0$ or $y_1 < 0$ ↳ $y_1 = 0$, $y_2 < 0$
 
*Figure (the five straight-line trajectories).* Axes $y_1$ (horizontal) and $y_2$ (vertical), unlabelled. Numbered trajectories, each drawn as a dot (initial point) with an arrow towards the origin: (1) in the second quadrant on the dotted line $y_2 = -y_1$, arrow pointing down-right to the origin; (2) in the fourth quadrant on the same dotted line, arrow pointing up-left to the origin; (3) on the positive $y_2$-axis, arrow pointing down; (4) on the negative $y_2$-axis, arrow pointing up; (5) the origin itself (a dot labelled 5).
 
**Right page.**
 
**Ex.** In-between, the trajectories move into the origin, but not along straight lines. In fact, given $\lambda_i < 0$ are distinct, the trajectories approach the origin tangent to the straight line corresponding to the eigenvector of the eigenvalue with least [blacked-out word] magnitude.
 
*Figure (stable improper node for this example).* Axes $y_1$ (horizontal) and $y_2$ (vertical). The $y_2$-axis is overdrawn with a dotted line extending beyond the plot (the eigenvector $(0,1)$, $\lambda = -1$); a dotted diagonal from upper left to lower right is the line $y_2 = -y_1$ (eigenvector $(1,-1)$, $\lambda = -2$). About ten curved trajectories, all with arrows pointing towards the origin: in the upper half they come in from the upper left and upper right and bend to enter the origin tangent to the vertical axis; in the lower half they come in from the lower right (roughly parallel to the dotted diagonal) and from the lower left, again entering tangent to the vertical axis. Two curves cross the $y_1$-axis before turning in (one from the far left curving under the axis, one from the far right curving over it).
 
**Def.** Any system with $\lambda_i < 0$ distinct real provides similar results and is called a *stable (improper) node*.
 
**Rem.** Showing the property discussed above is messy to show in general, but is easier to prove for a system where the eigenvectors are parallel to the axes.
 
## HW 15 — Improper unstable nodes; saddles
_File `20261121_235533.jpg`. Left page headed "~~[blacked out]~~ nodes", with "improper unstable" written underneath; right page "Saddle (nodes)"; both section 2.4._
 
**Left page.**
 
**Def.** What if both eigenvalues are positive?
 
**Ex.** Let $\dot{\vect{y}} = \mat{A}\vect{y}$, $\mat{A} = \begin{pmatrix} 1 & 3 \\ 0 & 2 \end{pmatrix}$, where the general solution is
$$\vect{y} = c_1\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{t} + c_2\begin{pmatrix} 3 \\ 1 \end{pmatrix}e^{2t}.$$
The straight-line solutions are
$c_1 = 0$: $\vect{y} = c_2\begin{pmatrix} 3 \\ 1 \end{pmatrix}e^{2t} \Rightarrow y_1 = 3y_2$
$c_2 = 0$: $\vect{y} = c_1\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{t} \Rightarrow y_2 = 0$
Between these lines the curves are tangent to the straight line corresponding to the eigenvector of the eigenvalue with least magnitude.
 
*Figure (unstable improper node).* Axes $y_1$ (horizontal), $y_2$ (vertical). Along the $y_1$-axis, arrows point away from the origin in both directions. A dotted line through the origin with slope $1/3$ (the line $y_1 = 3y_2$) carries a dot in the first quadrant with an arrow continuing outwards up-right, and a dot in the third quadrant with an arrow outwards down-left. Four curved trajectories leave the origin tangent to the $y_1$-axis and then turn parallel to the dotted line: one rises steeply into the first quadrant (arrow up-right), one goes out low in the first quadrant (arrow right), one S-shaped curve sweeps from the origin down through the fourth quadrant and back across into the third (arrow down-left), and one goes left just below the axis (arrow left). All arrows point away from the origin.
 
**Def.** Any system with distinct real $\lambda_i > 0$ gives similar results and is called an *unstable (improper) node*.
 
**Right page.**
 
**Def.** What if the eigenvalues have differing signs?
 
**Ex.** We examine a simple example where the eigenvectors are scaled basis vectors. Let $\dot{\vect{y}} = \mat{A}\vect{y}$, $\mat{A} = \begin{pmatrix} 2 & 0 \\ 0 & -4 \end{pmatrix}$ so
$$\vect{y} = c_1\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^{2t} + c_2\begin{pmatrix} 0 \\ 1 \end{pmatrix}e^{-4t}$$
 
*Figure (saddle).* Axes $y_1$ (horizontal), $y_2$ (vertical). On the $y_2$-axis, arrows point towards the origin from above and from below. On the $y_1$-axis, arrows point away from the origin to the left and to the right. In each quadrant one hyperbola-like branch (asymptotic to both axes): it comes down (or up) close to the $y_2$-axis and turns away along the $y_1$-axis, with an arrow showing motion from near the vertical axis towards the horizontal one.
 
Also we solve for $y_2$ as a function of $y_1$:
$$\frac{\dd y_2}{\dd y_1} = \frac{-4y_2}{2y_1} \Rightarrow\Rightarrow y_2 = \pm\frac{A}{y_1^2}$$
 
**Def.** Any system with one positive and one negative eigenvalue gives similar results and is called a *saddle (node)*.
 
## HW 16 — Proper nodes; degenerate nodes; zero eigenvalue
_File `20261121_235546.jpg`. Left page "Proper nodes", right page "Degenerate nodes"; both section 2.4 (the left page number is in the gutter)._
 
**Left page.**
 
**Def.** What if the eigenvalues are equal? There may still exist two l.i. eigenvectors.
 
**Ex.** Let $\mat{A} = \mat{I}_2$. Then $\lambda_1 = \lambda_2 = 1$, and the general solution is
$$\vect{y} = c_1\begin{pmatrix} 1 \\ 0 \end{pmatrix}e^t + c_2\begin{pmatrix} 0 \\ 1 \end{pmatrix}e^t \Rightarrow \vect{y} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}e^t$$
 
*Figure (unstable proper node, star).* Axes $y_1$ (horizontal), $y_2$ (vertical). Straight rays from the origin with arrows pointing outwards: up-right, up-left, down-left, down-right (and one more to the lower left). One point in the first quadrant is marked by a dot with dashed lines dropping to the axes, the feet labelled $c_1$ (on the $y_1$-axis) and $c_2$ (on the $y_2$-axis); a dotted segment joins the origin to the dot and the ray continues outwards with an arrow. A second dot on the ray in the third quadrant, joined to the origin by a dotted segment, with an arrow outwards.
 
**Def.** This is called a *proper node* and it is unstable if $\lambda > 0$ and stable if $\lambda < 0$.
 
**Right page.**
 
**Def.** What if there is only one eigenvector?
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 0 & 1 \\ -1 & 2 \end{pmatrix}$. Then $\lambda = 1$, $\vect{x}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, so the solution is $\vect{y} = c\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^t$.
There is only one straight line $\dfrac{y_2}{y_1} = 1$:
 
*Figure (unstable degenerate node).* Axes $y_1$, $y_2$. A dotted line $y_2 = y_1$ through the origin, with a dot on it in each of the first and third quadrants and arrows pointing outwards along the line (up-right and down-left). Several curves, no arrowheads on them: U-shaped curves opening upwards on the left of the $y_2$-axis (one dipping into the third quadrant), arcs bowing to the right in the fourth quadrant, and short strokes parallel to the diagonal in the first quadrant. They suggest trajectories that bend around the origin, leaving parallel to $y_2 = y_1$.
 
**Rem.** [a small square bullet] The trajectories bend around, almost (but not quite) spiralling. Any system with one eigenvector is similar and is called an *inflected/degenerate node*. It is stable if $\lambda < 0$ and unstable if $\lambda > 0$.
 
**Def.** If an eigenvalue is 0, then $\det\mat{A} = 0$. Consequently, $\vect{y} = \vect{0}$ is not the unique solution to $\dot{\vect{y}} = \mat{A}\vect{y} = \vect{0}$.
 
## HW 17 — Zero eigenvalue example; centres
_File `20261121_235557.jpg`. The photo is upside down (rotate 180°). Left page "Degenerate nodes", right page "Complex phase portraits"; both section 2.4._
 
**Left page.** [The heading says "Degenerate nodes" but the example continues the zero-eigenvalue remark at the end of HW 16.]
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 3 & 2 \\ 3 & 2 \end{pmatrix}$.
Then $\lambda_1 = 0$, $\vect{x}^{(1)} = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$; $\lambda_2 = 5$, $\vect{x}^{(2)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. ["5" is written over another digit]
The solution is $\vect{y} = c_1\begin{pmatrix} 2 \\ -3 \end{pmatrix} + c_2\begin{pmatrix} 1 \\ 1 \end{pmatrix}e^{5t}$.
 
*Figure (zero eigenvalue: a line of critical points).* Axes $y_1$, $y_2$. A dotted line through the origin with slope $-3/2$ (the eigenvector $(2,-3)$: every point on it is a critical point; one point on it in the fourth quadrant is marked with a dot). Three parallel straight lines of slope $1$ (direction $(1,1)$), each crossing the dotted line, with arrowheads at both ends pointing away from the dotted line (up-right and down-left).
 
It can be seen that the phase portrait consists of a collection of linear equations.
 
**Right page.**
 
**Def.** We will prove that if the eigenvalues are purely imaginary, that the trajectories are ellipses. ["are" written above a blacked-out word]
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 0 & 1 \\ -2 & 0 \end{pmatrix}$. Then $\dot{y}_1 = y_2$ and $\dot{y}_2 = -2y_1$.
$$\frac{\dot{y}_2}{\dot{y}_1} = \frac{-2y_1}{y_2} \Rightarrow\Rightarrow y_1^2 + \tfrac{1}{2}y_2^2 = c$$
 
*Figure (centre).* Axes $y_1$, $y_2$. Two concentric dashed ellipses centred at the origin, elongated along the $y_2$-axis (taller than wide). On the left halves, small arrows point upwards; on the right halves, arrows point downwards (clockwise motion).
 
We then determine the direction of flow. Consider the sign of $\dot{y}_1$ when $y_2 > 0$. We can see that $y_2 = \dot{y}_1$ is increasing and thus the system flows 'clockwise'.
[possible error: when $y_2 > 0$, $\dot y_1 = y_2 > 0$, so it is $y_1$ that is increasing.]
 
**Def.** Any system with purely imaginary eigenvalues is called a *CENTRE*, and has elliptical trajectories.
 
## HW 18 — Spirals
_File `20261121_235635.jpg`. Both pages "Spirals", section 2.4._
 
**Left page.**
 
**Def.** If the eigenvalues are complex with nonzero real part, then the trajectories either:
↳ Spiral in (real part $(-)$)
↳ Spiral out (real part $(+)$)
To prove this in general requires diagonalisation, but it can easily be demonstrated below.
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}$. Then $\lambda_1 = 2 + i$, $\lambda_2 = 2 - i$ and solution
$$\vect{y} = c_1\begin{pmatrix} e^{2t}\cos t \\ e^{2t}\sin t \end{pmatrix} + c_2\begin{pmatrix} e^{2t}\sin t \\ -e^{2t}\cos t \end{pmatrix}$$
Thus (let $c_1 = 1$, $c_2 = 0$), we have that $y_1^2 + y_2^2 = e^{4t}$ (logarithmic spiral)
In polar coordinates:
$$r(t) = \sqrt{y_1^2 + y_2^2} = e^{2t} \quad \text{[spiral out]}, \qquad \theta(t) = \arctan(y_2/y_1) = t, \qquad \dot{\theta}(t) = 1 > 0 \quad \text{[anti-clockwise]}$$
 
*Figure (unstable spiral).* Labelled "from $\dot\theta$". Axes through the origin; a spiral starting at the origin and winding outwards anticlockwise for about two turns, with an arrowhead on the outer turn in the upper left showing anticlockwise motion.
 
**Right page.**
 
**Def.** For a more exact illustration we can use the slope of the trajectories as a guide.
 
**Ex.** Take
$$\frac{\dot{y}_2}{\dot{y}_1} = \frac{y_1 + 2y_2}{2y_1 - y_2}.$$
We find the nullclines:
$$\dd y_2 = y_1 + 2y_2 = 0 \Rightarrow y_2 = -\tfrac{1}{2}y_1,\ \frac{\dd y_2}{\dd y_1} = 0; \qquad \dd y_1 = 2y_1 - y_2 = 0 \Rightarrow y_2 = 2y_1,\ \frac{\dd y_2}{\dd y_1} \to \infty.$$
 
*Figure (direction field with nullclines for the spiral).* Axes $y_1$, $y_2$. Annotations: "$y_2 = 0 \Rightarrow \frac{\dd y_2}{\dd y_1} = \frac{1}{2}$" next to the $y_1$-axis and "$y_1 = 0 \Rightarrow \frac{\dd y_2}{\dd y_1} = -2$" next to the $y_2$-axis. Short slope marks of slope $1/2$ are drawn across the $y_1$-axis, and of slope $-2$ across the $y_2$-axis. A dotted line through the second and fourth quadrants (the nullcline $y_2 = -\frac12 y_1$) carries short horizontal marks; a dotted steep line through the first and third quadrants (the nullcline $y_2 = 2y_1$) carries short vertical arrows (pointing up in the first quadrant, down in the third). Two or three trajectory curves wind anticlockwise outwards around the origin with arrowheads. [The drawing is cluttered (overlapping strokes); it is legible enough to redraw from the nullclines and slopes stated, but not stroke by stroke. This is the drawing, not the photo.]
 
Thus we have a more detailed idea of the slope trajectories at certain points.
 
**Def.** A system of complex eigenvalues is called a *spiral*, and has:
↳ Spiralling out (unstable) if real part is positive
↳ Spiralling in (stable) if real part is negative
We can treat centres as a special case where the real part is zero.
 
## HW 19 — Critical points; stability of critical points (trace and determinant)
_File `20261121_235649.jpg`. Left page "Critical points", right page "Stability of critical points"; both section 2.5. Lower third of both pages blank._
 
**Left page.**
 
**Def.** A *critical point* occurs when $\dot{\vect{y}} = \vect{0}$. In other words,
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} f_1(y_1, y_2) \\ f_2(y_1, y_2) \end{pmatrix}$$
has a critical point if $f_1(y_1^*, y_2^*) = 0$ and $f_2(y_1^*, y_2^*) = 0$.
 
**Rem.** The trivial solution is a critical point as $\vect{y} = \vect{0} \Rightarrow \dot{\vect{y}} = \vect{0}$.
 
**Def.** Non-linear systems may have more than one critical point. Take $\dot{\vect{y}} = \begin{pmatrix} y_1 - y_2^2 \\ y_2 - y_1 y_2 \end{pmatrix}$.
Then $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and $\begin{pmatrix} -1 \\ -1 \end{pmatrix}$ are all critical points.
[possible error: $(-1, -1)$ gives $y_1 - y_2^2 = -2 \ne 0$; the third critical point is $(1, -1)$.]
 
**Def.** Linear systems (i.e. $\dot{\vect{y}} = \mat{A}\vect{y}$) only has one critical point at the origin.
[possible error: only when $\det\mat A \ne 0$; HW 16–17 show a whole line of critical points when $\det\mat A = 0$.]
 
**Right page.**
 
**Ex.** The linear pendulum (see 3B1B) is a good model. The differential equation modelling its motion has two critical points:
↳ At rest (stable, perturbations return to rest)
↳ Vertically above (unstable, perturbations cause pendulum to swing until rest)
We can see that critical points can either be STABLE or UNSTABLE.
 
**Def.** To assess the stability of a critical point we examine the trace and the determinant. The eigenvalues of $\mat{A}$ determine stability:
$$\det(\mat{A} - \lambda\mat{I}) = \begin{vmatrix} a_{11} - \lambda & a_{12} \\ a_{21} & a_{22} - \lambda \end{vmatrix} = \lambda^2 - \tr(\mat{A})\lambda + \det\mat{A}$$
which is a quadratic in $\lambda$. Thus
$$\lambda_{\pm} = \frac{\tr\mat{A} \pm \sqrt{(\tr\mat{A})^2 - 4\det\mat{A}}}{2}$$
[the notes write "Tr"; `\tr` is used here]
 
**Def.** If $\det\mat{A} > 0$ and $(\tr\mat{A})^2 - 4\det\mat{A} < 0$ then the eigenvalues are complex conjugates.
 
## HW 20 — Stability criteria for critical points; examples; stability chart
_File `20261121_235658.jpg`. Left page "Stability criteria for critical points", right page "Examples on stability criteria"; both section 2.5. $\Delta$ (not defined on the page) is the discriminant $(\tr\mat A)^2 - 4\det\mat A$ from HW 19._
 
**Left page.**
 
**Def.** If $\det\mat{A} < 0$, the eigenvalues are real and of opposite sign. Thus $\vect{0}$ is a saddle.
If $\det\mat{A} > 0$ and $\Delta > 0$, the eigenvalues are real and:
↳ $\tr\mat{A} > 0 \Rightarrow \lambda_1, \lambda_2 > 0 \Rightarrow$ unstable node
↳ $\tr\mat{A} < 0 \Rightarrow \lambda_1, \lambda_2 < 0 \Rightarrow$ stable node
If $\det\mat{A} > 0$ and $\Delta < 0$, the eigenvalues are complex conjugates and:
↳ $\tr\mat{A} > 0 \Rightarrow \operatorname{Re}(\lambda_i) > 0 \Rightarrow$ unstable spiral
↳ $\tr\mat{A} < 0 \Rightarrow \operatorname{Re}(\lambda_i) < 0 \Rightarrow$ stable spiral
If $\det\mat{A} > 0$ and $\Delta = 0$, the eigenvalues $\lambda_{1,2} = \frac{1}{2}\tr\mat{A}$
↳ If two l.i. eigenvectors, then proper
↳ If one eigenvector, then degenerate
If $\det\mat{A} > 0$ and $\tr\mat{A} = 0$, the eigenvalues $\lambda_{1,2} = \pm i\sqrt{\det\mat{A}} \Rightarrow$ centre
If $\det\mat{A} = 0$: there is one eigenvalue $\lambda = 0$.
 
**Right page.**
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 2 & -1 \\ 3 & -2 \end{pmatrix}$. Then $\tr\mat{A} = 0$ and $\det\mat{A} = -1 < 0$. Thus the crit. point is a saddle.
 
**Ex.** Let $\mat{A} = \begin{pmatrix} 2 & 3 \\ 2 & 5 \end{pmatrix}$. Then $\tr\mat{A} = 7$ and $\det\mat{A} = 4 > 0$. $\Delta = 49 - 16 > 0$. Thus the crit point is an unstable proper node.
[possible error: $\Delta > 0$ gives two distinct positive eigenvalues, i.e. an unstable *improper* node (left page); a proper node needs $\Delta = 0$.]
 
**Ex.** Let $\mat{A} = \begin{pmatrix} -2 & 1 \\ -6 & 2 \end{pmatrix}$. Then $\tr\mat{A} = 0$ and $\det\mat{A} = 2 > 0$. Thus the crit. point is a centre.
 
**Def.** Stability chart
 
*Figure (trace–determinant stability chart).* Horizontal axis "$\tr\mat A$ (expand)" with an arrow to the right; its left end is labelled "$\lambda = 0$". Vertical axis "$\det\mat A$ (orientation)" with an arrow upwards. A dashed parabola through the origin opening upwards (the curve $\Delta = 0$, i.e. $\det\mat A = \frac14(\tr\mat A)^2$). Labels: "Im" just inside the parabola's left arm and "Re" just outside it (complex eigenvalues inside, real outside). Regions, each with a small icon: "stable node" (left, outside the parabola, above the axis); "stable focus" (left, inside, with a small spiral icon winding in); "centre" on the positive $\det\mat A$ axis (concentric-circles icon); "unstable focus" (right, inside, spiral icon winding out); "unstable node" (right, outside); "saddle" below the horizontal axis on the vertical axis (an X-shaped saddle icon).
 
## HW 21 — Non-homogeneous linear systems; non-linear systems: solving for phase curves
_File `20261121_235705.jpg`. Left page "Non-homogenous linear systems", right page "Non-linear systems"; both numbered 2.6 [in CN, non-linear systems are §2.7]._
 
**Left page.**
 
**Def.** A non-homogenous linear system is given in the form $\dot{\vect{y}} = \mat{A}\vect{y} + \vect{g}$ where $\vect{g} \in \R^n$.
They are simply a linear translation away from their homogenous counterpart.
The critical point is given by
$$\vect{y}^* = \begin{pmatrix} y_1^* \\ y_2^* \end{pmatrix} = -\mat{A}^{-1}\vect{g} \equiv \mat{A}\cdot\vect{y}^* + \vect{g} = \vect{0}$$
It follows that if we set
$$\begin{cases} p = y_1 - y_1^* \\ q = y_2 - y_2^* \end{cases} \Leftrightarrow \begin{cases} y_1 = p + y_1^* \\ y_2 = q + y_2^* \end{cases} \Rightarrow \begin{cases} \dot{p} = \dot{y}_1 \\ \dot{q} = \dot{y}_2 \end{cases}$$
then
$$\begin{pmatrix} \dot{p} \\ \dot{q} \end{pmatrix} = \begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \mat{A}\vect{y} + \vect{g} = \mat{A}\left(\begin{bmatrix} p \\ q \end{bmatrix} + \begin{bmatrix} y_1^* \\ y_2^* \end{bmatrix}\right) + \vect{g} = \mat{A}\begin{pmatrix} p \\ q \end{pmatrix} + \mat{A}\vect{y}^* + \vect{g} = \mat{A}\begin{pmatrix} p \\ q \end{pmatrix} + (-\vect{g}) + \vect{g} = \mat{A}\begin{pmatrix} p \\ q \end{pmatrix}$$
 
**Right page.**
 
**Def.** Consider the general 2D system
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} f_1(y_1, y_2) \\ f_2(y_1, y_2) \end{pmatrix}$$
where $f_i$ are nonlinear functions of $y_i$.
 
**Def.** In some cases you can still solve for phase curves.
 
**Ex.** Consider the non-linear system $\ddot{\theta} = -\frac{g}{\ell}\sin\theta$. Letting $y_1 = \theta$ and $y_2 = \dot{\theta}$:
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} y_2 \\ -\frac{g}{\ell}\sin(y_1) \end{pmatrix}$$
By the chain rule:
$$\frac{\dd y_2}{\dd y_1} = \frac{-g/\ell\,\sin(y_1)}{y_2} \Leftrightarrow \int y_2 \dd y_2 = \frac{-g}{\ell}\int \sin y_1 \dd y_1$$
and solving for $y_2$:
$$y_2 = \pm\sqrt{\frac{g}{\ell}\cos y_1 + c}$$
[possible error: $\frac12 y_2^2 = \frac{g}{\ell}\cos y_1 + c$ gives $y_2 = \pm\sqrt{\frac{2g}{\ell}\cos y_1 + C}$; the factor 2 is missing.]
This is easier to sketch using a computer. Looking at the graph, there seem to be critical points at $y_1 = n\pi$, $y_2 = 0$. They seem to alternate between saddle and center (what does this correspond to in a pendulum's motion?)
[no graph is drawn in the notes]
 
**Ex.** Another system where you can solve for the phase curves is the predator–prey model. See MATH1072.
 
## HW 22 — Critical points for non-linear systems; linearisation
_File `20261121_235712.jpg`. Left page "Critical points for non-linear systems", right page "Linearisation of non-linear systems"; both section 2.7._
 
**Left page.**
 
**Def.** As defined before, a critical point of a non-linear system $\dot{\vect{y}} = \vect{f}(\vect{y})$ is where $\dot{\vect{y}} = \vect{0} \Rightarrow \vect{f}(\vect{y}^*) = \vect{0}$.
This generally results in non-linear equations to solve for the critical points.
 
**Ex.** Take the non-linear pendulum again.
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} f_1(y_1, y_2) \\ f_2(y_1, y_2) \end{pmatrix} = \begin{pmatrix} y_2 \\ -\sin y_1 \end{pmatrix}$$
Critical point occur where $f_1(y_1, y_2) = y_2 = 0$, $f_2(y_1, y_2) = -\sin y_1 = 0 \Rightarrow y_1 = n\pi$, $n \in \Z$.
 
**Ex.** Take the Lotka–Volterra predator prey model.
$$\begin{pmatrix} \dot{r} \\ \dot{f} \end{pmatrix} = \begin{pmatrix} 2r - rf \\ rf - f \end{pmatrix}$$
Critical points must satisfy $2r - rf = 0$ AND $rf - f = 0$
From (1): $r = 0$, $f = 0$
From (2): $f = 2$, $r = 1$
 
**Right page.**
 
**Def.** A general method for finding the linearised system (approximation) about the critical point of a non-linear system is provided by Taylor series. We can thus determine the nature of the system (locally) about any critical point.
Suppose $(y_1^*, y_2^*)$ is a critical point of
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} f_1(y_1, y_2) \\ f_2(y_1, y_2) \end{pmatrix}$$
Then $f_1(y_1^*, y_2^*) = 0$ and $f_2(y_1^*, y_2^*) = 0$, and by Taylor series:
$$\begin{aligned} \dot{y}_1 = f_1(y_1, y_2) &\approx f(y_1^*, y_2^*) + \left.\frac{\partial f_1}{\partial y_1}\right|_{y_1^*, y_2^*}(y_1 - y_1^*) + \left.\frac{\partial f_1}{\partial y_2}\right|_{y_1^*, y_2^*}(y_2 - y_2^*) \\ &\approx \left.\frac{\partial f_1}{\partial y_1}\right|_{y_1^*, y_2^*}(y_1 - y_1^*) + \left.\frac{\partial f_1}{\partial y_2}\right|_{y_1^*, y_2^*}(y_2 - y_2^*) \end{aligned}$$
and similarly for $\dot{y}_2$.
The linearised system at $(y_1^*, y_2^*)$ is thus
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} \partial f_1/\partial y_1 & \partial f_1/\partial y_2 \\ \partial f_2/\partial y_1 & \partial f_2/\partial y_2 \end{pmatrix}\begin{pmatrix} \bar{y}_1 \\ \bar{y}_2 \end{pmatrix}$$
Note that $\dot{\bar{y}}_1 = \dot{y}_1$ and $\dot{\bar{y}}_2 = \dot{y}_2$, so we can convert this to matrix form:
$$\dot{\bar{\vect{y}}} = \frac{\partial\vect{f}}{\partial\vect{y}}\bar{\vect{y}} \qquad \text{where } \frac{\partial\vect{f}}{\partial\vect{y}} \text{ is the Jacobian at } y_1^*, y_2^*$$
[$\bar y_i = y_i - y_i^*$ is implied, not stated. "$f(y_1^*, y_2^*)$" in the first line should be $f_1$.]
 
## HW 23 — Linearisation examples: non-linear pendulum, Lotka–Volterra
_File `20261121_235720.jpg`. Both pages "Linearisation", section 2.7. Lower half of both pages blank._
 
**Left page.**
 
**Ex.** Again consider the non-linear pendulum
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} y_2 \\ -\sin y_1 \end{pmatrix}, \qquad \frac{g}{\ell} = 1$$
The linearised matrix (Jacobian) is
$$J_f(y_1, y_2) = \begin{pmatrix} \partial f_1/\partial y_1 & \partial f_1/\partial y_2 \\ \partial f_2/\partial y_1 & \partial f_2/\partial y_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -\cos y_1 & 0 \end{pmatrix}$$
[possible error: the indices in the general matrix are miswritten in the notes: the entries read $\partial f_1/\partial y_1$, $\partial f_{?}/\partial y_{?}$ (the subscripts are smudged/overwritten), $\partial f_2/\partial y_2$, $\partial f_2/\partial y_2$. The numerical matrix is the correct Jacobian.]
For the critical point at $(\pi, 0)$:
$$J_f(\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \to \tr J_f = 0,\ \det J_f = -1$$
In terms of the variables $\bar{y}_1 = y_1 - \pi$, $\bar{y}_2 = y_2$, the linearised system is
$$\begin{pmatrix} \dot{\bar{y}}_1 \\ \dot{\bar{y}}_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} \bar{y}_1 \\ \bar{y}_2 \end{pmatrix} \to \text{saddle}$$
[the second component on the left is written $\dot{\bar y}_1$; it should be $\dot{\bar y}_2$]
 
**Right page.**
 
**Ex.** Again consider the Lotka–Volterra model
$$\begin{pmatrix} \dot{r} \\ \dot{f} \end{pmatrix} = \begin{pmatrix} 2r - rf \\ rf - f \end{pmatrix}$$
The Jacobian is
$$J_f(y_1, y_2) = \begin{pmatrix} \partial f_1/\partial y_1 & \partial f_1/\partial y_2 \\ \partial f_2/\partial y_1 & \partial f_2/\partial y_2 \end{pmatrix} = \begin{pmatrix} 2 - f & -r \\ f & r - 1 \end{pmatrix}$$
For the critical point at $(r, f) = (0, 0)$:
$$J_f(0, 0) = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix} \to \tr J_f = -2 \ (\text{or } \lambda_1 = 2,\ \lambda_2 = -1) \to \text{saddle}$$
[possible error: $\tr J_f(0,0) = 2 + (-1) = 1$; $\det = -2$. The conclusion (saddle) is right.]
For the critical point at $(r, f) = (1, 2)$:
$$J_f(1, 2) = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} \to \tr J_f = 0,\ \det J_f = 2 \to \text{centre}$$
 
## HW 24 — Linearisation: damped pendulum; special cases where linearisation fails
_File `20261121_235733.jpg`. Both pages "Linearisation", section 2.7._
 
**Left page.**
 
**Ex.** Now consider the damped non-linear pendulum with $g/\ell = 1$, damping constant $c$. In this example we do not have integral curves.
 
**Rem.** In general you cannot solve for integral curves, but you can solve for the critical points.
 
**Ex.** Let $y_1 = \theta$ and $y_2 = \dot{\theta}$
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} y_2 \\ -\sin y_1 - cy_2 \end{pmatrix}$$
The critical points are at $(n\pi, 0)$. The Jacobian is given by
$$J_f = \begin{pmatrix} \partial f_1/\partial y_1 & \partial f_1/\partial y_2 \\ \partial f_2/\partial y_1 & \partial f_2/\partial y_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -\cos y_1 & -c \end{pmatrix}$$
$$J_f(0, 0) = \begin{pmatrix} 0 & 1 \\ -1 & -c \end{pmatrix} \to \tr J_f = -c,\ \det J_f = 1; \qquad J_f(\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & -c \end{pmatrix} \to \tr J_f = -c,\ \det J_f = -1$$
As $\det J_f$ and $\tr J_f \ne 0$ in both cases, so the non-linear system will have stable spiral/node at $(2n\pi, 0)$ and saddle at $((2n-1)\pi, 0)$.
Note that this information is only <u>local</u> to the critical points.
 
**Right page.**
 
In this case, we can use energy considerations to prove the resulting 'picture'/dynamics are qualitatively correct.
 
**Rem.** In most cases, the linearised system (local approx.) is topologically consistent/equivalent to non-linear flow in some neighbourhood of the critical point. There are TWO SPECIAL CASES where the linearised systems gives flows that are not similar to the non-linear flow (even locally!)
↳ $\det\mat{A} = 0$
↳ $\tr\mat{A} = 0$, $\det\mat{A} > 0$ (centre)
 
**Ex.** Let
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} + \begin{pmatrix} y_1(y_1^2 + y_2^2) \\ y_2(y_1^2 + y_2^2) \end{pmatrix}$$
The linearised system gives a centre ($\tr\mat{A} = 0$, $\det\mat{A} > 0$) but the full non-linear system actually (slowly) spiral out.
This can be proven by taking polar coordinates as $y_1 = r\cos\theta$, $y_2 = r\sin\theta$ and calculating $\dot{r}$ from $r^2 = y_1^2 + y_2^2$.
 
## HW 25 — Non-linear system: competing species model
_File `20261121_235740.jpg`. Both pages "Non-linear system: competing species model", section 2.7. Lower half of the right page blank._
 
**Left page.**
 
**Ex.** Suppose $x, y$ are the populations of two species which compete for food. Then WLOG, without $x$, $y$ would grow exponentially i.e. $\dot{y} = r_2 y$. As both compete for the same food source, their growth rates decrease proportionally to the product of $x$ and $y$. Therefore,
$$\dot{x} = r_1 x - s_1 xy, \qquad \dot{y} = r_2 y - s_2 xy$$
Suppose all coefficients are 1. Then,
$$\begin{pmatrix} \dot{x} \\ \dot{y} \end{pmatrix} = \begin{pmatrix} x - xy \\ 4y - xy \end{pmatrix} \quad (r_2 = 4)$$
[i.e. all coefficients are 1 except $r_2 = 4$]
The critical points are given by:
$\dot{x} = 0 \Rightarrow x = 0$ or $y = 1$; [arrows down to] $y = 0$ [under $x = 0$] and $x = 4$ [under $y = 1$].
The linearised matrix/Jacobian is given by:
$$J_f(x, y) = \begin{pmatrix} 1 - y & -x \\ -y & 4 - x \end{pmatrix}$$
$$J_f(0, 0) = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix} \to \lambda_1 = 1,\ \lambda_2 = 4;\ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
↳ unstable improper node, fast eigendirection $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$
$$J_f(4, 1) = \begin{pmatrix} 0 & -4 \\ -1 & 0 \end{pmatrix} \to \tr\mat{A} = 0,\ \det\mat{A} = -4 < 0;\ \lambda_1 = 2,\ \lambda_2 = -2;\ \vect{x}^{(1)} = \begin{pmatrix} 2 \\ -1 \end{pmatrix},\ \vect{x}^{(2)} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
↳ saddle
 
**Right page.**
 
**Ex.** As $\det\mat{A} \ne 0$ and $\tr\mat{A} \ne 0$, the local approximation given by the linearised systems is accurate. We can also prove that there are no limit cycles or misc. complicated behaviour and so we can put the whole picture together.
[possible error: at the saddle $(4, 1)$, $\tr\mat A = 0$ (left page). Linearisation is still valid there because $\det\mat A \ne 0$ and the point is a saddle, not a centre; HW 24 lists the failing cases as $\det\mat A = 0$ or "$\tr\mat A = 0$, $\det\mat A > 0$".]
 
*Figure (competing-species phase portrait, first quadrant).* Axes $x$ (horizontal) and $y$ (vertical), first quadrant only. The origin is marked with a cross (unstable node), with arrows pointing away from it along both axes. The saddle at $(4, 1)$: a dashed horizontal line from the $y$-axis at height 1 to the saddle (the nullcline $y = 1$) and a short dashed vertical line below the saddle down to the $x$-axis (the nullcline $x = 4$). Through the saddle, a straight line from upper left to lower right (direction $(2,-1)$, unstable) with arrows pointing away from the saddle (up-left and down-right), and a line from lower left to upper right (direction $(2,1)$, stable) with arrows pointing towards the saddle. The stable line continues down to the left as a dashed curve that ends at the origin: the heteroclinic trajectory from the origin to the saddle. Other trajectories: near the $y$-axis, curves leave the origin and rise (arrows up); above the unstable line, curves run up-left parallel to it; to the right, curves come in from the upper right towards the saddle and turn off along the unstable line (one turning up-left, one turning down-right); below the saddle, a small arc with an arrow to the right; a curve near the $x$-axis rises to the right (arrow) towards the saddle.
 
**Rem.** The *heteroclinic trajectory* joins two critical points. In this diagram it is given by another dotted line.
 
## HW 26 — Summary of non-linear systems
_File `20261121_235748.jpg`. Left page "Summary of non-linear systems", section 2.7. The right page is blank._
 
**N.** [a label "N." in the margin]
(1) If the phase curves from
$$\frac{\dd y_2}{\dd y_1} = \frac{f_2(y_1, y_2)}{f_1(y_1, y_2)}$$
are solvable, do so and sketch the phase curves (either as $y_2(y_1)$, or as some contours of some $f(y_1, y_2)$)
(2) If the phase curves are not solvable, find the critical points and investigate their TYPE and STABILITY and sketch on the phase portrait.
(a) Critical points: solve $(y_1^*, y_2^*)$ from $f_1(y_1^*, y_2^*) = 0$ and $f_2(y_1^*, y_2^*) = 0$
(b) Type and stability: find Jacobian, evaluate at critical points
(c) Classify critical point: calculate $\det\mat{A}$, $\tr\mat{A}$ and recall stability chart
(d) Sketch flow near critical points:
↳ If node/saddle, find eigenvalues + vectors, sketch straight-line traj. and direction of flow
↳ If spiral, find stability and direction of flow

# MATH2100 Applied Mathematical Analysis (MATH2010 ODEs + MATH2011 PDEs): transcription, part 2 of 5 (HW 27–44)
 
_Transcription phase. Nothing here is book text yet. Sources, legibility check and conventions: see part 1 (`claude/notes-math2100-1.md`)._
 
**This part:** Laplace transforms: definition and basic transforms, shifting theorems, inversion, partial fractions (four cases), derivatives and solving ODEs and systems, transfer functions, the Gamma function, convolution, periodic functions. "CN §" = CN-ODE.
 
---
 
## HW 27 — Introduction to Laplace transforms: definition, constants, powers, exponentials
_File `20261121_235754.jpg`. Both pages "Introduction to Laplace transforms", section 3.1. The notes' "P." means proof._
 
**Left page.**
 
**N.** The Laplace transform is an integral transform. We use Laplace transforms to convert differential equations to algebraic equations.
 
**Def.** Let $f(t)$ be a function where $t > 0$. Define the Laplace transform by
$$\mathcal{L}(f(t))(s) = F(s) = \int_0^\infty f(t)e^{-st}\dd t$$
 
**Def.** Laplace transform of constant:
$$\mathcal{L}(c)(s) = \frac{c}{s}$$
**P.** Let
$$\int_0^\infty k e^{-st}\dd t = k\lim_{n\to\infty}\int_0^n e^{-st}\dd t = k\lim_{n\to\infty}\left.\frac{-e^{-st}}{s}\right|_0^n = k/s$$
Note we assume that $e^{-st} \to 0$ as $n \to \infty$, which is true if $\operatorname{Re}(s) > 0$. [read: $e^{-sn} \to 0$; the constant is $c$ in the statement and $k$ in the proof]
 
**Right page.**
 
**Def.** Laplace transform for power $t^n$:
$$\mathcal{L}(t^n)(s) = \frac{n!}{s^{n+1}}, \qquad n \in \Z$$
[possible error: needs $n \ge 0$ ($n \in \N_0$), not $n \in \Z$.]
**P.**
$$\int_0^\infty t^n e^{-st}\dd t = \left.\frac{t^n e^{-st}}{-s}\right|_0^\infty + \int_0^\infty nt^{n-1}\frac{e^{-st}}{s}\dd t = 0 + \frac{n}{s}\int_0^\infty t^{n-1}e^{-st}\dd t = \frac{n}{s}F_{n-1}(s) = \dots = \frac{n!}{s^{n+1}}$$
 
**Def.** Laplace transform for exponential $e^{at}$:
$$\mathcal{L}(e^{at}) = \frac{1}{s - a}$$
**P.**
$$\int_0^\infty e^{at}e^{-st}\dd t = \int_0^\infty e^{-(s-a)t}\dd t = \left.\frac{e^{-(s-a)t}}{-(s-a)}\right|_0^\infty = \frac{1}{s - a} \quad \text{if } s > a$$
 
## HW 28 — Linearity; sine and cosine; step functions
_File `20261121_235801.jpg`. Both pages "Introduction to Laplace transforms", section 3.1. Lower third of both pages blank._
 
**Left page.**
 
**Def.** The Laplace transform is linear: if $f(t) = ag(t) + bh(t)$ then
$$F(s) = \int_0^\infty \bigl(ag(t) + bh(t)\bigr)e^{-st}\dd t = \dots \text{ (by linearity of integral)} = aG(s) + bH(s)$$
 
**Def.** Laplace transform for sine, cosine
$$\mathcal{L}(\cos\alpha t) = \frac{s}{s^2 + \alpha^2}, \qquad \mathcal{L}(\sin\alpha t) = \frac{\alpha}{s^2 + \alpha^2}$$
**P.** Consider $e^{i\alpha t} = \cos(\alpha t) + i\sin(\alpha t)$. Then
$$\mathcal{L}(e^{i\alpha t}) = \frac{1}{s - i\alpha} = \frac{s + i\alpha}{s^2 + \alpha^2} = \frac{s}{s^2 + \alpha^2} + i\frac{\alpha}{s^2 + \alpha^2}$$
 
**Right page.**
 
**Def.** We consider the Laplace transform for piecewise continuous functions. Consider the step function
$$u(t - k) = \begin{cases} 0 & 0 \le t < k \\ 1 & t \ge k \end{cases}$$
The Laplace transform is given by:
$$\mathcal{L}\bigl(u(t - k)\bigr) = \int_k^\infty e^{-st}\dd t = \frac{e^{-ks}}{s}$$
Suppose the step is down – then:
$$\mathcal{L}\bigl(1 - u(t - k)\bigr) = \frac{1}{s} - \frac{e^{-ks}}{s}$$
or up and down – then:
$$\mathcal{L}\bigl(u(t - a) - u(t - b)\bigr) = \frac{e^{-as}}{s} - \frac{e^{-bs}}{s}$$
Lastly consider this more complicated example:
$$f(t) = \begin{cases} 1 & 0 \le t < 3 \\ 2 & 3 \le t < 4 \\ 0 & t \ge 4 \end{cases}$$
Then the Laplace transform is given by:
$$f(t) = 1 + u(t - 3) - 2u(t - 4), \qquad F(s) = \frac{1}{s} + \frac{e^{-3s}}{s} - 2\frac{e^{-4s}}{s}$$
 
## HW 29 — The first shifting theorem
_File `20261121_235807.jpg`. Both pages "The first shifting theorem", section 3.1. Right page mostly blank._
 
**Left page.**
 
**Def.** We define the first shifting theorem:
$$\text{if } \mathcal{L}(f(t)) = F(s) \text{ then } \mathcal{L}\bigl(e^{at}f(t)\bigr) = F(s - a)$$
Therefore, if the Laplace transform of $f(t)$ is known, we can find the Laplace transform of $e^{at}f(t)$ without needing to 'integrate'.
 
**Ex.**
For $f(t) = e^{at}t^n$, $\mathcal{L}(f(t)) = \dfrac{n!}{(s - a)^{n+1}}$
For $f(t) = e^{at}\cos(\alpha t)$, $\mathcal{L}(f(t)) = \dfrac{s - a}{(s - a)^2 + \alpha^2}$
For $f(t) = e^{at}\sin(\alpha t)$, $\mathcal{L}(f(t)) = \dfrac{\alpha}{(s - a)^2 + \alpha^2}$
For $f(t) = e^{at}u(t - k)$, $\mathcal{L}(f(t)) = \dfrac{e^{-k(s-a)}}{s - a}$
 
**Right page.**
 
**Ex.** Consider $f(t) = 5e^{3t}\cos(2t) + 4t^3e^{-5t}$. Then,
$$F(s) = 5\mathcal{L}\bigl(e^{3t}\cos(2t)\bigr) + 4\mathcal{L}(t^3e^{-5t}) = 5 \times \frac{s - 3}{(s - 3)^2 + 4} + 4 \times \frac{6}{(s + 5)^4} = \frac{5(s - 3)}{(s - 3)^2 + 4} + \frac{24}{(s + 5)^4}$$
by the first shifting theorem.
 
## HW 30 — Inverting Laplace transforms
_File `20261121_235814.jpg`. Both pages "Inverting Laplace transforms", section 3.1._
 
**Left page.**
 
**Def.** We first consider the inverse of a power, or a shifted power.
$$\mathcal{L}^{-1}\left(\frac{1}{(s - a)^n}\right) = e^{at}\frac{t^{n-1}}{(n - 1)!}$$
 
**Ex.** If $F(s) = 5(s + 10)^{-2}$ then
$$\mathcal{L}^{-1}(F(s)) = 5 \cdot \frac{t^1}{1!}e^{-10t} = 5te^{-10t}$$
 
**Def.** The inverse of a function with irreducible quadratic denominator.
$$\mathcal{L}^{-1}\left(\frac{bs + c}{s^2 + \alpha^2}\right) = b\mathcal{L}^{-1}\left(\frac{s}{s^2 + \alpha^2}\right) + \frac{c}{\alpha}\mathcal{L}^{-1}\left(\frac{\alpha}{s^2 + \alpha^2}\right) = b\cos\alpha t + \frac{c}{\alpha}\sin\alpha t$$
 
**Ex.** If $F(s) = \dfrac{5s - 2}{s^2 + 4}$ then $f(t) = 5\cos(2t) + -1\sin(2t)$
 
**Ex.** If $F(s) = \dfrac{3}{(s - 4)^3} + \dfrac{6}{s^2 + 9}$ then
$$f(t) = 3\mathcal{L}^{-1}\left(\frac{1}{(s - 4)^3}\right) + 2\mathcal{L}^{-1}\left(\frac{3}{s^2 + 3^2}\right) = \frac{3e^{4t}t^2}{2!} + 2\sin 3t$$
[a small blacked-out mark before the "2"]
 
**Right page.**
 
**Def.** We can use partial fractions to find inverses. Recall that
$$\frac{A}{s - b} + \frac{B}{s - c} = \frac{(A + B)s - Ac - Bb}{(s - b)(s - c)}$$
Therefore, if $P_1(x)$ is a polynomial of degree 1,
$$\mathcal{L}^{-1}\left(\frac{P_1(s)}{(s - b)(s - c)}\right) = \mathcal{L}^{-1}\left(\frac{A}{s - b} + \frac{B}{s - c}\right) = Ae^{bt} + Be^{ct}$$
 
**Ex.** If $F(s) = \dfrac{6}{s(s + 2)}$ then
$$\mathcal{L}^{-1}\left(\frac{6}{s(s + 2)}\right) = \mathcal{L}^{-1}\left(\frac{3}{s} - \frac{3}{s + 2}\right) = 3 - 3e^{-2t}$$
 
## HW 31 — Laplace transform of $t^\alpha$ (Gamma function); well-definedness
_File `20261121_235820.jpg`. Left page "Laplace transform of $\mathcal{L}(t^\alpha)$," followed by a blacked-out word; right page "Well-definedness of Laplace transforms"; both section 3.1. Right page mostly blank._
 
**Left page.**
 
**Def.** Recall that for $n \in \Z$: $\mathcal{L}(t^n)(s) = \dfrac{n!}{s^{n+1}}$
If $\alpha$ is not an integer, but $\alpha > 0$, then
$$\mathcal{L}(t^\alpha) = \int_0^\infty e^{-st}t^\alpha\dd t = \int_0^\infty e^{-x}\frac{x^\alpha}{s^\alpha}\frac{\dd x}{s} \quad (x = st) \quad = \frac{1}{s^{\alpha+1}}\int_0^\infty e^{-x}x^\alpha\dd x = \frac{\Gamma(\alpha + 1)}{s^{\alpha+1}}$$
 
**Def.** Recall from STAT2003 that:
↳ $\Gamma(n + 1) = n!$
↳ $\Gamma(x + 1) = x\Gamma(x)$
 
**Ex.**
$$\mathcal{L}(\sqrt{t}) = \frac{\Gamma(3/2)}{s^{3/2}} = \frac{\sqrt{\pi}}{2s^{3/2}}, \qquad \mathcal{L}(t^{3.1}) = \frac{\Gamma(4.2)}{s^{4.2}}$$
[possible error: by the formula, $\mathcal{L}(t^{3.1}) = \Gamma(4.1)/s^{4.1}$.]
 
**Right page.**
 
**Def.** The Laplace transform is well defined if
↳ $e^{-st}f(t)$ is defined $\forall t \ge 0$
↳ $f(t)$ cannot grow faster than $e^{-st}$.
[possible error: should be "faster than $e^{st}$" (an exponential); the next line has the precise condition.]
In general, $\abs{f(t)} \le Me^{\gamma t}$ ($\exists M, \gamma$, $\forall t > 0$).
 
**Ex.** $\mathcal{L}(e^{t^2})$ is undefined due to its growth.
 
## HW 32 — Laplace transforms of derivatives; solving linear ODEs
_File `20261121_235829.jpg`. Left page "Laplace transforms of differentials", right page "Solving linear ODEs"; both section 3.2._
 
**Left page.**
 
**Def.** Consider the Laplace transform of the first derivative of a function.
$$\mathcal{L}(\dot{f}(t)) = \int_0^\infty e^{-st}\dot{f}(t)\dd t = \left.e^{-st}f(t)\right|_0^\infty + s\int_0^\infty f(t)e^{-st}\dd t = -f(0) + s\mathcal{L}(f(t))(s)$$
For the second derivative of a function:
$$\begin{aligned} \mathcal{L}(\ddot{f}(t))(s) &= \mathcal{L}\bigl([\dot{f}(t)]'\bigr)(s) = s\mathcal{L}(\dot{f}(t)) - \dot{f}(0) \\ &= s\bigl[s\mathcal{L}(f(t))(s) - f(0)\bigr] - \dot{f}(0) = s^2\mathcal{L}(f(t))(s) - sf(0) - \dot{f}(0) \end{aligned}$$
For the $n$th derivative we thus have:
$$\mathcal{L}(f^{(n)}(t))(s) = s^n\mathcal{L}(f) - s^{n-1}f(0) - s^{n-2}\dot{f}(0) - \dots - f^{(n-1)}(0)$$
 
**Right page.**
 
**Ex.** Suppose we have $\dot{y} + 2y = 2e^{-2t}$. Taking the Laplace transform:
$$\mathcal{L}(\dot{y}) + 2\mathcal{L}(y) = \frac{2}{s + 2}$$
↳ $s\mathcal{L}(y) - y(0) + 2\mathcal{L}(y) = \dfrac{2}{s + 2}$
↳ $(s + 2)\mathcal{L}(y) = \dfrac{2}{s + 2} + y(0)$
↳ $\mathcal{L}(y) = \dfrac{2}{(s + 2)^2} + \dfrac{y(0)}{s + 2}$
Now taking the inverse Laplace transform:
$$y = \mathcal{L}^{-1}\left(\frac{2}{(s + 2)^2} + \frac{y(0)}{s + 2}\right) = 2e^{-2t}t + y(0)e^{-2t}$$
 
**Ex.** Suppose we have $\ddot{y} + 2\dot{y} + y = e^{-t}$. Then,
$$\mathcal{L}(\ddot{y}) + 2\mathcal{L}(\dot{y}) + \mathcal{L}(y) = \frac{1}{s + 1}$$
↳ $s^2\mathcal{L}(y) - sf(0) - \dot{f}(0) + 2s\mathcal{L}(y) - 2f(0) + \mathcal{L}(y) = \dfrac{1}{s + 1}$ [$f$ here means $y$]
↳ $(s^2 + 2s + 1)\mathcal{L}(y) = y(0)(s + 2) + \dot{y}(0) + \dfrac{1}{s + 1}$
↳ $\mathcal{L}(y) = \dfrac{y(0)(s + 2)}{(s + 1)^2} + \dfrac{\dot{y}(0)}{(s + 1)^2} + \dfrac{1}{(s + 1)^3}$
↳↳ $y = e^{-t}\left(y(0) + (\dot{y}(0) + y(0))t + \dfrac{t^2}{2}\right)$
 
## HW 33 — Forcing functions and transfer functions
_File `20261121_235835.jpg`. Both pages "Forcing functions and transfer functions", section 3.2. The right page has only "Ex. Take" and is otherwise blank (an unfinished example)._
 
**Left page.**
 
**Ex.** Consider $\ddot{y} - 4\dot{y} + 4y = r(t)$. We call $r(t)$ the *forcing* or *input function*. Taking the Laplace transform:
$$\mathcal{L}(\ddot{y}) - 4\mathcal{L}(\dot{y}) + 4\mathcal{L}(y) = \mathcal{L}(r(t))$$
↳ $s^2\mathcal{L}(y) - sy(0) - \dot{y}(0) - 4\bigl(s\mathcal{L}(y) - y(0)\bigr) + 4\mathcal{L}(y) = \mathcal{L}(r(t))$
↳ $(s^2 - 4s + 4)\mathcal{L}(y) = R(s) + y(0)(s - 4) + \dot{y}(0)$
Solving for $\mathcal{L}(y)$:
$$\mathcal{L}(y) = \frac{1}{s^2 - 4s + 4}\bigl(R(s) + y(0)(s - 4) + \dot{y}(0)\bigr)$$
Now consider the case where $y(0) = \dot{y}(0) = 0$. Then $\mathcal{L}(y) = R(s) \cdot \dfrac{1}{s^2 - 4s + 4}$.
The leftover function is called the *transfer function* and is determined by the LHS.
In fact, for a general second-order ODE $a\ddot{y} + b\dot{y} + cy = r(t)$, then
$$Q(s) = \frac{1}{as^2 + bs + c} \quad \text{and} \quad Y(s) = Q(s)R(s) + Q(s)\bigl(asy(0) + a\dot{y}(0) + b\dot{y}(0)\bigr)$$
[possible error: the last term should be $b\,y(0)$, not $b\,\dot y(0)$.]
 
**Right page.** **Ex.** Take [nothing further written]
 
## HW 34 — Solving systems of ODEs with Laplace transforms
_File `20261121_235842.jpg`. Both pages "Solving systems of ODEs", section 3.2. In this hand "3" and "5" look alike in "$s - 3$"; the reading $s - 3$ is used throughout (it is the only one consistent with the system). Right page mostly blank._
 
**Left page.**
 
**Def.** The method to solve a system of ODEs is essentially similar, but now there are $n$ equations and $n$ Laplace transforms.
 
**Ex.** Let
$$\begin{pmatrix} \dot{y}_1 \\ \dot{y}_2 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} + \begin{pmatrix} e^{-2t} \\ e^{-2t} \end{pmatrix}$$
Let $Y_i(s) = \mathcal{L}(y_i)$ and take the Laplace transform of each equation:
(1) $sY_1(s) = 3Y_1(s) + Y_2(s) + \dfrac{1}{s + 2} + y_1(0)$
(2) $sY_2(s) = 3Y_2(s) + \dfrac{1}{s + 2} + y_2(0)$
which can be rewritten as
(1) $(s - 3)Y_1(s) = Y_2(s) + \dfrac{1}{s + 2} + y_1(0)$
(2) $(s - 3)Y_2(s) = \dfrac{1}{s + 2} + y_2(0)$
and so
(1) $Y_1(s) = \bigl(y_1(0) + Y_2(s)\bigr)/(s - 3) + 1/\bigl((s + 2)(s - 3)\bigr)$
(2) $Y_2(s) = y_2(0)/(s - 3) + 1/\bigl((s + 2)(s - 3)\bigr)$.
To take the inverse Laplace transform, we must use partial fractions. Combining the two sim. equations:
$$\begin{aligned} Y_1(s) &= \frac{y_1(0)}{s - 3} + \frac{1}{s - 3}\left[\frac{y_2(0)}{s - 3} + \frac{1}{5}\cdot\frac{1}{s - 3} - \frac{1}{5}\cdot\frac{1}{s + 2}\right] + \frac{1}{(s + 2)(s - 3)} \\ &= \frac{y_1(0)}{s - 3} + \frac{y_2(0) + 1/5}{(s - 3)^2} + \frac{4}{5}\cdot\frac{1}{(s - 2)(s + 3)} \\ &= \frac{y_1(0)}{s - 3} + \frac{y_2(0) + 1/5}{(s - 3)^2} + \frac{4}{25}\cdot\frac{1}{s - 3} - \frac{4}{25}\cdot\frac{1}{s + 2} \end{aligned}$$
[possible error: in the middle line the denominator should be $(s + 2)(s - 3)$, as in the lines above and below.]
$$Y_2(s) = \frac{y_2(0)}{s - 3} + \frac{1}{5}\cdot\frac{1}{s - 3} - \frac{1}{5}\cdot\frac{1}{s + 2}$$
 
**Right page.**
 
**Ex.** Taking the inverse Laplace transforms, we obtain:
$$y_1(t) = \mathcal{L}^{-1}(Y_1(s)) = y_1(0)e^{3t} + \bigl(y_2(0) + 1/5\bigr)te^{3t} + \frac{1}{6}e^{3t} - \frac{4}{25}e^{-2t}$$
[possible error: from the last line of $Y_1(s)$, the coefficient of $e^{3t}$ is $\frac{4}{25}$, not $\frac16$.]
$$y_2(t) = \mathcal{L}^{-1}(Y_2(s)) = y_2(0)e^{3t} + \frac{1}{5}e^{3t} - \frac{1}{5}e^{-2t}$$
 
## HW 35 — Inverse Laplace transforms via partial fractions: overview
_File `20261121_235851.jpg`. Both pages "Inverse Laplace via partial fractions", section 3.3. Lower halves blank._
 
**Left page.**
 
**Def.** We most often use [blacked-out words] partial fractions to find the inverse Laplace transform of some fractional function.
 
**Ex.** If $F(s) = \dfrac{1}{(s - 2)(s - 3)}$ we find constants $A_1, A_2$:
$$F(s) = \frac{1}{(s - 2)(s - 3)} = \frac{A_1}{s - 2} + \frac{A_2}{s - 3}$$
and thus $\mathcal{L}^{-1}(F(s)) = A_1e^{2t} + A_2e^{3t}$
 
**Ex.** If $F(s) = \dfrac{1}{(s - 2)^2(s - 3)}$ we find $A_1, A_2, B_1$:
$$F(s) = \frac{1}{(s - 2)^2(s - 3)} = \frac{A_1}{s - 2} + \frac{A_2}{(s - 2)^2} + \frac{B_1}{(s - 3)}$$
and thus $\mathcal{L}^{-1}(F(s)) = A_1e^{2t} + A_2te^{2t} + B_1e^{3t}$
 
**Ex.** If $F(s)$ is irreducible (complex roots), then see the following example.
 
**Right page.**
 
**Ex.** If $F(s) = \dfrac{1}{(s^2 + 4)(s - 3)}$ we find $A_1, A_2, B_1$:
$$F(s) = \frac{1}{(s^2 + 4)(s - 3)} = \frac{A_1s + A_2}{s^2 + 4} + \frac{B_1}{s - 3}$$
and thus $\mathcal{L}^{-1}(F(s)) = A_1\cos 2t + \frac{1}{2}A_2\sin 2t + B_1e^{3t}$
 
**Def.** We will discuss the four more general partial fraction cases in more detail:
↳ Simple linear factors
↳ Repeated simple linear factors
↳ Irreducible quadratic factors
↳ Repeated irreducible quadratic factors
 
## HW 36 — Partial fractions: Case 1 (simple linear factors), Case 2 (repeated linear factors)
_File `20261121_235858.jpg`. Both pages "Inverse Laplace via partial fractions", section 3.3._
 
**Left page.**
 
**Def.** Case 1: simple linear factors
If $F(s) = \dfrac{N(s)}{\prod_{i=1}^n (s - a_i)}$ then we can find $A_i$ such that
$$F(s) = \sum_{i=1}^n \frac{A_i}{s - a_i} \quad \text{and thus} \quad \mathcal{L}^{-1}(F(s)) = \sum_{i=1}^n A_ie^{a_it}$$
 
**Ex.** Consider $F(s) = \dfrac{-7s - 1}{(s - 1)(s + 2)(s + 3)}$.
[possible error: the denominator should be $(s - 1)(s - 2)(s + 3)$, as in CN §3.3.1 and as used in the substitution $s = 2$ and the decomposition below.]
By letting, say, $s = 1$, $s = 2$, $s = -3$, we obtain: $A_1 = 2$, $A_2 = -3$, $A_3 = -1$
Thus
$$F(s) = [\text{blacked out}] = \frac{2}{s - 1} - \frac{3}{s - 2} - \frac{1}{s + 3}$$
so
$$\mathcal{L}^{-1}(F(s)) = 2e^t - 3e^{2t} - e^{-3t}$$
[possible error: with denominator $(s-1)(s-2)(s+3)$, setting $s = -3$ gives $A_3 = 20/20 = 1$, so the last terms should be $+\frac{1}{s+3}$ and $+e^{-3t}$.]
 
**Right page.**
 
**Def.** Case 2: repeated simple linear factors
If $F(s) = \dfrac{N(s)}{(s - a)^n}$ we can find $A_i$ such that $= \sum_{i=1}^n \dfrac{A_i}{(s - a)^i}$
More generally, let
$$F(s) = \frac{N(s)}{(s - a_1)^3(s - a_2)^2(s - a_3)\cdots(s - a_n)}$$
Then we can find $A_i, B_i, C_i$ such that
$$F(s) = \frac{A_1}{s - a_1} + \frac{A_2}{(s - a_1)^2} + \frac{A_3}{(s - a_1)^3} + \frac{B_1}{s - a_2} + \frac{B_2}{(s - a_2)^2} + \frac{C_1}{s - a_3} + \dots + \frac{C_{n-2}}{s - a_n}$$
and so
$$\mathcal{L}^{-1}(F(s)) = A_1e^{a_1t} + A_2te^{a_1t} + A_3\frac{t^2}{2}e^{a_2t} + B_1e^{a_2t} + B_2e^{a_2t}t + \dots$$
[possible error: the $A_3$ term should have $e^{a_1 t}$, not $e^{a_2 t}$.]
 
**Ex.** Consider $F(s) = \dfrac{15s + 12}{(s + 2)^3(s - 1)}$. Again let $s = -2$, $s = 1$, $s = 0$. We obtain:
$$F(s) = \frac{-1}{s + 2} - \frac{3}{(s + 2)^2} + \frac{6}{(s + 2)^3} + \frac{1}{s - 2}$$
so
$$\mathcal{L}^{-1}(F(s)) = -e^{-2t} - 3te^{-2t} + 3t^2e^{-2t} + e^{2t}$$
[possible error: the last factor is $(s - 1)$, so the last terms should be $\frac{1}{s - 1}$ and $e^{t}$; the other coefficients check out.]
 
## HW 37 — Partial fractions: Case 3 (irreducible quadratic factors)
_File `20261121_235904.jpg`. Both pages "Inverse Laplace via partial fractions", section 3.3._
 
**Left page.**
 
**Def.** Case 3: irreducible quadratic factors
If $F(s) = \dfrac{N(s)}{(s - a)^2 + \alpha^2}$ then we can find $A, B$ such that
$$F(s) = \frac{A(s - a)}{(s - a)^2 + \alpha^2} + \frac{B}{(s - a)^2 + \alpha^2}$$
and thus the inverse Laplace transform is:
$$\mathcal{L}^{-1}(F(s)) = e^{\alpha t}\cos(\alpha t) + e^{at}\sin(\alpha t)$$
[possible error: should be $Ae^{at}\cos(\alpha t) + \frac{B}{\alpha}e^{at}\sin(\alpha t)$: the coefficients are missing and the first exponent has $\alpha$ for $a$.]
More generally, say
$$F(s) = \frac{N(s)}{[(s - a_1)^2 + b_1^2](s - a_2)\cdots(s - a_n)}$$
Then we can find $A_i, B_i, C_i$ such that
$$F(s) = \frac{A_1(s - a_1)}{(s - a_1)^2 + b_1^2} + \left(\frac{1}{b_1}\right)b_1\cdot\frac{B_1}{(s - a_1)^2 + b_1^2} + \frac{C_1}{s - a_2} + \dots + \frac{C_{n-1}}{s - a_n}$$
[a small blacked-out box before $C_1$]
and therefore
$$\mathcal{L}^{-1}(F(s)) = A_1e^{a_1t}\cos b_1t + \frac{B_1}{b_1}e^{a_1t}\sin b_1t + C_1e^{a_2t} + \dots + C_{n-1}e^{a_nt}$$
[the notes write the exponentials as $e$ with the coefficient raised, e.g. "${}^{A_1}e^{a_1t}$", "${}^{C_1}e^{a_2t}$", with a blacked-out box; read as products. The $C_i$ in "$C_{n-1}\,C^{a_n t}$" is a badly formed $e$.]
 
**Right page.**
 
**Ex.** Consider $F(s) = \dfrac{3(s - 10)}{s^2 - 4s + 20}$.
A quadratic is irreducible if its roots are complex. Here $s^2 - 4s + 20 = \bigl(s - (2 + 4i)\bigr)\bigl(s - (2 - 4i)\bigr)$.
If a quadratic is irreducible, it can always be written in the form $\bigl((s - a)^2 + \alpha^2\bigr)$ by completing the square: $s^2 - 4s + 20 = (s - 2)^2 + 16$.
Thus,
$$F(s) = \frac{3(s - 10)}{s^2 - 4s + 20} = \frac{3(s - 2 - 8)}{(s - 2)^2 + 16} = 3\cdot\frac{s - 2}{(s - 2)^2 + 16} - 6\cdot\frac{4}{(s - 2)^2 + 16}$$
$$f(t) = 3e^{2t}\cos 4t - 6e^{2t}\sin 4t$$
 
## HW 38 — Partial fractions: Case 4 (repeated irreducible quadratic factors); differentiating a transform
_File `20261121_235915.jpg`. Both pages "Inverse Laplace via partial fractions", section 3.3._
 
**Left page.**
 
**Def.** Case 4: repeated irreducible quad. factors
Now we need only know how to find the inverse Laplace transforms of functions like
$$F(s) = \frac{1}{\bigl((s - a)^2 + \alpha^2\bigr)^m}$$
We have no idea (yet) how to do this! While we can use methods with complex numbers, a more interesting method involves the differential of the transformed function.
Suppose we know the transform of $f$, i.e. we know $F(s) = \mathcal{L}(f(t)) = \int_0^\infty e^{-st}f(t)\dd t$.
Then the differential of $F(s)$ w.r.t. $s$ is
$$\frac{\dd F(s)}{\dd s} = \frac{\dd}{\dd s}\int_0^\infty e^{-st}f(t)\dd t = \int_0^\infty \frac{\dd}{\dd s}e^{-st}f(t)\dd t = \int_0^\infty -te^{-st}f(t)\dd t = \mathcal{L}(-tf(t))$$
and so
$$\mathcal{L}(-tf(t)) = \frac{\dd F(s)}{\dd s}.$$
 
**Right page.**
 
**Ex.** If we know $\mathcal{L}(t^3) = 6s^{-4}$ then
$$-\frac{\dd}{\dd s}\left(\frac{6}{s^4}\right) = \frac{24}{s^5} = \frac{4!}{s^5} = \mathcal{L}(t^4) = \mathcal{L}(t \times t^3)$$
which is true!
 
**Ex.** Suppose $\mathcal{L}(\cos(\alpha t)) = \dfrac{s}{s^2 + \alpha^2}$. The theorem implies that
$$\mathcal{L}(-t\cos(\alpha t)) = \frac{\dd}{\dd s}F(s) = \frac{\dd}{\dd s}\left(\frac{s}{s^2 + \alpha^2}\right) = \dots = \frac{1}{s^2 + \alpha^2} - \frac{2s^2}{(s^2 + \alpha^2)^2}$$
We can use this to find the inverse Laplace transform of repeated irreducible quadratic factors (alongside $\mathcal{L}(t\sin(\alpha t))$) and we obtain:
$$\mathcal{L}^{-1}\left(\frac{s}{(s^2 + \alpha^2)^2}\right) = \frac{1}{2\alpha}t\sin(\alpha t)$$
$$\mathcal{L}^{-1}\left(\frac{s^2}{(s^2 + \alpha^2)^2}\right) = \frac{1}{2\alpha}\sin(\alpha t) + \frac{1}{2}t\cos(\alpha t)$$
$$\mathcal{L}^{-1}\left(\frac{\alpha^2}{(s^2 + \alpha^2)^2}\right) = \frac{1}{2\alpha}\sin(\alpha t) - \frac{1}{2}t\cos(\alpha t)$$
 
## HW 39 — Case 4 example; the second shifting theorem
_File `20261121_235930.jpg`. Left page "Inverse Laplace via partial fractions" (section 3.3, number in the gutter), right page "Second shifting theorem" (section 3.4). Lower halves blank._
 
**Left page.**
 
**Ex.** Consider the following:
$$\begin{aligned} F(s) = \frac{s^2 - 7}{(s^2 + 4)^2} &= \frac{s^2}{(s^2 + 4)^2} - \frac{7}{(s^2 + 4)^2} = \frac{s^2}{(s^2 + 4)^2} - \frac{7}{4}\cdot\frac{4}{(s^2 + 4)^2} \\ &= \frac{1}{2\cdot 2}\sin(2t) + \frac{1}{2}t\cos(2t) - \frac{7}{4}\left(\frac{1}{2\cdot 2}\sin(2t) - \frac{1}{2}t\cos(2t)\right) \\ &= \dots = -\frac{3}{16}\sin 2t + \frac{11}{8}t\cos 2t \end{aligned}$$
[from the third line on, these are the inverse transforms $f(t)$, still written after "$F(s) =$"]
 
**Right page.**
 
**Def.** Recall the unit (Heaviside) step function:
$$u(t - k) = \begin{cases} 0 & 0 \le t < k \\ 1 & t \ge k \end{cases}$$
Now consider $u(t - k)f(t - k)$. The Laplace transform of this function is quite simple:
$$\mathcal{L}\bigl(f(t - k)u(t - k)\bigr) = e^{-sk}F(s)$$
**P.** Consider (and directly compute):
$$\begin{aligned} \mathcal{L}\bigl(f(t - k)u(t - k)\bigr) &= \int_0^\infty f(t - k)u(t - k)e^{-st}\dd t = \int_k^\infty f(t - k)e^{-st}\dd t \\ &= \int_0^\infty f(z)e^{-s(z + k)}\dd z \quad \text{by } z = t - k,\ \dd z = \dd t \\ &= e^{-ks}\int_0^\infty f(z)e^{-zs}\dd z \end{aligned}$$
which follows the result.
 
## HW 40 — Second shifting theorem: examples
_File `20261121_235952(0).jpg`. Both pages "Second shifting theorem", section 3.4. Lower third blank._
 
**Left page.**
 
**Ex.** Consider the following example:
$$\mathcal{L}^{-1}\left(\frac{e^{-ks}}{s^2}\right) = \mathcal{L}^{-1}\left(e^{-ks}\cdot\frac{1}{s^2}\right) = f(t - k)u(t - k)$$
and so to find $f$: $\mathcal{L}^{-1}\left(\dfrac{1}{s^2}\right) = t = f(t)$ and thus $f(t - k) = t - k$.
 
**Ex.** Consider
$$\begin{aligned} \mathcal{L}^{-1}\left(\frac{(1 - e^{-s})^2}{s^2}\right) &= \mathcal{L}^{-1}\left(\frac{1}{s^2} - \frac{2e^{-s}}{s^2} + \frac{e^{-2s}}{s^2}\right) = \mathcal{L}^{-1}\left(\frac{1}{s^2}\right) - 2\mathcal{L}^{-1}\left(e^{-s}\frac{1}{s^2}\right) + \mathcal{L}^{-1}\left(e^{-2s}\frac{1}{s^2}\right) \\ &= t - 2f(t - 1)u(t - 1) + f(t - 2)u(t - 2) \\ &= t - 2(t - 1)u(t - 1) + (t - 2)u(t - 2) \end{aligned}$$
["$(t-1)$" is written above a blacked-out box after "$2f$"]
 
**Right page.**
 
**Ex.** Going the other way is generally harder as the functions must all be expressed as a sum of functions in the form $f(t - k)u(t - k)$.
Take
$$h(t) = \begin{cases} 2 & t < 1 \\ 0 & t \ge 1 \end{cases} = 2\bigl(1 - u(t - 1)\bigr) = 2 - 2u(t - 1)$$
so
$$\mathcal{L}(h(t)) = \mathcal{L}(2) - \mathcal{L}\bigl(f(t - 1)u(t - 1)\bigr) = 2/s - 2e^{-s}/s$$
Take
$$h(t) = \begin{cases} t^2 & t < 1 \\ 1 & t \ge 1 \end{cases} = t^2\bigl(1 - u(t - 1)\bigr) + u(t - 1) = t^2 + (1 - t^2)u(t - 1)$$
so that $f(t - 1) = 1 - t^2$. Use the substitution $x = t - 1$. Then,
$$f(x) = 1 - (x + 1)^2 = \dots = -2x - x^2, \qquad F(s) = -2/s^2 - 2/s^3$$
and so
$$\mathcal{L}(h(t)) = 2/s^3 - e^{-s}\bigl(2/s^2 + 2/s^3\bigr)$$
 
## HW 41 — The convolution theorem
_File `20261122_000010.jpg`. Both pages "Convolution theorem", section 3.5. Lower half of the right page blank._
 
**Left page.**
 
**Def.** Unfortunately $\mathcal{L}^{-1}\bigl(F(s)G(s)\bigr) \ne f(t)g(t)$. i.e. the Laplace transform is not multiplicative. However, a similar analogue is true!
 
**Def.** Define the convolution theorem by
$$\mathcal{L}^{-1}\bigl(F(s)G(s)\bigr) = f * g(t)$$
where the *convolution* of two functions is defined by:
$$f * g(t) = \int_0^t f(\tau)g(t - \tau)\dd\tau$$
 
**P.** Firstly consider the second shift theorem:
$$e^{-s\tau}G(s) = \int_0^\infty g(t - \tau)u(t - \tau)e^{-st}\dd t = \int_\tau^\infty g(t - \tau)e^{-st}\dd t$$
Now,
$$F(s)G(s) = \int_0^\infty e^{-s\tau}f(\tau)\dd\tau \times G(s) = \int_0^\infty G(s)e^{-s\tau}f(\tau)\dd\tau = \int_0^\infty\int_\tau^\infty g(t - \tau)e^{-st}f(\tau)\dd t\dd\tau$$
We now change the order of integration.
 
**Right page.**
 
**P.** [the "P." label is next to a small blacked-out box] Now $\tau$ is integrated from $0$ to $t$, and $t$ from $0$ to $\infty$.
$$\begin{aligned} F(s)G(s) &= \int_0^\infty\int_0^t g(t - \tau)e^{-st}f(\tau)\dd\tau\dd t = \int_0^\infty\left[\int_0^t g(t - \tau)f(\tau)\dd\tau\right]e^{-st}\dd t \\ &= \int_0^\infty \bigl(f * g(t)\bigr)e^{-st}\dd t = \mathcal{L}\bigl(f * g(t)\bigr) \end{aligned}$$
[a blacked-out box before "$(f * g(t))$" in the third line]
Note that convolution is commutative. The proof of this statement is by the change of variables $T = t - \tau$.
 
## HW 42 — Convolution theorem: examples; combining with the second shifting theorem
_File `20261122_000030.jpg`. Both pages "Convolution theorem", section 3.5._
 
**Left page.**
 
**Ex.** Find $\mathcal{L}^{-1}\left(\dfrac{2s}{(s^2 + 1)^2}\right)$.
Let $F(s) = 2/(s^2 + 1)$ $\to f(t) = 2\sin t$. Let $G(s) = s/(s^2 + 1)$ $\to g(t) = \cos t$. Then
$$\begin{aligned} \mathcal{L}^{-1}\left(\frac{2s}{(s^2 + 1)^2}\right) &= \int_0^t 2\sin\tau\cos(t - \tau)\dd\tau = \int_0^t \bigl[\sin(\tau + t - \tau) + \sin(\tau - t + \tau)\bigr]\dd\tau \\ &= \int_0^t \sin t\dd\tau + \int_0^t \sin(2\tau - t)\dd\tau = \sin t\,\tau\Big|_0^t - \left.\frac{\cos(2\tau - t)}{2}\right|_0^t = \dots = t\sin t \end{aligned}$$
 
**Ex.** Find $\mathcal{L}^{-1}\left(\dfrac{1}{(s - 2)^2(s + 1)}\right)$.
Let $F(s) = 1/(s - 2)^2$ $\to f(t) = te^{2t}$. Let $G(s) = 1/(s + 1)$ $\to g(t) = e^{-t}$.
By convolution $\mathcal{L}^{-1}\left(\dfrac{1}{(s - 2)^2(s + 1)}\right) = f * g(t)$.
Thus using integration by parts,
$$\mathcal{L}^{-1}\left(\frac{1}{(s - 2)^2(s + 1)}\right) = \int_0^t f(\tau)g(t - \tau)\dd\tau$$
 
**Right page.**
 
**Ex.** [continued]
$$\dots = \int_0^t \tau e^{2\tau}e^{-(t - \tau)}\dd\tau = \dots = \frac{t}{3}e^{2t} - \frac{e^{2t}}{9} + \frac{e^{-t}}{9}$$
 
**N.** To find the [inv.] Laplace transform of a function with an exponential, first find the inverse Laplace transform without the exponential and then use the second shifting theorem. ["inv." is inserted above the line with a caret]
 
**Ex.** Find $\mathcal{L}^{-1}\left(\dfrac{e^{-3s}}{s^2}\right)$. We know $\mathcal{L}^{-1}\left(\dfrac{1}{s^2}\right) = t$. Thus,
$$\mathcal{L}^{-1}\left(\frac{e^{-3s}}{s^2}\right) = \mathcal{L}^{-1}\left(e^{-3s}\cdot\frac{1}{s^2}\right) = g(t - 3)u(t - 3) = (t - 3)u(t - 3)$$
 
**Ex.** Find $\mathcal{L}^{-1}\left(\dfrac{e^{-3s}}{(s - 2)^2(s + 1)}\right)$.
$$\begin{aligned} &= \mathcal{L}^{-1}\left(e^{-3s}\cdot\frac{1}{(s - 2)^2(s + 1)}\right) \quad \text{[2nd ST]} \\ &= h(t - 3)u(t - 3) = u(t - 3)\left(\frac{t - 3}{3}e^{2(t-3)} - \frac{e^{2(t-3)}}{9} + \frac{e^{-(t-3)}}{9}\right) \end{aligned}$$
 
## HW 43 — Solving linear ODEs with convolution; resonance example
_File `20261122_000037.jpg`. Both pages "Solving linear ODEs with convolution", section 3.5. Lower half of the right page blank._
 
**Left page.**
 
**Def.** For a second order linear constant coeff. ODE, with time-dependent forcing
$$\ddot{y} + a\dot{y} + by = r(t), \qquad y(0) = \dot{y}(0) = 0$$
the Laplace transform (recall) has the particularly simple form $Y(s) = Q(s)R(s)$ with transfer function
$$Q(s) = \frac{1}{s^2 + as + b}$$
Now, by convolution, $y(t) = q * r(t)$ where $\mathcal{L}(q(t)) = Q(s)$, $q(t) = \mathcal{L}^{-1}(Q(s))$.
Note we never have to work out $R(s)$!
 
**Ex.** Consider a scenario where we have mass attached to a spring which is periodically forced with a frequency equal to the natural frequency of the spring. The differential equation is given by:
$$\ddot{x}(t) + \omega_0^2x(t) = F(t)$$
Assuming the initial velocity and position of the mass is zero, the IVP is:
$$\ddot{x}(t) + 9x(t) = r(t) = \cos(3t)$$
 
**Right page.**
 
**Ex.** Thus if $X(s) = \mathcal{L}(x(t))$, then $= Q(s)\cdot R(t)$ where
$$Q(s) = \frac{3}{3s^2 + 9}$$
[possible error: $Q(s) = \frac{1}{s^2 + 9} = \frac13\cdot\frac{3}{s^2+9}$; as written, $\frac{3}{3s^2 + 9} = \frac{1}{s^2 + 3}$. The working below uses $q(t) = \frac13\sin 3t$, which is right. Also "$R(t)$" should be $R(s)$.]
which by convolution has inverse transform
$$\begin{aligned} x(t) &= \mathcal{L}^{-1}(X(s)) = q * r(t) = \int_0^t q(\tau)r(t - \tau)\dd\tau = \frac{1}{2}\int_0^t \frac{2}{3}\sin(3\tau)\cos\bigl(3(t - \tau)\bigr)\dd\tau \\ &= \frac{1}{6}\int_0^t \sin 3t\dd\tau + \frac{1}{6}\int_0^t \sin(6\tau - 3t)\dd\tau = \dots = \frac{1}{6}t\sin 3t \end{aligned}$$
 
## HW 44 — Laplace transforms of periodic functions
_File `20261122_000045.jpg`. Both pages "Laplace transforms of periodic functions", section 3.5._
 
**Left page.**
 
**Def.** Suppose $f$ is periodic with period $p$, i.e. $f(t + p) = f(t)$. Consider the Laplace transform of $f$:
$$\mathcal{L}(f(t)) = \int_0^\infty e^{-st}f(t)\dd t = \int_0^p \dots + \int_p^{2p} \dots + \int_{2p}^{3p} + \dots$$
Now
$$\int_p^{2p} e^{-st}f(t)\dd t = \int_0^p e^{-(x+p)s}f(x + p)\dd x = e^{-ps}\int_0^p e^{-xs}f(x)\dd x$$
Similarly
$$\int_{np}^{(n+1)p} e^{-st}f(t)\dd t = \int_0^p e^{-xs}f(x)\dd x \times e^{-snp}$$
Therefore,
$$\mathcal{L}(f(t)) = \sum_{n=0}^\infty (e^{-sp})^n\int_0^p f(x)e^{-sx}\dd x = \frac{1}{1 - e^{-sp}}\int_0^p f(x)e^{-sx}\dd x$$
 
**Right page.**
 
**Ex.** Consider a square wave:
$$f(t) = \begin{cases} 1 & 0 \le t < a \\ 0 & a \le t < 2a \end{cases} \quad \text{where } f(t + 2a) = f(t)$$
A diagram is given below:
 
*Figure (square wave).* Horizontal axis with an arrow to the right, ticks labelled $a$, $2a$, $3a$, $4a$; vertical axis with levels $0$ and $1$ marked. The graph is drawn with dashed segments: at height 1 on $[0, a)$ and $[2a, 3a)$, and at height 0 (on the axis) on $[a, 2a)$ and $[3a, 4a)$. No vertical jump lines.
 
The Laplace transform is given by:
$$F(s) = \frac{1}{1 - e^{-s2a}}\int_0^{2a} f(x)e^{-sx}\dd x = \frac{1}{1 - [e^{-sa}]^2}\int_0^a e^{-sx}\dd x = \frac{1}{(1 - e^{-sa})(1 + e^{-sa})}\left.\frac{e^{-sx}}{-s}\right|_0^a = \dots = \frac{1}{s(1 + e^{-sa})}$$

# MATH2100 Applied Mathematical Analysis (MATH2010 ODEs + MATH2011 PDEs): transcription, part 3 of 5 (HW 45–68)
 
_Transcription phase. Nothing here is book text yet. Sources, legibility check and conventions: see part 1 (`claude/notes-math2100-1.md`)._
 
**This part:** introduction to PDEs, Fourier series (coefficients, convergence, even/odd, half-range expansions, differentiation, forced oscillations), vector calculus (grad, div, curl, level surfaces, flux, divergence theorem, conservation laws), derivation of the heat, Laplace and wave equations. "CN §" = CN-PDE.
 
---
 
## HW 45 — Contents page (MATH2011 half)
_File `20261122_000106.jpg`. Single page, photographed sideways. Readable._
 
**MATH2100**
**Applied Math. Analysis**
 
| No. | Title |
|---|---|
| 1 | Intro to MATH2011 (PDEs) |
| 2 | Fourier Series |
| 2.0 | Coefficients and Convergence |
| 2.1 | Odd and even functions |
| 2.2 | Half-range expansion |
| 2.3 | Derivatives of Fourier series |
| 2.4 | Example: forced oscillations |
| 3 | Vector calculus review |
| 3.4 | Gauss' divergence theorem |
| 3.5 | Conservation laws |
| 4 | PDE Overview |
| 5 | 1D wave equation |
| 5.1 | D'Alembert's solution |
| 5.2 | IVPs for infinite strings |
| 5.3 | The error function erf(x) |
| 6 | Fourier's method |
| 6.1 | 1D wave equation |
| 6.2 | 1D heat equation |
| 6.3 | Inhomo. heat equation |
 
[The list stops at 6.3; the CN (MATH2011) also has 6.4–6.6 and chapter 7.]
 
## HW 46 — Introduction to PDEs
_File `20261122_000120.jpg`. Both pages "Introduction to PDEs", section 1._
 
**Left page.**
 
**N.** In contrast to an ODE (where we have one independent variable), PDEs have multiple independent variables. Many PDEs have been used for models that require spatial dependence as well as time dependence.
 
**Def.** Partial differential equations (PDEs)
A *PDE* is an equation involving partial derivatives of an unknown function with respect to (abbreviated w.r.t.) two or more independent variables.
For example,
$$\frac{\partial u}{\partial t} + \frac{\partial^3 u}{\partial x^3} - 6u\frac{\partial u}{\partial x} = 0 \quad \text{(KdV eq.)}$$
$$\frac{1}{c^2}\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2} - m^2u \quad \text{(Klein–Gordon)}$$
$$i\frac{\partial u}{\partial t} = -\frac{1}{2m}\frac{\partial^2 u}{\partial x^2} + V(x, t)u \quad \text{(Schrödinger)}$$
$$\frac{\partial^2 u}{\partial t^2} - \frac{\partial^2 u}{\partial x^2} - \sin u = 0 \quad \text{(Sine–Gordon)}$$
$$\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial u}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2 u}{\partial\phi^2} + \ell(\ell + 1)u = 0 \quad \text{(Spherical harmonic diff. equation)}$$
are some commonly used PDEs.
[possible error: CN §1 has $+\sin u$ in the Sine–Gordon equation.]
 
**Right page.**
 
**Def.** Order of PDE
The *order* of a PDE is defined as the order of the highest partial derivative in the PDE.
 
**Def.** Linearity
A PDE is *linear* if the dependent variable and its partial derivatives occur linearly.
 
**Def.** Homogenous
A PDE is *homogenous* if every term of the PDE contains the dependent variable or partials.
 
**N.** We will examine three famous PDEs in MATH2100:
(1) 1D Wave Equation $\dfrac{\partial^2 u}{\partial t^2} = c^2\dfrac{\partial^2 u}{\partial x^2}$. Used in acoustics, electromagnetism, fluid dynamics, etc.
(2) 1D Heat Equation $\dfrac{\partial u}{\partial t} = c^2\dfrac{\partial^2 u}{\partial x^2}$. Used in heat transfer, finance, etc.
(3) 2D Laplace Equation $\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = 0$. Used in many applications where state depends on position (not time).
 
## HW 47 — The "big three" PDEs, superposition, Fourier's method; assumed knowledge
_File `20261122_000129.jpg`. Left page "Introduction to PDEs", right page "Assumed knowledge"; both section 1._
 
**Left page.**
 
**N.** The 'big three' PDEs are second-order linear homogenous PDEs with constant coefficients. Solutions of such a PDE (luckily) obey the superposition principle.
 
**Def.** Superposition principle
Let $u_1, \dots, u_k$ be solutions of a given linear and homogenous PDE. Then the linear combination (or superposition)
$$u = \sum_{i=1}^k c_iu_i = c_1u_1 + \dots + c_ku_k$$
is also a solution of the PDE for any $c_i \in \R$.
 
**N.** To derive analytic solutions of the big three PDEs, with initial and boundary conditions, we use Fourier's method. This method involves applying two important techniques: Fourier series and separation of variables.
The main idea in the separation of variables is to try and reduce a PDE to PDEs in fewer independent variables (which are easier to solve), or even ODEs.
 
**Right page.**
 
**N.** A knowledge of solutions of second-order, linear, homogenous, constant-coefficient ODEs will be required in solving PDEs in the process of separation of variables. We thus recall the following results:
 
**Def.** Given a … ODE
$$a\frac{\partial^2 y}{\partial x^2} + b\frac{\dd y}{\dd x} + cy = 0$$
we have the aux. equation $a\lambda^2 + b\lambda + c = 0$, where the roots determine the solution:
↳ If $\lambda_1, \lambda_2 \in \R$ are unique then $y = Ae^{\lambda_1x} + Be^{\lambda_2x}$.
↳ If $\lambda_1 = \lambda_2 \in \R$ then $y = (A + Bx)e^{\lambda_1x}$.
↳ If $\lambda_1, \lambda_2 \in \C$, recall $\lambda_1$ and $\lambda_2$ form a conjugate pair $\lambda = \alpha \pm i\beta$. Then $y = e^{\alpha x}\bigl(A\cos(\beta x) + B\sin(\beta x)\bigr)$.
["Given a … ODE": the "…" is in the notes. The second derivative is written with $\partial$.]
 
## HW 48 — Introduction to Fourier series; sawtooth example
_File `20261122_000139.jpg`. Both pages "Introduction to Fourier series", section 2.0._
 
**Left page.**
 
**N.** Consider a periodic function $f$ with period $p$, i.e. $f(x + p) = f(x)$ $\forall x \in \R$. What if we analyse $f$ in terms of the 'elementary' periodic functions with period $p$? i.e. $\cos\left(\frac{2\pi}{p}x\right), \dots$, $\sin\left(\frac{2\pi}{p}x\right), \dots$
We may express $f$ by
$$f(x) = a_0 + a_1\cos\left(\frac{2\pi}{p}x\right) + b_1\sin\left(\frac{2\pi}{p}x\right) + a_2\cos\left(\frac{4\pi}{p}x\right) + b_2\sin\left(\frac{4\pi}{p}x\right) + \dots$$
The only issue is finding the coefficients.
 
**Ex.** Consider the following periodic function:
 
*Figure (sawtooth, period 1).* Axes $x$ (horizontal, arrow) and $y$ (vertical); $y$-tick 2, $x$-ticks 0, 1, 2, 3. Three solid ramps, each rising linearly from $(n, 0)$ to $(n+1, 2)$, with dashed vertical lines at $x = 1, 2, 3$ marking the drops back to 0; "…" after the third ramp. Annotated: $f(x) = 2x$, $0 < x < 1$, $f(x + 1) = f(x)$.
 
This function has support $\R$ and is periodic with period 1. It is piecewise continuous.
The relevant elementary functions have period 1: $1, \cos(2\pi x), \cos(4\pi x), \dots, \sin(2\pi x), \dots$
 
**Right page.**
 
**Ex.** (continued) The Fourier series of this function is given by
$$f(x) = 1 + \frac{-2}{\pi}\sin(2\pi x) + \frac{-1}{\pi}\sin(4\pi x) + \frac{-2}{3\pi}\sin(6\pi x) + \frac{-1}{2\pi}\sin(8\pi x) + \dots$$
Each successive approximation/additional term will provide a more accurate representation.
 
*Figure (partial sums, six small panels in a 3 × 2 grid, each with plain axes and no tick labels).* (1) a dashed horizontal line at constant height (the term $a_0 = 1$); (2) a dashed single sine wave about that level (one term); (3) a dashed curve with two oscillations superimposed, starting high, dipping, then a hump (two terms); (4) a more jagged dashed curve rising roughly like a ramp with small wiggles (more terms); (5) a dotted curve with even more small wiggles approximating two ramps; (6) the target: two solid straight ramps (sawtooth). The panels show the partial sums approaching the sawtooth. [Freehand sketches, not accurate plots.]
 
## HW 49 — Fourier series: definition; orthogonality
_File `20261122_000146.jpg`. Left page "Fourier series", right page "Orthogonality"; both section 2.0. Lower half of the left page blank._
 
**Left page.**
 
**Def.** A *Fourier series* is an expansion of a periodic function into a sum of elementary periodic functions (e.g. trig)
In general, given a function $f$ with period $p$ defined on $\R$, we try expand it as
$$f(x) = a_0 + \sum a_n\cos\left(\frac{2n\pi}{p}x\right) + \sum b_n\sin\left(\frac{2n\pi}{p}x\right)$$
It is conventional to let $p = 2L$:
$$f(x) = a_0 + \sum_{n=1}^\infty a_n\cos\left(\frac{n\pi}{L}x\right) + \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi}{L}x\right)$$
where $a_i, b_i$ are called *Fourier coefficients*.
 
**Right page.**
 
**N.** We wish to answer the following question: How do we find the Fourier coefficients $a_i, b_i$ when we are given $f$?
 
**Def.** Recall the definition of orthogonality: Let $V$ be a vector space. Let $\vect{u}, \vect{v} \in V$. Then $\vect{u}$ and $\vect{v}$ are *orthogonal* if $\inner{\vect{u}, \vect{v}} = 0$.
We wish to show that the set
$$\left\{1, \cos\left(\frac{n\pi x}{L}\right), \sin\left(\frac{n\pi x}{L}\right)\right\}$$
is orthogonal under the inner product
$$\inner{f_1, f_2} = \int_{-L}^L f_1(x)f_2(x)\dd x$$
 
**Rem.** [a blacked-out word] We can show that this set actually forms a basis for the space of periodic functions.
 
**Rem.** While we consider the interval $[-L, L]$ for our proofs, this set is orthogonal over any period $[a, a + 2L]$. The proof will be assessed in Assignment 3.
 
## HW 50 — Proof of orthogonality
_File `20261122_000155.jpg`. Both pages "Proof of orthogonality", section 2.0._
 
**Left page.**
 
**P.** First consider, for $n \ne 0$,
$$\int_{-L}^L 1 \times \cos\left(\frac{n\pi x}{L}\right)\dd x = \left.\frac{L}{n\pi}\sin\left(\frac{n\pi x}{L}\right)\right|_{-L}^L = \frac{L}{n\pi}\bigl[\sin n\pi - \sin(-n\pi)\bigr] = 0$$
Similarly we can show
$$\int_{-L}^L 1 \times \sin\left(\frac{n\pi x}{L}\right)\dd x = 0.$$
Now consider, for $m \ne n$,
$$\begin{aligned} \int_{-L}^L \cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\dd x &= \int_{-L}^L \frac{1}{2}\left(\cos\frac{(m - n)\pi x}{L} + \cos\frac{(m + n)\pi x}{L}\right)\dd x \\ &= \frac{1}{2}\left(\frac{L}{(m - n)\pi}\sin\left(\frac{(m - n)\pi x}{L}\right) + \frac{L}{(m + n)\pi}\sin\left(\frac{(m + n)\pi x}{L}\right)\right)\Bigg|_{-L}^L = 0 \end{aligned}$$
[each sine is struck through with an arrow to "0": it vanishes at $x = \pm L$]
by $\cos\alpha\cos\beta = \frac{1}{2}\bigl(\cos(\alpha + \beta) + \cos(\alpha - \beta)\bigr)$
 
**Right page.**
 
**P.** Similarly consider, for $m \ne n$,
$$\int_{-L}^L \sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\dd x = \int_{-L}^L \frac{1}{2}\left(\cos\frac{(m - n)\pi x}{L} + \cos\frac{(m + n)\pi x}{L}\right)\dd x = \dots = 0$$
by $\sin\alpha\sin\beta = \frac{1}{2}\bigl(\cos(\alpha - \beta) - \cos(\alpha + \beta)\bigr)$.
[possible error: by the identity quoted, the integrand is $\frac12\bigl(\cos\frac{(m-n)\pi x}{L} - \cos\frac{(m+n)\pi x}{L}\bigr)$; the sign is $+$ in the notes. The integral is $0$ either way.]
We lastly consider, for $m \ne n$,
$$\begin{aligned} \int_{-L}^L \sin\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\dd x &= \int_{-L}^L \frac{1}{2}\left(\sin\left(\frac{(m + n)\pi x}{L}\right) + \sin\left(\frac{(m - n)\pi x}{L}\right)\right)\dd x \\ &= -\frac{1}{2}\left[\frac{L}{\pi(m + n)}\cos\frac{(m + n)\pi x}{L} + \frac{L}{\pi(m - n)}\cos\frac{(m - n)\pi x}{L}\right]\Bigg|_{-L}^L = 0 \end{aligned}$$
[each cosine is struck through with an arrow to "0": the difference between $x = L$ and $x = -L$ vanishes]
and, for $m = n$,
$$\int_{-L}^L \dots\dd x = \frac{1}{2}\int_{-L}^L \sin\left(\frac{2n\pi}{L}x\right)\dd x = \begin{cases} -\frac{1}{2}\cdot\frac{L}{2n\pi}\cos\left(\frac{2\pi n}{L}x\right)\Big|_{-L}^L = 0 & n \ne 0 \\ 0 & n = 0 \end{cases}$$
Therefore, $\left\{1, \cos\left(\frac{n\pi x}{L}\right), \sin\left(\frac{n\pi x}{L}\right)\right\}$ is orthogonal.
 
## HW 51 — Fourier coefficients; sawtooth example worked
_File `20261122_000207.jpg`. Both pages "Fourier coefficients", section 2.0._
 
**Left page.**
 
**N.** We now return to the question of finding the Fourier coefficients. The coefficients are given by:
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x, \qquad a_m = \frac{\int_{-L}^L \cos\left(\frac{m\pi x}{L}\right)f(x)\dd x}{\int_{-L}^L \cos^2\left(\frac{m\pi x}{L}\right)\dd x}, \qquad b_m = \frac{\int_{-L}^L \sin\left(\frac{m\pi x}{L}\right)f(x)\dd x}{\int_{-L}^L \sin^2\left(\frac{m\pi x}{L}\right)\dd x}$$
 
**P.** For $a_0$, we multiply both sides of the Fourier series by 1 (in orthogonal set) and integrate over $[-L, L]$:
$$\int_{-L}^L f(x)\dd x = a_0\int_{-L}^L 1\dd x + \sum(0 + 0) = 2La_0$$
implying the result. Refer the lecture workbook (W7L2) for the proofs for $a_m, b_m$.
[W7L2: week 7, lecture 2 of the CN workbook]
 
**Right page.**
 
**Ex.** (continued) Consider $f(x) = 2x$, $x \in [0, 1]$, $f(x + 1) = f(x)$. Then $p = 1 = 2L \Rightarrow L = 1/2$.
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x = 1\int_{-1/2}^{1/2} f(x)\dd x = \int_0^{2L}\frac{1}{2L}f(x)\dd x \ \text{[change period]} = \int_0^1 f(x)\dd x = \int_0^1 2x\dd x = 1$$
For $n \ge 1$:
$$a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = \frac{1}{L}\int_0^{2L} f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 2x\cos(2\pi xn)\dd x = \dots \text{(integrate by parts)} = 0$$
$$\begin{aligned} b_n &= \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 2x\sin(2n\pi x)\dd x \\ &= 4x\cdot\frac{-1}{2n\pi}\cos(2n\pi x)\Big|_0^1 - 4\int_0^1 \frac{-1}{2n\pi}\cos(2n\pi x)\dd x = \dots = -2/n\pi. \end{aligned}$$
[the second integral is struck through with an arrow to "0"]
Thus
$$f(x) = 1 + \sum_{n=1}^\infty -\frac{2}{n\pi}\sin\left(\frac{n\pi x}{L}\right).$$
[$L = 1/2$ here, so $\sin(n\pi x/L) = \sin(2n\pi x)$, matching HW 48.]
 
## HW 52 — Half sine-wave rectifier; summary on finding Fourier series
_File `20261122_000216.jpg`. Left page "Fourier coefficients", right page "Summary on finding Fourier series"; both section 2.0. The last line of the left page is near the page edge but readable._
 
**Left page.**
 
**Ex.** Consider the half sine-wave rectifier.
$$f(x) = \begin{cases} 0 & -\pi \le x \le 0 \\ \sin x & 0 < x < \pi \end{cases}, \qquad f(x + 2\pi) = f(x), \quad p = 2\pi, \quad L = \pi$$
 
*Figure (half-wave rectified sine).* Horizontal axis with ticks $-\pi$, $\pi$, $2\pi$, $3\pi$ and a vertical axis with an arrow up. Positive sine arches on $(-2\pi, -\pi)$, $(0, \pi)$ and $(2\pi, 3\pi)$, flat at zero in between. [The drawing places arches between each pair of labelled ticks a little loosely; the formula fixes them on $(2k\pi, (2k+1)\pi)$.]
 
The Fourier series is given by:
$$a_0 = \int_{-\pi}^\pi \frac{1}{2\pi}f(x)\dd x = \frac{1}{2\pi}\int_0^\pi \sin x\dd x = \dots = \frac{1}{\pi}$$
$$\begin{aligned} a_n &= \frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos(nx)\dd x \quad (n \ne 1) \\ &= \dots = \frac{1}{2\pi}\int_0^\pi \sin\bigl((n + 1)x\bigr) + \sin\bigl((1 - n)x\bigr)\dd x \\ &= \dots = -\frac{1}{2\pi}\begin{cases} 0 & n = 2k + 1 \\ -2/(2k + 1) + 1/(2k - 1) & n = 2k \end{cases} \end{aligned}$$
Thus $a_2 = -2/3\pi$, $a_3 = 0$, etc. We can show $a_1 = 0$.
[possible error: the even case should be $\frac{1}{\pi}\cdot\frac{-2}{(2k-1)(2k+1)}$, i.e. $a_n = -\frac{2}{\pi(n^2 - 1)}$, which gives the stated $a_2 = -2/(3\pi)$. The bracket as written, $-\frac{1}{2\pi}\bigl(-\frac{2}{2k+1} + \frac{1}{2k-1}\bigr)$, gives $-\frac{1}{2\pi}\cdot\frac13$ at $k = 1$ and does not match.]
$$b_n = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin(nx)\dd x \quad (n \ne 1) = \frac{1}{2\pi}\int_0^\pi \cos\bigl((1 - n)x\bigr) - \cos\bigl((n + 1)x\bigr)\dd x = \dots \text{(similar)} = 0$$
$$b_1 = 1/\pi\int_{0}^\pi \sin^2 x\dd x = \dots = 1/2$$
[the lower limit of the $b_1$ integral is written "$-0$" with a blacked-out mark; read as $0$]
So
$$f(x) = \frac{1}{\pi} + \frac{1}{2}\sin x - \frac{2}{\pi}\sum_{k=1}^\infty \frac{\cos(2kx)}{(2k - 1)(2k + 1)}.$$
[the summation index is written $n=1$ under the sum while the summand uses $k$]
 
**Right page.**
 
**N.** We have shown (in summary) that if $f(x) = f(x + 2L)$ $\forall x \in \R$ then
$$f(x) = a_0 + \sum_{n=1}^\infty \left(a_n\cos\left(\frac{n\pi x}{L}\right) + b_n\sin\left(\frac{n\pi x}{L}\right)\right)$$
where
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x, \qquad a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x, \qquad b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x$$
(or, for general $a$)
$$a_0 = \frac{1}{2L}\int_a^{a+2L} f(x)\dd x, \qquad a_n = \frac{1}{L}\int_a^{a+2L} f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x, \qquad b_n = \frac{1}{L}\int_a^{a+2L} f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x$$
 
## HW 53 — Convergence of Fourier series
_File `20261122_000223.jpg`. Both pages "Convergence of Fourier series", section 2.0. The right page has text only in its top third._
 
**Left page.**
 
**N.** We do not know whether the Fourier series of $f$ actually converges to $f$. It turns out that the series does converge provided that $f$ is piecewise continuous on $[-L, L]$.
 
**Def.** Let $f$ be a function. Then $f$ is *piecewise continuous* on the interval $[-L, L]$ if $f$ is comprised of a finite number of continuous functions, and at each point of discontinuity the one sided limits $\lim_{x \to d^\pm} f$ both exist. The limits $\lim_{x \to L^-} f$, $\lim_{x \to -L^+} f$ must also exist.
 
*Figure (a piecewise continuous function on $[-L, L]$).* Horizontal axis with arrows at both ends; dashed vertical lines at $-L$ (left) and $+L$ (right), labelled below. Vertical axis with arrows at both ends. Pieces from left to right: (1) from a filled dot on the dashed line at $-L$ (moderate height) the curve rises in an S-shape to a filled dot higher up (closed right end); (2) the next piece starts with an open circle slightly lower than (1)'s start, falls steeply below the axis and runs flat to a filled dot just left of the vertical axis, at its lowest point; (3) from a filled dot on the vertical axis above the origin the curve rises a little, then falls into a dip and ends with an open circle; (4) from an open circle higher up, the curve dips and rises to a filled dot on the dashed line at $+L$. So there are jumps between pieces, each with one-sided limits, and the end values at $\pm L$ exist.
 
**Def.** If $f$ is piecewise continuous on the interval $[-L, L]$, and is periodic with period $2L$, then its Fourier series converges to
$$\frac{1}{2}\bigl(f(x^+) + f(x^-)\bigr)$$
at every $x$ where $f$ has left & right derivatives.
 
**Right page.**
 
**N.** If the one-sided limits of $f$ exist at $x = a$, we define $f(a^\pm) = \lim_{x \to a^\pm} f(x)$.
If $f$ is continuous on $a$, then $f(a^+) = f(a^-) = f(a)$. Thus if $f$ is continuous at $a$, the Fourier series at $a$ converges to $f(a)$.
If $f$ is NOT continuous at some $d$, then the Fourier series converges to $\frac{1}{2}\bigl(f(d^+) + f(d^-)\bigr)$.
 
## HW 54 — Convergence examples; odd and even functions
_File `20261122_000230.jpg`. Left page "Convergence of Fourier series" (section 2.0), right page "Odd and even functions" (section 2.1). Lower third of the right page blank._
 
**Left page.**
 
**Ex.** (continued) Consider the following periodic function:
 
*Figure (sawtooth, as in HW 48).* Axes with $y$-tick 2 and $x$-ticks 0, 1, 2, 3; three ramps rising from $(n, 0)$ to $(n+1, 2)$ with dashed vertical lines at $x = 1, 2, 3$. Annotated $f(x) = 2x$, $0 < x < 1$, $f(x + 1) = f(x)$.
 
Recall that the Fourier series of $f$ is
$$f(x) = 1 - \frac{2}{\pi}\sum_{n=1}^\infty \frac{\sin(2n\pi x)}{n}$$
The series converges to $f$ at all points except at the points of discontinuity $x = \alpha \in \Z$. At these points, the series converges to $\frac{1}{2}(2 + 0) = 1$.
 
**Ex.** (continued) Consider the half sine-wave rectifier. Recall its Fourier series is given by
$$f(x) = \frac{1}{\pi} + \frac{1}{2}\sin x - \frac{2}{\pi}\left(\frac{1}{3}\cos(2x) + \frac{1}{15}\cos(4x) + \dots\right)$$
Note that $f$ is everywhere continuous and that the left and right derivatives exist at every point. Thus the Fourier series converges to $f$ for all $x$.
 
**Rem.** Thus for $-\pi < x < 0$ we have
$$0 = \frac{1}{\pi} + \frac{1}{2}\sin x - \frac{2}{\pi}(\dots)$$
which implies
$$\sin(x) = -\frac{2}{\pi} + \frac{4}{\pi}\left(\frac{1}{3}\cos(2x) + \frac{1}{15}\cos(4x) + \dots\right)$$
[valid for $-\pi < x < 0$, as stated above; the notes do not restate the range]
 
**Right page.**
 
**Def.** A function is *even* if $f(-x) = f(x)$ for all $x$. A function is *odd* if $f(-x) = -f(x)$ for all $x$.
 
**Rem.** Even functions are symmetric about the $y$-axis. Odd functions are symmetric about the origin.
 
**N.** We describe some properties of odd and even functions:
1) $\displaystyle\int_{-a}^a f = \begin{cases} 2\int_0^{2a} f & \text{if } f \text{ even} \\ 0 & \text{if } f \text{ odd} \end{cases}$
[possible error: the upper limit should be $a$: $2\int_0^a f$.]
2) If $f$ and $g$ are even, $f \times g$ is even.
3) If $f$ and $g$ are odd, $f \times g$ is [blacked-out word] even.
4) If $f$ is odd, $g$ is even (WLOG), $f \times g$ is odd.
**N.** Note that $1, \cos\left(\frac{\pi x}{L}\right), \cos\left(\frac{2\pi x}{L}\right), \dots$ are even; $\sin\left(\frac{\pi x}{L}\right), \sin\left(\frac{2\pi x}{L}\right), \dots$ are odd.
 
## HW 55 — Fourier cosine series (even) and Fourier sine series (odd)
_File `20261122_000242.jpg`. Left page "Fourier cosine series (even)", right page "Fourier sine series (odd)"; both section 2.1._
 
**Left page.**
 
**N.** Suppose $f$ is periodic with period $2L$ and is also even. Thus $f(x + 2L) = f(x)$, $f(-x) = f(x)$, $x \in \R$. Then,
$$b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = 0$$
[annotations: "even" over $f(x)$, "odd" over the sine, "odd" under the product]
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x = \frac{1}{L}\int_0^L f(x)\dd x$$
$$a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x$$
[annotations: "even" over $f$ and over the cosine, "even" under the product]
and so
$$f(x) = a_0 + \sum_{n=1}^\infty a_n\cos\left(\frac{n\pi x}{L}\right)\dd x$$
[a stray "$\dd x$" at the end of the series]
where $a_0, a_n$ are given as above. This is called the *Fourier cosine series* (for even functions).
 
**Right page.**
 
**N.** Similarly, suppose $f$ is periodic with period $2L$ and is odd. Thus $f(x + 2L) = f(x)$, $f(-x) = -f(x)$, $x \in \R$. Then,
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x = 0, \qquad a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = 0$$
[annotations: "odd" over $f$, "even" over the cosine, "odd" under the product]
$$b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x$$
[annotations: "odd" over $f$ and over the sine, "even" under the product]
and so
$$f(x) = \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right)\dd x$$
[again a stray "$\dd x$"]
where $b_n$ is as above. This is called the *Fourier sine series* (for odd functions).
 
## HW 56 — Fourier cosine and sine series: examples
_File `20261122_000251.jpg`. Left page "Fourier cosine series (example)", right page "Fourier sine series (example)"; both section 2.1._
 
**Left page.**
 
**Ex.** Consider
$$f_1(x) = \begin{cases} x & \text{if } 0 \le x < 1 \\ -x & \text{if } -1 < x < 0 \end{cases} = \abs{x}$$
defined on $(-1, 1)$, and $f_1(x + 2) = f_1(x)$.
 
*Figure (triangle wave).* Horizontal axis with ticks $-2$, $-1$, $1$, $2$; vertical axis with an arrow up. A zig-zag: zero at $x = -2, 0, 2$ and peaks at $x = -1$ and $x = 1$ (height 1), with dotted vertical lines from the peaks at $x = \pm1$ down to the axis; the line continues beyond $x = 2$ rising and beyond $x = -2$ (rising to the left).
 
Note that $f_1$ is even with period 2. Thus we use the Fourier cosine series
$$f_1(x) = a_0 + \sum_{n=1}^\infty a_n\cos(n\pi x) \quad \leftarrow \text{note } L = 1$$
where
$$a_0 = \frac{1}{L}\int_0^L f_1(x)\dd x = \int_0^1 x\dd x = \frac{1}{2}$$
$$a_n = \frac{2}{L}\int_0^L f_1(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 x\cos(n\pi x)\dd x = \dots \text{(integrate by parts)} = \begin{cases} 0 & \text{if } n = 2m \\ \dfrac{-4}{(2m + 1)^n\pi^2} & \text{if } n = 2m + 1 \end{cases}$$
[small blacked-out boxes after "$a_0$", "$a_n$" and in front of two integrals (crossed-out factors)]
[possible error: the denominator should be $(2m + 1)^2\pi^2$; the exponent reads $n$.]
 
**Right page.**
 
**Ex.** Consider
$$f_2(x) = \begin{cases} x & \text{if } -1 < x < 1 \\ f_2(x + 2) & \forall x \in \R \end{cases}$$
 
*Figure (sawtooth, odd, period 2).* Horizontal and vertical axes crossing at the centre. Parallel straight segments of slope 1, each over an interval of length 2, from below the axis up to above it, with dotted vertical lines at the jumps (at odd integers). About five segments are drawn, with the middle one through the origin. No tick labels.
 
Note that $f_2$ is odd [the word "odd" is written above a blacked-out word] with period 2. Thus we use the Fourier sine series
$$f_2(x) = \sum_{n=1}^\infty b_n\sin(n\pi x) \quad \leftarrow \text{note } L = 1.$$
where
$$b_n = \frac{2}{L}\int_0^L f_2(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 f_2(x)\sin(n\pi x)\dd x = \dots \text{(integrate by parts)} = -\frac{2}{n\pi}(-1)^n$$
 
**N.** Note the Fourier series for $g(x) = f_1(x) + f_2(x)$ is simply the sum of the cos. series for $f_1$ and the sin. series for $f_2$.
This holds for ANY periodic function $g$, where we can write $g = f_1 + f_2$ for some even $f_1$ (period $2L$) and some odd $f_2$ (period $2L$).
 
## HW 57 — Half-range expansions
_File `20261122_000300.jpg`. Both pages "Half-range expansions", section 2.2._
 
**Left page.**
 
**N.** Suppose we are given a function $f(x)$ that is only defined for $x \in [0, L]$. We may still be able to obtain a Fourier series decomposition, in which there are two ways to proceed.
1) Extend $f$ to an even periodic function $f_1$:
$$f_1(x) = f(x) \quad 0 \le x \le L; \qquad f_1(x + 2L) = f_1(x),\ f_1(-x) = f_1(x) \quad x \in \R$$
Then
$$f_1(x) = a_0 + \sum_{n=1}^\infty a_n\cos\left(\frac{n\pi x}{L}\right) \quad \text{for } x \in \R$$
and therefore
$$f(x) = a_0 + \sum_{n=1}^\infty a_n\cos\left(\frac{n\pi x}{L}\right) \quad \text{for } 0 \le x < L$$
where
$$a_0 = \frac{1}{L}\int_0^L f_1(x)\dd x = \frac{1}{L}\int_0^L f(x)\dd x, \qquad a_n = \frac{2}{L}\int_0^L f_1(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x$$
This is called the *half-range cosine series* for $f(x)$, $0 \le x < L$. (It is also the cosine series for the even periodic extension $f_1$ for $-\infty < x < \infty$.)
**Right page.**
 
**N.** We can also proceed as follows.
2) Extend $f$ to an odd periodic function $f_2$:
$$f_2(x) = f(x) \quad 0 \le x < L; \qquad f_2(x + 2L) = f_2(x),\ f_2(-x) = f_2(-x) \quad x \in \R$$
[possible error: the odd condition should read $f_2(-x) = -f_2(x)$.]
Then
$$f_2(x) = \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right) \quad \text{for } x \in \R$$
and therefore
$$f(x) = \sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right) \quad \text{for } 0 \le x < L$$
where
$$b_n = \frac{2}{L}\int_0^L f_2(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x$$
This is called the *half-range sine series* for $f(x)$, $0 \le x < L$. (It is also the sine series for the odd periodic extension $f_2$ for $-\infty < x < \infty$.)
 
## HW 58 — Half-range expansions: example $f(x) = x$ on $[0, 1]$
_File `20261122_000309.jpg`. Both pages "Half-range expansions", section 2.2._
 
**Left page.**
 
**Ex.** Consider $f(x) = x$ for $0 \le x \le 1$.
<u>Method 1</u>: half-range cosine series
$$f(x) = x = a_0 + \sum_{n=1}^\infty a_n\cos(n\pi x) \quad \text{for } 0 \le x < 1$$
where
$$a_0 = \frac{1}{L}\int_0^L f(x)\dd x = 1\int_0^1 x\dd x = \frac{1}{2}$$
$$a_n = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 x\cos(n\pi x)\dd x = \dots \text{(integration by parts)} = \frac{2}{(n\pi)^2}\bigl((-1)^n - 1\bigr) = \begin{cases} 0 & n = 2k \\ \dfrac{-4}{(2k + 1)^2\pi^2} & n = 2k + 1 \end{cases}$$
and so
$$x = \frac{1}{2} - \frac{4}{\pi^2}\sum_{k=0}^\infty \frac{\cos\bigl([2k + 1]x\bigr)}{(2k + 1)^2}$$
[possible error: the argument should be $(2k + 1)\pi x$; the $\pi$ is missing.]
Note that this is also the Fourier cosine series for the function $f_1(x)$ in the previous example.
 
**Right page.**
 
**Ex.** (continued)
<u>Method 2</u>: half-range sine series
$$f(x) = x = \sum_{n=1}^\infty b_n\sin(n\pi x) \quad \text{for } 0 \le x < 1$$
where
$$b_n = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = 2\int_0^1 x\sin\left(\frac{n\pi x}{1}\right)\dd x = \dots \text{(integration by parts)} = \frac{2}{n\pi}(-1)^n$$
[possible error: $2\int_0^1 x\sin(n\pi x)\dd x = -\frac{2}{n\pi}(-1)^n = \frac{2(-1)^{n+1}}{n\pi}$; the minus sign is missing here (HW 56 has it).]
Note that at $x = 1$, the Fourier series converges to $0$, not $1$. Also note that it is also the Fourier sine series for the function $f_2(x)$ in the previous example.
 
## HW 59 — Differentiating Fourier series
_File `20261122_000318.jpg`. Both pages "Differentiating Fourier series", section 2.3._
 
**Left page.**
 
**Def.** Suppose $f$ is periodic with period $2L$, and
$$f(x) = a_0 + \sum_{n=1}^\infty \left(a_n\cos\left(\frac{n\pi x}{L}\right) + b_n\sin\left(\frac{n\pi x}{L}\right)\right)$$
Here we suppose that $f'(x)$ is at least piecewise continuous. Then $f'(x)$ is also periodic with period $2L$, since
$$f'(x + 2L) = \lim_{h \to 0}\frac{f(x + 2L + h) - f(x + 2L)}{h} = \lim_{h \to 0}\frac{f(x + h) - f(x)}{h} = f'(x)$$
Thus we can also expand $f'$ in a Fourier series:
$$f'(x) = A_0 + \sum_{n=1}^\infty \left(A_n\cos\left(\frac{n\pi x}{L}\right) + B_n\sin\left(\frac{n\pi x}{L}\right)\right)$$
 
**N.** We now want to know how the two series are related. Consider
$$A_0 = \frac{1}{2L}\int_{-L}^L f'(x)\dd x = \frac{1}{2L}\bigl[f(x)\bigr]_{-L}^L = \frac{1}{2L}\bigl(f(L) - f(-L)\bigr)$$
[the page ends here; $f(L) = f(-L)$ by periodicity, so $A_0 = 0$, which is used on the right page ("$0 + \dots$") but not written]
 
**Right page.**
 
**N.** (continued)
$$\begin{aligned} A_n &= \frac{1}{L}\int_{-L}^L f'(x)\cos\left(\frac{n\pi x}{L}\right)\dd x = \frac{1}{L}\int_{-L}^L \cos\left(\frac{n\pi x}{L}\right)\cdot\dd\bigl(f(x)\bigr) \\ &= \frac{1}{L}f(x)\cos\left(\frac{n\pi x}{L}\right)\Big|_{-L}^L - \frac{1}{L}\int_{-L}^L f(x)\dd\left(\cos\left(\frac{n\pi x}{L}\right)\right) \\ &= \frac{1}{L}\bigl[f(L)\cos(n\pi) - f(-L)\cos(-n\pi)\bigr] - \frac{1}{L}\int_{-L}^L f(x)\left(-\frac{n\pi}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\dd x \\ &= \frac{n\pi}{L}\cdot\frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = \frac{n\pi}{L}b_n \end{aligned}$$
[the bracket $[f(L)\cos(n\pi) - f(-L)\cos(-n\pi)]$ is struck through with an arrow to "0"]
$$B_n = \frac{1}{L}\int_{-L}^L f'(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = \dots \text{(by parts, similar to } A_n) = \frac{-n\pi}{L}a_n$$
This is exactly what we obtain if we differentiate $f$ term by term.
$$f'(x) = 0 + \sum_{n=1}^\infty \left[-\frac{n\pi}{L}a_n\sin\left(\frac{n\pi x}{L}\right) + \frac{n\pi}{L}b_n\cos\left(\frac{n\pi x}{L}\right)\right]$$
 
## HW 60 — Differentiating Fourier series: triangle-wave example
_File `20261122_000330.jpg`. Both pages "Differentiating Fourier series", section 2.3._
 
**Left page.**
 
**Ex.** Consider
$$f(x) = \begin{cases} x + \pi/2 & \text{if } -\pi < x < 0 \\ -x + \pi/2 & \text{if } 0 < x < \pi \end{cases}$$
where $f(x + 2\pi) = f(x)$ for $-\infty < x < \infty$.
 
**Def.** If $f$ is even, $f'$ is odd. If $f$ is odd, $f'$ is even.
[a curved arrow runs from the example down to this box]
 
Thus $p = 2L = 2\pi$. Note $f$ is even, so $b_n = 0$. For $a_n$, we have:
$$a_0 = \frac{1}{2L}\int_{-L}^L f(x)\dd x = \frac{1}{L}\int_0^L f(x)\dd x = \frac{1}{\pi}\int_0^\pi \left(-x + \frac{\pi}{2}\right)\dd x = 0$$
$$\begin{aligned} a_n &= \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x \quad \text{[“even” over the integrand]} \\ &= \dots = \frac{2}{\pi}\int_0^\pi \left(-x + \frac{\pi}{2}\right)\cos(nx)\dd x = \dots \text{(integration by parts)} \\ &= -\frac{2}{n^2\pi}\bigl((-1)^n - 1\bigr) = \begin{cases} 0 & \text{if } n = 2k \\ 4/\bigl((2k + 1)^2\pi\bigr) & \text{if } n = 2k + 1 \end{cases} \end{aligned}$$
and therefore
$$f(x) = \frac{4}{\pi}\left[\cos x + \frac{1}{9}\cos 3x + \frac{1}{25}\cos 5x + \dots\right]$$
 
**Right page.**
 
**Ex.** (continued) Note that
$$f'(x) = \begin{cases} 1 & \text{if } -\pi < x < 0 \\ -1 & \text{if } 0 < x < \pi \end{cases}$$
where $f'(x + 2\pi) = f'(x)$ for $-\infty < x < \infty$.
Note $f$ is continuous, while $f'$ is piecewise cts. Note $f$ is even, while $f'$ is odd.
Differentiating the Fourier series of $f$ gives:
$$f'(x) = \frac{4}{\pi}\left[-\sin x - \frac{3}{9}\sin 3x - \frac{5}{25}\sin 5x\right] = -\frac{4}{\pi}\left[\sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x\right] = -\frac{4}{\pi}\sum_{k=0}^\infty \frac{\sin\bigl([2k + 1]x\bigr)}{2k + 1}$$
<u>Check</u>: $f'$ is odd with $p = 2\pi$, so $f'(x) = \sum_{n=1}^\infty B_n\sin(nx)$ where
$$B_n = \frac{1}{L}\int_{-L}^L f'(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = \dots \text{(by parts)} = \frac{2}{n\pi}\bigl((-1)^n - 1\bigr) = \begin{cases} 0 & n = 2k \\ -4/\bigl((2k + 1)\pi\bigr) & n = 2k + 1 \end{cases}$$
[annotations: "odd" over $f'$ and over the sine, "even" under the product]
which is identical to the series before!
 
## HW 61 — Application: forced oscillations
_File `20261122_000339.jpg`. Both pages "Example on forced oscillations", section 2.4._
 
**Left page.**
 
**Ex.** Consider the application of Fourier series on a spring with forced oscillations.
 
*Figure (forced mass–spring–damper).* A vertical wall line on the left. From the wall a horizontal line runs right into a coil spring (drawn as loops), ending at a dot labelled $m$ (the mass). Above, a small rectangle labelled $c$ (dashpot/damper) is connected by a line from the wall side across the top and down to the mass. From the mass an arrow points right, labelled $r(t)$ (the forcing). Below the spring, a short dashed vertical tick marks the equilibrium position with a small arrow to the right, labelled $y$ (displacement).
 
Forced oscillations are described by the differential equation:
$$m\ddot{y}(t) = -ky(t) - c\dot{y}(t) + r(t)$$
where $y(t)$: position, $c$: damping coefficient, $k$: restoring force by Hooke's law.
Now suppose $r(t)$ is periodic with period $2L$ and has been applied for sufficient time so that the system is at a steady state (i.e. all effects of ICs died away). Then $y$, $\dot{y}$ and $\ddot{y}$ [blacked-out word] will be periodic with period $2L$, and we can substitute in the Fourier series and equate coefficients to obtain the solution.
 
**Right page.**
 
**Ex.** Consider
$$\ddot{y}(t) + \frac{1}{50}\dot{y}(t) + 25y(t) = r(t) \quad \text{where} \quad r(t) = \begin{cases} t + \pi/2 & \text{if } -\pi < t < 0 \\ -t + \pi/2 & \text{if } 0 < t < \pi \end{cases}$$
and $r(t + 2\pi) = r(t)$ for $-\infty < t < \infty$.
We first solve the DE:
<u>$y_H$</u>: $\lambda^2 + \frac{1}{50}\lambda + 25 = 0$
$$\Rightarrow \lambda = \frac{1}{100}\bigl(-1 \pm i\underbrace{\sqrt{249\,999}}_{\beta}\bigr) \Rightarrow y_H(t) = e^{-t/100}\left(A\cos\left(\frac{\beta}{100}t\right) + B\sin\left(\frac{\beta}{100}t\right)\right)$$
We know that $r$ has Fourier series
$$r(t) = \frac{4}{\pi}\left[\cos t + \frac{1}{9}\cos 3t + \frac{1}{25}\cos 5t\right](+\dots)$$
By the method of undetermined coefficients, try
$$y_p(t) = a_0 + \sum\bigl(a_n\cos(nt) + b_n\sin(nt)\bigr)$$
$$y_p'(t) = \sum_{n=1}^\infty \bigl(-na_n\sin(nt) + nb_n\cos(nt)\bigr), \qquad y_p''(t) = \sum_{n=1}^\infty \bigl(-n^2a_n\cos(nt) - n^2b_n\sin(nt)\bigr)$$
We now substitute into the ODE:
$$\text{LHS} = \sum_{n=1}^\infty \left(-n^2a_n + \frac{1}{50}nb_n + 25a_n\right)\cos(nt) + \left(-n^2b_n - \frac{1}{50}na_n + 25b_n\right)\sin(nt) + 25a_0$$
$$= \text{RHS} = \frac{4}{\pi}\left(\cos t + \frac{1}{9}\cos 3t + \frac{1}{25}\cos 5t + \dots\right)$$
[this $r$ is the function of HW 60 with $x \to t$; its series is taken from there]
 
## HW 62 — Forced oscillations (continued): equating coefficients
_File `20261122_000346.jpg`. Left page "Example on forced oscillations", section 2.4. The right page is blank._
 
**Ex.** (continued) Equating coefficients gives
<u>constant</u>: $25a_0 = 0 \Rightarrow a_0 = 0$
<u>$\cos(nt)$</u>:
if $n$ is even, $-(2k)^2a_{2k} + \frac{1}{50}(2k)b_{2k} + 25a_{2k} = 0$
if $n$ is odd, $-(2k + 1)^2a_{2k+1} + \frac{1}{50}(2k + 1)b_{2k+1} + 25a_{2k+1} = \dfrac{4}{(2k + 1)^2\pi}$ [a small blacked-out box before the 4]
<u>$\sin(nt)$</u>:
if $n$ is even, $-(2k)^2b_{2k} - \frac{1}{50}(2k)a_{2k} + 25b_{2k} = 0$
if $n$ is odd, $-(2k + 1)^2b_{2k+1} - \frac{1}{50}(2k + 1)a_{2k+1} + 25b_{2k+1} = 0$
$\Rightarrow$ If $n$ even, $a_{2k} = b_{2k} = 0$
If $n$ odd, $k = 2$, $b_5 = \dfrac{8}{5\pi}$, $a_5 = 0$
If $n$ odd, $k \ne 2$,
$$b_{2k+1} = \frac{1}{2500\bigl(25 - (2k + 1)^2\bigr)^2 + (2k + 1)^2}\cdot\frac{200}{(2k + 1)\pi}$$
$$a_{2k+1} = \frac{25 - (2k + 1)^2}{50\bigl(25 - (2k + 1)^2\bigr)^2 + (2k + 1)^2}\cdot\frac{200}{(2k + 1)^2\pi}$$
[possible error: solving the two odd-$n$ equations gives $a_{2k+1} = \dfrac{25 - (2k+1)^2}{2500\bigl(25 - (2k+1)^2\bigr)^2 + (2k+1)^2}\cdot\dfrac{10\,000}{(2k+1)^2\pi}$; the $b_{2k+1}$ formula and $b_5$, $a_5$ check out.]
In this way we determine an approx. solution of the ODE in terms of a Fourier series. We calculate as many $a_n, b_n$ as needed.
 
## HW 63 — Introduction to vector calculus; level surfaces
_File `20261122_000401.jpg`. Left page "Introduction to vector calculus" (section 3.1), right page "Level surfaces" (section 3.2). Unit vectors are written $\vec\imath, \vec\jmath, \vec k$ and vectors underlined in the notes; transcribed with `\vect{}`._
 
**Left page.**
 
**Def.** A *scalar field* is a function of position $(x, y, z)$ defined through some region in space. We know this formally as some function $f: \R^n \to \R$, where $n$ is typically 3.
 
**Def.** A *vector field* is a vector function of position $(x, y, z)$ defined through some region in space. We know this formally as some function $f: \R^n \to \R^n$, where $n$ is typically 3.
 
**Rem.** Scalar and vector fields may also depend on some time $t$, i.e. our variables are $(x, y, z, t)$.
 
**Def.** We define the *gradient/del operator* by
$$\nabla = \frac{\partial}{\partial x}\vec{\imath} + \frac{\partial}{\partial y}\vec{\jmath} + \frac{\partial}{\partial z}\vec{k}$$
 
**Def.** We define the *divergence operator* by
$$\nabla\cdot\vect{f} = \frac{\partial f_1}{\partial x} + \frac{\partial f_2}{\partial y} + \frac{\partial f_3}{\partial z}$$
 
**Def.** We define the *curl operator* by
$$\nabla\times\vect{f} = \begin{vmatrix} \vec{\imath} & \vec{\jmath} & \vec{k} \\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\ f_1 & f_2 & f_3 \end{vmatrix}$$
 
**Right page.**
 
**Def.** Given a scalar field $f: \R^n \to \R$ and a point $p = (x_1, \dots, x_n)$, the equation $f(x_1, \dots, x_n) = c \in \R$ defines a two-dimensional surface $S$ passing through the point $p$. (Analogous to normal) This surface $S$ is called a *level surface* for $f$.
 
**Def.** $\nabla f$ evaluated at $P$ is a vector perpendicular to the level surface $S$.
↳ The direction of $\nabla f$ is the direction of greatest rate of increase
↳ The magnitude of $\nabla f$ is the rate of greatest increase.
 
*Figure (geometric interpretation of the gradient, divergence and curl at $P$).* A closed kidney/bean-shaped curve labelled $S$ (the level surface seen edge-on), with an indentation on the lower right. A point $P(x_0, y_0, z_0)$ inside it, near the upper middle. From $P$ a long vertical arrow points straight up, crossing the top of the curve, labelled $\nabla f$. Just above $P$ on that arrow, a small curling arrow ("C" shape) labelled $\nabla\times f$ (rotation about the gradient line). A short diagonal arrow from $P$ up and to the right, labelled $\nabla\cdot f$. Short arrows from $P$ pointing left and down (outflow, with the diagonal one: divergence as net outflow). Caption: "A geometric interpretation of the gradient $\nabla f$. (with div., curl, at $P$)".
 
**Def.** The divergence measures the net flow of a vector field at a point. The curl measures the rotation of flow of a vector field at a point.
 
## HW 64 — Flux vector fields; Laplacian; Gauss' divergence theorem (small-box argument, start)
_File `20261122_000409.jpg`. Left page "Flux vector fields" (section 3.3), right page "Gauss' divergence theorem" (section 3.4)._
 
**Left page.**
 
**Def.** If we have some substance 'flowing' through space, it is useful to introduce the *flux vector field* $\vect{J}(x, y, z, t)$, where
$$\vect{J}\cdot\vect{n}\,\delta S = \text{amount of substance flowing across } \delta S \text{ per unit time} = \text{flux across } \delta S.$$
 
**Ex.** In a moving fluid with velocity field $\vect{v}$ and density (scalar) field $\rho$, then $\vect{J} = \rho\vect{v}$ is the mass flux vector field.
 
**Def.** When we add the fluxes through all $\delta S$ making up a surface $S$, we get the flux over the surface. The <u>total flux</u> is therefore given by:
$$\iint_S \vect{J}(x, y, z)\cdot\vect{n}(x, y, z)\dd\vect{S} \quad \text{or simply} \quad \iint_S \vect{J}\cdot\vect{n}\dd\vect{S}.$$
[possible error: with $\vect n$ written out, the area element should be the scalar $\dd S$; $\dd\vect S$ already means $\vect n\dd S$.]
 
**Def.** (continued from 3.1) We define the *Laplacian operator* by
$$\nabla^2 = \frac{\partial^2}{\partial x^2}\vec{\imath} + \frac{\partial^2}{\partial y^2}\vec{\jmath} + \frac{\partial^2}{\partial z^2}\vec{k}$$
[possible error: the Laplacian is the scalar operator $\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$, without unit vectors.]
 
**Right page.**
 
**N.** Consider what happens if $S$ is the surface of a small rectangular box, with sides parallel to the basis (canonical) coordinates.
 
*Figure (small box for the divergence theorem).* Right-handed axes from an origin: $z$ up, $y$ to the right, $x$ drawn towards the lower left. A small box drawn in dashed lines above and to the right of the origin, its eight corners labelled. Readable labels: $A$ (front bottom left), $B$ (front bottom right), $D$ (front top left), $H$ (back top left), $G$ (back top right), $E$ (centre, on an inner edge), $F$ (back right, middle). The label $C$ (front top right) is a small faint mark and not certain. [ambiguous drawing: the corner labels are small and partly overlapping; the corner positions are clear in CN §3.4 (MATH2011 p. 57), which should be used to label the redrawn box. From the text: $ABCD$ is the face at $x + \Delta x$ (outward normal $\vec\imath$), $EFGH$ the face at $x - \Delta x$, $|BF| = 2\Delta x$, $|AB| = 2\Delta y$, $|BC| = 2\Delta z$.]
 
Suppose $P$ is the centre of the box. Suppose $\abs{BF} = 2\Delta x$, $\abs{AB} = 2\Delta y$, $\abs{BC} = 2\Delta z$. Let $V$ be enclosed by $S$.
We estimate the flux of $V$ over the face $ABCD$:
$$\vect{J}_{(x + \Delta x, y, z)} = \vect{J}(x, y, z) + \Delta x\frac{\partial\vect{J}}{\partial x}$$
[a blacked-out word after $\vect J$]
The outward unit normal vector on $ABCD$ is $\vect{n} = \vec{\imath}$. The area of the face is $\delta S = 4\Delta y\Delta z$.
$$(\vect{J}\cdot\vect{n})\,\delta S_{\text{left}} = J_1(x, y, z)\,4\Delta y\Delta z + \partial J_1/\partial x\,4\Delta x\Delta y\Delta z$$
For the flux over $EFGH$:
$$\vect{J}(x - \Delta x, y, z) = \vect{J}(x, y, z) - \Delta x\,\partial\vect{J}/\partial x, \qquad (\vect{J}\cdot\vect{n})\,\delta S_{\text{right}} = -J_1(x, y, z)\,4\Delta y\Delta z + \partial J_1/\partial x\,4\Delta x\Delta y\Delta z$$
So the flux out over $ABCD$ and $EFGH$ is
$$(\vect{J}\cdot\vect{n})\,\delta S_{\text{left}} + (\vect{J}\cdot\vect{n})\,\delta S_{\text{right}} = \frac{\partial J_1}{\partial x}\times 8\Delta x\Delta y\Delta z = \frac{\partial J_1}{\partial x}\delta V.$$
[the faces are labelled "left" ($ABCD$) and "right" ($EFGH$) although they are the front and back faces in $x$]
 
## HW 65 — Gauss' divergence theorem (completed); sphere example
_File `20261122_000415.jpg`. Both pages "Gauss' divergence theorem", section 3.4. Lower third of both pages blank._
 
**Left page.**
 
**N.** Similarly for the other faces: The flux out over $BCGF$ and $ADHE$ is
$$(\vect{J}\cdot\vect{n})\,\delta S_{\text{front}} + (\vect{J}\cdot\vect{n})\,\delta S_{\text{rear}} = \frac{\partial J_2}{\partial y}\delta V$$
The flux out over $ABFE$ and $DCGH$ is
$$(\vect{J}\cdot\vect{n})\,\delta S_{\text{top}} + (\vect{J}\cdot\vect{n})\,\delta S_{\text{bottom}} = \frac{\partial J_3}{\partial z}\delta V$$
The total flux out of $V$ over $S$ is thus
$$\sum(\vect{J}\cdot\vect{n})\,\delta S = \left(\frac{\partial J_1}{\partial x} + \frac{\partial J_2}{\partial y} + \frac{\partial J_3}{\partial z}\right)\delta V = (\nabla\cdot\vect{J})\,\delta V$$
 
**N.** When considering a general surface $S$ enclosing a 3-D region $V$, we can divide $V$ into 'many tiny boxes'. Taking the limit as the boxes grow smaller we have the result:
$$\oiint_S \vect{J}\cdot\vect{n}\dd S = \iiint_V \operatorname{div}\vect{J}\dd V$$
 
**Right page.**
 
**Ex.** Consider $\vect{J}(x, y, z) = \alpha(x\vec{\imath} + y\vec{\jmath} + z\vec{k}) = \alpha\vect{r}$. Let $S$ be the surface of the sphere centred at the origin with radius $a > 0$. Note that $\vect{r}$, $\vect{J}$ and $\vect{n}$ are all pointed radially out from the origin.
$$\vect{n} = \frac{\vect{r}}{\norm{\vect{r}}} = \frac{\vect{r}}{a} \Rightarrow \vect{J}\cdot\vect{n} = \alpha\vect{r}\cdot\frac{\vect{r}}{a} = \frac{\alpha}{a}\norm{\vect{r}}^2 = \alpha a.$$
Therefore,
$$\oiint_S \vect{J}\cdot\vect{n}\dd S = \alpha a\oiint_S \dd S \ [\leftarrow \text{area of sphere } S] = \alpha a(4\pi a^2) = \alpha 4\pi a^3$$
$$\iiint_V \nabla\cdot\vect{J}\dd V = 3\alpha\iiint_V \dd V \ [\leftarrow \text{volume of sphere } S] = 3\alpha\cdot\left(\tfrac{4}{3}\pi a^3\right) = \alpha 4\pi a^3$$
which are identical as expected.
[`\oiint` needs the `esint` package or a macro; see the notation proposals in the inventory]
 
## HW 66 — A conservation law; incompressible fluid
_File `20261122_000429.jpg`. Both pages "A conservation law", section 3.5._
 
**Left page.**
 
**N.** Consider some substance flowing through space, with density $\rho(x, y, z, t)$ and flux vector field $\vect{J}(x, y, z, t)$.
 
*Figure 1 (volume element).* A point $O$ (origin) with an arrow labelled $\vect r$ to a small hatched blob labelled $\delta V$, up and to the right.
The amount of substance in volume element $\delta V$ at $(x, y, z)$ at time $t$ is $\rho(x, y, z, t)\,\delta V$.
 
*Figure 2 (surface element).* A point $O$ with an arrow $\vect r$ to a small hatched surface patch (drawn as a lumpy hatched blob, $\delta S$). From the patch two arrows: one up and to the right labelled $\vect n$ (unit normal), one horizontal to the right labelled $\vect J$.
The amount of substance flowing per unit time out across $\delta S$ at $(x, y, z)$ is $(\vect{J}\cdot\vect{n})\,\delta S$.
 
Note that if the substance is conserved (i.e. not created/destroyed) then for every closed surface $S$ and corresponding enclosed 3D region $V$, we must have
$$\underbrace{\frac{\dd}{\dd t}\underbrace{\iiint_V \rho\dd V}_{\text{amount in } V \text{ at time } t}}_{\text{rate at which amount is increasing}} = \underbrace{-\underbrace{\oiint_S \vect{J}\cdot\vect{n}\dd S}_{\text{flux OUT of } V \dots \text{ over } S}}_{\text{flux into } V \text{ over } S \text{ per u. time}}$$
[the four under-braces are as labelled in the notes]
 
**Right page.**
 
**N.** Now from the divergence theorem:
$$\oiint_S \vect{J}\cdot\vect{n}\dd S = \iiint_V \operatorname{div}\vect{J}\dd V \Rightarrow \iiint \frac{\partial\rho}{\partial t} + \operatorname{div}\vect{J}\dd V = 0$$
[the "+" is written above a blacked-out symbol]
and as $S$ and $V$ are arbitrary, it follows that at every point $(x, y, z)$ we must have
$$\frac{\partial\rho(x, y, z, t)}{\partial t} + \nabla\cdot\vect{J}(x, y, z, t) = 0$$
This is the conservation of substance.
 
**Ex.** Consider a moving fluid with velocity field $\vect{v}(x, y, z, t)$. If the fluid is incompressible, we have a constant mass density $\rho(x, y, z, t) = \rho_0$. The mass flux vector field is $\vect{J} = \rho_0\vect{v}$. We have:
$$\frac{\partial\rho_0}{\partial t} + \nabla\cdot(\rho_0\vect{v}) = 0 \Rightarrow \rho_0(\nabla\cdot\vect{v}) = 0 \Rightarrow \nabla\cdot\vect{v} = 0$$
[$\partial\rho_0/\partial t$ is struck through with an arrow to "0"]
which is the conservation of mass in an incompressible fluid.
 
## HW 67 — Conservation law: heat conduction; the heat equation
_File `20261122_000437.jpg`. Left page "A conservation law" (section 3.5), right page "The heat equation" (section 4.1). Lower half of the right page blank. The notes underline $u$ in this derivation (as if a vector); it is a scalar field and is written $u$ here._
 
**Left page.**
 
**Ex.** Consider the conduction of heat in a uniform solid. Let
- $u(x, y, z, t)$ = temperature at $(x, y, z)$, time $t$
- $\rho$ = unit density of solid (const.)
- $\sigma$ = specific heat of solid (const.) (amount of heat energy needed to raise a unit mass by one unit of temperature)
The heat energy density is given by $\rho \times \sigma \times u(x, y, z, t)$ and the heat energy flux vector is given by
$$\vect{J}(x, y, z, t) = -K\nabla u(x, y, z, t)$$
[$K$ (thermal conductivity) is not defined in the notes]
We have conservation of heat energy:
$$\frac{\partial}{\partial t}\bigl(\rho\sigma u(x, y, z, t)\bigr) + \nabla\cdot\bigl(-K\nabla u(x, y, z, t)\bigr) = 0$$
Thus
$$\frac{\partial u}{\partial t} - \frac{K}{\rho\sigma}(\nabla\cdot\nabla u) = 0 \Rightarrow \frac{\partial u}{\partial t} = c^2\nabla\cdot(\nabla u) \quad \left\{c^2 = \frac{K}{\rho\sigma} \text{ thermal diffusivity}\right. \Rightarrow \frac{\partial u}{\partial t} = c^2\nabla^2u$$
[the "$-$" in the first line is written over a blacked-out mark]
This is the heat equation.
 
**Right page.**
 
**Def.** We define the *one-dimensional heat equation* by
$$\frac{\partial u(x, t)}{\partial t} = c^2\frac{\partial^2 u(x, t)}{\partial x^2}$$
 
**Ex.** Consider an iron bar at an initial temperature $u = u_0$. Assume one face is held at temperature $u = u_1$ and the other at $u = u_2$.
 
*Figure (bar with end temperatures).* A long horizontal rectangle (the bar), labelled $u(x, t)$ in the middle. The left end is a hatched square labelled $u_1$, at $x = 0$ (label below); the right end is a dashed square labelled $u_2$, at $x = L$ (label below).
 
We wish to obtain the solution $u(x, t)$ with initial conditions $u(x, 0) = u_0$ and boundary conditions $u(0, t) = u_1$ and $u(L, t) = u_2$.
 
## HW 68 — Laplace's equation; the wave equation (derivation, start)
_File `20261122_000446.jpg`. Left page "Laplace's equation" (section 4.2), right page "The wave equation" (section 4.3). Lower two-thirds of the left page blank._
 
**Left page.**
 
**N.** Consider a 3-D region with a prescribed temperature distribution (i.e. constant in time) on the surface. We expect the temperature inside to approach a steady-state distribution $u(x, y, z)$, by the heat equation:
$$\frac{\partial u}{\partial t} = c^2\nabla^2u \Rightarrow \nabla^2u = 0$$
[$\partial u/\partial t$ is struck through with an arrow to "0"]
or alternatively,
$$\frac{\partial^2 u(x, y)}{\partial x^2} + \frac{\partial^2 u(x, y)}{\partial y^2} = 0$$
for a system with no $z$-dependence. This is the *2D Laplace equation*.
 
**Right page.**
 
**N.** Consider the small displacement of a stretched string whose equilibrium position is along the $x$-axis.
 
*Figure 1 (stretched string).* A horizontal axis labelled $x$ (open arrowhead on the right) between two vertical posts. The string is fixed at both posts and drawn as one full sine period: an arch above the axis over the left half and a trough below over the right half. On the left arch, a vertical double-headed measurement mark from the axis up to the string, labelled $u$ (the displacement).
 
Consider a small segment as shown.
 
*Figure 2 (string segment).* Axes: vertical $u$ (arrow up), horizontal $x$ (arrow right). A single arch of string with arrowheads at both ends (tension pulling down-left at the left end, down-right at the right end). Dashed vertical lines down from the string to the $x$-axis at $x$ and at $x + \delta x$ (labelled). At the left point (a dot on the arch above $x$), a short dashed horizontal and vertical make a small right triangle with the string: the angle $\theta_1$ at its left vertex, the vertical side labelled $\Delta u$.
 
We have
$$\tan\theta_1 = \frac{\Delta u}{\Delta x} = \frac{u(x, t) - u(x - h, t)}{x - (x - h)} \approx \frac{\partial u(x, t)}{\partial x}, \qquad \tan\theta_2 = \frac{\Delta u}{\Delta x} = \dots \approx -\frac{\partial u(x + \delta x, t)}{\partial x}$$
Assume the tension $T$ in the string has constant magnitude. The force on the given segment (in $+u$ direction) is
$$\begin{aligned} &\approx -T\sin\theta_2 - T\sin\theta_1 \\ &\approx -T\tan\theta_2 - T\tan\theta_1 \quad [\swarrow \text{as } \cos\theta \approx 1 \text{ for small } \theta] \\ &\approx T\left(\frac{\partial u(x + \delta x, t)}{\partial x} - \frac{\partial u(x, t)}{\partial x}\right) \\ &\approx T\left(\frac{\partial u(x, t)}{\partial x} + \delta x\frac{\partial^2 u(x, t)}{\partial x^2} - \frac{\partial u(x, t)}{\partial x}\right) \end{aligned}$$
[the two first-derivative terms in the last line are struck through (they cancel); $\theta_2$, the angle at $x + \delta x$, is not marked in the figure]

# MATH2100 Applied Mathematical Analysis (MATH2010 ODEs + MATH2011 PDEs): transcription, part 4 of 5 (HW 69–100)
 
_Transcription phase. Nothing here is book text yet. Sources, legibility check and conventions: see part 1 (`claude/notes-math2100-1.md`)._
 
**This part:** wave equation (d'Alembert, IVP for the infinite string, erf), Fourier's method for the wave and heat equations, inhomogeneous heat equation, another approach via the steady state, stretched string with loading, steady 2-D heat (Laplace's equation in a rectangle), the fundamental solution and the heat equation on the line, method of images, semi-infinite slab, temperature waves in the Earth, Kelvin's Earth-age model, harmonic functions and conjugates, 2-D point sources and images, potential flow and electrostatics. "CN §" = CN-PDE.
 
---
 
## HW 69 — The wave equation (derivation, end); d'Alembert's solution (start)
_File `20261122_000455.jpg`. Left page "The wave equation" (section 4.3), right page "D'Alembert's solution (wave equation)" (section 5.1)._
 
**Left page.**
 
**N.** Thus the force on the given segment is $T\dfrac{\partial^2 u}{\partial x^2}\delta x$.
If the mass/unit length of the string is $\rho$, then the mass × acc. in the $+u$ direction is
$$(\rho\,\delta x)\frac{\partial^2 u(x, t)}{\partial t^2}$$
Thus by Newton's second law we have
$$T\frac{\partial^2 u(x, t)}{\partial x^2}\delta x = \rho\,\delta x\frac{\partial^2 u(x, t)}{\partial t^2} \Rightarrow \frac{\partial^2 u}{\partial t^2} = c^2\frac{\partial^2 u}{\partial x^2} \quad \text{where } c = \frac{T}{\rho}.$$
[possible error: $c^2 = T/\rho$, not $c = T/\rho$.]
This is the 1D wave equation.
 
**Rem.** Note that/recall that the three PDEs are all linear and homogenous and thus all follow the superposition principle.
 
**Rem.** PDEs have a much richer set of solutions and so it is not easy to find general solutions.
 
**Right page.**
 
**N.** It is difficult to obtain a general solution to a PDE. However, it is possible to find one for the 1-D wave equation
$$\frac{\partial^2 u(x, t)}{\partial t^2} = c^2\frac{\partial^2 u(x, t)}{\partial x^2}$$
Let $v = x + ct$ and $w = x - ct$, so that $x = \frac{1}{2}(v + w)$ and $t = \frac{1}{2c}(v - w)$. ["$x+$" is inserted above "$v = ct$"]
Then by the chain rule,
$$\frac{\partial}{\partial x} = \frac{\partial}{\partial v}\frac{\partial v}{\partial x} + \frac{\partial}{\partial w}\frac{\partial w}{\partial x} = \frac{\partial}{\partial v} + \frac{\partial}{\partial w}, \qquad \frac{\partial}{\partial t} = \frac{\partial}{\partial v}\frac{\partial v}{\partial t} + \frac{\partial}{\partial w}\frac{\partial w}{\partial t} = c\frac{\partial}{\partial v} - c\frac{\partial}{\partial w}$$
This implies
$$\frac{\partial^2 u}{\partial t^2} = \left(c\frac{\partial}{\partial v} - c\frac{\partial}{\partial w}\right)\left(c\frac{\partial}{\partial v} - c\frac{\partial}{\partial w}\right)u = c^2\left(\frac{\partial^2}{\partial v^2} + \frac{\partial^2}{\partial w^2} - 2\frac{\partial^2}{\partial v\partial w}\right)u$$
$$\frac{\partial^2 u}{\partial x^2} = \left(\frac{\partial}{\partial v} + \frac{\partial}{\partial w}\right)\left(\frac{\partial}{\partial v} + \frac{\partial}{\partial w}\right)u = \left(\frac{\partial^2}{\partial v^2} + \frac{\partial^2}{\partial w^2} + 2\frac{\partial^2}{\partial v\partial w}\right)u$$
and thus
$$0 = -\frac{\partial^2 u}{\partial x^2}c^2 + \frac{\partial^2 u}{\partial t^2} = -4c^2\frac{\partial^2 u}{\partial w\partial v}$$
 
## HW 70 — d'Alembert's general solution; IVP for the infinite string (start)
_File `20261122_000503.jpg`. Left page "D'Alembert's solution (wave equation)" (section 5.1), right page "IVPs for infinite string (wave equation)" (section 5.2)._
 
**Left page.**
 
**N.** It is easier to solve this DE. We have:
$$0 = \frac{\partial^2 u}{\partial w\partial v} = \frac{\partial}{\partial w}\left(\frac{\partial u}{\partial v}\right) \Rightarrow \frac{\partial u}{\partial v} = A(v)$$
where $A(v)$ is some arbitrary function of $v$. Thus
$$u(v, w) = \int A(v)\dd v + G(w) = F(v) + G(w) = F(x + ct) + G(x - ct)$$
which is the general solution for some arbitrary functions $F, G$ (twice differentiable).
 
**Rem.** $F(x + ct)$ represents a wave of constant shape travelling to the <u>left</u> at speed $c$. $G(x - ct)$ represents a wave of constant shape travelling to the <u>right</u> at speed $c$.
 
*Figure (left-travelling wave).* Horizontal axis (arrow right) and a vertical axis (arrow up). To the right of the vertical axis, a bell-shaped bump centred at $x_0$ (dashed vertical line at its peak, $x_0$ labelled below), labelled "$t = 0$" above and "$u = F(x)$" beside it. To the left of the vertical axis, a smaller/narrower copy of the bump centred at $x_0 - ct$ (dashed centre line, labelled below), labelled "$t > 0$" above and "$u = F(x + ct)$" beside it. A short arrow pointing left near the vertical axis shows the direction of travel. [The two bumps should be the same shape; the left one is drawn smaller.]
 
To fix a particular solution of the wave equation, we must have enough information to fix $F$ and $G$.
 
**Right page.**
 
**N.** Suppose we have a very long (infinitely long) string and we are interested in the middle, so we can ignore end effects/boundary conditions.* Therefore we consider
$$\frac{\partial^2 u(x, t)}{\partial t^2} - c^2\frac{\partial^2 u(x, t)}{\partial x^2} = 0, \qquad t \ge 0,\ -\infty < x < \infty$$
or in nicer notation $u_{tt}(x, t) - c^2u_{xx}(x, t) = 0$.
Suppose we have the following initial conditions
$$u(x, 0) = f(x) \leftarrow \text{initial shape}, \qquad u_t(x, 0) = g(x) \leftarrow \text{initial velocity shape}$$
We know that the solution of the PDE is $u(x, t) = F(x + ct) + G(x - ct)$. Now
$$u_t(x, t) = \partial F(x + ct)/\partial t + \partial G(x - ct)/\partial t = cF'(x + ct) - cG'(x - ct)$$
By the initial conditions
$$f(x) = u(x, 0) = F(x) + G(x) \quad (1), \qquad g(x) = u_t(x, 0) = cF'(x) - cG'(x) \quad (2)$$
\* To deal with the effects of boundaries for a finite string, we can use Fourier's method (see part 6)
 
## HW 71 — d'Alembert's solution for the IVP; plucked and struck strings
_File `20261122_000511.jpg`. Both pages "IVPs for infinite string (wave equation)", section 5.2._
 
**Left page.**
 
**N.** Integrate (2):
$$\int g(x)\dd x = cF(x) - cG(x) \Rightarrow F(x) - G(x) = \frac{1}{c}\int_{x_0}^x g(u)\dd u + A \quad (3)$$
Add (1) and (3):
$$2F(x) = f(x) + \frac{1}{c}\int_{x_0}^x g(u)\dd u + A$$
Subtract (3) from (1):
$$2G(x) = f(x) - \frac{1}{c}\int_{x_0}^x g(u)\dd u - A$$
Therefore,
$$F(x + ct) + G(x - ct) = \frac{1}{2}f(x + ct) + \frac{1}{2c}\int_{x_0}^{x+ct} g(u)\dd u + \frac{1}{2}f(x - ct) - \frac{1}{2c}\int_{x_0}^{x-ct} g(u)\dd u$$
and therefore
$$u(x, t) = \frac{1}{2}f(x + ct) + \frac{1}{2}f(x - ct) + \frac{1}{2c}\int_{x-ct}^{x+ct} g(u)\dd u$$
which is *D'Alembert's solution* for the IVP of the 1D wave equation on the whole $x$-axis.
 
**Right page.**
 
**Ex.** Consider a plucked string, with IC $u(x, 0) = f(x)$, $u_t(x, 0) = 0$ $\Rightarrow g(x) = 0$, i.e. a string released from rest with initial shape given by $f(x)$. ["i.e." is written above a blacked-out word] Then
$$u(x, t) = \frac{1}{2}f(x + ct) + \frac{1}{2}f(x - ct)$$
Thus we get pulses to the left and right, each at speed $c$, each with shape $\frac{1}{2}f(x)$.
 
*Figure (plucked string, two panels).* Left panel, labelled "$f(x)$, $t = 0$" with an arrow: axes $x$ and $u$; a triangular pulse with apex $u_0$ on the $u$-axis and base from $-a$ to $a$. Right panel: the same axes with two small triangular pulses of height $u_0/2$ (dashed level line labelled $u_0/2$), one on the left with base from $-a - ct$ to $a - ct$ and one on the right with base from $-a + ct$ to $a + ct$ (labels below the axis); arrows labelled $c$ above them point left and right respectively.
 
**Ex.** Consider a struck string, with IC $u(x, 0) = 0$, $u_t(x, 0) = Ae^{-x^2}$. Then D'Alembert's solution is
$$u(x, t) = \frac{1}{2c}\int_{x-ct}^{x+ct} Ae^{-u^2}\dd u \quad \text{[non-elementary integral]}$$
We introduce a new function $\operatorname{erf}(x)$. Then,
$$u(x, t) = \underbrace{\frac{A}{2c}\frac{\sqrt{\pi}}{2}}_{B}\bigl(\operatorname{erf}(x + ct) - \operatorname{erf}(x - ct)\bigr)$$
 
*Figure (struck string at time $t$).* Horizontal axis with arrows at both ends, a vertical axis. A symmetric hump with its maximum on the vertical axis, passing through the axis at $-ct$ and $ct$ (marked with dots and labelled), and continuing below the axis outside $[-ct, ct]$. [possible error: $\operatorname{erf}(x + ct) - \operatorname{erf}(x - ct) > 0$ for all $x$ when $t > 0$, so the solution never goes below the axis; the hump should only decay towards 0 outside $[-ct, ct]$ (compare to CN §5.2).]
 
## HW 72 — The error function; Fourier's method for the wave equation (start)
_File `20261122_000520.jpg`. Left page "Error function" (section 5.3), right page "Fourier's method (wave equation)" (section 6.1)._
 
**Left page.**
 
**Def.** We define the *error function* by
$$\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-s^2}\dd s \quad \text{[total integral 1]}$$
The error function is odd:
$$\operatorname{erf}(-x) = \frac{2}{\sqrt{\pi}}\int_0^{-x} e^{-u^2}\dd u = \frac{-2}{\sqrt{\pi}}\int_0^x e^{-z^2}\dd z = -\operatorname{erf}(x)$$
[the middle line has two small blacked-out marks next to the upper limit and the exponent; the substitution is $z = -u$]
The error function is also (sigmoidally) monotonically increasing.
$$\frac{\dd}{\dd x}\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}e^{-x^2} > 0$$
A plot of $\operatorname{erf}(x)$ is as follows:
 
*Figure (erf).* Axes with arrows; vertical ticks at $1$ and $-1$. A sigmoid curve through the origin, rising steeply there, approaching 1 as $x \to \infty$ and $-1$ as $x \to -\infty$ (arrowheads on both ends). A few dots are placed along the curve (and two stray dots above it on the right).
 
**Right page.**
 
**N.** Suppose the string is not infinite, but instead occupies the interval $[0, L]$.
 
*Figure (finite string).* Axes: vertical $u$, horizontal (arrow right). The origin labelled 0; a dashed vertical line at $L$. A wavy curve from $(0, 0)$ to $(L, 0)$: up into a crest, down through the axis into a trough, up into a second crest, and back to 0 at $L$.
 
We wish to solve $u_{tt} - c^2u_{xx} = 0$, for $0 \le x \le L$, $t \ge 0$, with
$$\left.\begin{aligned} u(x, 0) &= f(x) \\ u_t(x, 0) &= g(x) \end{aligned}\right\}\text{ICs} \qquad \left.\begin{aligned} u(0, t) &= 0 \\ u(L, t) &= 0 \end{aligned}\right\}\text{BCs}$$
It is difficult to use the general form of the solution $u(x, t) = F(x + ct) + G(x - ct)$ because of boundary conditions. We therefore use Fourier's method, which is quite different from D'Alembert's method for the infinite string.
The idea is to find all possible solutions of the DE and the BCs with separable form $u(x, t) = F(x)G(t)$ and then we can superpose these to get a general solution. We then impose ICs to finish the problem.
 
## HW 73 — Fourier's method for the wave equation: separation, the three cases for $k$
_File `20261122_000527.jpg`. Both pages "Fourier's method (wave equation)", section 6.1._
 
**Left page.**
 
**N.** We first substitute the separable form into the boundary conditions:
$$0 = u(0, t) = F(0)G(t) \Rightarrow \underline{\underline{F(0) = 0}} \text{ or } G(t) = 0 \ \hookrightarrow u(t) = 0 \text{ trivial sol.}$$
$$0 = u(L, t) = F(L)G(t) \Rightarrow \underline{\underline{F(L) = 0}} \text{ or } G(t) = 0 \ \hookrightarrow u(t) = 0 \text{ trivial sol.}$$
We thus have $F(0) = 0$, $F(L) = 0$.
We now substitute into the wave equation: ["wave" is written above a blacked-out word]
$$u_{tt}(x, t) = F(x)G''(t), \qquad u_{xx}(x, t) = F''(x)G(t)$$
$$\Rightarrow 0 = F(x)G''(t) - c^2F''(x)G(t) \Rightarrow \underbrace{\frac{G''(t)}{c^2G(t)}}_{\text{function of } t} = \underbrace{\frac{F''(x)}{F(x)}}_{\text{function of } x} = \underbrace{k}_{\text{some constant}}$$
This gives two separate systems:
$$G''(t) = kc^2G(t) \leftarrow G\text{-system}, \qquad F''(x) = kF(x) \leftarrow F\text{-system}$$
We first consider the $F$-system with the boundary conditions $F(0) = 0$, $F(L) = 0$. There are three cases.
 
**Right page.**
 
**N.** Case (a): $k = 0$
$F''(x) = 0 \Rightarrow F(x) = Ax + B$; as $F(0) = 0 \Rightarrow B = 0$; as $F(L) = 0 \Rightarrow AL = 0 \Rightarrow A = 0$.
So $u(x, t) = 0$, which is the trivial solution. Thus for non-trivial solutions, $k \ne 0$.
 
Case (b): $k > 0$, $k = \mu^2$
$F''(x) = \mu^2F(x) \Rightarrow F''(x) - \mu^2F(x) = 0 \Rightarrow F(x) = Ae^{\mu x} + Be^{-\mu x}$
as $F(0) = 0 \Rightarrow A + B = 0$; as $F(L) = 0 \Rightarrow Ae^{2\mu L} + B = 0$
This leads to $A = 0$, $B = 0$, so $u(x, t) = 0$. Thus for non-trivial solutions, $k < 0$.
 
Case (c): $k < 0$, $k = -p^2 < 0$, $p > 0$
$F''(x) + p^2F(x) = 0 \Rightarrow F(x) = A\cos(px) + B\sin(px)$
as $F(0) = 0 \Rightarrow A = 0 \Rightarrow F(x) = B\sin(px)$
as $F(L) = 0 \Rightarrow B\sin(pL) = 0 \Rightarrow \sin(pL) = 0$ ($B = 0$ is trivial) $\Rightarrow pL = n\pi$ for $n \in \N$
which implies $k = -p^2 = -\left(\frac{n\pi}{L}\right)^2$. Therefore $F(x) = B\sin\left(\frac{n\pi}{L}x\right)$.
 
## HW 74 — Fourier's method for the wave equation: solution, normal modes
_File `20261122_000540.jpg`. Both pages "Fourier's method (wave equation)", section 6.1._
 
**Left page.**
 
**N.** Now consider the $G$-system with our value of $k$:
$$G''(t) = -\left(\frac{n\pi c}{L}\right)^2G(t) \Rightarrow G(t) = a\cos\left(\frac{n\pi c}{L}t\right) + b\sin\left(\frac{n\pi c}{L}t\right)$$
Therefore,
$$\begin{aligned} u(x, t) = F(x)G(t) &= B\sin\left(\frac{n\pi}{L}x\right)\cdot G(t) \\ &= \left[A_n\cos\left(\frac{n\pi c}{L}t\right) + B_n\sin\left(\frac{n\pi c}{L}t\right)\right]\times\sin\left(\frac{n\pi}{L}x\right) \quad \{A_n = Ba,\ B_n = Bb\} \end{aligned}$$
[an arrow points from $G(t)$ above up to the formula for $G$; the margin note reads "$A_n = Ba$, $D_n = Bb$", where "$D_n$" should be $B_n$]
Now use superposition principle:
$$u(x, t) = \sum_{n=1}^\infty u_n(x, t) = \sum_{n=1}^\infty \sin\left(\frac{n\pi}{L}x\right)\cdot\left[A_n\cos\left(\frac{n\pi c}{L}t\right) + B_n\sin\left(\frac{n\pi c}{L}t\right)\right]$$
We now impose the ICs:
$$f(x) = u(x, 0) = \sum_{n=1}^\infty A_n\sin\left(\frac{n\pi}{L}x\right) \quad [\swarrow \text{Fourier half-range series for } f(x)]$$
so $A_n = 2/L\int_0^L f(x)\sin\left(\frac{n\pi}{L}x\right)\dd x$
$$g(x) = u_t(x, 0) = \sum_{n=1}^\infty \left(0 + \frac{n\pi c}{L}B_n\right)\sin\left(\frac{n\pi}{L}x\right) \quad [\swarrow \text{Fourier half-range series for } g(x)]$$
so $\frac{n\pi c}{L}B_n = 2/L\int_0^L g(x)\sin\left(\frac{n\pi}{L}x\right)\dd x$
 
**Right page.**
 
**N.** We therefore arrive at the solution
$$u(x, t) = \sum_{n=1}^\infty \left[A_n\cos\left(\frac{n\pi c}{L}t\right) + B_n\sin\left(\frac{n\pi c}{L}t\right)\right]\sin\left(\frac{n\pi}{L}x\right)$$
where
$$A_n = \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi}{L}x\right)\dd x, \qquad B_n = \frac{2}{n\pi c}\int_0^L g(x)\sin\left(\frac{n\pi}{L}x\right)\dd x$$
or we can rewrite it as
$$u(x, t) = \sum_{n=1}^\infty \left[A_nu_n^{(A)}(x, t) + B_nu_n^{(B)}(x, t)\right]$$
where
$$u_n^{(A)}(x, t) = \cos\left(\frac{n\pi c}{L}t\right)\sin\left(\frac{n\pi}{L}x\right), \qquad u_n^{(B)}(x, t) = \sin\left(\frac{n\pi c}{L}t\right)\sin\left(\frac{n\pi}{L}x\right)$$
– called the *normal modes* of vibration of the string. Note they are periodic in both time and space.
 
**N.** Recall that $\cos(\omega t)$, $\sin(\omega t)$ have angular frequency $\omega$, frequency (number of cycles per unit time) $\nu = \omega/2\pi$ and period $T = 1/\nu = 2\pi/\omega$.
Therefore $u_n^{(A)}(x, t)$ and $u_n^{(B)}(x, t)$ have
+ angular frequency $\omega_n = n\pi c/L$
+ frequency $\nu_n = nc/2L$
+ period $T_n = 2L/nc$
**Rem.** We can show this general solution is also of the form $f(x + ct) + g(x - ct)$, as previously.
 
## HW 75 — Normal modes (figure); plucked-string example on $[0, L]$
_File `20261122_000637.jpg`. Both pages "Fourier's method (wave equation)", section 6.1._
 
**Left page.**
 
**N.** *Figure (first two normal modes, two panels).* Left panel: axes $u$ (vertical) and $x$ (horizontal, arrow), with $L$ marked. A dashed arch $\sin(\pi x/L)$ above the axis from $0$ to $L$ and its mirror $-\sin(\pi x/L)$ below (dashed), together a closed oval envelope (labelled with arrows "$\sin(\frac{\pi x}{L})$" above and "$-\sin(\frac{\pi x}{L})$" below). Inside, a solid smaller arch (the string at some time) with a vertical double-headed arrow at its middle showing the up–down oscillation. Caption: $\nu_1 = c/2L$.
Right panel: same axes. Dashed envelope of one full sine period over $[0, L]$ and its mirror image (the curves $\pm\sin(2\pi x/L)$; labelled in the notes "$\sin(\frac{\pi x}{L})$" and "$-\sin(\frac{\pi x}{L})$"). A solid curve with a smaller crest on the left half and a trough on the right half, with vertical double-headed arrows at the crest and the trough; the node at $L/2$. Caption: $\nu_2 = 2\nu_1 = c/L$.
[possible error: the right-panel envelope labels should read $\pm\sin(2\pi x/L)$.]
 
We denote $u_1^{(A)}, u_1^{(B)}$ the *fundamental mode* of vibration (they differ by phase in time). $u_2^{(A)}, u_2^{(B)}$ denote the *first overtone*, and so on.
 
**Ex.** Solve the wave equation $u_{tt} - c^2u_{xx} = 0$ for $0 < x < L$ and $t > 0$, with initial conditions $u(x, 0) = f(x)$ and $u_t(x, 0) = 0$, and boundary conditions $u(0, t) = u(L, t) = 0$, where
$$f(x) = \begin{cases} 0 & \text{if } L/2 + a < x < L \\ 0 & \text{if } 0 < x < L/2 - a \\ u_0(x - L/2 + a)/a & \text{if } L/2 - a < x < L/2 \\ u_0(L/2 + a - x)/a & \text{if } L/2 < x < L/2 + a \end{cases}$$
 
*Figure (initial shape).* Axes $f(x)$ (vertical) and $x$. A triangle with base from $L/2 - a$ to $L/2 + a$ on the axis and apex at $(L/2, u_0)$; a dotted horizontal line from $u_0$ on the vertical axis to the apex and a dotted vertical line from the apex down to $L/2$. Ticks labelled $L/2 - a$, $L/2$, $L/2 + a$.
 
**Right page.**
 
**Ex.** From the general result
$$u(x, t) = \sum_{n=1}^\infty \left[A_n\cos\left(\frac{n\pi c}{L}t\right) + B_n\sin\left(\frac{n\pi c}{L}t\right)\right]\sin\left(\frac{n\pi}{L}x\right)$$
Now
$$B_n = \frac{2}{n\pi c}\int_0^L g(x)\sin\left(\frac{n\pi x}{L}\right)\dd x = 0 \quad [g = 0]$$
$$\begin{aligned} A_n &= \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\dd x \\ &= \frac{2}{L}\int_{L/2-a}^{L/2} \frac{u_0(x - L/2 + a)}{a}\sin\left(\frac{n\pi x}{L}\right)\dd x + \frac{2}{L}\int_{L/2}^{L/2+a} \frac{u_0(-x + L/2 + a)}{a}\sin\left(\frac{n\pi x}{L}\right)\dd x \\ &= \frac{4u_0L}{an^2\pi^2}\sin\left(\frac{n\pi}{2}\right)\left[1 - \cos\left(\frac{n\pi a}{L}\right)\right] \end{aligned}$$
and so
$$\begin{aligned} u(x, t) &= \sum_{n=1}^\infty \left[\frac{4u_0L}{an^2\pi^2}\sin\left(\frac{n\pi}{2}\right)\left(1 - \cos\left(\frac{n\pi a}{L}\right)\right)\cos\left(\frac{n\pi c}{L}t\right)\right] \\ &= \sum_{m=0}^\infty \left[\frac{4u_0L}{a\pi^2}\cdot\frac{(-1)^m}{(2m + 1)^2}\left(1 - \cos\left(\frac{[2m + 1]\pi a}{L}\right)\right)\cos\left(\frac{[2m + 1]\pi c}{L}t\right)\right] \end{aligned}$$
[possible error: the factor $\sin\left(\frac{n\pi}{L}x\right)$ (with $n = 2m+1$) is missing from both lines of $u(x, t)$.]
 
## HW 76 — Fourier's method for the 1D heat equation (insulated ends): setup, cases (a), (b)
_File `20261122_000646.jpg`. Both pages "Fourier's method (1D heat equation)", section 6.2._
 
**Left page.**
 
**N.** Consider a perfectly insulated iron bar as below.
 
*Figure (insulated bar).* A rectangular box drawn in perspective (a long bar), with its axis along a dashed line labelled $x$ (arrow to the right). The near end face carries a small circle labelled $0$; a dot on the axis at the far end is labelled $L$, with a short dashed vertical line through it.
 
The heat flux vector is
$$\vect{J} = -K\nabla u = -K\frac{\partial u}{\partial x}\vec{\imath} = -Ku_x\vec{\imath}$$
If there is no heat flow through the face at $x = 0$, then $\vect{J}(0, t) = -Ku_x(0, t)\vec{\imath} = \vect{0}$. Therefore (and similarly), $u_x(0, t) = 0$ and $u_x(L, t) = 0$.
We can describe the problem then as follows:
PDE: $u_t(x, t) = c^2u_{xx}(x, t)$
BCs: $u_x(0, t) = 0$, $u_x(L, t) = 0$
ICs: $u(x, 0) = f(x)$
where $f(x)$ is the initial temperature distribution.
Following Fourier's method, we look for solutions of the PDE and the BCs in the separable form $u(x, t) = F(x)G(t)$, $\Rightarrow u_x(x, t) = F'(x)G(t)$.
We then apply the boundary conditions:
$$0 = u_x(0, t) = F'(0)G(t) \Rightarrow F'(0) = 0, \qquad 0 = u_x(L, t) = F'(L)G(t) \Rightarrow F'(L) = 0$$
 
**Right page.**
 
**N.** We now substitute into the heat equation:
$$u_t(x, t) = F(x)G'(t), \quad u_{xx}(x, t) = F''(x)G(t) \Rightarrow F(x)G'(t) = c^2F''(x)G(t) \Rightarrow \underbrace{\frac{G'(t)}{c^2G(t)}}_{\text{function } t} = \underbrace{\frac{F''(x)}{F(x)}}_{\text{function } x} = \underbrace{k}_{\text{some constant}}$$
This gives two separate systems:
$$G'(t) = kc^2G(t) \leftarrow G\text{-system}, \qquad F''(x) = kF(x) \leftarrow F\text{-system}$$
We first consider the $F$-system, with three cases.
Case (a): $k = 0$
$F''(x) = 0 \Rightarrow F(x) = ax + b$; as $F'(0) = 0 \Rightarrow F(x) = b$; as $k = 0 \Rightarrow G'(t) = 0 \Rightarrow G(t) = c$
so combining gives $u(x, t) = cb = A_0$.
[the constant $c$ here clashes with the wave speed $c$]
Case (b): $k = \mu^2 > 0$, $\mu > 0$
$F''(x) - \mu^2F(x) = 0 \Rightarrow F(x) = ae^{\mu x} + be^{-\mu x} \Rightarrow F'(x) = a\mu e^{\mu x} - b\mu e^{-\mu x}$
as $F'(0) = 0 \Rightarrow a - b = 0$; as $F'(L) = 0 \Rightarrow a\mu e^{2\mu x} - b\mu = 0$
[read: $e^{2\mu L}$ (after multiplying by $e^{\mu L}$); the notes write $e^{2\mu x}$]
This leads to $a = 0$, $b = 0$, so $u(x, t) = 0$. This is a trivial solution.
 
## HW 77 — Heat equation (insulated ends): case (c), solution; triangle example; long-time limit
_File `20261122_000706.jpg`. Both pages "Fourier's method (1D heat equation)", section 6.2._
 
**Left page.**
 
**N.** Case (c): $k < 0$, $k = -p^2$, $p > 0$
$F''(x) + p^2F(x) = 0 \Rightarrow F(x) = a\cos(px) + b\sin(px) \Rightarrow F'(x) = -ap\sin(px) + bp\cos(px)$
as $F'(0) = 0 \Rightarrow bp = 0 \Rightarrow b = 0 \Rightarrow F(x) = a\cos(px)$
as $F'(L) = 0 \Rightarrow -ap\sin(pL) = 0 \Rightarrow \sin(pL) = 0$ ($a = 0$ is trivial) $\Rightarrow pL = n\pi$ for $n \in \N$
which implies $k = -p^2 = -\left(\frac{n\pi}{L}\right)^2$. Therefore $F(x) = a\cos\left(\frac{n\pi}{L}x\right)$.
Now consider the $G$-system with the found $k$:
$$G'(t) = -c^2\left(\frac{n\pi}{L}\right)^2G(t) \Rightarrow G(t) = D\exp\bigl[-(n\pi c/L)^2t\bigr]$$
Therefore, combining we arrive at
$$u(x, t) = aD\exp\bigl[-(n\pi c/L)^2t\bigr]\cos\left(\frac{n\pi}{L}x\right)$$
which gives the (infinite) family of solutions $u_0(x, t) = A_0$, $u_n(x, t) = {}$ [an arrow points back up to the line above].
Using the superposition principle:
$$u(x, t) = \sum_{n=0}^\infty A_ne^{-(n\pi c/L)^2t}\cos\left(\frac{n\pi}{L}x\right)$$
 
**Right page.**
 
**N.** We now impose the ICs:
$$f(x) = u(x, 0) = \sum_{n=1}^\infty A_n\cos(n\pi x/L) \quad [\swarrow \text{Fourier half-range cosine series for } f(x),\ 0 \le x \le L]$$
[the sum should start at $n = 0$ (or read $A_0 + \sum_{n=1}^\infty$), as in the line before]
so
$$A_0 = \frac{1}{L}\int_0^L f(x)\dd x, \qquad A_n = \frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\dd x$$
 
**Ex.** Solve the heat equation where
$$f(x) = \begin{cases} \frac{2u_0}{L}x & \text{if } 0 < x < L/2 \\ \frac{2u_0}{L}(L - x) & \text{if } L/2 < x < L \end{cases}$$
 
*Figure (initial temperature).* Axes with $x$ to the right; a triangle with base $[0, L]$ and apex at $(L/2, u_0)$, a dotted horizontal line from $u_0$ on the vertical axis to the apex and a dotted vertical line down to $L/2$. Ticks $0$, $L/2$, $L$. Caption beside: "The temperature (initial) distribution is given here."
 
$$A_0 = \frac{2u_0}{L^2}\left[\int_0^{L/2} x\dd x + \int_{L/2}^L (L - x)\dd x\right] = \frac{u_0}{2}$$
$$A_n = \frac{4u_0}{L^2}\left[\int_0^{L/2} x\cos\left(\frac{n\pi x}{L}\right)\dd x + \int_{L/2}^L (L - x)\cos\left(\frac{n\pi x}{L}\right)\dd x\right] = \frac{4u_0}{[\text{blacked out}]\,n^2}\left(2\cos\left(\frac{n\pi}{2}\right) - \cos(n\pi) - 1\right)$$
[ambiguous: part of the denominator is blacked out; the integrals give $\frac{4u_0}{n^2\pi^2}$, so a $\pi^2$ is missing or hidden.]
Therefore $u(x, t) = A_0 + \sum_{n=1}^\infty A_n\cos(n\pi x/L)$ where $A_0, A_n$ given above.
[possible error: the time factor $e^{-(n\pi c/L)^2t}$ is missing from each term.]
 
**N.** In general, as $t \to \infty$, $u(x, t) \to A_0$. We can show
$$\underbrace{L\rho\sigma u(x, t)}_{\text{heat energy}} \to \underbrace{L\rho\sigma A_0}_{\text{final heat at temp. } A_0} = \underbrace{\int_0^L \rho\sigma f(x)\dd x}_{\text{initial heat with } f(x)}.$$
[the left side is the total heat energy, written as $L\rho\sigma u$; as $u$ depends on $x$ it should be $\int_0^L\rho\sigma u(x,t)\dd x$]
 
## HW 78 — Inhomogeneous heat equation: setup, particular solution by undetermined coefficients
_File `20261122_000715.jpg`. Both pages "Inhomogenous heat equation", section 6.3._
 
**Left page.**
 
**N.** What if we have a source of heat energy present? Then the 1-D heat equation is modified to
$$u_t(x, t) - c^2u_{xx}(x, t) = q(x, t)$$
where $q(x, t)$ is a given 'source' function. Then the amount of energy produced in $(x, x + \delta x)$ per unit time is $\rho\sigma\cdot q(x, t)\,\delta x$.
 
**N.** We aim to solve the problem
<u>DE</u>: $u_t(x, t) - c^2u_{xx}(x, t) = q(x, t)$
<u>IC</u>: $u(x, 0) = f(x)$
<u>BC</u>: $u(0, t) = 0$, $u(L, t) = 0$
When $q = 0$ we get a solution of the form
$$u^{(h)}(x, t) = \sum_{n=1}^\infty A_n(t)\sin\left(\frac{n\pi x}{L}\right) \quad \text{where} \quad A_n(t) = A_ne^{-(n\pi c/L)^2}$$
[possible error: the exponent is missing its factor $t$: $A_ne^{-(n\pi c/L)^2t}$.]
Thus the general solution of the inhomogenous PDE is
$$u(x, t) = u^{(h)}(x, t) + u^{(p)}(x, t)$$
 
**Right page.**
 
**N.** The particular solution we must now derive. We will use the method of undet. coeffs. Expand $q(x, t)$ as a half-range sine series at each value of $t$:
$$q(x, t) = \sum_{n=1}^\infty Q_n(t)\sin\left(\frac{n\pi x}{L}\right), \qquad Q_n(t) = \frac{2}{L}\int_0^L q(x, t)\sin\left(\frac{n\pi x}{L}\right)\dd x$$
Then it can be seen that $u^{(p)}$ has the form
$$u^{(p)}(x, t) = \sum_{n=1}^\infty B_n(t)\sin\left(\frac{n\pi x}{L}\right)$$
Substituting $u^{(p)}$ and $q$ into the PDE we obtain
$$\sum_{n=1}^\infty \left[B_n'(t) + \left(\frac{n\pi c}{L}\right)^2B_n(t)\right]\sin\left(\frac{n\pi x}{L}\right) = \sum_{n=1}^\infty Q_n(t)\sin\left(\frac{n\pi x}{L}\right)$$
which implies
$$\sum_{n=1}^\infty \left[B_n'(t) + \left(\frac{n\pi c}{L}\right)^2B_n(t) - Q_n(t)\right]\sin\left(\frac{n\pi x}{L}\right) = 0$$
As $\sin\left(\frac{n\pi x}{L}\right)$ are orthogonal, we obtain
$$B_n'(t) + \left(\frac{n\pi c}{L}\right)^2B_n(t) = Q_n(t)$$
which is a first order linear ODE. The solution is
$$B_n(t) = e^{-(n\pi c/L)^2t}\left[C_n + \int e^{(n\pi c/L)^2t}Q_n(t)\dd t\right] = C_n\exp\bigl[-(n\pi c/L)^2t\bigr] + \hat{B}_n(t)$$
 
 
## HW 79 — Inhomogeneous heat equation: general solution; example with constant source
_File `20261122_000751.jpg`. Both pages "Inhomogenous heat equation", section 6.3. A shadow crosses both pages; readable._
 
**Left page.**
 
**N.** Hence the general solution is given by
$$u(x,t) = u^{(h)}(x,t) + u^{(p)}(x,t) = \sum_{n=1}^\infty \Bigl\{\underbrace{(A_n + C_n)}_{D_n} e^{-(n\pi c/L)^2 t} + \hat B_n(t)\Bigr\}\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
and it follows that the general solution still possesses the form
$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\Bigl(\frac{n\pi}{L}x\Bigr)$$
where $B_n(t)$ satisfies the earlier first-order linear ODE. Note that the general solution constructed above satisfies the boundary conditions already, so there is no need to impose them. We do impose the initial conditions:
$$f(x) = u(x,0) = \sum_{n=1}^\infty B_n(0)\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
where
$$B_n(0) = \frac{2}{L}\int_0^L f(x)\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x$$
and so $B_n(0)$ is determined from the IC. This gives the IC for the earlier first-order linear ODE, which in turn determines the coefficients $B_n(t)$.
 
**Right page.**
 
**Ex.** Let
$$q(x,t) = q_0 \quad 0 \le x \le L,\ t > 0, \qquad f(x) = u_0 \quad 0 \le x \le L$$
where $u_0, q_0 \in \R$. Then
$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
where $B_n(t)$ satisfies the first order ODE
$$B_n'(t) + \Bigl(\frac{n\pi c}{L}\Bigr)^2 B_n(t) = Q_n(t).$$
The IC $B_n(0)$ for this ODE is determined by the IC of the problem:
$$f(x) = u_0 = u(x,0) = \sum_{n=1}^\infty B_n(0)\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
$$\Rightarrow B_n(0) = \frac{2}{L}\int_0^L u_0\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x = -\frac{2u_0}{n\pi}\cos\Bigl(\frac{n\pi x}{L}\Bigr)\Big|_0^L = \frac{2u_0}{n\pi}\bigl(1 - (-1)^n\bigr)$$
The general solution for the first order ODE is thus
$$B_n(t) = D_n e^{-(n\pi c/L)^2} + e^{-(n\pi c/L)^2 t} \times \int e^{(n\pi c/L)^2}\cdot\frac{2q_0}{n\pi}\bigl(1-(-1)^n\bigr)\dd t = \Bigl(\frac{L}{n\pi c}\Bigr)^2\frac{2q_0}{n\pi}\bigl(1-(-1)^n\bigr) + D_n e^{-(n\pi c/L)^2 t}$$
[possible error: in the first line both exponents $-(n\pi c/L)^2$ (on $D_n$) and $(n\pi c/L)^2$ (in the integral) are missing their factor $t$; the last line has it. The step $Q_n(t) = \frac{2q_0}{n\pi}(1-(-1)^n)$ is used without being written (same integral as $B_n(0)$ with $q_0$ for $u_0$).]
 
*Figure:* none.
 
---
 
## HW 80 — Inhomogeneous heat equation: example (end); another approach for a time-independent source
_File `20261122_000801.jpg`. Left page "Inhomogenous heat equation" (section 6.3), right page "Another approach to inhomo. heat equation" (section 6.4). A shadow crosses both pages; readable._
 
**Left page.**
 
**Ex.** We now consider the ICs.
$$B_n(0) = \frac{2u_0}{n\pi}\bigl(1-(-1)^n\bigr) = D_n + \Bigl(\frac{L}{n\pi c}\Bigr)^2\frac{2q_0}{n\pi}\bigl(1-(-1)^n\bigr)$$
which implies
$$D_n = \frac{2}{n\pi}\bigl(1-(-1)^n\bigr)\Bigl(u_0 - q\Bigl(\frac{L}{n\pi c}\Bigr)^2\Bigr) = \begin{cases} 0 & n \text{ even}\\[1mm] \dfrac{4}{(2k+1)\pi}\Bigl[u_0 - q\Bigl(\dfrac{L}{(2k+1)\pi c}\Bigr)^2\Bigr] & n \text{ odd}\end{cases}$$
[possible error: $q$ should be $q_0$ (also in the next line, where the subscript is unclear); the odd case switches from $n$ to $k$ without saying $n = 2k+1$.]
and so
$$B_{2k}(t) = 0$$
$$B_{2k+1}(t) = \frac{4q_0L^2}{(2k+1)^3\pi^3c^2} + \frac{4}{(2k+1)\pi}\Bigl[u_0 - \frac{q_0L^2}{(2k+1)^2\pi^2c^2}\Bigr] \times e^{-[(2k+1)\pi c/L]^2 t}$$
Therefore, the solution is
$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\Bigl(\frac{n\pi x}{L}\Bigr) = \sum_{k=0}^\infty \frac{4q_0L^2}{(2k+1)^3\pi^3c^2}\sin\Bigl(\frac{(2k+1)\pi x}{L}\Bigr) + \sum_{k=0}^\infty\frac{4}{(2k+1)\pi}\Bigl[u_0 - \frac{q_0L^2}{(2k+1)^2\pi^2c^2}\Bigr]\times e^{-((2k+1)\pi c/L)^2 t}\sin\Bigl(\frac{(2k+1)\pi x}{L}\Bigr)$$
Margin annotations: an arrow from "steady-state term" to the first sum, and an arrow from "$\to 0$" to the second sum (the transient part decays).
 
**Right page.**
 
**N.** There is another way to approach the inhomogenous heat equation if $q(x,t) = q(x)$ does not depend on $t$. Consider again
$$u_t(x,t) - c^2u_{xx}(x,t) = q_0 \qquad 0 < x < L,\ t > 0$$
As $t \to \infty$, $u(x,t) \to u^s(x,t)$ — the steady state — where
$$\underbrace{u^s_t(x)}_{\to 0} - c^2u^s_{xx}(x) = q_0$$
[the $u^s_t$ term is struck through with "0" written above it; the steady state is written $u^s(x,t)$ in the first line and $u^s(x)$ afterwards.]
and
$$u^s(0) = u^s(L) = 0$$
We first integrate the DE twice: [the word "integrate" is written above a blacked-out word]
$$u^s_{xx} = -q_0/c^2 \iff u^s(x) = -\frac{q_0}{2c^2}x^2 + \alpha x + \beta \iff u^s(x) = -\frac{q_0x}{2c^2}(x - L)$$
<u>Check</u>: that $u^s(x)$ is the steady-state part of our previous solution, i.e.
$$-\frac{q_0x}{2c^2}(x-L) = \sum_{n=1}^\infty\Bigl(\frac{L}{n\pi c}\Bigr)^2\Bigl(\frac{4q_0}{n\pi}\Bigr)\sin\Bigl(\frac{n\pi x}{L}\Bigr) = \sum_{k=0}^\infty\frac{4q_0L^2}{(2k+1)^3\pi^3c^2}\sin\Bigl(\frac{(2k+1)\pi x}{L}\Bigr)$$
[possible error: the middle sum runs over all $n \ge 1$ with $4q_0/(n\pi)$; it should be odd $n$ only (or carry the factor $2(1-(-1)^n)q_0/(n\pi)$), as the right-hand side does. The last step from "$\iff$" to $u^s = -\frac{q_0x}{2c^2}(x-L)$ uses the BCs ($\beta = 0$, $\alpha = q_0L/(2c^2)$), not written. The check is stated, not carried out.]
 
*Figure:* none.
 
---
 
## HW 81 — Another approach (end); stretched string with forcing
_File `20261122_000814.jpg`. Left page "Another approach to inhomo. heat equation" (section 6.4), right page "Stretched string with forcing/loading" (section 6.5). Lower third of the left page and lower half of the right page blank._
 
**Left page.**
 
**N.** To find the unsteady part of the solution,
$$\hat u(x,t) = u(x,t) - u^s(x)$$
Then subbing into the heat equation, we can see that $\hat u(x,t)$ is a solution of the hom. heat eq. Therefore,
$$\hat u(0,t) = u(0,t) - u^s(0) = 0,\qquad \hat u(L,t) = u(L,t) - u^s(L) = 0,$$
$$\hat u(x,0) = u(x,0) - u^s(x) = f(x) - u^s(x) = \hat f(x)$$
but we have the solution of these equations
$$\hat u(x,t) = \sum_{n=1}^\infty \hat A_n e^{-(n\pi c/L)^2t}\sin\Bigl(\frac{n\pi x}{L}\Bigr) \quad\text{where}\quad \hat A_n = \frac{2}{L}\int_0^L\hat f(x)\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x$$
The total solution of the original problem is
$$u(x,t) = u^s(x) + \hat u(x,t)$$
It is easy to see that
$$\hat u(x,t) = \sum_{k=0}^\infty\frac{4}{\pi(2k+1)}\Bigl(u_0 - \frac{q_0L^2}{(2k+1)^2\pi^2c^2}\Bigr)e^{-((2k+1)\pi c/L)^2t}\times\sin\Bigl(\frac{(2k+1)\pi x}{L}\Bigr)$$
 
**Right page.**
 
**N.** We do something similar for the system
$$u_{tt}(x,t) - c^2u_{xx}(x,t) = F(x,t)$$
with
- BC: $u(0,t) = u(L,t) = 0$, $t > 0$
- IC: $u(x,0) = f(x)$, $0 < x < L$; $u_t(x,0) = g(x)$, $0 < x < L$
We proceed similar to before. We try find a solution of the PDE and ICs in the form
$$u(x,t) = \sum_{n=1}^\infty B_n(t)\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
By writing
$$F(x,t) = \sum_{n=1}^\infty K_n(t)\sin\Bigl(\frac{n\pi x}{L}\Bigr) \;\hookrightarrow\; K_n(t) = \frac{2}{L}\int_0^L F(x,t)\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x \quad\text{(known if } F(x,t) \text{ given)}$$
and sub. $u(x,t)$ and $F(x,t)$ into the non-hom. PDE to get a 2nd-order ODE, which we solve to obtain $B_n(t)$. If $F(x,t) = F(x)$ does not depend on $t$, we can simply proceed as in (6.4).
 
*Figure:* none.
 
---
 
## HW 82 — Stretched string under gravity; catenary
_File `20261122_000832.jpg`. Both pages "Stretched string with forcing/loading", section 6.5. Lower quarter of the right page blank apart from the last line._
 
**Left page.**
 
**Ex.** Suppose a string is vibrating in the vertical plane.
 
*Figure (string under gravity):* two vertical posts, the left one shorter, the right one taller (the string's fixed ends), joined by a horizontal axis line that runs slightly past the right post. A wavy curve (about one and a half sine periods) starts at the foot of the left post, rises to a hump, dips below the axis, rises to a second hump and comes down to meet the axis at the right post. Two small downward arrows mark gravity: one on the first hump (labelled with a small symbol that looks like "θ" or a second "g" — ambiguous), one on the trough labelled "$g$".
 
Then taking into account the gravity force,
$$u_{tt}(x,t) - c^2u_{xx}(x,t) = -g$$
for $0 < x < L$, $t > 0$. The steady-state solution
$$u^s(x) = \lim_{t\to\infty} u(x,t)$$
is given by the solution to
$$u^s_{tt}(x) - c^2u^s_{xx}(x) = -g, \qquad u^s(0) = u^s(L) = 0 \quad\Rightarrow\quad u^s(x) = \frac{g}{2c^2}x(x - L)$$
which is the equilibrium displacement of the string under gravity. The shape of a string at rest is given by the catenary.
$$u^s(x) = \frac{2}{\lambda}\sinh\Bigl(\frac{\lambda x}{2}\Bigr)\sinh\Bigl(\frac{\lambda(x-L)}{2}\Bigr) = \frac{1}{\lambda}\Bigl[\cosh\Bigl(\frac{\lambda(2x-L)}{2}\Bigr) - \cosh\Bigl(\frac{\lambda L}{2}\Bigr)\Bigr]$$
where $\lambda$ is determined by
$$\frac{\lambda\ell}{2} = \sinh\Bigl(\frac{\lambda L}{2}\Bigr) \qquad \ell \text{ is length of string}$$
Here we are interested in situation where $\lambda L \ll 1$, $\ell/L \approx 1$, so using $\sinh(\theta) \approx \theta$ for small $\theta$ gives
[possible error: written "$\sinh(\theta) \approx 0$"; the approximation used on the next page is $\sinh\theta \approx \theta$.]
 
**Right page.**
 
**Ex.** (continued)
$$u^s(x) = \frac{2}{\lambda}\Bigl(\frac{\lambda x}{2}\Bigr)\frac{\lambda(x-L)}{2} = \frac{\lambda}{2}x(x-L)$$
[written $u'(x)$; the superscript is $s$, not a prime.]
Thus by comparison, we have $\lambda \approx g/c^2$ so we have
$$\frac{gL}{c^2} \ll 1 \;\Rightarrow\; \rho gL \ll T \;\Rightarrow\; \text{weight} \ll \text{tension}$$
[$c^2 = T/\rho$ from the wave-equation derivation (HW 68–69) is used without being restated.]
As in our previous approach to the heat equation,
- <u>PDE</u>: $u_{tt} - c^2u_{xx} = -g$
- <u>BC</u>: $u(0,t) = u(L,t) = 0$
- <u>IC</u>: $u(x,0) = f(x)$, $u_t(x,0) = g(x)$
[possible error: $g$ is used both for gravity and for the initial velocity $g(x)$.]
and so
$$\underbrace{u(x,t)}_{\text{displacement}} = \underbrace{u^s(x)}_{\text{equib.}} + \underbrace{\hat u(x,t)}_{\text{displ. from eq.}}$$
We (eventually) derive the force string problem for $\hat u(x,t)$ and obtain
$$\hat u(x,t) = \sum_{n=1}^\infty\Bigl[\hat A_n\cos\Bigl(\frac{n\pi c}{L}t\Bigr) + \hat B_n\sin\Bigl(\frac{n\pi c}{L}t\Bigr)\Bigr]\sin\Bigl(\frac{n\pi x}{L}\Bigr)$$
where
$$\hat A_n = \frac{2}{L}\int_0^L\hat f(x)\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x, \qquad \frac{n\pi c}{L}\hat B_n = \frac{2}{L}\int_0^L g(x)\sin\Bigl(\frac{n\pi x}{L}\Bigr)\dd x$$
[\"force string\" as written, presumably \"free string\"; $\hat f = f - u^s$ by analogy with HW 81, not defined on this page.]
 
**Ex.** Plucked string (see MATH2011 pg. 107) [a pointer to CN MATH2011 p. 107; nothing else is written.]
 
---
 
## HW 83 — Steady-state 2-D heat: Laplace's equation; iron bar; rectangular beam (setup)
_File `20261122_000845.jpg`. Both pages "Steady-state 2-D heat", section 6.6. Lower third of the left page and lower quarter of the right page blank._
 
**Left page.**
 
**N.** Recall the 3D heat equation
$$u_t(x,y,z,t) = c^2\nabla^2u(x,y,z,t)$$
For a steady-state temperature distribution, $u = u(x,y,z)$ implies that $u_t = 0$. Thus the heat equation reduced to Laplace's equation:
$$\nabla^2u(x,y,z) = 0 \;\Rightarrow\; u_{xx} + u_{yy} + u_{zz} = 0$$
If there is no $y$ or $z$ dependence, this problem simplifies to $u_{xx}(x) = 0 \Rightarrow u(x) = \alpha x + \beta$. [an ink blot over the "=".]
 
**Ex.** Consider the iron bar example below:
 
*Figure (iron bar):* a rectangular bar drawn in perspective, long axis running to the upper right, front (left) end face a rounded rectangle. A curved arrow from the label "$u = u_0$" (upper left) points into a dot at the centre of the left end face; a line from the label "$u = u_1$" (right) points to a dot near the centre of the far (right) end. Inside the bar a dotted line runs along the axis, with a short arrow on it near the middle labelled "$u(x)$", and an "$L$" written near the far end (the bar's length). A dotted vertical line marks a cross-section part way along.
 
Then
$$u_0 = u(0) \Rightarrow u_0 = \beta \Rightarrow u(x) = \alpha x + u_0$$
$$u_1 = u(L) \Rightarrow u_1 = \alpha L + u_0 \Rightarrow \alpha = u_1 - u_0/L$$
which implies
$$u(x) = \frac{u_1 - u_0}{L}x + u_0$$
[\"$\alpha = u_1 - u_0/L$\" is missing brackets: $(u_1-u_0)/L$, as in the last line. The second line is written \"$u_L = u(L)$\" with the subscript unclear; $u_1$ is meant.]
 
**Right page.**
 
**N.** If there is no $z$ dependence, $u$ satisfies the 2D Laplace equation:
$$u_{xx}(x,y) + u_{yy}(x,y) = 0$$
To solve this we employ Fourier's method.
 
**Ex.** Now consider a steady temperature distribution in a long beam of rectangular cross-section:
 
*Figure (beam):* a sketchy long beam drawn in perspective: two long parallel lines for the top edges running to the upper left, a long line for the bottom edge, and short dashed strokes between them suggesting the faces (no closed outline). To its right a small 3D axis triad: $y$ up, $x$ down-right, $z$ left. Labels to the right: "$u = f(x)$ on top face", "$u = 0$ on other three faces". [The sketch is faint and schematic; the CN figure for this example (MATH2011 CN §6.6) may be the better model for the redraw.]
 
Now there are no ICs, but only BCs. We thus have a boundary value problem (BVP):
- PDE: $u_{xx}(x,y) + u_{yy}(x,y) = 0$, $0 < x < a$, $0 < y < b$
- BCs: $u(0,y) = 0$, $0 < y < b$; $u(a,y) = 0$, $0 < y < b$; $u(x,0) = 0$, $0 < x < a$; $u(x,b) = f(x)$, $0 < x < a$
We look for all possible solutions to the homogenous equations in the separable form
$$u(x,y) = F(x)G(y)$$
 
---
 
## HW 84 — Steady-state 2-D heat: separation, the three cases for $k$
_File `20261122_000900.jpg`. Both pages "Steady-state 2-D heat", section 6.6. Lower fifth of the right page blank._
 
**Left page.**
 
**N.** First we consider the homogenous BCs:
$$u(0,y) = 0 \Rightarrow F(0)G(y) = 0 \Rightarrow F(0) = 0$$
$$u(a,y) = 0 \Rightarrow F(a)G(y) = 0 \Rightarrow F(a) = 0$$
$$u(x,0) = 0 \Rightarrow F(x)G(0) = 0 \Rightarrow G(0) = 0$$
Now consider the PDE: we sub. the expression $u(x) = F(x)G(y)$ into the PDE [$u(x)$ as written; $u(x,y)$ meant]
$$F''(x)G(y) + F(x)G''(y) = 0 \;\Rightarrow\; \frac{F''(x)}{F(x)} = -\frac{G''(y)}{G(y)} = k$$
We therefore have an $F$-system and $G$-system:
- $F$-system: $F''(x) = kF(x)$, $F(0) = F(a) = 0$
- $G$-system: $G''(y) = -kG(y)$, $G(0) = 0$
We first consider the $F$-system, with three cases:
Case (a): $k = 0$
$$F''(x) = 0 \Rightarrow F(x) = Ax + B;\quad \text{as } F(0) = 0 \Rightarrow F(x) = Ax;\quad \text{as } F(a) = 0 \Rightarrow F(x) = 0$$
which implies we have a trivial solution. Thus for non-trivial solutions, $k \ne 0$.
 
**Right page.**
 
**N.** Case (b): $k > 0$, $k = \mu^2$
$$F''(x) = \mu^2F(x) \Rightarrow F(x) = Ae^{\mu x} + Be^{-\mu x}$$
as $F(0) = 0 \Rightarrow A + B = 0$; as $F(a) = 0 \Rightarrow Ae^{2\mu a} + B = 0$
which leads to $A = 0$, $B = 0$, which is the trivial solution. Thus for non-trivial solutions, $k < 0$.
 
Case (c): $k < 0$, $k = -p^2$, $p > 0$
$$F''(x) = -p^2F(x) \Rightarrow F(x) = A\cos(px) + B\sin(px)$$
as $F(0) = 0 \Rightarrow A = 0 \Rightarrow F(x) = B\sin(px)$;
as $F(a) = 0 \Rightarrow B\sin(pa) = 0 \Rightarrow \sin(pa) = 0$ ($B = 0$ is trivial) $\Rightarrow pa = n\pi$ for $n \in \N$
which implies $p = \frac{n\pi}{a}$. Therefore $F(x) = B\sin\bigl(\frac{n\pi}{a}x\bigr)$.
 
The $G$-system, with our value of $k$, is thus
$$G''(y) = \Bigl(\frac{n\pi}{a}\Bigr)^2G(y) \Rightarrow G(y) = C\cosh(n\pi/a\,y) + D\sinh(n\pi/a\,y) \Rightarrow G(y) = D\sinh(n\pi/a\,y) \quad (\text{as } G(0) = 0)$$
We therefore have the infinite family of solutions:
$$u_n(x,y) = B_n\sin\Bigl(\frac{n\pi}{a}x\Bigr)\sinh\Bigl(\frac{n\pi}{a}y\Bigr)$$
 
---
 
## HW 85 — Steady-state 2-D heat: superposition, coefficients; triangular-profile example
_File `20261122_000913.jpg`. Both pages "Steady-state 2-D heat", section 6.6. Lower fifth of the right page blank._
 
**Left page.**
 
**N.** Using the superposition principle:
$$u(x,y) = \sum_{n=1}^\infty B_n\sin\Bigl(\frac{n\pi x}{a}\Bigr)\sinh\Bigl(\frac{n\pi y}{a}\Bigr)$$
There is one more boundary condition left to fix $B_n$:
$$u(x,b) = f(x) \Rightarrow f(x) = u(x,b) = \sum_{n=1}^\infty B_n\sinh\Bigl(\frac{n\pi b}{a}\Bigr)\sin\Bigl(\frac{n\pi}{a}x\Bigr)$$
which is the Fourier half-range sine series, $0 < x < a$ for $f(x)$. Thus
$$B_n\sinh\Bigl(\frac{n\pi b}{a}\Bigr) = \frac{2}{a}\int_0^a f(x)\sin\Bigl(\frac{n\pi}{a}x\Bigr)\dd x$$
which implies
$$B_n = \frac{2}{a\sinh\bigl(\frac{n\pi b}{a}\bigr)}\int_0^a f(x)\sin\Bigl(\frac{n\pi}{a}x\Bigr)\dd x$$
 
**Ex.** Let
$$f(x) = \begin{cases} \dfrac{2u_0}{a}x & 0 < x < a/2\\[1mm] \dfrac{2u_0}{a}(a - x) & a/2 < x < a\end{cases}$$
[The constant is written like "$\mu_0$" on this page and "$u_0$" on the next; $u_0$ is meant.]
We may want to guess (by symmetry) that $u(x,y) = \frac{y}{b}f(x)$. It is easy to verify this satisfies the PDE and all BCs, except on the line $x = a/2$. However, this is not the solution!
 
**Right page.**
 
**Ex.** Using the Fourier series we have
$$u(x,y) = \sum_{n=1}^\infty B_n\sin\Bigl(\frac{n\pi x}{a}\Bigr)\sinh\Bigl(\frac{n\pi y}{a}\Bigr)$$
where
$$B_n = \frac{2}{a\sinh\bigl(\frac{n\pi b}{a}\bigr)}\Bigl[\int_0^{a/2}\frac{2u_0}{a}x\sin\Bigl(\frac{n\pi}{a}x\Bigr)\dd x + \int_{a/2}^a\frac{2u_0}{a}(a-x)\sin\Bigl(\frac{n\pi}{a}x\Bigr)\dd x\Bigr]$$
Using integration by parts,
$$\int x\sin(\alpha x)\dd x = -\frac{x}{\alpha}\cos(\alpha x) + \frac{1}{\alpha^2}\sin(\alpha x)$$
we have
$$
\begin{aligned}
B_n = \dots = \frac{4u_0}{a^2\sinh\bigl(\frac{n\pi b}{a}\bigr)}\Bigl\{&-\frac{a^2}{2n\pi}\cos\Bigl(\frac{n\pi}{2}\Bigr) + \Bigl(\frac{a}{n\pi}\Bigr)^2\sin\Bigl(\frac{n\pi}{2}\Bigr) - (0+0)\\
&- \Bigl[-\frac{a^2}{n\pi}\cos(n\pi) + 0 - \Bigl(-\frac{a^2}{n\pi}\cos\Bigl(\frac{n\pi}{2}\Bigr) + \Bigl(\frac{a}{n\pi}\Bigr)^2\sin\Bigl(\frac{n\pi}{a}\Bigr)\Bigr)\Bigr]\Bigr\}\\
&- \frac{4u_0}{n\pi\sinh(n\pi b/a)}\times\bigl[\cos(n\pi) - \cos(n\pi/2)\bigr]\\
= \frac{8u_0}{(n\pi)^2}\cdot\frac{1}{\sinh(n\pi b/a)}\sin\Bigl(\frac{n\pi}{2}\Bigr) &\quad \Big\}\ 0 \text{ if } n \text{ even},\ (-1)^m\ \ 2m+1
\end{aligned}
$$
[Layout of the intermediate step as written; the brackets do not close cleanly. possible error: inside the square bracket, $\sin(n\pi/a)$ should be $\sin(n\pi/2)$, and the inner $-\frac{a^2}{n\pi}\cos(n\pi/2)$ should be $-\frac{a^2}{2n\pi}\cos(n\pi/2)$ (the $x$-term at $x = a/2$). The final result is correct: checked, $B_n = \frac{2}{a\sinh(n\pi b/a)}\cdot\frac{2u_0}{a}\cdot 2\bigl(\frac{a}{n\pi}\bigr)^2\sin\frac{n\pi}{2} = \frac{8u_0\sin(n\pi/2)}{(n\pi)^2\sinh(n\pi b/a)}$. The brace note means $\sin(n\pi/2) = 0$ for $n$ even and $(-1)^m$ for $n = 2m+1$.]
 
---
 
## HW 86 — Laplace's equation: smoothness, maximum property, general rectangle problem; fundamental solution of the heat equation
_File `20261122_000928.jpg`. Left page "Steady-state 2-D heat" (section 6.6), right page "Fundamental solution of heat equation" (section 7.1). The left page is photographed at a slight angle and is a little soft at the bottom, but readable. Lower fifth of the right page blank._
 
**Left page.**
 
**N.** It can be shown that the above solution is <u>very smooth</u> inside the region $\{(x,y) : 0 < x < a,\ 0 < y < b\}$ which is a general feature of Laplace's equation in 2D. Another interesting property for Laplace's equation is that $u(x,y)$ in the interior does not take any values bigger than the largest value of $u$ on the boundary.
 
The solution of the more general problem is given by
 
*Figure (general Dirichlet problem on a rectangle):* axes with the vertical axis on the left and the horizontal axis (arrow to the right) at the bottom; $a$ is marked below the horizontal axis at the right side of the rectangle. A rectangle sits in the first quadrant with its left side on the vertical axis and its bottom on the horizontal axis. Inside: "$\nabla^2u = 0$". Boundary labels with short curved arrows pointing at the side: top "$u = f(x)$"; right "$\leftarrow u = h(y)$"; bottom "$u = g(x)$" (arrow up from below); left, a label at the top left of the axis with a hooked arrow to the left side, read "$u = h(y)$" or "$u = k(y)$" [ambiguous in the notebook: the letter looks like "h", but the decomposition below gives the left side $k$, so $u = k(y)$ is meant].
 
$$u(x,y) = u^{(1)}(x,y) + u^{(2)}(x,y) + u^{(3)}(x,y) + u^{(4)}(x,y)$$
 
*Figure (decomposition):* four small rectangles in a row, one under each term (arrow from each term down to its rectangle). The boundary values are written beside each side:
1. top $f$, right $0$, bottom $0$, left $0$
2. top $0$, right $0$, bottom $g$, left $0$
3. top $0$, right $h$, bottom $0$, left $0$
4. top $0$, right $0$, bottom $0$, left $k$
[In rectangle 1 the top label is a small "f" that looks like "$\ddagger$"; in rectangle 4 the bottom "0" is a filled dot.]
 
where each solution is obtained in a similar way to the previous example.
 
**Right page.**
 
**N.** Here we consider heat conduction in an infinitely long cylinder with insulated sides — the boundaries are effectively at $\pm\infty$. Now the problem is defined by
$$u_t(x,t) = c^2u_{xx}(x,t),\quad t \ge 0,\ -\infty < x < \infty; \qquad u(x,0) = f(x),\quad -\infty < x < \infty$$
Here Fourier's method is not useful.
 
We instead use a special solution:
$$G(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\exp\bigl(-x^2/4c^2t\bigr)$$
This is called the fundamental solution to the 1D heat equation on $(-\infty,\infty)$.
 
**N.** Some properties of the fund. sol. $G(x,t)$ is:
- $\lim_{t\to0^+}G(x,t) = 0$ for $x \ne 0$ (L'Hopital's)
- $\lim_{t\to0^+}G(0,t) = \lim_{t\to0^+}\frac{1}{\sqrt{4\pi c^2t}} = +\infty$
- $\int_{-\infty}^\infty G(x,t)\dd x = 1$ $\forall t > 0$
---
 
## HW 87 — Properties of the fundamental solution; 1-D heat equation on the line, general solution
_File `20261122_000942.jpg`. Left page "Properties of fundamental solution" (section 7.1), right page "1-D heat equation general solution" (section 7.2). The left page curves into the gutter; line ends there are soft but readable at full resolution. Lower quarter of the left page blank._
 
**Left page.**
 
**N.** Note that at any $t > 0$, $G(x,t)$ is a Gaussian:
 
*Figure (fundamental solution at several times):* axes with a vertical axis in the middle and a horizontal axis. Three (or four) bell curves centred on the vertical axis, nested: the tallest and narrowest on top, then progressively lower and wider ones, the lowest nearly flat along the axis. No labels on the curves. Text to the right: "where the area under each curve is 1. As $t \to 0^+$, we approach an infinite spike at $x = 0$."
 
This limit below is the Dirac $\delta$-function.
$$\delta(x) = \lim_{t\to0^+}G(x,t) = \begin{cases} 0 & x \ne 0\\ \infty & x = 0\end{cases}$$
The amount of energy in the system at any time $t$ is
$$H(t) = \int_{-\infty}^\infty\rho\sigma G(x,t)\dd x = \rho\sigma\int_{-\infty}^\infty G(x,t)\dd x = \rho\sigma$$
As $t \to 0^+$, all of the heat energy is localised at $t = 0$. [Read from a full-resolution crop of the gutter. possible error: presumably "localised at $x = 0$" (as $t \to 0^+$).] Therefore, $G(x,t)$ is the temperature distribution at $t > 0$ resulting from injection of amount of heat $\rho\sigma$ into the system at $x = 0$ at $t = 0$.
 
We can translate/shift this anywhere on the $x$-axis by the translation $G(x - y, t)$.
 
**Right page.**
 
**N.** If we inject heat $\alpha_1\rho\sigma$ at $y_1$, $\alpha_2\rho\sigma$ at $y_2$, … by superposition, we have that
$$\alpha_1G(x - y_1, t) + \alpha_2G(x - y_2, t) + \cdots$$
is also a solution to the infinite length heat equation.
 
We now claim that the solution of the infinite heat equation with initial conditions is
$$u(x,t) = \int_{-\infty}^\infty G(x-y,t)\underbrace{f(y)}_{\text{`IC'}}\dd y$$
This is a convolution integral. It can be thought of as injecting heat $\rho\sigma f(y)\dd y$ in $(y, y + \dd y)$ along the $x$-axis to establish the initial temp. distribution. [an ink blot between "$y$" and "$y+\dd y$"]
 
**P.** For the PDE, let
$$u_t(x,t) = \frac{\partial}{\partial t}\int_{-\infty}^\infty G(x-y,t)f(y)\dd y, \qquad u_{xx}(x,t) = \frac{\partial^2}{\partial x^2}\int_{-\infty}^\infty G(x-y,t)f(y)\dd y$$
Interchange the integral and derivative.
For the BC, make the substitution
$$z = \frac{y - x}{\sqrt{4c^2t}} \Rightarrow \dd y = \sqrt{4c^2t}\dd z$$
then compute $u(x,t)$ and take $t \to 0^+$.
[Proof sketch only. possible error: "For the BC" should be "for the IC" (the condition checked is $u(x,0^+) = f(x)$).]
 
---
 
## HW 88 — 1-D heat equation on the line: solution formula; step initial data and the error function
_File `20261122_000952.jpg`. Both pages "1-D heat equation general solution", section 7.2. Lower third of the right page blank._
 
**Left page.**
 
**N.** Therefore, the solution for the heat equation with IC $u(x,0) = f(x)$ is: [a blacked-out word after "IC"]
$$u(x,t) = \int_{-\infty}^\infty G(x-y,t)f(y)\dd y = \frac{1}{\sqrt{4\pi c^2t}}\int_{-\infty}^\infty e^{-(x-y)^2/4c^2t}f(y)\dd y$$
 
**Ex.** Let
$$f(x) = \begin{cases} u_0 & x > 0\\ u_1 & x < 0\end{cases} \qquad u_0, u_1 \in \R.$$
The solution is
$$u(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\Bigl\{u_0\int_0^\infty e^{-(x-y)^2/4c^2t}\dd y + u_1\int_{-\infty}^0 e^{-(x-y)^2/4c^2t}\dd y\Bigr\}$$
Make the substitution
$$z = \frac{x - y}{\sqrt{4c^2t}} \Rightarrow y = x - \sqrt{4c^2t}\,z \Rightarrow \dd y = -\sqrt{4c^2t}\dd z$$
where $y = 0 \Rightarrow z = x/\sqrt{4c^2t}$, $y = \pm\infty \Rightarrow z = \mp\infty$. [the "$\mp$" is written above a blotted-out sign]
Note that
$$\int_{-\infty}^0 e^{-x^2}\dd x = \int_0^\infty e^{-x^2}\dd x = \frac{\sqrt\pi}{2}.$$
 
**Right page.**
 
**N.** Then, we have: [the upper limits "$x/\dots$" abbreviate $x/\sqrt{4c^2t}$]
$$
\begin{aligned}
u(x,t) &= -\frac{u_0}{\sqrt\pi}\int_{x/\sqrt{4c^2t}}^{-\infty}e^{-z^2}\dd z - \frac{u_1}{\sqrt\pi}\int_\infty^{x/\dots}e^{-z^2}\dd z\\
&= \frac{u_0}{\sqrt\pi}\int_{-\infty}^{x/\dots}e^{-z^2}\dd z + \frac{u_1}{\sqrt\pi}\int_{x/\dots}^\infty e^{-z^2}\dd z\\
&= \frac{u_0}{\sqrt\pi}\Bigl\{\int_{-\infty}^0e^{-z^2}\dd z + \int_0^{x/\dots}e^{-z^2}\dd z\Bigr\} + \frac{u_1}{\sqrt\pi}\Bigl\{\int_0^\infty e^{-z^2}\dd z + \int_{x/\dots}^0e^{-z^2}\dd z\Bigr\}\\
&= \frac{u_0}{\sqrt\pi}\times\frac{\sqrt\pi}{2} + \frac{u_0}{\sqrt\pi}\int_0^{x/\dots}e^{-z^2}\dd z - \frac{u_1}{\sqrt\pi}\int_0^{x/\dots}e^{-z^2}\dd z + \frac{u_1}{\sqrt\pi}\times\frac{\sqrt\pi}{2}\\
&= \tfrac12(u_0 + u_1) + \tfrac12(u_0 - u_1)\operatorname{erf}\Bigl(\frac{x}{\sqrt{4c^2t}}\Bigr)
\end{aligned}
$$
where (recall)
$$\operatorname{erf}(x) = \frac{2}{\sqrt\pi}\int_0^xe^{-z^2}\dd z$$
[Checked: correct. The lower limit 0 in the third line's $u_1$ integral is written over a blot.]
 
---
 
## HW 89 — Heat equation on the line: odd step-pulse example; reading it as a half-line problem
_File `20261122_001003.jpg`. Both pages "1-D heat equation general solution", section 7.2. The right ends of the last lines of the left page run into the gutter but are repeated legibly on the right page's edge. Lower two-thirds of the right page blank._
 
**Left page.**
 
**Ex.** Let
$$f(x) = u(x,0) = \begin{cases} u_0 & 0 < x < a\\ -u_0 & -a < x < 0\\ 0 & \abs{x} > a\end{cases} \qquad u_0 \in \R$$
The solution is
$$u(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_{-\infty}^\infty e^{-(x-y)^2/4c^2t}f(y)\dd y = \frac{1}{\sqrt{4\pi c^2t}}\Bigl\{u_0\int_0^ae^{-(x-y)^2/4c^2t}\dd y - u_0\int_{-a}^0e^{-(x-y)^2/4c^2t}\dd y\Bigr\}$$
Make the substitution
$$z = \frac{x - y}{\sqrt{4c^2t}} \Rightarrow y = 0 \to z = x/\sqrt{4c^2t},\quad y = \pm a \to z = x \mp a/\sqrt{4c^2t}$$
[the "$\mp$" is written above a blotted sign; $(x \mp a)/\sqrt{4c^2t}$ meant.]
Then
$$
\begin{aligned}
u(x,t) &= \frac{u_0}{\sqrt\pi}\Bigl\{-\int_{-x/\sqrt{4c^2t}}^{(x+a)/\sqrt{4c^2t}}e^{-z^2}\dd z + \int_{x-a/\sqrt{4c^2t}}^{x/\sqrt{4c^2t}}e^{-z^2}\dd z\Bigr\}\\
&= \frac{u_0}{\sqrt\pi}\Bigl\{-\int_{x/\sqrt{4c^2t}}^0e^{-z^2}\dd z - \int_0^{x+a/\sqrt{4c^2t}}e^{-z^2}\dd z + \int_{x-a/\sqrt{4c^2t}}^0e^{-z^2}\dd z + \int_0^{x/\sqrt{4c^2t}}e^{-z^2}\dd z\Bigr\}\\
&= \frac{u_0}{2}\Bigl\{2\operatorname{erf}\Bigl(\frac{x}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{x+a}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{x-a}{\sqrt{4c^2t}}\Bigr)\Bigr\}
\end{aligned}
$$
[possible error: the lower limit of the first integral is written $-x/\sqrt{4c^2t}$; it should be $x/\sqrt{4c^2t}$ (as in the next line). "$x \pm a/\sqrt{4c^2t}$" throughout means $(x \pm a)/\sqrt{4c^2t}$. Final result checked: correct.]
Note that
$$u(0,t) = \frac{u_0}{2}\Bigl\{2\operatorname{erf}(0) - \operatorname{erf}\Bigl(\frac{a}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{-a}{\sqrt{4c^2t}}\Bigr)\Bigr\} = 0$$
 
**Right page.**
 
**N.** Note that the solution $u(x,t)$ of this problem satisfies $u(0,t)$ for $t > 0$. Thus the solution of [\"$u(0,t) = 0$\" meant]
$$u_t(x,t) = c^2u_{xx}(x,t),\quad \underline{0 < x < \infty},\ t > 0$$
$$\text{IC}\ \Bigl\{\ u(x,0) = \begin{cases} u_0 & 0 < x < a\\ 0 & x > a\end{cases} \qquad \text{BC}\ \{\ u(0,t) = 0 \quad t > 0$$
is also given by
$$u(x,t) = \frac{u_0}{2}\Bigl\{2\operatorname{erf}\Bigl(\frac{x}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{x+a}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{x-a}{\sqrt{4c^2t}}\Bigr)\Bigr\}$$
but now we are restricted to $x \ge 0$, $t \ge 0$.
 
---
 
## HW 90 — 1-D heat equation: method of images
_File `20261122_001023.jpg`. Both pages "1-D heat equation method of images", section 7.3. Lower half of the right page blank._
 
**Left page.**
 
**N.** Following the previous example, we consider the problem
$$u_t(x,t) = c^2u_{xx}(x,t),\quad 0 < x < \infty,\ t > 0$$
with
- IC: $u(x,0) = F(x)$, $0 < x < \infty$
- BC: $u(0,t) = 0$, $t > 0$
The idea is to convert to a problem on the whole $x$-axis with no boundary. This is done by extending the initial condition to an odd function:
$$F(x),\ 0 < x < \infty \;\longrightarrow\; f(x) = \begin{cases} F(x) & 0 < x < \infty\\ -F(-x) & -\infty < x < 0\end{cases}$$
The solution to the extended problem on $-\infty < x < \infty$ also provides a solution of the original problem on $0 < x < \infty$, including BC. This is called the <u>method of images</u>.
 
The solution is
$$
\begin{aligned}
u(x,t) &= \frac{1}{\sqrt{4\pi c^2t}}\int_{-\infty}^\infty e^{-(x-y)^2/4c^2t}f(y)\dd y\\
&= \frac{1}{\sqrt{4\pi c^2t}}\Bigl\{\int_0^\infty F(y)e^{-(x-y)^2/4c^2t}\dd y + \int_{-\infty}^0 -F(-y)e^{-(x-y)^2/4c^2t}\dd y\Bigr\}\\
&= \frac{1}{\sqrt{4\pi c^2t}}\Bigl\{\int_0^\infty F(y)e^{-(x-y)^2/4c^2t}\dd y + \int_\infty^0 e^{-(x+y)^2/4c^2t}\dd y\Bigr\}
\end{aligned}
$$
[possible error: the last integral has lost its factor $F(y)$ (after $y \to -y$ it is $\int_\infty^0 F(y)e^{-(x+y)^2/4c^2t}\dd y$, as the next page uses).]
 
**Right page.**
 
**N.** (continued)
$$u(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_0^\infty F(y)\Bigl[e^{-(x-y)^2/4c^2t} - e^{-(x+y)^2/4c^2t}\Bigr]\dd y$$
Note that, as required,
$$u(0,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_0^\infty\bigl(e^{-y^2/4c^2t} - e^{-y^2/4c^2t}\bigr)F(y)\dd y = 0$$
[the bracket is struck through with an arrow to "0".]
 
**Rem.** In the case of a non-zero BC $u(0,t) = u_0 \ne 0$, we must first convert to a zero BC before applying the method of images. We set
$$\hat u(x,t) = u(x,t) - u_0$$
[$u_0$ written above a blotted symbol]
which satisfies the heat equation, but now has boundary conditions $\hat u(0,t) = u(0,t) - u_0 = 0$ and initial conditions $\hat u(x,0) = u(x,0) = u_0 = F(x) - u_0$. We then solve for $\hat u(x,t)$ and set $u(x,t) = \hat u(x,t) + u_0$.
[possible error: "$\hat u(x,0) = u(x,0) = u_0$" should read $\hat u(x,0) = u(x,0) - u_0 = F(x) - u_0$.]
 
---
 
## HW 91 — Method of images for an insulated end
_File `20261122_001034.jpg`. Both pages "1-D heat equation method of images", section 7.3. Lower half of the right page blank._
 
**Left page.**
 
**N.** Now suppose we have the insulation condition.
 
*Figure (bar with insulated end):* a bar drawn in perspective (a rectangle with a rounded right end), its left end face hatched with diagonal lines and a dot at its centre; a label "insulated face" above with a line to the hatched face. A horizontal axis through the middle of the bar, arrow to the right, labelled $x$; a vertical line divides the bar near its middle. To the right, double-underlined: "$u(0,t) = 0$". [possible error: for an insulated face the condition is $u_x(0,t) = 0$, as in the BC below.]
 
Then we have
$$u_t(x,t) = c^2u_{xx}(x,t),\quad 0 < x < \infty,\ t > 0$$
with
- IC: $u(x,0) = F(x)$, $0 < x < \infty$
- BC: $u_x(0,t) = 0$, $t > 0$
The trick this time is to extend the problem to the whole $x$-axis with an even initial function:
$$F(x),\ 0 < x < \infty \;\longrightarrow\; f(x) = \begin{cases} F(x) & 0 < x < \infty\\ F(-x) & -\infty < x < 0\end{cases}$$
Again a solution of the extended problem also gives a solution of the original problem on $0 < x < \infty$.
 
The solution is
$$u(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_{-\infty}^\infty e^{-(x-y)^2/4c^2t}F(y)\dd y = \frac{1}{\sqrt{4\pi c^2t}}\Bigl\{\int_0^\infty e^{-(x-y)^2/4c^2t}F(y)\dd y + \int_{-\infty}^0e^{-(x-y)^2/4c^2t}F(-y)\dd y\Bigr\}$$
[possible error: in the first integral $F(y)$ should be the extension $f(y)$.]
 
**Right page.**
 
**N.** (continued) Proceeding as before, we obtain
$$u(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_0^\infty F(y)\Bigl[e^{-(x-y)^2/4c^2t} + e^{-(x+y)^2/4c^2t}\Bigr]\dd y$$
For the boundary conditions, note
$$u_x(x,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_0^\infty\Bigl\{-\frac{x-y}{2c^2t}e^{-(x-y)^2/4c^2t} - \frac{x+y}{2c^2t}e^{-(x+y)^2/4c^2t}\Bigr\}F(y)\dd y$$
and so
$$u_x(0,t) = \frac{1}{\sqrt{4\pi c^2t}}\int_0^\infty\Bigl\{\frac{y}{2c^2t}e^{-y^2/4c^2t} - \frac{y}{2c^3t}e^{-y^2/4c^2t}\Bigr\}F(y)\dd y = 0$$
[possible error: the second denominator is written $2c^3t$; it should be $2c^2t$ (otherwise the terms don't cancel).]
 
---
 
## HW 92 — Method of images: insulated semi-infinite slab; temperature waves in the Earth (start)
_File `20261122_001049.jpg`. Left page "1-D heat equation method of images" (section 7.4), right page "Ex: Temperature waves in the Earth" (section 7.5). Lower fifth of the right page blank._
 
**Left page.**
 
**Ex.** Consider the semi-infinite slab
 
*Figure (semi-infinite slab):* a short vertical line at the left with diagonal hatching to its right (the insulated face), labelled below "↖ insulated face"; from it a horizontal arrow runs to the right, labelled "$u(x,t)$" above.
 
with $u_t(x,t) = c^2u_{xx}(x,t)$,
- IC: $u(x,0) = F(x) = \begin{cases} u_0 & 0 < x < \ell\\ 0 & x > \ell\end{cases}$
- BC: $u_x(0,t) = 0$
We use the method of images and extend $F$ to an even function
$$f(x) = \begin{cases} F(x) & x > 0\\ F(-x) & x < 0\end{cases}$$
 
*Figure (even extension):* left: axes (vertical axis at the left, horizontal axis with arrow to the right); a horizontal segment at height $u_0$ (labelled on the vertical axis) from the axis to a point, then a dashed vertical drop to the horizontal axis (at $x = \ell$, not labelled). A curved arrow points right to a rectangle that is completely scribbled out (a discarded first attempt). Below it, the redrawn extension: a horizontal axis with arrows at both ends and a vertical axis in the middle; a horizontal segment at height $u_0$ (label at the right end) running symmetrically either side of the vertical axis, with dashed vertical drops to the axis at both ends ($x = \pm\ell$, not labelled).
 
The solution (see problem sheet) is
$$u(x,t) = \frac{u_0}{2}\Bigl\{\operatorname{erf}\Bigl(\frac{x+\ell}{\sqrt{4c^2t}}\Bigr) - \operatorname{erf}\Bigl(\frac{x-\ell}{\sqrt{4c^2t}}\Bigr)\Bigr\}$$
but now for $x \ge 0$, $t \ge 0$.
[The derivation is left to the problem sheet; not in the notes.]
 
**Right page.**
 
**N.** Consider the variation of temperature in soil as a result of periodic variation of temperature at the surface (either daily or yearly)
 
*Figure (soil):* a horizontal line (the ground surface) with a small circle on it; from the circle a vertical arrow points down, labelled $x$ on its left (depth). To the right of the arrow, under a small "$\tau$" [or a squiggle; ambiguous], the label "$u = u_0\cos(\omega t)$" at the surface. Text to the right: "We model a semi-infinite region with sinusoidal BC."
 
We have:
$$u_t(x,t) = c^2u_{xx}(x,t) \qquad 0 \le x < \infty,\ -\infty < t < \infty$$
with
- BC: $u(0,t) = u_0\cos(\omega t)$
- IC: irrelevant here
It is convenient to consider the BC in complex form:
$$\text{BC: } u(0,t) = u_0\exp(i\omega t)$$
and, inspired by the method of separation of variables, look for a complex solution in the form —
$$u(x,t) = X(x)\exp(i\omega t)$$
— the real part will provide the desired solution. Then,
$$u_t(x,t) = i\omega X(x)e^{i\omega t}, \qquad u_{xx}(x,t) = X''(x)e^{i\omega t}$$
and we substitute into the PDE to get (continued.)
 
---
 
## HW 93 — Temperature waves in the Earth (solution)
_File `20261122_001059.jpg`. Both pages "Ex: temperature waves in the Earth", section 7.5. Lower quarter of the left page and lower third of the right page blank._
 
**Left page.**
 
**N.** (continued)
$$0 = u_t(x,t) - c^2u_{xx}(x,t) = \bigl[i\omega X(x) - c^2X''(x)\bigr]e^{i\omega t}$$
which implies
$$X''(x) = \frac{i\omega}{c^2}X(x) = \alpha^2X(x)$$
[written $\ddot X(x)$, with dots, on the left-hand side]
and thus
$$\alpha_\pm = \pm\Bigl(\frac{i\omega}{c^2}\Bigr)^{1/2} = \pm\sqrt{\frac{\omega}{c^2}}\,i^{1/2} = \pm\sqrt{\frac{\omega}{c^2}}\bigl(e^{\pi i/2}\bigr)^{1/2} = \pm\sqrt{\frac{\omega}{c^2}}\,e^{\frac{\pi}{4}i} = \pm\sqrt{\frac{\omega}{c^2}}\Bigl(\cos\frac\pi4 + i\sin\frac\pi4\Bigr) = \pm\sqrt{\frac{\omega}{c^2}}\,\frac{1+i}{\sqrt2}$$
and so
$$X(x) = Ae^{\alpha_+x} + Be^{\alpha_-x} = Ae^{\sqrt{\frac{\omega}{2c^2}}(1+i)x} + Be^{-\sqrt{\frac{\omega}{2c^2}}(1+i)x}$$
which implies (as we want $X(x)$ to be bounded as $x \to \infty$)
$$X(x) = B\exp\Bigl\{-\sqrt{\frac{\omega}{2c^2}}(1+i)x\Bigr\}$$
 
**Right page.**
 
**N.** (continued) Therefore,
$$u(x,t) = u_0e^{-\sqrt{\frac{\omega}{2c^2}}x}e^{i(\omega t - \sqrt{\frac{\omega}{2c^2}}x)}$$
[$B = u_0$ from the BC $u(0,t) = u_0e^{i\omega t}$; this step is not written. An ink blot before the "$x$" in the second exponent.]
and taking the real part we obtain
$$u(x,t) = u_0e^{-\sqrt{\frac{\omega}{2c^2}}x}\cos\Bigl(\omega t - \sqrt{\frac{\omega}{2c^2}}x\Bigr)$$
This solution describes an attenuated temperature wave, where amplitude decreases exponentially as $x$ increases.
 
**Rem.**
1. It can be checked directly that this $u(x,t)$ satisfies the PDE and the BCs.
2. The temperature at depth $x$ is out of phase with the temperature at $x = 0$.
3. The larger $\omega$ is, the greater the attenuation and the smaller the penetration of the wave into the soil. Therefore:
   - daily variations → smaller penetration
   - yearly variations → larger penetration
see pg. 135 for details. [= CN MATH2011 p. 135]
 
---
 
## HW 94 — Lord Kelvin's Earth-age model; harmonic functions
_File `20261122_001116.jpg`. Left page "Ex: Lord Kelvin's Earth age model" (section 7.6), right page "Harmonic functions" (section 7.7; a blacked-out word precedes the title). Lower fifth of the left page blank._
 
**Left page.**
 
**N.** On a completely different length scale, as we bore down into the Earth's crust, the temperature steadily increases by $\sim 3^\circ\mathrm{C}/100\,\mathrm{m}$. Lord Kelvin (unsuccessfully) used this to estimate the age of the Earth.
 
He assumed Earth is hot, solid and cooling. Thus we have the following conditions:
$$u(0,t) = u_0\ (\sim 0^\circ\mathrm{C}) \leftarrow \text{ice}$$
$$u_x(0,t) = 3\times10^{-4}\,^\circ\mathrm{C}/\mathrm{cm}$$
$$u(x,0) = \theta_0\ (\sim 1200^\circ\mathrm{C}) \leftarrow \text{melt point of iron}$$
This problem has the solution
$$u(x,t) = \theta_0\operatorname{erf}\Bigl(\frac{x}{\sqrt{4c^2t}}\Bigr)$$
$$u_x(x,t) = \cdots, \qquad u_x(0,t) = \theta_0/\sqrt{\pi c^2t}$$
$$t = \theta_0^2/\pi c^2(u_x(0,t))^2 \approx \frac{(1200)^2}{\pi c^2(3\times10^{-4})^2} \approx 27\times10^6 \text{ years}$$
Margin (with an arrow to the formula for $t$): "everything on RHS is known, $c$ for basalt is $\sim 6\times10^{-2}\,\mathrm{cm^2/sec}$".
[The solution formula takes $u_0 = 0$. The value $6\times10^{-2}\,\mathrm{cm^2/s}$ is $c^2$ (units of diffusivity), not $c$. possible error: with $c^2 = 6\times10^{-2}$ the formula gives about $2.7\times10^6$ years; $27\times10^6$ years needs $c^2 = 6\times10^{-3}$, which is the value CN-PDE p. 137 actually puts in its computation (while stating $6\times10^{-2}$ in the text). The inconsistency is in the source.]
 
**Right page.**
 
**N.** Recall the definition of a level surface of a scalar field $\varphi(x,y,z)$ as the surfaces on which $\varphi$ are constant. (In two dimensions, these are contour lines)
 
In three dimensions, $\nabla\varphi$ at some point is directed $\perp$ to the level surface through that point, in the direction of increasing $\varphi$. (In two dimensions, $\nabla\varphi$ is directed perpendicular to the contour line, direction of increasing $\varphi$)
 
**Def.** We define a harmonic function as follows:
A harmonic function is a twice cts. diff. function (scalar field) $f : U \to \R$ that satisfies the Laplace equation
$$\nabla^2u = \frac{\partial^2f}{\partial x^2} + \frac{\partial^2f}{\partial y^2} = 0$$
[possible error: mixes $u$ and $f$ ($\nabla^2f$ meant); the definition is stated in two variables.]
 
An important property of harmonic functions is that they come in <u>pairs</u>. Given a harmonic $u(x,y)$ on some region $U$, we can always find a harmonic $v(x,y)$ on $U$ such that
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad\text{and}\quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \qquad \Big\}\ \text{conjugate harmonics}$$
This is the Cauchy–Riemann condition.
[Stated without proof; "always" holds on simply connected regions — not stated in the notes.]
 
---
 
## HW 95 — Harmonic functions: finding conjugates; conjugate of the steady-state rectangle solution
_File `20261122_001123.jpg`. Both pages "Harmonic functions", section 7.7. Right page: text in the top third only._
 
**Left page.**
 
**Ex.** Take $u(x,y) = x^2 - y^2$. We can show $u(x,y)$ is a harmonic function. We must find a $v(x,y)$ satisfying the Cauchy–Riemann conditions.
$$v_y = u_x = 2x \Rightarrow v(x,y) = 2xy + F(x)$$
$$v_x = u_y = 2y + F'(x) \Rightarrow F(x) = c \in \R$$
Thus $v(x,y) = 2xy + c$.
[possible error: the second line should read $v_x = -u_y$; as written, $u_y = -2y$ and "$v_x = u_y = 2y + F'(x)$" is inconsistent. With $v_x = -u_y = 2y$ and $v_x = 2y + F'(x)$ we get $F' = 0$, as concluded. That $u$ is harmonic ($u_{xx} + u_{yy} = 2 - 2 = 0$) is asserted, not shown.]
 
**Ex.** We can show $u(x,y) = \sin\bigl(\frac{n\pi}{a}x\bigr)\sinh\bigl(\frac{n\pi}{a}y\bigr)$ is harmonic:
$$u_x = \tfrac{n\pi}{a}\cos\bigl(\tfrac{n\pi}{a}x\bigr)\sinh\bigl(\tfrac{n\pi}{a}y\bigr), \qquad u_y = \tfrac{n\pi}{a}\sin\bigl(\tfrac{n\pi}{a}x\bigr)\cosh\bigl(\tfrac{n\pi}{a}y\bigr)$$
$$u_{xx} = -\bigl(\tfrac{n\pi}{a}\bigr)^2\sin\bigl(\tfrac{n\pi}{a}x\bigr)\sinh\bigl(\tfrac{n\pi}{a}y\bigr), \qquad u_{yy} = \bigl(\tfrac{n\pi}{a}\bigr)^2\sin\bigl(\tfrac{n\pi}{a}x\bigr)\sinh\bigl(\tfrac{n\pi}{a}y\bigr)$$
and thus $u_{xx} + u_{yy} = 0$.
 
We now find $v_n(x,y)$ satisfying the C–R conditions.
$$v_y(x,y) = u_x = \tfrac{n\pi}{a}\cos\bigl(\tfrac{n\pi}{a}x\bigr)\sinh\bigl(\tfrac{n\pi}{a}y\bigr) \Rightarrow v(x,y) = \cos\bigl(\tfrac{n\pi}{a}x\bigr)\cosh\bigl(\tfrac{n\pi}{a}y\bigr) + F(x)$$
$$v_x(x,y) = -\tfrac{n\pi}{a}\sin\bigl(\tfrac{n\pi}{a}x\bigr)\cosh\bigl(\tfrac{n\pi}{a}y\bigr) + F'(x) \Rightarrow F'(x) = 0 \text{ so } F(x) = c$$
and so
$$v_n(x,y) = \cos\bigl(\tfrac{n\pi}{a}x\bigr)\cosh\bigl(\tfrac{n\pi}{a}y\bigr)$$
[The comparison $v_x = -u_y$ that gives $F' = 0$ is not written.]
 
**Right page.**
 
**Ex.** (continued) Thus, the harmonic function conjugate to the steady-state 2-D heat equation example (6.6) is
$$v(x,y) = \frac{8u_0}{\pi^2}\sum_{n=0}^\infty\frac{(-1)^m\cos\bigl(\frac{(2m+1)\pi x}{a}\bigr)\cosh\bigl(\frac{(2m+1)\pi y}{a}\bigr)}{(2m+1)^2\sinh\bigl(\frac{(2m+1)\pi b}{a}\bigr)}$$
(Recall the solution was
$$u(x,y) = \frac{8u_0}{\pi^2}\sum_{n=0}^\infty\frac{(-1)^n\sin\bigl(\frac{(2m+1)\pi x}{a}\bigr)\sinh\bigl(\frac{(2m+1)\pi y}{a}\bigr)}{(2m+1)^2\sinh\bigl(\frac{(2m+1)\pi b}{a}\bigr)}\ )$$
[possible error: the summation index is written $n$ but the terms use $m$ (and $(-1)^n$ in the second formula); $m$ throughout is meant. The $u$ series is HW 85's result with odd $n = 2m+1$, not written out there.]
 
---
 
## HW 96 — Harmonic functions: heat stream function; 2-D point source/sink
_File `20261122_001131.jpg`. Left page "Harmonic functions" (section 7.7), right page "2D Point source/sink" (section 7.8). Left page: text and figure in the top third only, the rest blank._
 
**Left page.**
 
**N.** If $u(x,y)$ is the temperature in the rectangle, then $v(x,y)$ is the heat stream function. Recall that the contour lines of $u$ are lines of 'constant temperature'. Then the contour lines of $v$ are lines of heat flow.
 
*Figure (contour lines of $u$ and $v$):* axes with a vertical axis at the left and a horizontal axis with an arrow to the right. In the first quadrant, three nested U-shaped curves (opening upwards, one above the other, the lowest the flattest), labelled "contour lines of $u$". Crossing them, two curves with arrowheads that fan out downwards (one going down-left, one down-right), plus short near-vertical strokes between, labelled "corresponding contour lines of $v$". The $v$-lines cross the $u$-lines at right angles. [Small and schematic; no values.]
 
**Right page.**
 
**N.** Consider the function
$$u(x,y) = A\ln(x^2 + y^2) = A\ln(r^2)$$
Also note that
$$\nabla f(r) = \frac{\partial f(r)}{\partial x}\vec\imath + \frac{\partial f(r)}{\partial y}\vec\jmath = f'(r)\frac{\partial r}{\partial x}\vec\imath + f'(r)\frac{\partial r}{\partial y}\vec\jmath = f'(r)\nabla r = f'(r)\frac{\vect r}{r}$$
$$\nabla^2f(r) = \nabla\cdot\nabla f = \nabla\cdot\Bigl(f'(r)\frac{\vect r}{r}\Bigr)$$
Thus
$$\nabla u(x,y) = \frac{2A}{r^2}\vect r \Rightarrow \frac{\partial u}{\partial x} = \frac{2A}{x^2+y^2}x,\quad \frac{\partial u}{\partial y} = \frac{2A}{x^2+y^2}y$$
$$\Rightarrow \frac{\partial^2u}{\partial x^2} = 2A\frac{y^2 - x^2}{(x^2+y^2)^2},\quad \frac{\partial^2u}{\partial y^2} = 2A\frac{x^2-y^2}{(x^2+y^2)^2}$$
and so $u$ satisfies $\nabla^2u = 0$.
[For $(x,y) \ne (0,0)$; not stated.]
The level/contour lines of $u$ are
$$2A\ln r = c \Rightarrow r = \text{some constant}$$
and so we can interpret $u(x,y)$ as the scalar field (e.g. temperature) produced by a point source/sink in 2D (depending on the sign of $A$)
 
---
 
## HW 97 — 2-D point source/sink (figures, general formula); point source next to an insulated wall
_File `20261122_001149.jpg`. Both pages "2D point source/sink", section 7.8. Lower third of the left page and lower fifth of the right page blank._
 
**Left page.**
 
**N.** [figures only, continuing HW 96]
 
*Figure 1 (contours of $u = A\ln r^2$):* axes crossing at the centre; two concentric circles (roughly circular, slightly lopsided) around the origin, plus a small circle at the origin. No labels.
 
*Figure 2 (heat flux):* axes crossing at the centre; four arrows pointing radially outwards along the axes (right, left, up, down) and four dotted radial lines with arrowheads along the diagonals, also pointing outwards. Label at the top right: "$\vect J = -k\nabla u$". Below right: a blacked-out word, then "$A < 0$ (source)".
[As drawn, the arrows point outward, i.e. heat flows away from the origin, which with $\vect J = -k\nabla u$ and $\nabla u = 2A\vect r/r^2$ requires $A < 0$: consistent with the label.]
 
**Rem.** Note that a point source/sink of strength $Q$ at $O$ in 2D is equivalent to a line source/sink in 3D.
 
**N.** In general, the temperature distribution due to a point source/sink of heat of unit strength at $(x_0, y_0)$ is
$$u(x,y) = \mp\frac{1}{4\pi k}\ln\bigl\{(x - x_0)^2 + (y - y_0)^2\bigr\}$$
The corresponding stream function is
$$v(x,y) = 2A\arctan\Bigl(\frac{y}{x}\Bigr) + c$$
[possible error: the stream function is written for $u = A\ln(x^2+y^2)$ at the origin (HW 96), not for the general $(x_0,y_0)$ formula just above it; for that, $v = \mp\frac{1}{2\pi k}\arctan\frac{y-y_0}{x-x_0}$ would correspond. Recorded as written; CN §7.8 should be checked. The sign convention "$\mp$" (source/sink) is not explained.]
 
**Right page.**
 
**Ex.** Consider a point source next to an insulated wall.
 
*Figure (source by insulated wall):* a vertical wall at the left (a vertical line with hatching on its left side and an arrow at the top, the $y$-axis); a horizontal arrow from the wall to the right (the $x$-axis); a small circle on the axis a short distance from the wall, labelled $A$ above. Text to the right: "insulated: $u_x(0,y) = 0$".
 
To solve this, we use an extension of the method of images. Consider now the problem:
 
*Figure (image problem):* horizontal and vertical axes crossing; two small circles on the horizontal axis, symmetric about the vertical axis, at $-a$ (left) and $a$ (right), each labelled $A$ above. Text to the right: "Note here we ignore the insulating wall."
 
As the Laplace equation is linear, and we can add solutions, the solution to the image problem is
$$u(x,y) = A\ln\{(x-a)^2 + y^2\} + A\ln\{(x+a)^2 + y^2\}$$
We claim this is the solution to the original problem, including the BC, on $0 < x < \infty$, $-\infty < y < \infty$.
We can also add $v$:
$$v(x,y) = 2A\arctan\Bigl(\frac{y}{x-a}\Bigr) + 2A\arctan\Bigl(\frac{y}{x+a}\Bigr) = 2A\arctan\Bigl(\frac{2xy}{x^2 - a^2 - y^2}\Bigr)$$
[Checked with $\arctan p + \arctan q = \arctan\frac{p+q}{1-pq}$: correct (modulo branch).]
 
---
 
## HW 98 — duplicate of HW 97
_File `20261122_001209.jpg`. The same two pages as HW 97 (2D point source/sink, section 7.8), photographed again from a slightly different angle. Content identical; nothing new. Not used further._
 
---
 
## HW 99 — Point source next to a zero-temperature wall; other applications of Laplace's equation: potential flow
_File `20261122_001227.jpg`. Left page "2D point source/sink" (section 7.8), right page "Other applications of Laplace's equation" (section 7.9). A broad shadow crosses the right page; readable._
 
**Left page.**
 
**Ex.** Consider a point source next to a zero-temperature wall
 
*Figure:* as in HW 97 (hatched vertical wall with an arrow up, horizontal axis arrow to the right, a small circle on the axis labelled $A$ below). Text to the right: a blacked-out word, then "$u(0,y) = 0$".
 
We similarly consider the image problem
 
*Figure (image problem):* axes crossing; small circles on the horizontal axis at the left, labelled "$-A$" below, and at the right, labelled "$A$" below (strengths $-A$ and $A$, at $x = -a$ and $x = a$; positions not labelled). Text to the right: "Note we similarly ignore the wall".
 
and in this case we obtain
$$u(x,y) = A\ln\{(x-a)^2 + y^2\} - A\ln\{(x+a)^2 + y^2\}$$
We can easily check that
- $\nabla^2u = 0$
- $u(0,y) = 0$
Also,
$$v(x,y) = 2A\arctan\Bigl(\frac{2ay}{x^2 - a^2 + y^2}\Bigr)$$
[Checked: $2A\arctan\frac{y}{x-a} - 2A\arctan\frac{y}{x+a} = 2A\arctan\frac{2ay}{x^2-a^2+y^2}$. Correct.]
 
**Right page.**
 
**N.** Recall that for an incompressible fluid with velocity field $\vect v(x,y,z,t)$, $\nabla\cdot\vect v = 0$. For steady flow we have $\vect v = \vect v(x,y,z)$ — i.e. steady flow is not time dependent.
 
If $\vect v(x,y,z)$ can be expressed as follows for a suitable scalar field $\varphi(x,y,z)$:
$$\vect v(x,y,z) = \nabla\varphi(x,y,z)$$
Then we have that
$$\nabla\times\vect v = \nabla\times(\nabla\varphi) = 0 \quad \leftarrow \operatorname{curl}\vect v = 0$$
Such a steady flow is curl-free/irrotational.
 
Therefore, if we have:
- an incompressible fluid $\nabla\cdot\vect v = 0$
- irrotational $\vect v = \nabla\varphi$
then we must have
$$0 = \nabla\cdot\vect v = \nabla\cdot\nabla\varphi = \frac{\partial^2\varphi}{\partial x^2} + \frac{\partial^2\varphi}{\partial y^2} + \frac{\partial^2\varphi}{\partial z^2}$$
and thus the scalar field $\varphi$ satisfies the 3D Laplace's equation. We call $\varphi(x,y,z)$ the velocity potential.
 
---
 
## HW 100 — Other applications of Laplace's equation: stream function, uniform flow, electrostatics
_File `20261122_001242.jpg`. Both pages "Other applications of Laplace's equation", section 7.9. Left page: text in the top half only. This is the last page of the notes._
 
**Left page.**
 
**N.** In 2D (no $z$-dependence) we thus have
$$\varphi_{xx} + \varphi_{yy} = 0$$
We know $\varphi(x,y)$ is harmonic, so there exists some scalar field $\psi(x,y)$ such that
$$\frac{\partial\varphi}{\partial x} = \frac{\partial\psi}{\partial y}, \qquad \frac{\partial\varphi}{\partial y} = -\frac{\partial\psi}{\partial x}$$
and
$$\nabla^2\psi(x,y) = 0$$
We also know that the contour lines of $\psi$ are the fluid lines of $\nabla\varphi$. These are the field lines of the velocity field $\vect v$ (i.e. the lines along which fluid is flowing). Thus $\psi$ is the velocity stream function.
 
**Right page.**
 
**Ex.** Consider the uniform field $\varphi(x,y) = Bx$
 
*Figure (uniform flow):* axes (vertical axis with arrow up, horizontal axis with arrow right). A grid: three vertical lines (one through the origin's left, two to the right), labelled at the top "$\varphi = c$"; four horizontal lines, labelled at the lower right "$\psi = c$". Small right-pointing arrowheads on three of the horizontal lines (the flow direction, along $\nabla\varphi$).
 
We can see $\nabla^2\varphi = 0$ and $\psi(x,y) = By$.
 
**N.** The variation of the electromagnetic field in free space (away from all charges) is governed by Maxwell's equations:
$$\nabla\cdot\vect E = 0,\quad \nabla\times\vect E = -\partial\vect B/\partial t,\quad \nabla\cdot\vect B = 0,\quad \nabla\times\vect B = \tfrac{1}{c^2}\partial\vect E/\partial t$$
where $\vect E$ is the electric field and $\vect B$ is the magnetic field. In static (no $t$-dependence) the equations decouple:
$$\nabla\cdot\vect E = 0,\quad \nabla\times\vect E = \vect 0,\quad \nabla\cdot\vect B = 0,\quad \nabla\times\vect B = \vect 0$$
As for irrotational, incompressible flow, we can introduce the electrostatic potential $\varphi(x,y,z)$ such that
$$\vect E = -\nabla\varphi(x,y,z)$$
so that $\nabla\times\vect E = 0$ as required. Then
$$\nabla\cdot\vect E = 0 \Rightarrow 0 = \nabla\cdot\nabla\varphi \Rightarrow \nabla^2\varphi = 0$$
and we obtain again Laplace's equation.
[The notes use the same letter $c$ for the speed of light here as for the wave speed and for contour constants.]
 
---
# MATH2100 Applied Mathematical Analysis: transcription, part 5 of 5 (typed notes)
 
_Transcription phase. Sources and conventions: see part 1 (`claude/notes-math2100-1.md`)._
 
## Typed notes: section and page index, figures, content found only here
 
Page numbers are the **printed** page numbers (CN-ODE: printed = PDF page; CN-PDE: printed = PDF page − 1). Both workbooks are lecture *workbooks*: many derivations and examples are left as empty boxes to be filled in during lectures, and those boxes are what the handwritten notes fill in. Several numbered "Figures" in CN-PDE are also empty frames (Figs 1, 2, 5, 7, 8, 16 and the space beside several examples); they are marked "(empty frame)" below. Only content that the handwritten notes lack is transcribed here.
 
### CN-ODE: MATH2010 *Analysis of Ordinary Differential Equations*, workbook (119 pp.)
 
| § | Title | pp. | HW |
|---|---|---|---|
| 1 | Introduction (ODEs vs PDEs; electrical circuit; systems vs Laplace; texts) | 4–8 | 02–04 |
| 2.1.1 | Introduction to systems of ODEs (Lotka–Volterra, mass–spring–damper, $n$th order → system) | 9–11 | 04–05 |
| 2.1.2 | Classifying ODEs: linear, order, homogeneous | 11–13 | 05–06 |
| 2.1.3 | The superposition principle | 13 | 06 |
| 2.2.1 | The system in matrix form | 13–14 | 07 |
| 2.2.2 | Homogeneous case with constant coefficients (eigenvalue method, real/equal/complex roots, Wronskian, summary box p. 22, complex eigenvalues pp. 24–27) | 14–27 | 07–10 |
| 2.3 | Theory and theorems for first-order systems (existence, uniqueness, counterexamples) | 28–29 | 11 |
| 2.4 | Homogeneous constant-coefficient 2-D systems and the phase plane; 2.4.1 phase portrait; 2.4.2 direction fields and nullclines; 2.4.3 real eigenvalues; 2.4.4 complex eigenvalues; 2.4.5 summary of the 6 types | 30–50 | 12–18 |
| 2.5 | Critical points (2.5.1) and stability (2.5.2), stability criteria, stability chart | 51–56 | 19–20 |
| 2.6 | Non-homogeneous linear systems | 57 | 21 |
| 2.7 | Nonlinear systems: 2.7.1 phase curves; 2.7.2 critical points; 2.7.3 linearisation (pendulum, Lotka–Volterra, damped pendulum, failure cases, competing species); 2.7.4 summary | 58–71 | 21–26 |
| 3.1 | Laplace transform: definition, simple functions, piecewise continuous, first shifting theorem, summary table (p. 79), inverting, Gamma function | 72–82 | 27–31 |
| 3.2 | Transforms of derivatives; solving linear ODEs; forcing and transfer functions; systems | 83–91 | 31–34 |
| 3.3 | Inverse transforms by partial fractions; the four cases; differentiating a transform | 92–100 | 35–39 |
| 3.4 | Second shifting theorem (3.4.1); **circuit examples (3.4.2)** | 101–109 | 39–40; **3.4.2 not in HW** |
| 3.5 | Convolution theorem; using it; solving linear ODEs by convolution (resonance); periodic functions | 110–117 | 41–44 |
| — | Summary of Laplace transforms; Table of Laplace transforms | 118–119 | — |
 
**Figures in CN-ODE** (redraw in TikZ/pgfplots; most are computer plots):
- **p. 5, series RLC circuit**: loop with inductor $L$ (coil, left side), resistor $R$ (top, current arrow $I(t)$), capacitor $C$ (right, charge $Q(t)$), source $E(t)$ (bottom). Same as HW 02.
- **p. 7, three panels for the LC example $Q = c_2\sin t$, $I = c_2\cos t$**: (a) 3-D plot "Helix": axes $t$ (0–20, to the right), $Q$ and $I$ (−1 to 1); the solution curve is a helix of radius 1 winding along the $t$-axis (about 3 turns). (b) "Work with $Q(t)$": $Q(t)$ against $t \in [0, 20]$, a sine wave of amplitude 1 (axis −1.5 to 1.5). (c) "or in $(Q, I)$ space": the unit circle in the $(Q, I)$ plane with an arrowhead (clockwise), labelled "Phase space" in red.
- **p. 8, switched-off voltage**: step $E(t) = E_0$ on $[0, k)$, 0 after; and a response sketch: a curve starting at $-2E_0/\omega^2$… oscillating as $-2E_0\cos(\omega t)/\omega^2$ with marks $\pi/\omega$, $2\pi/\omega$ ("Then for some circuits the result is oscillatory behaviour").
- **p. 10, mass–spring–damper**: block on a surface attached to a wall by a spring and a dashpot. Same as HW 04.
- **p. 30, four time-series panels**: "Exponential decay" $e^{-3t}$; "Exponential growth" $e^{2t}$; "Oscillation" $\sin(5t)$; "Decaying oscillation" $e^{-t}\cos(t)$; each on a dashed grid against $t$.
- **pp. 31–48, phase-portrait grids**: blank square grids with axes $y_1$, $y_2$ (to be drawn on in lectures); the drawn versions are in HW 12–18. Computer phase portraits on p. 37 (stable improper node, blue trajectories tangent to the slow eigenvector) and p. 42 (saddle).
- **pp. 44–45, summary**: small portraits for straight-line solutions, stable/unstable improper nodes, and a direction-field diagram showing the slope $\dd y_2/\dd y_1$ and the nullclines (horizontal where $\dot y_2 = 0$, vertical where $\dot y_1 = 0$).
- **pp. 49–50, summary of the six types** (2.4.5): small computer portraits for 1 saddle, 2 improper node, 3 proper node (star), 4 degenerate/inflected node, 5 spiral, 6 centre (nested ellipses), and 7 one zero eigenvalue (parallel straight-line trajectories, red line of critical points). Matches HW 13–18.
- **p. 52, stable vs unstable**: three small portraits (stable node with "nearby trajectories stay near", saddle, centre "a centre is also stable") and three blank grids.
- **p. 55, stability chart**: blank 2×2 frame (drawn version on p. 70 and in HW 20).
- **p. 59, nonlinear pendulum phase portrait** ("Phase Portrait for the Pendulum"): $y_1 = \theta \in [-2\pi, 2\pi]$ roughly, $y_2 = \dot\theta$; closed orbits (centres) around $(\pm2k\pi, 0)$, separatrices through the saddles at $(\pm\pi, 0)$, wavy open trajectories above and below (rotations).
- **p. 60, Lotka–Volterra** ("Lotka–Volterra Predator Prey Model"): nested closed contour curves around the critical point $(1, 2)$ (for $a = 2, b = 1, k = 1, \ell = 1$) in the first quadrant.
- **p. 63, pendulum near the critical points**: small copy of the pendulum portrait.
- **p. 66, damped pendulum**: spirals into the centres $(2k\pi, 0)$ (blue), three wells side by side.
- **p. 67, spiral**: a single trajectory spiralling into the origin.
- **p. 69, competing species**: blank axes for the sketch (drawn version in HW 25).
- **p. 70, stability chart (trace–determinant)**: horizontal axis Trace$(A)$, vertical Determinant$(A)$; parabola $\tr(A)^2 - 4\det(A) = 0$ (labelled "proper or inflected nodes"); regions: left inside parabola "stable focus", right inside "UNstable focus", vertical axis above 0 "Centers" (red), left below parabola "stable node", right below "UNstable node", lower half-plane "saddles" (yellow); arrow to the horizontal axis "One zero eigenvalue on $\det(A) = 0$".
- **p. 82, Gamma function**: small plot of $\Gamma(x)$ for $x > 0$ (decreasing from $+\infty$ near 0, minimum near 1.46, rising).
- **p. 101, shifted function**: $f(t)$ and $f(t-k)u(t-k)$ (same curve shifted right by $k$, zero before $k$).
- **p. 102, ramp/step pictures**: a ramp; a function $h(t)$ that is $t^2$ for $t < 1$ and 1 after (smooth rise then flat).
- **p. 104, piecewise function**: blank axes for $g(t) = 2$ ($0 \le t < \pi$), 0 ($\pi \le t < 2\pi$), $\sin t$ ($t \ge 2\pi$).
- **p. 105–109, circuit examples** (content not in HW, transcribed below): LC circuit diagram; switched pulse $E_0(1 - u(t-k))$ (rectangle of height $E_0$ on $[0, k)$); Dirac pulse: rectangle of height $1/k$ on $[a, a+k]$, "Area $= k \times 1/k = 1$"; impulse response: $Q(t) = 0$ before $a$, then a sine wave starting at $t = a$.
- **p. 111, convolution region**: two triangles in the $(\tau, t)$ plane showing the region of integration $0 \le \tau \le t$, swept by vertical strips (integrate $\tau$ first) and by horizontal strips (integrate $t$ first).
- **pp. 114–115, resonance**: a mass–spring picture labelled "Oscillating support"; and a plot of the response, an oscillation whose amplitude grows linearly with $t$ inside a straight-line envelope ("The amplitude of the resulting oscillations grows linearly with time"; resonance).
- **p. 117, square wave**: $f = 1$ on $[0, a)$, 0 on $[a, 2a)$, periodic (blue dashed). Same as HW 44.
**Content found only in CN-ODE**
1. **§3.4.2 Circuit examples (pp. 105–109).** LC circuit $L\ddot Q + R\dot Q + Q/C = E(t)$. Unforced, $R = 0$: purely oscillatory (centres); set $1/LC = \omega^2$, period $2\pi/\omega$; with $y = Q$, $\ddot y + \omega^2y = E(t)/L = \bar E(t)$; unforced solution $Y(s) = (sy(0) + \dot y(0))/(s^2 + \omega^2)$. *Switched pulse:* $Q(0) = \dot Q(0) = 0$, $\bar E(t) = \bar E_0$ for $0 \le t < k$, 0 for $t \ge k$, i.e. $\bar E_0(1 - u(t-k))$; $Y(s) = \bar E_0(1 - e^{-ks})/\bigl(s(s^2 + \omega^2)\bigr)$; partial fractions give $Q(t) = \frac{\bar E_0}{\omega^2}(1 - \cos\omega t)$ for $0 \le t < k$ and $\frac{\bar E_0}{\omega^2}(\cos\omega(t-k) - \cos\omega t)$ for $t \ge k$: "oscillations in charge result and are usually sustained"; take $k = \pi/\omega$; but if the EMF is turned off after $t = 2\pi/\omega$ (the box is empty: presumably no oscillation remains). *The Dirac delta function (a pulse of applied voltage):* impulse of strength $1/k$ on $[a, a+k]$: $\frac{u(t-a) - u(t-(a+k))}{k}$; its integral over any interval containing $[a, a+k]$ is 1; $\delta(t-a) = \lim_{k\to0}\frac{u(t-a) - u(t-(a+k))}{k} = \infty$ at $t = a$, 0 otherwise; $\int_0^\infty\delta(t-a)\dd t = 1$; $\mathcal L$ of the pulse $= e^{-sa}\frac{1 - e^{-ks}}{ks} \to e^{-sa}$ (L'Hôpital), so $\mathcal L(\delta(t-a)) = e^{-sa}$. For the LC circuit with zero ICs and $\bar E(t) = \bar E_0\delta(t-a)$: $Y(s) = \bar E_0e^{-as}/(s^2 + \omega^2)$, $Q(t) = \frac{\bar E_0}{\omega}\sin(\omega(t-a))u(t-a)$: "the impulse starts an oscillation going at $t = a$".
2. **Texts (p. 8):** Adkins & Davidson, *Ordinary Differential Equations*; Kreyszig, *Advanced Engineering Mathematics* (Ch. 4 and 6); Thompson, *Laplace Transforms*. (References only; not book content.)
3. **Software pointers (p. 33):** the UQ "mathsims" applets (General Linear Model, $a = 0, b = -3, c = 3, d = 0$ gives $\dot x = -3y$, $\dot y = 3x$, purely oscillatory) and *pplane* (type in the right-hand side, click "Graph Phase Plane", each click draws a trajectory forwards and backwards in time). No code.
4. **Summary and table of Laplace transforms (pp. 79, 118–119):** $1 \to 1/s$; $t^n \to n!/s^{n+1}$; $t^a \to \Gamma(a+1)/s^{a+1}$; $e^{at} \to 1/(s-a)$; $\cos\omega t \to s/(s^2+\omega^2)$; $\sin\omega t \to \omega/(s^2+\omega^2)$; $u(t-k) \to e^{-ks}/s$; $\delta(t-a) \to e^{-as}$; linearity; first shift $e^{at}f(t) \to F(s-a)$; second shift $f(t-k)u(t-k) \to e^{-ks}F(s)$; convolution $\int_0^tf(\tau)g(t-\tau)\dd\tau \to F(s)G(s)$; derivatives $f^{(n)} \to s^nF(s) - s^{n-1}f(0) - \dots - f^{(n-1)}(0)$; $tf(t) \to -F'(s)$; periodic $f$ (period $p$) $\to \frac{1}{1 - e^{-ps}}\int_0^pe^{-st}f(t)\dd t$. All entries appear separately in HW except $\delta$.
### CN-PDE: MATH2011 *and the PDE section of MATH2100/7100*, lecture workbook (155 pp.)
 
| § | Title | pp. | HW |
|---|---|---|---|
| 1 | Introduction to PDEs (definition; KdV, Klein–Gordon, Schrödinger, sine-Gordon, spherical harmonic equations; order, linear, homogeneous; Big Three; superposition; Fourier's method; assumed ODE knowledge) | 3–7 | 46–47 |
| 2 | Fourier series (periodic functions, Fourier analysis, orthogonality, coefficients, sawtooth, half-wave rectifier, convergence theorem) | 8–29 | 48–54 |
| 2.1 | Even and odd functions; cosine and sine series | 30–36 | 54–56 |
| 2.2 | Half-range expansions | 37–40 | 57–58 |
| 2.3 | Differentiating a Fourier series | 41–45 | 59–60 |
| 2.4 | Application: forced oscillations | 46–48 | 61–62 |
| 3, 3.1 | Vector calculus; the gradient operator (Del) | 49–52 | 63 |
| 3.2 | Level surfaces | 53–54 | 63 |
| 3.3 | Flux vector field | 55–56 | 64 |
| 3.4 | Gauss' divergence theorem | 57–59 | 64–65 |
| 3.5 | A conservation law (incompressible fluid; heat conduction) | 60–63 | 66–67 |
| 4.1–4.4 | The heat equation; Laplace's equation; the wave equation; summary | 64–68 | 67–69 |
| 5.1 | D'Alembert's solution | 69–71 | 69–70 |
| 5.2 | IVP for the infinite string (plucked, struck) | 72–75 | 70–71 |
| 5.3 | Properties of erf | 76–77 | 72 |
| 6.1 | Fourier's method for the wave equation (normal modes, plucked string) | 78–88 | 72–75 |
| 6.2 | Fourier's method for the 1-D heat equation | 89–95 | 76–77 |
| 6.3 | Inhomogeneous heat equation | 96–100 | 78–80 |
| 6.4 | Another approach | 101–102 | 80–81 |
| 6.5 | Stretched string with forcing (loading); effect of weight; plucked string | 103–107 | 81–82 |
| 6.6 | Steady-state problems: heat conduction in 2-D | 108–115 | 83–86 |
| 7.1 | 1-D heat equation on the whole $x$-axis | 116–117 | 86–88 |
| 7.2 | Properties of $G(x,t)$ | 118–125 | 87–89 |
| 7.3 | Method of images on the positive $x$-axis | 126–130 | 90–91 |
| 7.4 | Example: semi-infinite slab | 131–132 | 92 |
| 7.5 | Temperature waves in the Earth | 133–135 | 92–93 |
| 7.6 | Another model (Kelvin) | 136–137 | 94 |
| 7.7 | Harmonic functions | 138–141 | 94–96 |
| 7.8 | Point source/sink in 2-D | 142–149 | 96–99 |
| 7.9 | Other applications of Laplace's equation: 7.9.1 steady irrotational flow; 7.9.2 electrostatics | 150–154 | 99–100 |
 
**Figures in CN-PDE**
- **Fig. 1 (p. 8), Fig. 2 (p. 9):** "An example / another example of a periodic function": empty frames.
- **Fig. 3 (p. 10), Fourier analysis of a periodic function:** a sawtooth $f(x)$ (ramps of height 2 on $[0,1]$, repeating) equals the constant 1 plus the sine terms $-\frac{2}{\pi}\sin(2\pi x)$, $-\frac{1}{\pi}\sin(4\pi x)$, $-\frac{2}{3\pi}\sin(6\pi x)$, $-\frac{1}{2\pi}\sin(8\pi x)$, …, drawn as a column of small plots joined by "=" and "+".
- **Fig. 4 (p. 10), successive approximations:** six panels: the sawtooth; partial sums with 1, 2, 3, 4, 5 sine terms, each closer to the sawtooth (Gibbs-type overshoot at the jumps). Same as HW 48.
- **Figs 5, 7, 8 (pp. 20, 27, 28):** empty frames (convergence examples; drawn in HW 53–54).
- **Fig. 6 (p. 23), Fig. 9 (p. 29):** half sine-wave rectifier: $f = 0$ on $(-\pi, 0)$, $\sin x$ on $(0, \pi)$, period $2\pi$ (Fig. 6 caption only; Fig. 9 labelled "The half sine-wave rectifier"). Same as HW 52.
- **p. 46, forced oscillations:** mass on a spring and dashpot attached to a wall on the left; displacement $y(t)$ arrow to the right; forcing $r(t)$. Same as HW 61.
- **Fig. 10 (p. 49):** a shaded region $R$ in 3-D axes with a point $(x, y, z)$: "$\varphi(x,y,z)$ is defined everywhere in the shaded region $R$".
- **Fig. 11 (p. 50):** a surface in 3-D axes with unit normal vectors $\vect n(x,y,z)$ drawn at points (a vector field defined by the surface).
- **p. 53, level surface:** a closed surface $\varphi(x,y,z) = \varphi(x_0,y_0,z_0)$ through $P(x_0,y_0,z_0)$ with $\nabla\varphi$ drawn perpendicular to it at $P$. Same as HW 63.
- **Fig. 12 (p. 54):** radial fields $\vect J = \alpha\vect r_0$-type: left $\alpha > 0$ (arrows outward from a point), right $\alpha < 0$ (arrows inward), $\vect r_0 = x_0\vec\imath + y_0\vec\jmath + z_0\vec k$.
- **p. 55, flux through $\delta S$:** a small surface element with normal $\vect n$ and flux vector $\vect J$ at angle; origin $O$.
- **p. 57, small box:** rectangular box with corners $A$–$H$, sides $\delta x, \delta y, \delta z$, $\vect J$ arrows in and out. Same as HW 64.
- **Fig. 13 (p. 58):** a volume $V$ with surface $S$ divided into many small boxes (grid inside a blob).
- **p. 59, sphere example:** sphere of radius $a$ with radial arrows ($\vect n$ and $\vect J$ outward).
- **p. 60, volume and surface elements:** $\delta V$ at position $\vect r$ from $O$; surface element $\delta S$ with $\vect n$ and $\vect J$. Same as HW 66.
- **p. 64, iron bar:** bar from $x = 0$ to $x = L$, ends at $u = u_0$ and $u = u_1$, "insulated sides". Same as HW 67.
- **p. 64, Laplace region:** a 3-D region with prescribed temperature on its boundary $\partial R$.
- **p. 65, stretched string:** string between two fixed supports, displacement $u(x,t)$; small segment between $x$ and $x + \delta x$ with tensions $T$ at angles at each end. Same as HW 68.
- **Fig. 14 (p. 71):** a hump of fixed shape at $t = 0$ ($u = F(x)$) and the same hump translated to the left at $t > 0$ ($u = F(x + ct)$).
- **Fig. 15 (p. 77):** struck string: $B\,\mathrm{erf}(x + ct)$ (bottom left) and $-B\,\mathrm{erf}(x - ct)$ (bottom right) summing to a plateau that spreads (top).
- **Fig. 16 (p. 78):** "Suppose a string occupies $0 \le x \le L$": empty frame.
- **Fig. 17 (p. 86):** fundamental mode: top dashed $\sin(n\pi x/L)$ envelope, bottom dashed its negative, $n = 1$, $\nu_1 = c/2L$ (string shapes between the envelopes).
- **Fig. 18 (p. 86):** second mode: top-left and bottom-right dashed $\sin(2\pi x/L)$, bottom-left and top-right dashed $-\sin(2\pi x/L)$; $\nu_2 = 2\nu_1$ (node at $x = L/2$).
- **p. 89, rod with insulated sides:** cylinder along $x$ from 0 to $L$, "thermally insulated surface", heat flow along the axis. **p. 96:** same rod with a heat source $q$ inside.
- **p. 104, string under gravity:** string between supports at $x = 0$ and $x = L$, sagging, gravity arrow.
- **p. 108, beam (Example 6.6.1):** iron bar with $u = u_0$ and $u = u_1$ at the ends.
- **p. 109, long rectangular beam:** beam in perspective, $u = f(x)$ on top face, $u = 0$ on the other three faces; cross-section: rectangle $0 < x < a$, $0 < y < b$ with $u = f(x)$ on top, $u = 0$ on the other sides, $\nabla^2u = 0$ inside. Same as HW 83.
- **p. 112, Example 6.10.2 (triangular profile):** cross-section rectangle with $u = f(x)$ on top (tent function of height $u_0$ at $x = a/2$) and $u = 0$ elsewhere.
- **p. 115, Dirichlet BVP:** region $R$ with "$u$ prescribed on boundary", $u_{xx} + u_{yy} = 0$ inside ("called a Dirichlet BVP"); rectangle with $u = f(x)$ top, $u = h(y)$ right, $u = g(x)$ bottom, $u = k(y)$ left; and the four-rectangle decomposition $u = u^{(1)} + u^{(2)} + u^{(3)} + u^{(4)}$ ("soln of" each subproblem). Same as HW 86.
- **p. 116, infinitely long cylinder** with insulated sides (dashed ends at $\pm\infty$).
- **p. 126, odd extension:** blank (drawn in HW 90 only in words).
- **p. 129, insulated face and even extension:** cylinder with "insulated face" at $x = 0$; $u = F(x)$ on $x > 0$ and its even reflection ("unphysical" for $x < 0$, "physical" for $x > 0$).
- **p. 131, semi-infinite slab:** hatched insulated face at $x = 0$, $u(x,t)$ for $x > 0$.
- **p. 133, temperature waves:** ground surface (dashed line), $x$ pointing down, "$u = u_0\cos(\omega t)$" at the surface. Same as HW 92.
- **p. 136, Kelvin model:** ground surface with $x$ down, "$u(0,t) = u_0 \sim 0^\circ$C" at the surface and "$u(x, 0) = \theta_0$" below; and a sketch of the initial profile (constant $\theta_0$, dropping to 0 at $x = 0$) → later profile (erf shape).
- **p. 141, contour lines:** "contour lines of $u$ (constant temperature)" and "corresponding contour lines of $v$" crossing at right angles. Same as HW 96.
- **p. 142, point source:** 3-D axes with the line $z$ through the origin, the plane, "$u$ depends only on $r = \sqrt{x^2+y^2}$".
- **p. 143, flux from a point source/sink:** circles (contours of $u$) around the origin; radial arrows $\vect J = -k\nabla u$ outward for $A < 0$ (source) and inward for $A > 0$ (sink). Same as HW 97.
- **p. 144, cylinder of radius $a$, unit height** around the $z$-axis, unit normal $\vect n = \vect r/r$ (line-source argument).
- **p. 145, point source at $(x_0, y_0)$:** axes, point $(x_0,y_0)$ with radial arrows.
- **p. 146:** point $(x,y)$ in polar coordinates $r, \theta$; circles and radial lines ("lines of heat flow").
- **p. 147, insulated wall (Example 6.12.1):** hatched wall $x = 0$, "point source" at $(a, 0)$, "insulated: $u_x(0,y) = 0$ – BC", $\nabla^2u = 0$; image problem: sources at $(\pm a, 0)$, "unphysical region" $x < 0$. Same as HW 97.
- **p. 148, zero-temperature wall (Example 6.12.2):** wall $u = 0$, source $A$ at $(a,0)$; image: $-A$ at $(-a, 0)$. Same as HW 99.
- **p. 149, more elaborate image problems:** left: quarter plane $x > 0$, $y > 0$ bounded by two hatched walls, the wall on the $y$-axis labelled "$u = 0$", the wall on the $x$-axis labelled "$u_x = 0$" [possible error: on $y = 0$ an insulated wall would be $u_y = 0$], a source at $(a, b)$; an arrow to the right panel: plain axes with the point $(a, b)$ only (the image sources are not drawn). No solution is given (content not in HW).
- **p. 152, uniform field (Example 6.13.1.1):** grid of lines $\varphi = $ const (vertical) and $\psi = $ const (horizontal) with flow arrows to the right. Same as HW 100.
- **p. 152, point source in 2-D (Example 6.13.1.2):** radial lines $\psi = $ const and circles $\varphi = $ const around a source; and a source near a wall solved by images (sketch).
- **p. 153, impenetrable wall:** wall with normal $\vect n$ and velocity $\vect v$ tangent to it.
- **p. 154, point charge (Example 6.13.2.1):** $\varphi = A\ln(x^2+y^2)$, "equipotential curves" (circles) and radial field lines of $\vect E$; two small panels "$A < 0$ (positive charge)" (arrows out) and "$A > 0$ (negative charge)" (arrows in); "The conjugate harmonic function now gives the field lines of $\vect E$".
**Content found only in CN-PDE**
1. **Thermal diffusion (p. 132, §7.4):** conduction of heat is sometimes called thermal diffusion, since the same PDE governs molecular diffusion: $u \to c(x,t)$ (concentration of diffusate), $c^2 \to D$ (coefficient of diffusion), $c_t = Dc_{xx}$ (1-D diffusion equation). Typical $D \sim 10^{-5}\,\mathrm{cm^2/s}$; over length scales $\sim 5$ cm, diffusion times $\sim 25/10^{-5}$ s $\sim 30$ days; over $\sim 10^{-4}$ cm, $\sim 10^{-8}/10^{-5}$ s $\sim 10^{-3}$ s: "very important transfer process for cells".
2. **Penetration depth numbers (p. 135, §7.5):** typical soil $c^2 \sim 2\times10^{-3}\,\mathrm{cm^2/s}$. Yearly: $\omega \sim 2\pi/(365\cdot24\cdot3600)\,\mathrm{s^{-1}}$; at $x \sim 1$ m, $\sqrt{\omega/2c^2}\,x \sim 0.7 \sim \pi/4$ and $e^{-\sqrt{\omega/2c^2}x} \sim 1/2$: a $\pi/4$ phase lag and attenuation by $1/2$ at 1 m; $\pi$ lag and $1/16$ at 4 m ("winter 4 metres down when summer at the surface … usefulness of a deep cellar"). Daily: $\omega$ multiplied by 365, $\sqrt{365} \approx 19$, so the same effects occur at depth $x/19$: amplitude $1/16$ and "reversal of time of day" at about $400/19 \sim 21$ cm: daily variations affect only the topsoil.
3. **Kelvin's conclusion (p. 137):** "Allowing for uncertainties in the data, Kelvin concluded that age of Earth $\le 400\times10^6$ years." Also the assumptions "chemically inert" and the "flat Earth" approximation (p. 136). [CN's arithmetic uses $c^2 = 6\times10^{-3}$ although the text says $6\times10^{-2}$; see HW 94.]
4. **Line-source argument for the strength of a point source (pp. 144–145):** a point source/sink of strength $Q$ at $O$ in 2-D equals a line source in 3-D of line density $Q$ along the $z$-axis; the heat flowing out through a cylinder of radius $a$ and unit height, with $\vect n = \vect r/r$, fixes the constant: $u = -\frac{1}{2\pi k}\ln r$ is the temperature due to a point source of unit strength at $O$, and $u = +\frac{1}{2\pi k}\ln r$ that of a unit sink. More generally $u = \mp\frac{1}{4\pi k}\ln\{(x-x_0)^2 + (y-y_0)^2\}$ at $(x_0, y_0)$, with $\nabla^2u = 0$ for $(x,y) \ne (x_0,y_0)$. In polar coordinates the contour lines of $v$ are radial lines, perpendicular to the circles $u = $ const: the lines of heat flow (p. 146). [The HW has the formula but not the derivation of $1/(2\pi k)$.]
5. **More elaborate image problems (p. 149):** "We may similarly consider more elaborate image problems" with the quarter-plane figure only (see figures).
6. **Impenetrable wall (p. 153):** at an impenetrable wall $\vect v\cdot\vect n = 0$; since $\vect J = \rho_0\vect v$ is the mass-flux vector, there is no flux of mass across the wall. Steady flow: if a steady flow is irrotational, $\vect v = \nabla\varphi$; we may also have $\nabla\cdot\vect v = 0$ (solenoidal).
7. **Point source of fluid and point charge in 2-D (pp. 152, 154):** the same methods (including images) apply to flow from a point source; for a point charge at the origin $\varphi = A\ln(x^2+y^2)$, the equipotentials are circles and the conjugate harmonic function gives the field lines of $\vect E$; $A < 0$ positive charge, $A > 0$ negative charge.
8. **Introduction (p. 4):** PDEs in finance and economics; third-order PDEs for waves in dispersive media (water waves, plasma), fourth-order PDEs in beam mechanics and image processing. (Context only.)
9. **Convergence theorem reference (p. 26):** "Theorem 1 (K pp. 486)" (Kreyszig) for the Fourier convergence theorem; Example 1.4.1 (K pp. 500) for forced oscillations. References only.
