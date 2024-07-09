import pytest
from lexer import tokenize
from parser import parse

def test_indentation():
    yaml_string = "name: Coding Challenges\nchallenge:\n  name: YAML Parser"
    tokens = tokenize(yaml_string)
    parsed_data = parse(tokens)
    assert parsed_data == {
        "name": "Coding Challenges",
        "challenge": {
            "name": "YAML Parser"
        }
    }