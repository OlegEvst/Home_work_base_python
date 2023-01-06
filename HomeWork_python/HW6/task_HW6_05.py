# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random

def give_list(user_number: int):
    random_list = [random.randint(1,201) for k in range(user_number)]
    enumerate_list = list(enumerate(random_list))
    number_list = []
    value_list = []
    for i in range(len(enumerate_list)):
        if enumerate_list[i][0] != enumerate_list[i][1]:
            number_list.append(enumerate_list[i][0])
            value_list.append(enumerate_list[i][1])
        result_list = list(zip(number_list,value_list))
    return random_list, enumerate_list, result_list
"""Функция принемает число и возвращает 3 списка
    Args:
        user_number (int): Число рандомных чисел в списке

    Returns:
        random_list (list): Рандомный список целых чисел
        enumerate_list (list): Список картежей
        result_list (list): Отфильтрованный список по условию
""" 
random_user_list = give_list(10)
print(f'{random_user_list[0]} -->\033[1;31m{random_user_list[1]}\033[0m --> \033[1;33m{random_user_list[2]}\033[0m')

