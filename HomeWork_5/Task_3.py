# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


from random import randint as rI
from unittest.mock import patch

def Compressed(list: str):
    newList = ''
    count = 0
    found = list[0]
    for i in range(len(list)):
        
        if found == list[i] and i < len(list)-1:
            count += 1
        elif i == len(list)-1:
            newList += str(count+1) + found
        else:
            newList += str(count) + found
            count = 1
            found = list[i]
    return newList

def Unpacked(list: str):
    newList = ''
    multi = ''
    for i in range(len(list)):
        if list[i].isdigit():
            multi += list[i]            
        else:        
            newList += int(multi) * list[i]
            multi = ''
    
    return newList


list = rI(1,9)*'a' + rI(1,9)*'b' + rI(1,9)*'c'

listCompressed = str(rI(1,9)) + 'a' + str(rI(1,9)) + 'b' + str(rI(1,9)) + 'c'

with open(r'HomeWork_5\Input.txt', 'w') as file:
    file.write(list + '\n')
    file.write(listCompressed + '\n')

path = r'HomeWork_5\Input.txt'
with open(path) as file:
    listIn = file.readline().replace('\n','')
    listCompressedIn = file.readline().replace('\n','')


print(listIn)
print(Compressed(listIn))

print(listCompressedIn)
print(Unpacked(listCompressedIn))


with open(r'HomeWork_5\Output.txt', 'w') as file:
    file.write(Compressed(listIn) + '\n')
    file.write(Unpacked(listCompressedIn) + '\n')



  









