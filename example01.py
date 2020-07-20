# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func():
    try:
        var_1 = float(input("Введите делимое: "))
        var_2 = float(input("Введите делитель: "))
        result = round((var_1 / var_2), 2)
    except ValueError:
        return "необходимо ввести число"
    except ZeroDivisionError:
        return "на 0 делить нельзя"
    return result


print(my_func())
