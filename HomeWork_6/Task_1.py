# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce
import random

n = int(input('Введите количество элементов списка: '))
    
# Исполльзуем ListComprehension
mylist = [random.randint(0, 9) for _ in range(0, n)]

print(mylist)

# sum = 0
# count = 0
# for i in range(1,n,2):
#     sum += mylist[i]
#     count += 1
#     print(f'Элемент на {count} нечетной позиции, индекс: [{i}] = {mylist[i]}')
   
# print(f'Сумма элементов списка, стоящих на нечётных позициях = {sum}')

mylist = list(filter(lambda i: i[0] % 2, list(enumerate(mylist))))
print(mylist)
print(f'Сумма элементов на нечетных позициях = {sum(list(map(lambda x: x[1], mylist)))}')
print(f'Сумма элементов на нечетных позициях = {reduce(lambda x,y: x[1] + y[1], mylist)}')
