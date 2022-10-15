# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

import random


n = int(input('Введите натуральное число: '))
N = n
if N == 1:
    print(N)

myList = []
d = 2
while N > 1:        
    if N % d == 0:
        myList.append(d)
        N //= d
    else:
        d += 1
print(myList)

# for i in range(len(myList)):
#     myList[i] = str(myList[i])

# Используем ListComprehension и map
# 1 вариант    
# myList = [str(i) for i in myList]
# 2 вариант
myList = list(map(str,myList))
print(myList)

result = ' x '.join(myList)
print(f'Список простых множителей числа {n} = {result}')