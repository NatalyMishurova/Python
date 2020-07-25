# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from random import randint

numbers = []
for i in range(100, 1002, 2):
    numbers.append(i)

print(f"Список четных чисел от 100 до 1000: {numbers}")

from functools import reduce

result_numbers = reduce((lambda x, y: x * y), numbers)
print(f"Произведение всех четных чисел от 100 до 1000: {result_numbers}")
