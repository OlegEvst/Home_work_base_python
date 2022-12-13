# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.

def give_list(input_string: str):
    while True:
        try:
            num = input(input_string).split(' ') 
            num = list(map(int, num))
            return num
        except ValueError:
            print("Вы ввели не число")

def min_max_number(input_list: list):
    max_number = max(input_list)
    min_number = min(input_list)
    return max_number,min_number

number = give_list('Введите набор чисел через пробел:')
result = min_max_number(number)

print(f'Максимальное число: {result[0]}, минимальное число: {result[1]}')