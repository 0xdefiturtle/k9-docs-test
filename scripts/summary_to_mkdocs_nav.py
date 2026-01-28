import re
from pathlib import Path

summary_path = Path("docs/SUMMARY.md")
text = summary_path.read_text(encoding="utf-8").splitlines()

link_re = re.compile(r'^\s*[*+-]\s+\[([^\]]+)\]\(([^)]+)\)\s*$')

items = []
for line in text:
    m = link_re.match(line)
    if not m:
        continue
    title, href = m.group(1).strip(), m.group(2).strip()
    # Normalize GitBook -> MkDocs home page rename
    href = href.replace("README.md", "index.md")
    # Strip leading ./ if present
    href = href[2:] if href.startswith("./") else href
    # Determine nesting by indentation (2 spaces per level is common)
    indent = len(line) - len(line.lstrip(" "))
    level = indent // 2
    items.append((level, title, href))

# Build nested nav structure
nav_stack = [[]]  # stack of lists
level_stack = [0]

def add_item(level, title, href):
    # Ensure stack matches level
    while level < level_stack[-1]:
        nav_stack.pop()
        level_stack.pop()
    while level > level_stack[-1]:
        # Create a new nested list under the last dict item
        parent = nav_stack[-1][-1]
        if not isinstance(parent, dict):
            raise RuntimeError("Unexpected structure while nesting")
        (k, v), = parent.items()
        if isinstance(v, str):
            parent[k] = []
        nav_stack.append(parent[k])
        level_stack.append(level_stack[-1] + 1)

    nav_stack[-1].append({title: href})

for level, title, href in items:
    add_item(level, title, href)

def yaml_dump(obj, indent=0):
    sp = "  " * indent
    lines = []
    if isinstance(obj, list):
        for item in obj:
            # item is dict with single key
            (k, v), = item.items()
            if isinstance(v, str):
                lines.append(f"{sp}- {k}: {v}")
            else:
                lines.append(f"{sp}- {k}:")
                lines.extend(yaml_dump(v, indent + 1))
    return lines

out = ["nav:"] + yaml_dump(nav_stack[0], 1)
print("\n".join(out))
