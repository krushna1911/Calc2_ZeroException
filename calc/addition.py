""" This is the addition calculation that is being inherits"""

from calc.calculation import Calculation


class Addition(Calculation):
    # pylint: disable=too-few-public-methods
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):

        """ This is encapsulation """

        return self.value_a + self.value_b
