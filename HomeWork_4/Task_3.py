# Задайте последовательность цифр. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random


n = int(input('Введите количество элементов последовательности цифр: '))

list = []
for i in range(n):
    list.append(random.randint(1,9))

print('Исходная последовательность: ')
print(list)

# Через множества

listResult = set(list)
print('Множество: ')
print(f'{listResult} не разобрался как решить через множество')

# Множество не содержит дубликаты элементов, как удалить из множества элементы
# повторяющиеся в списке я не разобрался

# Через циклы

newList = []
for i in range(len(list)):
    found = list[i]
    count = 0
    for j in range(len(list)):
        if found == list[j]:
            count += 1
    if count == 1:
        newList.append(list[i])

print('Список неповторяющихся элементов исходной последовательности: ')
print(newList)
