# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует 
# этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков C# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

def get_language_data(filename: str):   
    with open(filename,'r', encoding="utf8") as file: 
        atribute = file.read().replace(' ', '').split(',')
        result = []
        for char in atribute:
            next = char.strip().upper()
            input_hexadecimal = ''.join(hex(ord(x))[2:] for x in next)
            result.append(input_hexadecimal.upper())
        number_list = [i for i in range(1, len(atribute) + 1)]
        return atribute, number_list, convert_number(result)
"""Функция считывает значения из файла, преобразует 2 списка и вызывает конвертатор 
    из букв в 16 систему исчисления.

    Args:
        filename (str): Текстовый файл с данными
        input_hexadecimal (str): Переменная записывает результат конвернирвоания 
        названий языков программирования в 16 систему исчисления.

    Returns:
        atribute _list_ : Список языков программирования 
        number_list _list_: Нумерованный список языков программирования
        result _list_: Переконвертированный список из 16 системы исчисления в 10 систему и сложения поэлементно числа.
    """        

def convert_number(result_list):
    dictionary = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, 
                    '7' : 7,'8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 
                    'D' : 13, 'E' : 14, 'F' : 15}
    final_list = []
    decimal = 0 
    for char in result_list:
        length = len(char) - 1 
        for i in char: 
            decimal += dictionary[i]*16**length 
            length -= 1
            decimal_sum = sum([int(j) for j in list(str(int(decimal)))])
            final_list.append(decimal_sum)
    return final_list
"""Функция получает список сотоящий из строк в 16 системе исчисления, конвертирует и возвращает список из 
значений сумм числа в 10 системе.

    Args:
        result_list _list_ : Cписок с названием языков программировния в 16 системе
        decimal _int_: Значение в 10 системе
        decimal_sum _int_: Значение очков слова

    Returns:
        final_list _list_ : Список из значений очков суммы слова в 10 сисеме  
    """
def get_capital_letter(source_list):
    """Функция создаёт список ("кортеж") из 3 списков.
    1) Нумерация (порядок)
    2) название языка програмирования с большой буквы
    3) Сумма очков слова языка програмирования

    Args:
        source_list (_type_): 3 списка

    Returns:
        all_list_List_: Сшитый список из 3 списков
    """
    new_upper_list = list(map(lambda x: x.upper(), source_list[0]))
    all_list = list(zip(source_list[1],new_upper_list, source_list[2]))
    return all_list

def tuple_unpacking(final_list : list):
    count = 0  
    for i in range(len(final_list)):
        if not final_list[i][2] % final_list[i][0]:
            count += final_list[i][2]
    return count

lang_list = get_language_data('HomeWork_python\HW5\programming_language.txt')
cart = get_capital_letter(lang_list)

print(f'Исходный список с результатами очков: {cart}')
print(f'\n\033[1;31m Cумма, очков отвечающий условию : {tuple_unpacking(cart)}\033[0m')

#Посмотрел семинар, я максимльно усложнил задачу. Буду упрощать.


