#Составьте алгоритм нахождения случайного числа без использования библиотеки random.

import datetime
import math
# Импортируем 2 библиотеки 
def get_second():
    second = datetime.datetime.today().second
    return second
# Функция отдаёт секунды с реальном времени
def get_range(second_to_day):
    value = math.ceil(math.exp(second_to_day) % 1000) 
    return value
# Функция отдаёт число, math cell откругляет до билижайшего целого числа полученного путём
# экспонирования сенуд и берем остаток от полученного числа

def random_print(random_set,value):
    for i in range(value):
        random_set.add(str(i))
    for j in random_set:
        print(int(j))
        break
# Функция печаетет первое число из заполненного множества и мы получаем рандомное число
# без закономерности

result = get_range(get_second())
random_print(set(),result)





    