# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

# Я не знаю, как ты будешь в этом разбираться, но это работает :)

from dataclasses import replace

def itsMagic(str):
    str = str.replace(' - ', ' -')
    str = str.replace(' + ', ' +')
    str = str.replace(' = 0', '')
    str = str.replace('*', '')
    # print(str)

    list = str.split(' ')
    # print(list)
    for i in range(len(list)):
        if 'x' not in list[i]:
            nakedNumber = list[i]
            list.remove(list[i])

    nakedNumber = int(nakedNumber.replace('+', ''))
    # print(nakedNumber)

    listRatio = []
    listDegree = []
    newList = []
    for i in range(len(list)):
        newList.append(list[i].split('x')) 
        

    # print(newList)

    for i in range(len(newList)):
        listRatio.append(newList[i][0]) 
        listDegree.append(newList[i][1])

    # print(listRatio)
    # print(listDegree)

    if i in range(len(listRatio)):    
        if len(listRatio[i]) == 1:        
            if '+' in listRatio[i]:
                listRatio[i] = listRatio[i].replace('+', '1')
            if '-' in listRatio[i]:
                listRatio[i] = listRatio[i].replace('-', '-1')    
        
    for i in range(len(listRatio)):
        listRatio[i] = listRatio[i].replace('+', '')

    # print(listRatio)
    # print(listDegree)

    listRatio = [int(i) for i in listRatio]
    listDegree = [int(i) for i in listDegree]
    # print(listRatio)
    # print(listDegree)

    dictionary = dict(zip(listDegree, listRatio))
    dictionary[0] = nakedNumber
    # print(dictionary)
    return dictionary

with open(r'HomeWork_4\firstFile.txt', 'w') as file:
    file.write('23*x**9 - 16*x**8 + 3*x**7 + 15*x**4 - 2*x**3 + x**2 + 20 = 0')
with open(r'HomeWork_4\SecondFile.txt', 'w') as file:
    file.write('17x**9 + 15x**8 - 8x**7 + 15x**6 - 10x**4 + 7x**3 - 13x**1 + 33 = 0')

path_first = r'HomeWork_4\firstFile.txt'
path_second = r'HomeWork_4\SecondFile.txt'

with open(path_first) as file:
    polynomial_first = file.readline()

with open(path_second) as file:
    polynomial_second = file.readline()

print(polynomial_first)
print(polynomial_second)

first = itsMagic(polynomial_first)
second = itsMagic(polynomial_second)   

# print(first)
# print(second)

sum_keys = set(first.keys()).union(set(second.keys()))
sum_dict = {}

for key in sum_keys:
    values1 = first.get(key)
    values2 = second.get(key)
    if values1 == None:
        sum_values = values2
    elif values2 == None:
        sum_values = values1
    else:
        sum_values = values1 + values2
    sum_dict[key] = sum_values

print(sum_dict)

keys = sum_dict.keys()
values = sum_dict.values()

# print(keys)
# print(values)

keys = [str(i) for i in keys]
values = [str(i) for i in values]

polynomial_result = ''

for i in range(len(keys) - 1, -1, -1):
    polynomial_result += values[i] + '*x**' + keys[i] + ' '

polynomial_result = polynomial_result.replace(' ', ' + ')
polynomial_result = polynomial_result.replace('+ -', '- ')
polynomial_result = polynomial_result.replace('*x**0 +', ' = 0')


print(polynomial_result)

with open(r'HomeWork_4\finalFile.txt', 'w') as file:
    file.write(polynomial_result)

    

