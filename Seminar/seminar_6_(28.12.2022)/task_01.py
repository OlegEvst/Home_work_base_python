# Задача с семинара:
# 1. Напишите программу вычисления арифметического выражения заданного строкой.
#  Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:* 
# 1+2*3 => 7; 
# (1+2)*3 => 9;

def input_expression(input_string: str):
    while True:
        try:
            expression = list(''.join(input(input_string)))
            for char in expression:
                if char == '^[0-9]' or char == '*' or char == '/' or char == '-' or char == '+':
                    return expression
        except:
            print('Попробуйте ещё раз, вы ввели не математическое выражение!')

def priority_action(oper :str, argument_one: str, argument_two: str):
    match oper:
        case '*':
            return int(argument_one) * int(argument_two)
        case '/':
            return int(argument_one) / int(argument_two)
        case '+':
            return int(argument_one) + int(argument_two)
        case '-':
            return int(argument_one) - int(argument_two)      

def priority(data, argument_1, argument_2):
    for i in range(len(data)):
        try:
            ind1 = data.index(argument_1)
        except ValueError:
            ind1 = -1
        try:
            ind2 = data.index(argument_2)
        except ValueError:
            ind2 = -1
        min_ind = min(ind1, ind2)
        max_ind = max(ind1, ind2)
        if min_ind != -1:
            data[min_ind - 1] = priority_action(data[min_ind], data[min_ind - 1], data[min_ind + 1])
            data.pop(min_ind)
            data.pop(min_ind)
        elif min_ind == -1 and max_ind != -1:
            data[max_ind - 1] = priority_action(data[max_ind], data[max_ind - 1], data[max_ind + 1])
            data.pop(max_ind)
            data.pop(max_ind)
        elif min_ind == max_ind == -1:
            break
    return data

mathematical_list = input_expression('Введите математическое выражение: ')
mathematical_list = priority(mathematical_list, '/', '*')
print(mathematical_list)
mathematical_list = priority(mathematical_list, '+', '-')
print(mathematical_list)
print(f'Result = {mathematical_list[0]}')
