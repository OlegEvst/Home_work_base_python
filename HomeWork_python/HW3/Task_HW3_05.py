# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def give_int(input_string: str):
    while True:
        try:
            num = int(input (input_string)) 
            return num 
        except ValueError:
            print("Вы ввели не число")
'''
Функция получает строку,
проверяет на int = True,
проверяет границы min и max
возвращает int
'''
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
'''
Функция получает int,
с помощью рекурсии выполняется классическая 
последовательность F_{n}=F_{n+2}-F_{n+1}}:
возвращает int
'''
def negaFibonacci(n):
    if n in (1, 2):
        return(1 if n == 1 else -1)
    else:
        x, y = 1, -1
        for i in range(2, n):
            x, y = y, x - y
    return y
'''
Функция получает int,
последовательность рабоатет по Fn = F(n+2)-F(n+1).
возвращает int
'''
def print_list(input_number):
    fibonacci_list = []
    for char in range(1, input_number + 1):
        fibonacci_list.append(fibonacci(char))
        fibonacci_list.insert(0, negaFibonacci(char))
    return fibonacci_list
'''
Функция получает int,
формируется список из элементов двух последовательностей.
возвращает list
'''
number = give_int('Введите размерность списка: ')
print(f'k = {number} -> список будет выглядеть так: {print_list(number)}')
