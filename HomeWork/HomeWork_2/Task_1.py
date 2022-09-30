# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# 1 способ
number = float(input('Введите вещественное число: '))
sum = 0
print(f'Сумма цифр числа {number}:')

while number != int(number):
    number = int(number * 1000)

while number != 0:
    sum += number % 10
    number = number // 10

print(sum)

# 2 способ
number = input('Введите вещественное число: ')
sum = 0
for i in number:
    if i != '.':
        sum += int(i)
print(sum)

# 3 способ
number = float(input('Введите вещественное число: '))
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print(sum)

# 4 способ
number = float(input('Введите вещественное число: '))
sum = 0
number = abs(number)


def digit_after_dot_counter(number: float):
    count = 0
    div = 1
    while True:
        if not (number*div == int(number*div)):
            count += 1
            div *= 10
        else:
            break
    return count


print(number * pow(10**digit_after_dot_counter(number)))

while number > 0:
    sum += number % 10
    number //= 10

print(sum)

# 5 способ
def float_to_completed_integer(real_number: float) -> int:
    magnitude = int(1)
    temp = float(real_number)
    while not temp.is_integer():
        magnitude *= 10
        temp = real_number * magnitude
    return int(temp)

def get_digits_sum(any_number):
    no_point_number = float_to_completed_integer(any_number)
    no_point_number = abs(no_point_number)
    sum = 0
    while no_point_number > 0:
        sum += no_point_number % 10
        no_point_number //= 10
    return sum

print(get_digits_sum(123.456789))
