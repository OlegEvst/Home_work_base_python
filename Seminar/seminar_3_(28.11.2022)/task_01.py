# 1. Задайте список. Напишите программу, которая определит, присутствует ли 
# в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

input_list = ['gfh5', 'gfh2', '67', 'jy32', '3put']
test_1 = 3

def get_number(user_list, user_number):
    for char in user_list:
        if str(user_number) in char:
            return (user_list.index(char) 
                if user_list.index(char) 
                else 'Такого числа нет')
       
print(get_number(input_list, test_1))