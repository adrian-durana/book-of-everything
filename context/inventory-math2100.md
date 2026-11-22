# Coverage inventory: MATH2100 Applied Mathematical Analysis (MATH2010 ODEs + MATH2011 PDEs)

_Built from the 100 photos of the handwritten notebook (main source) and the two lecture workbooks (supplement), all from the semester the course was taken (Semester 2, 2025). Transcription: `claude/notes-math2100-1.md` to `-5.md`._

**Sources.** "HW nn" means photo nn (a two-page spread, in shooting order; HW 01 and HW 45 are single contents pages; HW 98 duplicates HW 97 and is not used). "CN-ODE §x (p. n)" means the MATH2010 workbook, printed page = PDF page. "CN-PDE §x (p. n)" means the MATH2011 workbook, printed page = PDF page − 1. The workbooks leave most derivations as empty boxes that the handwritten notes fill in, so HW is the reference wherever both exist. Items marked **CN only** appear only in the workbooks (transcribed in part 5).

**Code:** none in the notes. Part II uses Python; computer-drawn plots in the workbooks (phase portraits and so on) are redrawn in pgfplots, with data from Python if needed.

**Status:** ◻ to do (nothing drafted yet). **↔ merge (X)** marks an item that overlaps another course or a chapter already written; merge it into that material rather than adding a second copy. **Sections** are proposed headings within each chapter (`tools/chapters.py` lists chapters only); rename them as other courses are merged in.

---

## Ch 17 Vector Calculus (`ch:vector-calculus`), Part I
### §17.a Scalar and vector fields; grad, div, curl ↔ merge (MATH1072, MATH2001)
- ◻ Def. scalar field, vector field; fields that also depend on $t$ (HW 63, CN-PDE §3 p. 49, Fig. 10)
- ◻ Def. gradient (del) operator, divergence, curl (determinant form) (HW 63, CN-PDE §3.1 pp. 49–52, Fig. 11)
- ◻ Def. Laplacian $\nabla^2$ (HW 64; see errors list, 30)
- ◻ Interpretation: divergence = net outflow, curl = rotation of flow; figure of $\nabla f$, $\nabla\cdot f$, $\nabla\times f$ at a point on a level surface (HW 63)
### §17.b Level surfaces ↔ merge (MATH1072, MATH2001; Ch 15 gradient)
- ◻ Def. level surface; $\nabla f$ is normal to the level surface, its direction is the direction of greatest increase and its magnitude the greatest rate (HW 63, HW 94 right page, CN-PDE §3.2 pp. 53–54, figure p. 53)
- ◻ Fig. 12: radial fields $\alpha\vect r$ for $\alpha > 0$ and $\alpha < 0$ (CN-PDE p. 54) **CN only**
### §17.c Flux and the divergence theorem ↔ merge (MATH2001)
- ◻ Def. flux vector field $\vect J$; flux across $\delta S$; total flux $\iint_S \vect J\cdot\vect n \dd S$; mass flux $\rho\vect v$ example (HW 64, CN-PDE §3.3 pp. 55–56, figure p. 55)
- ◻ Gauss' divergence theorem: small-box argument (faces $ABCD$/$EFGH$ etc., Taylor expansion of $\vect J$, total flux $= (\nabla\cdot\vect J)\,\delta V$), then "many tiny boxes" limit (HW 64–65, CN-PDE §3.4 pp. 57–58, box figure p. 57, Fig. 13). Not a rigorous proof; say so
- ◻ Ex. $\vect J = \alpha\vect r$ over the sphere of radius $a$: both sides equal $4\pi\alpha a^3$ (HW 65, CN-PDE p. 59 figure)

## Ch 18 First-Order Ordinary Differential Equations (`ch:first-order-odes`)
### §18.a What an ODE is; classification ↔ merge (MATH1072)
- ◻ Def. ODE (one independent variable); mass–spring–damper example (HW 02, CN-ODE §1 p. 4)
- ◻ Classification tree: ordinary/partial, linear/non-linear, homogeneous/non-homogeneous; Def. linear, order, homogeneous (via $cy$ is a solution); examples with $L[y]$ (HW 05–06, CN-ODE §2.1.2 pp. 11–13)
- ◻ Revision: linear first-order ODE by integrating factor $e^{\int p}$ (HW 06) ↔ merge (MATH1072)
### §18.b Existence and uniqueness (for first-order systems) ↔ merge (MATH1072)
- ◻ IVP $\dot{\vect y} = \vect f(t, \vect y)$, $\vect y(t_0) = \vect K$; existence (continuous $f_i$) and uniqueness (continuous $\partial f_i/\partial y_j$) on some $(t_0 - \alpha, t_0 + \alpha)$; stated without proof (HW 11, CN-ODE §2.3 pp. 28–29)
- ◻ Counterexamples: $\dot y = y^2$ blows up; $\dot y = 2y/t$ ($f$ discontinuous at $t = 0$); $\dot y = \sqrt y$, $y(0) = 0$ has solutions $t^2/4$ and $0$ (HW 11)
- (Placement: see hub question 2.)

## Ch 19 Linear Higher-Order ODEs (`ch:linear-higher-order-odes`)
- ◻ Superposition principle for linear homogeneous ODEs and systems (HW 06, CN-ODE §2.1.3 p. 13) ↔ merge (MATH1072, MATH2001)
- ◻ Constant-coefficient second-order equations: trial $e^{\lambda t}$, auxiliary equation, the cases (distinct real, repeated, complex $\alpha \pm i\beta$, purely imaginary) (HW 06, 07, 47; CN-PDE §1 p. 7) ↔ merge (MATH1072, MATH2001). HW 47 is the same list again (in $x$), recalled for separation of variables: use once
- ◻ LC circuit $\ddot Q + Q = 0$: $\lambda = \pm i$, real form $A\cos t + B\sin t$, IVP $Q(0) = 0$ (HW 03, CN-ODE §1 p. 7): motivating example, shared with Ch 20/22
- ◻ Method of undetermined coefficients with a Fourier-series forcing: see Ch 23 §23.e

## Ch 20 Linear Systems of ODEs (`ch:linear-systems-odes`)
### §20.a Systems of first-order ODEs
- ◻ Motivation: epidemic model, series RLC circuit (figure) and Kirchhoff's law (HW 02, CN-ODE §1 p. 5); Lotka–Volterra and mass–spring–damper as first-order systems (HW 04, CN-ODE §2.1.1 pp. 9–10, figure p. 10). One or two of these only (STYLE: one motivating example)
- ◻ Converting an $n$th-order ODE into $n$ first-order equations; example $\ddot y + \dot y - 2y = 0$ (HW 05, CN-ODE §2.1.1 p. 11)
- ◻ Second-order linear ODE as $\dot{\vect y} = \mat A(t)\vect y + \vect R(t)$; homogeneous vs inhomogeneous systems (HW 07, CN-ODE §2.2.1 pp. 13–14)
- ◻ Circuit in matrix form (HW 03)
### §20.b Constant coefficients: the eigenvalue method
- ◻ Trial $\vect y = \vect x e^{\lambda t}$ gives $\mat A\vect x = \lambda\vect x$; general solution for distinct eigenvalues (HW 08, CN-ODE §2.2.2 pp. 14–17) ↔ merge (Ch 7, eigenvalues: MATH1071, MATH2001)
- ◻ Ex. $\ddot y + 2\dot y - 15y = 0$ as a system: $\lambda = 3, -5$ (HW 08)
- ◻ Fundamental matrix; Wronskian; nonzero Wronskian ⟹ linear independence (HW 09, CN-ODE §2.2.2) ↔ merge (MATH1072 if it has the Wronskian)
- ◻ Summary box for $2\times 2$ systems; IVP example $\ddot y - 3\dot y - 4y = 0$, $y(0) = 4$, $\dot y(0) = 6$ (HW 09, CN-ODE p. 22)
### §20.c Complex eigenvalues
- ◻ Conjugate eigenvalues give conjugate eigenvectors; real solution from the real and imaginary parts of one complex solution, with $c_2 = \bar c_1$; example $\ddot y + 4y = 0$ (HW 10, CN-ODE pp. 24–27)
### §20.d Systems by Laplace transform: see Ch 21 §21.d (HW 34)

## Ch 21 The Laplace Transform (`ch:laplace-transform`)
### §21.a Definition and basic transforms
- ◻ Motivation: circuit with a switched-off voltage $E(t)$ (HW 04, CN-ODE §1 p. 8 figures: step and response)
- ◻ Def. $\mathcal L(f)(s) = \int_0^\infty f(t)e^{-st}\dd t$ (HW 27, CN-ODE §3.1 p. 72)
- ◻ Transforms of $c$, $t^n$ (induction by parts), $e^{at}$, with proofs (HW 27)
- ◻ Linearity; $\cos\alpha t$, $\sin\alpha t$ via $e^{i\alpha t}$ (HW 28)
- ◻ Piecewise-continuous functions: unit step $u(t-k)$, steps down, up-and-down, the three-level example (HW 28, CN-ODE pp. 75–77)
- ◻ $\mathcal L(t^\alpha) = \Gamma(\alpha+1)/s^{\alpha+1}$; $\Gamma(n+1) = n!$, $\Gamma(x+1) = x\Gamma(x)$ recalled from STAT2003; $\mathcal L(\sqrt t)$ (HW 31, CN-ODE p. 82 with Gamma plot) ↔ merge (Ch 29, Gamma function: STAT2003, written) — cite, don't redefine
- ◻ Well-definedness: exponential order $\abs{f(t)} \le Me^{\gamma t}$; $e^{t^2}$ has no transform (HW 31)
- ◻ Summary table (CN-ODE p. 79; full table pp. 118–119) → one table at the end of the chapter **CN only** (all entries in HW except $\delta$)
### §21.b Shifting theorems
- ◻ First shifting theorem $\mathcal L(e^{at}f) = F(s-a)$; four standard shifted transforms; example $5e^{3t}\cos 2t + 4t^3e^{-5t}$ (HW 29, CN-ODE §3.1)
- ◻ Second shifting theorem $\mathcal L(f(t-k)u(t-k)) = e^{-ks}F(s)$, with proof (HW 39, CN-ODE §3.4.1 p. 101, figure of shifted $f$)
- ◻ Examples: $\mathcal L^{-1}(e^{-ks}/s^2)$, $\mathcal L^{-1}((1-e^{-s})^2/s^2)$; forward direction for $h(t) = 2$ then $0$, and $t^2$ then $1$ (HW 40, CN-ODE p. 102 figures; p. 104 piecewise $g$ figure)
### §21.c Inversion and partial fractions
- ◻ Inverse of shifted powers and of $(bs+c)/(s^2+\alpha^2)$; three examples (HW 30, CN-ODE §3.1)
- ◻ Partial fractions overview and examples (HW 30, 35, CN-ODE §3.3 pp. 92–93)
- ◻ Case 1 simple linear factors; Case 2 repeated linear factors; Case 3 irreducible quadratics (completing the square); Case 4 repeated irreducible quadratics; one example each (HW 36–39, CN-ODE §3.3.1–3.3.4 pp. 94–100)
- ◻ Differentiating a transform: $\mathcal L(-tf(t)) = F'(s)$ (proof by differentiating under the integral); checks with $t^4$; inverse transforms of $s/(s^2+\alpha^2)^2$, $s^2/(\cdot)^2$, $\alpha^2/(\cdot)^2$ (HW 38, CN-ODE p. 98) ↔ link (Ch 12/15: differentiating under the integral sign)
### §21.d Solving ODEs and systems
- ◻ Transforms of $\dot f$, $\ddot f$, $f^{(n)}$, with proofs (HW 32, CN-ODE §3.2 pp. 83–85)
- ◻ Examples $\dot y + 2y = 2e^{-2t}$ and $\ddot y + 2\dot y + y = e^{-t}$ (HW 32)
- ◻ Forcing (input) function and transfer function $Q(s) = 1/(as^2+bs+c)$; $Y = QR + Q(\ldots)$ (HW 33, CN-ODE pp. 87–89)
- ◻ Systems: $\dot{\vect y} = \begin{psmallmatrix}3&1\\0&3\end{psmallmatrix}\vect y + e^{-2t}\begin{psmallmatrix}1\\1\end{psmallmatrix}$ (HW 34, CN-ODE pp. 90–91)
### §21.e Convolution
- ◻ $\mathcal L$ is not multiplicative; Def. convolution $f*g$; convolution theorem with proof (change of order of integration; CN-ODE p. 111 figure of the triangular region); commutativity (HW 41, CN-ODE §3.5 pp. 110–111) ↔ link (Ch 16 change of order; Ch 32 convolution of densities, STAT2003)
- ◻ Examples $\mathcal L^{-1}(2s/(s^2+1)^2) = t\sin t$ and $\mathcal L^{-1}(1/((s-2)^2(s+1)))$; combining with the second shift (HW 42, CN-ODE p. 112)
- ◻ Solving $\ddot y + a\dot y + by = r(t)$ with zero ICs as $y = q*r$; resonance $\ddot x + 9x = \cos 3t$ gives $\frac16 t\sin 3t$ (HW 43, CN-ODE pp. 113–115; figures: oscillating support, linearly growing amplitude)
### §21.f Periodic functions
- ◻ $\mathcal L(f) = \frac{1}{1-e^{-ps}}\int_0^p f e^{-st}\dd t$, with proof (geometric series) (HW 44, CN-ODE p. 116)
- ◻ Square wave (figure) $F = 1/(s(1+e^{-as}))$ (HW 44, CN-ODE p. 117)
### §21.g Circuit examples and the Dirac delta **CN only**
- ◻ LC circuit $\ddot y + \omega^2 y = \bar E(t)$; switched pulse $\bar E_0(1 - u(t-k))$ and its solution (CN-ODE §3.4.2 pp. 105–107, figures)
- ◻ Def. Dirac delta as the limit of pulses of area 1; $\mathcal L(\delta(t-a)) = e^{-as}$ (L'Hôpital); impulse response $Q(t) = \frac{\bar E_0}{\omega}\sin(\omega(t-a))u(t-a)$ (CN-ODE pp. 107–109, figures) ↔ link (Ch 24: $\delta$ as $\lim_{t\to0^+}G$, HW 87)

## Ch 22 Stability and Phase-Plane Analysis (`ch:stability-phase-plane`)
### §22.a The phase plane ↔ merge (MATH1072)
- ◻ Expected behaviours (decay, growth, oscillation, growing/decaying oscillation; CN-ODE p. 30 four plots); phase space $(y_1, y_2)$; LC circuit: circles in $(Q, I)$, helix in $(t, Q, I)$ (HW 03, 12, CN-ODE p. 7 three panels)
- ◻ Linear pendulum: ellipses $y_1^2 + \frac19 y_2^2 = c^2$ (HW 12)
- ◻ Def. trajectory, phase portrait; time arrow; trajectories cannot cross (uniqueness); trivial trajectory (HW 12, CN-ODE §2.4.1 pp. 31–33)
- ◻ Def. velocity vector, direction field, slope $\dd y_2/\dd y_1 = f_2/f_1$, nullclines (HW 13, CN-ODE §2.4.2 pp. 34–36, 44–45)
### §22.b Phase portraits of linear systems (six types)
- ◻ Summary list of the six types (HW 13, CN-ODE §2.4.5 pp. 49–50, seven small portraits)
- ◻ Real distinct eigenvalues: straight-line solutions; stable improper node, example $\begin{psmallmatrix}-2&0\\1&-1\end{psmallmatrix}$, five straight trajectories and full portrait (HW 14, CN-ODE §2.4.3 p. 37)
- ◻ Unstable improper node, example $\begin{psmallmatrix}1&3\\0&2\end{psmallmatrix}$ (HW 15)
- ◻ Saddle, example $\diag(2,-4)$, $y_2 \propto y_1^{-2}$ (HW 15, CN-ODE p. 42)
- ◻ Proper node (star), $\mat A = \mat I$ (HW 16)
- ◻ Degenerate (inflected) node, example $\begin{psmallmatrix}0&1\\-1&2\end{psmallmatrix}$ (HW 16)
- ◻ Zero eigenvalue: line of critical points, example $\begin{psmallmatrix}3&2\\3&2\end{psmallmatrix}$ (HW 16–17)
- ◻ Centre: ellipses, example $\begin{psmallmatrix}0&1\\-2&0\end{psmallmatrix}$, direction of flow (HW 17, CN-ODE §2.4.4)
- ◻ Spirals: example $\begin{psmallmatrix}2&-1\\1&2\end{psmallmatrix}$ in polar form ($r = e^{2t}$, $\dot\theta = 1$); nullclines and slopes as a sketching guide (HW 18, CN-ODE pp. 46–48)
### §22.c Critical points and stability
- ◻ Def. critical point; nonlinear systems can have several (example) (HW 19, CN-ODE §2.5.1 p. 51)
- ◻ Stable vs unstable; pendulum at rest/inverted (HW 19, CN-ODE §2.5.2 p. 52, three portraits)
- ◻ Characteristic polynomial $\lambda^2 - \tr\mat A\,\lambda + \det\mat A$; stability criteria by $\det$, $\tr$ and discriminant; three examples; trace–determinant stability chart (HW 19–20, CN-ODE pp. 53–56, chart p. 70) — use the CN p. 70 chart as the model figure
- ◻ Non-homogeneous systems $\dot{\vect y} = \mat A\vect y + \vect g$: critical point $-\mat A^{-1}\vect g$, translation to a homogeneous system (HW 21, CN-ODE §2.6 p. 57) (could sit in Ch 20 instead)
### §22.d Nonlinear systems
- ◻ Solving for phase curves: nonlinear pendulum $y_2 = \pm\sqrt{\ldots}$, CN-ODE p. 59 portrait; predator–prey ("see MATH1072"; CN-ODE p. 60 contours) (HW 21, CN-ODE §2.7.1) ↔ merge (MATH1072)
- ◻ Critical points of the pendulum and Lotka–Volterra (HW 22, CN-ODE §2.7.2)
- ◻ Linearisation by Taylor series; Jacobian (HW 22, CN-ODE §2.7.3) ↔ link (Ch 15, Jacobian and Taylor's theorem)
- ◻ Examples: pendulum (saddle at $(\pi, 0)$), Lotka–Volterra (saddle, centre), damped pendulum (spiral/node and saddles; CN-ODE pp. 63, 66–67 figures) (HW 23–24)
- ◻ When linearisation fails: $\det\mat A = 0$, or a centre; example that slowly spirals out (HW 24)
- ◻ Competing species $\dot x = x - xy$, $\dot y = 4y - xy$: unstable node and saddle, heteroclinic trajectory, full portrait (HW 25, CN-ODE p. 69)
- ◻ Summary procedure for nonlinear systems (HW 26, CN-ODE §2.7.4 p. 71)

## Ch 23 Fourier Series (`ch:fourier-series`)
### §23.a Periodic functions and Fourier series
- ◻ Periodic functions; expansion in $\cos(2n\pi x/p)$, $\sin(2n\pi x/p)$; sawtooth $f = 2x$ on $(0,1)$ with its series and partial-sum panels (HW 48, CN-PDE §2 pp. 8–10, Figs 3–4)
- ◻ Def. Fourier series with $p = 2L$; Fourier coefficients (HW 49, CN-PDE pp. 11–13)
### §23.b Orthogonality and the coefficients ↔ merge (Ch 8, inner products: MATH2001)
- ◻ Orthogonality of $\{1, \cos(n\pi x/L), \sin(n\pi x/L)\}$ under $\int_{-L}^L f_1f_2$, with proof (product-to-sum identities) (HW 49–50, CN-PDE pp. 14–18); remark: also orthogonal over any period (proof left to an assignment)
- ◻ Coefficient formulas; proof for $a_0$ (the $a_m$, $b_m$ proofs are only in the workbook, W7L2: CN-PDE pp. 18–21) (HW 51)
- ◻ Sawtooth worked: $1 - \frac2\pi\sum \sin(2n\pi x)/n$ (HW 51)
- ◻ Half sine-wave rectifier (figure; CN-PDE Figs 6, 9) (HW 52, CN-PDE pp. 22–24)
- ◻ Summary box, including the general interval $[a, a+2L]$ (HW 52)
### §23.c Convergence
- ◻ Def. piecewise continuous on $[-L, L]$ (figure); $f(a^\pm)$ (HW 53) ↔ merge (Ch 10, one-sided limits: MATH2401)
- ◻ Convergence theorem: the series converges to $\frac12(f(x^+) + f(x^-))$ where one-sided derivatives exist. Stated without proof (HW 53, CN-PDE p. 26, Theorem 1)
- ◻ Examples: sawtooth at the jumps; rectifier everywhere; resulting series for $\sin x$ on $(-\pi, 0)$ (HW 54, CN-PDE pp. 27–29)
### §23.d Even and odd functions; half-range expansions
- ◻ Def. even, odd; four properties (HW 54, CN-PDE §2.1 pp. 30–31)
- ◻ Fourier cosine series (even) and sine series (odd) (HW 55, CN-PDE pp. 32–33)
- ◻ Examples $\abs x$ (cosine series) and $x$ on $(-1, 1)$ (sine series), triangle and sawtooth figures; any $g$ = even + odd part (HW 56, CN-PDE pp. 34–36)
- ◻ Half-range cosine and sine series via even/odd periodic extensions (HW 57, CN-PDE §2.2 pp. 37–38)
- ◻ Example $f(x) = x$ on $[0,1]$ by both methods (HW 58, CN-PDE pp. 39–40)
### §23.e Differentiation and an application
- ◻ $f'$ is periodic; $A_0 = 0$, $A_n = \frac{n\pi}{L}b_n$, $B_n = -\frac{n\pi}{L}a_n$: term-by-term differentiation (HW 59, CN-PDE §2.3 pp. 41–43) ↔ link (Ch 13, term-by-term differentiation: MATH2401)
- ◻ Derivative of an even function is odd and vice versa; triangle-wave example and check (HW 60, CN-PDE pp. 44–45)
- ◻ Forced oscillations $\ddot y + \frac1{50}\dot y + 25y = r(t)$ with the triangle wave: homogeneous solution, undetermined coefficients with a Fourier series, equating coefficients ($b_5 = 8/(5\pi)$ dominates) (HW 61–62, CN-PDE §2.4 pp. 46–48, mass–spring figure) ↔ link (Ch 19)

## Ch 24 Partial Differential Equations (`ch:pdes`)
(Large chapter: see hub question 1.)
### §24.a Introduction
- ◻ Def. PDE; examples KdV, Klein–Gordon, Schrödinger, sine-Gordon, spherical harmonic equation; order, linear, homogeneous (HW 46, CN-PDE §1 pp. 3–5)
- ◻ The "big three": 1-D wave, 1-D heat, 2-D Laplace equations and their uses (HW 46, CN-PDE p. 5)
- ◻ Superposition principle for linear homogeneous PDEs; Fourier's method = Fourier series + separation of variables (HW 47, CN-PDE p. 6) ↔ merge (MATH2001, if it covers separation of variables)
### §24.b Derivations: conservation laws and the big three
- ◻ Conservation law $\partial\rho/\partial t + \nabla\cdot\vect J = 0$ from the divergence theorem (figures: $\delta V$, $\delta S$ with $\vect n$ and $\vect J$) (HW 66, CN-PDE §3.5 pp. 60–61)
- ◻ Incompressible fluid: $\nabla\cdot\vect v = 0$ (HW 66, CN-PDE p. 62)
- ◻ Heat conduction: $\vect J = -K\nabla u$, heat equation $u_t = c^2\nabla^2 u$, $c^2 = K/(\rho\sigma)$; 1-D heat equation; iron bar with end temperatures (HW 67, CN-PDE §4.1 pp. 63–64)
- ◻ Laplace's equation as the steady state (3-D region figure CN-PDE p. 64) (HW 68, CN-PDE §4.2)
- ◻ Wave equation for a stretched string (two figures), $c^2 = T/\rho$ (HW 68–69, CN-PDE §4.3 pp. 65–67); summary (CN-PDE §4.4 p. 68)
- ◻ **CN only:** thermal diffusion and the diffusion equation $c_t = Dc_{xx}$ with diffusion-time estimates (CN-PDE §7.4 p. 132)
### §24.c The wave equation on the line: d'Alembert
- ◻ Characteristic variables $v = x + ct$, $w = x - ct$; $u_{vw} = 0$; general solution $F(x+ct) + G(x-ct)$; travelling-wave figure (HW 69–70, CN-PDE §5.1 pp. 69–71, Fig. 14)
- ◻ IVP on the infinite string; d'Alembert's formula, with derivation (HW 70–71, CN-PDE §5.2 pp. 72–73)
- ◻ Plucked string (two triangular pulses, figure); struck string with $u_t(x,0) = Ae^{-x^2}$ in terms of erf (figure; CN-PDE Fig. 15) (HW 71, CN-PDE pp. 74–75)
- ◻ Def. error function; odd; increasing; plot (HW 72, CN-PDE §5.3 pp. 76–77) ↔ link (Ch 29 normal distribution; the notes do not make the link)
### §24.d Fourier's method on a bounded interval
- ◻ Wave equation on $[0, L]$ with fixed ends: separation, the three cases for $k$, eigenfunctions $\sin(n\pi x/L)$, $G$-system, superposition, coefficients from half-range sine series (HW 72–74, CN-PDE §6.1 pp. 78–84, Fig. 16)
- ◻ Normal modes, angular frequency, frequency, period; fundamental mode and first overtone (figure; CN-PDE Figs 17–18) (HW 74–75, CN-PDE pp. 85–86)
- ◻ Plucked string on $[0, L]$: triangular initial shape (figure), $A_n$, solution (HW 75, CN-PDE pp. 87–88)
- ◻ Heat equation with insulated ends $u_x(0,t) = u_x(L,t) = 0$ (bar figure): three cases, cosine eigenfunctions, solution, coefficients from half-range cosine series (HW 76–77, CN-PDE §6.2 pp. 89–93)
- ◻ Triangular initial temperature example (figure); $u \to A_0$ and conservation of heat energy (HW 77, CN-PDE pp. 94–95)
### §24.e Inhomogeneous problems
- ◻ Heat equation with a source $q(x,t)$: expand $q$ in a sine series, ODE $B_n' + (n\pi c/L)^2 B_n = Q_n$, ICs (HW 78–79, CN-PDE §6.3 pp. 96–98, rod figure p. 96)
- ◻ Example: constant source $q_0$ and initial temperature $u_0$; steady-state and transient parts (HW 79–80, CN-PDE pp. 99–100)
- ◻ Another approach for a time-independent source: steady state $u^s(x) = -\frac{q_0x}{2c^2}(x-L)$ plus a homogeneous problem for $\hat u = u - u^s$ (HW 80–81, CN-PDE §6.4 pp. 101–102)
- ◻ Forced (loaded) string $u_{tt} - c^2u_{xx} = F(x,t)$: same method, second-order ODE for $B_n$ (HW 81, CN-PDE §6.5 p. 103)
- ◻ String under gravity: steady state $\frac{g}{2c^2}x(x-L)$, catenary comparison, weight ≪ tension; displacement = equilibrium + free vibration (HW 82, CN-PDE pp. 104–106, figure p. 104)
- ◻ Plucked string under gravity: HW only points to CN-PDE p. 107; take from there **CN only**
### §24.f Laplace's equation in a rectangle
- ◻ Steady state: Laplace's equation; 1-D case and the iron bar $u = u_0 + (u_1 - u_0)x/L$ (HW 83, CN-PDE §6.6 p. 108, figure)
- ◻ Rectangular beam: BVP with $u = f(x)$ on top, $0$ elsewhere (figure; CN-PDE p. 109): separation, cases, $\sin(n\pi x/a)\sinh(n\pi y/a)$, coefficients (HW 83–85, CN-PDE pp. 109–111)
- ◻ Triangular profile example: the tempting guess $\frac yb f(x)$ fails; $B_n = \frac{8u_0\sin(n\pi/2)}{(n\pi)^2\sinh(n\pi b/a)}$ (HW 85, CN-PDE pp. 112–114, figure p. 112)
- ◻ Smoothness and maximum property (stated); general Dirichlet problem on a rectangle as a sum of four problems (figures) (HW 86, CN-PDE p. 115)
### §24.g The heat equation on infinite and semi-infinite domains
- ◻ Fundamental solution $G(x,t)$ and its properties; Gaussian at each $t$ (figure); Dirac delta as $t \to 0^+$; heat injected at a point; translation (HW 86–87, CN-PDE §7.1–7.2 pp. 116–121, cylinder figure p. 116) ↔ link (Ch 29 normal density; Ch 21 §21.g delta)
- ◻ Solution $u = \int G(x-y,t)f(y)\dd y$ as a convolution; proof sketch (HW 87–88, CN-PDE pp. 122–123)
- ◻ Examples: step initial data → erf (HW 88); odd step pulse, $u(0,t) = 0$, read as a half-line problem (HW 89) (CN-PDE pp. 124–125); Gaussian integral $\int_0^\infty e^{-x^2} = \sqrt\pi/2$ used ↔ link (Ch 29)
- ◻ Method of images: odd extension for $u(0,t) = 0$; non-zero boundary value by subtracting $u_0$; even extension for an insulated end $u_x(0,t) = 0$ (figure) (HW 90–91, CN-PDE §7.3 pp. 126–130, figures pp. 126, 129)
- ◻ Insulated semi-infinite slab (figures), solution quoted from the problem sheet (HW 92, CN-PDE §7.4 p. 131)
- ◻ Temperature waves in the Earth: complex BC, $X'' = (i\omega/c^2)X$, attenuated wave $u_0 e^{-\sqrt{\omega/2c^2}x}\cos(\omega t - \sqrt{\omega/2c^2}x)$; remarks on phase lag and penetration (soil figure) (HW 92–93, CN-PDE §7.5 pp. 133–134)
- ◻ **CN only:** penetration-depth numbers, yearly vs daily, "deep cellar" (CN-PDE p. 135)
- ◻ Kelvin's Earth-age model: $u = \theta_0\operatorname{erf}(x/\sqrt{4c^2t})$, $t = \theta_0^2/(\pi c^2u_x(0,t)^2)$ (HW 94, CN-PDE §7.6 pp. 136–137, figures p. 136); **CN only:** his conclusion "age ≤ 400 × 10⁶ years" and the assumptions. See errors list, 46
### §24.h Harmonic functions and potential theory
- ◻ Def. harmonic function; conjugate pairs via the Cauchy–Riemann equations (stated) (HW 94, CN-PDE §7.7 pp. 138–139)
- ◻ Examples: $x^2 - y^2$ and $2xy$; conjugate of $\sin(n\pi x/a)\sinh(n\pi y/a)$; conjugate of the rectangle solution (HW 95, CN-PDE p. 140)
- ◻ Heat stream function: contour lines of $v$ are lines of heat flow (figure) (HW 96, CN-PDE p. 141)
- ◻ Point source/sink in 2-D: $u = A\ln(x^2+y^2)$ is harmonic away from 0; $\nabla f(r) = f'(r)\vect r/r$; contours and flux figures; equivalent to a line source in 3-D; general formula at $(x_0, y_0)$; stream function (HW 96–97, CN-PDE §7.8 pp. 142–146)
- ◻ **CN only:** line-source argument fixing the constant $1/(2\pi k)$ (CN-PDE pp. 144–145, cylinder figure)
- ◻ Images in 2-D: source by an insulated wall (sources $A$, $A$ at $\pm a$); source by a zero-temperature wall ($A$, $-A$); with stream functions (HW 97, 99, CN-PDE pp. 147–148, figures)
- ◻ **CN only:** quarter-plane image problem, figure only (CN-PDE p. 149)
- ◻ Steady irrotational incompressible flow: velocity potential, Laplace's equation, stream function; uniform flow example (grid figure) (HW 99–100, CN-PDE §7.9.1 pp. 150–152)
- ◻ **CN only:** point source of fluid (figure p. 152); impenetrable wall $\vect v\cdot\vect n = 0$ (figure p. 153)
- ◻ Electrostatics: Maxwell's equations, static case, $\vect E = -\nabla\varphi$, Laplace's equation (HW 100, CN-PDE §7.9.2 pp. 153–154); **CN only:** point charge $\varphi = A\ln(x^2+y^2)$, equipotentials and field lines (figure p. 154)

## Not used
- Contents pages HW 01, HW 45 (structure only). HW 98 (duplicate of HW 97).
- CN-ODE p. 8: textbook list (Adkins & Davidson; Kreyszig; Thompson). CN-ODE p. 33: "mathsims" applets and *pplane* (software pointers, no code).
- CN-PDE p. 4: PDEs in finance, dispersive media, beams (context only). CN-PDE references to Kreyszig page numbers.
- Problem sheets and assignments are cited (HW 49, 92) but not supplied.

---

## Overlaps with other courses and written chapters
| Topic | MATH2100 source | Overlaps | Action |
|---|---|---|---|
| Classifying ODEs; integrating factor; constant-coefficient 2nd-order ODEs; superposition | HW 05–07, 47 | MATH1072, MATH2001 (Ch 18–19) | ↔ merge |
| Existence and uniqueness | HW 11 | MATH1072 (Ch 18) | ↔ merge |
| Phase plane, predator–prey phase curves, stability | HW 12–26 | MATH1072 (Ch 22; HW 21 says "see MATH1072") | ↔ merge |
| Eigenvalues and eigenvectors | HW 08–10 | MATH1071, MATH2001 (Ch 7) | cite |
| Jacobian, Taylor linearisation | HW 22–23 | MATH2401, MATH1072 (Ch 15) | cite |
| Gamma function | HW 31 | STAT2003, **Ch 29 (written)** | ↔ merge: cite Ch 29, don't redefine |
| Convolution | HW 41, 87 | STAT2003 Ch 32 (convolution of densities, not yet written) | link in the linking pass |
| Gaussian integral, fundamental solution = normal density, erf | HW 72, 86–88 | STAT2003 **Ch 29 (written)** | link in the linking pass (not in the notes) |
| Inner product, orthogonality | HW 49–50 | MATH2001 (Ch 8) | cite |
| Piecewise continuity, one-sided limits; term-by-term differentiation; differentiating under the integral | HW 38, 53, 59, 87 | MATH2401/2400 (Ch 10, 12, 13) | cite |
| Change of order of integration | HW 41 | MATH2001 (Ch 16) | cite |
| grad, div, curl, level surfaces, flux, divergence theorem | HW 63–65 | MATH1072, MATH2001 (Ch 17) | ↔ merge |
| Separation of variables for PDEs | HW 72–85 | MATH2001 (Ch 24, per `chapters.py`) | ↔ merge |

No item overlaps Chapters 25–28, 30 or 31.

---

## Suspected errors in the notes
Numbered for reference; nothing has been corrected in the transcription. "HW" = handwritten notes.
1. HW 03: the amplitude is called $B$, then $c_2$.
2. HW 06: $L[cy] = (c-1)t^5$, not $-t^5$ (the non-homogeneity argument still works for $c \ne 1$).
3. HW 07: $\ddot y = -q y - p\dot y + r$; the line before the system has $-r$.
4. HW 08: "two unique eigenvectors $\lambda_1, \lambda_2$" should be "two distinct eigenvalues".
5. HW 17: when $y_2 > 0$ it is $y_1$ (not $y_2$) that increases.
6. HW 19: the third critical point of $(y_1 - y_2^2, y_2 - y_1y_2)$ is $(1, -1)$, not $(-1, -1)$.
7. HW 19: a linear system has only the origin as critical point only if $\det\mat A \ne 0$ (HW 16–17 show a line of critical points).
8. HW 20: $\begin{psmallmatrix}2&3\\2&5\end{psmallmatrix}$ has $\Delta > 0$: an unstable *improper* node, not proper.
9. HW 21: pendulum phase curves $y_2 = \pm\sqrt{\frac{2g}{\ell}\cos y_1 + C}$ (factor 2 missing).
10. HW 22: "$f(y_1^*, y_2^*)$" should be $f_1$; $\bar y_i = y_i - y_i^*$ is not defined.
11. HW 23: general Jacobian indices miswritten; $\tr J_f(0,0) = 1$, not $-2$; $\dot{\bar y}_1$ written for $\dot{\bar y}_2$.
12. HW 25: says $\tr\mat A \ne 0$ at the saddle $(4,1)$, where $\tr\mat A = 0$ (the conclusion holds since it is a saddle).
13. HW 27: $\mathcal L(t^n) = n!/s^{n+1}$ needs $n \ge 0$, not $n \in \Z$ (also HW 31).
14. HW 31: $\mathcal L(t^{3.1}) = \Gamma(4.1)/s^{4.1}$, not $\Gamma(4.2)/s^{4.2}$.
15. HW 31: "cannot grow faster than $e^{-st}$" should be an exponential $e^{\gamma t}$ (the next line is right).
16. HW 33: in $Y(s)$ the last term is $b\,y(0)$, not $b\,\dot y(0)$.
17. HW 34: middle line denominator $(s-2)(s+3)$ should be $(s+2)(s-3)$; the coefficient of $e^{3t}$ in $y_1$ is $4/25$, not $1/6$.
18. HW 36: Case 1 example denominator should be $(s-1)(s-2)(s+3)$, and then $A_3 = +1$ (so $+e^{-3t}$); Case 2 general formula: the $A_3$ term has $e^{a_1t}$; Case 2 example: last term $1/(s-1)$ and $e^{t}$.
19. HW 37: Case 3 inverse should be $Ae^{at}\cos\alpha t + \frac{B}{\alpha}e^{at}\sin\alpha t$.
20. HW 43: $Q(s) = 1/(s^2+9)$, not $3/(3s^2+9)$; $R(t)$ should be $R(s)$ (the working uses the right $q$).
21. HW 46: sine-Gordon has $+\sin u$ in CN-PDE §1.
22. HW 50: $\sin\alpha\sin\beta$ expansion has $-\cos(\alpha+\beta)$; the integral is 0 either way.
23. HW 52: even-$n$ rectifier coefficient is $a_n = -\frac{2}{\pi(n^2-1)}$; the bracket as written doesn't give the stated $a_2$.
24. HW 54: $\int_{-a}^a f = 2\int_0^a f$ for even $f$ (upper limit written $2a$).
25. HW 56: denominator $(2m+1)^2\pi^2$ (exponent written $n$).
26. HW 57: odd extension condition $f_2(-x) = -f_2(x)$.
27. HW 58: cosine argument $(2k+1)\pi x$ ($\pi$ missing); $b_n = \frac{2(-1)^{n+1}}{n\pi}$ (sign).
28. HW 62: $a_{2k+1}$ constants: $\frac{25-(2k+1)^2}{2500(25-(2k+1)^2)^2 + (2k+1)^2}\cdot\frac{10\,000}{(2k+1)^2\pi}$.
29. HW 64: total flux written with $\dd\vect S$ and $\vect n$ together; should be $\dd S$.
30. HW 64: the Laplacian is written with unit vectors; it is the scalar operator $\partial_{xx} + \partial_{yy} + \partial_{zz}$.
31. HW 69: $c^2 = T/\rho$, not $c = T/\rho$.
32. HW 71: struck-string figure dips below the axis; the solution is positive for all $x$ when $t > 0$.
33. HW 75: second-mode envelope labelled $\pm\sin(\pi x/L)$, should be $\pm\sin(2\pi x/L)$; the plucked-string solution lacks the factor $\sin(n\pi x/L)$.
34. HW 76: $e^{2\mu L}$, not $e^{2\mu x}$.
35. HW 77: the IC series should start at $n = 0$; $A_n$ denominator is $n^2\pi^2$ (partly blacked out); the triangle example's solution lacks $e^{-(n\pi c/L)^2t}$; total heat energy should be $\int_0^L\rho\sigma u\dd x$.
36. HW 78–79: several exponents $-(n\pi c/L)^2$ lack the factor $t$.
37. HW 80: $q$ should be $q_0$; the steady-state check sums over all $n$ where only odd $n$ contribute.
38. HW 82: "$\sinh\theta \approx 0$" should be $\approx \theta$; $g$ is both gravity and the initial velocity; "force string" presumably "free string".
39. HW 83: $\alpha = (u_1 - u_0)/L$ (brackets missing).
40. HW 85: intermediate step has $\sin(n\pi/a)$ for $\sin(n\pi/2)$ and a wrong coefficient; the final $B_n$ is correct.
41. HW 87: "For the BC" should be "for the IC"; heat localised at $x = 0$, not $t = 0$.
42. HW 89: lower limit $-x/\sqrt{4c^2t}$ should be $x/\sqrt{4c^2t}$; "$x \pm a/\sqrt{\cdot}$" means $(x \pm a)/\sqrt{\cdot}$.
43. HW 90: the reflected integral loses its factor $F(y)$; $\hat u(x,0) = F(x) - u_0$.
44. HW 91: insulated-face figure says $u(0,t) = 0$ (should be $u_x(0,t) = 0$); $F(y)$ for $f(y)$ in the first integral; denominator $2c^3t$ should be $2c^2t$.
45. HW 94: harmonic-function definition mixes $u$ and $f$; "always" a conjugate needs a simply connected region (not stated; flag only).
46. HW 94 and CN-PDE p. 137: Kelvin estimate. The stated diffusivity $6\times10^{-2}$ cm²/s gives about $2.7\times10^6$ years; the quoted $27\times10^6$ years needs $6\times10^{-3}$ (the value CN actually uses). The value is $c^2$, not $c$.
47. HW 95: $v_x = -u_y$ (sign); summation index $n$ where terms use $m$.
48. HW 97: the stream function $2A\arctan(y/x)$ belongs to $A\ln(x^2+y^2)$ at the origin, not to the general $(x_0, y_0)$ formula above it.
49. CN-PDE p. 149: on the wall $y = 0$ an insulated condition is $u_y = 0$, not $u_x = 0$.

Ambiguities (handwriting, not errors): HW 10 sign in the conjugate solution; HW 34 "3"/"5" (read as 3); HW 86 left boundary label "$h$"/"$k$" (read as $k$). Each is resolved in the transcription.

## Notation the book doesn't have yet
| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\Laplace`, `\invLaplace` | $\mathcal{L}$, $\mathcal{L}^{-1}$ | Laplace transform and inverse | Used throughout Ch 21. Check against any likelihood notation planned for Part IV (likelihood is often $L$ or $\mathcal L$) |
| `\heav{t-k}` | $u(t-k)$ | unit (Heaviside) step | The notes use $u$, which clashes with the PDE unknown $u(x,t)$ in Ch 24; a macro lets the hub switch to $H(t-k)$ later in one line |
| `\erf` (`\DeclareMathOperator`) | $\operatorname{erf}$ | error function | Ch 24 (d'Alembert, heat equation on the line, Kelvin) |
| `\Real`, `\Imag` (`\DeclareMathOperator`) | $\operatorname{Re}$, $\operatorname{Im}$ | real and imaginary parts | LaTeX's `\Re`/`\Im` are fraktur; used in Ch 20–22 (complex eigenvalues, stability) |
| `\grad`, `\divg`, `\curl` | $\nabla$, $\nabla\cdot$, $\nabla\times$ (the notes also write "div", "curl") | vector operators | One convention for Ch 17 and Ch 24; MATH1072/MATH2001 will use them too |
| `\lap` | $\nabla^2$ | Laplacian | Fixes $\nabla^2$ rather than $\Delta$ ($\Delta$ is the discriminant in Ch 22) |
| `\oiint` (package `esint`) | $\oiint$ | closed surface integral | Divergence theorem and conservation law (HW 65–66) |
| `\ihat`, `\jhat`, `\khat` | $\vect i$, $\vect j$, $\vect k$ (bold, to match `\vect`) | standard unit vectors | The notes write $\vec\imath$, $\vec\jmath$, $\vec k$ |
| `\conv` (optional) | $f * g$ | convolution | Shared by Ch 21, Ch 24 and Ch 32 (STAT2003); only if the hub wants one symbol fixed |

Existing macros cover the rest: `\vect`, `\mat`, `\tr`, `\diag`, `\dd`, `\inner` (function inner product, HW 49), `\abs`, `\norm`, `\R`, `\C`, `\Z`, `\N` (the notes' $n \in \N$ in $pL = n\pi$ matches $\N = \{1, 2, \ldots\}$). The Gamma function uses $\Gamma$ as in Ch 29. Partial derivatives appear both as $\partial u/\partial t$ and as subscripts $u_t$, $u_{xx}$; no macro proposed, but the hub may want to fix one style per chapter.

## Code in the notes
None. The workbooks contain computer-drawn plots (phase portraits, the pendulum and Lotka–Volterra contours, the damped pendulum, the Gamma function, partial sums of Fourier series, the resonance envelope); these are redrawn in pgfplots, with data generated in Python where needed. CN-ODE p. 33 points to the "mathsims" applets and *pplane* (no code).
