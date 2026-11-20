# Style Guide — Book of Everything

This is a living document. The section "Writing and layout preferences" collects the author's review feedback (from Chapter 25 onwards). It applies to every chapter, not only the one that prompted it.

## Content rule (current phase: course ingestion)
- **Write only what is in the course materials** (handwritten notes, course notes, slides). Do not add new information: no extra theorems, proofs, examples, remarks, figures or extensions.
- **Correct mistakes.** Fix errors in the notes, especially in the handwritten ones, and list each correction in the course's coverage inventory.
- **Leave gaps alone.** If a source states a result without proof, state it without proof and say so ("not proved in this course"). Later courses will usually fill the gap.
- **One motivating example, two at most.** Keep the background and motivation from the course notes, but use only one (in extreme cases two) motivating examples per section or subsection.
- **Writing style.** Use the writing style and wording of the handwritten notes as the main reference. Use the typed notes' style where they explain the content better. For courses with no handwritten notes, use the style of the STAT2003 and STAT1301 typed notes.
- **Figures.** Every image in the typed or handwritten notes (diagrams, plots, Venn diagrams, trees) is redrawn in TikZ/pgfplots. Use the shared `bookplot` style from the preamble. Plots of random simulations use data generated in R with a fixed seed, pasted as coordinates.
- **Titles change as content grows.** Rename, merge and rearrange sections and subsections whenever new course material is added, so the structure stays logical.
- **No linking material yet.** Cross-references are limited to "Builds on" and direct citations of results the sources themselves use. Connections, motivation and linking information are added in a separate pass, after every course has been ingested.

## Voice
- Aim between lecture notes and a textbook: precise, but readable. Write in full sentences, and don't pad.
- Use "we" in arguments ("we show that…"). Never use "the student" or "the reader will…".
- Before a hard proof, give one sentence on the idea.
- Use Australian/British spelling: optimisation, modelling, behaviour, parametrise.

## Structure
- Part → Chapter → Section → Subsection. Aim for 15–40 pages per chapter.
- Every chapter starts with `\chapterinfo{<courses>}{<builds on>}`. "Builds on" uses `\cref` to earlier chapters, or is just `nothing` (lower case, no full stop).
- A chapter may use only material from chapters it lists in "Builds on" (plus general mathematical maturity). Anything else is stated in full, or proved in the chapter.

## Environments
| Environment | Use for |
|---|---|
| `definition` | Every new term. The term being defined goes in `\emph{}`. |
| `theorem` | Major results. |
| `proposition` | Smaller results worth naming. |
| `lemma` | Technical steps used in proofs. |
| `corollary` | Immediate consequences. |
| `proof` | A full proof for every stated result in the Important and Background tiers. If a proof is genuinely beyond scope, say so and give a reference. |
| `example` + `solution` | 1–2 per major method. Rewrite exam questions; don't copy them. |
| `remark` | Intuition, warnings, common mistakes, connections. |
| `python` / `rcode` | Short snippets. R (`rcode`) for Parts III–IV (Probability, Statistics); Python (`python`) for all other Parts. Use the other language only when strictly necessary. |

- All items share one counter per chapter (Definition 3.1, Theorem 3.2, …).
- Give every result a short descriptive name in brackets where one exists, e.g. `[Continuity of probability]`. Don't attach names to individual list items (no "(complement rule)").

## Writing and layout preferences (author's review feedback)
These come from the author's reviews (Chapter 25 onwards). Every piece of review feedback, even when it is about one chapter, is recorded here as a general rule and applied to every chapter, including new ones and those drafted by course chats. When a review adds a new preference, add it here in the same session.

### Tone and length
- This is a personal reference book. Don't write as if the reader is seeing the material for the first time. The exception is the harder third-year courses, where the expanded, first-encounter style is kept.
- Open each chapter with one short explanatory paragraph: what the topic is for, its main building blocks, and what the chapter covers. Model it on the Chapter 25 opening ("The purpose of this chapter is to introduce…").
- Keep section and subsection introductions short. Set a model up once, then let the examples be brief (see Ch 25, "Coin-tossing models").
- Keep the source's wording where it reads well. Paraphrase only to shorten or clarify.
- Cut filler sentences:
  - announcements such as "Because this principle is so important, we formulate it as a theorem";
  - restatements of the obvious, such as "Axiom 2 just states that the probability of the certain event is 1";
  - commentary on a figure that only repeats what the figure shows, such as "In this diagram, A ∩ C = ∅, so A and C are disjoint".
- Cut qualifiers that add nothing, such as "(in days)" or "(and will)".
- Prefer precise words: "almost surely" rather than "certainly" where that is the meaning, and "a set of possible outcomes" where the set isn't unique.
- Numbers in prose: write "0.5" rather than "½" for values such as limits and probabilities.
- Don't elaborate on a term that is outside the chapter's scope (e.g. no examples of measurable spaces in the random-variable definition).
- Distribution definitions all follow one template: "A random variable $X$ has a *… distribution* with parameters …, written $X \sim \ldots$, if its pmf/pdf is [display]. It counts … / It describes …". The motivating story goes in the text before or in that last sentence, not in the "if" clause.
- Property theorems for distributions all follow one template: "[Properties of the … distribution] For $X \sim \ldots$, 1. the PGF/MGF is …, 2. $\E(X) = …$, 3. $\Var(X) = …$, then CDF and tail probability if given." Proofs follow the same order. Paired results (e.g. the geometric and exponential memoryless properties) have the same statement and proof shape.
- Results stated without proof in the course are followed by "Not proved in this course." (or "These are not proved in this course.").
- Paired results mirror each other too: if the MGF has a "Moments from the MGF" theorem, the PGF gets a matching "Moments from the PGF" theorem rather than the same facts in running text.
- Paired definitions (discrete and continuous, pmf and pdf, …) mirror each other: the same structure and the same items (values taken, positivity, normalisation, how probabilities are computed, notation), so each can be read against the other.
- Use "is invertible" rather than "can be inverted"; prefer the shorter standard phrase.
- Keep a source's lists of examples when they show different kinds of case (for example discrete and continuous random experiments). Trim the surrounding commentary instead.
- Go straight to the general result when it is just as easy: don't work a specific case first ("ℙ(X = 8) = 5/36. In the same way, …").
- Leave out trivial cases that add nothing (e.g. the 0th central moment, which is always 1).
- A list inside a sentence can be set off with em dashes: "the most important ones --- the expectation, the variance and the moments --- and ends with …".
- Write "compare to", not "compare".
- Question lists in examples: at most two questions per kind (for example two probability questions and two statistics questions).
- Reactions to a result should be brief and accurate: "This is surprisingly small!", not "so not very big!".

### Naming and referring
- Name a result by what it is, not by its number: "The inclusion–exclusion principle extends to n events", not "Property 5 extends…".
- Don't attach names to individual list items (no "(complement rule)" after an item).
- Refer to an axiom or property by its name ("Axiom 3") rather than an equation number. Number an equation only if it is cited again.
- Write "the Kolmogorov axioms", not "the axioms (Kolmogorov, 1933)". Leave out dates and citations of historical origin.
- Don't read symbols out in words ("$A \cup B$ ($A$ union $B$)") outside the chapter that introduces them; set operations belong to the Foundations chapter on sets.
- Say "probability measure" for $\Prob$ (not "probability law" or "probability rule").
- Coins: "heads" and "tails" in lower case.

### Italics
- Theorem bodies are upright (set in the preamble).
- Italicise only the term a definition names (in a definition box, the term in the title: *event*, not *occurs*), terms defined in running text, and maths. No italics for emphasis.

### Lists
- Short-point lists (`itemize`, `enumerate`) have no punctuation between or after items. Lists of full sentences keep their full stops.
- A proof of an enumerated list of statements is itself a list: "Proof." on its own line, then `\item[1.]`, `\item[2.]`, …, with `\qedhere` at the end of the last item.

### Equations and spacing
- Long equations broken over lines use `align*`. The continuation line starts with `&\qquad +`, a little right of the `=`, not right-aligned as in `multline`.
- Inline fractions of probabilities get light spacing: `\Prob(A \cap B) \mkern2mu / \mkern2mu \Prob(B)`.
- Avoid paragraphs whose last line holds only a word or two: reword slightly. Check the built PDF for these before handing a chapter over.
- If a line inside a box has stretched word spacing (usually from long inline maths), put `\raggedright` at the start of that paragraph. Normal word spacing with a gap at the right edge is preferred to stretched spacing.

### Figures
- Place each figure with `[H]` directly after the box or paragraph that first mentions it.
- A figure must explain its idea on its own: label the elements (outcomes, weights, urns, positions) and say in the caption what to read off it. Redraw any figure from the notes that doesn't do this. Examples: Ch 25 Figs 25.3 and 25.7.
- Drop figures that only illustrate an analogy already clear in words (e.g. the triangles for the area measure).

### Tables
- Probability mass tables are a cross: values in the first row, probabilities in the second, a vertical rule after the label column and a horizontal rule between the rows, no top or bottom rules (`\begin{tabular}{c|ccc…}` … `\hline` …). Joint pmf tables use the same style. Pad them lightly: `\renewcommand{\arraystretch}{1.25}` inside the `center` environment.

### Boxes and headers
- "Builds on: nothing" in the chapter box (lower case, no full stop).
- Courses in the chapter box are listed in dependency order (X relies on Y, which relies on Z).
- Odd-page headers show the section title only, without its number.
- `solution` ends with ◀.

### Notation
- Expectation is written $\E(X)$, $\E(X^2)$, $\E(g(X))$, with $\E\bigl((X - \mu)^2\bigr)$ for powers of brackets. $\E[X]$ and $\E X$ are mentioned once, as alternatives, in the definition. Use $\E X$ only where brackets would clutter, e.g. $(\E X)^2$.
- Alternative symbols for a quantity go in its definition ("written $\Var(X)$ or $\sigma_X^2$"), not in the surrounding text.
- State facts as formulas where that is clearer: $\sigma_{aX+b} = \abs{a}\,\sigma_X$, not "the standard deviation of $aX + b$ is $\abs{a}$ times …".
- Every theorem box has a name in brackets, and states its result as a formula where possible ("$-1 \le \Corr(X, Y) \le 1$", not "always lies between −1 and 1").
- Definitions may be phrased "We define the *term* … by …", "The *term* of … is …" or "… has a *term* if …"; all are fine. Avoid "obvious"; say "follows in the same way".
- Keep theorem names short when the section makes the context clear ("Memoryless property", not "Memoryless property of the exponential distribution"). When a result reappears for another object, say where it was met before.
- A proof that ends in a formula gives it in a display: "…, and so [display]", not "Hence $\lim … = …$" inline.
- In a list of labelled items ("Binomial: the number of …"), capitalise the first word of each item.
- Don't link to specific theorems or definitions in chapter or section introductions (for now). Links to other chapters are fine there, but don't go out of the way to add them.
- Name results plainly: "Markov inequality", "Chebyshev inequality", "Generalised Markov inequality" (not "Markov's inequality, general form"). Give a colloquial name alongside the formal one where it is common, e.g. "Law of the unconscious statistician, LOTUS".
- Distributions: $\Bern(p)$ = Ber, $\Pois(\lambda)$ = Poi, $\Normal(\mu, \sigma^2)$ = $\mathcal{N}$ (may revert later), $\GammaDist(\alpha, \lambda)$ = Gamma (shape, rate; mention the scale form $\GammaDist(\alpha, \beta)$, $\beta = 1/\lambda$), $\BetaDist(\alpha, \beta)$ = Beta. Always use the macros.
- Positive and negative reals: $\R^{+}$ and $\R^{-}$. Power set: `\powerset(\Omega)`, not $2^\Omega$.
- Elementary probabilities: $p_i = \Prob(\set{a_i})$.

## Labels and cross-references
- Use `\cref{...}` only, never "Theorem~\ref{...}".
- Label prefixes are `ch:`, `sec:`, `def:`, `thm:`, `lem:`, `prop:`, `cor:`, `ex:`, `rem:`, `eq:` and `app:`, each followed by a kebab-case descriptive name. Examples: `thm:central-limit-theorem`, `def:cdf`.
- Labels must be globally unique and never renamed once used.
- Link back to an earlier result whenever a proof uses it.

## Notation
- Use the macros in `notation.tex` for everything they cover. Never type raw notation that has a macro.
- Notation is consistent across the whole book, whatever the source notes used. If a source uses different notation, convert it.
- New notation is proposed, not invented: add it to `NOTATION_REQUESTS.md`. It is decided in the hub chat and then added to `notation.tex` and the notation appendix.
- Fixed conventions so far:
  - The normal distribution is parametrised by variance, $\Normal(\mu, \sigma^2)$.
  - The exponential and gamma distributions use rates.
  - Vectors are bold column vectors.
  - Differentials are upright: `\dd x`.
