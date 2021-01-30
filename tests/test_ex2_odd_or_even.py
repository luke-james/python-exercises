import pytest
import sys
sys.path.append('../src')
from src.ex2_odd_or_even import OddsOrEvens

@pytest.mark.ex2test
class TestOddOrEven:

    def test_is_number_even(self):

        # Arrange
        number = [6]
        oe = OddsOrEvens(number)

        # Act
        message = oe.calculate()

        # Assert
        assert message == "The number is even!"

    def test_is_number_odd(self):

        # Arrange
        number = [5]
        oe = OddsOrEvens(number)

        # Act
        message = oe.calculate()

        # Assert
        assert message == "The number is odd!"

    def test_is_number_multiple_of_four(self):

        # Arrange
        number = [8]
        oe = OddsOrEvens(number)

        # Act
        message = oe.calculate()

        # Assert
        assert message == "The number is a multiple of 4!"

    def test_does_number_divide_exactly_yes(self):

        # Arrange
        numbers = [2, 8]
        oe = OddsOrEvens(numbers)

        # Act
        message = oe.calculate()

        # Assert
        assert message == f'The numbers divide exactly!'

    def test_does_number_divide_exactly_yes(self):

        # Arrange
        numbers = [8, 2]
        oe = OddsOrEvens(numbers)

        # Act
        message = oe.calculate()

        # Assert
        assert message == f'The number is even!'

