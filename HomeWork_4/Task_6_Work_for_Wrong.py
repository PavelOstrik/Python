# Разбираем 4 и 5 задачу
from distutils.command.build_scripts import first_line_re
from random import randint as rI

def creatCoef():  # функция создавать коэффициенты
    coef = {}    
    degree = int(input('Введите максимальную степень: '))

    for i in range(degree, -1, -1): 
        coef[i] = rI(-20,20)    # coef[i] - значение ключа, присваиваем ему значение 

    return coef

# coefEquation = creatCoef()
# print(coefEquation) # {9: 11, 8: -14, 7: -12, 6: 16, 5: 1, 4: 15, 3: 8, 2: -18, 1: -7, 0: -14}
# Задокументированные уравнения всегда будут разными, так как работает генератор сл чисел

def creatEquation(coefEquation: dict): # :dict просто помечаем что это словарь

    equation = ''

    first = True

    # Заполняем нашу строку чтобы получить уравнение
    # Коэффициенты у нас находятся в значениях, степени в ключях
    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])  
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])  
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])
        # переводим в строку, так как int не склеивается
        # чтобы не получить ситуации, когда плюс стоит перед минусом, вводим условие
        # и значение = коэффициент меняем на положительное фун-ией abs

    return(equation + ' = 0')
# + 15x^9 + 6x^7 - 1x^6 + 10x^5 + 8x^4 - 13x^3 - 18x^2 + 11x^1 - 5x^0
# Как убрать первый плюс, для этого мы создаем перменную first = True
# В цикл добавляем условие if first: 
# и после первого срабатывания его меняем на first = False, чтобы больше он
# не срабатывал

def parseEquation(equation: str):  # str пишем просто как пояснение    

    # Теперь нам надо обратно развернуть наше уравнение в словарь
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    # делаем так, чтобы каждый элемент уравнения смотрелся отдельным членом, и мы 
    # могли разбить по split
    # print(equation)
    # 9x^9 -2x^8 +18x^7 -5x^6 +2x^5 -17x^4 -8x^3 +2x^2 +8x^1 +9x^0 = 0
    equation = equation.split()  # По умолчанию разделение идет по пробелу
    # print(equation) 
    # ['9x^9', '-2x^8', '+18x^7', '-5x^6', '+2x^5', '-17x^4', '-8x^3', '+2x^2', '+8x^1', '+9x^0', '=', '0']
    equation = equation[:-2]
    # Срез нашего списка чтобы убрать 2 последних элемента  ['='], ['0']
    dictEquation = {}

    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^', )
        print(equation[i])
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    # Сплитим по x^ и убираем все плюсы
    # Присваиваем в словаре значению ключа коэффициенты из нашего списка

    return dictEquation

equation1 = creatEquation(creatCoef())
print(equation1)
# 16x^9 - 10x^8 - 15x^7 + 4x^6 - 12x^5 + 18x^4 - 19x^3 - 15x^2 - 20x^1 + 20x^0 = 0
equation2 = creatEquation(creatCoef())
print(equation2)
#  -3x^9 - 12x^8 + 5x^7 - 12x^6 - 8x^5 + 2x^4 + 3x^3 - 19x^2 - 9x^1 - 3x^0 = 0

parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)
# print(parEq1)
# {9: -12, 8: -14, 7: 12, 6: -16, 5: 15, 4: 19, 3: 15, 2: 5, 1: -3, 0: 2}
# print(parEq2)
# {9: 17, 8: -20, 7: 15, 6: 13, 5: 9, 4: 5, 3: 20, 2: 6, 1: -15, 0: -15}

# Теперь мы складываем 2 словара

resultEquation = {}
for i in range(max(len(parEq1), len(parEq2)), -1, -1):
# Мы выбираем максимальную длину из длин наших словарей
# -1, -1 пишем чтобы перебор шел от последнего элемента до 0, переворачиваем
    first = parEq1.get(i) 
    # Мы берем первое значение по ключу нашего 1 словаря и кладем его в first
    # 9: -12 ключ 9 значение -12
    second = parEq2.get(i)
    # Мы берем первое значение по ключу нашего 2 словаря и кладем его в second
    # 9: 17 ключ 9 значение -17
    # Если такого ключа нет, он нам выдаст None
    if first != None or second != None:
    # Здесь мы делаем проверку, если первое значение не равняется None или второе не равняется None
    # Если ключей нет в обоих словарях, то мы просто пропускаем этот шаг
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)
        # Если первое не None, то мы берем его значение, если оно равно None, то мы берем 0
        # Почему 0, потому что мы будем складывать получать новый коэффициент нашей степени

print(resultEquation)
# {9: 15, 8: 15, 7: 8, 5: 4, 4: -12, 3: -18, 2: 5, 1: 3, 0: -5}
# {9: -1, 8: 1, 6: 17, 5: -20, 4: -12, 3: 9, 2: 1, 1: -5, 0: -13}
# {9: 14, 8: 16, 7: 8, 6: 17, 5: -16, 4: -24, 3: -9, 2: 6, 1: -2, 0: -18}

# И создаем из суммарного словаря полноценное уравнение
# print(creatEquation(resultEquation))
# -4x^9 - 16x^8 - 16x^7 - 15x^6 - 9x^5 + 7x^4 + 2x^3 - 30x^2 - 17x^1 + 17x^0 = 0

# Можно создать свой отдельный метод для красивой печати

def printEquation(equation: str):
    print(equation.replace(' 1x', 'x').replace('x^1', 'x').replace('x^0', ''))

  
printEquation(creatEquation(resultEquation))
