# Реализуйте алгоритм перемешивания списка.


import random

# 1 способ
num = int(input('Введите количество элементов списка: '))

myList = []

for _ in range(num):
    myList.append(random.randint(0, num))

print(myList)

newList = []

while 0 < len(myList):
    index = random.choice(range(len(myList)))
    newList.append(myList[index])
    myList.pop(index)

print(newList)

# 2 способ
n = int(input('Введите количество элементов списка: '))

list = []

for i in range(0, n):
    list.append(random.randint(0,10))

print('Изначальный список: ')
print(list)

shaker_list = list[:]

list_lenght = len(shaker_list)
for i in range(list_lenght):
    random_index = random.randint(0, list_lenght - 1)
    temp = shaker_list[i]
    shaker_list[i] = shaker_list[random_index]
    shaker_list[random_index] = temp
    

print('Перемешанный список: ')
print(shaker_list)

