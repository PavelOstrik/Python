
# Просто как демонстрация импорт нескольких методов
from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


# Опишем метод, который будет собирать информацию со всех датчиков
# и отдавать их одной порцией  
def new_create(data, device = 1):  # device = 1 пишем в качестве демонстрации
    t, p, w = data
    style = 'style="font-size:22px;"' # Здесь описываем стиль и какой мы хотим видеть шрифт
    html = '<html>\n  <head></head>\n <body>\n' # представление для html
    html += '    <p {}> Temperature: {} c</p>\n'\
        .format(style, t)
    html += '    <p {}> Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}> Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '    </body>\n</html>'

    with open(r'Lection_4_jion_job\new_index.html', 'w') as page:
        page.write(html)
    
    return data    

# Далее описываем то, что будет генерировать наш HTML файл

def create(device = 1):  # device = 1 пишем в качестве демонстрации
    style = 'style="font-size:22px;"' # Здесь описываем стиль и какой мы хотим видеть шрифт
    html = '<html>\n  <head></head>\n <body>\n' # представление для html
    html += '    <p {}> Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}> Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '    <p {}> Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '    </body>\n</html>'

    with open(r'Lection_4_jion_job\index.html', 'w') as page:
        page.write(html)
    
    return html

