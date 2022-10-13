# Опишем еще один модуль отвечающий за xml представление
# Данные xml часто используют, если надо передать данные от клиента серверу
# и наоборот

from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

# Далее описываем то, что будет генерировать наш xml файл

def new_create(data, device = 1):  # device = 1 пишем в качестве демонстрации
    t, p, w = data
    t = t * 1.8 + 32 # Чтобы цельсии представить в виде Фаренгейта
    xml = '<xml>\n'    
    xml += '    <temperature units = "f">{}>/temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}>/wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure_view units = "mmHg">{}>/pressure_view>\n'\
        .format(p)
    xml += '</xml>'

    with open(r'Lection_4_jion_job\new_data.xml', 'w') as page:
        page.write(xml)
    
    return data

    

# Опишем метод, который будет собирать информацию со всех датчиков
# и отдавать их одной порцией  

def create(device = 1):  # device = 1 пишем в качестве демонстрации
    xml = '<xml>\n'    
    xml += '    <temperature units = "c">{}>/temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}>/wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure_view units = "mmHg">{}>/pressure_view>\n'\
        .format(pressure_view(device))
    xml += '</xml>'

    with open(r'Lection_4_jion_job\data.xml', 'w') as page:
        page.write(xml)
    
    return xml