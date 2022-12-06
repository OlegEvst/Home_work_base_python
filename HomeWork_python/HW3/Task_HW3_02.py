# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math

def give_list(input_string: str):
    while True:
        try:
            num = input(input_string).split(' ') 
            num_int = list(map(int, num))
            if 0 in num_int:
                print(f'Вы ввели 0')
                continue 
            return num_int 
        except ValueError:
            print("Вы ввели не число")
'''
Функция получает строку,
преобразует из сроковых значений в целые числа,
проверяет чтобы элементы не был равен 0,
возвращает list
'''
def get_multiplication_list(processed_list):
    next_list = []
    value = len(processed_list)
    for i in range(0, math.ceil(value / 2)):
        next_list.append(processed_list[i] * processed_list[value - 1 - i])
    return next_list
'''
Функция получает список,
добавляем в новый список произведение пар первых и последних элементов,
путём прохода цикла от 1 до середины списка и от последнего элемента до середины
возвращает list
'''
user_input_list = give_list('Введите числа через пробел: ')
result_list = get_multiplication_list(user_input_list)

print(f'{user_input_list} -> результат: {result_list}')