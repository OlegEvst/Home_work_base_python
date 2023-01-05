# 2- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def give_list(input_string: str):
    while True:
        try:
            num = input(input_string).split(',') 
            num_int = list(map(int, num))
            if 0 in num_int:
                print(f'Вы ввели 0')
                continue 
            return num_int 
        except ValueError:
            print("Вы ввели не число")
"""Функция получает строку, если это число то превращает в числовой список.
       Список без нулей.
    Args:
        input_string (str): Исходные строки

    Returns:
       num_int(list): Список из чисел
    """

def op_number(source_list: list):
    """Функция получает список, с помощью zip перемножает 2 списка (исходный и перевёрнутый)
    Args:
        source_list (list):  Исходный список

    Returns:
        union (list): Список перемноженных чисел
    """
    union = [num1 * num2 for num1, num2 in zip(source_list, list(reversed(source_list)))]
    return union[:int(len(source_list)/ 2)] if len(source_list) % 2 == 0 else union[:int((len(source_list)/ 2) + 1)]

input_list = give_list('Введите числа через запятую:')
result = op_number(input_list)

print(f'Результат перемножения чисел равен --> {result}')