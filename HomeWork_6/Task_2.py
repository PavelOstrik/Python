# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

import random
from unittest import result

num = int(input('Введите количество элементов списка: '))

# myList = []
# for _ in range(num):
#     myList.append(random.randint(-num,num))

# Примерняем ListComprehension
myList = [random.randint(-num,num) for _ in range(num)]

print(myList)

xy = []

with open('file.txt') as data:
    xy = data.read().split('\n')

multi = myList[int(xy[0])] * myList[int(xy[1])]

print(f'Произведение элементов на позициях {xy[0]} и {xy[1]} равно {multi}')



