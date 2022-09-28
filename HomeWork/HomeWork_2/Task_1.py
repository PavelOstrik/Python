# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = float(input('Введите вещественное число: '))
sum = 0
print(f'Сумма цифр числа {number}:')

while number != int(number):
        number = int(number * 1000)        

while number != 0:
    sum += number % 10
    number = number // 10    

print(sum)

