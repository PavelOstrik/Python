# Предоставлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension

from random import randint as rI

myList = [rI(1,9) for _ in range(int(input('Введите количество элементов списка: ')))]
print(myList)
new_myList = [myList[i] for i in range(1, len(myList)) if myList[i] > myList[i -1]]
res_list = [number for i, number in enumerate(myList) if i > 0 and myList[i] > myList[i - 1]]
z_list = [num1 for num1, num2 in zip(myList[1:], myList[:-1]) if num1 > num2]
print(new_myList)
print(res_list)
print(z_list)
print(list(zip(myList[1:], myList[:-1])))
print(list(zip(myList[1:])))
print(list(zip(myList[:-1])))
