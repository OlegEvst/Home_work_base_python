from random import randint
import datetime 
import names
import random

def get_name_and_surname():
    name_and_surname = names.get_full_name()
    return name_and_surname.split()
"""Функция геренирует случайное имя с помощью модуля names

    Returns:
        name_and_surname _string_: Возвращаемое имя, через split (имя фамилия)
"""

def get_brihtday():
    date = datetime.date(randint(1978,2004), randint(1,12),randint(1,30))
    return date
"""Функция геренирует случайную дату в интервале 

    Returns:
        date _string_: Возвращает дату
    """

def get_work():
    with open('D:/Рабочий стол/GB/Python основы/Lesson/Lesson_04/users_data/work.txt', 'r', encoding="utf8") as file:
        atribute = file.read().rstrip().split(',')
        works = [char for char in atribute]
        work = random.choice(works).capitalize()
    return work
"""Функция выбирает случайную профессию из файла work

    Returns:
        work _list_: Возвращаемый список из профессий
    """
