#1- Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#Дополнительно: можете проверить, что это действительно число, и что это 
# действительно входит в нужный диапазон

# *Пример:*

#- 6 -> да
#- 7 -> да
#- 1 -> нет

input_number = int(input('Введите число от 1 до 7: '))
if type(input_number) == int and input_number > 0 and input_number < 8:
 if input_number != 6 or input_number != 7:
  print(f'{input_number} -> Выходной день')
 else:
  print(f'{input_number} -> Выходной день')
else:
    print('Введённые данные не валидны')