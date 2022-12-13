# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

user_list = [1,1,1,1,2,2,2,3,3,3,4]

def get_result_list(source_list: list):
    main_list = []
    [main_list.append(i) for i in source_list if not i in main_list]
    return main_list

"""_the function takes a random list, creates a temporary array 
    in which it writes unique elements_
    Args:
        source_list (list): list
    Returns:
        _type_: _list_
"""
get_list = get_result_list(user_list)

print(f'{user_list} -> {get_list}')




    