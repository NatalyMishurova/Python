# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def list(self):
        while True:
            try:
                numbers = int(input('Введите число и нажмите Enter: '))
                self.my_list.append(numbers)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение. Необходимо ввести число.")
                out = input(f'Введите stop если хотите выйти. Если продолжаем, нажмите Enter.')

                if out == 'STOP' or out == 'stop' or out == 'Stop':
                    return f'Вы вышли'
                else:
                    print(try_except.list())

try_except = Error()
print(try_except.list())