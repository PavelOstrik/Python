# Задайте строку из набора чисел в отдельном файле. Напишите программу,
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
# покажите мин и макс числа в отдельных файлах


# моё решение
from random import randint



path = "file1.txt"
with open(path) as file1:

    for line in file1:
        if line != '':
            numbers = line.split()
    print(numbers)

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(numbers)

    maxElement = numbers[0]
    minElement = numbers[0]

    for i in range(len(numbers)):

        if numbers[i] > maxElement:
            maxElement = numbers[i]

        if numbers[i] < minElement:
            minElement = numbers[i]
    print(f'Минимальный элемент: {minElement}')
    print(f'Максимальный элемент: {maxElement}')

with open('fileMin.txt', 'w') as fileMin:
    fileMin.write(str(minElement))

with open('fileMax.txt', 'w') as fileMax:
    fileMax.write(str(maxElement))

# 2 способ
def createList(list):
    list = []
    for i in range(list):
        list.append(randint(0,999))
    return list

def createLine(list):
    line = ''
    for i in range(len(list)):
        line += str(list[i]) + ''
    return line

with open('from.txt', 'w') as f:
    f.write(createLine(createList(10)))

readedLine = ''
with open ('from.txt', 'r') as f:
    readedLine = f.readline()
print(readedLine)

line = readedLine.split(' ')
print(line)

minI = 0
maxI = 0

for i in range(len(line)):
    if int(line[i] < int(line[minI])):
        minI = i
    if int(line[i] > int(line[maxI])):
        maxI = i

print(str(line[minI]) + ' ' + str(line[maxI]))

with open('newfile.txt', 'w') as f:
    f.write(str(line[minI]) + '\n')
    f.write(str(line[maxI]) + '\n')

# 3 способ
numbers = []
read:str
with open('1file.txt', 'r') as file:
    read = file.readline()

list = read.split(' ')
for i in list:
    numbers.append(int(i))

print(numbers)
maximum = max(numbers)
minimum = min(numbers)

with open('3file.txt', 'w') as file:
    m = file.write(f'{maximum} {minimum}' )




        
    
