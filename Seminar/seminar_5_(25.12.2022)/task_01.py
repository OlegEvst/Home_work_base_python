# Задана натуральная степень n. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
 
# Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0

# Уточнения:
# n - это степень икса первого элемента полинома
# при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0

# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого

import random

def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return abs(num)
        except:
            print('Попробуйте ещё раз, вы ввели не число')

def random_list(length_list):
    random_numbers = [random.randint(0, 100) for i in range(length_list + 1)]
    if random_numbers[0] == 0:
        random_numbers[0] = random.randint(1, 100)
    return random_numbers  

def cart_list(result_list):
    deegre_list = [i for i in range(len(result_list))]
    upper_list = list(reversed(deegre_list))
    union = []
    for i in list(zip(result_list, upper_list)):
        union.append(i)
    return union 

def give_deegre(input_list):
    value = ''
    for i,j in input_list: 
        if j != 0:
            value += f'{i}*x^{j} '
            value += f'+'
    if input_list[-1]!= 0:
        value += f'{input_list[-1][j]} = 0'
    else:
        value += value[:-2] + "= 0"
    return value

number = give_int('Введите целое положительное число: ')
user_list = random_list(number)
result = cart_list(user_list)
my_task = give_deegre(result)

print(f'n = {number} -> {my_task}' )


    


