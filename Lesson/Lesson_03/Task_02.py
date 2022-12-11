# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 12 3 5 8 15 23 38
# Получить:
# ((2,4), (8, 64), (38, 1444)]

path ='D:\Рабочий стол\GB\Python основы\Lesson\Lesson_03/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(data[:space_pos])
    data = data[space_pos + 1:]

# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]


# res = where(lambda x: not x % 2, numbers)
# res = select(lambda x: (x, x**2), res)

# print(res)

res = map(int, numbers)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)

