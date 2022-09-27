# 2. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# o Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def dictionary(N):
    array = {}
    
    for i in range(1, N + 1):
        array[i] = 3 * i + 1

    return array

N = int(input('Введите число: '))
array = dictionary(N)
print(array)