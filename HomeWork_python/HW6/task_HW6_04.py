# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

from typing import Optional
import random

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
"""Функция получает строку,
проверяет на int = True,
проверяет границы min и max
возвращает int

    Args:
        input_string (str): Вводное значение
        min_num (Optional[int], optional): _description_. Defaults to 5.
        max_num (Optional[int], optional): _description_. Defaults to 20.

    Returns:
        num (int): Валидное целое число
"""

def give_list(user_number: int):
    random_list = [random.randint(1,100) for k in range(user_number)]
    source_list = []
    for char in random_list:
        result = 0
        while (char != 0):
            result = result + char % 10
            char = char // 10
        source_list.append(result)
    is_odd = lambda number: False if number % 2 else True
    filter_list = list(map(is_odd, source_list))
    result_list = [i for i,j in zip(random_list,filter_list) if j == True]
    return random_list, source_list, result_list
"""_Функция получает целое число,
заполняет список рандомными целыми числами от 1 до 100
создаёт список из суммы чисел элементов списка
проверяет, если сумма чётная то с помощью map возвращает true

    Args:
        user_number (int): Размер рандомного списка

    Returns:
        random_list (list): Рандомный список из чисел
        source_list (list): Список из сумм чисел рандомного списка
        filter_list (list): Список стоящий из истинных или ложных условий
        result_list (list): Список состоящий из элементов, чья сумма чисел чётная
    """

number = give_int('Введите размерность списка: ')
random_user_list = give_list(number)

print(f'Рандомный массив:{random_user_list[0]}\n'
      f'Сумма чисел рандомного массива:{random_user_list[1]}\n'
      f'Финальный список:{random_user_list[2]}')
