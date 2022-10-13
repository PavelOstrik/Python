# Связующий модуль между model и view

# import model
# Если мы хотим поменять модуль, то мы просто импортируем его вместо предыдущего
import model_sub as model
import view

# Здесь мы опишем функцию "кнопку", которую будет нажимать пользователь

def button_click():
    value_a = view.get_value() # Метод получения значений из view
    value_b = view.get_value()
    model.init(value_a, value_b) # Инициализируем входные данные нашей модели
    # result = model.sum() 
    # result = model.mult()  # Поменяли функцию sum на mult
    result = model.do_it()   # Дали общее название операциям, ради более общего вывода
    view.view_data(result, 'result') # возвращаем результат и имя операции

