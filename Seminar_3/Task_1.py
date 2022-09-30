# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# 1 способ
from turtle import position


num = input('Введите искомое число: ')
list = ['adsdkn46dg', 'dsf56ll4', 'qqqqq', '12lfkmdm444']

positionList = []

for i in range(len(list)):
    if num in list[i]:
        positionList.append(i)

print(positionList)

# 2 способ
num = input('Введите искомое число: ')
list = ['adsdkn46dg', 'dsf56ll4', 'qqqqq', '12lfkmdm444']

listOsIndex = []
for i in range(len(list)):
    if list[i].find(num) != -1:
        listOsIndex.append(i)

if len(listOsIndex) > 0:
    print(f'Элементы с индексом {listOsIndex} содержат символ {num}')
else:
    print(f'Элементы списка не сожержат символ {num}')


# 3 способ
num = int(input('Введите искомое число: '))

lst_str = ['adsdkn46dg', 'dsf56ll4', 'qqqqq', '12lfkmdm444']

def find_index(lst,number):
    number_str = str(number)
    i = 0
    while i < len(lst):
        if (lst(i).find(number_str) != -1):
            return 1
        i += 1
    return -1

idx = find_index(lst_str, num)
if idx >= 0:
    print(
        f'Искомое число {num} найдено в строке "{lst_str(idx)}" (номер строки в списке {idx+1})')
else:
    print(f'Искомого числа {num} нет в исходном списке')




