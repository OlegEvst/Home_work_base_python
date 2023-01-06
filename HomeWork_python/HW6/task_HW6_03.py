# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def give_int(input_string: str):
    """Функция принемает строку и если число, возвращает число

    Args:
        input_string (str): Вводная строка

    Returns:
        num (int): Целое число, после проверок
    """
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число")

def print_list(char: int):
    """Функция получает число и с помощью list comprehension возводит в степень
        и печатает в консоль.

    Args:
        char (int): Число степени
    """
    degree_number = [(-3)**char for char in range(number)]
    print(f"Последовательность: {degree_number}")

number = give_int('Введите целое число: ')
print_list(number)



