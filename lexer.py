import re

def tokenize(input_string):
    tokens = []
    lines = input_string.splitlines()
    for line in lines:
        if line.strip():
            match = re.match(r'(\w+):\s*(.*)', line)
            if match:
                key, value = match.groups()
                tokens.append((key, value))
            else:
                raise ValueError(f"Invalid YAML format: {line}")
    return tokens