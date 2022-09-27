# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

first_string = str(input('Введите 1 строку: '))
second_string = str(input('Введите 2 строку: '))

count = 0
for i in range(len(second_string) + 1):
    l = len(first_string) + i
    if first_string == second_string[i:l]:
        count += 1

print(count)

# 2 способ, красива запись через метод

str_sub = input('Введите 1 строку: ')
str_src = input('Введите 2 строку: ')

def count_substrings(source, substr):
    len_substr = len(substr)
    len_source = len(source)
    i = 0
    for iend in range( len_substr, len_source + 1):
        if source[iend - len_substr : iend] == substr:
            i += 1
    return i

print(f'Число вхождений строки "{str_sub}" в строку "{str_src}" = ', count_substrings(str_src, str_sub))


# 3 способ

first_string = input('Введите 1 строку: ')
second_string = input('Введите 2 строку: ')

string = ''
subString = ''

if len(first_string) > len(second_string):
    string = first_string
    subString = second_string
else:
    string = second_string
    subString = first_string

print(string.count(subString))

# 4 способ

count = 0
counter = 0

for i in range(len(string) - len(subString) + 1):
    if string[i] == subString[0]:
        counterIn = 0
        for k in range(len(subString)):
            if subString[0+k] == string[i+k]:
                counterIn += 1
        if counterIn == len(subString):
            counter += 1

print(f'Counter = {counter}')


