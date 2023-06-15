def remove_lines_between(filename, start_line, end_line):
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, 'w', encoding="utf-8") as file:
        for i, line in enumerate(lines, start=1):
            if i < start_line or i > end_line:
                file.write(line)
