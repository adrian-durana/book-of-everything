# MATH1061 Discrete Mathematics: transcription, part 3 of 3 (HW 50–77)

_Transcription phase. Source: 77 photos of the handwritten notes (one notebook page per photo), taken in shooting order. "HW nn" is the photo number nn in shooting order; the file name is given under each heading. No typed notes or slides were supplied. Course taken in one semester; no dates are recorded here (several pages carry a "Lecture notes" date header, which is omitted)._

**Conventions.** Wording, structure and labels (Def., Th., Lemma, Proof/P., Ex., Rem., Cor.) follow the notes. Maths uses `notation.tex` macros where they exist (`\Z`, `\Q`, `\R`, `\N`, `\abs`, `\powerset`, `\T`). Logical "not" is kept as the notes' $\sim$. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected); `[illegible]` would mark unreadable text (none needed). Crossed-out text is noted only where it carries meaning. Figures are described in enough detail to redraw in TikZ.

**This part:** groups, subgroups, isomorphisms, fields, counting, probability, binomial coefficients, inclusion–exclusion, pigeonhole principle, graph theory.

---

## HW 50 — Groups
_File `20261121_225924.jpg`. Heading "Groups and properties of groups (supertopic)". In the notes "$\circ$" is used for multiplication._

**Def.** Let $G$ be a set, and let $*$ be a binary operation $* : G \times G \to G$. We call $(G, *)$ a *group* iff it has the following properties:
1) Closure: $\forall g, h \in G,\ g * h \in G$
2) Associative: $\forall g, h, k \in G,\ g * (h * k) = (g * h) * k$
3) Identity: $\exists e \in G : e * g = g * e = g\ \forall g \in G$
4) Inverses: $\exists g^{-1} \in G : g * g^{-1} = g^{-1} * g = e\ \forall g \in G$
[the quantifier order in 4) should read "$\forall g \in G\ \exists g^{-1} \in G$"; as written the trailing "$\forall g$" makes this ambiguous]
**Rem.** $* : G \times G \to G$ implies closure – still need to check!

**Ex.** $(\Z, +)$ is a group.
1) $+ : \Z \times \Z \to \Z$ is closed: $a + b \in \Z\ \forall a, b \in \Z$
2) $a + (b + c) = (a + b) + c$, so $(\Z, +)$ is associative
3) $\forall n \in \Z$, 0 satisfies the identity element, so $(\Z, +)$ has an identity element
4) $\forall n \in \Z$, $(-n)$ satisfies the inverse, so $(\Z, +)$ has an inverse element

**Ex.** $(\R, \circ)$ is not a group.
1) $\circ : \R \times \R \to \R$ is closed
2) $(\R, \circ)$ is associative
3) $1 \in \R$ satisfies the identity element
4) Take $x \in \R$. $x \cdot y = 1$, $\forall y \in \R$ $\implies y = \frac{1}{x}$, undef. $x = 0$.
So $0 \in \R$ has no inverse. $\implies (\R, \circ)$ is not a group.

## HW 51 — $\Z_n$; $(\Z_3, +)$; non-examples in $\Z_4$
_File `20261121_225927.jpg`. **The last line is cut off at the right edge of the photo.**_

**Ex.** $\Z_n :=$ the equivalence classes of integers modulo $n$. $\Z_n = \{[0], [1], [2], \dots, [n-1]\}$.
Define $+ : \Z_n \times \Z_n \to \Z_n$ by $[a] + [b] = [a + b]$; $\circ : \Z_n \times \Z_n \to \Z_n$ by $[a] \circ [b] = [a \circ b]$.
[the notes do not show that these operations are well defined]

**Ex.** Consider $(\Z_3, +)$. i.e. $[0] + [2] = [2]$, $[1] + [2] = [3] = [0]$.
We can make an addition table for $\Z_3$:

| $+$ | $[0]$ | $[1]$ | $[2]$ |
|---|---|---|---|
| $[0]$ | $[0]$ | $[1]$ | $[2]$ |
| $[1]$ | $[1]$ | $[2]$ | $[0]$ |
| $[2]$ | $[2]$ | $[0]$ | $[1]$ |

closure ✓; associative ✓; identity: $[0]$ ✓; inverses: $[0]^{-1} = [0]$, $[1]^{-1} = [2]$ [$[2]^{-1} = [1]$ is not written]
$\therefore (\Z_3, +)$ is a group.

**Ex.** $(\Z_4, \circ)$ is NOT a group – no inverse for $[0]$.
$(\Z_4 - \{0\}, \circ)$ is NOT a group – not closed, $[2] \circ [2] =$ [cut off at the right edge of the photo; presumably $[0]$, but not visible]

## HW 52 — Bijections of $\R$ under composition; abelian groups; symmetric group
_File `20261121_225933.jpg`._

**Ex.** Consider the set of:
↳ all bijections from $\R$ to $\R$.
↳ the operation $\circ$ – function composition.
1) closure: the composition of two bijections from $\R$ to $\R$ is itself a bijection from $\R$ to $\R$. ✓
2) associative: Let $f, g, h$ be bijections from $\R$ to $\R$. Then $\forall x \in \R$,
$$((f \circ g) \circ h)(x) = f(g(h(x))) = (f \circ (g \circ h))(x) \implies (f \circ g) \circ (h) = (f) \circ (g \circ h) \ ✓$$
3) identity: $i_{\R}$ is the identity function on $\R$. $\implies i_{\R}(x) = x$. For any bijection $f$ from $\R$ to $\R$, $i_{\R} \circ f = f \circ i_{\R} = f$. ✓
4) inverses: If a function is bijective, there exists an inverse. ✓

**Rem.** Note that $f \circ g \ne g \circ f \implies$ composition is not commutative. Groups need not be commutative.

**Def.** A group $(G, *)$ is *abelian* if $*$ is commutative: $\forall g, h \in G,\ g * h = h * g$. Otherwise, $(G, *)$ is *non-abelian*.

**Def.** The *symmetric group* $S_n$ consists of all bijections $f : X \to X$ where $X = \{1, 2, \dots, n\}$, $n \in \N$.
For $n \ge 3$, $S_n$ is non-abelian. [stated without proof]

## HW 53 — Uniqueness of identity and inverses
_File `20261121_225937.jpg`. "P." is used for "Proof"._

**Th.** The identity element in a group is unique.
**P.** Suppose $(G, *)$ has two identity elements $e_1, e_2$. We now evaluate $e_1 * e_2$ two ways:
1) Since $e_1$ is an identity, $e_2 \in G$, then $e_1 * e_2 = e_2$
2) Since $e_2$ is an identity, $e_1 \in G$, then $e_1 * e_2 = e_1$
$\implies e_1 = e_2$ $\implies$ The identity element in a group is unique. $\square$

**Th.** The inverse of every element in a group is unique.
**P.** Suppose $(G, *)$ has an element $g \in G$ such that $g$ has two inverses $h_1, h_2$. Let $e$ be the identity element.
We evaluate $h_1 * g * h_2$ two ways:
1) $(h_1 * g) * h_2 = e * h_2 = h_2$
2) $h_1 * (h_2 * g) = h_1 * e = h_1$
[possible error: should be $h_1 * (g * h_2)$, to match $h_1 * g * h_2$.]
By associativity, (1) = (2) $\implies h_1 = h_2$ $\implies$ Each element has a unique inverse. $\square$

## HW 54 — Subgroups; subgroups of $(\Z_6, +)$
_File `20261121_225944.jpg`. In this example the classes $[k]$ of $\Z_6$ are written without brackets as $k$._

**Subgroups**
**Def.** Let $(G, *)$ be a group, let $H \subseteq G$. If $(H, *)$ is a group, $H$ is a *subgroup* of $G$.
i.e. $H$ is a subgroup of $G$ if:
1) $\forall g, h \in H,\ g * h \in H$ (closure)
2) if $e$ is id. of $(G, *)$, then $e \in H$ (identity)
3) $\forall h \in H$, if $h^{-1}$ is the inverse of $h$ in $(G, *)$, then $h^{-1} \in H$ (inverse)
**Rem.** The property of associativity is inherited. i.e. $(H, *)$ is associative.

**Def.** When group context is clear, we write $H \le G$. If $H \le G$ and $H \ne G$, $H$ is a *proper subgroup* of $G$.
If $e$ is the identity of group $G$, the *trivial subgroup* of $G$ is $\{e\}$.
[the subgroup symbol is handwritten between $\le$ and $\subseteq$; read as $\le$]

**Ex.** Find all subgroups of $(\Z_6, +)$.

| $+$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 2 | 3 | 4 | 5 | 0 |
| 2 | 2 | 3 | 4 | 5 | 0 | 1 |
| 3 | 3 | 4 | 5 | 0 | 1 | 2 |
| 4 | 4 | 5 | 0 | 1 | 2 | 3 |
| 5 | 5 | 0 | 1 | 2 | 3 | 4 |

$H_1 = \{0\}$ is the trivial subgroup.
$H = \{0, 1\}$ is NOT a subgroup: $1 + 1 = 2 \notin H$.
$H_2 = \{0, 3\}$ is a subgroup: $0 + 0 = 0$, $0 + 3 = 3$, $3 + 3 = 0$, closure ✓; $0 \in H_2$ identity ✓; $0^{-1} = 0 \in H_2$, $3^{-1} = 3 \in H_2$, inverses ✓.
$H_3 = \{0, 2, 4\}$ and $H_4 = \{0, 1, 2, 3, 4, 5\} = \Z_6$ are the two remaining subgroups.
[the notes do not show why there are no others]

## HW 55 — Powers of elements; cyclic subgroups
_File `20261121_225949.jpg`._

**Powers of elements**
**Def.** Let $(G, *)$ be a group. By associativity, $(x * y) * z = x * (y * z)$ $\forall x, y, z \in G$, and thus $x * y * z$ is non-ambiguous.
Given a group $(G, *)$ and an element $g \in G$, we define powers of $g$ as follows:
$$g^k : g * g * g \ (k \text{ times}),\ k \in \Z^{+}; \qquad g^{-k} : g^{-1} * g^{-1} * g^{-1} \ (k \text{ times}),\ k \in \Z^{+}; \qquad g^0 : \text{the identity of } (G, *)$$
$$g^i * g^j = g^{i+j} \quad \text{and} \quad (g^i)^{-1} = g^{-1} \quad \forall i, j \in \Z$$
[possible error: should be $(g^i)^{-1} = g^{-i}$.]

**Cyclic subgroups**
**Def.** Let $a \in G$ be an element of a group $(G, *)$.
$$\langle a \rangle = \{a^k \mid k \in \Z\} = \{\dots, a^{-2}, a^{-1}, e, a^1, a^2, \dots\}$$
$\langle a \rangle$ is the *cyclic subgroup* of $G$ *generated by* $a$. If $G = \langle a \rangle$ for some $a \in G$, we say $G$ is *cyclic*.
[that $\langle a \rangle$ is a subgroup is not proved]

**Ex.** The subgroups of $(\Z_6, +)$ are all cyclic.
$H_1 = \{0\} = \langle 0 \rangle$, $H_2 = \{0, 3\} = \langle 3 \rangle$, $H_3 = \{0, 2, 4\} = \langle 2 \rangle$, $H_4 = \{0, 1, 2, 3, 4, 5\} = \langle 1 \rangle$.

## HW 56 — Group isomorphisms
_File `20261121_225954.jpg`. Contains four tables (Cayley tables) and a symbol key._

**Group isomorphisms**
**Ex.** Informally, consider the groups $(\Z_4, +)$ and $(\Z_5 \setminus \{0\}, \circ)$.

| $+$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
|---|---|---|---|---|
| $[0]$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
| $[1]$ | $[1]$ | $[2]$ | $[3]$ | $[0]$ |
| $[2]$ | $[2]$ | $[3]$ | $[0]$ | $[1]$ |
| $[3]$ | $[3]$ | $[0]$ | $[1]$ | $[2]$ |

| $\circ$ | $[1]$ | $[2]$ | $[3]$ | $[4]$ |
|---|---|---|---|---|
| $[1]$ | $[1]$ | $[2]$ | $[3]$ | $[4]$ |
| $[2]$ | $[2]$ | $[4]$ | $[1]$ | $[3]$ |
| $[3]$ | $[3]$ | $[1]$ | $[4]$ | $[2]$ |
| $[4]$ | $[4]$ | $[3]$ | $[2]$ | $[1]$ |

Below each table is a double-headed vertical arrow ↕ pointing to a relabelled version:

Left, $(\Z_4, +)$ with symbols ○ = $[0]$, ♡ = $[1]$, □ = $[2]$, △ = $[3]$:

| $+$ | ○ | ♡ | □ | △ |
|---|---|---|---|---|
| ○ | ○ | ♡ | □ | △ |
| ♡ | ♡ | □ | △ | ○ |
| □ | □ | △ | ○ | ♡ |
| △ | △ | ○ | ♡ | □ |

Right, $(\Z_5 \setminus \{0\}, \circ)$ with rows and columns reordered as $1, 2, 4, 3$:

| $\circ$ | 1 | 2 | 4 | 3 |
|---|---|---|---|---|
| 1 | 1 | 2 | 4 | 3 |
| 2 | 2 | 4 | 3 | 1 |
| 4 | 4 | 3 | 1 | 2 |
| 3 | 3 | 1 | 2 | 4 |

Key at the far right: $1 \cdot$ ○, $2 \cdot$ ♡, $3 \cdot$ △, $4 \cdot$ □. [the reordered table, read through this key, is the same as the symbol table on the left]

**Def.** Two groups $(G, *)$ and $(H, \circ)$ are *isomorphic* iff there exists a bijection $f : G \to H$ s.t. $\forall x, y \in G$,
$$f(x * y) = f(x) \circ f(y).$$
Such a bijection is called an *isomorphism*.
**Rem.** If $f : G \to H$ is an isomorphism, and $e \in G$ and $\varepsilon \in H$ are the corresponding identity elements, $f(e) = \varepsilon$. [stated without proof; the symbol for the identity of $H$ looks like "ε" or "z"]
**Rem.** If $G$ and $H$ are isomorphic, they must share the same properties: i.e. number of elements; abelian / commutative; number of subgroups etc.

## HW 57 — An explicit isomorphism; non-isomorphisms; Chinese remainder theorem
_File `20261121_225959.jpg`._

**Ex.** Show that $(\Z_4, +)$ and $(\Z_5 - \{0\}, \circ)$ are isomorphic.
$$[0]_4 \mapsto [1]_5, \quad [1]_4 \mapsto [2]_5, \quad [2]_4 \mapsto [4]_5, \quad [3]_4 \mapsto [3]_5$$
[the last two images are written over earlier digits; the values follow from the formula $[2]_5^k$]
Define $f : \Z_4 \to \Z_5 \setminus \{0\}$, $f([k]_4) = [2]_5^k$ $\forall [k]_4 \in \Z_4$.
The function $f$ is a bijection.
Let $[a]_4, [b]_4 \in \Z_4$. Then
$$f([a]_4 + [b]_4) = f([a + b]_4) = [2]_5^{a+b}, \qquad f([a]_4) \circ f([b]_4) = [2]_5^a \circ [2]_5^b = [2]_5^{a+b}$$
Therefore $f$ is an isomorphism.
[the notes do not check that $f$ is well defined, i.e. independent of the representative $k$ (this uses $[2]_5^4 = [1]_5$)]

**Th.** For any prime $p$, $(\Z_p \setminus \{0\}, \circ)$ is isomorphic to $(\Z_{p-1}, +)$. [stated without proof]

**Examples of non-isomorphisms**
- $(\Z, +)$ and $(\R \setminus \{0\}, \circ)$: not isomorphic, $\nexists$ bijection
- $(\Z_{12}, +)$ and $(\Z_{11} \setminus \{0\}, \circ)$: differing # of elements (12 vs. 10)
- $(\Z_6, +)$ and $(S_3)$: $\Z_6$ is abelian, $S_3$ is non-abelian

**Cartesian product isomorphisms – Chinese remainder theorem.**
**Th.** $(\Z_n \times \Z_m, +)$ is isomorphic to $(\Z_{mn}, +)$ iff $\gcd(n, m) = 1$. [stated without proof; the operation on $\Z_n \times \Z_m$ is not defined in the notes]
i.e. modular arithmetic for large numbers e.g. $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$ (prime factorisation) can be done as arithmetic modulo the prime powers $p_i^{e_i}$ (useful for applications e.g. cryptography).

## HW 58 — Cartesian product isomorphisms
_File `20261121_230004.jpg`. Contains two Cayley tables with markings._

**Cartesian product isomorphisms**
**Ex.** Consider the product $\Z_2 \times \Z_3 = \{(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)\}$.
1) Define addition by: $(a, b) + (c, d) = (a + c, b + d)$ $\forall (a, b), (c, d) \in \Z_2 \times \Z_3$
2) Define $f : \Z_6 \to \Z_2 \times \Z_3$ by $f(x) = (x, x)$ [i.e. ($x \bmod 2$, $x \bmod 3$)]
↳ $f(0) = (0, 0)$, $f(1) = (1, 1)$, $f(2) = (0, 2)$, $f(3) = (1, 0)$, $f(4) = (0, 1)$, $f(5) = (1, 2)$
$\therefore f$ is a bijection, and
$$f(x + y) = (x + y, x + y), \qquad f(x) + f(y) = (x, x) + (y, y) = (x + y, x + y)$$
$\therefore f$ is an isomorphism.

**Ex.** Are $(\Z_2 \times \Z_2, +)$ and $(\Z_4, +)$ isomorphic?

| $+$ | $(0,0)$ | $(0,1)$ | $(1,0)$ | $(1,1)$ |
|---|---|---|---|---|
| $(0,0)$ | $(0,0)$ | $(0,1)$ | $(1,0)$ | $(1,1)$ |
| $(0,1)$ | $(0,1)$ | $(0,0)$ | $(1,1)$ | $(1,0)$ |
| $(1,0)$ | $(1,0)$ | $(1,1)$ | $(0,0)$ | $(0,1)$ |
| $(1,1)$ | $(1,1)$ | $(1,0)$ | $(0,1)$ | $(0,0)$ |

Marking: a straight line is drawn through the main diagonal of this table, joining the four $(0,0)$ entries (each lightly circled).

| $+$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
|---|---|---|---|---|
| $[0]$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
| $[1]$ | $[1]$ | $[2]$ | $[3]$ | $[0]$ |
| $[2]$ | $[2]$ | $[3]$ | $[0]$ | $[1]$ |
| $[3]$ | $[3]$ | $[0]$ | $[1]$ | $[2]$ |

Marking: the diagonal entries $[2]$ (row $[1]$) and $[2]$ (row $[3]$) are underlined with a bracket, showing that the diagonal is not all $[0]$.

Any isomorphism $f : \Z_2 \times \Z_2 \to \Z_4$ sends $(0, 0) \mapsto 0$.
↳ $\forall x \in \Z_2 \times \Z_2$ has property $x + x = (0, 0)$
↳ NOT ALL $x \in \Z_4$ has property $x + x = 0$
Therefore there is no bijection between the two groups $\implies$ not isomorphic. ($\gcd(2, 4) = 2 \ne 1$)
[possible error: there are bijections between the two sets (both have 4 elements); the argument shows there is no *isomorphism*. Also the CRT condition for $\Z_2 \times \Z_2$ vs $\Z_4$ is $\gcd(2, 2) = 2 \ne 1$, not $\gcd(2, 4)$.]

## HW 59 — Fields
_File `20261121_230008.jpg`. "(1071)" in the notes refers to the course MATH1071._

**Fields**
**Def.** A *field* $F$ $(F, +, \circ)$ is a set $F$ with two binary operations $+ : F \times F \to F$, $\circ : F \times F \to F$ such that:
1) $(F, +)$ is an abelian group, identity denoted by 0
2) $(F - \{0\}, \circ)$ is an abelian group
3) The distributive laws hold.

**Ex.** $(\R, +, \circ)$ and $(\C, +, \circ)$ are both fields.
**Ex.** $(\Q, +, \circ)$ is a field – check the field axioms (1071).
**Ex.** $(\Z_6, +, \circ)$ is NOT a field:
↳ $(\Z_6, +)$ is an abelian group, identity $[0]$.
↳ $(\Z_6 \setminus \{0\}, \circ)$ is NOT a group: $[2] \circ [3] = [0] \notin \Z_6 \setminus \{0\}$.
$\implies \Z_6$ is not a field.

**Th.** If $p$ is prime, then $\Z_p$ is a field. (1071) [stated without proof]

**Rem.** Fields allow us to solve equations the same way we are used to solving them, in $(\R, +, \circ)$. Fields are also used:
↳ in linear algebra – the components of vectors and matrices can be elements of any field.
↳ in comp. science – finite fields like $\Z_2$, $\Z_5$ behave like reals, but are stored and defined precisely using a finite number of bits.
↳ number theory, cryptography, coding theory, combinatorics, analysis and other areas of maths.

## HW 60 — Permutations
_File `20261121_230014.jpg`._

**Permutations**
**Def.** A *permutation* of a set of objects is an arrangement of the objects into an order.
For any $n \in \Z^{+}$, the number of permutations of a set with $n$ elements is $n!$ [underlined; stated without proof]

**Ex.** Consider the permutations of the letters of OBJECTS. How many permutations are there?
↳ $7! = 5040$
How many permutations start with a vowel?
↳ seven blanks filled as $2 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 2 \cdot 6! = 1440$; an arrow under the first factor 2 is labelled "O or E", an arrow under the second factor 6 is labelled "regardless of choice".

**Ex.** Consider all licence plates consisting of:
↳ 3 digits from the set $\{0, 1, 2, \dots, 9\}$
↳ 3 letters from the set $\{A, B, C, \dots, Z\}$
How many license plates are possible?
↳ $10^3 \cdot 26^3 = 17{,}576{,}000$
How many licence plates have no repeated symbols?
↳ $10 \cdot 9 \cdot 8 \cdot 26 \cdot 25 \cdot 24 = 11{,}232{,}000$
How many licence plates have one repeated symbol?
↳ total number: 17,576,000
↳ no repeated symbols: 11,232,000
↳ the remaining 6,344,000 must have at least one repeated symbol.
[possible error: the question asks for "one repeated symbol" but the answer counts "at least one repeated symbol".]

## HW 61 — Introduction to counting; counting selections
_File `20261121_230018.jpg`._

**Introduction to counting**
**Ex.** Suppose a restaurant has: ↳ 4 types of ice-cream ↳ 2 types of cookies to select for dessert.
If you select one ice-cream and one cookie, there are $4 \cdot 2 = 8$ choices.
If you select EITHER one ice-cream or one cookie, there are $4 + 2 = 6$ choices.

**Counting selections**
**Ex.** Select $r$ elements from a set containing $n$ elements. How many ways are there to do the selection? The answer depends on:
↳ whether order matters
↳ whether repetition is allowed

Case 1: order matters, repetition is allowed [a crossed-out word before "matters"]
↳ the number of selections of $r$ elements from a set containing $n$ elements is $n^r$.
↳ example: selecting a PIN
Case 2: order matters, repetition is NOT allowed ["NOT" inserted above the line]
↳ the number of selections is the $r$-permutations $P(n, r)$ or ${}_nP_r$
↳ example: how many ways can 1st, 2nd, 3rd be selected?

**Def.** $r$-permutation: $\dfrac{n!}{(n - r)!}$

## HW 62 — Combinations; permutations with repeated letters
_File `20261121_230024.jpg`._

**Counting selections**
**Ex.** Case 3: order does not matter, repetition NOT allowed ["NOT" inserted above the line]
↳ the number of selections is the $r$-combinations $C(n, r)$ or ${}_nC_r$, or $\binom{n}{r}$
↳ example: how many ways can a group of 5 be selected from a group of 10?

**Def.** $r$-combination:
$$\binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!(n - r)!}$$

**Ex.** Case 4: order does not matter, repetition allowed [a crossed-out word before "allowed"]
↳ this case is substantially more difficult, so a general solution will not be given.
↳ example: suppose there are five available flavours of ice cream, of which you can have three scoops. how many variations are there? [not answered in the notes]

**Ex.** How many permutations of the letters of ALFALFA are there?
↳ Method 1: (seven blanks drawn)
1) select positions for 3 A's $\binom{7}{3}$
2) select positions for 2 F's $\binom{4}{2}$
3) put 2 L's in remaining positions $\binom{2}{2} = 1$
Answer: $\binom{7}{3} \cdot \binom{4}{2} \cdot 1 = 210$
↳ Method 2: $A_1 A_2 A_3 F_1 F_2 L_1 L_2$
1) all letters distinct, $7!$ possibilities
2) if 3 A's indistinguishable, $\frac{7!}{3!}$ possibilities
3) if above + 2 F's indist., then $\frac{7!}{3!\,2!}$ possibilities
4) if above + 2 L's indist., then $\frac{7!}{3!\,2!\,2!} = 210$

## HW 63 — Introduction to probability
_File `20261121_230030.jpg`._

**Introduction to probability**
**Def.** A process is *random* if, when it takes place, one outcome from some set of possible outcomes will occur, but it is impossible to predict with certainty which outcome it will be.
**Def.** A *sample space* is the set of all possible outcomes of a random process.
**Ex.** The sample space for the experiment of flipping two fair coins is $S = \{HH, HT, TH, TT\}$.
**Th.** An *event* is a subset of a sample space. [labelled "Th." but is a definition]

Let $S$ be a finite sample space, in which all outcomes are equally likely. If $E$ is an event in $S$, the probability of $E$ – $P(E)$ – is:
$$P(E) = \frac{\text{number of outcomes in } E}{\text{number of outcomes in } S} = \frac{\abs{E}}{\abs{S}}$$
For any event $E$, $0 \le P(E) \le 1$.

**Ex.** A fair coin is tossed seven times. $S = 2^7$
[possible error: should be $\abs{S} = 2^7$.]
What is the probability we get exactly 5 heads?
$$P(5 \text{ heads}) = \frac{\binom{7}{5}}{2^7} = \frac{21}{128}$$
What is the probability we get at least 5 heads?
$$P(\ge 5 \text{ heads}) = \frac{\binom{7}{5} + \binom{7}{6} + \binom{7}{7}}{128} = \frac{29}{128}$$

## HW 64 — Probability examples: same suit; birthday problem
_File `20261121_230034.jpg`._

**Probability examples**
**Ex.** Suppose three cards are drawn at random from a standard deck of cards. What is the probability that all three cards have the same suit?
$S$ – set of all possible selections of 3 cards out of 52 cards. Order does not matter, repetition not allowed $\implies \abs{S} = \binom{52}{3}$
$E$ – set of three card selections with identical suit. Step 1: select a suit. Step 2: select three cards of chosen suit.
$$\implies \abs{E} = \binom{4}{1}\binom{13}{3} \implies P(E) = \frac{\binom{4}{1}\binom{13}{3}}{\binom{52}{3}} = \frac{1144}{22100} \approx 0.05$$

**Ex.** Suppose there are 23 people in a room – what is the probability that at least 2 people share a birthday?
$S$ – set of all possible ordered lists of birthdays for the 23 people $\implies \abs{S} = 365^{23}$
$E$ – event that at least 2 people share a birthday $\implies E^c$ – event that there are no shared birthdays
$\abs{E^c} = 365 \cdot 364 \cdot \dots \cdot 343$, $\abs{E} = \abs{S} - \abs{E^c}$
$$\implies P(E) = \frac{\abs{S} - \abs{E^c}}{\abs{S}} = 1 - \frac{\abs{E^c}}{\abs{S}} = 1 - \frac{365 \cdot 364 \cdots}{365^{23}} = 1 - 0.493 = 0.507$$

## HW 65 — Binomial coefficients; symmetry; Pascal's formula
_File `20261121_230042.jpg`._

**Binomial coefficients**
**Def.**
$$\binom{n}{r} = \#\text{ of subsets of } S \text{ with exactly } r \text{ elements} = \frac{n!}{r!(n - r)!}, \qquad n, r \in \Z^{+},\ \abs{S} = n$$
This is called a *binomial coefficient*.

**Th.** $\binom{n}{r} = \binom{n}{n - r}$
**Proof.**
$$\binom{n}{n - r} = \frac{n!}{(n - r)!\,(n - (n - r))!} = \frac{n!}{(n - r)!\,r!} = \binom{n}{r}$$
**P2.** Choosing a subset $A \subseteq S$ (what to take) is equivalent to choosing a subset $S - A$ (what to leave behind).

**Th.** $\binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r}$, i.e. *Pascal's formula*
**Proof.**
$$\begin{aligned}
\binom{n}{r-1} + \binom{n}{r} &= \frac{n!}{(r-1)!\,(n - r + 1)!} + \frac{n!}{r!\,(n - r)!} \\
&= \frac{r\,n!}{r!\,(n - r + 1)!} + \frac{n!\,(n - r + 1)}{r!\,(n - r + 1)!} \\
&= \frac{r\,n! + n\,n! - r\,n! + n!}{r!\,(n - r + 1)!} \\
&= \frac{n!\,(n + 1)}{r!\,(n + 1 - r)!} = \frac{(n + 1)!}{r!\,(n + 1 - r)!} = \binom{n+1}{r} \qquad \square
\end{aligned}$$

## HW 66 — Binomial theorem
_File `20261121_230047.jpg`. The lower half of the page is blank._

**Binomial theorem**
**Def.** Given $a, b \in \R$, $n \in \Z^{+}$,
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} \cdot b^k = a^n + \binom{n}{1} a^{n-1} b + \binom{n}{2} a^{n-2} b^2 + \dots + \binom{n}{n-1} a b^{n-1} + b^n$$
**P.** See UQ Extend lecture 40. [no proof in the notes; this points to the course's online lecture]

**Ex.**
$$(x + y)^4 = \sum_{k=0}^{4} \binom{4}{k} x^{4-k} \cdot y^k = \binom{4}{0}x^4 + \binom{4}{1}x^3y^1 + \binom{4}{2}x^2y^2 + \binom{4}{3}x \cdot y^3 + \binom{4}{4}y^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4$$

## HW 67 — Inclusion–exclusion
_File `20261121_230053.jpg`. Contains two Venn diagrams. The lower third of the page is blank._

**Inclusion–exclusion**
**Def.** For any finite sets $A$ and $B$,
$$\abs{A \cup B} = \abs{A} + \abs{B} - \abs{A \cap B}$$

**Figure (two-set Venn diagram).** Two overlapping circles, $A$ on the left and $B$ on the right, labels above. The parts of $A$ outside $B$ and of $B$ outside $A$ are hatched with diagonal lines; the lens $A \cap B$ is left blank.

Recall that if $A$ and $B$ are disjoint, $\abs{A \cup B} = \abs{A} + \abs{B}$.
By definition, $\abs{A \cap B} = 0$, so the inclusion–exclusion principle works for sets regardless if they are disjoint.

**Def.** For any finite sets $A, B, C$,
$$\abs{A \cup B \cup C} = \abs{A} + \abs{B} + \abs{C} - \abs{A \cap B} - \abs{B \cap C} - \abs{A \cap C} + \abs{A \cap B \cap C}$$
[both formulas are stated without proof]

**Figure (three-set Venn diagram).** Three overlapping circles: $A$ at the top (label above), $B$ at the lower left (label to its left), $C$ at the lower right (label below right). Diagonal hatching fills the parts of each circle that lie in only that set, and also the regions $A \cap C$ (outside $B$) and $B \cap C$ (outside $A$). The region $A \cap B$ (outside $C$) is left blank. The central region $A \cap B \cap C$ is shaded densely (almost solid).
[the shading is not explained in the notes and does not follow an obvious pattern; it may be incomplete. Check before redrawing.]

## HW 68 — Pigeonhole principle
_File `20261121_230057.jpg`._

**Pigeonhole principle**
**Def.** Suppose you have $n$ pigeons sitting in $k$ pigeonholes. If $n > k$, then at least one pigeonhole contains at least two pigeons.

The *contrapositive* of the pigeonhole principle is: If each pigeonhole contains at most one pigeon, then $n \le k$.

Equivalently, a function from $A$ to $B$, $\abs{A} < \abs{B}$ cannot be injective.
[possible error: should be $\abs{A} > \abs{B}$ (more pigeons than holes).]

**Ex.** Show that in every group of $n$ people, there are at least two people who have the same number of friends within the group. $n > 2$.
pigeons ↔ people; pigeonholes ↔ # of friends
Note: if someone has $n - 1$ friends $\implies$ no-one has 0 friends
$\implies$ the options for # of friends are either: $1, 2, \dots, (n - 1)$ or $0, 1, 2, \dots, (n - 2)$
Since there are $n$ people (pigeons), and $n - 1$ pigeonholes, by the pigeonhole principle, the statement is true.

## HW 69 — Generalised pigeonhole principle
_File `20261121_230102.jpg`. The lower third of the page is blank._

**Generalised pigeonhole principle**
**Def.** Suppose you have $n$ pigeons sitting in $k$ pigeonholes. If $n > k \cdot m$, then at least one of the pigeonholes contains at least $m + 1$ pigeons.

The *contrapositive* of the pigeonhole principle: If each pigeonhole contains at most $m$ pigeons, then $n \le km$.

**Ex.** Show that in a group of 25 people, at least 3 must be born in the same month.
Let $n = 25$, $m = 2$. We have: 25 pigeons (people) ($n$); 12 pigeonholes (months) ($k$).
Since $n > 12 \cdot 2$, by the g.p.p., there is a month in which $\ge 3$ people from the group have a birthday.

## HW 70 — Graphs: definitions, loops, parallel edges, simple graphs
_File `20261121_230106.jpg`. Contains three graph drawings._

**Introduction to graph theory**
**Def.** A *graph* $G$ consists of two finite sets:
↳ a non-empty set of *vertices* $V(G)$
↳ a (possibly empty) set of *edges* $E(G)$ where each edge is associated with a set $\{v, w\} \subseteq V(G)$
↳↳ the vertices $v, w$ are the *endpoints* of the edge.

**Ex.** Two drawings of the same graph, separated by "or":
- Left: a rectangle with vertices $a$ (top left), $b$ (top right), $c$ (bottom right), $d$ (bottom left), and edges along the four sides $a$–$b$, $b$–$c$, $c$–$d$, $d$–$a$.
- Right: the four vertices in a horizontal row, $a, b, c, d$ from left to right. Straight edges $a$–$b$, $b$–$c$, $c$–$d$ along the row; the fourth edge $a$–$d$ is a long S-shaped curve that rises above $a$–$b$, crosses the row between $b$ and $c$, and passes below $c$ to reach $d$.

This graph $G$ has four vertices i.e. $\abs{V(G)} = 4$, $V(G) = \{a, b, c, d\}$, and has four edges i.e. $\abs{E(G)} = 4$, whose endpoints are $\{a, b\}, \{b, c\}, \{c, d\}, \{a, d\}$. [a scribbled-out word precedes "whose"]

**Ex.** Vertices $x$, $y$, $z$ in a row. Two curved edges between $x$ and $y$: $e_1$ arching above, $e_2$ below. A straight edge $e_3$ from $y$ to $z$. A small loop $e_4$ at $z$ (on its right).
$V(G) = \{x, y, z\}$, $E(G) = \{e_1, e_2, e_3, e_4\}$.

**Def.** A *loop* is an edge whose endpoints are equal, which is denoted $\{v, v\}$ or $\{v\}$.
*Parallel edges* / *multiple edges* are two (or more) edges with the same set of endpoints.
A *simple graph* has no loops and no parallel edges.

## HW 71 — Incidence, adjacency, isolated vertices
_File `20261121_230111.jpg`. Contains one graph drawing._

**Introduction to graph theory**
**Ex.** Graph drawing: $v_2$ at top centre-left, $v_3$ at top right of it, $v_1$ lower left, $v_4$ lower middle (below between $v_2$ and $v_3$), $v_5$ further right on its own.
Edges: $e_1$ a loop at $v_1$ (drawn as a circle around/below $v_1$); $e_2$ from $v_1$ to $v_2$; $e_3$ from $v_2$ to $v_3$ (horizontal); $e_4$ from $v_2$ to $v_4$; $e_5$ and $e_6$ two parallel edges between $v_3$ and $v_4$ (one nearly straight, one curved). $v_5$ has no edges.

**Def.** An edge and a vertex are *incident* iff the vertex is an endpoint of the edge. (ex: $e_3$ is incident with $v_2$ and $v_3$)
**Def.** Two edges are *adjacent* if they are incident with one another / the same vertex.
Two vertices are *adjacent* if they are connected by an edge.
(ex: $e_2$ and $e_3$ are adjacent; $v_2$ and $v_4$ are adjacent)
An *isolated* vertex is a vertex which is incident with no edges. (ex: $v_5$ is isolated)

## HW 72 — Degree; handshake theorem
_File `20261121_230117.jpg`. Contains two graph drawings._

**Introduction to graph theory**
**Def.** The *degree* of a vertex $v$ is the number of edges incident with $v$, written as $\deg(v)$. Each loop is counted twice.

**Ex.** Two graphs, $G$ (left) and $H$ (right), names underlined.
- $G$: five vertices. Upper left $w$ [the label is small and looks like "u"; the degree list calls it $w$], $v$ at the top middle (isolated), $x$ at the bottom middle, $y$ at upper right of $x$, $z$ at lower right of $y$. Edges: $w$–$x$, $x$–$y$, a small loop at $x$ (drawn on its right), and two parallel curved edges between $y$ and $z$.
$\deg(w) = 1$, $\deg(v) = 0$, $\deg(x) = 4$, $\deg(y) = 3$, $\deg(z) = 2$.
Degree sum $= 10 = 2 \cdot 5$ (an arrow from "#" points to the 5: the number of edges).
- $H$: six vertices at the corners of a hexagon wider than it is tall (two on top, one at the far left, one at the far right, two on the bottom). Edges: the six sides of the hexagon and the three long diagonals joining opposite vertices, all crossing at the centre.
every vertex has degree 3. Degree sum $= 18 = 2 \cdot 9$ (an arrow from "#" points to the 9).

**Handshake theorem**
**Def.** Let $G$ be a graph with $n$ vertices $V(G) = \{v_1, v_2, \dots, v_n\}$. Then,
$$\sum_{i=1}^{n} \deg(v_i) = \deg(v_1) + \deg(v_2) + \dots = 2 \cdot \abs{E(G)}$$
i.e. degree sum $= 2 \times$ # of edges. [stated without proof]

**Cor.** There is an even number of vertices of odd degree.
i.e. we cannot make a graph which has an odd number of vertices of odd degree. otherwise, the degree sum would contradict the handshake theorem.

## HW 73 — Walks, connectedness, trails and circuits
_File `20261121_230124.jpg`. Contains four graph drawings. The heading line "Th. Walks" stands above the definition._

**Walks, trails and circuits**
**Def.** Let $G$ be a graph and let $v, w$ be vertices in $G$. A *walk* from $v$ to $w$ is a finite alternating sequence
$$v_0\, e_1\, v_1\, e_2 \dots v_{n-1}\, e_n\, v_n$$
of vertices and edges, such that $v_0 =: v$, $v_n =: w$, and $e_i$ is an edge with endpoints $\{v_{i-1}, v_i\}$ for $i \in \{1, \dots, n\}$.

**Ex.** Graph $G$: $a$ at left, $b$ above-right of $a$, $c$ below-right of $b$, $d$ to the right of $b$. Edges $e_1 = a$–$b$, $e_2 = b$–$c$, $e_3 = a$–$c$, $e_4 = b$–$d$.
$a\, e_1\, b\, e_2\, c\, e_2\, b\, e_4\, d$ is a walk from $a$ to $d$.

**Def.** A graph is *connected* iff given any two vertices $v, w$ in $G$, there exists a walk from $v$ to $w$. ["only" and "matrices" are crossed out and replaced by "any" and "vertices"]

**Ex.** Two graphs:
- "connected": four vertices. Top left $p$, top right $q$, bottom left $r$, bottom right $s$. Two parallel curved edges between $p$ and $q$; edge $p$–$r$ (vertical); edge $p$–$s$ (diagonal).
- "not connected": six vertices at the positions of a hexagon (top, upper right, lower right, bottom, lower left, upper left). Two triangles drawn over them as a six-pointed star: one on top, lower-left and lower-right, the other on bottom, upper-left and upper-right. Two arrows point at the top vertex and the upper-right vertex, labelled "not connected" (they lie in different triangles). [in the drawing the triangle lines stop short of the vertex circles]
[vertex names $p, q, r, s$ added here; the vertices are unlabelled in the notes]

**Def.** A *trail* is a walk whose edges are distinct.
↳ in a trail, each edge can only appear at most once.
A *circuit* is a trail that both starts and ends at the same vertex.

**Ex.** Graph with vertices $A$ (top left), $B$ (top right), $D$ (bottom left), $C$ (bottom right; the label is written like "e" or "C"). Edges: $e_1 = A$–$D$ (left side); $e_2$ and $e_6$ two curved parallel edges from $A$ to $C$ ($e_2$ the outer, upper curve, $e_6$ the inner, lower curve); $e_3 = B$–$C$ (right side); $e_5 = D$–$C$ (bottom); $e_4$ a loop at $C$ (lower right).
$A\, e_2\, C\, e_4\, C\, e_3\, B$ is a trail from $A$ to $B$.
$A\, e_2\, C\, e_4\, C\, e_5\, D\, e_1\, A$ is a circuit.
$A\, e_2\, C\, e_2\, A$ is not a circuit – not a trail.
$A\, e_2\, C\, e_6\, A$ is a circuit.

## HW 74 — Euler circuits and Euler trails
_File `20261121_230128.jpg`. Contains one graph drawing._

**Euler circuits and Euler trails**
**Def.** An *Euler circuit* for graph $G$ is a circuit that uses every edge of $G$ exactly once.

**Ex.** Graph: vertex 1 at top left, 2 at top right, 3 below 2, 4 below 1. Edges: $a = 1$–$2$ (top); $b$ and $c$ two curved parallel edges between 2 and 3 ($c$ on the left, $b$ on the right); $d = 2$–$4$ (diagonal); $f = 1$–$4$ (left side); $e$ a loop at 4 (drawn below it).
$1\,a\,2\,b\,3\,c\,2\,d\,4\,e\,4\,f\,1$ is an Euler circuit.
Note that every vertex has an even degree.
**Proof.** See UQ Extend video 44.

**Th.** Let $G$ be a connected graph. Then $G$ has an Euler circuit iff every vertex of $G$ has even degree.
**Proof.** See UQ Extend video 44. [no proof in the notes]

**Def.** An *Euler trail* of a graph $G$ from vertices $u$ to $v$ is a trail from $u$ and $v$ that uses every edge exactly once. [sic: "from $u$ to $v$"]
**Rem.** Similar to Euler circuits, but the start and end points may differ.
If $u = v$, then $G$ has an Euler trail from $u$ to $v$ iff every vertex of the graph has even degree.
If $u \ne v$, then $G$ has an Euler trail from $u$ to $v$ iff $u$ and $v$ have odd degree, all other vertices have even degree.
**Proof.** See UQ Extend video 44. [no proof in the notes]
[possible error: both statements need $G$ to be connected, as in the theorem above; the remark does not say so.]

## HW 75 — Matrix representations of graphs; adjacency matrix
_File `20261121_230135.jpg`. Contains one graph drawing. "(for 1061 …)" refers to this course._

**Matrix representations of graphs**
**Th.** Recall that:
↳ $m \times n$ matrix $A$ over a set $S$ (for 1061, we will use $A \in M_{m \times n}(\N)$)
$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1j} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2j} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & \cdots & a_{ij} & \cdots & a_{in} \\ \vdots & \vdots & & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mj} & \cdots & a_{mn} \end{bmatrix} = [a_{ij}]$$
[the closing bracket in the notes ends at row $i$; rows below it are written outside the bracket]
↳ $a_{ij}$ represents the $(i, j)$th entry of $A$.
[the entries here include 0, so "$\N$" must include 0 here, unlike the book's $\N = \{1, 2, \dots\}$]

**Th.** Adjacency matrix [heading]
**Def.** Let $G$ be a graph with $n$ vertices. Label the vertices $V(G) = \{v_1, v_2, \dots, v_n\}$.
The *adjacency matrix* of $G$ is the $n \times n$ matrix $A = [a_{ij}]$ where $a_{ij}$ is the number of edges with endpoints $\{v_i, v_j\}$.
i.e. $a_{ij} = \begin{cases} r & \text{if } \exists\, r \text{ edges connecting } v_i, v_j \\ 0 & \text{else} \end{cases}$

**Ex.** Graph: $v_2$ top left, $v_3$ top right, $v_1$ bottom left, $v_4$ bottom right. Edges: two curved parallel edges $v_2$–$v_3$; $v_2$–$v_1$ (left side); $v_2$–$v_4$ (diagonal); $v_1$–$v_4$ (bottom); a loop at $v_4$, drawn as a circle around the label "$v_4$".
$$A = \begin{array}{c} \\ \\ \end{array}\begin{bmatrix} 0 & 1 & 0 & 1 \\ 1 & 0 & 2 & 1 \\ 0 & 2 & 0 & 0 \\ 1 & 1 & 0 & 1 \end{bmatrix} \quad \text{columns } v_1, v_2, v_3, v_4;\ \text{rows } v_1, v_2, v_3, v_4$$

**Rem.** The diagonal of $A$ is the amount of loops for $a_{ii}$ for $v_i$.
**Rem.** $A$ is symmetric on the diagonal. [i.e. symmetric about the diagonal: $A = A\T$]

## HW 76 — Incidence matrix
_File `20261121_230140.jpg`. Contains one graph drawing. The lower third of the page is blank._

**Matrix representations of graphs**
**Th.** Incidence matrix [heading]
**Def.** Let $G$ be a graph with $n$ vertices and $m$ edges. Label the vertices $V(G) = \{v_1, v_2, \dots, v_n\}$, label the edges $E(G) = \{e_1, e_2, \dots, e_m\}$.
The *incidence matrix* of $G$ is the $n \times m$ matrix $N = [n_{ij}]$ where $n_{ij}$ is the number of times (vertex) $v_i$ is incident with (edge) $e_j$.
i.e.
$$n_{ij} = \begin{cases} 2 & \text{if } e_j \text{ is a loop on } v_i \\ 1 & \text{if } e_j \text{ is an edge connecting } v_i \text{ to some other vertex} \\ 0 & \text{else} \end{cases}$$

**Ex.** Graph: $v_2$ at the top, $v_1$ lower left, $v_3$ lower right. Edges: $e_1$ a loop below $v_1$; $e_2 = v_1$–$v_2$; $e_3$ and $e_4$ two curved parallel edges between $v_2$ and $v_3$ ($e_3$ the inner/lower curve, $e_4$ the outer/upper curve).
$$N = \begin{bmatrix} 2 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} \quad \text{rows } v_1, v_2, v_3;\ \text{columns } e_1, e_2, e_3, e_4$$

**Lemma.** We can use incidence matrices to prove the handshake theorem.
**Proof.** See UQ Extend lecture 45. [no proof in the notes]

## HW 77 — Trees
_File `20261121_230146.jpg`. Contains three small graph drawings. The lower half of the page is blank._

**Trees**
**Def.** A graph is *circuit-free* iff it has no non-trivial circuits.
↳ trivial circuit: single vertex, no edges
A graph is a *tree* iff it is connected and it is circuit-free.
**Rem.** Since loops and multiple edges are nontrivial circuits, trees are simple graphs.

**Ex.** Three graphs, followed by "are all trees.":
1. Nine vertices. A vertex $t$ at the top with edges down-left to a leaf and down-right to a vertex $m$. From $m$: an edge straight down to a leaf and a horizontal edge right to a vertex $s$. From $s$: three edges down to three leaves (left, middle, right).
2. Two vertices joined by one edge.
3. A single vertex with no edges.
[vertex names $t, m, s$ added here; the vertices are unlabelled in the notes]

**Th.** A graph $G$ with $n$ vertices is a tree iff $G$ is simple, connected and has $n - 1$ edges.
**Proof.** See UQ Extend lecture 46. [no proof in the notes]
