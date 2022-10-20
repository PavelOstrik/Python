
# Блок отвечающий за вывод данных
# В этом модуле пишем все, что будет взаимодействовать с пользователем
def input_value(string: str):
    while True:
        try:   # Проверка на дурака от ввода не целого числа
            value = int(input(string))
            return value
        except:
            print('Ошибка ввода')

def print_values(variable: int):
    print(variable)
