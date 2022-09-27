# Задача: Имеется массив чисел. Нужно просуммировать все числа и вернуть сумму.

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

numbers = list(range(5))
print(numbers)
print(sum(numbers))

