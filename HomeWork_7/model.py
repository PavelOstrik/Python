
equation = ''

def init_equation(string):
    global equation    
    equation = string

def transform(string):
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    string = string.split()   
    return string 

def deleteElement(string, i):
    string.pop(i+1)
    string.pop(i)

def decision(string):        
    while len(string) > 1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if string[i] == '*':                    
                    string[i-1] = int(string[i-1]) * int(string[i+1])
                    deleteElement(string, i)                    
                    break
                if string[i] == '/':                    
                    string[i-1] = int(string[i-1]) / int(string[i+1])
                    deleteElement(string, i)                    
                    break
        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if string[i] == '+':                    
                    string[i-1] = int(string[i-1]) + int(string[i+1])
                    deleteElement(string, i)                    
                    break
                if string[i] == '-':                    
                    string[i-1] = int(string[i-1]) - int(string[i+1])
                    deleteElement(string, i)                    
                    break 
    result = string[0]
    return result




