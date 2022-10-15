# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.
# Use comprehension

myList = [i for i in range(20, int(input('N = '))+1) if i % 20 == 0 or i % 21 == 0]
f_myList = list(filter(lambda x: not x%20 or not x%21, (i for i in range(20, int(input('N = '))+1))))

print(myList)
print(f_myList)
