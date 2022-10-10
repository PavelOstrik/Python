# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
# 1 2 3 5 6 7 8 => 4


import random

list = [i for i in range(1,10)]

# list.pop(random.randrange(len(list)))
list.pop(random.randint(2, len(list) - 1))

print(list)

found = 0
for i in range(1, len(list) + 1):
    if list[i] -1 != list[i - 1]:
        found = list[i] -1
        list.insert(i, found)

print(list)
print(found)
