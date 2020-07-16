# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
while True:
    user_answer = input("Введите номер месяца:")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        break
    print("Ошибка ввода, вы ввели не число. Попробуйте еще раз.")
if user_answer in [1, 2, 12, '01', '02']:
    print(seasons_dict.get(1), seasons_list[0])
elif user_answer in [3, 4, 5, '03', '04', '05']:
    print(seasons_dict.get(2), seasons_list[1])
elif user_answer in [6, 7, 8, '06', '07', '08']:
    print(seasons_dict.get(3), seasons_list[2])
elif user_answer in [9, 10, 11, '09']:
    print(seasons_dict.get(4), seasons_list[3])
else:
    print("Эммм...такого месяца не существует")
