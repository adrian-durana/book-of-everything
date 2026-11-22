# MATH1061 Discrete Mathematics: transcription, part 1 of 3 (HW 01–25)

_Transcription phase. Source: 77 photos of the handwritten notes (one notebook page per photo), taken in shooting order. "HW nn" is the photo number nn in shooting order; the file name is given under each heading. No typed notes or slides were supplied. Course taken in one semester; no dates are recorded here (several pages carry a "Lecture notes" date header, which is omitted)._

**Conventions.** Wording, structure and labels (Def., Th., Lemma, Proof/P., Ex., Rem., Cor.) follow the notes. Maths uses `notation.tex` macros where they exist (`\Z`, `\Q`, `\R`, `\N`, `\abs`, `\powerset`, `\T`). Logical "not" is kept as the notes' $\sim$. Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected); `[illegible]` would mark unreadable text (none needed). Crossed-out text is noted only where it carries meaning. Figures are described in enough detail to redraw in TikZ.

**This part:** logic, quantifiers, proof methods, rational numbers, sequences, induction, recursion.

---

## HW 01 — Negation, conjunction, disjunction, logical equivalence
_File `20261121_225406.jpg`._

**Negation**

Let $p$ be a statement. The *negation* of $p$ is denoted $\sim p$ / $\neg p$ ("not $p$"). Defined by truth table:

| $p$ | $\sim p$ |
|---|---|
| T | F |
| F | T |

(bracketed: "negation")

| $p$ | $q$ | $p \wedge q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

(bracketed: "conj.")

| $p$ | $q$ | $p \vee q$ |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

(bracketed: "disj.")

**Conjunction**

Let $p$ and $q$ be statements. The *conjunction* of $p$ and $q$ is denoted $p \wedge q$ "$p$ and $q$".
$p \wedge q$ is true if $p$ AND $q$ are true, false otherwise.

**Disjunction**

The *disjunction* of $p$ and $q$ is denoted $p \vee q$ "$p$ or $q$".
$p \vee q$ is true when $p$ OR $q$ OR both are true, false if both F.
$p \vee q$ is "inclusive or" – one or other OR both.
$p \oplus q$ is "exclusive or" – only one or other (XOR).

A *statement form* is made of statement variables ($p, q$) and the symbols $\sim, \wedge, \vee$ with unambiguous parentheses.
Two statement forms $P$ and $Q$ are *logically equivalent* "$P \equiv Q$" if they have identical truth values for every combination of truth values for their statement variables.

**Ex.** $P = \sim(p \wedge q)$, $Q = \sim p \wedge \sim q$, $R = \sim p \vee \sim q$.

| $p$ | $q$ | $\sim p$ | $\sim q$ | $p \wedge q$ | $\sim(p\wedge q)$ | $\sim p \wedge \sim q$ | $\sim p \vee \sim q$ |
|---|---|---|---|---|---|---|---|
| T | T | F | F | T | F | F | F |
| T | F | F | T | F | T | F | T |
| F | T | T | F | F | T | F | T |
| F | F | T | T | F | T | T | T |

$\therefore P \equiv R$.

## HW 02 — Laws of logical equivalence; tautologies and contradictions
_File `20261121_225409.jpg`._

**De Morgan's laws** (negation of $\wedge$ and $\vee$)
$$\sim(p \wedge q) \equiv \sim p \vee \sim q, \qquad \sim(p \vee q) \equiv \sim p \wedge \sim q$$
(bracketed: distribute negation ($\sim$), flip conj./disj.)

$$p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r), \qquad p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$$
(bracketed: distributive laws)

$$p \vee (p \wedge q) \equiv p, \qquad p \wedge (p \vee q) \equiv p \qquad \text{(absorption laws)}$$
$$p \wedge p \equiv p, \qquad p \vee p \equiv p \qquad \text{(idempotent laws)}$$

**Statement form – tautology vs. contradiction**

*Tautology*: takes T for all possible truth values of variables.
*Contradiction*: takes F …

$$p \wedge (\text{taut.}) \equiv p, \quad p \vee (\text{cont.}) \equiv p \quad \text{(identity laws)}; \qquad p \vee (\text{taut.}) \equiv \text{taut.}, \quad p \wedge (\text{cont.}) \equiv \text{cont.} \quad \text{(universal bound laws)}$$
$$p \vee \sim p \equiv \text{taut.}, \quad p \wedge \sim p \equiv \text{cont.} \quad \text{(negation laws)}; \qquad \sim(\text{taut.}) \equiv \text{cont.}, \quad \sim(\text{cont.}) \equiv \text{taut.} \quad \text{(negations)}$$

**Ex. Q2** [the statement form is not written out; from the columns it is $(p \wedge \sim q) \wedge (\sim p \vee q)$]

| $p$ | $q$ | $\sim p$ | $\sim q$ | $p \wedge \sim q$ | $\sim p \vee q$ | $\wedge$ |
|---|---|---|---|---|---|---|
| T | T | F | F | F | T | F |
| T | F | F | T | T | F | F |
| F | T | T | F | F | T | F |
| F | F | T | T | F | T | F |

$\therefore$ contradictory.

**Ex. Q3** [statement forms $\sim p \vee (p \wedge q)$ and $\sim p \vee q$]

| $\sim p$ | $p \wedge q$ | $\vee$ | $\sim p \vee q$ |
|---|---|---|---|
| F | T | T | T |
| F | F | F | F |
| T | F | T | T |
| T | F | T | T |

$\therefore \sim p \vee (p \wedge q) \equiv \sim p \vee q$.

## HW 03 — Conditional statements
_File `20261121_225415.jpg`._

**Conditional Statements**

Let $p$ and $q$ be statement variables. The *conditional* from $p$ to $q$ – $p \to q$ – read as "if $p$ then $q$" or "$p$ implies $q$". Defined by truth table:

| $p$ | $q$ | $p \to q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Note that $p \to q$ is false when $p$ is true, $q$ is false.
$p$ is called the *hypothesis*; $q$ is called the *conclusion*.

**Expressing the Conditional with $\sim, \wedge, \vee$**

$$\underbrace{p \to q}_{\text{if } p \text{ then } q} \equiv \sim p \vee q$$

| $p$ | $q$ | $\sim p \vee q$ | $p \to q$ | $\sim q \to \sim p$ | $p \leftrightarrow q$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | F | F | F |
| F | T | T | T | T | F |
| F | F | T | T | T | T |

The *contrapositive* of $p \to q$ is $\sim q \to \sim p$. Logically equivalent.
The *negation* of $p \to q$ ($\sim(p \to q)$) is $p \wedge \sim q$.
Proof using logical equivalence:
$$\begin{aligned}
\sim(p \to q) &\equiv \sim(\sim p \vee q) && \because p \to q \equiv \sim p \vee q \\
&\equiv \sim(\sim p) \wedge \sim q && \because \text{De Morgan's law} \\
&\equiv p \wedge \sim q
\end{aligned}$$

The *biconditional* of $p$ and $q$, denoted $p \leftrightarrow q$, read as "$p$ if and only if $q$", is defined by:
$$p \leftrightarrow q \equiv (p \to q) \wedge (q \to p) \equiv (\sim p \vee q) \wedge (\sim q \vee p)$$

## HW 04 — Conditional: further equivalences, converse, inverse, necessary and sufficient conditions
_File `20261121_225419.jpg`. Page header "Lecture notes" followed by a date (date omitted here)._

| $p$ | $q$ | $p \to q$ | $\sim(p \to q)$ | $\sim p \to \sim q$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | F | T | T |
| F | T | T | F | F |
| F | F | T | F | T |

$$p \to q \equiv \sim(p \wedge \sim q) \equiv \sim p \vee q$$
$$\underbrace{p \,\bar{\wedge}\, q}_{\text{NAND}} \equiv \sim(p \wedge q)$$

[Ex.: show $p \to (q \vee r) \equiv (p \wedge \sim q) \to r$]
$$\begin{aligned}
p \to (q \vee r) &\equiv (p \wedge \sim q) \to r && \text{(Initial statement)} \\
\sim p \vee (q \vee r) &\equiv \sim(p \wedge \sim q) \vee r && \text{(Expressing conditional)} \\
\sim p \vee q \vee r &\equiv \sim p \vee q \vee r && \text{(De Morgan's law)} \\
\text{LHS} &\equiv \text{RHS}
\end{aligned}$$
$\therefore p \to (q \vee r) \equiv (p \wedge \sim q) \to r$.

OR
$$\begin{aligned}
p \to (q \vee r) &\equiv \sim p \vee (q \vee r) && \text{(Associative law)} \\
&\equiv (\sim p \vee q) \vee r && \text{(De Morgan's law)} \\
&\equiv \sim(p \wedge \sim q) \vee r && \text{(Logical equivalence for} \to) \\
&\equiv (p \wedge \sim q) \to r
\end{aligned}$$
[possible error: the justifications in the second derivation look shifted up by one line. Step 1 uses the equivalence for $\to$, step 2 the associative law, step 3 De Morgan's law, step 4 the equivalence for $\to$.]

The *converse* of $p \to q$ is $q \to p$. The converse is NOT logically equivalent to $p \to q$: $p \to q \not\equiv q \to p$.
The *inverse* of $p \to q$ is $\sim p \to \sim q$. $\sim p \to \sim q \equiv q \to p \not\equiv p \to q$.

**Necessary and Sufficient conditions**

"$p$ is a *necessary condition* for $q$" means $\sim p \to \sim q$
  ↳ NEEDED but needs more conditions
"$p$ is a *sufficient condition* for $q$" means $p \to q$
  ↳ LOGICALLY true, can be further strengthened

## HW 05 — Arguments and rules of inference
_File `20261121_225425.jpg`._

**Arguments**

Given a list of statements $p_1, p_2, \dots, p_n$ (*premises*) and another statement $q$ (the *conclusion*), an *argument* is the assertion that the conjunction of the premises $p_n$ implies $q$.

This is symbolically represented as
$$\begin{array}{l} p_1 \\ p_2 \\ \vdots \\ p_n \\ \hline \therefore\ q \end{array}$$
[in the notes there is no horizontal rule; the premises are stacked and the last line is "$\therefore q$"]

An argument is *valid* if whenever all of the premises are true the conclusion is also true. Thus an argument is valid if $(p_1 \wedge p_2 \wedge \dots \wedge p_n) \to q$ is T.
[possible error: "is T" should read "is a tautology" (true for every combination of truth values).]
The validity of an argument is independent of the conclusion.
[possible error: presumably "independent of whether the conclusion is actually true", i.e. validity depends only on the form of the argument.]
An argument is *invalid* if it is possible to have a situation in which all of the premises are true, but $q$ is false.
The validity of an argument can be checked with truth tables.

Each rule is written as premises stacked, then "$\therefore$ conclusion":

| Rule | Premises | Conclusion |
|---|---|---|
| Modus Ponens | $p \to q$; $p$ | $\therefore q$ |
| Modus Tollens | $p \to q$; $\sim q$ | $\therefore \sim p$ |
| Generalisation | $p$ / $q$ | $\therefore p \vee q$ / $\therefore p \vee q$ |
| Specialisation | $p \wedge q$ | $\therefore p$ / $\therefore q$ |
| Conjunction | $p$; $q$ | $\therefore p \wedge q$ |
| Elimination | $p \vee q$; $\sim q$ / $p \vee q$; $\sim p$ | $\therefore p$ / $\therefore q$ |
| Transitivity | $p \to q$; $q \to r$ | $\therefore p \to r$ |
| Proof by division into cases | $p \vee q$; $p \to r$; $q \to r$ | $\therefore r$ |

The RULES OF INFERENCE are stated above.

## HW 06 — Checking validity by contradiction; fallacies
_File `20261121_225428.jpg`._

Checking the validity of ~~a truth table~~ an argument can either be done using a) truth tables or b) the rules of inference.
However there exists an alternative method for determining validity:

If an argument is invalid then there is a situation where all of the premises are true, but the conclusion is false.
If we can find such truth values for all the variables, then the argument will be invalid.
If this is impossible to do, the argument is valid.

**Ex.**
$$\begin{array}{l} p \to \sim r \\ r \vee \sim q \\ q \\ \therefore \sim p \end{array}$$
Suppose this argument is invalid. Hence we can find truth values for $p, q, r$ so that all premises are true, and the conc. is false.
→ $\sim p$ is false $\therefore p$ is true
  $q$ is premise $\therefore q$ is true
  $p \to \sim r$ is premise $\therefore p \to \sim r$ is true $\therefore \sim r$ is true $\therefore r$ is FALSE
$\therefore r \vee \sim q$ is FALSE, proof by cont.

**Fallacies**

*Converse error*: $p \to q$; $q$; $\therefore p$ — just because $q$ is true does not imply $p$ is true – $q$ can be true for reasons other than $p$.

*Inverse error*: $p \to q$; $\sim p$; $\therefore \sim q$ — just because $p$ is not true does not infer that $q$ is not true – $p$ may not be necessary for $q$.

## HW 07 — Tutorial week 2 (logic exercises)
_File `20261121_225438.jpg` (photo is sideways; page heading "Tutorial week 2")._

**1)** $(\sim p \wedge \sim q) \wedge r$ is F
$\therefore (\sim p \wedge \sim q)$ is F or $r$ is F
$\sim(p \vee q)$ is F
$p \vee q$ is T
$\therefore p$ or $q$ or both are T
$\therefore$

| Case | $p$ | $q$ | $r$ |
|---|---|---|---|
| 1 | T | T | F |
| 2 | T | F | F |
| 3 | F | T | F |
| 4 | F | F | T |
| 5 | F | T | T |
| 6 | T | F | T |

[possible error: the form is false for 7 of the 8 rows. Case 4 ($p = q = $ F, $r = $ T) is the one row where it is TRUE, and the row $p = q = r = $ T is missing. The working above also only follows the branch "$\sim p \wedge \sim q$ is F", leaving out $p = q = r = $ F.]

**2)** $\sim(p \vee \sim q) \vee (\sim p \wedge \sim q) \equiv \sim p$
$$\begin{aligned}
&\equiv \sim(p \vee \sim q) \wedge \sim(p \vee q) \\
&\equiv \sim([p \vee \sim q] \vee [p \vee q]) \\
&\equiv \sim([p \vee p] \vee [\sim q \vee q]) \\
&\equiv \sim(p \vee \mathrm{T}) \\
&\equiv \sim p
\end{aligned}$$
(the last four lines are bracketed with the note "check")
[possible error: the main connective in line 1 should stay $\vee$: $\sim(p \vee \sim q) \vee \sim(p \vee q)$, which by De Morgan is $\sim([p \vee \sim q] \wedge [p \vee q])$. As written, $\sim(p \vee \mathrm{T}) \equiv$ contradiction, not $\sim p$. The identity itself is true: $\sim([p \vee \sim q] \wedge [p \vee q]) \equiv \sim(p \vee (\sim q \wedge q)) \equiv \sim p$.]

**3)** $(p \to (q \vee r)) \leftrightarrow ((p \wedge \sim q) \to r)$
$$\begin{aligned}
&\equiv (\sim p \vee (q \vee r)) \leftrightarrow (\sim(p \wedge \sim q) \vee r) \\
&\equiv (\sim[\sim p \vee (q \vee r)] \vee [\sim(p \wedge \sim q) \vee r]) \wedge (\sim[\sim(p \wedge \sim q) \vee r] \vee (\sim p \vee (q \vee r)))
\end{aligned}$$
Let $A = \sim p \vee (q \vee r)$, $B = \sim(p \wedge \sim q) \vee r$.
$$\equiv (\sim A \vee B) \wedge (\sim B \vee A) \equiv A \oplus B$$
$\therefore$ neither $\top$ or $\bot$ [tautology nor contradiction]
[possible error: $(\sim A \vee B) \wedge (\sim B \vee A) \equiv A \leftrightarrow B$, not $A \oplus B$. Since $A \equiv B$ (HW 04), the form is a tautology, not "neither".]

## HW 08 — Arguments by rules of inference and by contradiction
_File `20261121_225443.jpg`. Page header "Lecture notes" followed by a date (omitted)._

**Ex.**
$$\begin{array}{l} w \to b \\ d \to \sim b \\ \therefore \sim d \vee \sim w \end{array} \qquad (w \to b) \wedge (d \to \sim b) \to \sim d \vee \sim w$$

**Ex.** Premises 1) $p \to q$, 2) $p \vee r$, 3) $p \vee \sim r$; $\therefore q$. [premises 2–3 bracketed together]

| Step | Statement | Reason |
|---|---|---|
| 4) | $(p \vee r) \wedge (p \vee \sim r)$ | Conjunction |
| 5) | $p \vee (r \wedge \sim r)$ | Distributive law |
| 6) | $p \vee \bot$ | Negation law |
| 7) | $p$ | Identity law |
| $\therefore$ | $q$ by 1), 7) and modus ponens | |

[the notes spell it "modens ponens"]

**Ex.** Premises $w \to b$, $d \to \sim b$; $\therefore \sim d \vee \sim w$.
A first attempt in a box is crossed out with a large X: 3) $(w \to b) \wedge (d \to \sim b)$; 4) $(\sim w \vee b) \wedge (\sim d \vee \sim b)$; 5) $(b \vee \sim w) \wedge \sim(d \wedge b)$; $(b \vee \sim w) \wedge \sim(b \wedge d)$; 4=6) $(\sim b \vee \sim d) \wedge (b \vee \sim w)$; 7) $(\sim b \vee \sim d) \wedge \sim(\sim b \wedge w)$.
The working that stands:

| Step | Statement | Reason |
|---|---|---|
| 2=8) | $b \to \sim d$ | Contrapositive |
| $\therefore$ 9) | $w \to \sim d$ | Transitivity |
| 10) | $\sim w \vee \sim d$ | Logical eq. for $\to$ |
| $\therefore$ | $\sim d \vee \sim w$ by 10) | |

**Ex.** Suppose argument invalid – premises true, conclusion false.
Premises $p \to q$, $p \vee r$, $p \vee \sim r$; $\therefore q$.
→ $q$ false.
$\because p \to q$ true and $q$ false $\therefore p$ false
$\because p \vee r$ true and $p$ false $\therefore r$ true
↳ using 1) 2) now 3) is false QED $\therefore$ argument valid

**Ex.** Premises $p \to q$, $q \to r$, $\sim p \vee \sim q$; $\therefore r$.
→ $r$ false.
$\because p \to q$ true, $q$ false $\therefore p$ false
$\because q \to r$ true, $r$ false $\therefore q$ false
↳ $\sim p \vee \sim q$ is true $\therefore$ argument invalid, QED

## HW 09 — Quantified statements
_File `20261121_225449.jpg`._

**Quantified statements**

A *predicate* is a sentence that contains finitely many variables, which becomes a statement if the variables have specific values.
The *domain* of each variable in a predicate is the set of all possible values that may be assigned to it. Denoted $P(x)$.

The *truth set* of $P(x)$ is the set of all values in that, when assigned to $x$, make $P(x)$ a true statement. [a word is missing: "all values in $D$ that"]

**Ex.** $P(x)$ is the predicate "$x$ divides 5" $\subseteq \Z$ as domain of $x$. [read: "with $\Z$ as domain of $x$"]
The truth set of $P(x)$ is $\{-5, -1, 1, 5\}$.

Common domains: $\Z$, $\Z^{+} = \N$, $\N_0 = \Z \setminus \Z^{-}$, $\Q$, $\R$.

Let $Q(x)$ be a predicate and $D$ be the domain of $x$.
The *universal statement* $\forall x \in D,\ Q(x)$ is true iff $Q(x)$ is true for every $x$ in $D$.

The *existential statement* $\exists x \in D : Q(x)$ is true iff $Q(x)$ is true for at least one $x$ in $D$.

One of the most important statement forms in mathematics is $\forall x \in D,\ (P(x) \to Q(x))$.

**Ex.** $\forall x \in \R$, if $x > 3$ then $x^2 > 9$.

## HW 10 — Negations of quantified statements
_File `20261121_225453.jpg` (photo is sideways). The lower third of the page is blank._

**Negations of quantified statements**

Consider the universal statement $\forall x \in D,\ Q(x)$.
The negation of this statement is logically equivalent to:
$$\exists x \in D : \sim Q(x)$$

Now consider the existential statement $\exists x \in D : R(x)$.
The negation of this statement is logically equivalent to:
$$\forall x \in D,\ \sim R(x)$$

For the universal conditional statement $\forall x \in D,\ (P(x) \to Q(x))$
the negation of this statement is logically equivalent to:
$$\exists x \in D : \sim(P(x) \to Q(x)) \equiv \exists x \in D : P(x) \wedge \sim Q(x)$$

**Ex.** Statement: $\forall x \in \Z$, if $x \ge 1$ then $x \in \N$. — T
Negation: $\exists x \in \Z : x \ge 1$ and $x \notin \N$. — $\therefore$ F

## HW 11 — Statements with multiple quantifiers
_File `20261121_225500.jpg`._

**Statements with multiple quantifiers**

**Ex.** The predicate $x \le y$ for $x, y \in \R$ involves more than one variable.
We use notation such as $P(x, y)$ to denote such predicates.
Such predicates often appear in statements that involve more than one quantifier.
**Ex.** $\exists x \in \Z^{+} : \forall y \in \Z^{+},\ x \le y$

If you want to establish the truth of a statement of the form
$$\forall x \in D,\ \exists y \in E : P(x, y)$$
you must allow any $x \in D$ to be picked, and then you must find an element $y \in E$ which makes $P(x, y)$ true.
**Ex.** $\forall x \in \Z,\ \exists y \in \Z : x + y = 0$.
For any $x \in \Z$ take $y = -x$. Then $x + y = x - x = 0$.

If you want to establish the truth of a statement of the form
$$\exists x \in D : \forall y \in E,\ P(x, y)$$
you must find one particular $x \in D$ which makes $P(x, y)$ true regardless of the value of $y \in E$ picked.
**Ex.** $\exists x \in \Z^{+} : \forall y \in \Z^{+},\ x \le y$.
Take $x = 1$. Now $\forall y \in \Z^{+},\ x \le y$.

Negation of $\forall x \in D,\ \exists y \in E : P(x, y)$
↳ $\exists x \in D : \sim(\exists y \in E : P(x, y))$
↳ $\exists x \in D : \forall y \in E,\ \sim P(x, y)$

Negation of $\exists x \in D : \forall y \in E,\ P(x, y)$
↳ $\forall x \in D,\ \sim(\forall y \in E,\ P(x, y))$
↳ $\forall x \in D,\ \exists y \in E : \sim P(x, y)$

## HW 12 — Parity, primality, direct proof
_File `20261121_225523.jpg`._

**Parity**

**Th.**
$n$ is even $\iff \exists k \in \Z : n = 2k$
$n$ is odd $\iff \exists k \in \Z : n = 2k + 1$

**Primality**

**Def.** An integer $n$ is *composite* iff $n > 1$ and $n = rs$ for some positive integers $r$ and $s$, $r, s \ne 1$.
An integer $n$ is *prime* if $r$ or $s = 1$.
[possible error: as worded, the prime definition omits "$n > 1$ and, for all positive integers $r, s$ with $n = rs$"; the symbolic version below has it.]
$$n \text{ is prime} \iff n > 1 \wedge \forall r, s \in \Z^{+},\ n = rs \to (r = 1 \vee s = 1)$$
$$n \text{ is composite} \iff n > 1 \wedge \exists r, s \in \Z^{+} : n = rs \wedge r \ne 1 \wedge s \ne 1$$

**Proving existential statements** – find one example where $P(x)$ true.

**Direct proof of universal statements** $\forall x \in D,\ P(x) \to Q(x)$
1) Suppose $x \in D$ and $P(x)$ is true
2) Show that the conclusion $Q(x)$ is true using definitions, previously established results and the rules for logical inference
3) If $P(x)$ true and $Q(x)$ false, $P(x) \to Q(x)$ false

**Ex.** $\forall n \in \Z$, if $n$ is odd then $n^2$ is odd.
**Proof:** Suppose $n \in \Z$, $n$ is odd.
By definition, $n = 2k + 1$ for some $k \in \Z$.
Hence
$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
$\because k \in \Z$ and $2 \in \Z$, $2k^2 + 2k \in \Z$.
Thus $\exists \ell \in \Z : n^2 = 2\ell + 1$ $\therefore n^2$ is odd.

$d \mid n \iff n = dk,\ d \ne 0$ [written at the foot of the page; "for some $k \in \Z$" is not written]

## HW 13 — How to write a proof; disproof by counterexample
_File `20261121_225529.jpg`. A horizontal rule runs across the page below the "Disproof" line._

**How to write a proof**
- write the theorem to be proved
- clearly mark the beginning of the proof with "Proof:"
- use precise definitions for any mathematical terms
- write the proof in complete sentences
- give a reason for each assertion in your proof
- make your proof self-contained
- display equations and inequalities clearly
- conclude by stating what it is you have proved

**Disproof by counterexamples** → show counterexample true

**Ex.** $\forall m \in \Z,\ (m > 2) \to (m^2 - 4)$ composite.
**Proof.** Suppose $m > 2$.
Consider $m^2 - 4 = (m+2)(m-2)$.
$m = 3$: $5 = 5 \cdot 1$ $\therefore 5$ prime.
Since $5 = 5 \cdot 1$, this is false as 5 is prime.
[this is a disproof by counterexample, although it is headed "Proof."]

**Ex.** $(n+1)^2 - n^2$ is odd, $n \in \Z$.
**Proof.** Consider
$$(n+1)^2 - n^2 = n^2 + 2n + 1 - n^2 = 2n + 1$$
$\because n \in \Z$ $\therefore 2n + 1$ is odd. $\square$

## HW 14 — Direct proof and existence examples
_File `20261121_225536.jpg`. Page header "Lecture notes" followed by a date (omitted). Horizontal rules separate the examples._

**Ex.** Prove that $(x + 6 = 4y) \to \frac{x}{2}$ is odd, $x, y \in \Z$.
**Proof:** Suppose $x + 6 = 4y$ is true.
$$x = 4y - 6 = 2(2y - 3), \qquad \frac{x}{2} = 2y - 3 = 2y - 4 + 1 = 2(y - 2) + 1$$
Since $\frac{x}{2}$ is ~~not~~ odd.
~~for odd $y$, therefore $x$~~ ←
[A boxed case split to the right is crossed out with a large X: "If $y$ even then $y = 2k$, $k \in \Z$: $\frac{x}{2} = 2k - 3 = 2(k-1) - 1$ $\therefore$ odd. If $y$ odd then $y = 2k + 1$, $k \in \Z$: $\frac{x}{2} = 2k + 1 - 3 = 2k - 2 = 2(k-1)$ $\therefore$ even." The crossed-out work uses $\frac{x}{2} = y - 3$, which is wrong; the proof on the left stands.]

**Ex.** Prove that for each integer $n \ge 2$, the product of the first ~~two~~ $n$ primes $-1$ is prime.
**Proof:** see $n = 4$.
[a word "Proof" before the "Ex." is scribbled over in a hatched box; the counterexample itself is not written out]

**Ex.** $\exists m, n \in \Z : \left(\frac{1}{m} + \frac{1}{n}\right) \in \Z$
**Proof.** Suppose $m = 1$, $n = -1$.
$$\frac{1}{m} + \frac{1}{n} = \frac{1}{1} + \frac{1}{-1} = 1 + (-1) = 0$$
Since $0 \in \Z$, therefore $\exists m, n \in \Z : \left(\frac{1}{m} + \frac{1}{n}\right) \in \Z$.

**Ex.** $\forall m, n \in \Z$, if $n - m$ is even, then $n^3 - m^3$ is even.
**Proof.** [first attempt, marked "Wrong." by the author]
$$n^3 - m^3 = (n - m)(n^2 + 2nm + m^2) = (n - m)(n^2 + nm + m^2) = (n - m)\bigl[(n - m)^2 + 3nm\bigr]$$
**Proof** Suppose $m, n \in \Z$, $n - m$ is even. $n - m = 2k$ for some $k \in \Z$.
$$n^3 - m^3 = (n - m)(n^2 + nm + m^2) = 2k(n^2 + nm + m^2), \qquad n^2 + nm + m^2 \in \Z$$
$\therefore n^3 - m^3$ is even. $\square$

## HW 15 — Proof by contradiction and by contraposition
_File `20261121_225541.jpg`._

**Method of proof by contradiction**
1) Assume that the statement is false
2) Show that this leads logically to contradiction – it is impossible that the statement is false
3) Conclude that the statement is true

**Proof of contradiction for $\forall x \in D,\ (P(x) \to Q(x))$**
1) Assume that the statement is false – therefore the negation is true: $\exists x \in D$ s.t. $P(x) \wedge \sim Q(x)$.
2) Show that this assumption leads logically to contradiction.
3) Conclude that the statement is true.

**Method of contraposition proof**
1) Express the statement to be proved in the form $\forall x \in D,\ (P(x) \to Q(x))$
2) Rewrite this statement in contrapositive form $\forall x \in D,\ (\sim Q(x) \to \sim P(x))$ [a first attempt is crossed out]
3) Prove the contrapositive with direct proof:
  ↳ Suppose $x \in D$, and $Q(x)$ false
  ↳ Show that $P(x)$ is false
Often, the contrapositive form of a statement is easier to prove directly than the original statement.

## HW 16 — Rational numbers: closure lemmas, density
_File `20261121_225545.jpg`._

**Rational numbers**

The set of rationals $\Q$ is defined by $\exists a, b \in \Z : r = \frac{a}{b},\ b \ne 0$.
The decimal expansion of a rational number repeats.

**Lemmas:**
1. $\forall r, s \in \Q,\ r + s \in \Q$
2. $\forall r, s \in \Q,\ s \notin \{0\},\ r/s \in \Q$ OR $\forall r, s \in \Q,\ (s \ne 0) \to (r/s \in \Q)$

**Proof 1:** $r, s \in \Q$ $\therefore r = \frac{a}{b}$, $s = \frac{c}{d}$ where $a, b, c, d \in \Z$, $b, d \ne 0$.
$$r + s = \frac{ad + bc}{bd} \qquad \because a, b, c, d \in \Z \ \therefore ad + bc \in \Z,\ \therefore bd \in \Z,\ bd \ne 0$$
By definition therefore $(r + s) \in \Q$. $\square$

**Proof 2:** $r, s \in \Q$ and $s \ne 0$ $\therefore r = \frac{a}{b}$, $s = \frac{c}{d}$ where $a, b, c, d \in \Z$, $b, d \ne 0$.
$$r/s = \left(\frac{a}{b}\right) \div \left(\frac{c}{d}\right) = \frac{ad}{bc} \qquad \because a, b, c, d \in \Z \ \therefore ad \in \Z,\ \therefore bc \in \Z,\ bc \ne 0$$
By definition therefore $r/s \in \Q$. $\square$
[$c \ne 0$, needed for $bc \ne 0$, follows from $s \ne 0$ but is not stated.]

**Theorem:** $\forall r, s \in \Q,\ r < s,\ \exists q \in \Q : r < q < s$.
**Proof:** Suppose $r, s \in \Q$ and $r < s$.
By definition, $r = \frac{a}{b}$, $s = \frac{c}{d}$ where $a, b, c, d \in \Z$, $b, d \ne 0$.
Take $q = \frac{1}{2}(r + s)$. $(r + s) \in \Q$ and $2 \in \Q$, $2 \ne 0$ $\therefore q = \frac{1}{2}(r + s) \in \Q$.
Since $r < s$:
$$\tfrac{1}{2}(r + r) < \tfrac{1}{2}(r + s) < \tfrac{1}{2}(s + s)$$
$$= r < q = \tfrac{1}{2}(r + s) < s \qquad = r < q < s$$
$\therefore q \in \Q$ and $r < q < s$. $\square$
["=" is used for "hence" on the last two lines.]

## HW 17 — Rational numbers: inverses; rational + irrational
_File `20261121_225550.jpg`._

**Rational numbers**

**Theorem:** $\forall r \in \Q,\ r \ne 0,\ \exists s \in \Q,\ s \ne 0 : r \cdot s = 1$
**Proof:** Suppose $r$ is a nonzero rational number.
Then $r = \frac{a}{b}$ for some $a, b \in \Z \setminus \{0\}$.
Now $s = \frac{b}{a}$ is non-zero, rational as $a, b \in \Z \setminus \{0\}$.
Also, $rs = \frac{a}{b} \cdot \frac{b}{a} = 1$. $\square$
Therefore $\forall r \in \Q \setminus \{0\}\ \exists s \in \Q \setminus \{0\} : r \cdot s = 1$.

**Lemma:** The sum of any rational number and non-irrational number is irrational.
[possible error: "non-irrational" should be "irrational"; the proof treats $x \in \R \setminus \Q$.]
**Proof by contradiction:** Suppose the lemma is false.
Then $\exists q \in \Q,\ x \in \R \setminus \Q$ such that $x + q$ is rational.
Thus, by definition, $q = \frac{a}{b}$ and $x + q = \frac{c}{d}$, $a, b, c, d \in \Z$, $b, d \ne 0$.
Hence
$$x = \frac{c}{d} - q = \frac{c}{d} - \frac{a}{b} = \frac{bc - ad}{bd}$$
Since $a, b, c, d \in \Z$, $b, d \ne 0$, therefore $bc - ad \in \Z$, $bd \in \Z$.
Therefore by definition, $x \in \Q$.
This is a contradiction – therefore, the lemma is proved. $\square$

## HW 18 — Rational expressions; contrapositive with irrationals
_File `20261121_225554.jpg`. Page header "Lecture notes" followed by a date (omitted)._

**Ex.** Prove that $\forall r \in \Q,\ (2r^2 - 3r + 1) \in \Q$.
**Proof.** Suppose $r \in \Q$. Therefore $r = \frac{a}{b}$ for some $a, b \in \Z$, $b \ne 0$.
$$2r^2 - 3r + 1 = 2\left(\frac{a^2}{b^2}\right) - 3\left(\frac{a}{b}\right) + 1 = \frac{2a^2}{b^2} - \frac{3a}{b} + 1$$
Since $a, b \in \Z$, therefore $a^2, b^2 \in \Z$; $\because b \ne 0 \ \therefore b^2 \ne 0$; therefore $\frac{a^2}{b^2}, \frac{a}{b} \in \Q$.
Since $1 \in \Z \subset \Q$, therefore $2 \cdot \frac{a^2}{b^2} - 3 \cdot \frac{a}{b} + 1 \in \Q$.
Therefore $2r^2 - 3r + 1 \in \Q$. $\square$

**Ex.** Prove $\forall r \in \R,\ r^2 \in \bar{\Q} \to r \in \bar{\Q}$. [$\bar{\Q}$: the irrationals]
**Proof.** We will prove its contrapositive: $\forall r \in \R,\ r \in \Q \to r^2 \in \Q^2$
[possible error: "$\Q^2$" should be "$\Q$", as in the last line.]
Suppose $r \in \Q$:
Thus $r = \frac{a}{b}$, $a, b \in \Z$, $b \ne 0$. Hence $r^2 = \left(\frac{a}{b}\right)^2 = \frac{a^2}{b^2}$.
Since $a \in \Z$, $\therefore a^2 \in \Z$; $b \in \Z$, $\therefore b^2 \in \Z$; $a^2, b^2 \in \Z$, $\therefore \frac{a^2}{b^2} \in \Q$.
Therefore $r \in \Q \to r^2 \in \Q$. $\square$
[$b^2 \ne 0$ is not stated here.]

## HW 19 — Products of odd integers
_File `20261121_225600.jpg`. Page header "Lecture notes" followed by a date (omitted)._

**Ex.** Prove $\forall m, n \in \Z$, $mn$ odd $\Leftarrow$ $m, n$ odd. [the arrow was first written as $\Leftrightarrow$ and corrected to $\Leftarrow$]
**Proof.** Suppose $m, n$ are odd $\therefore m = 2k + 1$ for some $k \in \Z$, $n = 2\ell + 1$ for some $\ell \in \Z$.
Hence
$$m \cdot n = (2k + 1)(2\ell + 1) = 4k\ell + 2k + 2\ell + 1 = 2(2k\ell + k + \ell) + 1$$
Since $2, k, \ell \in \Z$, $\therefore 2k\ell, k, \ell \in \Z$ $\therefore 2k\ell + k + \ell \in \Z$.
$m, n \in \Z$. Therefore $\exists a \in \Z$ s.t. $m \cdot n = 2a + 1$ (by definition odd). $\square$

**Ex.** Prove $\forall m, n \in \Z$, $mn$ odd $\to m, n$ odd.
**Proof.** We will prove by taking the contrapositive: $m, n$ even $\to mn$ even.
Suppose $m, n$ are even $\therefore m = 2k$, $n = 2\ell$ for some $k, \ell \in \Z$.
Hence
$$m \cdot n = 2k \cdot 2\ell = 4k\ell = 2(2\ell k)$$
Since $2, k, \ell \in \Z$, $\therefore 2k\ell \in \Z$.
Therefore $\forall m, n \in \Z\ \exists a \in \Z$ s.t. $m \cdot n = 2a$ (def. even). $\square$
[possible error: the contrapositive of "$mn$ odd $\to$ ($m$ odd and $n$ odd)" is "($m$ even or $n$ even) $\to mn$ even". Proving the case where both are even is not enough.]

## HW 20 — Sequences; summation and product notation
_File `20261121_225614.jpg`._

**Sequences**

**Def.** A *sequence* is an ordered list of elements. It can be finite, or infinite. Each individual element in a sequence is called a *term*.

An *explicit / general formula* for a sequence is a rule showing how the value of a term depends upon $k$.

**Ex.** $\{2^k\}_{k \ge 0}$ or $\{2^k\}_{k=0}^{\infty}$ or $(2^k)_{k \in \N_0}$, etc. [the index set in the last form is small; it reads as $\N_0$]

**Summation notation:**
**Def.**
$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \dots + a_n, \qquad m \le n,\ m, n \in \Z$$
The variable $i$ '$a_i$' is a *dummy variable*. Any unused pronumeral can be used.
Dummy variables are only relevant INSIDE the sum – you can reuse them outside sums too.
You can also perform 'change in variables' too.

**Product notation**
$$\prod_{i=m}^{n} a_i = a_m \cdot a_{m+1} \cdot \dots \cdot a_n, \qquad m \le n,\ m, n \in \Z$$

## HW 21 — Mathematical induction
_File `20261121_225623.jpg`._

**Mathematical induction**

**Ex.** Suppose $P(n)$ is a predicate and we know:
- $P(1)$ — $P(1)$
- $P(2)$ — by $P(1) \to P(2)$
- $P(3)$ — by $P(2) \to P(3)$
- … $P(4)$ — by $P(3) \to P(4)$

Can we conclude that $P(4)$ is true? Yes – by repeated use of modus ponens. [spelt "modens ponens"]

**Def.** Let $P(n)$ be a predicate that is defined for all $n \in \Z$, $n \ge a$, $a \in \Z$. Suppose that:
1) $P(a)$ is true
2) $\forall k \in \Z,\ k \ge a,\ P(k) \to P(k+1)$
Then $P(n)$ is true $\forall n \in \Z,\ n \ge a$.

**Using mathematical induction**

**Def.** To prove that for every integer $n \ge a$, $P(a)$: [possible error: should be $P(n)$]
1) *Basis step*: Prove $P(a)$.
2) *Inductive step*: Prove that $\forall k \in \Z,\ k \ge a,\ P(k) \to P(k+1)$
  ↳ Here we must:
  - Suppose $k \in \Z$, $k \ge a$, $P(k)$ is true. (the *Inductive Hypothesis*)
  - Using this, show $P(k+1)$ is true.
3) Conclude: "Therefore, by the principle of mathematical induction, for every integer $n > 1$, $P(n)$."
[possible error: "$n > 1$" should be "$n \ge a$" for the general statement.]

## HW 22 — Strong induction; the well-ordering principle
_File `20261121_225633.jpg`._

**Strong mathematical induction**

**Def.** Suppose $P(n)$ is a predicate defined for any $n \ge a$, and let $b \ge a$, $a, b, n \in \Z$. Suppose:
1) Basis step: $P(a), P(a+1), \dots, P(b)$ is true
2) Inductive step: $\forall k \in \Z,\ k \ge b$, if $P(a), P(a+1), \dots, P(k)$ is true then $P(k+1)$ is true.
Then $P(n)$ is true for every integer $n \ge a$.
It can be shown that this is equivalent to the ordinary principle of mathematical induction.

**The well-ordering principle for $\Z$:**
**Def.** If $S$ is a non-empty set of integers, all of which are greater than some fixed integer, then $S$ has a least element.

**Def.** It can be shown that WOP $\equiv$ MI $\equiv$ SMI.

**Ex.** For each of the following sets, does the least element exist?
- $\{x \mid x \in \Z,\ x > 2\}$ — Y
- $\{x \in \N\}$ — Y
- $\{x \mid x \in \Z,\ x = 2k + 1,\ k \in \Z\}$ — N
- $\{x \mid x \in \R,\ x > 0\}$ — N

## HW 23 — Recurrence relations; ways to define sequences; recursive definitions
_File `20261121_225637.jpg`._

**Recurrence relations**

**Def.** A *recurrence relation* for a sequence $a_0, a_1, a_2, \dots$ is a formula that relates each term $a_k$ to some predecessor term $a_{k-1}, a_{k-2}, \dots, a_{k-i}$, $i \in \Z$, $k - i \ge 0$.
The *initial condition/s* specify the values of the initial term/s.

**Ex.** The Fibonacci sequence is defined recursively by:
$$F_0 = 1, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad \forall n \ge 2 \in \N$$

**Ways to define sequences**
**Def.**
- Informally: i.e. listing the first few terms until pattern is obv.
- With general formula: i.e. how each term $a_n$ depends on $n$.
- Recursively: i.e. by stating a recurrence relation between $a_n$.

**Recursive definitions**
**Def.** Many other objects other than numbers can be defined recursively as well, such as sets, sums, products, functions, etc.
A *recursive definition* for a set of objects requires three things:
- I BASE: a statement that a certain object belongs in the set.
- II RECURSION: a collection of rules showing how to form new objects for the set from existing objects in the set.
- III RESTRICTION: a statement that no objects belong to the set other than those from prior steps.

## HW 24 — The method of iteration
_File `20261121_225645.jpg`._

**The method of iteration**

**Def.** Given a sequence that is defined recursively, we may wish to find an explicit formula for the sequence. We can use the *method of iteration*:
1) Use iteration to write the first terms of the sequence, guess an explicit formula.
2) Use induction to prove the guess correct.

**Ex.** Find an explicit formula for the sequence defined by: $b_0 = 2$, $b_n = b_{n-1} + 5$.
We have $b_0 = 2$, $b_1 = 2 + 5 = 7$, …
Each term is $+5$ the previous term.
Note that repeated addition can be expressed as $\times$.
Guess: $b_n = 5n + 2$, $n \in \Z^{+}$, $n \ne 0$.
[possible error: the range should be $n \ge 0$ (as in the next line); $b_0 = 2$ fits the formula.]
Next, we prove that for $n \ge 0$, $b_n = 5n + 2$.

**Proof:**
*Basis step.* $n = 0 \implies b_0 = 2$ and $5(0) + 2 = 2$.
*Inductive hypothesis.* Suppose for some integer $k \ge 0$, $b_k = 5k + 2$.
$$b_{k+1} = b_k + 5 = 5k + 2 + 5 = 5(k+1) + 2$$
Therefore, by the principle of mathematical induction, for every integer $n \ge 0$, $b_n = 5n + 2$. $\square$

**Def.** It is not always possible to guess an explicit formula. Some recursively defined sequences do not possess one.

## HW 25 — Arithmetic and geometric sequences
_File `20261121_225648.jpg`. The lower half of the page is blank._

**Arithmetic sequences**
**Def.** A sequence $a_0, a_1, a_2, \dots$ is *arithmetic* iff there is a constant $d$ such that $a_k = a_{k-1} + d$ for every integer $k \ge 1$.
An explicit formula: $a_n = a_0 + dn$, $n \ge 0$, $n \in \Z$.

**Geometric sequences**
**Def.** A sequence $a_0, a_1, a_2, \dots$ is *geometric* iff there is a constant $r$ such that $a_k = r \cdot a_{k-1}$ for every integer $k \ge 1$.
An explicit formula: $a_n = a_0 \cdot r^n$, $n \ge 0$, $n \in \Z$.
