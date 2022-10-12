# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *. Приоритет опреаций стандартный.

# Пример:
# '2 + 2' => 4
# '1 + 2 + 3' => 7
# '1 - 2 * 3' => -5

from tkinter.tix import Tree


string = input('Введите уравнение: ')
print(string)

string = string.replace(' ', '').strip()
string = string.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
string = string.split()

def deleteElement(string, i):
    string.pop(i+1)
    string.pop(i)

print('Изначальное выражение: ')
print(string)

while len(string) > 1:
    if '*' in string or '/' in string:
        for i in range(len(string)):
            if string[i] == '*':
                print('Умножение')
                string[i-1] = int(string[i-1]) * int(string[i+1])
                deleteElement(string, i)
                print(string)
                break
            if string[i] == '/':
                print('Деление')
                string[i-1] = int(string[i-1]) / int(string[i+1])
                deleteElement(string, i)
                print(string)
                break
    elif '+' in string or '-' in string:
        for i in range(len(string)):
            if string[i] == '+':
                print('Сложение')
                string[i-1] = int(string[i-1]) + int(string[i+1])
                deleteElement(string, i)
                print(string)
                break
            if string[i] == '-':
                print('Вычитание')
                string[i-1] = int(string[i-1]) - int(string[i+1])
                deleteElement(string, i)
                print(string)
                break 


# 2 вариант через lambda

string = input('Введите уравнение: ')
print(string)

opSelect = {'*': lambda x, y: int(x) * int(y),
'/': lambda x, y: int(x) / int(y),
'+': lambda x, y: int(x) + int(y),
'-': lambda x, y: int(x) - int(y)}

string = string.replace(' ', '').strip()
string = string.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
string = string.split()

def deleteElement(string, i):
    string.pop(i+1)
    string.pop(i)

def operation(string, i, oper):
    if string[i] == oper:
        string[i-1] = opSelect.get(oper)(int(string[i-1]), int(string[i+1]))
        deleteElement(string, i)
        print(string)
        return True

print('Изначальное выражение: ')
print(string)     

while len(string) > 1:
    if '*' in string or '/' in string:
        for i in range(len(string)):
            if operation(string, i, '*'): break
            if operation(string, i, '/'): break

    elif '+' in string or '-' in string:
        for i in range(len(string)): 
            if operation(string, i, '+'): break
            if operation(string, i, '-'): break






