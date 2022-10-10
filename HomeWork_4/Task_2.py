# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
N = n
if N == 1:
    print(N)

list = []
d = 2
while N > 1:        
    if N % d == 0:
        list.append(d)
        N //= d
    else:
        d += 1
print(list)

# for i in range(len(list)):
#     list[i] = str(list[i])
    
list = [str(i) for i in list]
print(list)

result = ' x '.join(list)
print(f'Список простых множителей числа {n} = {result}')
