# 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# (-0.56) -> 11

def get_float(string_number):
    while True:
        try:
            number = float(input(string_number)) or number != 0
            return number
        except:
            print('Пожалуйста, введите вещественное число и не равное 0:')
# Функция принемает на вход строку и возвращает только 
# при введении числа, целого или вещественно и не 0

def get_summ(user_number):
    user_number = abs(int(str(user_number).replace('.', '')))
# В Введеном вещественном числе удаляется точка(если есть) и берет его по модулю
    result = 0
    while (user_number != 0):
        result = result + user_number % 10
        user_number = user_number // 10
    return result
# Функция принемает на вход вещественное число и возвращает сумму чисел 

def print_summ(summ_number):
    print(f'Сумма чисел в введённом числе равна = {summ_number}')
# Функция принта суммы чисел

input_number = get_float('')
summ_number = get_summ(input_number)
print_summ(summ_number)

