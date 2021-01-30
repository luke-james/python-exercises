import numbers


class AgeError(Exception):
    """ Throw this if a Person has been given an invalid age value. """
    pass


class InputParser:

    def __init__(self, console_input):
        self.console_input = console_input

    def parse_input(self):

        words = self.console_input.split()

        if len(words) < 2:
            self.__print_usage_instructions()
            raise ValueError

        if not isinstance(int(words[1]), numbers.Number):
            self.__print_usage_instructions()
            raise ValueError

        return words[0], int(words[1])

    @staticmethod
    def __print_usage_instructions():
        print("Usage Example: python3 ex1_character_input.py Luke 25")


class Person:

    """
    Name: Person
    Description: A class to store information about a Person, to print their information to the console.
    """

    def __init__(self, name="", age=-1):
        self.name = name
        self.age = age

    def print_character_input(self):

        if self.name == "":
            raise NameError("You haven't entered a valid name!")

        if self.age < 1:
            raise AgeError("You haven't entered a valid age!")

        print(f'Name: { self.name }, age: { self.age }')


if __name__ == "__main__":

    console_input = input("Please enter your name & age (e.g. Luke 25):")

    parser = None

    input_name = ""
    input_age = 0

    try:

        parser = InputParser(console_input)
        input_name, input_age = parser.parse_input()

    except ValueError:
        exit(1)

    try:

        person = Person(input_name, input_age)
        person.print_character_input()

    except NameError or ValueError:
        exit(1)

