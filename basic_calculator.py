class Calculator:
    VALUE_ERROR_MESSAGE = "Value must be an integer or a float"
    SYMBOLS = "+-*/"
    ZERO_DIVISION_MESSAGE = "Numbers cannot be divided by zero"

    def __init__(self):
        self.previous_result = 0

    def set_first_num(self, first_num):
        self.previous_result = first_num

    def addition(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.previous_result + second_num

        self.previous_result = result
        return self.previous_result

    def subtraction(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.previous_result - second_num

        self.previous_result = result
        return self.previous_result

    def multiplication(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.previous_result * second_num

        self.previous_result = result
        return self.previous_result

    def division(self, second_num):
        self.validate_value_is_integer(second_num)
        self.validate_value_is_not_zero(second_num)

        result = self.previous_result / second_num
        result_as_string = str(result)

        self.previous_result = self.format_as_int_or_float(result_as_string)
        return self.previous_result

    def reset(self):
        self.previous_result = 0

    def validate_value_is_integer(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError(self.VALUE_ERROR_MESSAGE)

    def validate_value_is_not_zero(self, second_num):
        if second_num == 0:
            raise ValueError(self.ZERO_DIVISION_MESSAGE)

    @staticmethod
    def format_as_int_or_float(result_as_string):
        result = float(result_as_string.rstrip('0').rstrip('.'))

        if '.' not in result_as_string:
            return int(result)

        return result
