class OddsOrEvens:

    '''
    This class will calculate the response message for the input given.
    '''

    def __init__(self, numbers=None):

        if numbers is None:
            numbers = []

        self.numbers = numbers
        self.odd_message = "The number is odd!"
        self.even_message = "The number is even!"

    def calculate(self):

        # This function will work out which function to call based on the number of inputs.

        if len(self.numbers) == 2:
            return self.__divides_whole(self.numbers[1], self.numbers[0])

        if len(self.numbers) == 1:
            return self.__is_number_odd(self.numbers[0])

        raise ValueError

    def __is_number_odd(self, num):

        # This function will work out whether the number to check is odd.

        message = self.even_message if num % 2 == 0 else self.odd_message
        return self.__is_number_multiple_of_4(num, message)

    @staticmethod
    def __is_number_multiple_of_4(num, message):

        # This function will calculate whether or not the number to check is a multiple of 4.

        return message if not num % 4 == 0 else "The number is a multiple of 4!"

    def __divides_whole(self, num1, num2):

        # This function will calculate whether or not the number to check divides wholly into into the number provided.

        return "The numbers divide exactly!" if num1 % num2 == 0 else self.__is_number_odd(num1)


if __name__ == "__main__":

    # Main function to run the program.

    while True:

        raw = input("Please enter some numbers (e.g. 4 or 4 16):")

        numbers = [int(x) for x in raw.split()]

        oe = OddsOrEvens(numbers)
        message = oe.calculate()

        print(message)