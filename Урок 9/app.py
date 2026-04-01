from utils.math_utils import PI, add, subtract
from utils.math_utils_evil import add as evil_add

result = add(10, 15)
print(result)
result_2 = subtract(10, 6)
print(result_2)
result_3 = evil_add(10, 20, 30)
print(result_3)
print(PI)
