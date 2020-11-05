"""
Modify this file, test
"""
from mock import patch


def test_invalid_input():
    pass


def test_valid_negative():
    pass

@patch('functions.get_stuff')
def test_thirteen(get_stuff):
    get_stuff.return_value = 7
    pass

# Mock this method as well
def test_thirteen_three():
    pass



def test_valid_input_positive():
    pass
