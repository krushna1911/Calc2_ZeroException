"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation object"""
    def get_result(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            result = value / result
        return result
