# 5-Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.
# Примеры:
# - [8, 8.5, 9, 9.4, 9.8, 10] => 3 (9, 9.4, 9.8)

value_mass = int(input('Введите размерность списка: '))

from random import randint
random_mass = []
for i in range(value_mass):
    random_mass.append(randint(1, 100))
    max_number = random_mass[0]
    count = 0
for j in random_mass:
    if max_number < j:
        max_number = j
for j in random_mass:
    if j > max_number * 0.9 and j < max_number * 1.1:
        count += 1
print(f'{random_mass} {max_number} {count}')