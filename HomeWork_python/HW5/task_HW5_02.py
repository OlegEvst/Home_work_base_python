# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from typing import Optional
from random import randint

print('\033[43mНа столе лежит 2021 конфета.\n' 
    'Играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьёвкой.\n' 
    'За один ход можно забрать не более чем 28 конфет.\n' 
    'Все конфеты оппонента достаются сделавшему последний ход.\n'
    'Играть можно, как с другим человеком так и с Ботом.\n'
    'Удачи!\033[0m')

def give_int(input_string: str,
        min_num: Optional[int] = 1,
        max_num: Optional[int] = 4) -> int:
    while True:
        print('\033[1;31m Введите 1 - если хотите поиграть с другим игроком \033[0m \n'
              '\033[1;31m Введите 2 - если хотите поиграть с лёгким ботом \033[0m \n'
              '\033[1;31m Введите 3 - если хотите поиграть со сложным ботом \033[0m \n'
              '\033[1;31m Введите 4 - если хотите покинуть игру\033[0m \n')
        try: 
            type_game = int(input(input_string)) 
            if type_game >= min_num and type_game <= max_num:
                if type_game == 1:
                    print(f'\033[1;32mВы выбрали игру против другого игрока \033[0m')
                elif type_game == 2:
                    print(f'\033[1;32mВы выбрали игру против лёгкого бота \033[0m')
                elif type_game == 3:
                    print(f'\033[1;32mВы выбрали игру против сложного бота \033[0m')
                elif type_game == 4:
                    return exit(print(f'\033[1;31m Вы покинули игру \033[0m'))
                return type_game
        except ValueError:
            print('\033[1;31m Введите 1 - если хотите поиграть с другим игроком \033[0m\n'
                  '\033[1;31m Введите 2 - если хотите поиграть с лёгким ботом \033[0m\n'
                  '\033[1;31m Введите 3 - если хотите поиграть со сложным ботом \033[0m\n')

def valid_name(input_string: str):
    while True:
        try:
            string = str(input (input_string))
            if all(char.isalpha() for char in string):
                return string
        except ValueError:
            print('033[1;31m Введите валидное имя\033[0m')

def give_player(user_type_game: int):
    if user_type_game == 1:
        user_one = valid_name('Введите имя игрока 1:')
        print(f'\033[1;32m{user_one}\033[0m - Хорошей игры!')
        user_two = valid_name('Введите имя игрока 2:')
        print(f'\033[1;32m{user_two}\033[0m - Хорошей игры!\n')
    elif user_type_game == 2:
        user_one = valid_name('Введите ваше имя:')
        print(f'\033[1;32m{user_one}\033[0m - Хорошей игры!')
        user_two = 'Легкий БОТ'
        print(f'С вами играет - \033[1;32m{user_two}\033[0m\n')
    elif user_type_game == 3:
        user_one = valid_name('Введите выше имя:')
        print(f'\033[1;32m{user_one}\033[0m - Хорошей игры!')
        user_two = 'Сложный БОТ'
        print(f'С вами играет - \033[1;31m{user_two}\033[0m\n')
    return user_one, user_two, user_type_game

def first_move(user_name: str):
    move_random = randint(0, 2)
    move_hard_random = randint(0, 2)
    if user_name[2] != 3:
        if move_random == 1:
            print(f"Первый ходит \033[1;35m{user_name[0]}\033[0m.")
            switch = 1
        else:
            print(f"Первый ходит \033[1;35m{user_name[1]}\033[0m.")
            switch = 0
    else:
        if move_random == 1 and move_hard_random == 1:
            print(f"Первый ходит \033[1;35m{user_name[0]}\033[0m.")
            switch = 1
        else:
            print(f"Первый ходит \033[1;35m{user_name[1]}\033[0m.")
            switch = 0
    return switch

def algorithm_game_user(gamers, count):
    value_candies = 221
    max_candies = 28
    while value_candies > 0:
        if count == 1:
            motion = int(input(f'\n{gamers[0]} заберёт = '))
            while motion < 1 or motion > max_candies:
                motion = int(input(f'\n\033[1;31m{gamers[0]} - Можно взять не более {max_candies} конфет за ход! :\033[0m'))
        value_candies -= motion
        if value_candies > 0:
                print(f'\nОсталось {value_candies}')
                count = 0
        if count == 0:
            motion = int(input(f'\n{gamers[1]} заберёт = '))
            while motion < 1 or motion > max_candies:
                motion = int(input(f'\n\033[1;31m{gamers[1]} - Можно взять не более {max_candies} конфет за ход! :\033[0m'))
        value_candies -= motion
        if value_candies > 0:
                print(f'\nОсталось {value_candies}')
                count = 1
    print(f'\n\033[1;31mПобедил --> {gamers[0]}\033[0m') if count == 1 else print(f'\n\033[1;31mПобедил --> {gamers[1]}\033[0m')

number = give_int('Поле ввода: ')
players = give_player(number)
move = first_move(players)
result_user = algorithm_game_user(players, move)

