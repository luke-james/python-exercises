class OddsOrEvens:

    def __init__(self, numbers=None):

        if numbers is None:
            numbers = []

        self.numbers = numbers
        self.odd_message = "Number is odd."
        self.even_message = "Number is even."

    def calculate(self):
        # Pass function in as param (strategy pattern)
        pass

    def __is_number_odd(self, num):
        return self.__is_number_multiple_of_4(num, "")

    def __is_number_multiple_of_4(self, num, message):
        return

    def __divides_whole(self, num1, num2):
        return


if __name__ == "__main__":
    # do something
    exit(0)