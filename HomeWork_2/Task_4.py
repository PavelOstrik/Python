# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

import random
from unittest import result


n = int(input('Введите количество элементов списка: '))
list = []

for i in range(0, n):
    list.append(random.randint(-n, n))

print(list)


with open('file.txt', 'a') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('2\n')
    data.write('3\n')
    data.write('4\n')

path = 'file.txt'
with open(path, 'r') as data:   
    str1 = int(data.readline())
    str2 = int(data.readline())      
    
    result = list[str1] * list[str2]
    print(result)

# 2 способ

num = int(input('Введите количество элементов списка: '))
myList = []

for _ in range(num):
    myList.append(random.randint(-num,num))

print(myList)

xy = []

with open('file.txt') as data:
    xy = data.read().split('\n')

multi = myList[int(xy[0]) * myList[int(xy[1])]]

print(f'Произведение элементов на позициях {xy[0]} и {xy[1]} равно {multi}')





 

