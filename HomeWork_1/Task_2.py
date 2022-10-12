# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            first_statement = not(x and y and z )
            second_statement = not x or not y or not z
            if first_statement == second_statement: print(f'Утверждение истинно при x = {x}, y = {y}, z = {z}')
            else: print(f'Утверждение ложно при x = {x}, y = {y}, z = {z}')

# 2 способ записи
trigger = True

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:            
            if not(x and y and z ) != (not x or not y or not z): 
                print('Не верно')
                trigger = False
                break

if trigger: print('Всегда верно')

