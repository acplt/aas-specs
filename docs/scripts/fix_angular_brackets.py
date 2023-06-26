import re

def escape_double_angular_brackets(content):
    pattern = r"<<(.*?)>>"
    return re.sub(pattern, r"&lt;&lt; \1 &gt;&gt;", content)


