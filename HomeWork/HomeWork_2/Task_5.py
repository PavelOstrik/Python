# Реализуйте алгоритм перемешивания списка.


import random

n = int(input('Введите количество элементов списка: '))

list = []

for i in range(0, n + 1):
    list.append(random.randint(0,10))

print('Изначальный список: ')
print(list)

shaker_list = []
for i in range(0, n + 1):
    i = random.randint(0, len(list) - 1)
    shaker_list.append(list[i])

print('Перемешанный список: ')
print(shaker_list)