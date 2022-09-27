# Задача: Найдите наибольшее число в списке.

def max(list):
    if len(list) == 2:
        if list[0] > list[1]: 
            return list[0]
        else: return list[1]

    sub_max = max(list[1:])

    if list[0] > sub_max:
        return list[0]
    else: return sub_max

numbers = list(range(5))
print(numbers)
print(max(numbers))