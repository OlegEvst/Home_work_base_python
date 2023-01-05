# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension
# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def give_index(input_list: list, input_string :str):
    while True:
        try:
           search = [i for i,val in enumerate(input_list) if val == input_string]
        except ValueError:
           search = [-1] 
        return search
""" Функция получает список и строку

    Args:
        input_list (list): Исходный список
        input_string (str): Искомая строка

    Returns:
        search (list): Список из индексов найденных строк в списке 
    """
            
user_list =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
user_string = str(input('Введите искомое значение:'))

task_print = give_index(user_list, user_string)

print(f'список: {user_list}, ищем: {user_string}, ответ: {task_print[1]}') if len(task_print) > 1 else print(f'список: {user_list}, ищем: {user_string}, ответ: {-1}')












# y = filter(lambda x: (x == 'qwe'), (user_list))

# if len(list(y)) > 1:
#     print(user_list.index(list(y))) 


# # print(len(list(y)))

# # print(user_list.index(list(y)))
# # index = user_list.index(y)
# # print('The index of e:', index)
# # list.index(element)
# # print(list(y))

