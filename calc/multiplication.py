"""This is the multiplication class"""
from calc.calculation import Calculation
#This is how you extend the Multiplication class with the Calculation
class Multiplication(Calculation):
    """The Multiplication class inherits the property from the calculation parent class"""
    def get_result(self):
        """This is encapsulation"""
        return self.value_a * self.value_b
