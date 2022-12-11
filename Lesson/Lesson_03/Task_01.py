# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 12 3 5 8 15 23 38
# Получить:
# ((2,4), (8, 64), (38, 1444)]

# def f(x):
#     return x**3

# list = [f(i) for i in range(1,100) if i % 2 == 0]

# print(list)

input_list = [i for i in [12,3,5,8,15,23,38] if i % 2 == 0]

def func_list(input_list):
    return input_list**2

result_list = [(i,func_list(i)) for i in input_list]


print(input_list)
print(result_list)