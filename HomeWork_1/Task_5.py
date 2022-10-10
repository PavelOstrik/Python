# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cgitb import reset
from unittest import result
import math

print('Введите координаты первой точки:')
x1 = int(input('x1: '))
y1 = int(input('y1: '))

print('Введите координаты второй точки:')
x2 = int(input('x2: '))
y2 = int(input('y2: '))

print('1 способ:')
result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'Расстояние между двумя точками в 2D пространстве = {round(result,2)}')

print('2 способ:')
result = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
print(f'Расстояние между двумя точками в 2D пространстве = {round(result,2)}')






