# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию
# степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random


k = int(input('Задайте натуральную степень: '))

listRatio = []

for i in range(k):
    listRatio.append(random.randint(0,100))

print(f'{listRatio}  Список коэффициентов') 

listDegree = []

for i in range(k, 0, -1):
    listDegree.append(i)

print(f'{listDegree}  Список степеней')


listRatio = [str(i) for i in listRatio]
listDegree = [str(i) for i in listDegree]

listResult = []
for i in range(len(listRatio)):
    if listRatio[i] != '0':
        if listDegree[i] == '1':
            listResult.append(listRatio[i] + 'x')   
        else:     
            listResult.append(listRatio[i] + 'x**' + listDegree[i])
    
    
print(f'{listResult}  Список элементов нашего многочлена')

sign = [' + ', ' - ']
result = ''
for i in range(len(listResult)):
    if i != len(listResult) - 1:
        result += listResult[i] + random.choice(sign)
    else:
        result += listResult[i] + ' = 0'

print(f'{result}  Встречайте, наш многочлен, тарам парам пам')

with open(r'HomeWork_4\HomeWork_4_Task_4.txt', 'w') as file:
    file.write(result)

    









