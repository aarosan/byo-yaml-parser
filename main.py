from lexer import tokenize
from parser import parse

def main():
    yaml_string = """name: Coding Challenges"""
    try:
        tokens = tokenize(yaml_string)
        parsed_data = parse(tokens)
        print("Valid YAML")
        print(parsed_data)
    except ValueError as e:
        print(f"Invalid YAML: {e}")
        exit(1)

if __name__ == "__main__":
    main()