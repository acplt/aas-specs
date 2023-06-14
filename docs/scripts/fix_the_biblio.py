import re


def add_anchor_to_biblio(adoc_file):
    with open(adoc_file, 'r') as file:
        content = file.read()

    biblio_patterns = [r'\[(\d+)\]\s+([A-Z]+[^\[]+\[Online\])',
                       r'\[(\d+)\]\s+([\(German\)\s]*"[^"]+)"', r'\[(\d+)\]\s+(DIN|ISO|IEC|OPC"[^"]+")']

    matches = {}

    for pattern in biblio_patterns:
        matches.update(re.findall(pattern, content))

    for key in matches.keys():
        biblio_tag = f'[{key}]'
        biblio_tag_mod = f'[{key}]'
        biblio_text = f'{matches.get(key)}'

        # Move the caption to the beginning of the figure tag
        modified_figure_tag = f'[#bib_{key}]\n{biblio_tag_mod} {biblio_text}'
        old_figure_tag = f'{biblio_tag} {biblio_text}'

        content = content.replace(old_figure_tag, modified_figure_tag)

    with open(adoc_file, 'w') as file:
        file.write(content)

    return matches.keys()

def add_link_to_biblio(adoc_file, keys):
    with open(adoc_file, 'r') as file:
        content = file.read()

    for key in keys:
        in_link_patterns = r'(?<!\[#bib_{key}\]\n)\[{key}\]'
        in_link_patterns = in_link_patterns.format(key=key)
        content = re.sub(in_link_patterns, f'link:#bib_{key}[[{key}\]]' ,content)

    with open(adoc_file, 'w') as file:
        file.write(content)
