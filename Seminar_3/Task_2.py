# Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

list1 = ["123", "234", 123, "567"]

x = '123'

count = 0

for i in range(len(list1)):
    if str(list1(i)) == x:
        count += 1

    if count == 2:
        print(i)
        break
else:
    if count == 0:
        print('Нет вхождения')
    else:
        print('Нет второго вхождения')