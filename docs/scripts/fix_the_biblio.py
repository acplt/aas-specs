import re


def add_anchor_to_biblio(content):
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
        modified_figure_tag = f'[#bib{key}]\n{biblio_tag_mod} {biblio_text}'
        old_figure_tag = f'{biblio_tag} {biblio_text}'

        content = content.replace(old_figure_tag, modified_figure_tag)

    return matches.keys(), content


def add_link_to_biblio(content, keys):
    for key in keys:
        in_link_patterns = r'(?<!\[#bib{key}\]\n)\[{key}\]'
        in_link_patterns = in_link_patterns.format(key=key)
        content = re.sub(in_link_patterns, f'link:#bib{key}[[{key}\]]', content)
    return content
