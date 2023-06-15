import re

def escape_double_angular_brackets(adoc_file):

    with open(adoc_file, 'r', encoding="utf-8") as file:
        content = file.read()

    pattern = r"<<(.*?)>>"
    modified_content = re.sub(pattern, r"&lt;&lt; \1 &gt;&gt;", content)

    # Write the modified content back to the ADoc file
    with open(adoc_file, 'w', encoding="utf-8") as file:
        file.write(modified_content)
