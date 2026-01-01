#!/usr/bin/env python3
"""
Convert Quarto (.qmd) files to GitBook-compatible Markdown (.md)

This script:
1. Converts Quarto callouts to GitBook hints
2. Converts R code chunks to fenced code blocks
3. Handles YAML front matter
4. Fixes math delimiters for KaTeX
5. Processes citations
"""

import re
import os
from pathlib import Path
import yaml

def convert_callouts(content: str) -> str:
    """Convert Quarto callouts to GitBook hints."""
    # Pattern for Quarto callouts: ::: {.callout-TYPE title="TITLE"}
    callout_pattern = r'::: \{\.callout-(\w+)(?: title="([^"]*)")?\}\n(.*?)\n:::'

    def replace_callout(match):
        callout_type = match.group(1)
        title = match.group(2) or callout_type.capitalize()
        content = match.group(3).strip()

        # Map Quarto types to GitBook hint styles
        type_map = {
            'note': 'info',
            'tip': 'success',
            'warning': 'warning',
            'caution': 'warning',
            'important': 'danger'
        }
        hint_type = type_map.get(callout_type, 'info')

        return f'''{{% hint style="{hint_type}" %}}
**{title}**

{content}
{{% endhint %}}'''

    return re.sub(callout_pattern, replace_callout, content, flags=re.DOTALL)


def convert_r_chunks(content: str) -> str:
    """Convert Quarto R code chunks to fenced code blocks."""
    # Pattern for R chunks with options
    chunk_pattern = r'```\{r\}\n(#\|[^\n]*\n)*'

    def replace_chunk_start(match):
        return '```r\n'

    # First pass: simple chunk starts
    content = re.sub(r'```\{r\}', '```r', content)

    # Remove #| chunk options (Quarto-specific)
    content = re.sub(r'^#\| .*$\n', '', content, flags=re.MULTILINE)

    return content


def fix_math_delimiters(content: str) -> str:
    """Ensure display math uses $$ on own lines for KaTeX."""
    # Find inline $$ that should be display math
    # Pattern: $$ not at start of line
    lines = content.split('\n')
    result = []

    for line in lines:
        # If line contains $$ but not at start/end, it might need fixing
        if '$$' in line and not line.strip().startswith('$$') and not line.strip().endswith('$$'):
            # Split display math to own lines
            line = re.sub(r'\$\$([^$]+)\$\$', r'\n$$\n\1\n$$\n', line)
        result.append(line)

    return '\n'.join(result)


def convert_yaml_frontmatter(content: str) -> tuple:
    """Extract and convert YAML front matter."""
    yaml_pattern = r'^---\n(.*?)\n---\n'
    match = re.match(yaml_pattern, content, re.DOTALL)

    if match:
        yaml_content = match.group(1)
        try:
            data = yaml.safe_load(yaml_content)
            title = data.get('title', '')
            # Remove YAML from content
            content = content[match.end():]
            return title, content
        except:
            pass

    return '', content


def convert_chapter(input_path: Path, output_path: Path) -> None:
    """Convert a single chapter from .qmd to .md."""
    print(f"Converting: {input_path.name}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from first heading if present
    title_match = re.match(r'^# (.+?)(?:\s*\{[^}]*\})?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else input_path.stem

    # Apply conversions
    content = convert_r_chunks(content)
    content = convert_callouts(content)
    content = fix_math_delimiters(content)

    # Remove Quarto-specific div classes (but keep content)
    content = re.sub(r'^::: \{[^}]*\}\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^:::\s*$', '', content, flags=re.MULTILINE)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  -> {output_path.name}")
    return title


def create_summary(chapters: list, output_dir: Path) -> None:
    """Create GitBook SUMMARY.md file."""
    summary = "# Summary\n\n"
    summary += "* [Introduction](README.md)\n\n"
    summary += "## Chapters\n\n"

    for num, (filename, title) in enumerate(chapters):
        summary += f"* [{title}](chapters/{filename})\n"

    with open(output_dir / 'SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"Created SUMMARY.md")


def create_book_json(output_dir: Path) -> None:
    """Create GitBook book.json configuration."""
    config = {
        "title": "Antitrust Methods: Research and Practice",
        "author": "Laurence Wilse-Samson",
        "description": "A practitioner-focused text on antitrust research methods",
        "language": "en",
        "gitbook": ">=3.0.0",
        "plugins": [
            "katex",
            "hints"
        ],
        "pluginsConfig": {
            "katex": {
                "delimiters": [
                    {"left": "$$", "right": "$$", "display": True},
                    {"left": "$", "right": "$", "display": False}
                ]
            }
        }
    }

    import json
    with open(output_dir / 'book.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    print("Created book.json")


def main():
    """Main conversion function."""
    base_dir = Path(__file__).parent.parent
    chapters_dir = base_dir / 'chapters'
    output_dir = base_dir / 'gitbook'
    output_chapters = output_dir / 'chapters'

    # Ensure output directories exist
    output_chapters.mkdir(parents=True, exist_ok=True)

    # Get all .qmd files
    qmd_files = sorted(chapters_dir.glob('*.qmd'))

    # Also check for index.qmd in root
    index_qmd = base_dir / 'index.qmd'

    chapters = []

    # Convert index to README
    if index_qmd.exists():
        title = convert_chapter(index_qmd, output_dir / 'README.md')
        print("Converted index.qmd to README.md")

    # Convert each chapter
    for qmd_file in qmd_files:
        output_file = output_chapters / qmd_file.with_suffix('.md').name
        title = convert_chapter(qmd_file, output_file)
        chapters.append((output_file.name, title))

    # Create GitBook configuration files
    create_summary(chapters, output_dir)
    create_book_json(output_dir)

    print(f"\nConversion complete! {len(chapters)} chapters converted.")
    print(f"Output directory: {output_dir}")


if __name__ == '__main__':
    main()
