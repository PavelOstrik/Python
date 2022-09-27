# Через методы
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

list = []
for i in range(0, 5):
    list.append(int(input('Введите элемент списка: ')))
print(list)
print(selectionSort(list))

#Через циклы
arr = []
for i in range(0, 5):
    arr.append(int(input('Введите элемент списка: ')))
print(arr)

for i in range(len(arr)):
    min_ind = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_ind]:
            min_ind = j

    arr[i], arr[min_ind] = arr[min_ind], arr[i]

print('Sorted array')
for i in range(len(arr)):
    print(arr[i], end = ', ')



    