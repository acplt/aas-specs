import re


# Define the callback function
def replacement(match):
    figure_tag = match[1]
    caption: str = match[2]

    # Move the caption to the beginning of the figure tag
    modified_figure_tag = f'.{caption.strip()}\n{figure_tag}\n'

    return modified_figure_tag


def move_caption_to_beginning(content):
    # Define the regular expression pattern to match figure tags with specific captions
    pattern = r'(image:\S+\[.*?\])\s+?\n?\n?(Figure.*?\n)'

    # Replace the original figure tags with the modified ones
    new_content = re.sub(pattern, replacement, content)
    return new_content
