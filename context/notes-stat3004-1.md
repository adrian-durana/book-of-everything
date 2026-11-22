# STAT3004 Probability Models & Stochastic Processes: transcription, part 1 of 3 (HW 01–16)

_Transcription phase. Nothing here is book text yet. No dates are recorded (the typed notes carry "Version" dates on each topic; they are omitted); only the semester would be given if a source needed identifying._

## Sources (all three parts)
| Code | Source | Role | Where transcribed |
|---|---|---|---|
| **HW nn** | 32 photos of the handwritten notes (`stat3004.zip`), one notebook page per photo, numbered in shooting order (file name under each heading). They cover **Topic 1 only** (probabilistic measure theory: algebra of sets → σ-algebras → probability measures → Lebesgue measure → Borel–Cantelli → random variables, distributions, random vectors → expectation and LOTUS → modes of convergence, Lévy → MCT, Fatou, DCT → LLN, CLT). | **Main source, Topic 1** | Parts 1–2, in full |
| **CN** | *STAT3004/7304: Probability Models and Stochastic Processes, Lecture Notes*, typed, 99 pp., six topics: 1 Probabilistic measure theory (pp. 5–19), 2 Discrete-time branching processes (19–25), 3 Random walks (25–34), 4 DTMCs (34–55), 5 Poisson processes and extensions (55–69), 6 CTMCs (69–99). | Supplement for Topic 1; **main source for Topics 2–6** | Part 3: section/page index, figures, content found only here |
| **CG** | *Course guide* ("Probability Models and Stochastic Processes … An intuitive guide, from beginning to end", 33 pp.), a study guide "built only from the course notes (Topics 1–6)": key ideas, exam recipes ("How to answer it"), worked examples, common traps, checklists. Theorem numbers refer to CN. | Secondary (derived from CN) | Part 3: index, its figures, the little that is not in CN |

Page counts: HW 32 pages; CN 99 pp. (printed page = PDF page); CG 33 pp.

**Which source leads where (user's instruction):** the handwritten notes are the main source for Topic 1, with CN as a supplement; CN is the source for Topics 2–6 (no handwritten notes exist for them).

## Legibility check (HW photos)
All 32 photos were read in order at full resolution (4000 × 3000, rotated upright); every doubtful spot was re-checked on a zoomed crop. **No retakes are needed.** Every photo has the usual broad diagonal shadow, but the ink is readable through it on every page; no page is cut off, and none is too dark. The softest photos (HW 11, 16, 32; lowest sharpness scores) still read cleanly, including the indices in HW 11's proof.

Content that can't be read is in the notebook itself (hatched cross-outs), so a retake won't help. None of it carries content the surrounding text doesn't already give:
- **HW 04** one word crossed out before "σ-algebras" in the intersection theorem.
- **HW 09** a crossed-out symbol at the start of the "$A_n$ infinitely often iff …" theorem.
- **HW 10** a hatched blot inside property (i), between "$\ge$" and "limsup".
- **HW 15** a whole line of text hatched out after "$\forall B \in \mathcal B(\R^d)$".
- **HW 17** one word crossed out ("decreasing" written above it) and one word after "(non-negative)".
- **HW 26** one word blotted before "$X_n \convd X$" (presumably "then").
- **HW 27** a crossed-out margin label before "N.".
- **HW 29** a blot between "$\le$" and "$\E$" in reverse Fatou, and one full hatched line in its proof.
- **HW 30** the two "$\E[X_n]$" in the last line are written below blots.

Genuinely ambiguous glyphs (in the notebook, a retake won't help), each resolved in brackets where it occurs:
- **HW 07** the "$\le$" in monotonicity looks like "$\subseteq$".
- **HW 10** the side note "else $\# < n < \infty$".
- **HW 13** "$X^{-1}(\{-1\})$": the short stroke before 1 may be a stray mark; $\{1\}$ is meant.
- **HW 19** the convex function is written with a $\gamma$/r-like glyph (once clearly $\varphi$).
- **HW 26** "$\sin(n+)$" (the $t$ looks like "+").

## Conventions
Wording, structure and labels (Def., Th., P. = proof, Ex., Rem., N. = note) follow the notes. Maths uses `notation.tex` macros (`\Prob`, `\E`, `\Var`, `\ind`, `\iid`, `\convp`, `\convd`, `\convas`, `\powerset`, `\Normal`, `\Bern`, `\Unif`, `\vect`, …). The notes write indicators as $I_A$ and convergence in probability as $\xrightarrow{\Prob}$; these are kept as written in the transcription (the book uses `\ind` and `\convp`). Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic re-computed where marked "Checked"); `[illegible]`/"[blotted]" marks unreadable text. "Not in CN" marks handwritten content that the typed notes don't have. Figures are described in enough detail to redraw in TikZ.

**This part:** sets, σ-algebras, generated and Borel σ-algebras, probability measures and continuity, Lebesgue measure, limsup/liminf and the Borel–Cantelli lemmas, random variables, distributions and cdfs, random vectors.

---

### HW 01 (`20261122_011924.jpg`): Algebra of sets (1)

**Algebra of sets**

**Def.** Let $\Omega$ denote the universal set / sample space.

**Ex.**
$$
\left.\begin{aligned}
\Omega &= \{H, T\}\\
\Omega &= \{1,2,3,4,5,6\}\\
\Omega &= \begin{Bmatrix} (1,1), & (1,2), & \cdots, & (1,6)\\ (2,1) & & \ddots & \vdots\\ \vdots & & & \\ (6,1) & & \cdots & (6,6) \end{Bmatrix}
\end{aligned}\right\}\ \abs{\Omega} < \infty
\qquad
\left.\begin{aligned}
\Omega &= [0,1]\\
\Omega &= \R
\end{aligned}\right\}\ \abs{\Omega} = \infty
$$
[Layout: the five sample spaces are listed down the left; a large brace groups the first three with "$\abs{\Omega} < \infty$", a smaller brace groups the last two with "$\abs{\Omega} = \infty$". The $6\times 6$ array of dice pairs is written as a grid with corner entries $(1,1)$, $(1,6)$, $(6,1)$, $(6,6)$ and dots.]

**Def.** Subsets / events
$A \subseteq \Omega$ if $\omega \in A \implies \omega \in \Omega$.

**Def.** Basic operations
Let $A, B \subseteq \Omega$. Then
$$
\begin{aligned}
A \cup B &:= \{\omega \in \Omega : \omega \in A \text{ or } \omega \in B\}\\
A \cap B &:= \{\omega \in \Omega : \omega \in A \text{ and } \omega \in B\}\\
A^c &:= \{\omega \in \Omega : \omega \notin A\}\\
A \setminus B &:= A \cap B^c = \{\omega \in A : \omega \notin B\}
\end{aligned}
$$

**Def.** Empty set $\emptyset$
$\emptyset \subseteq A$ for all $A \subseteq \Omega$, and $\emptyset^c = \Omega$; $\Omega^c = \emptyset$.

**Def.** Countable unions and intersections
For a sequence $A_1, A_2, \dots \subseteq \Omega$,
$$
\bigcup_{n=1}^\infty A_n := \{\omega \in \Omega : \omega \in A_n \text{ for some } n \in \N\}, \qquad
\bigcap_{n=1}^\infty A_n := \{\omega \in \Omega : \omega \in A_n \text{ for all } n \in \N\}.
$$
Finite unions / intersections are defined similarly for $n \le N$.

*Figure:* none.

---

### HW 02 (`20261122_011928.jpg`): Algebra of sets (2)

**Algebra of sets**

**Def.** De Morgan's laws
If $A_1, A_2, \dots \subseteq \Omega$,
$$\Bigl(\bigcap_{n=1}^\infty A_n\Bigr)^c = \bigcup_{n=1}^\infty A_n^c \quad\text{and}\quad \Bigl(\bigcup_{n=1}^\infty A_n\Bigr)^c = \bigcap_{n=1}^\infty A_n^c$$
[Labelled "Def." in the margin; CN Prop 1.1.4 states it as a proposition.]

**Def.** Disjoint sets
The sets $A, B$ are disjoint if $A \cap B = \emptyset$.
A sequence $A_1, A_2, \dots$ is mutually disjoint if $A_i \cap A_j = \emptyset$ for $i \ne j$.

**Rem.** If a sequence $A_1, A_2, \dots$ is disjoint, we denote
$$\bigcup_n A_n \;\to\; \bigsqcup_n A_n$$
[The arrow means "we write the union as" $\bigsqcup$; CN Def 1.1.6 uses $\bigsqcup$ as well.]

**Def.** Partition of sets
A collection of sets $A_1, \dots \subseteq \Omega$ forms a partition of $\Omega$ if they are mutually disjoint and $\bigcup_n A_n = \Omega$.
i.e. every $\omega \in \Omega$ belongs to only one $A_n \in \Omega$.
[possible error: "$A_n \in \Omega$" should be "$A_n \subseteq \Omega$" (or just "one $A_n$"); CN Def 1.1.7: "belongs to exactly one $A_n$".]

**Def.** Increasing and decreasing sequences of sets
A sequence of sets $A_1, A_2, \dots \subseteq \Omega$ is
- ↳ increasing ($A_n \uparrow$) if $A_n \subseteq A_{n+1}$, $\quad \lim_{n\to\infty} A_n := \bigcup_{n=1}^\infty A_n$
- ↳ decreasing ($A_n \downarrow$) if $A_n \supseteq A_{n+1}$, $\quad \lim_{n\to\infty} A_n := \bigcap_{n=1}^\infty A_n$

**Def.** Power set
For a set $\Omega$, the power set is the set of all subsets of $\Omega$
i.e. $\powerset(\Omega) := \{A : A \subseteq \Omega\}$
If $\abs{\Omega} = n$, $\abs{\powerset(\Omega)} = 2^n$

**Ex.** Let $\Omega = \{0,1,2\}$. Then
$$\powerset(\Omega) = \bigl\{\emptyset, \{0\}, \{1\}, \{2\}, \{0,1\}, \{0,2\}, \{1,2\}, \Omega\bigr\}$$

*Figure:* none.

---

### HW 03 (`20261122_011934.jpg`): σ-algebras (1)

**σ-algebras**

**Def.** Algebras (of sets)
A collection of events on $\Omega$, $\mathcal F$, is an algebra on $\Omega$ if
- (i) $\Omega \in \mathcal F$
- (ii) $A \in \mathcal F \implies A^c \in \mathcal F$ (closed under complements)
- (iii) $A, B \in \mathcal F \implies A \cup B \in \mathcal F$ (closed under unions)

**Ex.** Let $\Omega = \{H, T\}$.
$$
\underset{\text{not an algebra}}{\{\Omega\}} \;\rightsquigarrow\; \underset{\text{algebra}}{\{\emptyset, \Omega\}}
\qquad\qquad
\bigl\{\{H\}\bigr\} \;\rightsquigarrow\; \bigl\{\{H\}, \Omega\bigr\} \;\rightsquigarrow\; \bigl\{\emptyset, \{H\}, \{T\}, \Omega\bigr\}
$$
[The squiggly arrows (↝) show a collection being enlarged step by step until it is an algebra: $\{\Omega\}$ is "not an algebra", $\{\emptyset,\Omega\}$ is labelled "algebra". The intermediate $\{\{H\},\Omega\}$ is unlabelled. Not in CN.]

**Rem.** It follows that algebras are closed under intersections:
$$
\begin{array}{ccc}
A, B \in \mathcal F & \Longrightarrow & A \cap B \in \mathcal F\\
\big\downarrow \text{(ii)} & & \big\uparrow \text{(ii)}\\
A^c, B^c \in \mathcal F & \xrightarrow{\text{(iii)}} & (A^c \cup B^c) \in \mathcal F
\end{array}
$$
*Figure (commutative square):* four nodes at the corners of a rectangle. Top left "$A,B \in \mathcal F$", top right "$A \cap B \in \mathcal F$", joined by a double arrow $\Rightarrow$ left to right. A down-arrow labelled "(ii)" from top left to bottom left "$A^c, B^c \in \mathcal F$". A right arrow labelled "(iii)" (label above the arrow) from bottom left to bottom right "$(A^c \cup B^c) \in \mathcal F$". An up-arrow labelled "(ii)" from bottom right to top right. [The up-arrow step uses (ii) together with De Morgan: $(A^c \cup B^c)^c = A \cap B$; De Morgan is not named on the page.]

**Rem.** Note that algebras can be too small to be useful in probability, as we need only be closed under finite unions.
e.g. Suppose we have Bernoulli trials. Let
$$A_n = \{\text{event that first success occurs in trial } n\}$$
Then the event that success occurs (eventually) is $A = \bigcup_{n=1}^\infty A_n$.
[Not in CN (CN has no such motivating example).]

**Def.** A collection $\mathcal F$ is a <u>monotone class</u> if whenever $A_1, \dots \in \mathcal F$ with $A_n \uparrow A$ or $A_n \downarrow A$, the limit $A \in \mathcal F$.
i.e.
$$
\begin{aligned}
A_1, A_2, \dots \in \mathcal F \text{ s.t. } A_1 \subseteq A_2 \subseteq \cdots &\implies A = \bigcup_{n=1}^\infty A_n \in \mathcal F\\
\text{s.t. } A_1 \supseteq A_2 \supseteq \cdots &\implies A = \bigcap_{n=1}^\infty A_n \in \mathcal F
\end{aligned}
$$
[The second $\supseteq$ is overwritten by a small boxed smudge; $\supseteq$ is clear from the first one.]

*Figure:* the commutative square above.

---

### HW 04 (`20261122_011937.jpg`): σ-algebras (2)

**σ-algebras**

**Def.** σ-algebra
A collection $\mathcal F$ is a σ-algebra if it is an algebra that is also closed under countable (not just finite) unions:
- (i) $\Omega \in \mathcal F$
- (ii) $A \in \mathcal F \implies A^c \in \mathcal F$
- (iii) $A_1, A_2, \dots \in \mathcal F \implies \bigcup_{n=1}^\infty A_n \in \mathcal F$

It similarly follows that σ-algebras are closed under countable intersections.

**Th.** A collection $\mathcal F$ is a σ-algebra iff it is both an algebra and monotone class.

**P.** The forward direction is trivial. σ-algebras are algebras by definition, and we can take an increasing / decreasing sequence $A_1, A_2, \dots \in \mathcal F$ which by definition has union / intersection belonging in $\mathcal F$.

The reverse direction follows as so. We need only prove (iii).
Let $A_1, A_2, \dots \in \mathcal F$. As $\mathcal F$ is an algebra, the finite union $B_n := A_1 \cup \dots \cup A_n$ belongs to $\mathcal F$. Thus $B_n$ is an increasing sequence with limit $\bigcup_{i=1}^\infty A_i$.
As $\mathcal F$ is a monotone class, $\bigcup_{i=1}^\infty A_i \in \mathcal F$.

**Ex.** The trivial σ-algebra is $\{\emptyset, \Omega\}$. The largest σ-algebra is $\powerset(\Omega)$, but this is often too large to be 'consistent'.
[The quotes around 'consistent' are in the notes. "Trivial σ-algebra" is not named in CN; CN Rem 1.1.40 gives the reason $\powerset(\R)$ is too large.]

**Ex.** Let $\Omega = \{HH, HT, TH, TT\}$ represent the outcome of flipping a fair coin twice.
- ↳ If we care about every possible outcome, take $\mathcal F = \powerset(\Omega)$.
- ↳ If we only care that the two flips agree, a suitable, smaller σ-algebra is $\mathcal F = \{\emptyset, \Omega, \{HH, TT\}, \{HT, TH\}\}$.

**Th.** If $\{\mathcal F_i\}_{i \in I}$ is any collection of [one word crossed out] σ-algebras on $\Omega$, then
$$\bigcap_{i\in I} \mathcal F_i = \{A \subseteq \Omega : A \in \mathcal F_i,\ \forall i \in I\}$$
is also a σ-algebra on $\Omega$.

**P.**
- (i) $\Omega \in \mathcal F_i$ for all $i \in I$. Thus $\Omega \in \bigcap_i \mathcal F_i$.
- (ii) Let $A \in \mathcal F$. Then $A \in \mathcal F_i$, so $A^c \in \mathcal F_i$. Thus $A^c \in \bigcap_i \mathcal F_i$.
- (iii) Let $A_1, \dots \in \bigcap_i \mathcal F_i$. Then $A_1, \dots \in \mathcal F_i$, so $\bigcup_{n=1}^\infty A_n \in \mathcal F_i$. Thus $\bigcup_{n=1}^\infty A_n \in \bigcap_i \mathcal F_i$.

[possible error: in (ii), "Let $A \in \mathcal F$" should be "Let $A \in \bigcap_i \mathcal F_i$"; "Then $A \in \mathcal F_i$" means for every $i$. The proof is not written out in CN (Rem 1.1.23 calls it "a short, direct exercise"), so this page is the only source of it.]

*Figure:* none.

---

### HW 05 (`20261122_011943.jpg`): Generated σ-algebras (1)

**Generated σ-algebras**

**Def.** Generated σ-algebras
Let $\mathcal A$ be any arbitrary collection of subsets of $\Omega$. Then the σ-algebra generated by $\mathcal A$, denoted $\sigma(\mathcal A)$, is the intersection of all σ-algebras containing $\mathcal A$:
$$\sigma(\mathcal A) = \bigcap\{\mathcal F : \mathcal F \text{ is a σ-algebra on } \Omega,\ \mathcal A \subseteq \mathcal F\}$$
This is also a σ-algebra, as by the last theorem.
[The collection is written with a script letter resembling a looped "$\mathcal A$" (it can look like "$\lambda$" or "$\mathscr{L}$"); CN Def 1.1.24 uses $\mathcal A$.]

**Ex.** Let $\Omega = \{H, T\}$, and let $\mathcal A = \{\{H\}\}$. Then $\sigma(\mathcal A) = \{\{H\}, \Omega, \{T\}, \emptyset\}$.
[Not in CN.]

**Rem.** Generated σ-algebras are the smallest σ-algebras containing $\mathcal A$.

**Def.** Borel σ-algebra on $\R$
The Borel σ-algebra on $\R$, denoted $\mathcal B(\R)$, is the σ-algebra generated by open subsets of $\R$. Equivalently, it is generated by the collection $\{(-\infty, a] : a \in \R\}$.

**Rem.** $\mathcal B(\R)$ can also be generated by $\{(-\infty, a) ; a \in \R\}$. The two generating classes produce each other by a single countable limit:
$$
\begin{aligned}
(-\infty, a] &= \textstyle\bigcap_n (-\infty, a + \tfrac1n)\\
(-\infty, a) &= \textstyle\bigcup_n (-\infty, a - \tfrac1n)
\end{aligned}
$$
and so they generate the same σ-algebra.
[possible error: the second line should use the closed half-lines, $\bigcup_n (-\infty, a - \frac1n]$ (as in CN Rem 1.1.27); as written it builds an open half-line from open half-lines, which doesn't show that the closed class generates the open one.]

**Rem.** $\mathcal B(\R)$ contains sets of the forms $[a,b]$, $[a,b)$, $(a,b)$, $\{b\}$ for all $a < b \in \R$.
[CN Prop 1.1.28 lists $(a,b]$, $(a,b)$, $\{b\}$; the notes have $[a,b]$ and $[a,b)$ instead of $(a,b]$. All are Borel; no proof on either source (CN Rem 1.1.32 leaves it as an exercise; the course guide §1.1 gives the constructions of $(a,b]$, $\{b\}$, $(a,b)$).]

**Rem.** The Borel σ-algebra is enormous, but it is still strictly smaller than the power set of $\R$. In fact,
$$\abs{\mathcal B(\R)} = \abs{\R} \quad\text{but}\quad \abs{\powerset(\R)} > \abs{\R}$$
[Not in CN. Stated without proof.]

*Figure:* none.

---

### HW 06 (`20261122_011948.jpg`): Generated σ-algebras (2)

**Generated σ-algebras**

**Def.** Trace σ-algebras
Let $\mathcal F$ be a σ-algebra on $\Omega$, and let $I \subseteq \Omega$. The trace / restriction of $\mathcal F$ to $I$ is
$$\mathcal F \cap I := \{A \cap I : A \in \mathcal F\}$$
which is itself a σ-algebra on $I$.

**Ex.** Let $\Omega = \{0,1,2\}$, $\mathcal F = \powerset(\Omega)$, $I = \{0,1\}$. Then
$$
\begin{aligned}
\emptyset \cap I &= \emptyset & \{0,1\} \cap I &= \{0,1\}\\
\{0\} \cap I &= \{0\} & \{0,2\} \cap I &= \{0\}\\
\{1\} \cap I &= \{1\} & \{1,2\} \cap I &= \{1\}\\
\{2\} \cap I &= \emptyset & \Omega \cap I &= \{0,1\}
\end{aligned}
$$
and so $\mathcal F \cap I = \{\emptyset, \{0\}, \{1\}, \{0,1\}\} = \powerset(I)$.
[Not in CN. Checked: correct.]

**Ex.** Consider the Borel σ-algebra on $I \subseteq \R$. Then
$$\mathcal B(I) = \mathcal B(\R) \cap I, \qquad \mathcal B([0,1]) = \mathcal B(\R) \cap [0,1]$$

**Def.** Measurable space
A pair $(\Omega, \mathcal F)$, where $\Omega$ is a sample space, and $\mathcal F$ is a σ-algebra on $\Omega$, is called a measurable space.

[The lower third of the page is blank.]

*Figure:* none.

---

### HW 07 (`20261122_011955.jpg`): Probability measure (1)

**Probability measure**

**Def.** A function $\Prob : \mathcal F \to [0,1]$ is a <u>probability measure</u> on $(\Omega, \mathcal F)$ if it satisfies the three Kolmogorov axioms:
- (a) $\Prob(\Omega) = 1$
- (b) $\Prob(A) \ge 0$ for all $A \in \mathcal F$
- (c) countable additivity:
  if $A_1, A_2, \dots$ are mutually disjoint, $\displaystyle \Prob\Bigl(\bigcup_{n=1}^\infty A_n\Bigr) = \sum_{n=1}^\infty \Prob(A_n)$

The triple $(\Omega, \mathcal F, \Prob)$ is called a probability space.
The value $\Prob(A) \in [0,1]$ is called the probability of $A$.

**Th.** Consequences of Kolmogorov axioms (exercise)
- (a) $\Prob(\emptyset) = 0$
- (b) $\Prob(A^c) = 1 - \Prob(A)$
- (c) Monotonicity: $A \subseteq B \implies \Prob(A) \le \Prob(B)$
- (d) $\Prob(A \cup B) = \Prob(A) + \Prob(B) - \Prob(A \cap B)$
- (e) Boole's inequality:
  for any $A_1, \dots \in \mathcal F$ (need not be disjoint), $\displaystyle \Prob\Bigl(\bigcup_{n=1}^\infty A_n\Bigr) \le \sum_{n=1}^\infty \Prob(A_n)$

[(c): the "$\le$" is written with a curled lower stroke that looks like "$\subseteq$"; read as $\le$. (d): the notes give the inclusion–exclusion identity; CN Prop 1.1.36(d) gives finite subadditivity $\Prob(A\cup B) \le \Prob(A)+\Prob(B)$ instead, and proves (a)–(d). Boole's inequality is CN Thm 1.1.37 (proof left as an exercise, Rem 1.1.38).]

**Th.** Continuity of probability measures (exercise)
Let $(\Omega, \mathcal F, \Prob)$ be a probability space. Then
- (a) Continuity from below: if $A_n \uparrow A$, then $\Prob(A_n) \to \Prob(A)$
- (b) Continuity from above: if $A_n \downarrow A$, then $\Prob(A_n) \to \Prob(A)$

Margin note (right, with an arrow pointing down to the statement): "$\lim \Prob(A_n) = \Prob(\lim A_n)$".

**P.**
(a) Let $B_1 = A_1$, $B_n = A_n \setminus A_{n-1}$. These are mutually disjoint with $\bigcup_{k=1}^n B_k = A_n$ and $\bigcup_{n=1}^\infty B_k = A$. By countable additivity:
$$\Prob(A) = \sum_{n=1}^\infty \Prob(B_n) = \lim_{n\to\infty}\sum_{n=1}^{n} \Prob(B_k) = \lim_{n\to\infty} \Prob(A_n)$$
(b) Apply (a) to the increasing sequence $A_n^c \uparrow A^c$: $\Prob(A_n^c) \to \Prob(A^c)$
i.e. $1 - \Prob(A_n) \to 1 - \Prob(A)$, so $\Prob(A_n) \to \Prob(A)$.

[possible error: summation indices are mixed: $\bigcup_{n=1}^\infty B_k$ and $\sum_{n=1}^{n}\Prob(B_k)$ should be $\bigcup_{k=1}^\infty B_k$ and $\sum_{k=1}^{n}\Prob(B_k)$ (CN Thm 1.1.39). The heading says "(exercise)" but the proof is given.]

*Figure:* none.

---

### HW 08 (`20261122_012000.jpg`): Lebesgue measure

**Lebesgue measure**

**N.** Let $\Omega = [0,1]$. Suppose we randomly pick a number on $\Omega$.

*Figure (unit interval):* a horizontal segment with end ticks labelled $0$ (left) and $1$ (right). A short arc (a cup-shaped bracket "⌣") under the line about a third of the way along is labelled "$A$" beneath it, marking a subset. Just to the right of it a downward arrow above the line points to a point labelled "$\omega$" below the line (the randomly picked number). To the right of the segment: "For $A \subseteq \Omega$, we want the probability that $\omega$ falls on $A$."

**Rem.** Such a measure is the Lebesgue measure on $[0,1]$. It assigns to intervals their 'usual' length $\lambda((a,b]) = b - a$. Countable additivity is only satisfied if $\mathcal F = \mathcal B([0,1])$, and not if $\mathcal F = \powerset([0,1])$. This is because you can partition $\Omega$ into $V_1, \dots \subseteq \Omega$ where $\Prob(V_1) = \cdots$, but
$$\sum_{n=1}^\infty \Prob(V_n) = \begin{cases} 0 \\ \infty \end{cases} \ne 1$$
[The construction of the $V_n$ is not given ("$\Prob(V_1) = \cdots$" is written as an ellipsis). The brace means the sum is either $0$ or $\infty$ (all $V_n$ have equal measure). CN Rem 1.1.40 only says not every subset of $\R$ can be assigned a length; the partition argument is in the notes only, without the construction.]
[possible error: "only satisfied if $\mathcal F = \mathcal B([0,1])$" overstates it; the point (CN §1.1.5) is that $\lambda$ cannot be extended to all of $\powerset([0,1])$ countably additively, so a smaller σ-algebra such as $\mathcal B([0,1])$ is used.]

**Ex.** Uniform distribution
The probability space $([0,1], \mathcal B([0,1]), \lambda)$, where $\lambda$ is the Lebesgue measure restricted to Borel subsets of $[0,1]$, is the standard model for "picking a random uniform point in $[0,1]$". Here
$$\lambda([a,b]) = b - a \qquad \text{for } 0 \le a \le b \le 1$$
which matches the intuitive notion of "length as probability".

**Rem.** The Lebesgue measure is studied comprehensively in measure theory, far beyond the scope of this course. See MATH4408.
[Not in CN. MATH4408 is a UQ course code; not part of the book's course list.]

[The lower third of the page is blank.]

---

### HW 09 (`20261122_012012.jpg`): Borel–Cantelli lemmas (upper and lower limits) (1)

**Borel–Cantelli lemmas (upper and lower limits)**

**Def.** Upper and lower limits (sequences in $\R$)
Given $(x_n)_{n=1}^\infty$, define
$$
\limsup_{n\to\infty} x_n = \lim_{n\to\infty}\sup_{m\ge n} x_n = \inf_{n\ge1}\sup_{m\ge n} x_n,
\qquad
\liminf_{n\to\infty} x_n = \lim_{n\to\infty}\inf_{m\ge n} x_n = \sup_{n\ge1}\inf_{m\ge n} x_n
$$
[possible error: the inner sup/inf run over $m \ge n$ but act on $x_n$; should be $x_m$. Not in CN (CN defines limsup/liminf for events only).]

**Def.** Upper and lower limits (sequences of events)
Given $A_1, A_2, \dots \in \mathcal F$, define
$$
\begin{aligned}
\ast\quad \limsup_{n\to\infty} A_n &:= \bigcap_{m=1}^{\infty}\ \bigcup_{n=m}^{\infty} A_n =: \{A_n \text{ i.o.}\} && \text{"infinitely often"}\\
\liminf_{n\to\infty} A_n &:= \bigcup_{n=1}^{\infty}\ \bigcap_{n=n}^{\infty} A_n =: \{A_n \text{ a.b.f.m.}\} && \text{"all but finitely many"}
\end{aligned}
$$
[Under the $\bigcap_{m=1}^\infty$ is a small "(2)" and under the $\bigcup_{n=m}^\infty$ a small "(1)", keyed to the $\ast$ footnote at the bottom of the page. possible error: the liminf indices read $\bigcup_{n=1}^\infty \bigcap_{n=n}^\infty$; should be $\bigcup_{m=1}^\infty \bigcap_{n=m}^\infty$ (CN Def 1.1.42).]

where
$$
\begin{aligned}
\omega \in \{A_n \text{ i.o.}\} &\iff \abs{\{n : \omega \in A_n\}} = \infty\\
\omega \in \{A_n \text{ a.b.f.m.}\} &\iff \abs{\{n : \omega \in A_n\}} < \infty
\end{aligned}
$$
[Written as $\abs{n : \omega \in A_n}$ without inner braces. possible error: the second line should read $\abs{\{n : \omega \notin A_n\}} < \infty$ (only finitely many $n$ with $\omega \notin A_n$); as written it says $\omega$ is in only finitely many $A_n$.]

**Rem.** With sequences in $\R$, we have that
$$\liminf_{n\to\infty} x_n \le \limsup_{n\to\infty} x_n$$
Similarly, with sequences of events we have that
$$\{A_n \text{ a.b.f.m.}\} \subseteq \{A_n \text{ i.o.}\} \qquad \text{i.e. } A_n \text{ a.b.f.m. is stronger than } A_n \text{ i.o.}$$
For example, take the sequence of events
$$\{A_n \text{ holds } \forall \text{ even } n,\ \text{NOT holds } \forall \text{ odd } n\}$$
which $\not\subseteq \{A_n \text{ a.b.f.m.}\}$ but $\subseteq \{A_n \text{ i.o.}\}$.
[The "i.e. … stronger than …" is a margin note to the right of the inclusion. The example's wording is as written: it describes outcomes $\omega$ that lie in $A_n$ for every even $n$ and in no $A_n$ for odd $n$; such $\omega$ are in $\{A_n \text{ i.o.}\}$ but not in $\{A_n \text{ a.b.f.m.}\}$. The relation symbols are "$\subsetneq$"-like with a slash, read as $\not\subseteq$.]

**Th.** [a crossed-out symbol] $A_n$ infinitely often iff $\limsup_n A_n$, i.e.
$$\underbrace{\bigcap_{n\ge1}\bigcup_{m\ge n} A_n}_{\text{equivalent}} = \{A_n \text{ i.o.}\}$$
[The underbrace "equivalent" spans the left-hand side. possible error: the union is over $m \ge n$ but of $A_n$; should be $A_m$ (the proof on HW 10 uses $A_m$ in places). Not stated as a theorem in CN (CN Def 1.1.42 just defines $\{A_n \text{ i.o.}\}$ as the limsup and explains it in words).]

$\ast$ (1) From $m$ onwards, at least one $n$ outcome belongs to event for —
$\phantom{\ast}$ (2) Condition must hold for every single $m$
[The footnote to the limsup definition. (1) is written in two pieces: "From $m$ onwards, at least one $n$" on the line, with "outcome belongs to event for" written above it, ending in a dash; read as "(1) the outcome belongs to the event for at least one $n$ from $m$ onwards".]

*Figure:* none.

---

### HW 10 (`20261122_012018.jpg`): Borel–Cantelli lemmas (upper and lower limits) (2)

**Borel–Cantelli lemmas (upper and lower limits)**

**P.** To show two sets are equal, we must show they are both subsets of the other.
We first show that
$$\bigcap_{n\ge1}\bigcup_{m\ge n} A_n \subseteq \{A_n \text{ i.o.}\}$$
Suppose that
$$\omega \in \bigcap_{n\ge1}\bigcup_{m\ge n} A_n \iff \forall n : \omega \in \bigcup_{m\ge n} A_n \iff \exists\, m \ge n : \omega \in A_m$$
and therefore we obtain the subsequence $\{n : \omega \in A_n\}_{n=1}^\infty$. This subsequence has infinite elements, which implies $\omega \in \{A_n \text{ i.o.}\}$.

We now show
$$\{A_n \text{ i.o.}\} \subseteq \bigcap_{n\ge1}\bigcup_{m\ge n} A_n$$
Suppose that
$$
\omega \in \{A_n \text{ i.o.}\} \iff \abs{\{n : \omega \in A_n\}} = \infty
\implies \underbrace{\forall n \ge 1,\ \underbrace{\exists\, m \ge n : \omega \in A_m}_{(1)}}_{(2)}
\quad \Big\}\ \text{else } \# < n < \infty.
$$
where statements (1), (2) are equivalent to
- (1) $\omega \in \bigcup_{m\ge n} A_m$
- (2) $\omega \in \bigcap_{n\ge1}\bigcup_{m\ge n} A_m$

which concludes the proof.
[The brace note "else $\# < n < \infty$" is as written; it presumably means "otherwise the number of such $n$ would be finite". The unions on this page mix $A_n$ and $A_m$ (same issue as HW 09). In the first half, the second "$\iff$" drops "$\forall n$" ("$\forall n\ \exists m \ge n$" is meant).]

**Th.** Properties of upper and lower limits (for sequences of events) (exercise)
- (a) $\displaystyle \liminf_{n\to\infty} A_n = \Bigl(\limsup_{n\to\infty} A_n^c\Bigr)^c$
- (b) If $A_n \uparrow$ or $A_n \downarrow$, then $\displaystyle \limsup_{n\to\infty} A_n = \liminf_{n\to\infty} A_n$
- (i) $\displaystyle \Prob\Bigl(\limsup_{n\to\infty} A_n\Bigr) \ge [\text{blotted}]\ \limsup_{n\to\infty} \Prob(A_n)$
- (ii) $\displaystyle \Prob\Bigl(\liminf_{n\to\infty} A_n\Bigr) \le \liminf_{n\to\infty} \Prob(A_n)$

[(i) has a solid hatched blot (a crossed-out word or symbol) between "$\ge$" and "limsup"; the statement reads correctly without it. Items are labelled (a), (b), then (i), (ii) as written. CN has only (a) (Rem 1.1.43, as $\{A_n \text{ i.o.}\}^c = \{A_n^c \text{ a.b.f.m.}\}$); (b), (i), (ii) are in the notes only, without proof.]

*Figure:* none.

---

### HW 11 (`20261122_012025.jpg`): Borel–Cantelli I

**Borel–Cantelli I**

**Th.** Borel–Cantelli lemma I
If $A_1, A_2, \dots \in \mathcal F$ satisfy
$$\sum_{n=1}^\infty \Prob(A_n) < \infty \implies \Prob(A_n \text{ i.o.}) = 0$$

**P.** Define the sequence
$$B_n = \bigcup_{m=n}^\infty A_m \implies B_1 \supseteq B_2 \supseteq \cdots \quad \text{i.e. } B_n \downarrow$$
Then
$$0 \le \Prob(B_n) = \Prob\Bigl(\bigcup_{m=n}^\infty A_m\Bigr) \overset{\text{(Boole's)}}{\le} \sum_{m=n}^\infty \Prob(A_m) \overset{\text{(assume)}}{<} \infty$$
Note that the tail of the sum $\sum_{n\ge m}\Prob(A_n) \to 0$. Therefore,
$$
\begin{aligned}
\Prob(A_n \text{ i.o.}) &= \Prob\Bigl(\bigcap_{n=1}^\infty\bigcup_{m=n}^\infty A_m\Bigr)\\
&= \Prob\Bigl(\bigcap_{n=1}^\infty B_n\Bigr)\\
&= \lim_{n\to\infty}\Prob(B_n) && \text{(continuity from above)}\\
&= 0
\end{aligned}
$$
which concludes the proof.
[The labels "(Boole's)" and "(assume)" are written above the $\le$ and $<$. The last step (= 0) uses $\Prob(B_n) \le$ tail $\to 0$; the link is not written explicitly. CN Lemma 1.1.44 proves it with Boole directly (no continuity).]

**Ex.** Suppose $A_1, A_2, \dots$ satisfy $\Prob(A_n) = 1/n^2$. Then
$$\sum_{n=1}^\infty \Prob(A_n) = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < \infty$$
which implies by the first lemma that
$$\Prob(A_n \text{ i.o.}) = 0$$
i.e. $A_n$ occurs only finitely many times.
[The example also appears in the course guide §1.3 (with "independent events", which BC I doesn't need); not in CN.]

*Figure:* none.

---

### HW 12 (`20261122_012030.jpg`): Borel–Cantelli II

**Borel–Cantelli II**

**Th.** Borel–Cantelli lemma II
Suppose $A_1, A_2, \dots \in \mathcal F$ are independent events. Then if
$$\sum_{n=1}^\infty \Prob(A_n) = \infty \implies \Prob(A_n \text{ i.o.}) = 1$$

**P.** We must show
$$\Prob(A_n \text{ i.o.}) = \Prob\bigl(\{A_n^c \text{ a.b.f.m.}\}^c\bigr) = 1 - \Prob(\{A_n^c \text{ a.b.f.m.}\})$$
is equal to 1, which is equivalent to
$$\Prob(\{A_n^c \text{ a.b.f.m.}\}) = \Prob\Bigl(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty A_m^c\Bigr)$$
being equal to 0. By Booles' inequality,
$$\Prob\Bigl(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty A_m^c\Bigr) \le \sum_{n=1}^\infty \Prob\Bigl(\bigcap_{m=n}^\infty A_m^c\Bigr)$$
and so this is equivalent / it is sufficient to show $\Prob\bigl(\bigcap_{m=n}^\infty A_m^c\bigr) = 0$.
Therefore,
$$
\begin{aligned}
0 \le \Prob\Bigl(\bigcap_{m=n}^\infty A_m^c\Bigr) &\le \Prob\Bigl(\bigcap_{m=n}^N A_m^c\Bigr)\\
&= \prod_{m=n}^N \Prob(A_m^c) && \text{(independence)}\\
&= \prod_{m=n}^N \bigl(1 - \Prob(A_m)\bigr)\\
&\le \prod_{m=n}^N \exp[-\Prob(A_m)] && (1 - x \le \exp[-x] \text{ by convexity})\\
&= \exp\Bigl[-\sum_{m=n}^N \Prob(A_m)\Bigr]
\end{aligned}
$$
Note that the sum $\to \infty$ as $N \to \infty$, and so the RHS $\to 0$.
This implies that
$$\Prob\Bigl(\bigcap_{m=n}^\infty A_m^c\Bigr) = 0 \implies \Prob(A_n \text{ i.o.}) = 1$$
which concludes the proof.
["Booles'" as written. In a few places the index under $\bigcap$ reads "$m=n$" with the bound written "$n=n$"; read as $m=n$ throughout, matching the products.]

**Ex.** Suppose $A_1, A_2, \dots$ satisfy $\Prob(A_n) = 1/n$. Then
$$\sum_{n=1}^\infty \Prob(A_n) = \sum_{n=1}^\infty \frac1n \to \infty$$
which implies by the second lemma that (if $A_n$ are independent)
$$\Prob(A_n \text{ i.o.}) = 1.$$

*Figure:* none.

---

### HW 13 (`20261122_012038.jpg`): Random variables

**Random variables**

**Def.** Random variable
Given $(\Omega, \mathcal F)$, a random variable is a function $X : \Omega \to \R$ if it is $\mathcal F/\mathcal B(\R)$-measurable, i.e.
$$X^{-1}(B) = \{\omega \in \Omega : X(\omega) \in B\} \in \mathcal F \qquad \forall B \in \mathcal B(\R)$$
where $X^{-1}(B)$ is the pre-image of $B$.

**Rem.** Note that random variables need not be invertible.
Also note that we do not need $\Prob$ to define a random variable.
[CN Def 1.2.1 starts from a probability space $(\Omega,\mathcal F,\Prob)$; the remark that $\Prob$ isn't needed is in the notes only.]

*Figure (a random variable as a map):* on the left a rectangle labelled "$\Omega$" (label centred on the top edge) containing three small hollow points in a row, labelled $\omega$, $\omega'$, $\omega''$ beneath them. On the right a straight line drawn diagonally (from lower left to upper right) labelled "$\R$" at its top end, with two filled points on it: $X(\omega)$ (upper) and $X(\omega')$ (lower), labels to the right of the line. Three curved arrows leave the rectangle to the right: two (from the region of $\omega'$ and $\omega''$) arc over and end at the same place on the line near $X(\omega)$, and one ends near $X(\omega')$. [The arrows illustrate that several outcomes can map to the same value (the "need not be invertible" remark); their exact start points are not distinguishable.]

**Ex.** Let $(\Omega, \mathcal F) = ([0,1], \mathcal B[0,1])$, and
$$X(\omega) = I_{[0,p]}(\omega) = \begin{cases} 1 & \text{if } \omega \in [0,p]\\ 0 & \text{if not}\end{cases}$$

*Figure (indicator as a map):* left, a horizontal segment labelled "$\Omega$" above, with end ticks $0$ and $1$ and an interior tick $p$ (labels below); a hollow point labelled $\omega$ (above) lies between $0$ and $p$. Right, a horizontal number line with arrowheads at both ends, labelled "$\R$" above, with ticks labelled $0$ and $1$ below. Three curved arrows run underneath from the left segment to the right line: the outer two start under $[0,p]$ (one near $\omega$, one just left of $p$) and both end at $1$; the inner one starts just left of $1$ (in $(p,1]$) and ends at $0$. So points of $[0,p]$ go to $1$ and points of $(p,1]$ go to $0$.

Why is $X$ a random variable? Take $B \in \mathcal B(\R)$. Then
$$
\begin{array}{lll}
\text{Case 1:} & 0, 1 \in B & X^{-1}(B) = [0,1] = \Omega \in \mathcal F\\
\text{Case 2:} & 1 \in B,\ 0 \notin B & X^{-1}(B) = [0,p] \in \mathcal F\\
\text{Case 3:} & 1 \notin B,\ 0 \notin B & X^{-1}(B) = \emptyset \in \mathcal F\\
\text{Case 4:} & 1 \notin B,\ 0 \in B & X^{-1}(B) = (p,1] \in \mathcal F
\end{array}
$$
[Case 3 is written "$X^{-1}(\omega)$" for $X^{-1}(B)$. Not in CN.]

**Th.** $X$ is a random variable on $(\Omega, \mathcal F)$ iff $\{X \le x\} \in \mathcal F$ $\forall x \in \R$.
i.e. $\{\omega \in \Omega : X(\omega) \le x\} \in \mathcal F$ $\forall x \in \R$
i.e. $X^{-1}((-\infty, x]) \in \mathcal F$ $\forall x \in \R$
[Stated without proof (CN Prop 1.2.2, with the reason in Rem 1.2.3).]

**Rem.** For $X$ to be a random variable, $\mathcal F$ must be sufficiently large.
For example, suppose $\mathcal F = \{\emptyset, \Omega, [0, 1/2], (1/2, 1]\}$ for $p \ne 1/2$. Then
$$X^{-1}(\{{-1}\}) = [0,p] \notin \mathcal F \implies X \text{ is not a random variable}$$
However $X$ is a random variable if $\mathcal F = \sigma([0,p])$.
[The set is written "$\{-1\}$" (a short stroke before the 1, possibly a stray mark). For $X^{-1}(\cdot) = [0,p]$ it must be $\{1\}$: possible error or stray stroke; in the notebook, a retake won't help. "$\sigma([0,p])$" means $\sigma(\{[0,p]\})$. Not in CN.]

---

### HW 14 (`20261122_012044.jpg`): Distributions

**Distributions**

**Def.** Distribution of random variable
Let $X$ be a random variable on $(\Omega, \mathcal F, \Prob)$. The distribution of $X$ is a function $\mu_X : \mathcal B(\R) \to [0,1]$, where
$$
\left.\begin{aligned}
\underset{\substack{\cap\\ \mathcal B(\R)}}{\mu_X(B)} &= \Prob(X^{-1}(B))\\
&= \Prob(X \in B)
\end{aligned}\right\}
\quad
\begin{aligned}
X^{-1}(B) &= \{\omega \in \Omega : X(\omega) \in B\}\\
&= \{X \in B\}
\end{aligned}
$$
is the distribution of $X$.
[Under the $B$ in $\mu_X(B)$ is written "$\in \mathcal B(\R)$" vertically (a rotated "$\in$" then $\mathcal B(\R)$), i.e. $B \in \mathcal B(\R)$. CN Def 1.2.5 adds that $\mu_X$ is a probability measure on $(\R, \mathcal B(\R))$ (also called the law).]

**Def.** Cumulative distribution functions
The cumulative distribution function (cdf) of a random variable $X$ is a function $F_X : \R \to [0,1]$ where
$$F_X(x) = \Prob(X \le x) = \mu_X((-\infty, x])$$

**Ex.** Let $(\Omega, \mathcal F, \Prob) = ([0,1], \mathcal B[0,1], \Prob)$, where $\Prob$ is the Lebesgue measure on $[0,1]$ i.e. the length of $A$, and set $X(\omega) = I_{[0,p]}(\omega)$.
We compute the CDF.
$$
\begin{array}{llcl}
(1) & x < 0 & & X^{-1}((-\infty,x]) = \emptyset\\
    & 0, 1 \notin (-\infty, x] & \implies & F_X(x) = \Prob(\emptyset) = 0\\[4pt]
(2) & 0 \le x < 1 & & X^{-1}((-\infty,x]) = (p,1]\\
    & 0 \in (-\infty,x],\ 1 \notin (-\infty,x] & \implies & \Prob((p,1]) = 1 - p\\[4pt]
(3) & x \ge 1 & & X^{-1}((-\infty,x]) = \Omega\\
    & 0, 1 \in (-\infty,x] & \implies & \Prob(\Omega) = 1
\end{array}
$$
and so the CDF is
$$F_X(x) = \begin{cases} 0 & x < 0\\ 1-p & 0 \le x < 1\\ 1 & x \ge 1\end{cases}$$
[Checked: correct ($X = 0$ exactly on $(p,1]$). Not in CN.]

**Th.** Every CDF $F_X$ satisfies:
- (a) Monotone: $F_X$ is non-decreasing
- (b) Right-continuous: $\lim_{y\downarrow x} F_X(y) = F_X(x)$ $\quad \forall x \in \R$
- (c) Limits: $\lim_{x\to-\infty} F_X(x) = 0$ and $\lim_{x\to\infty} F_X(x) = 1$

[No proof in the notes; CN Prop 1.2.7 gives one. ↔ STAT2003 (Ch 26).]

*Figure:* none.

---

### HW 15 (`20261122_012051.jpg`): Random vectors (1)

**Random vectors**

**Def.** Random vector
Given $(\Omega, \mathcal F)$, a random vector is a function $\vect X = (X_1, \dots, X_d) : \Omega \to \R^d$ that is $\mathcal F/\mathcal B(\R^d)$ measurable, i.e.
$$\vect X^{-1}(B) \in \mathcal F \qquad \forall B \in \mathcal B(\R^d)\ \ [\text{a line of text crossed out with hatching}]$$
where
$$\mathcal B(\R^d) = \sigma\bigl((-\infty, x_1] \times \dots \times (-\infty, x_d],\ x_1, \dots, x_d \in \R\bigr)$$
[$\vect X$ is underlined (a vector) in the notes. The generating class for $\mathcal B(\R^d)$ is in the notes only; CN Def 1.2.4 doesn't define $\mathcal B(\R^d)$.]

**Th.** $\vect X$ is a random vector on $(\Omega, \mathcal F)$ iff
$$\{X_1 \le x_1, X_2 \le x_2, \dots, X_d \le x_d\} \in \mathcal F \qquad \forall x_1, \dots, x_d \in \R$$
[Stated without proof. CN Def 1.2.4 gives a different equivalent condition: each component $X_i$ is a random variable.]

**Ex.** Let $(\Omega, \mathcal F) = ([0,1]^2, \mathcal B([0,1]^2))$, and
$$\vect X(\vect\omega) = \begin{pmatrix} X_1(\vect\omega)\\ X_2(\vect\omega)\end{pmatrix} = \begin{pmatrix} I_{[0,p]}(\omega_1)\\ I_{[0,p]}(\omega_2)\end{pmatrix}$$

*Figure (unit square mapped to the four corners of $\{0,1\}^2$):* Left: a square labelled "$\Omega$" above, corners labelled $(0,0)$ bottom left, $(0,1)$ top left, $(1,1)$ top right, $(1,0)$ bottom right. A dashed vertical line at $\omega_1 = p$ (tick labelled $p$ below the square) and a dashed horizontal line at $\omega_2 = p$ (labelled $p$ on the left) split it into four rectangles, labelled in square brackets: top left $[D]$ ($\omega_1 \le p$, $\omega_2 > p$), top right $[A]$ ($\omega_1, \omega_2 > p$; the largest piece), bottom left $[C]$ ($\omega_1, \omega_2 \le p$), bottom right $[B]$ ($\omega_1 > p$, $\omega_2 \le p$). [The dashed lines sit at roughly one quarter of the side from the left and from the bottom, so $p \approx 0.25$ as drawn.] Right: axes labelled "$\R^2$", with points at $(0,0)$ (origin), $(1,0)$ on the horizontal axis, $(0,1)$ on the vertical axis and a hollow point $(1,1)$, each labelled. Four curved arrows run from a point in each rectangle to a corner point: $A \to (0,0)$, $B \to (0,1)$, $C \to (1,1)$, $D \to (1,0)$. Below, a curved arrow from left to right labelled $\vect X$ (underlined).

As an exercise, we can show $\vect X$ is a random variable / a random vector on $(\Omega, \mathcal F)$. It is sufficient to check $\forall x_1, x_2 \in \R$ that
$$\{X_1(\omega) \le x_1,\ X_2(\omega) \le x_2\} \in \mathcal F = \mathcal B([0,1]^2)$$
We similarly split into cases.
$$
\begin{array}{lll}
\text{Case 1:} & x_1 \ge 1,\ x_2 \ge 1 & \vect X^{-1}\bigl((-\infty,x_1]\times(-\infty,x_2]\bigr) = \Omega \in \mathcal F\\
\text{Case 2:} & 0 \le x_1 < 1,\ x_2 \ge 1 & \vect X^{-1} = A \cup B = (p,1] \times [0,1] \in \mathcal F\\
\text{Case 3:} & x_1 \ge 1,\ 0 \le x_2 < 1 & \vect X^{-1} = A \cup D = [0,1] \times (p,1] \in \mathcal F\\
\text{Case 4:} & 0 \le x_1, x_2 < 1 & \vect X^{-1} = A = (p,1]^2 \in \mathcal F\\
\text{Else:} & x_1, x_2 < 0 & \vect X^{-1} = \emptyset \in \mathcal F
\end{array}
$$
[possible error: "Else" should be "$x_1 < 0$ or $x_2 < 0$" (either one negative gives $\emptyset$). Checked the other cases: correct. Not in CN.]

---

### HW 16 (`20261122_012057.jpg`): Random vectors (2)

**Random vectors**

**Ex.** (c) [= continued from HW 15] Now introduce $\Prob$ as the Lebesgue measure on $([0,1]^2, \mathcal B[0,1]^2)$. We can think of $\Prob(A)$ as the "area" of $A$ for $A \in \mathcal B([0,1]^2)$.
First consider the joint distribution of $\vect X = (X_1, X_2)$.
$$
\begin{aligned}
\Prob(\vect X = (0,0)) &= \Prob(\vect X^{-1}(\{(0,0)\})) = \Prob(A) = (1-p)^2\\
\Prob(\vect X = (1,0)) &= \Prob(D) = p(1-p)\\
\Prob(\vect X = (0,1)) &= \Prob(B) = p(1-p)\\
\Prob(\vect X = (1,1)) &= \Prob(C) = p^2
\end{aligned}
$$
Now consider the marginal distribution of $\vect X = (X_1, X_2)$.
$$
\left.\begin{aligned}
\Prob(X_1 = 1) &= \Prob(\vect X = (1,0) \text{ or } \vect X = (1,1)) = \Prob(C \cup D) = p\\
\Prob(X_1 = 0) &= \Prob(A \cup B) = 1 - p
\end{aligned}\right\}\ X_1 \sim \Bern(p)
$$
$$
\left.\begin{aligned}
\Prob(X_2 = 1) &= \Prob(C \cup B) = p\\
\Prob(X_2 = 0) &= \Prob(A \cup D) = 1 - p
\end{aligned}\right\}\ X_2 \sim \Bern(p)
$$
We can conclude that $X_1$ and $X_2$ are independent, as
$$\Prob(X_1 = i, X_2 = j) = \Prob(X_1 = i)\,\Prob(X_2 = j) \qquad \forall i, j$$
[Checked against the HW 15 figure: all values correct. Not in CN.]

*Figure:* none (uses the HW 15 figure).

---

