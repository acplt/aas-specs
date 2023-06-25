import re

def read_keywords_from_file(filename):
    keyword_names = []

    with open(filename, 'r') as file:
        for line in file:
            class_name = line.strip()
            keyword_names.append(class_name)

    return keyword_names

def replace_qoutes_on_keyword(adoc_file):
    with open(adoc_file, 'r') as file:
        content = file.read()

    for keyword in KEYWORD_LIST:
        replacement = '`{}`'
        pattern = re.compile(r'\"' + re.escape(keyword) + r'\"', re.IGNORECASE)
        content = pattern.sub(replacement.format(keyword), content)

    # Write the modified content back to the ADoc file
    with open(adoc_file, 'w') as file:
        file.write(content)

KEYWORD_LIST = read_keywords_from_file("keyword.txt")