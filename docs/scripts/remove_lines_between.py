def remove_lines_between(filename, start_line, end_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i, line in enumerate(lines, start=1):
            if i < start_line or i > end_line:
                file.write(line)

directory = "../AASiD_1_Metamodel"
start_line = 43
end_line = 554
remove_lines_between(directory + "/AASiD_1_Metamodel_V3_0.adoc", start_line, end_line)
