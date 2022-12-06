# 3.Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



def isint(integer_num):
    while True:
        try:
            int(integer_num)
            return True
        except ValueError:
            return print('Введите натуральное число')

input_number = isint(input())

print('Число', input_number)