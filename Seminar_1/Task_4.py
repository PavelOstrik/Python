#  2. Напишите программу, которая будет принимать на вход дробь и показывать
#  первую цифру дробной части числа.
#  *Примеры:*
#  - 6,78 -> 7
#  - 5 -> нет
#  - 0,34 -> 3

number = float(input('Введите дробное число:  '))

if number % 1 != 0:
    result = int(number * 10 % 10)
    print(result)
else: print('Вы ввели не вещественное число')

#Еще одна проверка на дробное число
number = float(input('Введите дробное число:  '))

if number == int(number):
    print('Целое')
else: print('Дробное')
