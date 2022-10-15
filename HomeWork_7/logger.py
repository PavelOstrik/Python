from datetime import datetime as dt

path = 'HomeWork_7\log.txt'
string = ''
def logger(info: str):
    global string    
    string = str(dt.now().strftime('%Y:%m:%d-%H:%M:%S')) + ' | ' + info
    with open(path, 'a', encoding='UTF-8') as data:
        data.write(f'{string}\n')