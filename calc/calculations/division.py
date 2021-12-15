"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        result = self.values[0]
        for value in self.values[1:]:
            result = result / value
        return round(result, 3)
