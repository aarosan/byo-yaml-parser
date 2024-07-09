import re

def tokenize(input_string):
    tokens = []
    lines = input_string.splitlines()
    indent_level = 0
    for line in lines:
        if line.strip():
            current_indent = len(line) - len(line.lstrip(' '))
            if current_indent % 2 != 0:
                raise ValueError("Invalid indentationL must be multiple of 2 spaces")
            match = re.match(r'(\w+):\s*(.*)', line.strip())
            if match:
                key, value = match.groups()
                tokens.append((key, value, current_indent))
            else:
                raise ValueError(f"Invalid YAML format: {line}")
    return tokens