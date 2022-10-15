# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from audioop import mul
import random


n = int(input('Введите количество элементов списка: '))

# list = []
# for i in range(0, n):
#     list.append(random.randint(1,5))

# Исполльзуем ListComprehension
list = [random.randint(1,5) for i in range(0, n)]

print(list)

# newList = []
# for i in range(0, int((len(list) + 1) / 2)):
#     multi = list[i] * list[len(list)-i-1]
#     newList.append(multi)

# Используем ListComprehension
newList = [list[i] * list[len(list)-i-1] for i in range(0, int((len(list) + 1) / 2))]

print('Произведение пар чисел списка, где парой считаем первый и последний элемент: ')
print(newList)