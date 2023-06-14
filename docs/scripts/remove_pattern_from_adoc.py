import re

REGULAR_EXP_LIST = [r'Table of Contents\n\n(.*?)(?=\n\n==)', r'\[#_Toc\d* \.anchor]####Table \d*',
                    r'\[#_Ref\d* \.anchor]####Table \d*',
                    r'\[\#_Ref\d* \.anchor\](?:\#{2,4})', r'\[\#_Toc\d* \.anchor\](?:\#{2,4})', r'\{empty\}']


def remove_text_matching_regex(adoc_file):
    with open(adoc_file, 'r') as file:
        content = file.read()

    for regex in REGULAR_EXP_LIST:
        # Remove occurrences of the specified regular expression
        modified_content = re.sub(regex, '', content)

    # Write the modified content back to the ADoc file
    with open(adoc_file, 'w') as file:
        file.write(modified_content)
