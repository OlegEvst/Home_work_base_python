# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

input_one_number = float(input('Введите координату X: '))
input_two_number = float(input('Введите координату Y: '))
if input_one_number > 0 and input_two_number > 0:
    number = 1
elif input_one_number < 0 and input_two_number > 0:
    number = 2
elif input_one_number < 0 and input_two_number < 0:
    number = 3
else:
    number = 4
print(f"Точка находится в {number} четверти")

