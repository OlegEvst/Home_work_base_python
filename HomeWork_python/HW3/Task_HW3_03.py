# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07 5.1 8.2444 6.98] - 0.91 или 91 

def give_list(input_string: str):
    while True:
        try:
            num = input(input_string).split(' ') 
            num_float = list(map(float, num))
            return num_float
        except ValueError:
            print("Вы ввели не число")
'''
Функция получает строку,
преобразует из сроковых значений в вещественные числа,
проверяет чтобы элементы были вещественные
возвращает list
'''
def new_result_list(input_list: list):
    sort_list = []
    for i in input_list:
        sort_list.append(round(float(i),2) % 1)
        result = max(sort_list) - min(sort_list)
    return round(float(result),2), int(round(float(result),2) * 100)
'''
Функция получает список,
создаёт новый список из значений дробных частей первычного списка,
вычитает из максимального значения минимальное,
возвращает float и int
'''
user_input_list = give_list('Введите числа через пробел: ')
print_result = new_result_list(user_input_list)

print(f'{user_input_list} -> результат: {print_result[0]} или {print_result[1]}')