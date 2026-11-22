# MATH1071 / MATH2400 / MATH2401 — transcription, part 3: MATH2400 handwritten notes (HW2400 052–102)

_Continues `claude/notes-math1071-2.md`. Conventions: see the header of `claude/notes-math1071-1.md`._

---

## HW2400 052 · `20261121_230742.jpg` · Partition refinements

**Def.** A partition $P'$ is a refinement of $P$ if $P \subset P'$.

**Def.** [a theorem] If $P \subset P'$, then $L(f, P) \le L(f, P')$ and $U(f, P) \ge U(f, P')$.

**P.** We consider when $P'$ differs from $P$ only once. If $P'$ differs from $P$ $m$ times, repeat the below argument $m$ times.
Let $P = \{x_0, x_1, \dots, x_n\}$, $P' = \{x_0, x_1, \dots, x_{j-1}, r, x_j, \dots, x_n\}$. Then,
$$L(f, P) = \sum_{i=1}^{n} \inf_{x \in [x_{i-1}, x_i]} f(x)(x_i - x_{i-1}) = \sum_{i=1, i \ne j}^{n} \inf_{x \in [x_{i-1}, x_i]} f(x)(x_i - x_{i-1}) + \inf_{x \in [x_{j-1}, x_j]} f(x)$$
[possible error: the last term is missing the factor $(x_j - x_{j-1})$]
Note that:
$$\inf_{x \in [x_{j-1}, x_j]} f(x) \le \inf_{x \in [x_{j-1}, r]} f(x) \quad\text{and}\quad \inf_{x \in [x_{j-1}, x_j]} f(x) \le \inf_{x \in [r, x_j]} f(x).$$
Thus,
$$L(f, P) \le \sum_{i=1, i \ne j}^{n} \inf_{x \in [x_{i-1}, x_i]} f(x)(x_i - x_{i-1}) + \inf_{x \in [x_{j-1}, r]} f(x)(r - x_{j-1}) + \inf_{x \in [r, x_j]} f(x)(x_j - r) = L(f, P').$$
Similarly, $U(f, P) \ge U(f, P')$.

## HW2400 053 · `20261121_230747.jpg` · Darbour integrals [sic: Darboux]

**Def.** We define the lower Darboux integral of $f$ by:
$$\mathbb{L} = \underline{\int_a^b} f(x) \dd x = \sup\{L(f, P) : P \text{ is partition of } [a, b]\}$$
$$\mathbb{U} = \overline{\int_a^b} f(x) \dd x = \inf\{U(f, P) : P \text{ is partition of } [a, b]\}$$
(the upper integral is defined on the second line without a label; the shorthand letters are written as blackboard-bold $\mathbb{L}$, $\mathbb{U}$.)

**Def.** [a theorem] If $P_1$, $P_2$ are partitions of $[a, b]$, then $L(f, P_1) \le U(f, P_2)$.

**P.** Define $P = P_1 \cup P_2$. Thus, $L(f, P_1) \le L(f, P) \le U(f, P) \le U(f, P_2)$.

**Def.** [a theorem] The lower integral of $f$ is less than or equal to the higher integral of $f$.

**P.** Suppose for contradiction that $\mathbb{L} > \mathbb{U}$. Fix $\varepsilon = \frac{\mathbb{L} - \mathbb{U}}{2} > 0$. Then, there exist partitions $P_1$, $P_2$:
$$L(f, P_1) > \mathbb{L} - \varepsilon = \frac{\mathbb{L} + \mathbb{U}}{2} = \mathbb{U} + \varepsilon > U(f, P_2)$$
which is a contradiction.

## HW2400 054 · `20261121_230751.jpg` · Integrability

**Def.** The function $f$ is integrable if $\underline{\int_a^b} f(x) \dd x = \overline{\int_a^b} f(x) \dd x$. We denote $\int_a^b f(x) \dd x = \underline{\int_a^b} f(x) \dd x = \overline{\int_a^b} f(x) \dd x$.

**Ex.** Consider $f : [0, 1] \to \R$, $f(x) = c$. Show $f$ is integrable.

**P.** Note that for all $x \in [0, 1]$, $c \le f(x) \le c$. Take any partition $P$. Then,
$$c(1 - 0) \le L(f, P) \le \underline{\int_a^b} f \le \overline{\int_a^b} f \le U(f, P) \le c(1 - 0)$$
Thus $f$ is integrable and $\int_a^b f = c$.

## HW2400 055 · `20261121_230757(0).jpg` · Integrability (cont.)

**Def.** [a theorem] The function $f : [a, b] \to \R$ is integrable iff for all $\varepsilon > 0$, there exists some partition $P$ such that $U(f, P) - L(f, P) < \varepsilon$.

**P.** We first prove in the forward direction. Let $f$ be integrable. Fix $\varepsilon > 0$. There exists some partition $P_1$ such that:
$$\int_a^b f(x) \dd x = \underline{\int_a^b} f(x) \dd x < L(f, P_1) + \frac{\varepsilon}{2} \implies L(f, P_1) > \int_a^b f(x) \dd x - \frac{\varepsilon}{2}$$
There exist some partition $P_2$ such that:
$$\int_a^b f(x) \dd x = \overline{\int_a^b} f(x) \dd x > U(f, P_2) + \frac{\varepsilon}{2} \implies U(f, P_2) < \int_a^b f(x) \dd x + \frac{\varepsilon}{2}$$
[possible error: the first line should read "$> U(f, P_2) - \frac{\varepsilon}{2}$"; the implied line is right]
Let $P = P_1 \cup P_2$. Then,
$$U(f, P) - L(f, P) \le U(f, P_2) - L(f, P_1) < \int_a^b f(x) \dd x + \frac{\varepsilon}{2} - \int_a^b f(x) \dd x + \frac{\varepsilon}{2} = \varepsilon.$$
For the reverse direction, fix $\varepsilon > 0$. Then there exists $P$ such that $U(f, P) - L(f, P) < \varepsilon$. Then,
$$\overline{\int_a^b} f(x) \dd x - \underline{\int_a^b} f(x) \dd x \le U(f, P) - L(f, P) < \varepsilon.$$
so $f$ is integrable. (subscripts on $P$ in the last line are blotted out.)
(same theorem as MATH1071 HW 52.)

## HW2400 056 · `20261121_230810.jpg` · Integrability examples

**Ex.** Consider $f : [0, 1] \to \R$ such that: $f = \begin{cases} 1 & x \in \Q\\ 0 & x \in \R \setminus \Q\end{cases}$. Show $f$ is not integrable.

**P.** Let $P$ be a partition of $[0, 1]$. Then $\forall i$ in $1 \le i \le n$,
$$m_i = \inf\{f(x) : x_{i-1} \le x \le x_i\} = 0,\qquad M_i = \sup\{f(x) : x_{i-1} \le x \le x_i\} = 1$$
Thus,
$$L(f, P) = \sum_{i=1}^{n} m_i(x_i - x_{i-1}) = 0,\qquad U(f, P) = \sum_{i=1}^{n} M_i(x_i - x_{i-1}) = 1$$
Let $\varepsilon = 1/2$. Then, $U(f, P) - L(f, P) = 1 > \varepsilon$. Thus $f$ is not integrable.
(Uses density of $\Q$ and of the irrationals in each subinterval, not stated.)

## HW2400 057 · `20261121_230815.jpg` · Integrability over discontinuities

**Def.** [a theorem] If $f : [a, b] \to \R$ is continuous at all but finitely many points, then $f$ is integrable. [possible error: $f$ must also be bounded (as MATH1071 HW 53 states and the proof uses)]

**P.** We first show that continuity implies integrability. As $f$ is continuous on a compact interval, it is uniformly continuous. Fix $\varepsilon > 0$.
Then, there exists $\delta > 0$ such that $\abs{x - y} < \delta$ implies $\abs{f(x) - f(y)} < \varepsilon/\abs{b - a}$.
Let $P$ be a partition of $[a, b]$ such that $\Delta x_i < \delta$ for all $i$. Then, [crossed-out text]
$$U(f, P) - L(f, P) = \sum_{i=1}^{n}\Bigl(\sup_{[x_{i-1}, x_i]} f(x) - \inf_{[x_{i-1}, x_i]} f(x)\Bigr)(x_i - x_{i-1})$$
Since $f$ is continuous, by the EVT, $\exists x_i', x_i''$ such that $f(x_i') = \sup_{x \in [x_{i-1}, x_i]} f(x)$ and $f(x_i'') = \inf_{x \in [x_{i-1}, x_i]} f(x)$. Thus,
$$U(f, P) - L(f, P) = \sum_{i=1}^{n}(f(x_i') - f(x_i''))(x_i - x_{i-1}) < \sum_{i=1}^{n} \varepsilon/\abs{b - a}(x_i - x_{i-1}) = \varepsilon/\abs{b - a}(x_n - x_0) = \varepsilon/\abs{b - a} \cdot \abs{b - a} = \varepsilon.$$
Thus $f$ is integrable.
We now show that if $f$ has one discontinuity on $c \in [a, b]$, then $f$ is integrable. Since $f$ is bounded, there exists $M > 0$ such that $\abs{f(x)} \le M$ for all $x \in [a, b]$.
(same as MATH1071 HW 53.)

## HW2400 058 · `20261121_230820.jpg` · Integrability over discontinuities (cont.)

**P.** We define $\delta = \min\{\varepsilon/8M, \frac{b - c}{2}, \frac{c - a}{2}\}$. Thus $[c - \delta, c + \delta] \subset [a, b]$.
By the previous proof, $f$ is integrable on $[a, c - \delta]$ and $[c + \delta, b]$, since $f$ is continuous on both compact intervals. Thus there exists partitions $P_1$ of $[a, c - \delta]$ and $P_2$ of $[c + \delta, b]$ such that $U(f, P_1) - L(f, P_1) < \varepsilon/4$ and $U(f, P_2) - L(f, P_2) < \varepsilon/4$.
Define $P = P_1 \cup P_2$. Note that $P$ is a partition of $[a, b]$. Then,
$$\begin{aligned} U(f, P) - L(f, P) &= (U(f, P_1) - L(f, P_1)) + (U(f, P_2) - L(f, P_2)) + \Bigl(\sup_{x \in [c - \delta, c + \delta]} f(x) - \inf_{x \in [c - \delta, c + \delta]} f(x)\Bigr)(c + \delta - (c - \delta))\\ &< \frac{\varepsilon}{4} + \frac{\varepsilon}{4} + \Bigl(\sup_{x \in \cdots} f(x) - \inf_{x \in \cdots} f(x)\Bigr) \cdot 2\delta < \varepsilon/2 + 2M \cdot 2 \cdot \delta \le \varepsilon/2 + 4M \cdot \varepsilon/8M = \varepsilon/2 + \varepsilon/2 = \varepsilon. \end{aligned}$$
[possible error: "$< \varepsilon/2 + 2M \cdot 2\delta$" should be "$\le$" (the bracket is at most $2M$); the end is "$= \varepsilon$", so the final strict inequality comes from the first "$<$"]
Thus $f$ is integrable.
If $f$ has a finite number $n$ of discontinuities, then apply the second proof $n$ times.
(as in MATH1071 HW 54, $c$ must be interior.)

## HW2400 059 · `20261121_230828.jpg` · Monotone implies integrable

**Def.** [a theorem] If $f : [a, b] \to \R$ is monotone, it is integrable.

**P.** WLOG, assume $f$ is monotone increasing. Fix $\varepsilon > 0$. Let $P$ be a partition that splits $[a, b]$ into $n$ equal parts. Thus, each $x_k \in P$ [crossed-out word] is defined by $x_k = a + k \cdot \frac{b - a}{n}$. Then,
$$\begin{aligned} U(f, P) - L(f, P) &= \sum_{i=1}^{n}\Bigl(\sup_{[x_{i-1}, x_i]} f(x) - \inf_{[x_{i-1}, x_i]} f(x)\Bigr)(x_i - x_{i-1}) = \sum_{i=1}^{n}(f(x_i) - f(x_{i-1}))(x_i - x_{i-1})\\ &= (f(x_n) - f(x_0)) \cdot \frac{b - a}{n} = \frac{b - a}{n} \cdot (f(b) - f(a)) \end{aligned}$$
Choose $n$ such that $n > \frac{b - a}{\varepsilon} \cdot (f(b) - f(a))$. Then $f$ is integrable.
(as MATH1071 HW 55, with the theorem stated the right way round.)

## HW2400 060 · `20261121_230832.jpg` · Properties of the integral

**Def.** [a theorem] If $f, g : [a, b] \to \R$ are integrable, then the following properties apply:
(1) Let $k \in \R$. Then $kf$ is integrable, and $\int_a^b kf = k\int_a^b f$
(2) $f + g$ is integrable, and $\int_a^b (f + g) \dd x = \int_a^b f + \int_a^b g$
(3) If $f \le g$ on $[a, b]$, then $\int_a^b f \le \int_a^b g$
(4) If $f$ is integrable on both $[a, b]$ and $[b, c]$, then $f$ is integrable on $[a, c]$, and $\int_a^c f = \int_a^b f + \int_b^c f$
(5) For all $d \in [a, b]$, $f$ is integrable on $[a, d]$ and $[d, b]$.
(6) Triangle inequality for integrals: $\abs{f}$ is integrable, and $\bigl\lvert \int_a^b f \bigr\rvert \le \int_a^b \abs{f}$.
(7) Let $a < b$. Then, $\int_a^a f \equiv 0$, $\int_a^b f \equiv -\int_b^a f$
[(7) is a definition (convention), not a property; written with $\equiv$]

## HW2400 061 · `20261121_230839.jpg` · Mean value theorem for integrals / Fundamental theorem of calculus

**Def.** [a theorem] If $f$ is continuous on $[a, b]$, then there exists some $c \in [a, b]$ such that $\int_a^b f(x) \dd x = f(c)(b - a)$.

**P.** As $f$ is continuous, $f$ is integrable. By the EVT, $\exists x_m, x_M$ such that $f(x_m) = \min_{[a, b]} f(x)$ and $f(x_M) = \max_{[a, b]} f(x)$. Thus,
$$f(x_m)(b - a) \le \int_a^b f \le f(x_M)(b - a),\qquad f(x_m) \le \frac{\int_a^b f}{b - a} \le f(x_M)$$
By the IVT, $\exists c \in (a, b)$ such that: $f(c) = \frac{1}{b - a}\int_a^b f(x) \dd x$.
[possible error: the IVT gives $c$ between $x_m$ and $x_M$ (so $c \in [a, b]$, as stated in the theorem), not necessarily in $(a, b)$; the equality cases are not treated]

**Fundamental theorem of calculus**

**Def.** [a theorem] Let $f : [a, b] \to \R$ be continuous. Define $F(x) = \int_a^x f(t) \dd t$. Then $F$ is differentiable on $(a, b)$, $F$ is an antiderivative of $f$, and $\int_a^b f(t) \dd t = F(b) - F(a)$.

**P.** We first show that $F' = f$ on $[a, b]$. Let $x \in (a, b)$. Fix $h \in (a - x, b - x) \setminus \{0\}$. Then $F(x + h)$ is defined, and

## HW2400 062 · `20261121_230844.jpg` · Fundamental theorem of calculus (cont.)

$$F(x + h) - F(x) = \int_a^{x+h} f - \int_a^x f = \int_x^{x+h} f = \frac{h}{\abs{h}}\int_{\min\{x, x+h\}}^{\max\{x, x+h\}} f = \frac{h}{\abs{h}} \cdot \abs{h} \cdot f(c_h)$$
where $\min\{x, x + h\} \le c_h \le \max\{x, x + h\}$ by the mean value theorem for integrals.
Define $c : (a - x, b - x) \setminus \{0\} \to \R$ such that $c(h) = c_h$. By the squeeze theorem, since $\lim_{h \to 0} x = \lim_{h \to 0} x + h = x$, then $\lim_{h \to 0} c(h) = x$. Therefore,
$$\lim_{h \to 0} \frac{F(x + h) - F(x)}{h} = \lim_{h \to 0} f(c_h) = f(\lim_{h \to 0} c_h) = f(x).$$
Thus $F$ is differentiable on $(a, b)$ and $F' = f$.
For the remaining statement,
$$F(a) = \int_a^a f = 0,\quad F(b) = \int_a^b f \implies F(b) - F(a) = F(b) - 0 = \int_a^b f - 0 = \int_a^b f.$$
(a blot before the last integral.)
[the proof covers $x \in (a, b)$ only, although it announces "$F' = f$ on $[a, b]$"; $f(\lim c_h) = \lim f(c_h)$ uses continuity of $f$ (not cited)]

## HW2400 063 · `20261121_230850.jpg` · Remarks on integrability

**Def.** [a theorem] If $G' = f$ on $(a, b)$, then
$$(G - F)'(x) = G'(x) - F'(x) = f(x) - f(x) = 0. \implies G - F \equiv c \in \R \implies G(x) = F(x) + c$$
$$\implies G(b) - G(a) = (G(b) - c) - (G(a) - c) = F(b) - F(a) = \int_a^b f.$$
[possible error: should be $(F(b) + c) - (F(a) + c)$ written in terms of $G$; also "derivative zero $\implies$ constant" is used without proof (it follows from the MVT); $G$ must be continuous on $[a, b]$]

**Def.** [a statement] If $f$ is discontinuous, $F(x) = \int_a^x f(t) \dd t$ is not necessarily differentiable.

**P.** Consider $f : [-1, 1] \to \R$, $f(x) = \operatorname{sgn}(x)$. The integral is: $\int_{-1}^{x} f = \abs{x} - 1$. Note that $\abs{x}$ is not differentiable at $x = 0$.

**Def.** [remark] To formalise the above, it can be shown that integrating an integrable function makes it continuous (see 1071), and that integrating a continuous function makes it differentiable (by the FTC).
[see MATH1071 HW 56]

## HW2400 064 · `20261121_230853.jpg` · Integration techniques

**Def.** [a theorem] Integration by parts. Suppose $u, v : [a, b] \to \R$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Then $\int_a^b uv' \dd x = uv\big|_a^b - \int_a^b vu' \dd x$

**P.** By the product rule, $(uv)' = u'v + uv'$. Integrating gives $uv = \int u'v \dd x + \int uv' \dd x$, and rearranging gives the result. The formula for the definite integral follows from the FTC.
[$u'v$ and $uv'$ must be integrable; not stated]

**Def.** [a theorem] Integration by substitution. Suppose $f, g : [a, b] \to \R$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Then
$$\int_{g(a)}^{g(b)} f(u) \dd u = \int_a^b f(g(x))g'(x) \dd x$$
[possible error: hypotheses as in MATH1071 HW 61 ($g'$ continuous, $f$ continuous on the range of $g$)]

**Def.** Integration by partial fraction decomposition. See Lebl, or 1071.

**Rem.** The previous two definitions are not present in the workbook – their proofs cannot be assessed, and are thus omitted. See Lebl or 1071 for proofs.
[MATH1071 typed notes §7.1 cover partial fractions; MATH1071 HW 61 has the substitution proof]

## HW2400 065 · `20261121_230902.jpg` · Improper integrals

**Def.** Consider $f : (a, b] \to \R$. Note that $f$ is not necessarily bounded. Assume $f$ is integrable on $[a + \varepsilon, b]$, where $\varepsilon \in (0, b - a)$. Then the improper integral of the first kind is given by:
$$\lim_{\varepsilon \to 0^+} \int_{a+\varepsilon}^{b} f \dd x = \int_a^b f \dd x$$
(the lower limit "$a + \varepsilon$" is first written "$d + \varepsilon$".)

**Def.** Let $f : [a, \infty) \to \R$ be integrable on $[a, b]$ for all $b > a$. Then the improper integral of the second kind is given by:
$$\lim_{b \to \infty} \int_a^b f \dd x = \int_a^\infty f \dd x$$
[the existence of the limits is implicit; "first/second kind" is the notes' terminology]

**Def.** Given that both improper integrals exist, $\int_{-\infty}^{\infty} f \dd x = \int_{-\infty}^{0} f \dd x + \int_0^\infty f \dd x$

**Rem.** Note that $\int_{-\infty}^{\infty} f \dd x \ne \int_{-a}^{a} f \dd x$ as $a \to \infty$.

**Ex.** The integral $\int_{-\infty}^{\infty} x \dd x$ does not exist as the integrals $\int_{-\infty}^{0} x \dd x$ and $\int_0^\infty x \dd x$ do not.

## HW2400 066 · `20261121_230905.jpg` · Examples of improper integrals

**Ex.**
$$\int_0^1 \frac{1}{\sqrt{x}} \dd x = \lim_{\varepsilon \to 0^+} \int_\varepsilon^1 \frac{1}{\sqrt{x}} \dd x = \lim_{\varepsilon \to 0^+} 2\sqrt{x}\Big|_\varepsilon^1 = 2\lim_{\varepsilon \to 0^+}(1 - \sqrt{\varepsilon}) = 2.$$

**Ex.** Consider the general case $\int_0^1 x^p \dd x$.
- If $p > 0$, $x^p$ is continuous and therefore integrable on $[0, 1]$.
- If $p \in (-1, 0]$, the integral is $1/(p + 1)$. Proof as exercise, see above.
- If $p < -1$, a similar argument shows the integral must diverge.
- If $p = 1$, the integral must diverge. Again the proof is left as a similar exercise. [possible error: $p = -1$]
Therefore the integral exists for $p \in (-1, \infty)$.
[for $p > 0$ the value $1/(p+1)$ also holds; $p \in (-1, 0)$ is the improper case]

## HW2400 067 · `20261121_230911.jpg` · Integral test for series

**Def.** [a theorem] Let $f : [1, \infty) \to \R^{+}$ be non-increasing and continuous. Then $\int_1^\infty f \dd x$ and $\sum_{n=1}^{\infty} f(n)$ either converge or diverge together.

**P.** Consider a partition $\{1, 2, \dots, n, n + 1\}$ of the interval $[1, n + 1]$. As $f$ is non-increasing ("in" inserted over a crossed-out "de"),
$$\inf\{f(x) : x \in [x_{i-1}, x_i]\} = f(x_i),\qquad \sup\{f(x) : x \in [x_{i-1}, x_i]\} = f(x_{i-1})$$
Thus,
$$U(f, P) = \sum_{i=1}^{n} \sup_{\cdots} f(x)(x_i - x_{i-1}) = \sum_{i=1}^{n} f(x_{i-1}) \cdot 1 = \sum_{i=1}^{n} f(i).$$
By similar logic, $L(f, P) = \sum_{i=1}^{n} f(i + 1)$. Note that $L(f, P) \le \int_1^{n+1} f \dd x \le U(f, P)$.
If $\int_1^\infty f \dd x$ converges, then by comparison $L(f, P) = \sum_{i=1}^{n} f(i + 1) = \sum_{i=2}^{n+1} f(i)$ converges as $n \to \infty$.
If $\int_1^\infty f \dd x$ diverges, then by comparison $U(f, P) = \sum_{i=1}^{n} f(i)$ diverges as $n \to \infty$. Thus $\sum_{n=1}^{\infty} f(n)$ diverges.
Thus $\sum_{n=1}^{\infty} f(n) = S_1 + \sum_{n=2}^{\infty} f(n)$ converges. (an arrow links this line back to the "converges" case.)
Use similar logic for if the series diverges.
[$S_1$ means $f(1)$; the converse directions (series $\Rightarrow$ integral) are left to "similar logic"]
(cf. MATH1071 HW 63.)

## HW2400 068 · `20261121_230916.jpg` · Definitions of exp(x) and ln(x)

**Def.** One definition of $\ln(x)$ is the following: Let $\ln : (0, \infty) \to \R$ be such that $\ln(x) = \int_1^x \frac1t \dd t$.

**Def.** [a theorem] $\ln(x)$ is invertible.

**P.** $\sum_{n=1}^{\infty} \frac1n$ diverges, so $\ln(x)$ has no upper bound. Thus $\forall M > 0$, $\exists d$: $\ln(d) > M$.
By the FTC, $\frac{\dd}{\dd x}\ln(x) = \frac1x$. Thus $\ln(x)$ is diff. and hence continuous.
By the IVT, $\exists c$: $1 < c < d$, where $\ln(c) = M$.
It can be shown (proof as exercise) that $\ln(c^{-1}) = -\ln(c) = M$. [possible error: $\ln(c^{-1}) = -\ln(c) = -M$]
Thus, $\ln(x)$ is surjective.
As $\frac{\dd}{\dd x}\ln(x) = \frac1x > 0$, $\ln(x)$ is monotone and hence injective. Thus $\ln(x)$ is bijective.
Therefore, $f(x) = \ln(x)$ is invertible.
[the divergence of $\int_1^\infty \frac1t \dd t$ from that of $\sum \frac1n$ is the integral test (HW 067), not cited; "monotone" should be "strictly monotone" (from $f' > 0$ via the MVT)]

**Def.** Define $\exp : \R \to (0, \infty)$ such that $\exp(\ln(x)) = \ln(\exp(x)) = x$.

**P.** By the inverse function theorem, let $y = \ln(x)$. Then
$$(\exp(y))' = \frac{1}{(\ln(\exp(y)))'} = \frac{1}{1/\exp(y)} = \exp(y).$$
[possible error: the denominator should be $\ln'(\exp(y)) = 1/\exp(y)$; "$(\ln(\exp(y)))'$" is the derivative of $y$, which is $1$]

## HW2400 069 · `20261121_230936.jpg` · Sequences of functions, pointwise convergence

**Def.** Let $\Omega \subseteq \R$, and suppose $f_n : \Omega \to \R$ is a function $\forall n \in \N$. Consider the sequence $\{f_n\}_{n=1}^{\infty}$. Then the sequence $\{f_n\}$ converges pointwise to $f : \Omega \to \R$ if $\lim_{n \to \infty} f_n(x) = f(x)$, $\forall x \in \Omega$.

**Rem.** Equivalently, $\forall \varepsilon > 0$, $\forall x \in \Omega$, $\exists N \in \N$ such that $n \ge N \implies \abs{f_n(x) - f(x)} < \varepsilon$.

**Rem.** Note that $N$ is based on both $\varepsilon$ and $x$.

**Ex.** The sequence $f_n(x) = x^n$ converges on $[0, 1]$.

**P.** If $x \in [0, 1)$, then $\lim_{n \to \infty} f_n(x) = 0$. If $x = 1$, then $\lim_{n \to \infty} f_n(1) = 1$. Thus $\{f_n\}$ converges pointwise on $[0, 1]$ to
$$f(x) = \begin{cases} 0 & \text{if } x \in [0, 1)\\ 1 & \text{if } x = 1\end{cases}$$

**Rem.** We can think of pointwise convergence as the property that at every point, the sequence of function has its own speed of convergence. In contrast, uniform convergence imply that there is an overall speed of convergence.

**Rem.** Uniform convergence implies pointwise convergence.

## HW2400 070 · `20261121_230950.jpg` · Uniform convergence of functions

**Def.** Let $\Omega \to \R$. [read: $\Omega \subseteq \R$] The sequence $\{f_n\}$ converges uniformly to $f$, written $f_n \underset{n \to \infty}{\rightrightarrows} f$, if $\forall \varepsilon > 0$, $\exists N \in \N$ such that $n \ge N \implies \abs{f_n(x) - f(x)} < \varepsilon$ $\forall x \in \Omega$.

**Rem.** Note that the difference between pointwise and uniform continuity of functions is the positioning of '$\forall x \in \Omega$'. Here, $N$ is only based on $\varepsilon$. [read: "convergence", not "continuity"]

**Def.** [a theorem] If $f_n : \Omega \to \R$ is continuous $\forall n \in \N$, and if $f_n$ converges uniformly to $f$, then $f$ is continuous.

**P.** Fix $\varepsilon > 0$. Let $x \in \Omega$. Then, $\exists N \in \N$ such that $\abs{f_n(t) - f(t)} < \varepsilon/3$, $\forall n \ge N$, $\forall t \in \Omega$.
As $f_N$ is continuous on $\Omega$, it is continuous on $x$. Thus, $\exists \delta > 0$ such that $\forall y \in \Omega$, $\abs{x - y} < \delta \implies \abs{f_N(x) - f_N(y)} < \varepsilon/3$.
Now suppose $y \in \Omega$ and $\abs{x - y} < \delta$. Then,
$$\begin{aligned} \abs{f(x) - f(y)} &= \abs{f(x) - f_N(x) + f_N(x) - f_N(y) + f_N(y) - f(y)}\\ &\le \abs{f(x) - f_N(x)} + \abs{f_N(x) - f_N(y)} + \abs{f_N(y) - f(y)} < \underset{(\text{u.c.})}{\varepsilon/3} + \underset{(\text{c})}{\varepsilon/3} + \underset{(\text{u.c.})}{\varepsilon/3} = \varepsilon \end{aligned}$$

**Rem.** The above theorem is usually called the uniform limit theorem.

## HW2400 071 · `20261121_230955.jpg` · Examples on uniform convergence

**Ex.** Show $f_n(x) = x^n$ on $[0, 1]$ is not uniformly convergent.

**P.** We will prove using the negation. $\exists \varepsilon > 0$: $\forall n \in \N$, $\exists x \in \Omega$: $\abs{f_n(x) - f(x)} \ge \varepsilon$. Note $x$ can vary for different $n$.
Take $\varepsilon = \frac12$, $x_n = (3/4)^{1/n}$. Then $\forall n \in \N$, $0 \le (3/4)^{1/n} < 1 \implies f((3/4)^{1/n}) = 0$.
Also, $f_n((3/4)^{1/n}) = ((3/4)^{1/n})^n = 3/4$. Thus by the definition,
$$\abs{f_n(x) - f(x)} = \abs{3/4 - 0} = 3/4 > 1/2.$$
[the negation is of uniform convergence to the pointwise limit $f$ of HW 069]

**Ex.** Using the same mapping, $f_n \underset{n \to \infty}{\rightrightarrows} f$ on $[0, p]$ $\forall p < 1$.

**P.** Fix $\varepsilon > 0$. Then we must show $\exists N \in \N$: $\forall n \ge N$, $\abs{f_n(x) - f(x)} < \varepsilon$ $\forall x \in [0, p]$, $p < 1$. Thus,
$$\abs{f_n(x) - f(x)} = \abs{x^n - 0} = x^n = x^Nx^{n-N} \le x^N \le p^N$$
We must find $N$ such that $p^N < \varepsilon$. As $\ln(\cdot)$ is monotone increasing,
$$\ln p^N < \ln \varepsilon \implies N\ln p < \ln \varepsilon \implies N > \frac{\ln \varepsilon}{\ln p}$$
Thus set $N = \floor{\frac{\ln \varepsilon}{\ln p}} + 1$. (the bracket is drawn like $\lfloor\ \rfloor$ with long bars.)
[needs $0 < p < 1$ (for $\ln p$) and $\varepsilon < 1$, or $N \ge 1$ otherwise]

## HW2400 072 · `20261121_231001.jpg` · Examples on uniform convergence (cont.)

**Ex.** Show $f_n(x) = \sin^n(x)$ on $x \in \R$ is not uniformly convergent.

**P.** $f_n(x)$ is not pointwise convergent on any interval $I \subseteq \R$ with $I \ni \frac{3\pi}{2} + 2m\pi$, $m \in \N$.
As homework, show that $\sin^n(x)$ is (or is not) pointwise or uniform continuous on any subinterval of $\R$ (i.e. find one if one exists).
[at $x = \frac{3\pi}{2} + 2m\pi$, $\sin^n x = (-1)^n$ (not written); $m \in \Z$ would cover all such points; "continuous" should be "convergent"]

**Def.** [remark] We can rewrite the previous definition using limits by, given the conditions on $f_n$,
$$\lim_{x \to a}\Bigl(\lim_{n \to \infty} f_n(x)\Bigr) = \lim_{n \to \infty}\Bigl(\lim_{x \to a} f_n(x)\Bigr).$$
This is because:
- If $f$ is continuous, $f(a) = \lim_{x \to a} f(x)$.
- If $f_n$ is continuous, $f_n(a) = \lim_{x \to a} f_n(x)$.
- If $f_n$ is u.c., $f(x) = \lim_{n \to \infty} f_n(x)$.
["the previous definition" = the uniform limit theorem (HW 070); "u.c." here means uniformly convergent]

## HW2400 073 · `20261121_231006.jpg` · Interchanging limits

**Ex.** Is $\lim_{n \to \infty}\Bigl(\lim_{k \to \infty} \frac{n}{n + k}\Bigr) = \lim_{k \to \infty}\Bigl(\lim_{n \to \infty} \frac{n}{n + k}\Bigr)$?
No – $\lim_{n \to \infty}\bigl(\lim_{k \to \infty} \frac{n}{n + k}\bigr) = \lim_{n \to \infty}(0) = 0$
but – $\lim_{k \to \infty}\bigl(\lim_{n \to \infty} \frac{n}{n + k}\bigr) = \lim_{k \to \infty}(1) = 1$.

**Ex.** Let $f_n(x) = \frac{\sin(nx)}{\sqrt{n}}$ for $x \in \R$. Is $\lim_{n \to \infty}\bigl(\frac{\dd}{\dd x}f_n(x)\bigr) = \frac{\dd}{\dd x}\bigl(\lim_{n \to \infty} f_n(x)\bigr)$?
No – $\lim_{n \to \infty}\bigl(\frac{\dd}{\dd x}f_n(x)\bigr) = \lim_{n \to \infty}(\sqrt{n}\cos(nx))$. This limit does not exist for $x = 0$.
but – [crossed out] $\frac{\dd}{\dd x}\bigl(\lim_{n \to \infty} f_n(x)\bigr) = \frac{\dd}{\dd x} \cdot 0 = 0$.

**Ex.** Let $f_n(x) = n^2x(1 - x^2)^n$ for $x \in [0, 1]$. Is $\lim_{n \to \infty}\int_0^1 f_n(x) \dd x = \int_0^1 \lim_{n \to \infty} f_n(x) \dd x$?
No – $\lim_{n \to \infty}\int_0^1 f_n(x) \dd x = \lim_{n \to \infty}\bigl(\frac{n^2}{2n + 2}\bigr) = \infty$.
but – $\int_0^1 \lim_{n \to \infty} f_n(x) \dd x = \int_0^1 0 \dd x = 0$.
We can show $f_n$ is not uniformly convergent. (not shown)
(checked: $\int_0^1 n^2x(1 - x^2)^n \dd x = \frac{n^2}{2(n + 1)}$.)

## HW2400 074 · `20261121_231013.jpg` · Interchanging limits in integration

**Def.** [a theorem] Suppose $\{f_n\}$ is a sequence of functions which are integrable on $[a, b]$. Let $\{f_n\}$ converge uniformly on $[a, b]$ to a function $f$ which is integrable on $[a, b]$. Then,
$$\lim_{n \to \infty}\int_a^b f_n = \int_a^b \lim_{n \to \infty} f_n = \int_a^b f.$$

**P.** Fix $\varepsilon > 0$. Then $\exists N \in \N$: $\forall n \ge N$, $\abs{f_n(x) - f(x)} < \frac{\varepsilon}{2(b - a)}$. Thus for $n \ge N$:
$$\Bigl\lvert \int_a^b f_n - \int_a^b f \Bigr\rvert = \Bigl\lvert \int_a^b (f_n - f) \Bigr\rvert \le \int_a^b \abs{f_n(x) - f(x)} \dd x < \int_a^b \frac{\varepsilon}{2(b - a)} \dd x = \frac{\varepsilon}{2(b - a)}(b - a) = \varepsilon/2 < \varepsilon.$$
[the strict "$<$" between integrals needs a remark ($\le$ suffices, since the result is $\le \varepsilon/2 < \varepsilon$)]

## HW2400 075 · `20261121_231019.jpg` · Interchanging limits in differentiation

**Def.** [a theorem] Let $\{f_n\}$ be a sequence of continuously differentiable functions defined on $[a, b]$. Let the sequence $\{f_n\}$ converge pointwise to $f$. Let the sequence of derivatives $\{f_n'\}$ converge uniformly. Then $f$ is differentiable on $(a, b)$ and
$$\frac{\dd}{\dd x}\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{\dd}{\dd x}f_n(x).$$
Alternatively, $f' = \lim_{n \to \infty} f_n'$.

**P.** Let $g = \lim_{n \to \infty} f_n'$. Since $\{f_n'\}$ is continuous and uniformly convergent, $g$ is continuous. Let $x \in [a, b]$. Thus $g$ is integrable and so
$$\int_a^x g = \int_a^x \lim_{n \to \infty} f_n' = \lim_{n \to \infty}\int_a^x f_n' = \lim_{n \to \infty}(f_n(x) - f_n(a)) = f(x) - f(a).$$
Since $g$ is continuous, we have $g(x) = \frac{\dd}{\dd x}\int_a^x g = \frac{\dd}{\dd x}(f(x) - f(a)) = f'(x)$.
(Uses the uniform limit theorem (HW 070), HW 074, and the FTC (HW 061–062).)

## HW2400 076 · `20261121_231024.jpg` · Uniformly Cauchy sequences

**Def.** Let $\{f_n\}$ be a sequence of functions defined on $\Omega$. Then $\{f_n\}$ is uniformly Cauchy iff $\forall \varepsilon > 0$, $\exists N \in \N$: $\forall l, m \ge N$, then $\abs{f_l(x) - f_m(x)} < \varepsilon$ $\forall x \in \Omega$.

**Def.** [a theorem] The sequence of functions $\{f_n\}$ converges uniformly to some function $f$ iff the sequence is uniformly Cauchy.

**P.** We first prove in the forward direction. Assume $f_n \underset{n \to \infty}{\rightrightarrows} f$. Given $\varepsilon > 0$, $\exists N \in \N$: $k \ge N$, $\abs{f_k - f} < \varepsilon/2$ $\forall x \in \Omega$. If $l, m \ge N$, then
$$\abs{f_l(x) - f_m(x)} = \abs{f_l(x) - f(x) + f(x) - f_m(x)} \le \abs{f_l(x) - f(x)} + \abs{f(x) - f_m(x)} < \varepsilon/2 + \varepsilon/2 = \varepsilon.$$
We now prove in the reverse direction. As $\{f_n\}$ is Cauchy, it converges (at least) pointwise. Define $f : \Omega \to \R$ by $\lim_{n \to \infty} f_n(x) = f(x)$. Fix $\varepsilon > 0$.
$\exists N \in \N$: $\forall m, n \ge N$, $\forall x \in \Omega$, $\abs{f_m(x) - f_n(x)} < \varepsilon/2$.
Fix $n$, and consider $f_n(x) - \varepsilon/2 < f_m(x)$. This implies $f_n(x) - \varepsilon/2 \le \lim_{m \to \infty} f_m(x) = f(x)$. [the limit is written $\lim_{n \to \infty}$; read $m \to \infty$]
Similarly, $f(x) \le f_n(x) + \varepsilon/2$. Thus, $f_n(x) - \varepsilon/2 \le f(x) \le f_n(x) + \varepsilon/2$. This implies:
$$\abs{f_n(x) - f(x)} \le \varepsilon/2 < \varepsilon.$$
Thus $f$ is uniformly convergent. [read: "$f_n$ converges uniformly to $f$"]

## HW2400 077 · `20261121_231029.jpg` · Series of functions

**Def.** Let $\{f_n\}_{n=1}^{\infty}$ be a sequence of functions $f_n : \Omega \to \R$. Consider $\sum_{n=1}^{\infty} f_n(x) = \lim_{N \to \infty}\sum_{n=1}^{N} f_n(x)$.

**Def.** The series $\sum_{n=1}^{\infty} f_n(x)$ converges pointwise / uniformly if the sequence of partial sums $\{S_k\}$ converges pointwise / uniformly.

**Def.** [a theorem] Weierstraß M-test. Suppose the series $\sum M_n$ converges, with $M_n \ge 0$. Let $\{f_n\}$ be a sequence of functions such that for all $x \in \Omega$, $\abs{f_n(x)} \le M_n$. Then $\sum_{n=1}^{\infty} f_n$ converges uniformly on $\Omega$.

**P.** Suppose $\sum_{n=1}^{\infty} M_n$ converges. Let $S_k(x) = \sum_{i=1}^{k} f_i(x)$. Then by the Cauchy convergence test, $\forall \varepsilon > 0$, $\exists N \in \N$: $\forall m, n \ge N$, $\sum_{i=m+1}^{n} M_i < \varepsilon$. Thus,
$$\abs{S_n(x) - S_m(x)} = \Bigl\lvert \sum_{i=m+1}^{n} f_i(x) \Bigr\rvert \le \sum_{i=m+1}^{n} \abs{f_i(x)} \le \sum_{i=m+1}^{n} M_i < \varepsilon.$$
Thus $\{S_n\}$ is uniformly Cauchy, and thus uniformly convergent.

## HW2400 078 · `20261121_231033.jpg` · Interchanging limits in sums

**Def.** [a theorem] Let $\sum_{n=1}^{\infty} f_n$ converge at least pointwise to $f$ on $[a, b]$. If the convergence is uniform, then
- If each $f_n$ is continuous on $[a, b]$, then $f$ is continuous on $[a, b]$.
- If each $f_n$ and $f$ is integrable on $[a, b]$, then $\sum_{n=1}^{\infty}\int_a^b f_n = \int_a^b \sum_{n=1}^{\infty} f_n = \int_a^b f$

**P.** Let $S_k = \sum_{n=1}^{k} f_n$. As the sum of continuous functions are continuous, $S_k$ is continuous. As $S_k \underset{k \to \infty}{\rightrightarrows} f$, $f$ is thus continuous. Also,
$$\int_a^b f = \lim_{k \to \infty}\int_a^b S_k = \lim_{k \to \infty}\int_a^b \sum_{n=1}^{k} f_n = \lim_{k \to \infty}\sum_{n=1}^{k}\int_a^b f_n = \sum_{n=1}^{\infty}\int_a^b f_n$$

**Def.** [a theorem] If each $f_n'$ is continuous and $\sum_{n=1}^{\infty} f_n'$ converges uniformly on $[a, b]$ to some continuous $f'$, then $f'(x) = \sum_{n=1}^{\infty} f_n'(x)$ $\forall x \in [a, b]$.

**P.** As each $f_n'$ is continuous, so is $S_k' = \sum_{n=1}^{k} f_n'$. As $\{S_k'\}$ converges uniformly to some continuous $f'$,
$$f' = \lim_{k \to \infty} S_k' = \lim_{k \to \infty}\sum_{n=1}^{k} f_n' = \sum_{n=1}^{\infty} f_n'.$$
[possible error: the statement assumes its conclusion (the limit is called $f'$); what is needed is that $\sum f_n$ converges (pointwise) to $f$ and then HW 075 applied to $S_k$ gives $f' = \sum f_n'$]

## HW2400 079 · `20261121_231041.jpg` · Taylor series

**Def.** Let $f : I \to \R$ be continuously differentiable. Define the $n$-th order derivative of $f$ at $a \in I$ by $f^{(n)}(a)$.

**Def.** Suppose $f : I \to \R$ is $n$-times differentiable at $a \in I$. The $n$-th Taylor polynomial of $f$ at $a$ is
$$P_{n,a}(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$$

**Def.** If the limit exists, we define the Taylor series for $f$ (about $a$) by
$$\lim_{n \to \infty} P_{n,a}(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x - a)^k.$$

**Def.** [a theorem] Taylor's theorem – integral form. Let $n \in \N$, and let $f : I \to \R$ be $n + 1$-times differentiable on $I$. Let $a, x \in I$. Then $f(x) = P_{n,a}(x) + R_{n,a}(x)$, where
$$R_{n,a}(x) = \int_a^x \frac{f^{(n+1)}(t)(x - t)^n}{n!} \dd t.$$
We call $R_{n,a}(x)$ the $n$-th remainder term.
[possible error: the integral form needs $f^{(n+1)}$ integrable (e.g. $f \in C^{n+1}$)]

**P.** Define $L_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k + \int_a^x \frac{f^{(n+1)}(t)}{n!}(x - t)^n \dd t$.
We must prove $f(x) = L_n(x)$, for all $n \in \N$ and $x \in I$. We prove by induction.
For the base case, $f(x) = f(a) + \int_a^x f'(t) \dd t = L_0(x)$
For the induction hypothesis, we assume $f(x) = L_m(x)$ for some $m \in M$. [read $m \in \N$]

## HW2400 080 · `20261121_231047.jpg` · Taylor's theorem

**P.** (cont.) Then,
$$L_{m+1}(x) = \sum_{k=0}^{m+1} \frac{f^{(k)}(a)}{k!}(x - a)^k + \int_a^x \frac{f^{(m+2)}(t)}{(m + 1)!}(x - t)^{m+1} \dd t.$$
We integrate by parts. Let
$$u(t) = \frac{(x - t)^{m+1}}{(m + 1)!},\quad v'(t) = f^{(m+2)}(t),\quad \text{implying}\quad u'(t) = -\frac{(x - t)^m}{m!},\quad v(t) = f^{(m+1)}(t).$$
Then,
$$\begin{aligned} L_{m+1}(x) &= \sum_{k=0}^{m+1} \frac{f^{(k)}(a)}{k!}(x - a)^k + \frac{(x - t)^{m+1}}{(m + 1)!}f^{(m+1)}(t)\Big|_a^x - \int_a^x -\frac{f^{(m+1)}(t)(x - t)^m}{m!} \dd t\\ &= \sum_{k=0}^{m} \frac{f^{(k)}(a)}{k!}(x - a)^k + \int_a^x \frac{f^{(m+1)}(t)(x - t)^m}{m!} \dd t = L_m(x) = f(x) \end{aligned}$$
Thus $P(m) \implies P(m + 1)$ which closes the induction.
[the boundary term equals $-\frac{(x-a)^{m+1}}{(m+1)!}f^{(m+1)}(a)$, cancelling the $k = m + 1$ term of the sum (not written)]

## HW2400 081 · `20261121_231054.jpg` · Taylor's theorem (cont.)

**Def.** [a theorem] Suppose $f : I \to \R$ is infinitely differentiable at $a \in I$. Then $P_{n,a}(x)$ converges to $f(x)$ iff $R_{n,a}(x) \to 0$.

**P.** We first prove in the forward direction. Let $R_{n,a}(x) = f(x) - P_{n,a}(x)$. If $\lim_{n \to \infty} P_{n,a}(x) = f(x)$, then
$$\lim_{n \to \infty} R_{n,a}(x) = \lim_{n \to \infty} P_{n,a}(x) - \lim_{n \to \infty} P_{n,a}(x) = f(x) - f(x) = 0.$$
[possible error: the first limit should be $\lim f(x) = f(x)$]
We now prove in the reverse direction. Let $P_{n,a}(x) = f(x) - R_{n,a}(x)$. If $\lim_{n \to \infty} R_{n,a}(x) = 0$, then
$$\lim_{n \to \infty} P_{n,a}(x) = \lim_{n \to \infty} f(x) - \lim_{n \to \infty} R_{n,a}(x) = f(x) - 0 = f(x).$$

**Def.** The function $f : I \to \R$ is analytic at $a \in I$ if $P_{n,a}(x) \to f(x)$ $\forall x \in J \ni a$, where $J \subseteq I$ is open.

## HW2400 082 · `20261121_231057.jpg` · Lagrange form of remainder

**Def.** [a theorem] If $a \ne x$, we can write $R_{n,a}(x)$ by
$$R_{n,a}(x) = \frac{f^{(n+1)}(z)}{(n + 1)!}(x - a)^{n+1},\quad \text{for } z \text{ between } a, x.$$

**P.** WLOG, let $x > a$. Since $f^{(n+1)}$ is continuous on $[a, x]$, by the EVT $\exists m, M$:
$$m = \min\{f^{(n+1)}(t) : t \in [a, x]\},\quad M = \max\{f^{(n+1)}(t) : t \in [a, x]\}$$
As $0 \le (x - t)^n/n!$ $\forall t \in [a, x]$,
$$\frac{m(x - t)^n}{n!} \le f^{(n+1)}(t)\frac{(x - t)^n}{n!} \le \frac{M(x - t)^n}{n!}$$
$$\implies m\int_a^x \frac{(x - t)^n}{n!} \dd t \le R_{n,a}(x) \le M\int_a^x \frac{(x - t)^n}{n!} \dd t \implies m \le \frac{(n + 1)!}{(x - a)^{n+1}}R_{n,a}(x) \le M$$
By the IVT, there exists $z \in (a, x)$: $f^{(n+1)}(z) = \frac{(n + 1)!}{(x - a)^{n+1}}R_{n,a}(x)$. The result follows by rearrangement.
[the IVT gives $z \in [a, x]$; the case $x < a$ is "WLOG" but the sign of $(x - t)^n$ changes for odd $n$]

## HW2400 083 · `20261121_231103.jpg` · Familiar Maclaurin series

**Def.** The following are familiar Maclaurin series:
$$\sin(x) = \sum_{k=0}^{n} (-1)^k\frac{x^{2k+1}}{(2k + 1)!} + \frac{\sin^{(2n+2)}(z)}{(2n + 2)!}x^{2n+2}$$
$$\cos(x) = \sum_{k=0}^{n} (-1)^k\frac{x^{2k}}{(2k)!} + \frac{\cos^{(2n+1)}(z)}{(2n + 1)!}x^{2n+1}$$
$$\exp(x) = \sum_{k=0}^{n} \frac{x^k}{k!} + \frac{\exp^{(n+1)}(z)}{(n + 1)!}x^{n+1}$$
for some $z$ between $0$ and $x$.

**Exercise.** Show that these functions are analytic at $0$.

**Ex.** Use a Maclaurin series to show an approximation of $e$, with error $< 5 \times 10^{-6}$.
We know that by the Maclaurin series of $\exp(x)$,
$$\exp(1) = \sum_{k=0}^{\infty} \frac{1^k}{k!} = 1 + 1 + \frac12 + \dots + \frac{1}{n!} + \frac{e^z}{(n + 1)!}$$
As $0 < t < 1 = e^0 < e^z < e^1 < 3$, the error term will be $\frac{e^z}{(n + 1)!} < \frac{3}{(n + 1)!} < 0.000005$.
Taking $n = 9$ suffices. Thus,
$$e = 1 + 1 + \frac12 + \dots + \frac{1}{9!} + R_{9,0}(1)$$
where $0 < R_{9,0}(1) < 0.000005$.
[the first "$\exp(1) = \sum_{k=0}^{\infty}$" should be the finite sum plus remainder; "$0 < t < 1$" should read $0 < z < 1$. Checked: $3/10! \approx 8.3 \times 10^{-7} < 5 \times 10^{-6}$, while $3/9! \approx 8.3 \times 10^{-6}$ is not, so $n = 9$ is the least $n$ this bound certifies]

## HW2400 084 · `20261121_231107.jpg` · Examples on Taylor series

**Ex.** Show $e$ is irrational.

**P.** We know that $\forall n \in \N$, $e = 1 + 1 + \frac12 + \dots + \frac{1}{n!} + R_n$ such that $0 < R_n < 3/(n + 1)!$
Suppose for contradiction that $e$ is rational (corrected from "irrational"). Thus $e = a/b$, where $a, b \in \Z^{+}$. Choose $n > \max\{3, b\}$. Thus,
$$\frac{a}{b} = 1 + 1 + \frac12 + \dots + \frac{1}{n!} + R_n,\qquad \frac{n!\,a}{b} = n! + n! + \frac{n!}{2} + \dots + 1 + n!R_n$$
Note that every term (except possibly the last term) is an integer (on the RHS). Since the LHS is an integer (as $n > b$), then $n!R_n$ is an integer. Thus,
$$0 < R_n < 3/(n + 1)! \implies 0 < n!R_n < 3/(n + 1) < 3/4.$$
No integer exists between $0$ and $1$, ↯. Thus $e$ is irrational.

**Ex.** Compute the Taylor series of $f(x) = \ln(x)$ at $a = 1$.

**P.** Computing the derivatives, we can show that
$$\ln(x) = \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k}(x - 1)^k + \frac{\ln^{(n+1)}(z)}{(n + 1)!}(x - 1)^{n+1}.$$
for some $z$ between $1$ and $x$. (the sum is written with $(n - 1)^k$; read $(x - 1)^k$.)

**Rem.** Is $\ln(x)$ analytic at $x = 1$? If so, for how large an interval? Consider the Taylor series – it converges in $(0, 2]$, but does it converge to $\ln(x)$? (left open)

## HW2400 085 · `20261121_231114.jpg` · Power series

**Def.** A function of the form below is called a power series centred at $b$:
$$f(x) = \sum_{n=0}^{\infty} a_n(x - b)^n$$
Power series may not converge to all $\R$, but it is always defined at $x = b$, as $f(b) = a_0$.

**Def.** [a theorem] Suppose the series $\sum_{n=0}^{\infty} a_nx_0^n$ converges. Let $a \in \R$ be such that $0 < a < \abs{x_0}$. Then on $[-a, a]$, the power series $f(x) = \sum_{n=0}^{\infty} a_nx^n$ converges uniformly (and absolutely). Finally, $f'$ exists and $f'(x) = \sum_{n=1}^{\infty} na_nx^{n-1}$.

**P.** As $\sum a_nx_0^n$ converges, it is bounded. [read: its terms are bounded] Thus $\forall n$, $\exists M$: $\abs{a_nx_0^n} = \abs{a_n}\abs{x_0^n} \le M$. [should be "$\exists M\ \forall n$"]
If $x \in [-a, a]$, then $\abs{x} \le \abs{a}$. Thus,
$$\abs{a_nx^n} = \abs{a_n}\abs{x^n} \le \abs{a_n}\abs{a^n} = \abs{a_n}\abs{x_0}^n\Bigl\lvert \frac{a}{x_0} \Bigr\rvert^n \le M\Bigl\lvert \frac{a}{x_0} \Bigr\rvert^n.$$
As $\abs{\frac{a}{x_0}} < 1$, the geometric series $\sum M\abs{\frac{a}{x_0}}^n$ converges. Thus choose $M_n = M\abs{\frac{a}{x_0}}^n$. By the Weierstraß M test, $\sum a_nx^n$ converges uniformly and absolutely on $[-a, a]$.
To prove $f'$ converges,
$$\abs{na_nx^{n-1}} = n\abs{a_n}\abs{x^{n-1}} \le n\abs{a_n}\abs{a^{n-1}} = \frac{\abs{a_n}\abs{x_0}^n}{\abs{a}} \cdot n\Bigl\lvert \frac{a}{x_0} \Bigr\rvert^n$$
Use similar working and use the ratio test. Then use the Weierstraß M test.
(the last step to $f' = \sum na_nx^{n-1}$ (via HW 078) is not written.)

## HW2400 086 · `20261121_231118.jpg` · Power series (cont.)

**Def.** [a theorem] Any power series which converges on an open interval is its own Taylor series. If $f(x) = \sum_{n=0}^{\infty} a_n(x - b)^n$ converges $\forall x \in (b - R, b + R)$, then $f$ has derivatives of all orders in $(b - R, b + R)$. Also, $a_k = \frac{f^{(k)}(b)}{k!}$

**P.** We first prove this for $b = 0$. Suppose $f(x) = \sum a_nx^n$ converges on $(-R, R)$. Then, $f'(x) = \sum_{n=1}^{\infty} na_nx^{n-1}$ also converges on $(-R, R)$. Applying this theorem $k$ times,
$$f^{(k)}(x) = \sum_{n=k}^{\infty} n(n - 1)\cdots(n - k + 1)a_nx^{n-k} = k(k - 1)\cdots 1\,a_k + \sum_{n=k+1}^{\infty} n(n - 1)\cdots(n - k + 1)a_nx^{n-k}$$
on $(-R, R)$. Thus, $f$ is differentiable at all orders on $(-R, R)$. Moreover, $f^{(k)}(0) = k!\,a_k + 0$ and the result follows.
If $b \ne 0$, define $\bar f(x) = \sum a_nx^n$. Thus $f(x) = \bar f(x - b)$, so $f^{(k)}(b) = \bar f^{(k)}(b - b) = k!\,a_k$ and the result follows.
(the superscript on $f$ is written $(n)$ in places; read $(k)$.)

## HW2400 087 · `20261121_231124.jpg` · Vector functions

**Def.** We work in $\R^n$, with the standard inner product and the standard Euclidean norm.

**Def.** [a theorem (Cauchy–Schwarz; unnamed in the notes)] Let $\vect{x}, \vect{y} \in \R^n$. Then $\norm{\inner{\vect{x}, \vect{y}}} \le \norm{\vect{x}}\norm{\vect{y}}$. [the left side is $\abs{\inner{\vect x, \vect y}}$]

**P.** Trivial for $\vect{x}$ or $\vect{y} = \vect{0}$. Let $\vect{x}, \vect{y} \ne \vect{0}$. Let $\lambda \in \R$ and $f(\lambda) = \sum_{i=1}^{n}(\lambda x_i + y_i)^2 \ge 0$. Thus,
$$f(\lambda) = \lambda^2\Bigl(\sum_{i=1}^{n} x_i^2\Bigr) + 2\lambda\Bigl(\sum_{i=1}^{n} x_iy_i\Bigr) + [\text{crossed out}]\sum_{i=1}^{n} y_i^2$$
This is a quadratic in $\lambda$. As $f$ is non-negative, the discriminant is $\le 0$. Thus,
$$\Bigl(2\sum_{i=1}^{n} x_iy_i\Bigr)^2 - 4\sum_{i=1}^{n} x_i^2\sum_{i=1}^{n} y_i^2 \le 0.$$
and the result follows.

**Def.** [a theorem] Let $\vect{x}, \vect{y} \in \R^n$. Then $\norm{\vect{x} + \vect{y}} \le \norm{\vect{x}} + \norm{\vect{y}}$.

**P.**
$$\norm{\vect{x} + \vect{y}}^2 = \norm{\vect{x}}^2 + 2\inner{\vect{x}, \vect{y}} + \norm{\vect{y}}^2 \le \norm{\vect{x}}^2 + 2\abs{\inner{\vect{x}, \vect{y}}} + \norm{\vect{y}}^2 \le \norm{\vect{x}}^2 + 2\norm{\vect{x}}\norm{\vect{y}} + \norm{\vect{y}}^2 = (\norm{\vect{x}} + \norm{\vect{y}})^2$$
and the result follows.
(vectors are underlined in the notes: $\underline{x}$; transcribed with `\vect`.)

## HW2400 088 · `20261121_231129.jpg` · Limits of vector functions

**Def.** Let $f : \Omega \to \R^n$ be a function. Then we can rewrite each $f$ by $f = (f_1, f_2, \dots, f_n)\T$, where $f_i : \Omega \to \R$, $f_i(\vect{x}) = \inner{f(\vect{x}), \vect{e}_i}$.

**Def.** Suppose $\Omega \subseteq \R^n$. Then the point $\vect{a} \in \R^n$ is a limit point of $\Omega$ if $\forall \varepsilon > 0$, $\exists \vect{y} \in \Omega$: $0 < \abs{\vect{y} - \vect{a}} < \varepsilon$.

**Def.** We generalise the concept of intervals to $n$ dimensions. Let $\vect{a} \in \R^n$. Then the open $r$-ball of $\vect{a}$ is defined by $B_r(\vect{a}) = \{\vect{x} \in \R^n : \abs{\vect{x} - \vect{a}} < r\}$. The closed $r$-ball of $\vect{a}$ is defined by $\bar{B}_r(\vect{a}) = \{\vect{x} \in \R^n : \abs{\vect{x} - \vect{a}} \le r\}$.

**Def.** Let $f : \Omega \to \R^m$ be a function. Let $\vect{x}_0$ be a limit point of $\Omega$. Let $\vect{y}_0 \in \R^m$. Then $\lim_{\vect{x} \to \vect{x}_0} f(\vect{x}_0) = \vect{y}_0$ if $\forall \varepsilon > 0$, $\exists \delta > 0$: $\vect{x} \in \Omega$, $0 < \abs{\vect{x} - \vect{x}_0} < \delta \implies \abs{f(\vect{x}) - \vect{y}_0} < \varepsilon$.
[possible error: $\lim_{\vect{x} \to \vect{x}_0} f(\vect{x})$, not $f(\vect{x}_0)$]

**Rem.** This is equivalent to the following statement: $\forall \varepsilon > 0$, $\exists \delta > 0$: $\vect{x} \in \Omega$ and $\abs{\vect{x} - \vect{x}_0} < \delta \implies \abs{f(\vect{x}) - f(\vect{x}_0)} < \varepsilon$.
[possible error: this is the definition of continuity at $\vect{x}_0$ (with $\vect{y}_0 = f(\vect{x}_0)$), not an equivalent form of the limit]

**Def.** [a theorem] If the limit exists, it is unique.

**P.** Fix $\varepsilon > 0$. Choose $\delta_1, \delta_2$:
$0 < \abs{\vect{x} - \vect{a}} < \delta_1 \implies \abs{f(\vect{x}) - L_1} < \varepsilon/2$
$0 < \abs{\vect{x} - \vect{a}} < \delta_2 \implies \abs{f(\vect{x}) - L_2} < \varepsilon/2$
Let $\delta = \min\{\delta_1, \delta_2\}$. Then
$$\abs{L_1 - L_2} = \abs{L_1 - f(\vect{x}) + f(\vect{x}) - L_2} \le \abs{L_1 - f(\vect{x})} + \abs{f(\vect{x}) - L_2} < \varepsilon/2 + \varepsilon/2 = \varepsilon. \implies L_1 = L_2.$$

## HW2400 089 · `20261121_231135.jpg` · Limits of vector functions (cont.)

**Def.** [a theorem] Suppose that $\Omega \subseteq \R^n$ and $f, g : \Omega \to \R^m$, $c \in \R$ and let $\vect{a}$ be a limit point of $\Omega$. If $\lim_{\vect{x} \to \vect{a}} f(\vect{x})$ and $\lim_{\vect{x} \to \vect{a}} g(\vect{x})$ exist, then
(1) $\lim_{\vect{x} \to \vect{a}}(f + g)(\vect{x}) = \lim_{\vect{x} \to \vect{a}} f(\vect{x}) + \lim_{\vect{x} \to \vect{a}} g(\vect{x})$
(2) $\lim_{\vect{x} \to \vect{a}}(cf)(\vect{x}) = c\lim_{\vect{x} \to \vect{a}} f(\vect{x})$

**P.** Similar to single-variable case, exercise.

**Def.** [a theorem] Squeeze theorem. Suppose that $\Omega \subseteq \R^n$, $f, g, h : \Omega \to \R$, and let $\vect{a}$ be a limit point of $\Omega$. Let $f(\vect{x}) \le g(\vect{x}) \le h(\vect{x})$ $\forall \vect{x}$ on some $\delta_1$-ball of $\vect{a} \in \Omega$. If the limits of $f$ and $h$ exist, the limit of $g$ exists and the limits are shared. [possible error: the limits of $f$ and $h$ must be equal]

**P.** Fix $\varepsilon > 0$. Choose $\delta_2$: $\forall \vect{x} \in [B_{\delta_2}(\vect{a}) \setminus \{\vect{a}\}] \cap \Omega$, $\abs{f(\vect{x}) - L} < \varepsilon$ and [crossed out] $\abs{h(\vect{x}) - L} < \varepsilon$.
Choose $\delta = \min\{\delta_1, \delta_2\}$. If $\vect{x} \in [B_\delta(\vect{a}) \setminus \{\vect{a}\}] \cap \Omega$,
$$f(\vect{x}) \le g(\vect{x}) \le h(\vect{x}) \implies f(\vect{x}) - L \le g(\vect{x}) - L \le h(\vect{x}) - L \implies -\varepsilon \le g(\vect{x}) - L \le \varepsilon \implies \abs{g(\vect{x}) - L} < \varepsilon.$$
[the middle line should have strict inequalities $-\varepsilon < \dots < \varepsilon$]

**Def.** [a theorem] The function $f : \Omega \subseteq \R^n \to \R^m$ satisfies $\lim_{\vect{x} \to \vect{x}_0} f(\vect{x}) = \vect{b} = (b_1, b_2, \dots, b_m)\T$ iff $\lim_{\vect{x} \to \vect{x}_0} f_i(\vect{x}) = b_i$.

**P.** Suppose $\lim_{\vect{x} \to \vect{x}_0} f(\vect{x}) = \vect{b}$. Thus $\forall \varepsilon > 0$, $\exists \delta > 0$: if $\vect{x} \in \Omega$ and $0 < \abs{\vect{x} - \vect{x}_0} < \delta \implies \abs{f(\vect{x}) - \vect{b}} < \varepsilon$. Let $\vect{x} \in \Omega$ and $0 < \abs{\vect{x} - \vect{x}_0} < \delta$. Then,
$$\abs{f_i(\vect{x}) - b_i} = \sqrt{(f_i(\vect{x}) - b_i)^2} \le \sqrt{\textstyle\sum_{j=1}^{n}(f_j(\vect{x}) - b_j)^2} = \norm{f(\vect{x}) - \vect{b}} < \varepsilon.$$
[the sum runs to $m$]

## HW2400 090 · `20261121_231139.jpg` · Limits of vector functions (examples)

**P.** (cont.) We now prove in the reverse direction. Suppose $\lim_{\vect{x} \to \vect{x}_0} f_i(\vect{x}) = b_i$. Fix $\varepsilon > 0$. For all $i$, $\exists \delta_i > 0$: $\vect{x} \in \Omega$ and $0 < \abs{\vect{x} - \vect{x}_0} < \delta_i \implies \abs{f_i(\vect{x}) - b_i} < \varepsilon/\sqrt{m}$.
Choose $\delta = \min\{\delta_i\}$. Then if $\vect{x} \in \Omega$ and $0 < \abs{\vect{x} - \vect{x}_0} < \delta$ (a blot after $\delta$),
$$\norm{f(\vect{x}) - \vect{b}}^2 = \sum_i \abs{f_i(\vect{x}) - b_i}^2 < m\varepsilon^2 \cdot \Bigl(\frac{1}{\sqrt{m}}\Bigr)^2 = \varepsilon.$$
which implies the result. [possible error: the right-hand side is $\varepsilon^2$, giving $\norm{f(\vect x) - \vect b} < \varepsilon$]

**Ex.** Consider $f : \R^2 \setminus \{\vect{0}\} \to \R$, $f(x, y) = \dfrac{xy}{\sqrt{x^2 + y^2}}$. Show the limit $(x, y) \to (0, 0)$ exists.

**P.** Fix $\varepsilon > 0$. We must find $\delta > 0$: $0 < \norm{(x, y)} < \delta \implies \abs{f(x, y) - L} < \varepsilon$.
Consider $(x, y)$: $\norm{(x, y)} = \sqrt{x^2 + y^2} < \delta$. Note that $(\abs{x} - \abs{y})^2 \ge 0 \implies \abs{x}\abs{y} \le \frac12(x^2 + y^2)$. Thus,
$$\Bigl\lvert \frac{xy}{\sqrt{x^2 + y^2}} \Bigr\rvert = \frac{\abs{xy}}{\sqrt{x^2 + y^2}} \le \frac{x^2 + y^2}{2\sqrt{x^2 + y^2}} = \frac12\sqrt{x^2 + y^2} < \frac{\delta}{2}.$$
Choose $\delta = 2\varepsilon$. Thus $\lim_{(x,y) \to (0,0)} f(x, y) = 0$.

**Ex.** Consider $f : \R^2 \setminus \{\vect{0}\} \to \R$, $f(x, y) = \dfrac{xy^2}{x^2 + y^2}$. Does the limit $(x, y) \to (0, 0)$ exist?

**P.** Yes. We can simplify:
$$\abs{f(x, y) - 0} = \Bigl\lvert \frac{xy^2}{x^2 + y^2} \Bigr\rvert = \abs{x}\frac{y^2}{x^2 + y^2} \le \abs{x}.$$
Note: $\abs{x} = \sqrt{x^2} \le \sqrt{x^2 + y^2} < \delta$. Choose $\delta = \varepsilon$. The result follows, and $\lim_{(x,y) \to (0,0)} f(x, y) = 0$.

## HW2400 091 · `20261121_231145.jpg` · Limit composition, two-path rule

**Def.** [a theorem] Let $f : \Omega \subseteq \R^n \to \R^m$ be continuous at $\vect{a} \in \Omega$. Let $g : U \subseteq \R^p \to \Omega$ satisfy $\lim_{\vect{t} \to \vect{h}} g(\vect{t}) = \vect{a}$. Then,
$$\lim_{\vect{t} \to \vect{h}}(f \circ g)(\vect{t}) = f\Bigl(\lim_{\vect{t} \to \vect{h}} g(\vect{t})\Bigr) = f(\vect{a}).$$

**P.** Fix $\varepsilon > 0$. As $f$ is continuous on $\vect{a}$, $\exists \Delta > 0$: $\vect{h} \in \Omega$ and $\abs{\vect{a} - \vect{h}} < \Delta \implies \abs{f(\vect{a}) - f(\vect{h})} < \varepsilon$.
Also, $\exists \delta > 0$: $\vect{t} \in U$ and $0 < \abs{\vect{t} - \vect{h}} < \delta \implies \abs{g(\vect{t}) - \vect{a}} < \Delta$.
Combining the two inequalities:
$$0 < \abs{\vect{t} - \vect{h}} < \delta \implies \abs{g(\vect{t}) - \vect{a}} < \Delta \implies \abs{f(g(\vect{t})) - f(\vect{a})} < \varepsilon$$
and the result follows. [the letter $\vect{h}$ is used both for the limit point of $g$ and as a dummy point in the continuity of $f$]

**Def.** [a theorem (two-path rule)] Let $T : \Omega \subseteq \R^n \to \R^m$. Suppose $\mu, \eta : U \subseteq \R \to \Omega$, such that $\lim_{t \to h} \mu(t) = \lim_{t \to h} \eta(t) = \vect{a}$, if $\mu(t), \eta(t) \ne \vect{a}$ for $t \ne h$. If $\lim_{t \to h} T(\mu(t)) \ne \lim_{t \to h} T(\eta(t))$, $T$ has no limit at $\vect{a}$.

**P.** Suppose for contradiction that $\lim_{\vect{h} \to \vect{a}} T(\vect{h}) = \vect{L}$. Define $\bar T$ by
$$\bar T(\vect{h}) = \begin{cases} T(\vect{h}) & \text{if } \vect{h} \ne \vect{a}\\ \vect{L} & \text{if } \vect{h} = \vect{a}\end{cases}$$
Thus $\bar T$ is continuous at $\vect{a}$. If $t \ne h$, $\mu(t) \ne \vect{a}$, implying $\bar T(\mu(t)) = T(\mu(t))$. Hence
$$\lim_{t \to h} T(\mu(t)) = \lim_{t \to h} \bar T(\mu(t)) = \bar T\Bigl(\lim_{t \to h} \mu(t)\Bigr) = \bar T(\vect{a}) = \vect{L}$$
Similarly $\lim_{t \to h} T(\eta(t)) = \vect{L}$. Taking the contrapositive provides the statement.

## HW2400 092 · `20261121_231149.jpg` · Multivariate differentiation

**Ex.** Let $f(x, y, z) = \dfrac{xy + y^2 + zx}{x^2 + y^2 + z^2}$. Does $(x, y, z) \to (0, 0, 0)$ exist?

**P.** Choose path 1: $y = z = 0 \implies \lim_{x \to 0} 0 = 0$. Choose path 2: $x = y = z \implies \lim_{t \to 0} \frac{3t^2}{3t^2} = 1$. ↯ [so the limit does not exist]

**Def.** [a theorem] Let $T \in M_{m \times n}$. $\exists M > 0$: $\abs{T\vect{h}} \le M\abs{\vect{h}}$ for $\vect{h} \in \R^n$.

**P.**
$$\Bigl\lVert T\Bigl(\frac{\vect{h}}{\abs{\vect{h}}}\Bigr) \Bigr\rVert = \Bigl\lVert T\Bigl(\sum_{i=1}^{n} \frac{h_i}{\norm{\vect{h}}}\vect{e}_i\Bigr) \Bigr\rVert = \Bigl\lVert \sum_{i=1}^{n} \frac{h_i}{\norm{\vect{h}}}T(\vect{e}_i) \Bigr\rVert \le \Bigl\lVert \frac{h_i}{\norm{\vect{h}}}T(\vect{e}_i) \Bigr\rVert\sum_{i=1}^{n} = \sum_{i=1}^{n} \frac{\abs{h_i}}{\norm{\vect{h}}}\norm{T(\vect{e}_i)} \le \sum_{i=1}^{n} \norm{T(\vect{e}_i)}$$
Choose $K = \max\{T(\vect{e}_i)\}$. Then, let $M = nK$:
$$\Bigl\lVert T\Bigl(\frac{\vect{h}}{\abs{\vect{h}}}\Bigr) \Bigr\rVert \le M \implies \frac{1}{\norm{\vect{h}}}\norm{T(\vect{h})} \le M\norm{\vect{h}}$$
[possible error: the third expression misplaces the sum (it should be $\le \sum_i \norm{\frac{h_i}{\norm{\vect h}}T(\vect e_i)}$); $K = \max_i \norm{T(\vect{e}_i)}$; the last line should read $\norm{T(\vect{h})} \le M\norm{\vect{h}}$; $\vect{h} \ne \vect{0}$ is needed to divide]

## HW2400 093 · `20261121_231155.jpg` · Differentiability

**Def.** Let $\vect{a} \in \Omega \subseteq \R^n$. A function $f : \Omega \to \R^m$ is differentiable at $\vect{a}$ iff $\exists J \in M_{m \times n}$:
$$\lim_{\vect{h} \to \vect{0}} \frac{\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - J\vect{h}}}{\abs{\vect{h}}} = 0.$$

**Rem.** In other words, $f$ is differentiable at $\vect{a}$ if there is a linear transformation $y(\vect{a} + \vect{h}) = f(\vect{a}) + f'(\vect{a})\vect{h}$ such that $f(\vect{a} + \vect{h}) - y(\vect{a} + \vect{h})$ goes to $\vect{0}$ faster than $\vect{h}$ goes to $\vect{0}$. Define $J = f'(\vect{a}) \equiv Df(\vect{a})$.
[$y$ is affine, not linear]

**Rem.** Note that $\Omega \subseteq \R^n$ is open – $\forall \vect{x} \in \Omega$, $\exists \delta > 0$: $\abs{\vect{x} - \vect{y}} < \delta \implies \vect{y} \in \Omega$. In other words, no points exist on the boundary of $\Omega$. [read: "Recall that $\Omega$ is open if …"; "no points of $\Omega$ lie on its boundary"]

**Rem.** Note that for small $\abs{\vect{h}}$, $\vect{a} + \vect{h} \in \Omega$ as $\vect{a}$ is $\in$ open $\Omega$.

**Def.** If $f$ is differentiable $\forall \vect{x} \in \Omega$, we say that $f$ is differentiable on $\Omega$ (or simply differentiable).

**Ex.** Let $f : \R^n \to \R^m$, $f(\vect{x}) = B\vect{x}$ where $B \in M_{m \times n}$. Then $f$ is differentiable, and $f'(\vect{x}) = B$.

**P.** By the definition of differentiability,
$$\frac{\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - B\vect{h}}}{\abs{\vect{h}}} = \frac{\abs{B\vect{a} + B\vect{h} - B\vect{a} - B\vect{h}}}{\abs{\vect{h}}} = \frac{\abs{\vect{0}}}{\abs{\vect{h}}} = 0.$$
Thus $\lim_{\vect{h} \to \vect{0}} \frac{\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - B\vect{h}}}{\abs{\vect{h}}} = 0$.

## HW2400 094 · `20261121_231159.jpg` · Differentiable implies continuous

**Def.** [a theorem] Let $\Omega \subseteq \R^n$ be open. Let $f : \Omega \to \R^m$ be differentiable at $\vect{a}$. Then $f$ is continuous at $\vect{a}$.

**P.** We wish to show $\vect{a} + \vect{h} \in \Omega$ and $\abs{\vect{h}} < \delta \implies \abs{f(\vect{a} + \vect{h}) - f(\vect{a})} < \varepsilon$.
Fix $\varepsilon > 0$. As $f$ is diff. at $\vect{a}$, $\exists J \in M_{m \times n}$: $\lim_{\vect{h} \to \vect{0}} \frac{\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - J\vect{h}}}{\abs{\vect{h}}} = 0$.
Let $\varepsilon' = 1$. There exists $\delta'$: $0 < \norm{\vect{h}} < \delta'$, then
$$\frac{\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - J\vect{h}}}{\abs{\vect{h}}} < 1 \implies \abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - J\vect{h}} < \abs{\vect{h}}$$
$$\implies \abs{f(\vect{a} + \vect{h}) - f(\vect{a})} = \abs{f(\vect{a} + \vect{h}) - f(\vect{a}) + J\vect{h} - J\vect{h}} \le \abs{f(\vect{a} + \vect{h}) - f(\vect{a}) + J\vect{h}} + \abs{J\vect{h}} < \abs{\vect{h}} + \abs{J\vect{h}} < \abs{\vect{h}} + M\abs{\vect{h}} \quad (\text{lemma})$$
Take $\delta = \min\{\delta', \frac{\varepsilon}{1 + M}\}$. If $\abs{\vect{h}} < \delta$, then $\abs{f(\vect{a} + \vect{h}) - f(\vect{a})} < (1 + M)\frac{\varepsilon}{1 + M} = \varepsilon$.
[possible error: the first term in the triangle-inequality line should be $\abs{f(\vect{a} + \vect{h}) - f(\vect{a}) - J\vect{h}}$; "$< \abs{\vect h} + M\abs{\vect h}$" should be "$\le$"; "lemma" = HW 092 ($\abs{T\vect h} \le M\abs{\vect h}$)]

## HW2400 095 · `20261121_231205.jpg` · Partial derivatives, Jacobian

**Def.** Let $\Omega \subseteq \R^n$ be open. Consider the function $f : \Omega \to \R^m$ with components $f = (f_1, f_2, \dots, f_m)\T$. Let $\vect{x} \in \Omega$, let $i = 1, \dots, m$ and $j = 1, \dots, n$. The partial derivative of $f_i$ with respect to $x_j$ is
$$\frac{\partial f_i}{\partial x_j}(\vect{x}) = \lim_{t \to 0} \frac{f_i(\vect{x} + t\vect{e}_j) - f_i(\vect{x})}{t}.$$

**Rem.** Writing $f_i(x_1, \dots, x_n)$ in place of $f_i(\vect{x})$, we see that $\partial f_i/\partial x_j$ is the derivative of $f_i$ w.r.t. $x_j$, keeping the other variables fixed.

**Def.** Define $f : \Omega \to \R^m$ by $f = (f_1, f_2, \dots, f_m)\T$. If all partial derivatives $\partial f_i/\partial x_j(\vect{x})$ exist, the Jacobian matrix of $f$ is defined by
$$J_f(\vect{x}) = \begin{bmatrix} \partial f_1/\partial x_1 & \partial f_1/\partial x_2 & \cdots & \partial f_1/\partial x_n\\ \partial f_2/\partial x_1 & \partial f_2/\partial x_2 & \cdots & \partial f_2/\partial x_n\\ \vdots & \vdots & \ddots & \vdots\\ \partial f_m/\partial x_1 & \partial f_m/\partial x_2 & \cdots & \partial f_m/\partial x_n\end{bmatrix}$$
The determinant $\abs{J_f(\vect{x})}$ is the Jacobian of $f$. [defined only when $m = n$; not said]

**Def.** [a theorem] Let $\Omega \subseteq \R^n$ be open. Suppose $f : \Omega \to \R^m$ is differentiable at $\vect{a}$. Then all partial derivatives exist and $f'(\vect{a}) = J_f(\vect{a})$.

**Rem.** A corollary is that the matrix $J$ is unique.

## HW2400 096 · `20261121_231209.jpg` · Jacobian proof

**P.** Since $f$ is differentiable at $\vect{a}$, $\exists J \in M_{m \times n}$ and a function $R_{\vect{a}}$ such that if $\vect{a} + \vect{h} \in \Omega$,
$$f(\vect{a} + \vect{h}) = f(\vect{a}) + J\vect{h} + R_{\vect{a}}(\vect{h})\abs{\vect{h}},\qquad \lim_{\vect{h} \to \vect{0}} \abs{R_{\vect{a}}(\vect{h})} = 0$$
WLOG, set $R_{\vect{a}}(\vect{0}) = \vect{0}$. Thus $R_{\vect{a}}$ is continuous at $\vect{0}$.
Let $\vect{h} = t\vect{e}_j$, $t \in \R$. Then,
$$f(\vect{a} + \vect{h}) = f(\vect{a} + t\vect{e}_j) = f(\vect{a}) + Jt\vect{e}_j + R_{\vect{a}}(t\vect{e}_j)\abs{t\vect{e}_j}$$
$$\implies f_i(\vect{a} + t\vect{e}_j) = f_i(\vect{a}) + t\inner{J\vect{e}_j, \vect{e}_i} + \inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}\abs{t\vect{e}_j}$$
$$\implies \frac{f_i(\vect{a} + t\vect{e}_j) - f_i(\vect{a})}{t} = \inner{J\vect{e}_j, \vect{e}_i} + \inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i} \cdot \frac{\abs{t}}{t}$$
By the Cauchy–Schwarz inequality,
$$\inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}\frac{\abs{t}}{t} \le \abs{\inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}} = \abs{\inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}} \le \abs{R_{\vect{a}}(t\vect{e}_j)}\abs{\vect{e}_i} = \abs{R_{\vect{a}}(t\vect{e}_j)}$$
As $\lim_{t \to 0} t\vect{e}_j = \vect{0}$, and $R_{\vect{a}}$ is continuous at $\vect{0}$,
$$\lim_{t \to 0} \abs{R_{\vect{a}}(t\vect{e}_j)} = \abs{R_{\vect{a}}(\lim_{t \to 0} t\vect{e}_j)} = \abs{R_{\vect{a}}(\vect{0})} = 0$$
Thus by the squeeze theorem, $\inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}\frac{\abs{t}}{t} \to 0$. By the definition of partial derivatives,
$$\frac{\partial}{\partial x_j}f_i(\vect{a}) = \lim_{t \to 0}\bigl[\inner{J\vect{e}_j, \vect{e}_i} + \inner{R_{\vect{a}}(t\vect{e}_j), \vect{e}_i}\bigr] = \inner{J\vect{e}_j, \vect{e}_i}$$
It can be shown using linear algebra that $\inner{J\vect{e}_j, \vect{e}_i} = J_{i,j}$.
[the last-but-one display drops the factor $\abs{t}/t$; the squeeze needs the absolute value of the term, i.e. $0 \le \abs{\cdot} \le \abs{R_{\vect a}(t\vect e_j)}$]

## HW2400 097 · `20261121_231216.jpg` · Partial derivatives vs. differentiability

**Ex.** The Jacobian can exist even if the function is not differentiable at a point. As a corollary, the existence of partial derivatives does not guarantee that the function is differentiable.
Consider $f : \R^2 \to \R$, $f(x, y) = \begin{cases} \dfrac{xy}{x^2 + y^2} & (x, y) \ne \vect{0}\\ 0 & (x, y) = \vect{0}\end{cases}$
Then $f_x(0, 0) = \lim_{h \to 0} \frac{f(0, h) - f(0)}{h} = \lim_{h \to 0} \frac{0}{h} = 0 = f_y(0, 0)$
[possible error: $f_x(0, 0)$ uses $f(h, 0)$; by symmetry the value is the same]
We can show $f$ is not differentiable by:
(1) Showing $f$ is not continuous (two-paths)
(2) Definition of multivariable differentiability, show the limit to $\vect{0}$ is not $0$.
(neither is carried out)

**Def.** [a theorem] Let $\Omega \subseteq \R^n$ be open. Let $f : \Omega \to \R^m$ have all partial derivatives $\frac{\partial f_i}{\partial x_j}$ in an open ball around $\vect{a}$. Suppose these partial derivatives are continuous at $\vect{a}$. Then $f$ is differentiable at $\vect{a}$. (stated without proof)

**Def.** Let $\Omega \subseteq \R^n$. We say $f : \Omega \to \R^m$ is continuously differentiable if $f$ is differentiable in $\Omega$ and all partial derivatives are continuous in $\Omega$.

## HW2400 098 · `20261121_231222.jpg` · Multivariate chain rule

**Def.** [a theorem] Let $U \subseteq \R^n$, $V \subseteq \R^m$ both be open, and let $g : U \to V$ be differentiable at $\vect{a} \in U$. Let $f : V \to \R^p$ be differentiable at $g(\vect{a})$. Then $(f \circ g)(\vect{x})$ is differentiable at $\vect{a}$, and $(f \circ g)'(\vect{a}) = f'(g(\vect{a}))g'(\vect{a})$.

**Rem.** Note that $f' \in M_{p \times m}$, $g' \in M_{m \times n}$. Thus $(f \circ g)' \in M_{p \times n}$. This follows from $(f \circ g) : U \to \R^p$.

**P.** Let $\vect{b} := g(\vect{a})$. As $g$ and $f$ are differentiable at $\vect{a}$ and $\vect{b}$ respectively, there exists Jacobian matrices $J_g = g'(\vect{a})$, $J_f = f'(\vect{b})$ such that
$$g(\vect{a} + \vect{h}) = g(\vect{a}) + J_g(\vect{h}) + R_{g,\vect{a}}(\vect{h})\abs{\vect{h}} \quad \text{if } \vect{a} + \vect{h} \in U$$
$$f(\vect{b} + \vect{z}) = f(\vect{b}) + J_f(\vect{z}) + R_{f,\vect{b}}(\vect{z})\abs{\vect{z}} \quad \text{if } \vect{b} + \vect{z} \in V$$
and $\lim_{\vect{h} \to \vect{0}} \abs{R_{g,\vect{a}}(\vect{h})} = \lim_{\vect{z} \to \vect{0}} \abs{R_{f,\vect{b}}(\vect{z})} = 0$. WLOG, let $R_{g,\vect{a}}(\vect{0}) = R_{f,\vect{b}}(\vect{0}) = \vect{0}$.
Define $\vect{k}(\vect{h}) = g(\vect{a} + \vect{h}) - g(\vect{a}) = J_g\vect{h} + R_{g,\vect{a}}(\vect{h})\abs{\vect{h}}$. Then,
$$F(\vect{a} + \vect{h}) = f(g(\vect{a} + \vect{h})) = f(g(\vect{a}) + \vect{k}(\vect{h}))$$
It follows by substitution and manipulation that
$$\frac{F(\vect{a} + \vect{h}) - F(\vect{a}) - J_fJ_g\vect{h}}{\abs{\vect{h}}} = J_fR_{g,\vect{a}}(\vect{h}) + R_{f,\vect{b}}(\vect{k}(\vect{h})) \cdot \frac{\abs{\vect{k}(\vect{h})}}{\abs{\vect{h}}}$$
We need only show that the RHS $\to 0$ as $\vect{h} \to \vect{0}$, which is left as an exercise.
[$F := f \circ g$ is not defined on the page; the second limit is written $\vect{h} \to \vect{0}$; read $\vect{z} \to \vect{0}$]

## HW2400 099 · `20261121_231234.jpg` · General inverse function theorem

**L.** Let $\Omega \subseteq \R^n$ be open. If $f : \Omega \to \R^n$ is continuous and differentiable, and $\det(J_f(\vect{x}_0)) = 0$, then $f^{-1}$ is not differentiable at $f(\vect{x}_0)$.

**P.** Note that $f^{-1}(f(\vect{x})) = \vect{x}$. If $f^{-1}$ were differentiable at $f(\vect{x}_0)$, the multivariate chain rule would imply that:
$$J_{f^{-1}}(f(\vect{x}_0))J_f(\vect{x}_0) = I$$
This implies that $J_{f^{-1}}(f(\vect{x}_0)) = (J_f(\vect{x}_0))^{-1}$, which is a contradiction if $\det(J_f(\vect{x}_0)) = 0$.
[$f$ must be injective for $f^{-1}$ to exist (cf. the one-variable lemma, HW 047)]

**Def.** [a theorem] Let $\Omega \subseteq \R^n$ be open. Consider $f : \Omega \to \R^n$. Suppose $f$ is continuously differentiable at $\vect{x}_0$ and that $f'(\vect{x}_0) = J_f(\vect{x}_0)$ is invertible. Then there exists open sets $U \ni \vect{x}_0$, $V \ni f(\vect{x}_0)$ such that $f|_U : U \to V$ is invertible. Moreover, $f^{-1}$ is differentiable at $f(\vect{x}_0)$ and
$$J_{f^{-1}}(f(\vect{x}_0)) = (J_f(\vect{x}_0))^{-1}$$
[possible error: "continuously differentiable at $\vect{x}_0$" should be "continuously differentiable on $\Omega$" (or near $\vect{x}_0$)]

**Rem.** In other words, the derivative of the inverse is the inverse of the derivative.

**P.** Proof is omitted, see 2401. [MATH2401 typed notes §21.1]

## HW2400 100 · `20261121_231238.jpg` · General inverse function theorem (restated)

**Def.** [a theorem] Let $\Omega \subseteq \R^n$ be open. Consider $f : \Omega \to \R^n$. Suppose that $f$ is continuously differentiable on an open set containing $\vect{x}_0$, and that $f'(\vect{x}_0) = J_f(\vect{x}_0)$ is an invertible matrix. Then there exists open sets $U \ni \vect{x}_0$, $V \ni f(\vect{x}_0)$ such that $f|_U : U \to V$ has a continuous inverse. Moreover, $f^{-1} : V \to U$ is differentiable and
$$J_{f^{-1}}(\vect{y}) = \bigl(J_f(f^{-1}(\vect{y}))\bigr)^{-1} \quad \forall \vect{y} \in V$$
(this corrects the hypothesis of HW 099.)

**Rem.** [blank; the rest of the page is empty]

## HW2400 101 · `20261121_231243.jpg` · Examples of inverse function theorem

**Ex.** Let $f : \R^2 \to \R^2$ be given by $f(x, y) = \begin{pmatrix} e^x\cos y\\ e^x\sin y\end{pmatrix}$. Prove $f$ is locally invertible on $\R^2$.

**P.** We first find the Jacobian of $f$:
$$J_f(\vect{x}) = \begin{pmatrix} \partial f_1/\partial x & \partial f_2/\partial x\\ \partial f_1/\partial y & \partial f_2/\partial y\end{pmatrix}\T = \begin{pmatrix} e^x\cos y & -e^x\sin y\\ e^x\sin y & e^x\cos y\end{pmatrix}$$
Thus, $\abs{J_f(\vect{x})} = e^{2x}\cos^2 y + e^{2x}\sin^2 y = e^{2x}$.
Thus $J_f$ is continuous and $\abs{J_f(\vect{x})} \ne 0$ at every point in $\R^2$. By the inverse function theorem, $f$ is locally invertible at every point.
However, $f$ cannot be globally invertible as it is not injective – take $f(0, 0) = f(0, 2\pi) = (1, 0)\T$.
(checked.)

## HW2400 102 · `20261121_231247.jpg` · Examples of inverse function theorem (cont.)

**Ex.** Define $f : \R^2 \to \R^2$ by $f(x, y) = (x^2y + yx,\ 2xy + xy^2)\T$. Show that $f$ in an open set containing $(1, 1)\T$ has an inverse $f^{-1}$ defined in an open set containing $(2, 3)\T$. Hence find the derivative of $f^{-1}$ at $(2, 3)\T$.

**P.** Firstly, note that $f(1, 1) = (2, 3)\T$. We find the Jacobian of $f$:
$$J_f(\vect{x}) = \begin{pmatrix} \partial f_1/\partial x & \partial f_1/\partial y\\ \partial f_2/\partial x & \partial f_2/\partial y\end{pmatrix} = \begin{pmatrix} 2xy + y & x^2 + x\\ 2y + y^2 & 2x + 2xy\end{pmatrix},\qquad J_f(1, 1) = \begin{pmatrix} 3 & 2\\ 3 & 4\end{pmatrix}$$
Thus, $\abs{J_f(\vect{x})} = 12 - 6 = 6 \ne 0$. [read $\abs{J_f(1, 1)}$]
Hence by the inverse function theorem, the function is invertible on an open set containing $(2, 3)\T$.
$$J_{f^{-1}}(2, 3) = \begin{pmatrix} 3 & 2\\ 3 & 4\end{pmatrix}^{-1} = \frac16\begin{pmatrix} 4 & -2\\ -3 & 3\end{pmatrix}.$$
(checked: $f(1,1) = (2,3)$, $J_f(1,1)$, determinant and inverse are correct. "The function is invertible on an open set containing $(2,3)$" should be "$f^{-1}$ is defined on …")
