# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def info_user(user_name, user_surname, bday, user_town, email, user_phone):
    print(f"{user_name} {user_surname} {bday} {user_town} {email} {user_phone}")


info_user(user_phone='892222222', email='test@mail.ru', user_town='Воронеж', bday='1991', user_name='Наталья',
          user_surname='Мишурова')

# Второй вариант решения:
# def info_user(**info):
#     return info
#
#
# print(info_user(user_name='Наталья', user_surname='Мишурова', bday='1991', user_town='Воронеж', email='test@mail.ru',
#                 user_phone='892222222'))
