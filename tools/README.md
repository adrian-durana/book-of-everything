# tools

- `chapters.py`: the master chapter list (Part, folder, code language, then a slug, title and courses for each chapter). This is the single source of truth for the book's structure.
- `gen.py`: creates stub files for new chapters (and refreshes stubs that are still unwritten), then prints the `\part`/`\include` block for `main.tex`.

```
python3 tools/gen.py . > /tmp/parts.tex   # then paste into main.tex between the frontmatter and \appendix
```
Hub chat only: the chapter structure is a shared resource.
