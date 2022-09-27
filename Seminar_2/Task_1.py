# 1. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
# Пример:
# o Для N = 5: 1, -3, 9, -27, 81

from array import array


N = int(input('Введите число: '))
array = []
num = 1
for i in range(1, N + 1):
    array.append(num)
    num *= -3

print(array)

# 2 вариант записи
N = int(input('Введите число: '))
array = []

for i in range(0, N):
    array.append((-3) ** i)

print(array)

# 3 вариант записи


def pos_led(N):
    array = []
    num = 1
    for i in range(1, N + 1):
        array.append(num)
        num *= -3
    return array

N = int(input('Введите число: '))
array = pos_led(N)
print(array)

# 4 вариант записи
def degree(x):
    for i in range(0, x):
        print((-3) ** i, end = ', ')

N = int(input('Введите число: '))
degree(N)