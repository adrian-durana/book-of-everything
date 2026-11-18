# Book of Everything

A personal reference book of undergraduate mathematics and statistics from The University of Queensland, organised by topic.

## Build
```
latexmk main.tex        # output: build/main.pdf
```
To work on a single chapter, uncomment `\includeonly{...}` in `main.tex`.

## Layout
- `main.tex`: master file. Lists the Parts and chapters.
- `preamble.tex`: packages, layout and environments.
- `notation.tex`: all notation macros. This is the single source of truth.
- `chapters/<part>/<chapter>.tex`: one file per chapter.
- `appendices/`: the notation appendix and other appendices.
- `figures/data/`: data files for plots (generated in R), read by pgfplots.
- `tools/`: `chapters.py` (the master chapter list) and `gen.py` (stub generator).
- `STYLE.md`: the writing and formatting style guide.
- `CLAUDE.md`: workflow rules for Claude sessions.
- `NOTATION_REQUESTS.md`: proposed notation awaiting a decision.

## Working on the book
- Edit `.tex` files directly and push to `main`. Claude pulls `main` at the start of each session; mention what you changed so it can be reflected in `STYLE.md`.
- Planning documents (plan, outline, progress log, per-course coverage inventories) live in the claude.ai Project "Book of everything", not in this repo.
