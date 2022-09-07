from calculators.basic_calculator import BasicCalculator
from calculators.multiple_numbers_operation_calculator import MultipleNumbersOperationCalculator

cal = BasicCalculator()
cal.set_first_num(10)
print(cal.return_latest_number())
print(cal.addition(20))
print(cal.subtraction(5))
print(cal.division(5))
print(cal.multiplication(3))
cal.reset()
print(cal.addition(1))

mnoc = MultipleNumbersOperationCalculator()
print(mnoc.list_addition([1, 2, 4, 3]))
print(mnoc.list_subtraction([5, 1]))
mnoc.reset()
print(mnoc.list_subtraction([4, 2.5]))