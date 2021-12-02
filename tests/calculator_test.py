"""Testing the Calculator"""
import pprint
import pytest

from calculator.calculator import Calculator

#a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    """Clears the history items"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    """Test for the clearing the tuple by method clear_history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4

def test_count_history(clear_history):
    """Testing the length of tuple"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Testing the last item of the tuple"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_first_calculation_result(clear_history):
    """Testing the first item of tuple history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_division(clear_history):
    """ tests division of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert   Calculator.division_numbers(1,2) == 0.5
