# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

from datetime import datetime

def give_user_text(filename: str):
    """Функция получает файл, читает его. Если находит совпадение перезаписывает строку

    Args:
        filename (str): text
    """
    with open(filename,'r+', encoding="utf8") as file: 
        atribute = file.readline().replace('пугай','')
        file.write(f'modified:{datetime.now()} --> {atribute}\n')

text = give_user_text('HomeWork_python\HW5/text.txt')

#Делал и через список, так быстрее отрабатывает программа

