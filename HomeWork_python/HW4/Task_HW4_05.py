#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

import re

def give_str(input_string):
    while True:
        try:
            string = str(input (input_string))
            if bool(re.search('[а-яА-Я]', string)):
                return string
            elif bool(re.search('[a-zA-Z]', string)):
                return string
        except ValueError:
            print("Вы ввели не строку")

def write_user_data(filename: str, text: str) -> list[str]:
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)


def get_user_data(filename: str):
    with open(filename,'r', encoding="utf8") as file: 
        atribute = file.readline()
        encoding = "" 
        i = 0
        while i < len(atribute):
            count = 1
            while i + 1 < len(atribute) and atribute[i] == atribute[i + 1]:
                count = count + 1
                i = i + 1
            encoding += str(count) + atribute[i]
            i = i + 1
            next = ''
            for j in encoding:
                if j != '1':
                    next += j    
 
    print(next)
 
string = give_str('Введите слово:')
users = write_user_data('HomeWork_python\HW4/user_data.txt', string)
read_user_data = get_user_data('HomeWork_python\HW4/user_data.txt')





