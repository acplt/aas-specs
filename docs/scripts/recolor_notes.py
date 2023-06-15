import re


def recolor_notes(adoc_file):
    with open(adoc_file, 'r', encoding="utf-8") as file:
        content = file.read()

    matches = set()

    notes_patterns = [r'(?<!foot)(?<!\[)Note:.*', r'Note\s+\d+.*', r'EXAMPLE\s+\d+:.*']

    for pattern in notes_patterns:
        matches.update(re.findall(pattern, content))

    # Iterate over the matches and modify the figure tags
    for match in matches:
        old_note = match
        # match = re.sub(r'Note:|Note\s+(\d+)(:*)', lambda m: '' if m.group(1) is None else m.group(1)+" :", match)
        match = match.strip().capitalize()
        content = content.replace(old_note, f'====\n{match}\n====')

    with open(adoc_file, 'w', encoding="utf-8") as file:
        file.write(content)
