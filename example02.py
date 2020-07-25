# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
from random import randint

numbers = []
for i in range(13):
    numbers.append(randint(1, 400))

print(numbers)

new_numbers = []
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        new_numbers.append(numbers[i + 1])

print(new_numbers)
