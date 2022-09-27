# Задача: Напишите рекурсивную функцию для подсчета элементов в списке.

def count_list_element(list):
    count = 1
    if list == []: 
        return 0
    return 1 + count_list_element(list[1:])

numbers = list(range(5))
print(numbers)
print(count_list_element(numbers))    