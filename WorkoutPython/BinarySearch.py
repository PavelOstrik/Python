from mimetypes import guess_all_extensions
from tkinter.messagebox import NO


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(2,11))
print(my_list)
print(binary_search(my_list, 5))
