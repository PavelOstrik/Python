# Напишите программу, удаляющую из текста все слова, содержащие 'абв'.

path = r'Seminar_5\Pushkin.txt' 
list = []
with open(path, encoding="utf-8") as file:
    list = file.read().split()

print(list)

findTxt = input()

newList = []
for word in list:
    if findTxt not in word:
        newList.append(word)
      
print(' '.join(newList))
newList = ' '.join(newList)

with open(r'Seminar_5\Pushkin1.txt', 'w', encoding="utf-8") as file:
    file.write(newList)


