#!/usr/bin/env python3
"""Static citation guard for the Quarto book.

Fails (exit 1) if either:
  1. any @key cited in a .qmd has no matching entry in references/references.bib
     (this is what makes a citation render as raw "@key"), or
  2. _quarto.yml points `csl:` at a remote URL, whose fetch can fail at render
     time and make citeproc emit raw @keys for *every* citation.

Runs with the standard library only -- no Quarto, R, or network needed -- so it
is a fast, deterministic backstop against the citation regressions fixed in this
branch. Run from the repository root.
"""
import glob
import os
import re
import sys

BIB = "references/references.bib"
QUARTO = "_quarto.yml"
# Quarto cross-reference prefixes that look like @keys but are not citations.
XREF_PREFIXES = ("sec-", "fig-", "tbl-", "eq-", "lst-", "thm-", "def-")
KEY_RE = re.compile(r"@([A-Za-z][\w:.\-+]*)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def defined_keys() -> set:
    bib = open(BIB, encoding="utf-8").read()
    return set(re.findall(r"@\w+\{([^,\s]+)\s*,", bib))


def cited_keys() -> dict:
    """Map each cited key -> set of files citing it (code fences stripped)."""
    out: dict = {}
    for f in sorted(glob.glob("chapters/*.qmd") + glob.glob("*.qmd")):
        text = FENCE_RE.sub("", open(f, encoding="utf-8").read())
        for m in KEY_RE.finditer(text):
            key = m.group(1).rstrip(".,;:")
            if key.startswith(XREF_PREFIXES):
                continue
            out.setdefault(key, set()).add(os.path.basename(f))
    return out


def remote_csl() -> str | None:
    if not os.path.exists(QUARTO):
        return None
    m = re.search(r"^\s*csl:\s*(\S+)", open(QUARTO, encoding="utf-8").read(), re.M)
    if m and m.group(1).startswith(("http://", "https://")):
        return m.group(1)
    return None


def main() -> int:
    defined = defined_keys()
    cited = cited_keys()
    unresolved = {k: v for k, v in cited.items() if k not in defined}
    csl_url = remote_csl()

    ok = True
    if unresolved:
        ok = False
        print("✗ Unresolved citation keys (cited in text, absent from references.bib):")
        for key in sorted(unresolved):
            hint = "  [looks like a '---' em-dash parse bug]" if "---" in key else ""
            print(f"    @{key}{hint}  in {', '.join(sorted(unresolved[key]))}")
    if csl_url:
        ok = False
        print(f"✗ _quarto.yml uses a remote csl: {csl_url}")
        print("  Vendor the CSL locally and reference it by relative path so a failed")
        print("  fetch cannot make citeproc render every citation as raw text.")

    if ok:
        print(f"✓ All {len(cited)} cited keys resolve against {len(defined)} "
              "bib entries; csl is local.")
        return 0
    print("\nFix the above, then re-run: python3 program/scripts/check_citations.py")
    return 1


if __name__ == "__main__":
    sys.exit(main())
