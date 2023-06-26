import re


def move_caption_to_beginning(content):
    # Define the regular expression pattern to match figure tags with specific captions
    pattern = r'(image:\S+\[.*?\])(.*?\n)'

    # Find all occurrences of the pattern in the content
    matches = re.findall(pattern, content)

    # Iterate over the matches and modify the figure tags
    for match in matches:
        figure_tag = match[0]
        caption: str = match[1]

        # Move the caption to the beginning of the figure tag
        modified_figure_tag = f'.{caption.strip()}\n{figure_tag}\n'
        old_figure_tag = f'{figure_tag}{caption}'

        # Replace the original figure tag with the modified one
        content = content.replace(old_figure_tag, modified_figure_tag)

    return content
