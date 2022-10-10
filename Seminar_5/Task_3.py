# Дан список чисел. Создайте список, в который попадают числа, описывающие 
# возврастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д   


import random

list = [i for i in range(1,10)]
random.shuffle(list)
print(list)

newList = []
for i in range(len(list) - 1):
    subList = [list[i]]
    for j in range(i, len(list) - 1):
        if list[j] < list[j+1]:
            subList.append(list[j+1])
        else:
            break
    if len(subList) > 1 and ''.join(map(str,subList)) not in [''.join(map(str,i)) for i in newList]:
        newList.append(subList)

print(newList)

