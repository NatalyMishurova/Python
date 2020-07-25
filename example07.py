# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp = temp * i
        yield temp


n = int(input("Укажите факториал числа, которого Вы хотели бы узнать? "))
for el in fact(n):
    print(el)
