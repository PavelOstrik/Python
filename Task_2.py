# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#         Примеры:    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


numbers = []

# 1 сособо получения списка
# for i in range(0,5):
#     numbers.insert(i, int(input(f'Введите число: ')))

# 2 способ получения списка
for i in range(0,5):
    numbers.append(int(input(f'Введите число: ')))

print(numbers)

# Получаем максимальное число с помощью функции max
# print(max(nambers))

max = numbers[0]
for i in range(1,5):
    if numbers[i] > max: max = numbers[i]
print(f'Максимальный элемент списка: {max}')

# Решение через методы
def array(m):
    x = []
    for i in range(m):
        a = int(input(f'Введите x{i + 1}: '))
        x.append(a)

    return x

def max_el(array):
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = i

    return array(max)
l = int(input('Введите кол-во элементов: '))
new_array = array(l)
max = max_el(new_array)
print(f'Максимальный элемент списка: {max}')