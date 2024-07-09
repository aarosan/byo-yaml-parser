import pytest
from lexer import tokenize
from parser import parse

def test_valid_yaml():
    yaml_string = "name: Coding Challenges"
    tokens = tokenize(yaml_string)
    parsed_data = parse(tokens)
    assert parsed_data == {"name": "Coding Challenges"}

def test_invalid_yaml():
    yaml_string = "name Coding Challenges"
    with pytest.raises(ValueError):
        tokens = tokenize(yaml_string)