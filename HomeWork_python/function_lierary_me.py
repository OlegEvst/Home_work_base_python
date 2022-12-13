from random import randint


def give_list_float(input_string: str):
    while True:
        try:
            num = input(input_string).split(' ') 
            num_float = list(map(float, num))
            return num_float
        except ValueError:
            print("Вы ввели не число")

"""the function gives float a list
    Args:
        input_string (str): The function receives a string,
        converts string values into real numbers,
        checks that the elements are real
    Returns:
        _type_: list
    """
def give_list_int(input_string: str):
    while True:
        try:
            num = input(input_string).split(' ') 
            num_int = list(map(int, num))
            return num_int
        except ValueError:
            print("Вы ввели не число")
            
"""the function gives integer a list
    Args:
        input_string (str): The function receives a string,
        converts string values into real numbers,
        checks that the elements are real
    Returns:
        _type_: list
    """

def give_list_randon(user_number: int, min, max):
    random_list = []
    for i in range(1, user_number + 1):
        random_list.append(randint(min, max))
    return random_list

"""fills the list with random integers from minimum to maximum
    Args:
        user_number (int): integer
        min (_type_): integer
        max (_type_): integer
    Returns:
        _type_: list
"""
