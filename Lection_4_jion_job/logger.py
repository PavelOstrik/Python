# Как только дело касается какого то логирования данных
# нам необходимо использовать:
from datetime import datetime as dt


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'Lection_4_jion_job\log.csv', 'a') as file:
        file.write('{};Temperature;{}\n'.format(time, data))
    
def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'Lection_4_jion_job\log.csv', 'a') as file:
        file.write('{};Pressure;{}\n'.format(time, data))   

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'Lection_4_jion_job\log.csv', 'a') as file:
        file.write('{};Wind_speed;{}\n'.format(time, data))

    