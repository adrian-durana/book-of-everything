# Book of Everything — instructions for Claude sessions

This is a LaTeX reference book covering the author's undergraduate mathematics and statistics at UQ. It is organised by topic, not by course. The author edits all text directly.

## Before writing anything
0. **Content rule:** use only material from the course sources (corrections allowed, additions not). See the "Content rule" section of `STYLE.md`.
1. Read `STYLE.md`. It covers voice, environments, labels and notation rules. Its "Writing and layout preferences" section is the author's review feedback; follow it for every chapter, and check the built PDF against it (short last lines, figure placement, italics) before handing a chapter over.
2. Read `notation.tex` and use its macros. Never invent notation. If you need something new, add it to `NOTATION_REQUESTS.md` with a proposed macro and a reason.
3. Read the project docs (`claude/book-plan.md`, the course map and the coverage inventories) for scope and chapter assignments.

## File ownership
- **Shared files:** `main.tex`, `preamble.tex`, `notation.tex` and `appendices/notation.tex`. These are edited only in the hub chat. A course or chapter chat that needs a new chapter listed in `main.tex` should say so in its final message instead of editing the file.
- Course or chapter chats work on their own branch (`course/<code>`, e.g. `course/stat3001`) and only touch their own chapter files under `chapters/part-<n>-<name>/`.

## Notation requests
- Course chats add proposed notation to `NOTATION_REQUESTS.md` on their own branch.
- The hub chat processes the requests whenever it merges a course branch: it decides on each one, updates `notation.tex` and the notation appendix, and clears the entry.

## Ingesting a course
1. Build a coverage inventory. List every definition, theorem, proof, method and example in the source material, each mapped to a target chapter and section. Save it to the project as `claude/inventory-<course>.md`.
2. Draft new chapters, or extend existing ones. Merge into existing material; never duplicate a topic that already has a home.
3. Add the course code to `\chapterinfo` in every chapter the course contributes to.
4. Compile with `latexmk main.tex`. The output goes to `build/`. There should be no errors and no undefined references.

## Build
`latexmk main.tex` writes to `build/main.pdf`. If a build fails after adding a new folder, run `latexmk -g main.tex`.
