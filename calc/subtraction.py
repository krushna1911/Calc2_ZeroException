"""This is the Subtraction calculation that is being inherits from the calculation class"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """The Subtraction class inherits properties from the calculation parent class"""
    def get_result(self):
        """This is encapsulation"""
        return self.value_a - self.value_b
