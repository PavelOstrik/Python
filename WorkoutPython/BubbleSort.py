arr = []
for i in range(int(input('Введите размер списка: '))):
    arr.insert(i, int(input('Введите элемент списка: ')))
print(arr)

for i in range(len(arr)):    
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:    
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print('Sorted array')
for i in range(len(arr)):
    print(arr[i], end = ', ')
    
