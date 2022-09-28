# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

import random


n = int(input('Введите количество элементов списка: '))
list = []

for i in range(0, n):
    list.append(random.randint(-n, n))

print(list)

# НЕ победил(, не хочет читать путь к файлу и всё, что я только не пробовал

import pathlib
from pathlib import Path


with open("test.txt") as file:
    str1 = file.readline()
    str2 = file.readline()    

    multipli = list[str1] * list[str2]

    print[multipli]

