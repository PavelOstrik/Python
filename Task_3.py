#  1. Напишите программу, которая будет на вход принимать число N и выводить
#  числа от -N до N
#  *Примеры:*
#  - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number = int(input('Введите число: '))

if number < 0:
    number = number * (-1)

#1 способ
for i in range(-number, number + 1):
    print(i, end = ', ')

print()
#2 способ
numbers = list(range(-number, number + 1))
print(numbers)

print()
#3 способ через метод
def list_of_numbers(x):
    list = []
    for i in range(-x, x):
        list.append(i)
    return list

number = int(input('Введите число: '))

x = list_of_numbers(number)
print(x)







