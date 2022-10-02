# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



from operator import neg


def fibonacci(n):    
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Fn = F(n+2)−F(n+1)

def negativeFibonacci(n):
    if n in [-1]:
        return 1
    if n in [-2]:
        return -1
    else: 
        return negativeFibonacci(n+2) - negativeFibonacci(n+1)
        

n = int(input('Введите число: '))
nNegative = - n

listFibonacci = []    

for n in range(1, n + 1):
    listFibonacci.append(fibonacci(n))

print(f'Список чисел Фибоначчи для числа {n}:')
print(listFibonacci)  

listNegativeFibonacci = []

for nNegative in range(-1, nNegative - 1, -1):
    listNegativeFibonacci.append(negativeFibonacci(nNegative))

print(f'Список чисел Фибоначчи для числа {nNegative}:')    
print(listNegativeFibonacci)

listNegativeFibonacciReverse = []

for i in range(len(listNegativeFibonacci) - 1, -1, -1):     
    listNegativeFibonacciReverse.append(listNegativeFibonacci[i])  

print(f'Перевернутый список чисел Фибоначчи для числа {nNegative}:')    
print(listNegativeFibonacciReverse)

listZero = [0]
print(f'Список чисел Фибоначчидля числа {n} , в том числе для отрицательных индексов: ')
print(listNegativeFibonacciReverse + listZero + listFibonacci)
