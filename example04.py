# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_new_file = []
translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("file_for_example04.txt") as my_file:
    for el in my_file:
        el = el.split(" ", 1)
        my_new_file.append(translate[el[0]] + " " + el[1])
    print(my_new_file)

with open("my_new_file_for_example04.txt", "w", encoding="utf-8") as new_file:
    new_file.writelines(my_new_file)
