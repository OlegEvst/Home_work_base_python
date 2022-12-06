# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from typing import Optional
from random import randint

def give_int(input_string: str,
            min_num: Optional[int] = 5,
            max_num: Optional[int] = 20) -> int:
    while True:
        try:
            num = int(input (input_string)) 
            if min_num and num < min_num:
                print(f'Введите размерность больше {min_num}')
                continue
            if max_num and num > max_num:
                print (f'Введите размерность, меньше чем {max_num}')
                continue 
            return num 
        except ValueError:
            print("Вы ввели не число")
'''
Функция получает строку,
проверяет на int = True,
проверяет границы min и max
возвращает int
'''
def give_list(user_number: int):
    random_list = []
    for i in range(1, user_number + 1):
        random_list.append(randint(-100, 100))
    return random_list
'''
Функция получает целое число,
заполняет список рандомными целыми числами от -100 до 100
возвращает list
'''
def summ_list(user_list: list):
    next_list = []
    result = 0
    for i in user_list:
        if user_list.index(i) % 2 == 0:
            result += i
            next_list.append(i)
    return result, next_list
'''
Функция получает список,
суммирует элементы стоящие на нечётных позициях,
заполняет новый массив из элементов стоящих на нечётных позициях,
возвращает int и list
'''  
number = give_int('Введите размерность списка: ')
random_user_list = give_list(number)
get_result = summ_list(random_user_list)

print(f'{random_user_list} -> на нечётных позициях элементы {str(get_result[1])[1: -1]} ответ: {get_result[0]}')
