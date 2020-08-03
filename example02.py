# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open("file_for_example02.txt", "r", encoding='utf-8')
content = my_file.readlines()
print(f"Количество строк в файле: {len(content)}")
i = 0
for text in content:
    words = len(text.split())
    i = i + 1
    print(f"Количество слов в {i} строке: {words}")
my_file.close()
