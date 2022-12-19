# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
#  При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

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

        """checking the string

        Args:
            input_string (string): input string

        Returns:
            _type_: string
        """

def get_number_alphabet(filename: str) -> list[str]:
    
    with open(filename,'r', encoding="utf8") as file: 
        atribute = file.read().rstrip().split('\n')
        for i in atribute:
            if bool(re.search('[а-яА-Я]', i)):
               rus_alphabet = list(i)
            else:
               eng_alphabet = list(i)
        return rus_alphabet, eng_alphabet
"""required dictionary

Args:
    filename (str): file with strings 

Returns:
list[str]: rus/eng alphabet
"""

def generate_data(input_string: str, user_alphabet: list):
    if bool(re.search('[а-яА-Я]', input_string)):
        return input_string, user_alphabet[0]
    else:
        return input_string, user_alphabet[1]
"""returns the required dictionary

    Args:
        input_string (str): input user string
        user_alphabet (list): rus/eng alphabet
    Returns:
        _type_: List and input user string
    """    

def code_cesar(text, alpha, step):
    text_list = list(text)
    result = []
    for i in text_list:
        index = alpha.index(i)
        index = (index + step) % len(alpha)
        temp = alpha[index]
        result.append(temp)
    result = ''.join(result)
    return result
"""encrypts text

    Args:
        text (string): input user string
        alpha (list): alphabet
        step (int): step for encrypts

    Returns:
        _type_: string
    """

def write_user_code(code_print_cesar: str) -> list[str]:
    with open("HomeWork_python\HW4/data.txt", "w", encoding="utf8") as file:
        file.write(code_print_cesar)
"""write result function

    Args:
        code_print_cesar (str): user input text + encrypts text
    """

alphabet = get_number_alphabet('HomeWork_python\HW4/alphabet.txt')

string = give_str('Введите слово:')

result = generate_data(string, alphabet)

final_text = code_cesar(result[0], result[1], 1)

main = write_user_code("{0} -> {1}".format(result[0],final_text))