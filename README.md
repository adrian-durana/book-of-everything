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
- `STYLE.md`: the writing and formatting style guide.
- `CLAUDE.md`: workflow rules for Claude sessions.
- `NOTATION_REQUESTS.md`: proposed notation awaiting a decision.
