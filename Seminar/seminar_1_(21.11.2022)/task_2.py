# 2- Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# one_num, two_num, thre_num, four_num,five_num = map(int, 
# input('Введите 5 чисел, через запятую: ').split(","))
# max_num = one_num
# if two_num > one_num and two_num > thre_num and two_num > four_num and two_num > five_num:
#     max_num = two_num
# elif thre_num > one_num and thre_num > two_num and thre_num > four_num and thre_num > five_num:
#     max_num = thre_num
# elif four_num > one_num and four_num > two_num and four_num > thre_num and four_num > five_num:
#     max_num = four_num
# elif five_num > one_num and five_num > two_num and five_num > thre_num and five_num > four_num:
#     max_num = five_num 

# print(f'- {one_num}, {two_num}, {thre_num}, {four_num}, {five_num} -> {max_num}')

input_numbers = input('Введите 5 чисел, через запятую: ').split(",")
max_number = input_numbers[0]
for number in input_numbers:
    if max_number < number:
        max_number = number 
print(f'- {[int(value) for value in input_numbers]} -> {max_number}')
