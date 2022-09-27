# Напишите программу, которая выводит случайное число из отрезка [10, 99]
# и показывает наибольшую цифру числа.
# 78 -> 8 
# 12-> 2 
# 85 -> 8

import random 

number = random.randint(10,99)
print(number)
a = number // 10
b = number % 10

if a > b: print(a)
else: print(b)



