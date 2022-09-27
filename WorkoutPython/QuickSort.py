def quick_sort(array):
    left = []
    right = []
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i <= pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)

        return quick_sort(left) + [pivot] + quick_sort(right)


array = {10, 5, 2, 3, 4, 10, 15, 0, 20}
print(quick_sort(array))
