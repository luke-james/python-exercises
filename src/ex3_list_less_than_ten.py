import numbers

"""

Write a program that prints out a set of the elements of the list that are less than 5.

"""

class ListChecker:

    @staticmethod
    def get_sublist(ceil, list_to_check):
        return [x
                for x in ListChecker.validate_list_input(list_to_check)
                if x < ceil]

    @staticmethod
    def validate_list_input(list_to_validate):
        for x in list_to_validate:
            if not isinstance(x, numbers.Number) or type(x) == bool:
                raise ValueError
        return list_to_validate


if __name__ == "__main__":

    while True:

        numbers_for_list = input("Please enter some numbers (first number being the ceiling): ")

        list_to_check = []
        ceil = None

        try:
            list_to_check = [int(x) for x in numbers_for_list.split()]
        except ValueError:
            print("The list you provided contained an item that wasn't a whole number!")
            exit(1)

        if len(list_to_check) <= 2:
            exit(1)

        ceil = list_to_check[0]
        list_to_check.pop(0)

        sublist = ListChecker().get_sublist(ceil, list_to_check)
        print(set(sublist))