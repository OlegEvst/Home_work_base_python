# 5- Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

import math
# Подключаем модуль 
input_one_point = [float(input_one_point) for input_one_point in
                input('Введите координаты первой точки через "," ').split(',')]  
input_two_point = [float(input_two_point) for input_two_point in
                input('Введите координаты второй точки через "," ').split(',')]  

print(round(math.sqrt(pow(input_two_point[0] - input_one_point[0], 2) + 
                (pow(input_two_point[1] - input_one_point[1], 2))), 2))
# Используем 3 функции:
# 1: встройная функция округления
# 2: встройная функция извлечения корня
# 3: встройная функция возведения в степень


