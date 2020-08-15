# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Stock:
    def __str__(self):
        return f'Это склад'


class Equipment:
    def __init__(self, base):
        self.base = base

    def __str__(self):
        return f'Это базовое оборудование'


class Printer(Equipment):
    def __init__(self, base):
        super().__init__(base)

    def __str__(self):
        return f'{self.base} предназначен для вывода текстовой или графической информации,\nхранящейся в компьютере, на твёрдый физический носитель.'


class Scanner(Equipment):
    def __init__(self, base):
        super().__init__(base)

    def __str__(self):
        return f'{self.base} - устройство ввода, которое, анализируя какой-либо объект (обычно изображение, текст),\nсоздаёт его цифровое изображение.'


class Xerox(Equipment):
    def __init__(self, base):
        super().__init__(base)

    def __str__(self):
        return f'{self.base} - это копировальный аппарат.'


printer = Printer('Принтер')
scanner = Scanner('Сканер')
xerox = Xerox('Ксерокс')
print(printer)
print(scanner)
print(xerox)
