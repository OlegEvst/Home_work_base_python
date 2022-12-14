# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные 
# буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def get_user_data(filename: str) -> list[str]:
    with open(filename,'r', encoding="utf8") as file: 
        atribute = file.read().rstrip().split('\n')
        return atribute

def get_general_vocabulary(user_Name: list[str], user_Progress: list[str]) -> dict[str,int]:
    """the function gets two lists and connects them using zip

    Args:
        user_Name (list[str]): name from the file
        user_Progress (list[str]): rating from the file

    Returns:
        dict[str,int]: dict name + rating
    """
    first_user_dict = {}
    for param_one, param_two in zip(user_Name, user_Progress):
        first_user_dict[param_one] = int(param_two)
    return first_user_dict  

def rename_dict(result: dict[str,int]) -> dict[str,int]:
    """the function accepts a dictionary and changes the case of the name
    if the score is greater than 4

    Args:
        result (dict[str,int]): dict name + rating

    Returns:
        dict[str,int]: dict rename + rating
    """
    for user, count in result.copy().items():
        capital_name = user.upper() if count >= 4 else user[:]
        result[capital_name] = result.pop(user)
    return result

def this_print(print_dict: dict[str,int]):
    """print in console

    Args:
        print_dict (dict[str,int]): dict rename + rating
    """
    for give_one_parametr, give_two_parametr in print_dict.copy().items():
        print("{0}: {1}".format(give_one_parametr,give_two_parametr))


users = get_user_data('HomeWork_python\HW4/users.txt')
progress = get_user_data('HomeWork_python\HW4/users_progress.txt')
result = get_general_vocabulary(users,progress)
output_dict = rename_dict(result)
task_print = this_print(output_dict)



