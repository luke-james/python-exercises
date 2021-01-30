import pytest
import sys
sys.path.append('../src')
from src.ex1_character_input import Person, AgeError, InputParser


'''
This file will test exercise 1 - taking Character Input from the command line.
'''


def test_character_input():

    # Arrange
    name = "Luke James"
    age = 0
    new_person = Person(name, age)

    # Act && Assert
    with pytest.raises(AgeError):
        new_person.print_character_input()


def test_input_parser_ok():

    # Arrange
    name = "Luke"
    age = 25
    func_input = f'{ name } { age }'

    parser = InputParser(func_input)

    # Act && Assert
    input_name, input_age = parser.parse_input()

    assert input_name == name
    assert input_age == age


def test_input_parser_no_age():

    # Arrange
    input = "Luke"
    parser = InputParser(input)

    # Act && Assert

    with pytest.raises(ValueError):
        parser.parse_input()


def test_input_parser_invalid_age():

    # Arrange
    input = "Luke saldfjkhsdlkf"
    parser = InputParser(input)

    # Act && Assert

    with pytest.raises(ValueError):
        parser.parse_input()
