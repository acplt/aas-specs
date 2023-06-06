import re


def remove_text_matching_regex(adoc_file, regular_exp):
    with open(adoc_file, 'r') as file:
        content = file.read()

        # Remove occurrences of the specified regular expression
        modified_content = re.sub(regular_exp, '', content)

    # Write the modified content back to the ADoc file
    with open(adoc_file, 'w') as file:
        file.write(modified_content)


directory = "../AASiD_1_Metamodel"

regular_exp_list = [r'Table of Contents\n\n(.*?)(?=\n\n==)', r'\[#_Toc\d* \.anchor]####Table \d*', r'\[#_Ref\d* \.anchor]####Table \d*',
                    r'\[\#_Ref\d* \.anchor\]\#\#', r'\[\#_Toc\d* \.anchor\]\#\#', r'\{empty\}']

for regular_exp in regular_exp_list:
    remove_text_matching_regex(directory + "/AASiD_1_Metamodel_V3_0.adoc", regular_exp)
