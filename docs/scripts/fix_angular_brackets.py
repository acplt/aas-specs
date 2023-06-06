import re

def escape_double_angular_brackets(adoc_file):

    with open(adoc_file, 'r') as file:
        content = file.read()

    pattern = r"<<(.*?)>>"
    modified_content = re.sub(pattern, r"&lt;&lt; \1 &gt;&gt;", content)

    # Write the modified content back to the ADoc file
    with open(adoc_file, 'w') as file:
        file.write(modified_content)

directory = "../AASiD_1_Metamodel"
escape_double_angular_brackets(directory + "/AASiD_1_Metamodel_V3_0.adoc")
