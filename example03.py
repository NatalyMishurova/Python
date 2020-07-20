# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(x, y, z):
    user_numbers = [x, y, z]
    user_numbers.remove(min(x, y, z))
    return sum(user_numbers)


print(f'Сумма двух наибольших чисел равна: {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
