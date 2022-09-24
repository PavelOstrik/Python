# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))

first_statement = not(x and y and z )
second_statement = not x or not y or not z

if first_statement == second_statement: print('Утверждение истинно')
else: print('Утверждение ложно')