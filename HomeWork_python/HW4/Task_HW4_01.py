# 1 - Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from typing import Optional

def give_int(input_string: str,
            min_num: Optional[int] = 2,
            max_num: Optional[int] = 50) -> int:
    while True: 
        try:
            num = int(input (input_string)) 
            if min_num and num < min_num:
                print(f'Введите размерность больше {min_num}')
                continue
            if max_num and num > max_num:
                print (f'Введите размерность, меньше чем {max_num}')
                continue 
            return num 
        except ValueError:
            print("Вы ввели не число")

"""The function gets a string, checks the dimensions and the integer correspondence
    Args:
        input_string (str): string
        min_num: Optional[int]: integer
        max_num: Optional[int]: integer
    Returns:
        _type_: integer
"""

def give_simple_mult(input_number: int):
    result = []
    prime_number = 2 
    while prime_number <= input_number: 
        if not input_number % prime_number: 
            result.append(prime_number)
            input_number = input_number / prime_number
        else:
            prime_number += 1
    return result

"""_the function takes a positive integer and finds prime factors by dividing by the remainder
    Args:
        input_number (int): integer
        prime_number (int): integer
        result(list): list
    Returns:
        type: list
"""
number = give_int("Введите натуральное число N:")
final_number = give_simple_mult(number)

print(f'N = {number} -> {final_number}')