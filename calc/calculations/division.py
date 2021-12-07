"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        division_of_values = self.values[0]
        for value in self.values[1:]:
            division_of_values = division_of_values / value
            pprint.pprint(value)
        return round(division_of_values, 3)
