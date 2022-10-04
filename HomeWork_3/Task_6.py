# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.

import time



def random(n, min, max):
    list =[]

    for i in range(1, n+1):
        l = len(str(max))
        x = round(i+time.time() * 10 ** 10 % 10 ** l)

        while x > max or x < min:
            x = round(i+time.time() * 10 ** 10 % 10 ** l)

        if i % 2 == 0 and x > min:
            list.append(-x)
        else:
            list.append(x)

    return list

result_list = random(9, -200, 500)
print(result_list)