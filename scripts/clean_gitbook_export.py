from __future__ import annotations
import re
from pathlib import Path

DOCS_DIR = Path("docs")

# {% code ... %} ... {% endcode %}
RE_CODE_BLOCK = re.compile(r"{%\s*code[^%]*%}\s*(.*?)\s*{%\s*endcode\s*%}", re.DOTALL)

# {% embed url="..." %} Title {% endembed %}
RE_EMBED = re.compile(r'{%\s*embed\s+url="([^"]+)"\s*%}\s*(.*?)\s*{%\s*endembed\s*%}', re.DOTALL)

# Common GitBook hint blocks (optional, but you will likely have them)
RE_HINT = re.compile(r'{%\s*hint\s+style="([^"]+)"\s*%}\s*(.*?)\s*{%\s*endhint\s*%}', re.DOTALL)

def convert_embed(url: str, title: str) -> str:
    title = title.strip() or "Embedded content"
    url = url.strip()
    lower = url.lower()

    if lower.endswith((".mp4", ".webm", ".ogg")):
        return (
            f'\n\n<video controls style="max-width: 100%;" src="{url}"></video>\n\n'
            f'[{title}]({url})\n\n'
        )

    # Generic iframe fallback (works for many providers)
    return (
        f'\n\n<iframe src="{url}" style="width: 100%; height: 600px; border: 0;" '
        f'loading="lazy" allowfullscreen></iframe>\n\n'
        f'[{title}]({url})\n\n'
    )

def convert_hint(style: str, body: str) -> str:
    style = style.strip().lower()
    body = body.strip()

    # Map GitBook styles to Material admonitions
    mapping = {
        "info": "info",
        "warning": "warning",
        "danger": "danger",
        "success": "tip",
        "primary": "note",
    }
    admon = mapping.get(style, "note")
    # Indent body for admonition
    indented = "\n".join("    " + line for line in body.splitlines())
    return f"\n\n!!! {admon}\n{indented}\n\n"

def clean_text(s: str) -> str:
    # Replace the weird entity you’re seeing
    s = s.replace("&#xNAN;", "\n\n")

    # Convert GitBook code wrapper blocks -> just fenced blocks
    # If you prefer NOT to fence them, replace with r"\1" instead.
    s = RE_CODE_BLOCK.sub(lambda m: f"\n\n```\n{m.group(1).strip()}\n```\n\n", s)

    # Convert GitBook embed blocks
    s = RE_EMBED.sub(lambda m: convert_embed(m.group(1), m.group(2)), s)

    # Convert GitBook hint blocks (if present)
    s = RE_HINT.sub(lambda m: convert_hint(m.group(1), m.group(2)), s)

    # Convert "backslash used as line break" patterns into real newlines.
    # This targets sequences like: "identifier\ bytes32 ..." or "\ \ uint256 ..."
    s = re.sub(r"\\\s+", "\n", s)

    # Clean up excessive blank lines
    s = re.sub(r"\n{4,}", "\n\n\n", s)

    return s

def main() -> None:
    md_files = list(DOCS_DIR.rglob("*.md"))
    changed = 0

    for p in md_files:
        original = p.read_text(encoding="utf-8", errors="ignore")
        cleaned = clean_text(original)
        if cleaned != original:
            p.write_text(cleaned, encoding="utf-8")
            changed += 1

    print(f"Done. Updated {changed} file(s) out of {len(md_files)}.")

if __name__ == "__main__":
    main()
