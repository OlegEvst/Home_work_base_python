# 3. Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Число N вводится пользователем. 
# Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в зависимости от выбранного N: 
# если пользователь введет двойку, то в файле вряд ли будут индексы 5 или 16. 
# В решении должны быть и запись в файл, и чтение из файла.

# from random import randint

# with open('file.txt', 'w') as data:
#     data.write('0\n')
#     data.write('1\n')
#     data.write('5\n')
#     data.write('8\n')
#     data.write('10\n')

# def get_numbers(n):
#     return [randint(-n/2, n) for i in range(-n, n + 1)]

# def get_data_from_file(path):
#     data = open(path, 'r')
#     dlist = [int(line.strip()) for line in data]
#     data.close()
#     return dlist

# def get_mult(numbers, datalist):
#     mult = 1
#     for i in datalist:
#         mult *= numbers[i]
#     return mult

# path = 'file.txt'
# n = 2 
# datalist = get_data_from_file(path)
# numbers = get_numbers(n)

# print(numbers)
# print(datalist)
# print(get_mult(numbers, datalist))
    



# number = int(input('Введите число N:'))
# user_list = list(map(str,[i for i in range(-number,number + 1)]))
# message = "".join(map(str, user_list))

# with open('D:\Рабочий стол\GB\Python основы\Seminar\seminar_4_(11.12.2022)/file.txt', 'w') as file:
#     for line in message:
#         file.write(line + '\n')
# file.close()

# with open('D:\Рабочий стол\GB\Python основы\Seminar\seminar_4_(11.12.2022)/file.txt','r') as file:
#     print(file.read())
# file.close()


