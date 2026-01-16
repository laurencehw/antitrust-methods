#!/usr/bin/env python3
"""
Embed pre-rendered figures into GitBook markdown files.
Inserts figure references after R code blocks.
"""

import re
import csv
from pathlib import Path
from collections import defaultdict


def load_manifest(manifest_path: Path) -> dict:
    """Load the figure manifest and group by chapter."""
    figures = defaultdict(list)
    with open(manifest_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chapter = row['chapter']
            figure = row['figure']
            figures[chapter].append(figure)
    return figures


def embed_figures_in_chapter(md_path: Path, figures: list, fig_dir: str = "../figures") -> int:
    """Embed figure references after R code blocks in a chapter."""

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all R code blocks
    # Pattern: ```r ... ```
    r_block_pattern = r'(```r\n.*?```)'

    blocks = list(re.finditer(r_block_pattern, content, re.DOTALL))

    if not blocks:
        print(f"  No R blocks found in {md_path.name}")
        return 0

    # Count blocks that likely produce figures (contain ggplot, plot, etc.)
    figure_blocks = []
    for block in blocks:
        block_content = block.group(1)
        if re.search(r'ggplot|plot\(|geom_|hist\(|barplot|boxplot', block_content, re.IGNORECASE):
            figure_blocks.append(block)

    if not figure_blocks:
        print(f"  No figure-producing blocks in {md_path.name}")
        return 0

    # Match figures to blocks (in order)
    insertions = []
    for i, (block, fig) in enumerate(zip(figure_blocks, figures)):
        end_pos = block.end()
        fig_ref = f'\n\n![Figure {i+1}]({fig_dir}/{fig})\n'
        insertions.append((end_pos, fig_ref))

    # Apply insertions in reverse order to preserve positions
    new_content = content
    for pos, fig_ref in reversed(insertions):
        new_content = new_content[:pos] + fig_ref + new_content[pos:]

    # Write back
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(insertions)


def main():
    base_dir = Path(__file__).parent.parent
    gitbook_dir = base_dir / 'gitbook'
    chapters_dir = gitbook_dir / 'chapters'
    manifest_path = gitbook_dir / 'figures' / 'manifest.csv'

    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}")
        return

    # Load manifest
    figures = load_manifest(manifest_path)
    print(f"Loaded manifest with {sum(len(v) for v in figures.values())} figures")

    total_embedded = 0

    for chapter, figs in figures.items():
        # Find the corresponding markdown file
        md_file = chapters_dir / f"{chapter}.md"

        if not md_file.exists():
            # Try without the number prefix
            print(f"  Warning: {md_file.name} not found")
            continue

        count = embed_figures_in_chapter(md_file, figs)
        if count > 0:
            print(f"  {chapter}: embedded {count} figure(s)")
            total_embedded += count

    print(f"\nTotal figures embedded: {total_embedded}")


if __name__ == '__main__':
    main()
