# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК(наименьшее общее кратное)
# НОК - наименьшее натуральное число, которое делится на m и n без остатка

#Мой вариант решения
firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))

if firstNumber % secondNumber == 0:
    print(f'Наименьшее общее кратное для чисел {firstNumber} и {secondNumber} = {firstNumber}')
elif secondNumber % firstNumber == 0:
    print(f'Наименьшее общее кратное для чисел {firstNumber} и {secondNumber} = {secondNumber}')
else:
    for i in range(1,1000):
        if i % firstNumber == 0 and i % secondNumber == 0:
            print(f'Наименьшее общее кратное для чисел {firstNumber} и {secondNumber} = {i}')
            break

# Решение Кирилла

m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))

i = 1

while (min(m,n) * i) % max(m,n):
    i += 1

print(f'Наименьшее общее кратное для чисел {m} и {n} = {min(m,n) * i}')






