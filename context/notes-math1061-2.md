# MATH1061 Discrete Mathematics: transcription, part 2 of 3 (HW 26–49)

_Transcription phase. Source: 77 photos of the handwritten notes (one notebook page per photo), taken in shooting order. "HW nn" is the photo number nn in shooting order; the file name is given under each heading. No typed notes or slides were supplied. Course taken in one semester; no dates are recorded here (several pages carry a "Lecture notes" date header, which is omitted)._

**Conventions.** Wording, structure and labels (Def., Th., Lemma, Proof/P., Ex., Rem., Cor.) follow the notes. Maths uses `notation.tex` macros where they exist (`\Z`, `\Q`, `\R`, `\N`, `\abs`, `\powerset`, `\T`). Logical "not" is kept as the notes' $\sim$. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected); `[illegible]` would mark unreadable text (none needed). Crossed-out text is noted only where it carries meaning. Figures are described in enough detail to redraw in TikZ.

**This part:** sets, functions, cardinality and countability, relations, equivalence and order relations.

---

## HW 26 — Set theory definitions; subsets
_File `20261121_225654.jpg`._

**Set theory definitions**

**Def.** A *set* $S$ is a collection of objects – the *elements* of $S$.
If $x$ is in $S$, $x \in S$. If $x$ is not in $S$, $x \notin S$.
We can list the elements of $S$: $S = \{x_1, x_2, x_n\}$. [sic; presumably $\{x_1, x_2, \dots, x_n\}$]
Order does not matter, repetitions are ignored.

You can also define sets by a property their elements must satisfy, using *set-builder notation*:
$$A = \{x \in S \mid P(x)\}$$

**Ex.** $A = \{n \in \Z \mid n = 2k,\ k \in \Z\}$ is the set of evens.

The elements of a set can be sets themselves.

**Subsets**
**Def.** The set $A$ is a *subset* of a set $B$, written $A \subseteq B$, iff every element of $A$ is also an element of $B$.
$$A \subseteq B \iff \forall x,\ x \in A \to x \in B$$
Every set is a subset of itself.
$A$ is a *proper subset* of $B$, written $A \subset B$, iff $A \ne B$.
[possible error: should read "iff $A \subseteq B$ and $A \ne B$".]

Two sets are *equal* if they possess the same elements.

The *empty set* contains NO elements, and is denoted by: $\emptyset = \{\ \}$. $\emptyset$ is a subset of all sets.

For a finite set $A$, the *cardinality* of set $A$ is the number of elements in set $A$, denoted by $\abs{A}$.

## HW 27 — Russell's paradox; operations on sets
_File `20261121_225658.jpg`._

**Russell's Paradox**
**Def.** $S = \{A \mid A \text{ is a set and } A \notin A\}$
**Ex.** Is $S \in S$?
↳ if $S \in S$, then by definition $S \notin S$ ↯
↳ if $S \notin S$, then by definition $S \in S$ ↯

**Def.** To avoid problems similar to Russell's paradox, we can attempt to define all sets recursively:
↳ Base: $\emptyset$ is a set
↳ Recursion: we define several operations that build new sets from all sets [presumably "from old sets"]

**Operations on sets**
**Def.**
| | | |
|---|---|---|
| $A \cup B$: | $x \in A$ or $x \in B$ or both | (union) |
| $A \cap B$: | $x \in A$ and $x \in B$ | (intersection) |
| $B \setminus A$: | $x \in B$ and $x \notin A$ | (set diff.) |
| $A^c$: | $= \{x \in U \mid x \notin A\}$ | (complement) |

Given sets $A_0, A_1, A_2, \dots$, and $n \in \Z$, $n \ge 0$,
$$\bigcup_{i=0}^{n} A_i = \{x \mid x \in A_i \text{ for at least one } i = 0, 1, 2, \dots, n\}$$
$$\bigcup_{i=0}^{\infty} A_i = \{x \mid x \in A_i \text{ for at least one } i \ge 0,\ i \in \Z\}$$
$$\bigcap_{i=0}^{n} A_i = \{x \mid x \in A_i \text{ for all } i = 0, 1, 2, \dots, n\}$$
$$\bigcap_{i=0}^{\infty} A_i = \{x \mid x \in A_i \text{ for all } i \in \Z,\ i \ge 0\}$$
[$U$, the universal set, is used without definition here.]

## HW 28 — Power sets; disjoint sets; partitions
_File `20261121_225706.jpg`._

**Power sets**
**Def.** For any set $S$, the *power set* of $S$, denoted $\powerset(S)$, is the set of all subsets of $S$.
$$\powerset(S) = \{X \mid X \subseteq S\}$$
**Ex.** $S = \{1, 3\} \implies \powerset(S) = \{\emptyset, \{1\}, \{3\}, \{1, 3\}\}$.
For any set $S$, $\emptyset \in \powerset(S)$ and $S \in \powerset(S)$.
**Def.** If $\abs{S} = n$, then $\abs{\powerset(S)} = 2^n$. [stated without proof]

**Disjoint sets**
**Def.** Two sets are *disjoint* iff $A \cap B = \emptyset$.
Sets $A_1, A_2, A_3, \dots$ are *mutually disjoint* (or *pairwise disjoint*, or *nonoverlapping*) iff $A_i \cap A_j = \emptyset$ whenever $i \ne j$.

**Partitions of sets**
**Def.** A finite or infinite collection of nonempty sets $\{A_1, A_2, \dots\}$ is a *partition* of a set $A$ iff $A$ is the union of all $A_i$, and $A_1, A_2, \dots$ are mutually disjoint.
**Ex.** A partition of $S = \{2, 3, 5, 7, 11\}$ is given by $\{2, \{3, 5\}, \{7, 11\}\}$.
[possible error: the first block should be the set $\{2\}$: $\{\{2\}, \{3, 5\}, \{7, 11\}\}$.]

Mutually disjoint: all pairs of distinct sets are disjoint.

## HW 29 — Ordered n-tuples; Cartesian product
_File `20261121_225710.jpg`._

**Ordered $n$-tuple**
**Def.** Let $n \in \Z^{+}$, let $x_1, x_2, x_3, \dots, x_n$ be $n$, not necessarily distinct elements. The *ordered $n$-tuple*, denoted $(x_1, x_2, \dots, x_n)$, consists of the $n$ elements with their ordering: first $x_1$, then $x_2$, and so up to $x_n$.
When $n = 2$, we call $(x_1, x_2)$ an *ordered pair*. When $n = 3$, we call $(x_1, x_2, x_3)$ an *ordered triple*.
$$(x_1, x_2, \dots, x_n) = (y_1, y_2, \dots, y_n) \iff x_i = y_i \ \forall i,\ 1 \le i \le n$$
**Ex.** $(1, 2, 3) \ne (1, 2, 4)$, $(1, 3) \ne (3, 1)$.

**Cartesian product**
**Def.** The *Cartesian product* of sets $A$ and $B$, $A \times B$, is:
$$A \times B = \{(a, b) \mid a \in A,\ b \in B\}$$
**Ex.** If $A = \{a, b\}$ and $B = \{2, 3\}$ then $A \times B = \{(a, 2), (a, 3), (b, 2), (b, 3)\}$.
The familiar $x, y$ plane is $\R \times \R = \{(x, y) \mid x, y \in \R\}$.
In general,
$$A_1 \times A_2 \times \dots \times A_n = \{(a_1, a_2, \dots, a_n) \mid a_i \in A_i,\ 1 \le i \le n\}$$

## HW 30 — Intervals
_File `20261121_225715.jpg`. The lower half of the page is blank._

**Intervals**
**Def.** Given $a, b \in \R$ with $a \le b$,
$$\begin{aligned}
(a, b) &= \{x \in \R \mid a < x < b\} \\
[a, b) &= \{x \in \R \mid a \le x < b\} \\
(a, b] &= \{x \in \R \mid a < x \le b\} \\
[a, b] &= \{x \in \R \mid a \le x \le b\}
\end{aligned}$$
The symbols $\infty$ and $-\infty$ are used to indicate intervals that are unbounded.
$$\begin{aligned}
(a, \infty) &= \{x \in \R \mid x > a\} \\
[a, \infty) &= \{x \in \R \mid x \ge a\} \\
(-\infty, b) &= \{x \in \R \mid x < b\} \\
(-\infty, b] &= \{x \in \R \mid x \le b\}
\end{aligned}$$

## HW 31 — Properties of sets; proving set equality
_File `20261121_225720.jpg`._

**Properties of sets**

**Def.** If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.
**Proof.** Suppose $A, B, C$ are sets such that $A \subseteq B$ and $B \subseteq C$. Suppose $x \in A$.
Since $A \subseteq B$, $x \in B$. Since $B \subseteq C$, $x \in C$. $\square$

**Def.** Inclusion properties
$$A \cap B \subseteq A \text{ and } A \cap B \subseteq B, \qquad A \subseteq A \cup B \text{ and } B \subseteq A \cup B$$
**Proof.** See Venn diagram of sets $A, B$. [no diagram is drawn]

**Def.** Prove a set $A$ is equal to a set $B$. [heading; the method is shown by the example: prove $A \subseteq B$, then $B \subseteq A$]

**Ex.** Let $A = \{x \in \Z \mid x \equiv 1 \bmod 6\}$, $B = \{x \in \Z \mid x \equiv 1 \bmod 2 \wedge x \equiv 1 \bmod 3\}$. Prove $A = B$.
**Proof.** First we prove $A \subseteq B$:
Let $x \in A$. Then $x \in \Z$ and $x = 6k + 1$ for some $k \in \Z$.
Hence $x = 2(3k) + 1 \implies x \equiv 1 \bmod 2$; $x = 3(2k) + 1 \implies x \equiv 1 \bmod 3$.
Thus $x \in B$. $\therefore A \subseteq B$.

Next we prove $B \subseteq A$:
Let $x \in B$. Then $x \in \Z$ and $x = 2k + 1$ and $x = 3\ell + 1$ for some $k, \ell \in \Z$. Divide by parity cases:
↳ If $\ell$ is odd, $x = 3\ell + 1$ is even ↯
↳ If $\ell$ is even, $\ell = 2m$ for some $m \in \Z$.
$\therefore x = 3\ell + 1 = 3(2m) + 1 = 6m + 1$.
Thus $x \in A$. $\therefore B \subseteq A$. Hence $A = B$. $\square$
[congruence mod $n$ is used here before it is defined (HW 33 onwards / number theory pages).]

## HW 32 — Set identities
_File `20261121_225739.jpg`._

**Set identities**
**Th.** Let $A, B, C$ be any sets.
Sets are *commutative*: $A \cup B = B \cup A$, $A \cap B = B \cap A$
*associative*: $A \cup (B \cup C) = (A \cup B) \cup C$, $A \cap (B \cap C) = (A \cap B) \cap C$
*distributive*: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

They follow the *absorption laws*: $A \cup (A \cap B) = A$ and $A \cap (A \cup B) = A$
And *idempotent laws*: $A \cup A = A$ and $A \cap A = A$

**Further set identities**
**Th.** Let $A, B$ be subsets of the universal set $U$.
$$(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c$$
$$A - B = A \cap B^c, \qquad (A^c)^c = A$$
$$U^c = \emptyset \text{ and } \emptyset^c = U$$
$$A \cup \emptyset = A, \quad A \cap \emptyset = \emptyset, \qquad A \cap U = A, \quad A \cup U = U$$
[stated without proof; $A - B$ here and $B \setminus A$ on HW 27 are both used for set difference]

Similar to the laws of logical inference, we can use the set identities to prove further set properties.

## HW 33 — Functions; image and range
_File `20261121_225744.jpg`._

**Functions**
**Def.** A *function* $f$ from sets $X$ to $Y$, denoted $f : X \to Y$, is a subset of the Cartesian product $X \times Y$ such that $\forall x \in X,\ \exists y \in Y$ s.t. $(x, y) \in f$.
$X$ is the *domain* of $f$, $Y$ is the *co-domain* of $f$.
[possible error: the definition needs a *unique* $y$ for each $x$ ($\exists!$); as written any relation with full domain qualifies.]

If $f : X \to Y$ is a function and $(x, y) \in f$ then:
↳ we write $f(x) = y$, $f : x \mapsto y$
↳ $f(x)$ is the *value* of $f$ at $x$. $f(x)$ is the *image* of $x$ under $f$.
Note that $f$ is the function; $f(x)$ is an element of $Y$, i.e. $f(x) \in Y$.

**Image and Range**
**Def.** Given $f : X \to Y$ and an element $x \in X$, we call $f(x)$ the *image* of $x$.
If $A \subseteq X$, the *image of $A$* is:
↳ $f(A) = \{f(x) \mid x \in A\} = \{y \mid f(x) = y \text{ for some } x \in A\}$
Note that $f(A) \subseteq Y$.
**Def.** The set $f(X)$ is called the *range* of $f$.
↳ $f(X) = \{y \in Y \mid y = f(x) \text{ for some } x \in X\}$
Note that the range is a subset of the co-domain, implying there may exist elements in $Y$ not in $f(X)$.

**Th.** $f = g \iff \forall x \in X,\ f(x) = g(x)$
**Ex.** $x \ne \sqrt{x^2}$ since range of $f$ is $\Z$, range of $g$ is $\Z^{+}$.
[possible error: with domain $\Z$, the range of $g(x) = \sqrt{x^2} = \abs{x}$ is $\{0, 1, 2, \dots\} = \N_0$, not $\Z^{+}$ (0 is included). The domain is not stated.]

## HW 34 — Injective, surjective and bijective functions; inverse functions
_File `20261121_225751.jpg`._

**Injective functions**
**Def.** Let $f$ be a function from sets $X$ to $Y$.
$f$ is *injective* (one-to-one) iff for all elements $x_1, x_2$ in $X$, if $f(x_1) = f(x_2)$, then $x_1 = x_2$,
or contrapositively, if $x_1 \ne x_2$, $f(x_1) \ne f(x_2)$.

To prove $f : X \to Y$ is injective, we prove directly:
↳ Suppose $x_1, x_2 \in X$, $f(x_1) = f(x_2)$
↳ Show $x_1 = x_2$
↳ If not, show $x_1 \ne x_2$
Injectivity implies monotonicity.
[possible error: false in general. Monotonicity only makes sense for ordered sets, and even for $f : \R \to \R$ an injective function need not be monotone unless it is continuous.]

**Surjective functions**
**Def.** Let $f : X \to Y$. $f$ is *surjective* iff $\forall y \in Y,\ \exists x \in X$ such that $f(x) = y$. (onto)
i.e. all elements in $Y$ can be found with $f$ using input $x$.

To prove $f : X \to Y$ is surjective,
↳ Suppose $y \in Y$
↳ Construct an element $x \in X$ s.t. $f(x) = y$
↳ If not, find an element $y \in Y$ s.t. $y \ne f(x)$ for any $x \in X$.

**Bijective functions, inverse functions**
**Def.** $f$ is *bijective* (one-to-one correspondence) iff $f$ is both injective and surjective.
**Th.** Suppose $f$ is bijective. Then $\exists f^{-1} : Y \to X$ s.t. $f^{-1}(y) = x \iff f(x) = y$.
$f^{-1}$ is called the *inverse function* of $f$. [stated without proof]

## HW 35 — Examples of injective and surjective functions
_File `20261121_225757.jpg`. Heading "Examples of previous page functions"._

**Ex.** Let $f : \R \to \R$ be defined by $f(x) = x^2$. Is $f$ injective?
**Proof.** Take $x_1 = 2$, $x_2 = -2$. $f(x_1) = 4$, $f(x_2) = 4 \implies f(x_1) = f(x_2)$.
However $x_1 \ne x_2$, thus $f$ is not injective.

**Ex.** Let $f : \R \to \R$ be defined by $f(x) = 2x - 3$. Is $f$ surjective?
**Proof.** Take $y = 2x - 3 \implies x = \frac{y+3}{2}$.
Suppose $y \in \R$. Take $x \in \R$. [i.e. take $x = \frac{y+3}{2} \in \R$]
Then
$$f(x) = f\left(\frac{y+3}{2}\right) = 2\left(\frac{y+3}{2}\right) - 3 = y + 3 - 3 = y$$
Thus $f$ is surjective.

**Ex.** Let $f : \R \to \R$ be defined as $f(x) = x^2$. Is $f$ surjective?
**Proof.** Take $y = -1 \in \R$. Since $x^2 \ge 0\ \forall x \in \R$, $\nexists x \in \R$ s.t. $y = -1$. [i.e. s.t. $f(x) = -1$] Hence $f$ is not surjective.

## HW 36 — Composition of functions; identity functions; inverses
_File `20261121_225807.jpg`. The identity function is written with a hooked letter that looks like a script "i" or "ι"; it is transcribed as $i_X$ below._

**Composition of functions**
**Def.** Let $f : X \to Y$, $g : Y \to Z$ be functions. The *composition* of $f$ and $g$ is the function $g \circ f : X \to Z$, defined by $(g \circ f)(x) = g(f(x))$.
Function composition is not necessarily commutative.

**Th.** If $f : X \to Y$ and $i_X$ is the identity function on $X$, and $i_Y$ is the identity function on $Y$, then
$$f \circ i_X = f \quad \text{and} \quad i_Y \circ f = f.$$
**Proof.** Suppose $f$ is a function, $i_X, i_Y$ are identity functions. By definition, $i_X(x) = x\ \forall x \in X$, $i_Y(y) = y\ \forall y \in Y$.
For all $x \in X$, $(f \circ i_X)(x) = f(i_X(x)) = f(x)$. $\square$
For all $x \in X$, $(i_Y \circ f)(x) = i_Y(f(x)) = f(x)$. $\square$

**Th.** Let $f : X \to Y$ be bijective with inverse $f^{-1} : Y \to X$. Then $f^{-1} \circ f = i_X$ and $f \circ f^{-1} = i_Y$. [stated without a general proof; the example follows]

**Ex.** Take $f(x) = 2x + 1$, $f^{-1}(y) = \frac{y - 1}{2}$ $\forall x, y \in \R$.
Thus $\forall x \in \R$,
$$(f^{-1} \circ f)(x) = f^{-1}(f(x)) = f^{-1}(2x + 1) = \frac{2x + 1 - 1}{2} = x$$
$\therefore f^{-1} \circ f = i_X \implies i_{\R}$.
$\forall y \in \R$, $(f \circ f^{-1})(y) = \dots = y$ $\therefore f \circ f^{-1} = i_{\R}$.

## HW 37 — Composition preserves injectivity, surjectivity, bijectivity
_File `20261121_225814.jpg`._

**Composition of functions**

**Th.** If $f : X \to Y$ and $g : Y \to Z$ are both injective, then $g \circ f$ is also injective.
**Proof.** Suppose $f$ and $g$ are injective. Suppose $x_1, x_2 \in X$ and $(g \circ f)(x_1) = (g \circ f)(x_2)$.
Then $g(f(x_1)) = g(f(x_2))$.
Since $g$ is injective, $f(x_1) = f(x_2)$.
Since $f$ is injective, $x_1 = x_2$. $\square$

**Th.** If $f : X \to Y$ and $g : Y \to Z$ are both surjective, then $g \circ f$ is also surjective.
**Proof.** Suppose $f$ and $g$ are surjective. Suppose $z \in Z$.
Since $g$ is surjective, $\exists y \in Y : g(y) = z$.
Since $f$ is surjective, $\exists x \in X : f(x) = y$.
Hence, $\exists x \in X$ such that $(g \circ f)(x) = g(f(x)) = g(y) = z$. $\square$

**Th.** If $f : X \to Y$ and $g : Y \to Z$ are both injective and surjective (i.e. $f$ and $g$ are bijective), then $g \circ f$ is also bijective, and hence possesses an inverse.

## HW 38 — Cardinality; finite and infinite sets
_File `20261121_225820.jpg`._

**Cardinality**
**Def.** The *cardinality* of a set is a measure of how large it is.
For sets $X, Y$, they have the *same cardinality* iff there is a bijection between them. $\abs{X} = \abs{Y}$

**Def.** *Finite sets* either have no elements ($\emptyset$), or one for which there exists a bijection with a set of the form $\{1, 2, \dots, n\}$ for some $n \in \Z^{+}$.

**Def.** *Infinite sets* do not possess a bijection with a set of above.

**Finite sets**
**Th.** Suppose $X$ and $Y$ are finite sets.
1) If $\abs{X} > \abs{Y}$, there does not exist an injective function $f : X \to Y$.
2) If $\abs{X} < \abs{Y}$, there does not exist an ~~injective~~ surjective function $f : X \to Y$.
3) $\abs{X} = \abs{Y} \iff f$ is bijective
These results DO NOT APPLY to infinite sets (e.g. $\Z, \Q, \R$).
[stated without proof]
[possible error: item 3 does not say what $f$ is. Presumably "if $\abs{X} = \abs{Y}$, then $f : X \to Y$ is injective $\iff$ $f$ is surjective $\iff$ $f$ is bijective", or "$\abs{X} = \abs{Y} \iff$ there is a bijection $f : X \to Y$".]

**Infinite sets**
**Th.**
$$\abs{\Z^{+}} = \abs{\Z} = \abs{2\Z}, \qquad \abs{\Z^{+}} = \abs{\Q^{+}}$$
$$\implies \abs{\Z} = \abs{\Z^{+}} = \abs{2\Z} = \abs{\Q^{+}} = \abs{\Q}.$$
The infinite sets between $\Z$ and $\Q$ are equal.
[possible error: imprecise. Presumably "all these sets have the same cardinality". $\abs{\Z^{+}} = \abs{\Z}$ and $\abs{\Q^{+}} = \abs{\Q}$ are not proved in the notes.]

## HW 39 — Infinite set examples: $\abs{\Z} = \abs{2\Z}$, $\abs{\Z^{+}} = \abs{\Q^{+}}$
_File `20261121_225825.jpg`. Contains a figure._

**Infinite set examples**

**Ex.** Let $2\Z = \{n : n = 2k,\ k \in \Z\}$. Prove $\abs{\Z} = \abs{2\Z}$.
**Proof.** Define $f : \Z \to 2\Z$ as $f(k) = 2k$.
*Injective:* Suppose $k_1, k_2 \in \Z$, $f(k_1) = f(k_2)$. Then $2k_1 = 2k_2$, $k_1 = k_2$. Hence $f$ is injective.
*Surjective:* Suppose $n \in 2\Z$. Then $n = 2k$, $k \in \Z$. Hence $f(k) = 2k = n$. Hence $f$ is surjective.
Hence $f$ is a bijection from $\Z$ to $2\Z$, hence $\abs{\Z} = \abs{2\Z}$.

**Ex.** Prove $\abs{\Z^{+}} = \abs{\Q^{+}}$.
**Proof.** Proof by 'paths', geometrically:

**Figure (zigzag enumeration of $\Q^{+}$).** A grid of fractions $i/j$ with row $i = 1, \dots, 5$ (numerator) and column $j = 1, \dots, 5$ (denominator), so row 1 is $\frac11, \frac12, \frac13, \frac14, \frac15$, row 2 is $\frac21, \dots, \frac25$, and so on to row 5. Each row ends with "…" to the right, and each column has a vertical "⋮" below row 5.
Fractions in lowest terms are underlined with a small bracket and numbered (the number is written at the lower right of the bracket). Fractions not in lowest terms ($\frac22, \frac24, \frac33, \frac42$) have no bracket and no number. The numbering is:

| Fraction | $\frac11$ | $\frac12$ | $\frac21$ | $\frac31$ | $\frac13$ | $\frac14$ | $\frac23$ | $\frac32$ | $\frac41$ | $\frac51$ | $\frac15$ | $\frac25$ | $\frac34$ | $\frac43$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

Arrows trace one path through the grid along anti-diagonals:
- $\frac11 \to \frac12$ (right);
- $\frac12 \swarrow \frac21$; $\frac21 \downarrow \frac31$;
- $\frac31 \nearrow \frac22 \nearrow \frac13$; $\frac13 \to \frac14$ (right);
- $\frac14 \swarrow \frac23 \swarrow \frac32 \swarrow \frac41$; $\frac41 \downarrow \frac51$;
- $\frac51 \nearrow \frac42 \nearrow \frac33 \nearrow \frac24 \nearrow \frac15$; $\frac15 \downarrow \frac25$;
- $\frac25 \swarrow \frac34 \swarrow \frac43 \swarrow \frac52$.
To the right of the grid: "Injective: no duplicates of $\Q$ $\implies \Z \to \Q$ inj."
[possible error: at $\frac15$ the path steps down to $\frac25$ because the drawn grid stops at column 5. In the infinite grid the path should continue right to $\frac16$, then down the anti-diagonal $\frac16, \frac25, \frac34, \dots, \frac61$.]

$\implies$ every $x \in \Q^{+}$ is designated $z \in \Z^{+}$
$\implies \abs{\Q^{+}} = \abs{\Z^{+}}$ $\square$

## HW 40 — Countable and uncountable sets; Cantor's diagonal argument
_File `20261121_225833.jpg`._

**Countable and uncountable sets**
**Def.** A set is *countable* iff it is finite or countably infinite.
A set is *countably infinite* iff it shares a cardinality with the set positive integers $\Z^{+}$.
**Ex.** $\Z$, $2\Z$, $\Q^{+}$, $\Q$ are all countably infinite.

**Th.** Any subset of any countable set is countable. Any set with an uncountable subset is uncountable. [stated without proof]

**Th.** The set $\{x \in \R : 0 < x < 1\}$ is uncountable.
**Proof.** Suppose the set is countable. Hence the decimal representations of these numbers can be written in a list:
$$\begin{array}{l}
0.a_{1,1}\,a_{1,2}\,a_{1,3} \dots a_{1,n} \dots \\
0.a_{2,1}\,a_{2,2}\,a_{2,3} \dots a_{2,n} \dots \\
0.a_{3,1}\,a_{3,2}\,a_{3,3} \dots a_{3,n} \dots \\
\vdots
\end{array}$$
We now construct a new decimal as follows:
$$d_n = \begin{cases} 1 & \text{if } a_{n,n} \ne 1 \\ 2 & \text{if } a_{n,n} = 1 \end{cases}$$
Thus, $d \in \{x \in \R : 0 < x < 1\}$, but this is contradictory as due to the construction of $d$.
Therefore $\{x \in \R : 0 < x < 1\}$ is uncountable.
[$d = 0.d_1 d_2 d_3 \dots$ is not written out, nor is the reason for the contradiction: $d$ differs from the $n$-th listed number in the $n$-th digit, so it is not in the list.]

**Th.** Since $(0, 1) \subseteq \R$ and $(0, 1)$ is uncountable, $\R$ is uncountable.
Since we can construct a bijection by $f : \R \to (0, 1)$, $f(x) = \frac{1}{1 + e^x}$, hence $\abs{(0, 1)} = \abs{\R}$. [written $\abs{0, 1}$]

## HW 41 — Comparing cardinalities; the Schröder–Bernstein theorem
_File `20261121_225837.jpg`._

**Comparing cardinalities**
**Th.**
- $\abs{X} \le \abs{Y}$ iff $\exists$ inj. $f : X \to Y$.
- $\abs{X} \ge \abs{Y}$ iff $\exists$ sur. $f : X \to Y$.
- $\abs{X} > \abs{Y}$ iff $\exists$ sur. $f : X \to Y$, $\nexists$ inj. $f : X \to Y$
- $\abs{X} < \abs{Y}$ iff $\exists$ inj. $f : X \to Y$, $\nexists$ sur. $f : X \to Y$

**The Schröder–Bernstein theorem**
**Def.** If $\abs{X} \le \abs{Y}$ and $\abs{X} \ge \abs{Y}$, then $\abs{X} = \abs{Y}$. [stated without proof]
This implies that to show $\abs{X} = \abs{Y}$, we need only prove:
1) $\exists$ inj. $f : X \to Y$ and $\exists$ sur. $f : X \to Y$ (i.e. standard bijectivity)
2) $\exists$ inj. $f : X \to Y$ and $\exists$ inj. $f : Y \to X$ (i.e. two-way injectivity) [a first version is scribbled out]
3) $\exists$ sur. $f : X \to Y$ and $\exists$ sur. $f : Y \to X$ (i.e. two-way surjectivity) [a word before "surjectivity" is scribbled out]
Two-way injectivity and surjectivity can be easier than finding a bijection.
[possible error: in 1), an injection and a (possibly different) surjection $X \to Y$ are not "standard bijectivity"; the conclusion $\abs{X} = \abs{Y}$ follows from Schröder–Bernstein, not from having one bijective map.]

**Ex.** Show $\abs{\Z^{+}} = \abs{\Q^{+}}$ using Schröder–Bernstein.
1) $f : \Z^{+} \to \Q^{+}$, $f(n) = n\ \forall n \in \Z^{+}$ is injective $\implies \abs{X} \le \abs{Y} \implies \abs{\Z^{+}} \le \abs{\Q^{+}}$
2) $g : \Q^{+} \to \Z^{+}$, $g(q) = 2^a 3^b$, where $q = \frac{a}{b}$, $\forall q \in \Q^{+}$, $a, b \in \Z^{+}$, $b \ne 0$, $\gcd(a, b) = 1$.
Let $q_1 = \frac{a}{b}$ and $q_2 = \frac{c}{d}$, suppose $g(q_1) = g(q_2)$. Then $2^a 3^b = 2^c 3^d$.
By unique prime factorisation, $a = c$ and $b = d$.
Hence $q_1 = q_2 \implies g$ is injective [corrected in the notes from "surjective"] $\implies \abs{Y} \le \abs{X} \implies \abs{\Q^{+}} \le \abs{\Z^{+}}$.
By Schröder–Bernstein, $\abs{\Z^{+}} = \abs{\Q^{+}}$. $\square$

## HW 42 — Relations on sets; inverse relations
_File `20261121_225843.jpg`. Contains two figures._

**Relations on sets**
**Def.** For sets $A, B$, a *binary relation* $R$ from $A$ to $B$ is a subset of $A \times B$.
If $x, y \in R$, we also write $xRy$ – $x$ is *related to* $y$.
[possible error: should be "if $(x, y) \in R$".]
**Rem.** If $x$ is related to $y$, $y$ needs not be related to $x$; i.e. $xRy \not\Leftrightarrow yRx$.

**Ex.** Let $A = \{1, 2, 5\}$ and $B = \{5, 6\}$. Define the relation $\sigma$ by $a \,\sigma\, b \iff a < b$ $\forall a \in A, b \in B$.
Then $\sigma = \{(1, 5), (1, 6), (2, 5), (2, 6), (5, 6)\}$.

**Figure (arrow diagram of $\sigma$).** Two tall rounded rectangles side by side. The left one, labelled $A$ underneath, holds dots labelled 1, 2, 5 from top to bottom. The right one, labelled $B$, holds dots labelled 5 (upper) and 6 (lower). Five arrows go from left to right: $1 \to 5$, $1 \to 6$, $2 \to 5$, $2 \to 6$, $5 \to 6$.
To the right: "$\sigma$ is not a function."

**Def.** If $R$ is a binary relation from $A$ to $B$, the *inverse relation* $R^{-1}$ is defined from $B$ to $A$ by:
$$R^{-1} = \{(b, a) \in B \times A \mid (a, b) \in R\}$$
Hence $(b, a) \in R^{-1} \iff (a, b) \in R$.

**Def.** A *relation on a set* $A$ is from $A$ to $A$.
**Ex.** Define the relation $R$ on $\Z$ by: $\forall m, n \in \Z$, $mRn \iff m \mid n$.
Is $2R8$? Yes. Is $5R26$? No.
The inverse relation $R^{-1}$ on $\Z$ is defined by: $\forall m, n \in \Z$, $mR^{-1}n \iff nRm \iff n \mid m$.
Is $2R^{-1}8$? No. Is $8R^{-1}2$? Yes.

**Ex.** Let $R$ be defined on $A = \{2, 3, 6\}$, $\forall a, b \in A$, $aRb \iff a \mid b$.

**Figure (directed graph of $R$).** Three dots: 2 at upper left, 3 at lower left, 6 to the right between them. Each of 2 and 3 has a small loop. Arrows $2 \to 6$ and $3 \to 6$.
[possible error: $6 \mid 6$, so 6 should also have a loop.]

## HW 43 — Reflexive, symmetric and transitive relations
_File `20261121_225847.jpg`._

**Characteristics of relations (reflexivity, symmetry, transitivity)**
**Def.** Let $R$ be a relation on a set $A$.
$R$ is *reflexive* iff $\forall x \in A,\ xRx$
*symmetric* iff $\forall x, y \in A,\ xRy \to yRx$
*transitive* iff $\forall x, y, z \in A$, if $xRy$ and $yRz$ then $xRz$

**Ex.** Consider the relation ($<$) on $\R$.
$R$ is NOT reflexive: $1 \not< 1$.
NOT symmetric: $1 < 2 \not\Rightarrow 2 < 1$.
transitive: If $x < y$ and $y < z$, then $x < z$.

**Ex.** Fix $d \in \Z^{+}$. Consider relation $R$ defined by: $mRn \iff m \equiv n \pmod d$, $\forall m, n \in \Z$.
$R$ is reflexive:
↳ Suppose $m \in \Z$. Then $m - m = 0$, and $d \mid 0$, so $m \equiv m \pmod d$, hence $mRm$. $\square$
$R$ is symmetric:
↳ Suppose $m, n \in \Z$ and $mRn$. Then $m \equiv n \pmod d$, so $d \mid (m - n)$. Hence $d \mid -(m - n)$, so $d \mid (n - m)$.
Thus $n \equiv n \pmod d$, hence $nRm$. $\square$
[possible error: should be $n \equiv m \pmod d$.]
$R$ is transitive:
↳ Suppose $m, n, p \in \Z$, $mRn$, $nRp$. Then $m \equiv n \pmod d$ and $n \equiv p \pmod d$.
Hence $d \mid (m - n)$ and $d \mid (n - p)$.
Thus $d \mid (m - n) + (n - p) \implies d \mid (m - p)$.
Hence $m \equiv p \pmod d$, hence $mRp$. $\square$

## HW 44 — Symmetric iff $R = R^{-1}$
_File `20261121_225852.jpg`. The lower half of the page is blank._

**Characteristics of relations**
**Th.** A relation $R$ on a set $A$ is symmetric iff $R = R^{-1}$.
**Proof.** Let $R$ be a relation on set $A$.
($\Rightarrow$) Suppose $R$ is symmetric. Let $(x, y) \in R$. Since $R$ is symmetric, $(y, x) \in R$.
Hence $(x, y) \in R^{-1}$ by def. of $R^{-1}$. Hence $R \subseteq R^{-1}$. Analogously, $R^{-1} \subseteq R$. $\square$
($\Leftarrow$) Suppose $R = R^{-1}$. Let $(x, y) \in R$. Hence $(y, x) \in R^{-1}$, by def. of $R^{-1}$.
Hence $(y, x) \in R$, since $R = R^{-1}$. Hence $R$ is symmetric. $\square$

## HW 45 — Arrow diagrams of relations on a set
_File `20261121_225856.jpg`. Contains several small figures._

**Relation arrow diagrams (on a set)**
**Def.** If a binary relation is on a set $A$, the arrow diagram can be modified such that $A$ is only represented ONCE, instead of two sets of points.
**Def.** Modified arrow diagrams are drawn by:
↳ draw an arrow from an element's point onto each related element
↳ elements related to themselves are represented by looped arrows
**Ex.** $aRb$: two small circles labelled $a$ and $b$ (labels above), with an arrow from $a$ to $b$. $aRa$: one small circle labelled $a$ with a loop arrow on its right.

**Arrow diagrams and reflexivity, symmetry and transitivity**
**Th.** In terms of the arrow diagram of a relation $R$ on a set $A$:
↳ $R$ is reflexive iff there is a loop on every point of the diagram
↳ $R$ is symmetric iff, if there is an arrow from $x$ to $y$, there is also an arrow from $y$ to $x$.
↳ $R$ is transitive iff, if there is an arrow from $x$ to $y$ and from $y$ to $z$, there is also an arrow from $x$ to $z$.

**Figures beside the theorem (right margin), one per item:**
- Reflexive: a single point with a loop arrow on its left, labelled "$\forall x \in A$".
- Symmetric: point $x$ (upper left) and point $y$ (lower right). A curved arrow from $x$ to $y$ labelled "if" above it, and a curved arrow from $y$ back to $x$ labelled "then" below it.
- Transitive: point $x$ at top left, point $y$ to the right, point $z$ below $x$. Arrow $x \to y$ labelled "if"; arrow $y \to z$ labelled "if"; straight vertical arrow $x \to z$ labelled "then".

**Ex.** (two diagrams, each with its verdict to the right)
1. Three points: one at top left ($p$), one at top right ($r$), one lower in the middle ($q$). Arrows $p \to r$ (straight across the top), $p \to q$ and $q \to r$. A fourth, separate point to the right with a loop. Verdict: "not reflexive, not symmetric, transitive".
2. Three points in a row ($p$, $q$, $r$, left to right), each with a loop. Straight arrows $p \to q$ and $q \to r$ along the row; curved arrows underneath from $q$ back to $p$ and from $r$ back to $q$. Verdict: "not transitive, reflexive, symmetric".
[the point names $p, q, r$ are added here for reference; the points are unlabelled in the notes]

## HW 46 — Equivalence relations and classes
_File `20261121_225902.jpg`._

**Equivalence relations**
**Def.** Let $R$ be a relation on a set $A$. $R$ is an *equivalence relation* iff $R$ is reflexive and symmetric and transitive.

The *equivalence class* of $a$ is: $[a] = \{x \in A : xRa\}$. $\forall x \in A,\ x \in [a] \iff xRa$.
(the set of all elements related to $a$).

**Ex.** Let the relation $R$ be defined on $\Z$ by: $mRn \iff m \equiv n \pmod 3 \iff 3 \mid m - n$.
$R$ is an equivalence relation and
$$[0] = \{\dots, -6, -3, 0, 3, 6, \dots\} = [3] = [6] = \dots$$
$$[1] = \{\dots, -5, -2, 1, 4, 7, \dots\} = [4] = [7] = \dots$$
$$\vdots$$
Hence there are three equivalence classes, one for each remainder. Note $[0] \cap [1] = \emptyset$.

**Lemma.** If $R$ is an equivalence relation on a set $A$, and $a, b \in A$ satisfy $aRb$, then $[a] = [b]$.
**Proof.** Let $R$ be an equivalence relation on a set $A$, and suppose $a, b \in A$ and $aRb$.
$[a] \subseteq [b]$: Let $x \in [a]$, hence $xRa$. $xRa$, $aRb \implies xRb$. Thus $x \in [b]$. $\therefore [a] \subseteq [b]$.
$[b] \subseteq [a]$: Analogous to $[a] \subseteq [b]$, WLOG: Let $x \in [b]$, hence $xRb$. $xRb$, $bRa \implies xRa$. Since $aRb$, $bRa$ by symmetry of $R$. Thus $x \in [a]$. $\therefore [b] \subseteq [a]$.
Therefore $[a] = [b]$. $\square$

## HW 47 — Equivalence classes partition the set
_File `20261121_225906.jpg`. No page heading; continues HW 46._

**Lemma.** If $R$ is an equivalence relation on a set $A$, and $a, b \in A$ and $[a] \cap [b] \ne \emptyset$, then $[a] = [b]$.
**Rem.** An equivalent statement is as follows: If $R$ is an equivalence relation on a set $A$, and $a, b \in A$, then either $[a] \cap [b] = \emptyset$ (i.e. $a \not R b$), else $[a] = [b]$ (i.e. $aRb$).
**Proof.** Suppose $R$ is an equivalence relation on a set $A$, $a, b \in A$, $[a] \cap [b] \ne \emptyset$.
Then $\exists x \in [a] \cap [b] \implies x \in [a]$ and $x \in [b] \implies xRa$ and $xRb$.
Since $R$ is symmetric, $aRx$. $\implies aRx, xRb \implies aRb$.
By the previous Lemma, $[a] = [b]$. $\square$

**Th.** If $R$ is an equivalence relation on a set $A$, then the set of equivalence classes of $R$ forms a partition of $A$.
As a result, the union of all classes is $A$; the intersection of all classes is $\emptyset$.
[possible error: should be "distinct classes are pairwise disjoint"; "the intersection of all classes is $\emptyset$" is weaker, and false when there is only one class.]
[stated without proof; it follows from the two lemmas, but the notes do not say so]

**Ex.** Given an equivalence relation, find a partition:
$mRn \iff m \equiv n \pmod d \iff d \mid m - n$.
Then $\{[0], [1], [2], \dots, [d-1]\}$ is a partition of $\Z$.

**Def.** Given $R$ on $A$, and an equiv. class $A_i$ of $R$, then any element $a \in A_i$ is a *representative* of class $A_i$, i.e. $[a] = A_i$.

**Th.** Given a partition of set $A$, and a binary relation $R$ induced by the partition; $R$ must be reflexive, symmetric + transitive.
The binary relation *induced by the partition* is defined: $\forall x, y \in A$,
$$xRy \iff \exists \text{ a set in the partition } S \text{ s.t. } x, y \in S.$$
[stated without proof]

## HW 48 — Antisymmetric relations; partial order relations
_File `20261121_225913.jpg`. Contains four small figures._

**Antisymmetric relations**
**Def.** A relation $R$ on a set $A$ is *antisymmetric* iff $\forall a, b \in A$, if $aRb$ and $bRa$, then $a = b$.
i.e. $R$ is NOT antisymmetric iff $\exists a, b \in A$, $a \ne b$, such that $aRb$ and $bRa$.
**Rem.** Antisymmetry is NOT a negation of symmetry.

**Ex.** Four arrow diagrams, arranged 2 × 2, each on three points placed as a triangle: apex $T$ at top, $L$ at bottom left, $M$ at bottom right [point names added here; unlabelled in the notes]. Each has its verdict written to its right.
1. (top left) Arrows $L \to T$ and $T \to M$; a loop at $L$. — "not sym., antisym."
2. (top right) Curved arrows both ways between $L$ and $T$, and both ways between $T$ and $M$. — "not antisym., sym."
3. (bottom left) Curved arrows both ways between $L$ and $T$; one arrow $T \to M$. — "not sym., not antisym."
4. (bottom right) Each of the three points has a loop; no other arrows. — "sym, antisym."

Symmetry is independent of antisymmetry.

**Partial order relations**
**Def.** Let $R$ be on $A$. $R$ is a *partial order relation* iff $R$ is reflexive, antisymmetric and transitive.

**Ex.** Consider '$\le$' on $\R$.
$\forall x \in \R,\ x \le x$ (reflexive)
$\forall x, y \in \R$, if $x \le y$ and $y \le x$, $x = y$ (antisym.)
$\forall x, y, z \in \R$, if $x \le y$, $y \le z$, $x \le z$ (transitive)
$\therefore \le$ is a partial order relation on $\R$.

**Ex.** The subset relation $\subseteq$ on $\powerset(A)$ is a p. order relation:
$\forall X \in \powerset(A),\ X \subseteq X$
$\forall X, Y \in \powerset(A)$, if $X \subseteq Y$ and $Y \subseteq X$, $X = Y$
$\forall X, Y, Z \in \powerset(A)$, if $X \subseteq Y$, $Y \subseteq Z$, $X \subseteq Z$.
$\therefore \subseteq$ is a partial order relation on a set $A$. [i.e. on $\powerset(A)$]

## HW 49 — Comparable elements; total order relations
_File `20261121_225917.jpg`._

**Comparable elements**
**Def.** Let $R$ be on $A$. Elements $a, b \in A$ are *comparable* iff $aRb$ or $bRa$. Otherwise, they are *non-comparable*.
**Ex.** Consider '$\subseteq$' on $\powerset(A)$ where $A = \{1, 2, 3, 4\}$.
$\{1, 2\}$ and $\{1, 2, 3\}$ are comparable: $\{1, 2\} \subseteq \{1, 2, 3\}$.
$\{1, 2\}$ and $\{1, 4\}$ are non-comparable: $\{1, 2\} \not\subseteq \{1, 4\}$, $\{1, 4\} \not\subseteq \{1, 2\}$.

**Def.** Let $R$ be on $A$. $R$ is a *total order relation* on $A$ iff $R$ is a partial order relation s.t. all elements are comparable.
i.e. $R$ is reflexive, antisymmetric and transitive.
[possible error: the "i.e." restates the partial order conditions only; "and any two elements are comparable" is missing.]

**Ex.** Consider '$\mid$' defined on $A = \{1, 2, 4, 8, 16\}$. Is it a t.o. relation?
*Reflexive:* $\forall a \in A,\ a \mid a$ true, since $a = a \cdot 1$.
*Antisym.:* Suppose $a, b \in A$, $a \mid b$, $b \mid a$. Thus $b = ka$, $a = \ell b$ for some $k, \ell \in \Z^{+}$.
$\implies b = k\ell b \implies 1 = k\ell$ ($\because 0 \notin A$) $\implies k = \ell = 1$, thus $a = b$. $\therefore$ true
*Transitive:* Suppose $a, b, c \in A$, $a \mid b$ and $b \mid c$. Then $b = ka$, $c = \ell b$ for some $k, \ell \in \Z$. Thus $c = \ell k a \implies a \mid c$. $\therefore$ true.
Thus '$\mid$' on $A = \{1, 2, 4, 8, 16\}$ is a p.o. relation.

Let $a, b \in A$. Then $a = 2^k$, $b = 2^\ell$ for some $k, \ell \in \{0, 1, 2, 3, 4\}$. WLOG, assume $k \le \ell$.
Then $b = 2^\ell = 2^k \cdot 2^{\ell - k}$ where $\ell - k \in \{0, 1, 2, 3, 4\}$.
Since $2^{\ell - k} \in \Z$, $2^k \mid b$, hence $a \mid b$. $\implies aRb$.
Thus, $\forall a, b \in A$, $a$ and $b$ are comparable. Therefore '$\mid$' is a total order relation.
