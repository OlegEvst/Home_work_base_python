# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from task_HW6_05 import give_list

enumerate_source_list = give_list(10)

def whole_result(main_list):
    number = []
    value = []
    for i in range(len(main_list)):
        result = main_list[i][0] + main_list[i][1]
        if result % 5 == 0:
            number.append(main_list[i][0])
            value.append(main_list[i][1])
    result_list = list(zip(number,value))  
    return main_list, result_list 
"""Функция принемает список и возвращает 2 списка

    Args:
        main_list (list): Импортируемый список из задачи 5

    Returns:
        main_list (list):  Импортируемый список из задачи 5
        result_list (list): Отфильтрованный список по условию
"""  
       
decision_task = whole_result(enumerate_source_list[2])

print(f'{decision_task[0]} --> \033[1;33m{decision_task[1]}\033[0m')
