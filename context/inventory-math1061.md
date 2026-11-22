# Coverage inventory: MATH1061 Discrete Mathematics

_Built in the transcription phase from 77 photos of the handwritten notes (one notebook page per photo). No typed notes or slides were supplied. Transcription: `claude/notes-math1061-1.md` (HW 01–25), `-2.md` (HW 26–49), `-3.md` (HW 50–77)._

**Sources.** "HW nn" means photo nn in shooting order (one page per photo); file names are given in the notes docs. **Code:** none in the notes. Part I uses **Python**, but nothing here needs code. **Content rule:** source material only, with corrections. Section titles below are proposals; `tools/chapters.py` lists chapters only.

**Status:** ✅ written, ◻ to do. **↔ merge** = overlaps material already written (Ch 25–31) or another course's chapter.

**Gaps the hub should know about.**
1. **Number theory is thin.** Divisibility ($d \mid n$, HW 12), congruence mod $n$ (used HW 31, 43, 46–47), gcd (HW 41, 57, 58) and unique prime factorisation (HW 41) are used without their own pages. There is nothing on the division algorithm, the Euclidean algorithm, Bézout, modular inverses or RSA. Pages may be missing (see questions for the hub).
2. **Six results point to the course's online lectures for proof** ("See UQ Extend lecture/video 40, 44, 45, 46"): the binomial theorem, the Euler circuit and Euler trail theorems, the handshake proof via incidence matrices, and the tree characterisation. In the book these are "Not proved in this course."
3. Two forward references to MATH1071: "$(\Q, +, \circ)$ is a field – check the field axioms (1071)" and "$\Z_p$ is a field (1071)" (HW 59).

---

## Ch 1 Logic and Proof (`ch:logic-and-proof`)

### 1.1 Propositional logic
- ◻ Negation $\sim p$ / $\neg p$, conjunction $p \wedge q$, disjunction $p \vee q$ by truth tables; inclusive or vs exclusive or $p \oplus q$ (HW 01)
- ◻ Statement form; logical equivalence $P \equiv Q$; Ex. $\sim(p \wedge q) \equiv \sim p \vee \sim q$ by truth table (HW 01)
- ◻ Laws of logical equivalence: De Morgan, distributive, absorption, idempotent, identity, universal bound, negation laws, negations of taut./cont. (HW 02); commutative and associative laws are used (HW 04) but not listed
- ◻ Tautology and contradiction; Ex. contradiction $(p \wedge \sim q) \wedge (\sim p \vee q)$; Ex. $\sim p \vee (p \wedge q) \equiv \sim p \vee q$ (HW 02)
- ◻ Tutorial exercises (HW 07): truth assignments making a form false; simplification to $\sim p$; tautology check. All three contain errors (see below); use at most one, corrected.

### 1.2 Conditional statements
- ◻ Conditional $p \to q$: truth table, hypothesis, conclusion; $p \to q \equiv \sim p \vee q$ (HW 03)
- ◻ Contrapositive $\sim q \to \sim p$ ($\equiv$); negation $\sim(p \to q) \equiv p \wedge \sim q$ with proof by equivalences (HW 03)
- ◻ Biconditional $p \leftrightarrow q \equiv (p \to q) \wedge (q \to p)$ (HW 03)
- ◻ $p \to q \equiv \sim(p \wedge \sim q)$; NAND (HW 04)
- ◻ Ex. $p \to (q \vee r) \equiv (p \wedge \sim q) \to r$, two derivations (HW 04; second derivation's reasons are shifted)
- ◻ Converse $q \to p$, inverse $\sim p \to \sim q$, neither equivalent to $p \to q$ (HW 04)
- ◻ Necessary and sufficient conditions (HW 04)

### 1.3 Arguments and rules of inference
- ◻ Argument, premises, conclusion; valid / invalid; validity via truth tables (HW 05)
- ◻ Rules of inference table: modus ponens, modus tollens, generalisation, specialisation, conjunction, elimination, transitivity, proof by division into cases (HW 05)
- ◻ Validity by contradiction: look for premises true, conclusion false (HW 06); Ex. ($p \to \sim r$, $r \vee \sim q$, $q$ ∴ $\sim p$) (HW 06); two more examples, one valid and one invalid (HW 08)
- ◻ Derivations with rules of inference: ($p \to q$, $p \vee r$, $p \vee \sim r$ ∴ $q$) via distributive, negation and identity laws; ($w \to b$, $d \to \sim b$ ∴ $\sim d \vee \sim w$) via contrapositive and transitivity (HW 08)
- ◻ Fallacies: converse error, inverse error (HW 06)

### 1.4 Predicates and quantifiers
- ◻ Predicate, domain, truth set; Ex. "$x$ divides 5" on $\Z$ has truth set $\{-5, -1, 1, 5\}$ (HW 09)
- ◻ Common domains $\Z$, $\Z^{+} = \N$, $\N_0$, $\Q$, $\R$ (HW 09) ↔ Ch 2 / notation
- ◻ Universal and existential statements; universal conditional $\forall x \in D,\ P(x) \to Q(x)$ (HW 09)
- ◻ Negation of $\forall$, $\exists$ and universal conditionals; Ex. (HW 10)
- ◻ Multiple quantifiers: how to establish $\forall\exists$ and $\exists\forall$ statements; Ex. $x + y = 0$, Ex. $x = 1$ least in $\Z^{+}$; negations (HW 11)

### 1.5 Methods of proof
- ◻ Parity: even $\iff n = 2k$, odd $\iff n = 2k + 1$ (HW 12) ↔ Ch 5
- ◻ Prime and composite: definitions in words and symbols (HW 12) ↔ Ch 5
- ◻ Proving existential statements by example; direct proof of universal conditionals (method) (HW 12)
- ◻ How to write a proof (8-point checklist) (HW 13)
- ◻ Disproof by counterexample; Ex. $m^2 - 4$ composite for $m > 2$ is false ($m = 3$) (HW 13)
- ◻ Direct-proof examples: $n$ odd $\implies n^2$ odd (HW 12); $(n+1)^2 - n^2$ odd (HW 13); $x + 6 = 4y \implies x/2$ odd (HW 14); $\exists m, n: 1/m + 1/n \in \Z$ (HW 14); $n - m$ even $\implies n^3 - m^3$ even, with a first attempt marked "Wrong." (HW 14); products of odd integers (HW 19). **Keep one or two.**
- ◻ Ex. "product of the first $n$ primes $- 1$ is prime" disproved at $n = 4$, counterexample not written (HW 14)
- ◻ Proof by contradiction: method, and for universal conditionals (HW 15)
- ◻ Proof by contraposition: method (HW 15); Ex. $r^2$ irrational $\implies r$ irrational (HW 18); Ex. $mn$ odd $\implies m, n$ odd (HW 19, incomplete contrapositive)

### 1.6 Rational and irrational numbers (proof practice)
- ◻ Definition of $\Q$; decimal expansions repeat (stated) (HW 16) ↔ Ch 9 (MATH1071/2401 real numbers)
- ◻ Lemmas: $\Q$ closed under $+$ and under $\div$ by non-zero, with proofs (HW 16)
- ◻ Th. Between two rationals there is a rational ($q = \frac12(r + s)$), with proof (HW 16) ↔ Ch 9 (density)
- ◻ Th. Non-zero rationals have rational inverses, with proof (HW 17)
- ◻ Lemma: rational + irrational is irrational, proof by contradiction (HW 17)
- ◻ Ex. $2r^2 - 3r + 1 \in \Q$ for $r \in \Q$ (HW 18)
- Placement: could instead be a section of Ch 9. Proposed here because the notes use it as proof practice.

## Ch 2 Sets, Relations and Functions (`ch:sets-relations-functions`)

### 2.1 Sets
- ◻ Set, element, $\in$ / $\notin$, listing; order and repetition ignored; set-builder notation; Ex. evens; sets of sets (HW 26)
- ◻ Subset $A \subseteq B \iff \forall x,\ x \in A \to x \in B$; proper subset; equality; empty set (subset of all sets); cardinality $\abs{A}$ of a finite set (HW 26) ↔ Ch 25 (events as sets; Ch 25 uses set notation without defining it)
- ◻ Russell's paradox; recursive building of sets from $\emptyset$ (HW 27)
- ◻ Intervals: bounded and unbounded (HW 30) ↔ Ch 9
- ◻ Ordered $n$-tuples and equality; Cartesian product $A \times B$, $A_1 \times \dots \times A_n$; Ex.; $\R \times \R$ (HW 29)

### 2.2 Operations on sets
- ◻ Union, intersection, difference, complement (universal set $U$ used, not defined) (HW 27) ↔ Ch 25 (event operations, $A^c$)
- ◻ Indexed unions and intersections, finite and countable (HW 27) ↔ Ch 25 (countable unions in Axiom 3)
- ◻ Power set $\powerset(S)$; Ex. $S = \{1, 3\}$; $\abs{\powerset(S)} = 2^n$ (stated) (HW 28) ↔ Ch 25 ($F \subseteq \powerset(\Omega)$)
- ◻ Disjoint and mutually (pairwise) disjoint sets; partitions; Ex. $\{2, 3, 5, 7, 11\}$ (HW 28) ↔ Ch 25 (partitions in the law of total probability)

### 2.3 Set identities and proofs with sets
- ◻ Transitivity of $\subseteq$, with proof (HW 31)
- ◻ Inclusion properties $A \cap B \subseteq A \subseteq A \cup B$ ("see Venn diagram", no diagram drawn) (HW 31)
- ◻ Proving set equality by double inclusion; Ex. $\{x \equiv 1 \bmod 6\} = \{x \equiv 1 \bmod 2 \text{ and } \bmod 3\}$ (HW 31; uses congruence before it is defined)
- ◻ Set identities: commutative, associative, distributive, absorption, idempotent (HW 32); De Morgan for sets, $A - B = A \cap B^c$, double complement, $U^c$, $\emptyset^c$, identity and universal bound laws (HW 32), all stated without proof ↔ Ch 1 (parallel to the logical laws, as the notes say) ↔ Ch 25

### 2.4 Functions
- ◻ Function as a subset of $X \times Y$; domain, co-domain; $f(x) = y$, $x \mapsto y$; value, image (HW 33). The uniqueness condition is missing (see errors).
- ◻ Image $f(A)$ of a subset; range $f(X) \subseteq$ co-domain (HW 33)
- ◻ Th. $f = g \iff f(x) = g(x)\ \forall x$; Ex. $x$ vs $\sqrt{x^2}$ (HW 33)
- ◻ Injective: definition, contrapositive form, proof method; Ex. $x^2$ not injective (HW 34–35)
- ◻ Surjective: definition, proof method; Ex. $2x - 3$ surjective, $x^2$ not surjective (HW 34–35)
- ◻ Bijective; inverse function $f^{-1}$ exists for a bijection (stated) (HW 34)
- ◻ Composition $g \circ f$; not commutative (HW 36)
- ◻ Th. $f \circ i_X = f$, $i_Y \circ f = f$, with proof (HW 36)
- ◻ Th. $f^{-1} \circ f = i_X$, $f \circ f^{-1} = i_Y$ (stated); Ex. $f(x) = 2x + 1$ (HW 36)
- ◻ Th. Compositions of injections / surjections are injective / surjective, with proofs; of bijections bijective, hence invertible (HW 37)

### 2.5 Cardinality and countability
- ◻ Same cardinality iff a bijection exists; finite and infinite sets (HW 38)
- ◻ Th. Finite sets: no injection if $\abs{X} > \abs{Y}$, no surjection if $\abs{X} < \abs{Y}$, item 3 garbled (stated) (HW 38) ↔ Ch 3 (pigeonhole, HW 68)
- ◻ Th. $\abs{\Z^{+}} = \abs{\Z} = \abs{2\Z} = \abs{\Q^{+}} = \abs{\Q}$ (HW 38)
- ◻ Ex. $\abs{\Z} = \abs{2\Z}$ via $f(k) = 2k$, with proof (HW 39)
- ◻ Ex. $\abs{\Z^{+}} = \abs{\Q^{+}}$ by the zig-zag path; **Figure** (HW 39)
- ◻ Countable and countably infinite; Ex. $\Z$, $2\Z$, $\Q^{+}$, $\Q$ (HW 40)
- ◻ Th. Subsets of countable sets are countable; supersets of uncountable sets are uncountable (stated) (HW 40)
- ◻ Th. $(0, 1)$ is uncountable: Cantor's diagonal argument (HW 40) ↔ Ch 9 (MATH2401 may also cover countability)
- ◻ Th. $\R$ uncountable; bijection $\R \to (0, 1)$, $x \mapsto 1/(1 + e^x)$ (HW 40)
- ◻ Comparing cardinalities via injections and surjections (HW 41)
- ◻ Schröder–Bernstein theorem (stated); three ways to show $\abs{X} = \abs{Y}$ (HW 41)
- ◻ Ex. $\abs{\Z^{+}} = \abs{\Q^{+}}$ via Schröder–Bernstein, $g(a/b) = 2^a 3^b$ (HW 41; uses unique prime factorisation) ↔ Ch 5

### 2.6 Relations
- ◻ Binary relation $R \subseteq A \times B$, $xRy$; not symmetric in general (HW 42)
- ◻ Ex. $\sigma$ ($a < b$) from $\{1, 2, 5\}$ to $\{5, 6\}$; **Figure**: arrow diagram; "$\sigma$ is not a function" (HW 42)
- ◻ Inverse relation $R^{-1}$; relation on a set; Ex. divisibility on $\Z$ and its inverse (HW 42)
- ◻ Ex. divisibility on $\{2, 3, 6\}$; **Figure**: directed graph, one loop missing (HW 42)
- ◻ Arrow diagrams on a single set; loops (HW 45); **Figures**: $aRb$, $aRa$
- ◻ Reflexive, symmetric, transitive (HW 43); Ex. $<$ on $\R$ (HW 43)
- ◻ Ex. congruence mod $d$ is reflexive, symmetric and transitive, with proofs (HW 43) ↔ Ch 5
- ◻ Th. $R$ symmetric $\iff R = R^{-1}$, with proof (HW 44)
- ◻ Th. Reflexivity, symmetry and transitivity read off an arrow diagram; **Figures** (three small diagrams); two worked diagrams (HW 45)

### 2.7 Equivalence relations
- ◻ Equivalence relation; equivalence class $[a]$ (HW 46)
- ◻ Ex. congruence mod 3 on $\Z$: three classes (HW 46) ↔ Ch 5
- ◻ Lemma $aRb \implies [a] = [b]$, with proof (HW 46)
- ◻ Lemma $[a] \cap [b] \ne \emptyset \implies [a] = [b]$; Rem. either disjoint or equal; with proof (HW 47)
- ◻ Th. The equivalence classes partition $A$ (stated) (HW 47)
- ◻ Ex. $\{[0], \dots, [d-1]\}$ partitions $\Z$ (HW 47) ↔ Ch 5 ($\Z_n$)
- ◻ Representative of a class (HW 47)
- ◻ Th. Relation induced by a partition is an equivalence relation (stated) (HW 47)

### 2.8 Order relations
- ◻ Antisymmetric; not the negation of symmetry; **Figure**: four arrow diagrams (all combinations of symmetric / antisymmetric) (HW 48)
- ◻ Partial order; Ex. $\le$ on $\R$; Ex. $\subseteq$ on $\powerset(A)$ (HW 48)
- ◻ Comparable elements; Ex. in $\powerset(\{1, 2, 3, 4\})$ (HW 49)
- ◻ Total order; Ex. divisibility on $\{1, 2, 4, 8, 16\}$, full proof (HW 49)

## Ch 3 Induction, Recursion and Counting (`ch:induction-recursion-counting`)

### 3.1 Sequences, sums and products
- ◻ Sequence, term, explicit formula; notations $\{2^k\}_{k \ge 0}$ etc. (HW 20) ↔ Ch 9 (MATH1071/2401 sequences)
- ◻ Summation notation; dummy variables; change of variable (mentioned) (HW 20)
- ◻ Product notation (HW 20)

### 3.2 Mathematical induction
- ◻ Motivation: repeated modus ponens (HW 21)
- ◻ Principle of mathematical induction; basis step, inductive step, inductive hypothesis; how to write the conclusion (HW 21)
- ◻ Strong induction; equivalent to ordinary induction (stated) (HW 22)
- ◻ Well-ordering principle; WOP ≡ MI ≡ SMI (stated); Ex. which sets have a least element (HW 22)

### 3.3 Recursion
- ◻ Recurrence relation, initial conditions; Ex. Fibonacci $F_0 = F_1 = 1$ (HW 23)
- ◻ Three ways to define a sequence (HW 23)
- ◻ Recursive definitions of sets: base, recursion, restriction (HW 23) ↔ Ch 2 (sets built recursively, HW 27)
- ◻ Method of iteration: guess, then prove by induction; Ex. $b_n = b_{n-1} + 5$, $b_0 = 2 \implies b_n = 5n + 2$, with proof (HW 24)
- ◻ Not every recursive sequence has an explicit formula (HW 24)
- ◻ Arithmetic and geometric sequences, explicit formulas (HW 25) ↔ Ch 9

### 3.4 Counting
- ◻ Multiplication and addition principles; ice-cream and cookie example (HW 61) ↔ **merge Ch 25 §Counting** (Ch 25 has no explicit sum rule)
- ◻ Permutations of $n$ objects, $n!$; Ex. OBJECTS (7! and starting with a vowel) (HW 60) ↔ merge Ch 25 ($n!$ already defined)
- ◻ Ex. licence plates: total, no repeats, at least one repeat by complement (HW 60)
- ◻ Counting selections: order × repetition, four cases (HW 61–62) ↔ **merge Ch 25** (its four urn schemes: $n^k$, ${}^nP_k$, ${}^nC_k$, $\binom{n+k-1}{k}$). MATH1061 Case 1 = $n^r$ (PIN example); Case 2 = $P(n, r) = n!/(n-r)!$ (1st/2nd/3rd example); Case 3 = $\binom{n}{r} = P(n, r)/r!$ (group of 5 from 10); Case 4 "general solution will not be given" (five flavours, three scoops, not solved). Ch 25 already has Case 4 from STAT2003.
- ◻ Permutations with repeated letters: ALFALFA $= 210$, two methods (HW 62) (new; not in Ch 25)

### 3.5 Binomial coefficients and the binomial theorem
- ◻ $\binom{n}{r}$ as the number of $r$-subsets $= n!/(r!(n-r)!)$ (HW 65) ↔ merge Ch 25 (Ch 25 defines ${}^nC_k = \binom{n}{k}$)
- ◻ Th. $\binom{n}{r} = \binom{n}{n-r}$: algebraic proof and combinatorial proof (HW 65)
- ◻ Th. Pascal's formula, algebraic proof (HW 65)
- ◻ Binomial theorem (stated; "see UQ Extend lecture 40"); Ex. $(x + y)^4$ (HW 66) ↔ Ch 29 (binomial pmf sums to 1, if Ch 29 uses it)

### 3.6 Inclusion–exclusion and the pigeonhole principle
- ◻ Inclusion–exclusion for two and three finite sets (stated); disjoint case; **Figures**: two Venn diagrams (HW 67) ↔ **merge Ch 25** (Ch 25 has the probability version for $n$ events, `thm:inclusion-exclusion`); the counting version is new
- ◻ Pigeonhole principle; contrapositive; function form (HW 68) ↔ Ch 2 (finite-set cardinality theorem, HW 38)
- ◻ Ex. two people in a group with the same number of friends (HW 68)
- ◻ Generalised pigeonhole principle; contrapositive; Ex. 25 people, 3 share a birth month (HW 69)

## Ch 4 Graph Theory (`ch:graph-theory`)

### 4.1 Graphs
- ◻ Graph $G = (V(G), E(G))$, endpoints; **Figure**: one graph drawn two ways (rectangle, and in a line with a crossing edge) (HW 70)
- ◻ Ex. multigraph on $\{x, y, z\}$; **Figure** (HW 70)
- ◻ Loop, parallel/multiple edges, simple graph (HW 70)
- ◻ Incident, adjacent edges, adjacent vertices, isolated vertex; **Figure** (5 vertices, 6 edges) (HW 71)

### 4.2 Degree and the handshake theorem
- ◻ Degree $\deg(v)$, loops count twice (HW 72)
- ◻ Ex. $G$ (degrees 1, 0, 4, 3, 2; sum 10) and $H$ (6 vertices of degree 3; sum 18); **Figures** (HW 72)
- ◻ Handshake theorem (stated); Cor. even number of odd-degree vertices, with a one-line reason (HW 72)
- ◻ Lemma: handshake theorem via incidence matrices ("see UQ Extend lecture 45") (HW 76)

### 4.3 Walks, trails, circuits and connectedness
- ◻ Walk; Ex. with **Figure** (HW 73)
- ◻ Connected graph; **Figures**: connected multigraph, disconnected two-triangle graph (HW 73)
- ◻ Trail, circuit; Ex. with **Figure** (four trail / circuit / non-circuit sequences) (HW 73)

### 4.4 Euler circuits and trails
- ◻ Euler circuit; Ex. with **Figure** (HW 74)
- ◻ Th. connected $G$ has an Euler circuit iff all degrees are even ("see UQ Extend video 44") (HW 74)
- ◻ Euler trail; conditions for $u = v$ and $u \ne v$ ("see UQ Extend video 44") (HW 74)

### 4.5 Matrix representations
- ◻ Matrix notation $A = [a_{ij}] \in M_{m \times n}(\N)$ ("recall") (HW 75) ↔ Ch 6 (MATH1071 matrices)
- ◻ Adjacency matrix: definition, Ex. with **Figure**, diagonal = loops, symmetric (HW 75)
- ◻ Incidence matrix: definition, Ex. with **Figure** (HW 76)

### 4.6 Trees
- ◻ Circuit-free (trivial circuit), tree; trees are simple (HW 77)
- ◻ Ex. three trees; **Figure** (HW 77)
- ◻ Th. tree $\iff$ simple, connected, $n - 1$ edges ("see UQ Extend lecture 46") (HW 77)

## Ch 5 Number Theory and Algebraic Structures (`ch:number-theory-algebraic-structures`)

### 5.1 Divisibility, primes and congruence
- ◻ Parity, prime, composite (HW 12) — or keep in Ch 1 and cite here
- ◻ $d \mid n \iff n = dk$, $d \ne 0$ (HW 12, one line)
- ◻ Congruence mod $d$ is an equivalence relation (HW 43, 46) ↔ Ch 2
- ◻ $\Z_n$ as the classes mod $n$; $+$ and $\circ$ on classes (HW 51); well-definedness not shown
- Nothing else on number theory in the notes (see gaps).

### 5.2 Groups
- ◻ Group: closure, associativity, identity, inverses; Rem. closure needs checking (HW 50)
- ◻ Ex. $(\Z, +)$ is a group; $(\R, \circ)$ is not (0 has no inverse) (HW 50)
- ◻ Ex. $(\Z_3, +)$ via Cayley table (HW 51); $(\Z_4, \circ)$ and $(\Z_4 \setminus \{0\}, \circ)$ are not groups (HW 51, last line cut off)
- ◻ Ex. bijections $\R \to \R$ under composition form a group (HW 52)
- ◻ Abelian / non-abelian; symmetric group $S_n$; $S_n$ non-abelian for $n \ge 3$ (stated) (HW 52)
- ◻ Th. identity unique; Th. inverses unique, with proofs (HW 53)
- ◻ Powers $g^k$, $g^{-k}$, $g^0$; exponent laws (stated) (HW 55)

### 5.3 Subgroups and cyclic groups
- ◻ Subgroup tests (closure, identity, inverses); associativity inherited; $H \le G$, proper and trivial subgroups (HW 54)
- ◻ Ex. all subgroups of $(\Z_6, +)$ with Cayley table (HW 54)
- ◻ Cyclic subgroup $\langle a \rangle$; cyclic group; Ex. the subgroups of $\Z_6$ are cyclic (HW 55)

### 5.4 Isomorphisms
- ◻ Informal Ex. $(\Z_4, +)$ vs $(\Z_5 \setminus \{0\}, \circ)$: relabelled Cayley tables (**Figure**/tables) (HW 56)
- ◻ Isomorphism definition; Rem. identity maps to identity (stated); Rem. invariants (order, abelian, number of subgroups) (HW 56)
- ◻ Ex. explicit isomorphism $[k]_4 \mapsto [2]_5^k$ (HW 57)
- ◻ Th. $(\Z_p \setminus \{0\}, \circ) \cong (\Z_{p-1}, +)$ for prime $p$ (stated) (HW 57)
- ◻ Non-isomorphism examples: $\Z$ vs $\R \setminus \{0\}$, $\Z_{12}$ vs $\Z_{11} \setminus \{0\}$, $\Z_6$ vs $S_3$ (HW 57)
- ◻ Chinese remainder theorem: $\Z_n \times \Z_m \cong \Z_{nm}$ iff $\gcd(n, m) = 1$ (stated); motivation (HW 57)
- ◻ Ex. $\Z_6 \cong \Z_2 \times \Z_3$, explicit map and table of values; componentwise addition defined (HW 58)
- ◻ Ex. $\Z_2 \times \Z_2 \not\cong \Z_4$ via $x + x = 0$; two Cayley tables with markings (HW 58)

### 5.5 Fields
- ◻ Field $(F, +, \circ)$: two abelian groups and distributive laws (HW 59) ↔ Ch 6 / Ch 9 (MATH1071 field axioms, cited as "(1071)")
- ◻ Ex. $\R$, $\C$, $\Q$ are fields; $\Z_6$ is not (HW 59)
- ◻ Th. $\Z_p$ is a field for prime $p$ (stated, "(1071)") (HW 59) ↔ MATH1071
- ◻ Rem. uses of fields (linear algebra, computer science, other areas) (HW 59)

## Ch 25 Probability Spaces (`ch:probability-spaces`): ↔ merge (written chapter)
- ✅/↔ Random process, sample space, event (HW 63): already covered by Ch 25 §1–2 (STAT2003). MATH1061 wording ("impossible to predict with certainty which outcome") is close to Ch 25's random experiment. **No new content**; add MATH1061 to `\chapterinfo` (already listed).
- ↔ Equally likely outcomes $P(E) = \abs{E}/\abs{S}$; $0 \le P(E) \le 1$ (HW 63): Ch 25 has the equilikely principle (`thm:equilikely-principle`). Merge.
- ◻ Ex. seven tosses of a fair coin: exactly 5 heads $= 21/128$, at least 5 heads $= 29/128$ (HW 63). New example; could replace or join a Ch 25 example (one-example rule).
- ◻ Ex. three cards of the same suit $= 1144/22100 \approx 0.05$ (HW 64). New example.
- ↔ Ex. birthday problem with 23 people, $P \approx 0.507$, via the complement (HW 64): Ch 25 already has the birthday problem with 40 people (`ex:birthday-counting`, `ex:birthday-product-rule`). Merge (e.g. mention $n = 23$), don't duplicate.
- ↔ Inclusion–exclusion (HW 67): see Ch 3 §3.6; Ch 25 keeps the probability version.

## Other courses
- ↔ **MATH1071** (analysis chat): field axioms and $\Z_p$ a field (HW 59); matrix notation (HW 75); possibly rationals, density, sequences, arithmetic and geometric sequences, intervals (HW 16–18, 20, 25, 30) against Ch 9.
- ↔ **MATH2401/2400** (analysis chat): countability and Cantor's diagonal argument (HW 40) if covered there; density of $\Q$ (HW 16).
- ↔ **STAT2003/STAT1301** (Ch 25): counting, equally likely probability, birthday problem, inclusion–exclusion, sets and events.

## Not used yet
- References to the course's online lectures ("See UQ Extend lecture 40 / video 44 / lecture 45 / lecture 46"): replace with "Not proved in this course."
- Course-administrative remarks: "for 1061, we will use $A \in M_{m \times n}(\N)$" (HW 75), "(1071)" (HW 59), "Tutorial week 2" heading (HW 07).
- Crossed-out attempts (HW 08 box, HW 14 case split and "Wrong." proof).

## Suspected errors in the notes
Flagged inline in the transcription as `[possible error: …]` (items 19, 28 and 32 are transcriber's notes rather than error flags). None are applied yet.
1. HW 04: the reasons in the second derivation of $p \to (q \vee r) \equiv (p \wedge \sim q) \to r$ are shifted by one line.
2. HW 05: valid argument means $(p_1 \wedge \dots \wedge p_n) \to q$ is a **tautology**, not "is T". "Validity is independent of the conclusion" should say it depends only on form.
3. HW 07 Q1: the six listed cases are wrong. The form is false in 7 of 8 rows; case 4 ($p = q = $ F, $r = $ T) is the one row where it is true. Rows TTT and FFF are missing.
4. HW 07 Q2: line 1 changes $\vee$ to $\wedge$, so the derivation ends at a contradiction, not $\sim p$. (The identity itself holds.)
5. HW 07 Q3: $(\sim A \vee B) \wedge (\sim B \vee A) \equiv A \leftrightarrow B$, not $A \oplus B$. Since $A \equiv B$ (HW 04), the form is a tautology, not "neither".
6. HW 12: the verbal definition of prime is incomplete (the symbolic one is right).
7. HW 18: "$\Q^2$" should be "$\Q$"; $b^2 \ne 0$ is not stated.
8. HW 19: the contrapositive of "$mn$ odd $\to m, n$ odd" is "$m$ even **or** $n$ even $\to mn$ even". Only the both-even case is proved.
9. HW 17: "non-irrational" should be "irrational".
10. HW 21: "$P(a)$" should be "$P(n)$" in the statement; the conclusion says "$n > 1$" instead of "$n \ge a$".
11. HW 24: the guess's range "$n \in \Z^{+}$, $n \ne 0$" should be $n \ge 0$.
12. HW 26: proper subset should be "$A \subseteq B$ and $A \ne B$".
13. HW 28: the partition example should be $\{\{2\}, \{3, 5\}, \{7, 11\}\}$.
14. HW 33: the function definition needs a **unique** $y$ for each $x$.
15. HW 33: the range of $\sqrt{x^2}$ on $\Z$ includes 0 (it is $\N_0$, not $\Z^{+}$); the domain isn't stated.
16. HW 34: "Injectivity implies monotonicity" is false in general.
17. HW 38: item 3 of the finite-sets theorem doesn't say what $f$ is. "The infinite sets between $\Z$ and $\Q$ are equal" should say "have the same cardinality".
18. HW 39: the zig-zag path turns down at $\frac15$ because the grid is cut off; in the infinite grid it continues to $\frac16$.
19. HW 40: Cantor proof: $d = 0.d_1 d_2 \dots$ and the reason it is not in the list are not written out.
20. HW 41: method 1 ("an injection and a surjection $X \to Y$") is called "standard bijectivity", which it isn't.
21. HW 42: "If $x, y \in R$" should be "If $(x, y) \in R$". In the $\{2, 3, 6\}$ divisibility diagram, 6 needs a loop.
22. HW 43: symmetry proof ends "$n \equiv n$"; should be "$n \equiv m$".
23. HW 47: "the intersection of all classes is $\emptyset$" should be "distinct classes are pairwise disjoint".
24. HW 49: the "i.e." restating a total order omits comparability.
25. HW 50: inverse axiom quantifiers: "$\forall g\ \exists g^{-1}$".
26. HW 53: uniqueness-of-inverse proof writes $h_1 * (h_2 * g)$; should be $h_1 * (g * h_2)$.
27. HW 55: $(g^i)^{-1} = g^{-1}$ should be $g^{-i}$.
28. HW 57: well-definedness of $[k]_4 \mapsto [2]_5^k$ not checked (minor; flag only).
29. HW 58: "no bijection" should be "no isomorphism"; the gcd should be $\gcd(2, 2)$, not $\gcd(2, 4)$.
30. HW 60: "one repeated symbol" answered as "at least one repeated symbol".
31. HW 63: "$S = 2^7$" should be "$\abs{S} = 2^7$". "An event is a subset" is labelled Th. but is a definition.
32. HW 67: the shading of the three-set Venn diagram doesn't follow a clear pattern; redraw it to match the formula (e.g. shade the union).
33. HW 68: function form of the pigeonhole principle has $\abs{A} < \abs{B}$; should be $\abs{A} > \abs{B}$.
34. HW 74: Euler trail conditions need $G$ connected.
35. HW 75: $M_{m \times n}(\N)$ needs $0 \in \N$, which conflicts with the book's $\N = \{1, 2, \dots\}$.

## Notation the book doesn't have yet
To go through `NOTATION_REQUESTS.md` in the hub chat.

| Proposed macro | Renders as | Meaning | Reason |
|---|---|---|---|
| `\lnot` (built-in) or `\Not` | $\neg p$ (notes: $\sim p$) | negation | The notes use $\sim$; the book needs one choice for Ch 1. |
| `\xor` | $\oplus$ | exclusive or | Used HW 01, 07. |
| `\True`, `\False` | $\mathrm{T}$, $\mathrm{F}$ | truth values in tables | Truth tables throughout Ch 1. |
| `\taut`, `\contra` | $\top$, $\bot$ (or $\mathbf{t}$, $\mathbf{c}$) | tautology, contradiction | Used in laws (HW 02, 07, 08). |
| `\divides`, `\ndivides` | $\mid$, $\nmid$ | divides | `\given` is also $\mid$; a separate macro keeps "divides" searchable and spaced correctly. |
| `\Nzero` (or a convention $\N_0$) | $\N_0$ | $\{0, 1, 2, \dots\}$ | The book has $\N = \{1, 2, \dots\}$; the notes use $\N_0$ and $\Z^{+}$. |
| `\id` | $\mathrm{id}_X$ (notes: $i_X$) | identity function | HW 36, 52. |
| `\Zmod{n}` | $\Z_n$ (or $\Z/n\Z$) | integers mod $n$ | Ch 5 throughout; fixes one form. |
| `\gen{a}` | $\langle a \rangle$ | cyclic subgroup generated by $a$ | Avoids confusion with `\inner`. |
| `\eqclass{a}` | $[a]$ (optionally $[a]_n$) | equivalence class | HW 46–58 use $[a]$ and $[a]_4$. |
| `\Sym{n}` | $S_n$ | symmetric group | HW 52, 57. |
| `\iso` | $\cong$ | isomorphic | Notes write "is isomorphic to" in words; the book will want a symbol. |
| `\perm{n}{r}` | ${}^nP_r$ | $r$-permutations | Ch 25 already types ${}^nP_k$ by hand; the notes write $P(n, r)$ and ${}_nP_r$. One macro would fix this across Ch 3 and Ch 25. |
| (convention) | $A^c$ | complement | Ch 25 uses $A^c$; the notes agree. No macro needed; record the convention. |
| (convention) | $A \setminus B$ | set difference | The notes use both $A - B$ and $B \setminus A$. |
| `\Mat{m}{n}{S}` | $M_{m \times n}(S)$ | matrices over $S$ | HW 75; check MATH1071's notation first. |
| (convention) | group multiplication $\cdot$ | | The notes use $\circ$ both for multiplication in $\R$ and $\Z_n$ and for function composition (HW 50–59). The book should use $\cdot$ for multiplication and keep $\circ$ for composition. |

## Code in the notes
None.
