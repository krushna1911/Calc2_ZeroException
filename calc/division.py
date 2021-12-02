"""This is the division calculation"""
from calc.calculation import Calculation

"""This is how you extend the Division class with the Calculation"""


class Division(Calculation):
    """The division class inherits properties of calculation class"""
    def get_result(self):
        """This is encapsulation"""
        return self.value_a / self.value_b
