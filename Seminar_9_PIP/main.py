import random

# Получаем список списков
list_of_list = []

for i in range(5):
    new = []
    for k in range(5):
        new.append(str(random.randint(0,10))) # Переводим в строку, чтобы потом склеить
    list_of_list.append(new)

print(list_of_list)
# [['7', '1', '2', '2', '10'], ['7', '3', '5', '8', '7'], ['2', '5', '9', '6', '0'], ['6', '9', '8', '5', '7'], ['10', '6', '1', '4', '5']]

# Получаем список строк
for index, item in enumerate(list_of_list):
    list_of_list[index] = ';'.join(item)
    print(item) # вывести элементы списка, каждый в отдельной строке

print(list_of_list)
# ['7;1;2;2;10', '7;3;5;8;7', '2;5;9;6;0', '6;9;8;5;7', '10;6;1;4;5']

# Раскрыть список
print(*list_of_list)
# 0;3;4;2;1 5;2;9;8;8 10;7;9;2;7 4;8;9;0;6 10;7;7;0;2

# # Вывод всех элементов одной строкой
# list_of_list = ';'.join(list_of_list)
# print(list_of_list)

# Вывод элементов построчно
list_of_list = '\n'.join(list_of_list)
print(list_of_list)