# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите десятичное число: '))

div = 2
numberBinary = []
while number > 0:
    result = number % div
    number = number // div  
    numberBinary.append(result)

print('Получите двоичное число: ')
for i in range(len(numberBinary)-1, -1, -1):
    print(numberBinary[i], end='')

