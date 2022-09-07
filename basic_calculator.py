from calculators.calculator import Calculator


class BasicCalculator(Calculator):

    def __init__(self):
        super().__init__()

    def set_first_num(self, first_num):
        self.latest_result = first_num

    def addition(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.latest_result + second_num

        self.latest_result = result
        return self.latest_result

    def subtraction(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.latest_result - second_num

        self.latest_result = result
        return self.latest_result

    def multiplication(self, second_num):
        self.validate_value_is_integer(second_num)

        result = self.latest_result * second_num

        self.latest_result = result
        return self.latest_result

    def division(self, second_num):
        self.validate_value_is_integer(second_num)
        self.validate_value_is_not_zero(second_num)

        result = self.latest_result / second_num
        result_as_string = str(result)

        self.latest_result = self.format_as_int_or_float(result_as_string)
        return self.latest_result

    @staticmethod
    def format_as_int_or_float(result_as_string):
        result = float(result_as_string.rstrip('0').rstrip('.'))

        if '.' not in result_as_string:
            return int(result)

        return result
