# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_file = open("my_file.txt", "w")
while True:
    text = input("Введите какие-нибудь данные: ")
    my_file.write(text + '\n')
    if not text:
        break

my_file.close()

my_file = open("my_file.txt","r")
content = my_file.read()
print(content)
my_file.close()