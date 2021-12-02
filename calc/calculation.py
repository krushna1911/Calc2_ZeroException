"""This is our calculation base class / Abstract Class"""


class Calculation:
    """Constructor initialization"""
    # pylint: disable=too-few-public-methods
    def __init__(self, value_a, value_b):
        """self references the instantiated object of the class"""
        """these are instance properties that are being shared with the child classes"""
        self.value_a = value_a
        self.value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class

    @classmethod
    def create(cls, value_a, value_b):
        """Object for calculations"""
        return cls(value_a, value_b)
