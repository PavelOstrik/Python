# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from unittest import result


def multiplication_list(n):
    list = []

    for i in range(1, n + 1):
        result = 1
        for j in range(1, i + 1): 
            result *= j
        list.append(result)

    return list

n = int(input('Введите число: '))
print(f'Набор произведений чисел от 1 до {n}:')
print(multiplication_list(n))
