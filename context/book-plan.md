# Book of Everything — Plan and Decisions

_Last updated: 2026-11-22_

## Purpose
A reference book of all undergraduate statistics and mathematics knowledge (UQ). It is for relearning quickly: more formal than lecture notes, less formal than a textbook. Each chapter is self-contained, plus whatever earlier chapters it builds on. Expected size is 1,000–2,000 pages.

## Content rules (current phase: course ingestion)
- **Source material only.** Mistakes are corrected (and logged in `claude/progress.md`), but nothing new is added. Results a source states without proof are stated without proof.
- **One motivating example per section or subsection** (two at most).
- **Writing style:** follow the style and wording of the **handwritten notes**. Use the typed notes' style where they explain the content better. For courses without handwritten notes, use the style of the STAT2003 and STAT1301 typed notes.
- **Every image in the notes is redrawn in TikZ/pgfplots.**
- **Section and subsection titles are renamed and rearranged** as new course material is merged in.
- **No specific dates**; identify a source only by the semester the course was taken.
- **Detailed writing and layout rules:** `STYLE.md` in the repo ("Writing and layout preferences").
- **Linking phase (after every course is ingested):** add cross-references, motivation and gap-filling.

## Decisions
- **Organisation:** by topic, not by course. 8 Parts and 94 chapters (see `claude/outline-and-course-map.md`, which predates the R chapter; `tools/chapters.py` in the repo is authoritative). Course codes are recorded in each chapter's `\chapterinfo` box.
- **STAT1301 R tutorial** → Ch 90 "Programming in R" in Part VIII (may move later).
- **Depth:** the depth of the original courses. Nice-to-have tier (MATH3090, ECON1010/1020) gets summary chapters.
- **Format:** LaTeX. One master project, one file per chapter, global labels for cross-references.
- **Box style (2026-11-20):** keep option A (left bar with tint).
- **Notation:** one consistent set across the book, kept in `notation.tex`. New notation goes through `NOTATION_REQUESTS.md`. Bold vectors and matrices use `\bm` (2026-11-20).
- **Code:** R for Parts III–IV (Probability, Statistics); Python everywhere else, except the R chapter.
- **Computing material:** MATH2504 (converted from Julia), COSC2500 implementations and the STAT1301 R tutorial form Part VIII, Scientific Computing.
- **Courses:** MATH2400 and MATH2401 were both taken; MATH2401 is the primary source. MATH2100 = MATH2010 (ODEs) + MATH2011 (PDEs), and both were taken.
- **Workflow:** course chats transcribe and inventory each course (transcription phase) → hub drafts or merges chapters → user review → linking pass → index.

## Chat setup
- **Hub chat** (the original planning chat): finishes STAT2003 and STAT1301, owns structure, style, notation and the shared files, and does all LaTeX drafting for now.
- **Course chats** (14, one per course or group of related courses): transcription phase only. Each checks image legibility, writes `claude/notes-<course>.md` and `claude/inventory-<course>.md`, and doesn't edit the repository. Prompts and groupings: `claude/course-chats.md`.

## Editing workflow for the user
- Edit the `.tex` files directly and push to `main`. Claude is **not** notified automatically.
- At the start of every session, Claude pulls `main` before editing. Say what you changed so it can be folded into `STYLE.md`.
- Avoid editing a chapter while a chat is working on that same chapter.

## Where things live
- **LaTeX source:** GitHub, `adrian-durana/book-of-everything`. See its `README.md`.
- **Project docs:** this plan, `claude/outline-and-course-map.md`, `claude/progress.md`, `claude/course-chats.md`, coverage inventories (`claude/inventory-<course>.md`) and transcriptions (`claude/notes-<course>.md`).

## Open questions
- Which generated textbook to use as a style reference (user to decide).
