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

# Citation key to readable format mapping
# Built from references.bib - maps @key to (Author, Year) format
CITATION_MAP = {
    # Core academic references
    'nevo_2000': '(Nevo, 2000)',
    'berry_levinsohn_pakes_1995': '(Berry, Levinsohn & Pakes, 1995)',
    'rochet_tirole_2003': '(Rochet & Tirole, 2003)',
    'armstrong_2006': '(Armstrong, 2006)',
    'evans_schmalensee_2007': '(Evans & Schmalensee, 2007)',
    'hagiu_wright_2015': '(Hagiu & Wright, 2015)',
    'parker_van_alstyne_2005': '(Parker & Van Alstyne, 2005)',
    'katz_shapiro_2003': '(Katz & Shapiro, 2003)',
    'farrell_shapiro_2010': '(Farrell & Shapiro, 2010)',
    'schmalensee_2009': '(Schmalensee, 2009)',
    'davis_garces_2010': '(Davis & Garcés, 2010)',
    'harrington_2008': '(Harrington, 2008)',
    'porter_zona_1993': '(Porter & Zona, 1993)',
    'abrantes_mello_2010': '(Abrantes-Mello, 2010)',
    'motta_2004': '(Motta, 2004)',
    'tirole_1988': '(Tirole, 1988)',
    'whinston_2006': '(Whinston, 2006)',
    'shapiro_2001': '(Shapiro, 2001)',
    'ordover_saloner_salop_1990': '(Ordover, Saloner & Salop, 1990)',
    'salop_scheffman_1983': '(Salop & Scheffman, 1983)',
    'salop_2018': '(Salop, 2018)',
    'areeda_turner_1975': '(Areeda & Turner, 1975)',
    'edlin_hemphill_2012': '(Edlin & Hemphill, 2012)',
    'lemley_shapiro_2007': '(Lemley & Shapiro, 2007)',
    'hemphill_sampat_2012': '(Hemphill & Sampat, 2012)',
    'jaffe_weyl_2013': '(Jaffe & Weyl, 2013)',
    'cunningham_ederer_ma_2021': '(Cunningham, Ederer & Ma, 2021)',
    'scott_morton_2000': '(Scott Morton, 2000)',
    'miller_weinberg_2017': '(Miller & Weinberg, 2017)',
    'ashenfelter_hosken_2010': '(Ashenfelter & Hosken, 2010)',
    'weinberg_hosken_2013': '(Weinberg & Hosken, 2013)',
    'farrell_hayes_shapiro_sullivan_2007': '(Farrell et al., 2007)',
    'baker_rubinfeld_1999': '(Baker & Rubinfeld, 1999)',
    'dickey_rubinfeld_2014': '(Dickey & Rubinfeld, 2014)',
    'rubinfeld_2010': '(Rubinfeld, 2010)',

    # Econometrics and methods
    'angrist_pischke_2009': '(Angrist & Pischke, 2009)',
    'abadie_diamond_hainmueller_2010': '(Abadie, Diamond & Hainmueller, 2010)',
    'athey_imbens_2017': '(Athey & Imbens, 2017)',
    'callaway_santanna_2021': '(Callaway & Sant\'Anna, 2021)',
    'conley_decarolis_2016': '(Conley & Decarolis, 2016)',
    'manning_2003': '(Manning, 2003)',
    'fjc_reference_manual_2011': '(FJC Reference Manual, 2011)',
    'huntington_klein_2021': '(Huntington-Klein, 2021)',
    'alves_2022': '(Alves, 2022)',
    'cunningham_2021': '(Cunningham, 2021)',

    # Labor economics
    'azar_marinescu_steinbaum_2020': '(Azar, Marinescu & Steinbaum, 2020)',
    'ashenfelter_farber_ransom_2010': '(Ashenfelter, Farber & Ransom, 2010)',
    'benmelech_bergman_kim_2020': '(Benmelech, Bergman & Kim, 2020)',
    'krueger_ashenfelter_2018': '(Krueger & Ashenfelter, 2018)',
    'naidu_posner_weyl_2018': '(Naidu, Posner & Weyl, 2018)',
    'dube_lester_reich_2016': '(Dube, Lester & Reich, 2016)',

    # Additional methods
    'angrist_pischke_2015': '(Angrist & Pischke, 2015)',
    'goodman_bacon_2021': '(Goodman-Bacon, 2021)',
    'sun_abraham_2021': '(Sun & Abraham, 2021)',

    # US Guidelines and cases
    'doj_ftc_hmg_2010': '(DOJ/FTC Horizontal Merger Guidelines, 2010)',
    'doj_ftc_hmg_2023': '(DOJ/FTC Merger Guidelines, 2023)',
    'doj_ftc_vmg_2020': '(DOJ/FTC Vertical Merger Guidelines, 2020)',
    'doj_hr_guidance_2016': '(DOJ/FTC HR Guidance, 2016)',
    'us_microsoft_2001': '(*United States v. Microsoft*, 2001)',
    'us_actavis_2013': '(*FTC v. Actavis*, 2013)',
    'us_brooke_group_1993': '(*Brooke Group v. Brown & Williamson*, 1993)',
    'us_grinnell_1966': '(*United States v. Grinnell*, 1966)',
    'us_linkline_2009': '(*Pacific Bell v. linkLine*, 2009)',
    'us_tampa_electric_1961': '(*Tampa Electric v. Nashville Coal*, 1961)',
    'us_apple_ebooks_2013': '(*United States v. Apple Inc.*, 2013)',
    'us_amex_2018': '(*Ohio v. American Express*, 2018)',
    'us_epic_apple_2021': '(*Epic Games v. Apple*, 2021)',
    'us_google_search_2023': '(*United States v. Google (Search)*, 2023)',
    'us_google_adtech_2023': '(*United States v. Google (Ad Tech)*, 2023)',
    'us_alcoa_1945': '(*United States v. Alcoa*, 1945)',
    'us_brown_shoe_1962': '(*Brown Shoe v. United States*, 1962)',
    'us_trinko_2004': '(*Verizon v. Trinko*, 2004)',
    'us_qualcomm_2020': '(*FTC v. Qualcomm*, 2020)',
    'us_jindal_2021': '(*United States v. Jindal*, 2021)',
    'us_davita_2022': '(*United States v. DaVita*, 2022)',
    'us_connell_1975': '(*Connell Construction v. Plumbers Local 100*, 1975)',
    'ftc_noncompete_2023': '(FTC Non-Compete Clause Rule, 2023)',

    # EU Guidelines and cases
    'ec_hmg_2004': '(EC Horizontal Merger Guidelines, 2004)',
    'ec_market_definition_2024': '(EC Market Definition Notice, 2024)',
    'eu_united_brands_1978': '(*United Brands*, 1978)',
    'eu_akzo_1991': '(*AKZO*, 1991)',
    'eu_bronner_1998': '(*Bronner*, 1998)',
    'eu_ims_2004': '(*IMS Health*, 2004)',
    'eu_intel_2017': '(*Intel*, 2017)',
    'eu_post_danmark_2012': '(*Post Danmark*, 2012)',
    'eu_deutsche_telekom_2010': '(*Deutsche Telekom*, 2010)',
    'eu_telefonica_2014': '(*Telefónica*, 2014)',
    'eu_google_android_2018': '(*Google Android*, 2018)',
    'eu_google_shopping_2017': '(*Google Shopping*, 2017)',
    'eu_huawei_zte_2015': '(*Huawei v. ZTE*, 2015)',
    'eu_dma_2022': '(Digital Markets Act, 2022)',
    'ec_article102_guidance_2009': '(EC Article 102 Guidance, 2009)',
    'ec_market_definition_1997': '(EC Market Definition Notice, 1997)',

    # UK
    'cma_merger_assessment_2021': '(CMA Merger Assessment Guidelines, 2021)',
    'cma_market_definition_2018': '(CMA Market Definition, 2018)',

    # South Africa
    'sa_competition_act_1998': '(SA Competition Act, 1998)',
    'sa_oipmi_2023': '(SA OIPMI Final Report, 2023)',
    'sa_telkom_2013': '(*Competition Commission v. Telkom*, 2013)',
    'sa_media24_2012': '(*Competition Commission v. Media24*, 2012)',
    'sa_sasol_2014': '(*Competition Commission v. Sasol*, 2014)',

    # OECD
    'oecd_cartel_screens_2013': '(OECD Cartel Screens, 2013)',
    'oecd_leniency_2015': '(OECD Leniency Programmes, 2015)',
}


# Quarto @sec- cross-reference to GitBook link mapping
CROSSREF_MAP = {
    'sec-orientation': ('Chapter 1', 'chapters/01-orientation.md'),
    'sec-research-design': ('Chapter 2', 'chapters/02-research-design.md'),
    'sec-market-definition': ('Chapter 3', 'chapters/03-market-definition.md'),
    'sec-io-toolkit': ('Chapter 4', 'chapters/04-io-toolkit.md'),
    'sec-cartels': ('Chapter 5', 'chapters/05-cartels.md'),
    'sec-mergers': ('Chapter 6', 'chapters/06-mergers.md'),
    'sec-monopolization': ('Chapter 7', 'chapters/07-monopolization.md'),
    'sec-regulation-remedies': ('Chapter 8', 'chapters/08-regulation-remedies.md'),
    'sec-digital-markets': ('Chapter 9', 'chapters/09-digital-markets.md'),
    'sec-labor-markets': ('Chapter 10', 'chapters/10-labor-markets.md'),
    'sec-innovation-ip': ('Chapter 11', 'chapters/11-innovation-ip.md'),
    'sec-litigation-practice': ('Chapter 12', 'chapters/12-litigation-practice.md'),
    'sec-empirical-appendix': ('Empirical Appendix', 'chapters/13-empirical-appendix.md'),
}


def convert_crossrefs(content: str) -> str:
    """Convert Quarto @sec- cross-references to GitBook markdown links."""
    def replace_crossref(match):
        key = match.group(1)
        if key in CROSSREF_MAP:
            label, path = CROSSREF_MAP[key]
            return f'[{label}]({path})'
        return match.group(0)

    return re.sub(r'@(sec-[a-zA-Z0-9-]+)', replace_crossref, content)


def convert_citations(content: str) -> str:
    """Convert Pandoc-style citations to readable text."""

    def replace_citation(match):
        """Replace a single citation or group of citations."""
        citation_text = match.group(1)
        # Handle multiple citations separated by semicolons
        keys = [k.strip().lstrip('@') for k in citation_text.split(';')]

        readable_parts = []
        for key in keys:
            if key in CITATION_MAP:
                readable_parts.append(CITATION_MAP[key])
            else:
                # Fallback: convert key to readable format
                # e.g., author_year_2020 -> (Author Year, 2020)
                parts = key.split('_')
                if parts and parts[-1].isdigit():
                    year = parts[-1]
                    authors = ' '.join(p.capitalize() for p in parts[:-1])
                    readable_parts.append(f'({authors}, {year})')
                else:
                    readable_parts.append(f'({key})')

        return '; '.join(readable_parts)

    # Pattern for bracketed citations: [@key] or [@key1; @key2]
    content = re.sub(r'\[(@[^\]]+)\]', replace_citation, content)

    # Pattern for inline citations: @key (not in brackets)
    def replace_inline_citation(match):
        key = match.group(1)
        if key in CITATION_MAP:
            return CITATION_MAP[key]
        else:
            parts = key.split('_')
            if parts and parts[-1].isdigit():
                year = parts[-1]
                authors = ' '.join(p.capitalize() for p in parts[:-1])
                return f'({authors}, {year})'
            return f'({key})'

    # Match inline @key not already inside a [@...] bracket (which was handled above).
    # Don't restrict on trailing ] — the bracketed pass already consumed [@key] patterns,
    # and mixed brackets like [text, @key] need the @key converted too.
    content = re.sub(r'(?<!\[)@([a-zA-Z][a-zA-Z0-9_]+)', replace_inline_citation, content)

    return content


def convert_callouts(content: str) -> str:
    """Convert Quarto callouts to GitBook hints."""
    # Match :::{.callout-TYPE ...attrs...} tolerating optional space and 3+ colons
    # (case boxes use ":::{" with no space) and any attribute order
    # (e.g. {.callout-tip collapse="true" title="Answer"}).
    callout_pattern = r':::+\s*\{\.callout-(\w+)([^}]*)\}\n(.*?)\n:::+'

    def replace_callout(match):
        callout_type = match.group(1)
        attrs = match.group(2) or ''
        title_match = re.search(r'title="([^"]*)"', attrs)
        title = title_match.group(1) if title_match else callout_type.capitalize()
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


def convert_r_chunks(content: str, available_images: set = None) -> str:
    """Convert Quarto R code chunks to fenced code blocks.

    Extracts chunk labels and fig-caps from #| options before stripping them.
    For chunks that produce figures (matching an image in available_images),
    inserts a markdown image reference. For echo: false chunks, the code block
    is removed entirely and only the figure is shown.
    """
    if available_images is None:
        available_images = set()

    # Match full R code chunks: ```{r} ... ```
    chunk_pattern = re.compile(
        r'```\{r\}\n((?:#\|[^\n]*\n)*)' +  # opening + chunk options
        r'(.*?)' +                            # code body
        r'\n```',                              # closing
        re.DOTALL
    )

    def replace_chunk(match):
        options_block = match.group(1)
        code_body = match.group(2)

        # Parse chunk options
        label = None
        fig_cap = None
        echo = True
        eval_opt = True
        for line in options_block.strip().split('\n'):
            line = line.strip()
            if line.startswith('#| label:'):
                label = line.split(':', 1)[1].strip().strip('"').strip("'")
            elif line.startswith('#| fig-cap:'):
                fig_cap = line.split(':', 1)[1].strip().strip('"').strip("'")
            elif line.startswith('#| echo:'):
                val = line.split(':', 1)[1].strip().lower()
                echo = val not in ('false', 'no')
            elif line.startswith('#| eval:'):
                val = line.split(':', 1)[1].strip().lower()
                eval_opt = val not in ('false', 'no')

        # Check if this chunk has a rendered figure
        image_name = f"{label}-1.png" if label else None
        has_figure = image_name and image_name in available_images

        parts = []

        # Include code block unless echo: false
        if echo:
            parts.append(f"```r\n{code_body}\n```")

        # Insert figure reference if available
        if has_figure:
            caption = fig_cap or ''
            parts.append(f'\n![{caption}](../images/{image_name})\n')

        return '\n'.join(parts) if parts else ''

    content = chunk_pattern.sub(replace_chunk, content)

    # Clean up any remaining #| lines (from chunks that didn't match the pattern)
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


def convert_chapter(input_path: Path, output_path: Path,
                    available_images: set = None) -> None:
    """Convert a single chapter from .qmd to .md."""
    print(f"Converting: {input_path.name}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from first heading if present
    title_match = re.match(r'^# (.+?)(?:\s*\{[^}]*\})?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else input_path.stem

    # Apply conversions (crossrefs before citations so @sec- doesn't get mangled)
    content = convert_r_chunks(content, available_images=available_images)
    content = convert_callouts(content)
    content = convert_crossrefs(content)
    content = convert_citations(content)
    content = fix_math_delimiters(content)

    # Remove any remaining Quarto fenced-div markers (3+ colons, optional space)
    content = re.sub(r'^:::+\s*\{[^}]*\}\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^:::+\s*$', '', content, flags=re.MULTILINE)

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
    images_dir = output_dir / 'images'

    # Ensure output directories exist
    output_chapters.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    # Collect available rendered images
    available_images = {p.name for p in images_dir.glob('*.png')}
    print(f"Found {len(available_images)} rendered images in gitbook/images/")

    # Get all .qmd files
    qmd_files = sorted(chapters_dir.glob('*.qmd'))

    # Also check for index.qmd in root
    index_qmd = base_dir / 'index.qmd'

    chapters = []

    # Convert index to README
    if index_qmd.exists():
        title = convert_chapter(index_qmd, output_dir / 'README.md',
                                available_images=available_images)
        print("Converted index.qmd to README.md")

    # Convert each chapter
    for qmd_file in qmd_files:
        output_file = output_chapters / qmd_file.with_suffix('.md').name
        title = convert_chapter(qmd_file, output_file,
                                available_images=available_images)
        chapters.append((output_file.name, title))

    # Create GitBook configuration files
    create_summary(chapters, output_dir)
    create_book_json(output_dir)

    print(f"\nConversion complete! {len(chapters)} chapters converted.")
    print(f"Output directory: {output_dir}")


if __name__ == '__main__':
    main()
