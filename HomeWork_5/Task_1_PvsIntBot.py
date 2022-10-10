# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# b) Подумайте как наделить бота 'интеллектом'

import random


candies = int(input('Введите количество конфет: '))
limitStroke = 28

winCountCandies = candies % (limitStroke + 1)
print(f'\nЧтобы победить, первым ходом нужно взять {winCountCandies} конфет\n') 

# Жеребьевка
first = 0
second = 1
list = [first, second]

firstMove = random.choice(list)    

# Игра между игроком и ботом

if firstMove == first:
    print('Игрок ходит первым')    
    while candies > 1:
        while True:
            try:
                firstPlayer = int(input('Первый игрок берет конфеты: '))
                if firstPlayer <= limitStroke and firstPlayer > 0:
                    candies -= firstPlayer
                    print(candies)
                    break
                else:                    
                    print('\nВы взяли недопустимое количество конфет за ход')
                    print('Попробуй ешё раз, возьми от 1 до 28\n')                    
            except:
                print('Вы ввели не число, попробуй еще раз')
                  
        if candies <= 28:            
            print('\nБот выиграл, так как забрал все конфеты за последний ход\n')            
            exit()
        
        botPlayer =  candies % (limitStroke + 1)
        if botPlayer == 0:  botPlayer += 1  
        print(f'Бот берет конфеты: {botPlayer} ')     
        candies -= botPlayer
        print(candies)        
                   
        if candies <= 28:
            print('\nИгрок выиграл, так как забрал все конфеты за последний ход\n')            
            exit()
            
else:
    print('Бот ходит первым')
    while candies > 1:
        botPlayer =  candies % (limitStroke + 1)
        if botPlayer == 0:  botPlayer += 1  
        print(f'Бот берет конфеты: {botPlayer} ')     
        candies -= botPlayer
        print(candies)   

        if candies <= 28:
            print('\nИгрок выиграл, так как забрал все конфеты за последний ход\n')            
            exit()

        while True:
            try:
                firstPlayer = int(input('Первый игрок берет конфеты: '))
                if firstPlayer <= limitStroke and firstPlayer > 0:
                    candies -= firstPlayer
                    print(candies)
                    break
                else:
                    print('\nВы взяли недопустимое количество конфет за ход')
                    print('Попробуй ешё раз, возьми от 1 до 28\n')
            except:
                print('Вы ввели не число, попробуй еще раз')

        if candies <= 28:
            print('\nБот выиграл, так как забрал все конфеты за последний ход\n')            
            exit()