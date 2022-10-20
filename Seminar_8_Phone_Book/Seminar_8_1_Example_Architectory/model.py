# Блок отвечающий за ввод данных

a = 0
b = 0

def set_value_a(variable: int):
    global a
    a = variable

def set_value_b(variable: int):
    global b
    b = variable

def get_value_a():
    global a
    return a

def get_value_b():
    global b
    return b