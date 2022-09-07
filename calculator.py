import abc


class Calculator(abc.ABC):
    VALUE_ERROR_MESSAGE = "Value must be an integer or a float"
    SYMBOLS = "+-*/"
    ZERO_DIVISION_MESSAGE = "Numbers cannot be divided by zero"

    def __init__(self):
        self.latest_result = 0

    def reset(self):
        self.latest_result = 0

    def return_latest_number(self):
        return self.latest_result

    def validate_value_is_integer(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError(self.VALUE_ERROR_MESSAGE)

    def validate_value_is_not_zero(self, value):
        if value == 0:
            raise ValueError(self.ZERO_DIVISION_MESSAGE)
