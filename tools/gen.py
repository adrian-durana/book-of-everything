import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from chapters import PARTS
root = sys.argv[1]
roman = "I II III IV V VI VII VIII".split()
lines = []; n = 0
for i, (ptitle, folder, lang, chs) in enumerate(PARTS):
    os.makedirs(f"{root}/chapters/{folder}", exist_ok=True)
    lines.append(f"% ---- Part {roman[i]}: {ptitle} (code: {lang}) " + "-"*20)
    lines.append(f"\\part{{{ptitle}}}")
    for slug, title, courses in chs:
        n += 1
        path = f"{root}/chapters/{folder}/{slug}.tex"
        if not os.path.exists(path) or "Not yet written" in open(path).read():
            with open(path, "w") as f:
                f.write(f"\\chapter{{{title}}}\\label{{ch:{slug}}}\n\n"
                        f"\\chapterinfo{{{courses}}}{{\\textit{{to be completed}}}}\n\n"
                        f"\\textit{{Not yet written.}}\n")
        lines.append(f"\\include{{chapters/{folder}/{slug}}}  % Ch {n}")
    lines.append("")
print("\n".join(lines))
print(f"% total chapters: {n}", file=sys.stderr)
