# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random


candies = int(input('Введите количество конфет: '))
limitStroke = 28

winCountCandies = candies % (limitStroke + 1)
print(f'Чтобы победить первым ходом нужно взять {winCountCandies} конфет') 

# Жеребьевка
first = 0
second = 1
list = [first, second]

firstMove = random.choice(list)    

# Игра между игроком и ботом

if firstMove == first:
    print('Игрок ходит первым')
    while candies > 1:
        firstPlayer = int(input('Игрок берет конфеты: '))
        if firstPlayer <= limitStroke:
            candies -= firstPlayer
            print(candies)
        else:
            print('Вы взяли недопустимое количество конфет за ход')
            exit()       
        if candies <= 28:
            print('Бот выиграл, так как забрал все конфеты за последний ход')
            exit()
        
        botPlayer =  random.randint(1,28)  
        print(f'Бот берет конфеты: {botPlayer} ')     
        if botPlayer <= limitStroke:
            candies -= botPlayer
            print(candies)        
        else:
            print('Вы взяли недопустимое количество конфет за ход')
            exit()            
        if candies <= 28:
            print('Игрок выиграл, так как забрал все конфеты за последний ход')
            exit()
            
else:
    print('Бот ходит первым')
    while candies > 1:
        botPlayer =  random.randint(1,28)  
        print(f'Бот берет конфеты: {botPlayer} ')     
        if botPlayer <= limitStroke:
            candies -= botPlayer
            print(candies)        
        else:
            print('Вы взяли недопустимое количество конфет за ход')
            exit()            
        if candies <= 28:
            print('Игрок выиграл, так как забрал все конфеты за последний ход')
            exit()

        firstPlayer = int(input('Игрок берет конфеты: '))
        if firstPlayer <= limitStroke:
            candies -= firstPlayer
            print(candies)
        else:
            print('Вы взяли недопустимое количество конфет за ход')
            exit()       
        if candies <= 28:
            print('Бот выиграл, так как забрал все конфеты за последний ход')
            exit()