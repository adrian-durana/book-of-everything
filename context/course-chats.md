# Course chats: setup prompts (transcription phase)

_Written 2026-11-22 by the hub chat._

Each course chat lives in the "Book of everything" project, so it can read the project docs. Start a new chat, paste the **common prompt** with the course line filled in, then upload the material. The hub chat (the original planning chat) keeps STAT2003 and STAT1301, owns the shared files and does all LaTeX drafting for now.

**Phase:** transcription only. Course chats check legibility, transcribe and build inventories. Nothing goes into the LaTeX book or the PDF yet, and they don't edit the repository.

---

## Common prompt

> This chat ingests **[COURSES]** for my "Book of Everything", a LaTeX reference book of my UQ undergraduate maths and statistics, organised by topic rather than by course. Before starting, read the project docs `claude/book-plan.md`, `claude/outline-and-course-map.md` and `claude/inventory-stat2003.md` (the format to follow), and in the repo `adrian-durana/book-of-everything` read `CLAUDE.md`, `STYLE.md`, `notation.tex` and `tools/chapters.py` (the authoritative chapter list).
>
> We are in the **transcription phase**. Nothing goes into the book or the PDF yet, and you don't edit the repository or create branches. Your job is to turn my course material into reliable, structured source content that a later chat can draft chapters from. I'll upload the material next: **[MATERIAL]**.
>
> 1. **Legibility check.** Go through every image in order. List each photo that is blurred, cut off, too dark or ambiguous, by file name and what can't be read, so I can retake it. Don't guess at unreadable content.
> 2. **Transcription.** Write `claude/notes-<course>.md` to the project, split into parts (`notes-<course>-1.md`, …) if it gets long. For every handwritten page, in order: a faithful transcription with maths in LaTeX (use the macros in `notation.tex` where they exist), keeping the notes' structure (Def., Thm., Proof, Ex., Rem.) and wording, plus a description of each figure detailed enough to redraw it in TikZ (axes, labels, points, shading, arrows). Typed notes and slides don't need retyping: give a section and page index, and transcribe only figures and anything that appears nowhere else. Mark `[illegible]` and `[possible error: …]` inline; correct nothing silently.
> 3. **Coverage inventory.** Write `claude/inventory-<course>.md` in the same format as `claude/inventory-stat2003.md`: every definition, theorem, proof, method, example, figure and piece of code, with its source reference (photo number or notes section), mapped to a target chapter and section from `tools/chapters.py`. Mark anything that overlaps a chapter already written (Part III, Chapters 25–31) or another course as ↔ merge rather than new. End with: suspected errors in the notes; notation the book doesn't have yet (proposed macro and reason); code in the notes (language and what it does).
>
> **Rules:** source material only (no additions, no filling gaps); no specific dates anywhere, only the semester I took the course if a source needs identifying. When you're done, give me a short summary: the retake list, page and item counts, overlaps with other courses, and any questions for the hub chat.

---

## Chats and course lines

Suggested order follows the ingestion order in `claude/outline-and-course-map.md` (statistics first). Replace **[COURSES]** and **[MATERIAL]** with the lines below.

| # | Chat name | [COURSES] | Main target chapters (see `tools/chapters.py`) |
|---|---|---|---|
| 1 | STAT3500 | STAT3500 Problems & Applications in Modern Statistics | GLMs, GEEs, Bayesian inference, time series, simulation |
| 2 | STAT3004 | STAT3004 Probability Models & Stochastic Processes | generating functions, limit theorems, Markov chains, Poisson processes and CTMCs, stochastic models, simulation |
| 3 | STAT2004 | STAT2004 Statistical Modelling & Analysis | sampling distributions, estimation, likelihood, confidence intervals, testing, categorical data, linear models, ANOVA, GLMs, Bayesian inference |
| 4 | STAT3001 | STAT3001 Mathematical Statistics | point estimation, sufficiency and the exponential family, likelihood theory, confidence intervals, testing, Bayesian inference, EM and the bootstrap |
| 5 | Statistical learning | STAT3006 Statistical Learning and STAT3008 Selected Topics in Statistical Learning | Part VI: learning framework, nearest neighbours and trees, linear methods, ensembles, kernels and RKHS, SVMs, Gaussian processes, learning theory, unsupervised learning, generative models |
| 6 | Deep learning | STAT3007 Deep Learning | Part VI: learning framework, neural networks, training, deep architectures, reinforcement learning |
| 7 | Analysis | MATH1071 Advanced Calculus & Linear Algebra I, MATH2400 Mathematical Analysis and MATH2401 Mathematical Analysis & Advanced Topics (MATH2401 is the primary source; MATH1071's linear algebra goes to the linear algebra chapters) | Part I: vectors and matrices, eigenvalues, real numbers to metric spaces, differential calculus in several variables |
| 8 | Multivariable calculus and linear algebra II | MATH1072 Advanced Multivariate Calculus & ODEs and MATH2001 Calculus & Linear Algebra II | Part I: eigenvalues, vector spaces, several-variable calculus, multiple integrals, vector calculus; Part II: first-order and higher-order ODEs, stability; numerical chapters touched by MATH1072 |
| 9 | Differential equations | MATH2010 Analysis of Ordinary Differential Equations and MATH2011 Analysis of Partial Differential Equations | Part II: ODEs, linear systems, Laplace transform, stability and phase plane, Fourier series, PDEs |
| 10 | Discrete mathematics | MATH1061 Discrete Mathematics | Part I: logic and proof, sets, induction and counting, graph theory, number theory; overlaps Chapter 25 (counting) |
| 11 | Numerical linear algebra and optimisation | MATH3204 Numerical Linear Algebra & Optimisation | Part V: matrix factorisations to non-smooth and stochastic optimisation |
| 12 | Operations research and optimisation theory | MATH3202 Operations Research & Mathematical Planning and MATH3404 Optimisation Theory | Part V: calculus of variations, optimal control, linear, integer and dynamic programming, metaheuristics |
| 13 | Scientific computing | COSC2500 Numerical Methods in Computational Science and MATH2504 Programming of Simulation, Analysis, & Learning Systems (MATH2504's Julia becomes Python later; just record it now) | Part V: floating point to numerical ODEs; Part VIII: Python, software practice, algorithms, symbolic computation, workflows |
| 14 | Applications (summary tier) | MATH3090 Financial Mathematics, ECON1010 Introductory Microeconomics and ECON1020 Introductory Macroeconomics | Part VII (summary chapters only) |

**[MATERIAL]** examples: "zips of photos of my handwritten notes (main reference), plus the typed lecture notes PDF"; "the lecture slides PDFs and my handwritten notes".

## After a course chat finishes
- Retake any photos on its list and upload them to the same chat.
- Tell the hub chat it's done. The hub reviews the inventory, processes any notation proposals, and drafts the chapters later, chapter by chapter, under `STYLE.md`.
