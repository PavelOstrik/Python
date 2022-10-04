# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

with open('file2.txt', 'w') as file:
    file.write('2*x**2 + 4*x + 2 = 0')

path = 'file2.txt'
with open(path) as file:

    equation = file.readline()
    print(equation)

list = equation.split(' + ')
print(list)

a = int(list[0][0])
b = int(list[1][0])
c = int(list[2][0])

# # 1 способ
# newList = []
# for i in range(len(list)):
#     list[i] = list[i].split('*',1)[0]
#     if list[i] != '+' and list[i] != '=' and list[i] != '0':
#         newList.append(list[i])
# print(newList)

# a = int(newList[0])
# b = int(newList[1])
# c = int(newList[2])

# Ax**2 + Bx + C = 0
# D = b**2 - 4ac

D = b**2 - 4*a*c
print(f'Дискриминант равен {D}')
result = ''

if D > 0:
    x1 = (-b - D*0.5) / (2*a)
    x2 = (-b + D*0.5) / (2*a)
    print(f'Первый корень равен {x1}, второй корень равен {x2}')
    result = f'Первый корень равен {x1}, второй корень равен {x2}'    
elif D == 0:
    x = -b / (2*a)
    print(f'Имеем единственный корень (или два равных корня) равный {x}')
    result = f'Имеем единственный корень (или два равных корня) равный {x}'    
else:
    print('Действительных корней нет')
    result = 'Действительных корней нет'    

with open('file2_1.txt', 'w', encoding='UTF-8') as file2_1:
    file2_1.write(result)

