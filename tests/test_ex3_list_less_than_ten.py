import pytest

import sys
sys.path.append('../')

from src.ex3_list_less_than_ten import ListChecker

@pytest.mark.ex3test
class TestListChecker:

    def test_sublist_ok(self):

        # Arrange
        number_list = [2, 3, 5, 15, 5, 19, 6]
        ceiling = 5

        # Act
        lc = ListChecker.get_sublist(ceiling, number_list)

        # Assert
        assert lc == [2, 3]

    def test_sublist_with_word(self):

        # Arrange
        number_list = [2, 3, "hello", 5, 19, 6]
        ceiling = 5

        # Act & Assert
        with pytest.raises(ValueError):
            ListChecker.get_sublist(ceiling, number_list)

    def test_sublist_with_bool(self):

        # Arrange
        number_list = [2, 3, -1, False, 19, 6]
        ceiling = 5

        # Act & Assert
        with pytest.raises(ValueError):
            ListChecker.get_sublist(ceiling, number_list)