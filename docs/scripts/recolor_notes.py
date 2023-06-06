import re


def recolor_notes(adoc_file):
    with open(adoc_file, 'r') as file:
        content = file.read()

    matches = set()

    notes_patterns = [r'(?<!foot)(?<!\[)Note:.*', r'Note\s+\d+.*', r'EXAMPLE\s+\d+:']

    for pattern in notes_patterns:
        matches.update(re.findall(pattern, content))

    # Iterate over the matches and modify the figure tags
    for match in matches:
        old_notes = match
        content = content.replace(old_notes, f'[.note-block]\n{match}')

    with open(adoc_file, 'w') as file:
        file.write(content)


directory = "../AASiD_1_Metamodel"

keys = recolor_notes(directory + "/AASiD_1_Metamodel_V3_0.adoc")