# 2 - Напишите программу, которая принимает на вход число N и выдает набор 
# произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def get_integer(string_number):
    while True:
        try:
            number = int(input(string_number))
            assert number > 0
            return number
        except:
            print('Пожалуйста, введите положительное число N и не равное 0:')
# Функция принемает стороку, делает из нее число и возвращает только валидные значения
def get_factorial(user_number):
    result = 1
    for i in range(2, user_number + 1):
        result *= i
    return result
# Функция считает факториал через цикл
def print_factorial(factorial_number):
    print(f'Факториал числа равен = {factorial_number}')
# Функция принта факториала числа
input_number = get_integer('')
factorial_number = get_factorial(input_number)
print_factorial(factorial_number)