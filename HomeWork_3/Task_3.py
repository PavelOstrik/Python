# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

# 1 способ, без перевода в строку

n = int(input('Введите количество элементов списка: '))

list = []

for i in range(0, n):
    list.append(round(random.random() * random.randint(1,9), 2))

print(list)

newList = []

for i in range(len(list)):
    newList.append(round((list[i] - int(list[i])),2))

print(newList)

minElement = newList[0]
maxElement = newList[0]

for i in range(len(newList)):
    if list[i] > 0:

        if newList[i] > maxElement: 
            maxElement = newList[i] 

        if newList[i] < minElement: 
            minElement = newList[i]

print(f'разница между max: {maxElement} и min: {minElement} равна:')
print(f'{round((maxElement - minElement),2)}')





# 2 способ, с переводом в строку

# n = int(input('Введите количество элементов списка: '))

# list = []

# for i in range(0, n):
#     list.append(round(random.random() * random.randint(1,9), 2))
# print(list)

# for i in range(0, n):
#     list[i] = format(list[i], '.2f')
# print(list)

# newList = []

# for i in range(0, len(list)):    
#     newList.append(list[i].split('.'))    
#     newList[i] = int(newList[i][1])

# minElement = newList[0]
# maxElement = newList[0]
# for i in range(len(newList)):

#     if newList[i] > maxElement: 
#         maxElement = newList[i] 

#     if newList[i] < minElement: 
#         minElement = newList[i]
     
# print(f'разница между max: {maxElement/100} и min: {minElement/100} равна: ')
# print(f'{(maxElement - minElement)/100}')








