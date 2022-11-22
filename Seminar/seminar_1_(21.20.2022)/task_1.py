# 1- Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# Примеры:

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

one_number = int(input('Введите первое число: '))
two_number = int(input('Введите второе число: '))

if pow(one_number, 2) == two_number:
    print(f'- {one_number},{two_number} -> да')
else:
    print(f'- {one_number},{two_number} -> нет')