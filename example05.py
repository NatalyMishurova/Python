# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("file_for_example05.txt", "w", encoding="utf-8") as my_file:
    numbers = input("Введите числа через пробелы: ")
    my_file.writelines(numbers)
    my_numbers = numbers.split()
print(sum(map(int, my_numbers)))
