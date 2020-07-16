# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
count = int(input('Введите количество элементов будущего списка:'))
new_list = []
i = 0
while i < count:
    user_answer = input('Введите элемент списка:')
    new_list.append(user_answer)
    i = i + 1
print(new_list)
j = 0
for i in range(int(len(new_list) / 2)):
    new_list[j + 1], new_list[j] = new_list[j], new_list[j + 1]
    j = j + 2
print(new_list)
