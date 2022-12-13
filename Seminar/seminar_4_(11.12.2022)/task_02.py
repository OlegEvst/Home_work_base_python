# 2. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.
#  НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.

def give_list(input_string: int):
    while True:
        try:
            num = input(input_string).split(' ')
            num = list(map(int, num))
            if len(num) <= 2:
                return num
        except ValueError:
            print("Вы ввели не число")

number = give_list('Введите 2 числа через пробел:')

# def calculate(input_list: list):
#     greater = input_list[0] if input_list[0] > input_list[1] else input_list[1]
#     while(True): 
#         if((greater %  input_list[0] == 0) and (greater %  input_list[1]== 0)): 
#             result = greater 
#             break 
#         greater += 1 
#     return result


# print(calculate(number))

# def calculate(input_list: list):
#     while input_list[0] != 0:
#         input_list[0],input_list[1] = (input_list[0] % input_list[1]), input_list[0]
#     return input_list[0],input_list[1]

# def final_result(num_one, num_two: int):
#     summ = num_one + num_two
#     result = (num_one * num_two) // summ
#     return result
    
# number = give_list('Введите 2 числа через пробел:')
# main = calculate(number)

# print(main)
