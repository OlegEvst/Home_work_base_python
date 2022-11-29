# 4-Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.

# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

input_number = float(input('Введите дробное число: '))
result_number = int((input_number * 10) % 10)
if result_number != 0:
    print(f'- {input_number} -> {result_number}')
else:
    print(f'- {int(input_number)} -> нет')
