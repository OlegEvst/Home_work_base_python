# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def give_int(input_string: str):
    while True:
        try:
            num = int(input (input_string)) 
            return num 
        except ValueError:
            print("Вы ввели не число")
'''
Функция получает строку,
проверяет на int = True,
возвращает int
'''
def get_binary_number(input_integer: int):
    bufer_index = ''
    while input_integer > 0:
        bufer_index = str(input_integer % 2) + bufer_index
        input_integer = input_integer // 2
    return int(bufer_index)
'''
Функция получает десятичное целое число,
цики while работает пока не приёдет к 0,
через специальный строковый буфер сложим остаток от деления 
возвращает int
'''    
number = give_int('Введите десятичное число: ')
convert_number = get_binary_number(number)

print(f'{number} -> результат: {convert_number}')
