from Seminar_8_1 import view, model

# Метод получения данных
def set_value():
    a = view.input_value('Введите число: ')
    b = view.input_value('Введите число: ')
    model.set_value_a(a)
    model.set_value_b(b)

def print_values():
    view.print_values(model.get_value_a())
    view.print_values(model.get_value_b())