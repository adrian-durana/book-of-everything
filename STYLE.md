# Style Guide — Book of Everything (draft v0)

This is a living document. It will be revised after the pilot chapter, based on the author's edits.

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
- This is a personal reference book, so don't write as if the reader is seeing the material for the first time. Keep section introductions short. The exception is the harder third-year courses, where the expanded, first-encounter style of introduction is kept.
- Open each chapter with one short explanatory paragraph: what the topic is for, its main building blocks, and what the chapter covers. Model it on the Chapter 25 opening.
- Positive and negative reals: $\R^{+}$ and $\R^{-}$. Power set: `\powerset(\Omega)`, not $2^\Omega$.
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
- Theorem bodies are upright (preamble style). Italics only for a term being defined or mentioned, and for maths.
- Figures use `[H]` and sit in the source directly after the box or paragraph that first mentions them.
- A proof of an enumerated list of statements is itself a list: "Proof." on its own line, then `\item[1.]`, `\item[2.]`, …, with `\qedhere` at the end of the last item.
- `solution` ends with ◀.
- Coins: "heads" and "tails" in lower case.

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
