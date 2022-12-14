# Создайте программу для игры в 'Крестики-нолики'

from turtle import position


position = []

for i in range(1,10):
    position.append(i)

sign = "O"

moves = []

win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]


def winCondition():
    for i in win:
        if position[i[0]-1] == position[i[1]-1] == position[i[2]-1] == "O":
            print('Игра окончена, победил игрок, ходящий "O"')
            printField(position)
            exit()
        elif position[i[0]-1] == position[i[1]-1] == position[i[2]-1] == "X":
            print('Игра окончена, победил игрок, ходящий "X"')
            printField(position)
            exit()
        
        


def printField(position):
    print(f'{position[0]:^5}|{position[1]:^5}|{position[2]:^5}')
    print('-----------------')
    print(f'{position[3]:^5}|{position[4]:^5}|{position[5]:^5}')
    print('-----------------')
    print(f'{position[6]:^5}|{position[7]:^5}|{position[8]:^5}')

while True:

    while True:
        printField(position)
        index = int(input(f"\n\nХод {'игрока' if sign == 'X' else 'противника'}: "))
        if index in moves:
            print('Эта клетка уже занята')
        else:
            if sign == "O":
                sign = "X"
            else:
                sign = "O"
            moves.append(index)
            position[index-1] = sign
            winCondition()            
        if len(moves) == len(position):
            print('Игра завершена, результат ничья')
            exit()
