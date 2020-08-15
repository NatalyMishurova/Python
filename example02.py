# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

try:
    if num2 == 0:
        raise OwnError("На ноль делить нельзя")
    res = round((num1 / num2), 2)
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")
