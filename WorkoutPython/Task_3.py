# Задача 12: Напишите программу, которая будет принимать на вход два числа и выводить,
# является ли второе число кратным первому. Если число 2 не кратно числу 1,
# то программа выводит остаток от деления.
# 34, 5 -> не кратно, остаток 4
# 16, 4 -> кратно

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

if first_number % second_number == 0:
    print(f'Число {second_number} кратно {first_number}')
else: print(f'Число {second_number} НЕ кратно {first_number}, остаток от деления: {first_number % second_number}')