# 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

def get_value(input_value):
    while True:
        try:
            value = int(input(input_value))
            assert value > 0
            return value
        except:
            print('Пожалуйста, введите размерность массива не равное 0:')
# Функция пропускает только валидные значения
input_value = get_value('')

from random import randint
random_mass = []
for i in range(input_value + 1):
     random_mass.append(randint(-100, 100))
     if random_mass[i] < 0:
        random_mass.insert(i + 1, 0) 
print(random_mass)
# Не стал выносить в отдельные функции


