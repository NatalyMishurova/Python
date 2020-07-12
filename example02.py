# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds_in_minute = 60
seconds_in_hour = 3600

seconds = int(input("Введите количество секунд"))

h = seconds // seconds_in_hour
m = (seconds - h * seconds_in_hour) // seconds_in_minute
s = seconds - h * seconds_in_hour - m * seconds_in_minute

print("{} hours {} minutes {} seconds".format(h, m, s))
