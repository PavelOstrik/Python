# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
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

# Игра между двумя игроками

if firstMove == first:
    print('Первый игрок ходит первым')    
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
            print('\nВторой игрок выиграл, так как забрал все конфеты за последний ход\n')            
            exit()

        while True:
            try:
                secondPlayer = int(input('Второй игрок берет конфеты: '))        
                if secondPlayer <= limitStroke and secondPlayer > 0:
                    candies -= secondPlayer
                    print(candies) 
                    break       
                else:                    
                    print('\nВы взяли недопустимое количество конфет за ход')
                    print('Попробуй ешё раз, возьми от 1 до 28\n')
                    
            except:
                print('Вы ввели не число, попробуй еще раз')  
                        
        if candies <= 28:            
            print('\nПервый игрок выиграл, так как забрал все конфеты за последний ход\n')            
            exit()
                
else:
    print('Второй игрок ходит первым')
    while candies > 1:
        while True:
            try:
                secondPlayer = int(input('Второй игрок берет конфеты: '))        
                if secondPlayer <= limitStroke and secondPlayer > 0:
                    candies -= secondPlayer
                    print(candies) 
                    break       
                else:
                    print('\nВы взяли недопустимое количество конфет за ход')
                    print('Попробуй ешё раз, возьми от 1 до 28\n')
            except:
                print('Вы ввели не число, попробуй еще раз')
                            
        if candies <= 28:
            print('\nПервый игрок выиграл, так как забрал все конфеты за последний ход\n')            
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
        print('\nВторой игрок выиграл, так как забрал все конфеты за последний ход\n')            
        exit()




   



        
        


        
        
        

             
