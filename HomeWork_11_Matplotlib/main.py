# f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


x_limit = [-8,8.1]
koef = [-12, -18, 5, 10, -30]
color = 'r'
 
def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

x = np.arange(x_limit[0], x_limit[1], 0.01)

change_x = []
change_dir = 1
roots_x = []

for i in range(len(x) - 1):
    if change_dir == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = 1
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            change_x.append((x[i], func(x[i], *koef)))
            change_dir = -1
            
for i in range(len(x) - 1):
    if func(x[i], *koef) > 0 and func(x[i+1], *koef) < 0 :        
        roots_x.append(round(x[i],2))
    elif func(x[i], *koef) < 0 and func(x[i+1], *koef) > 0:
            roots_x.append(round(x[i],2))
        
print(roots_x)

def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


plt.figure(dpi=(120), figsize=(8,6))
plt.title(f'Исследовать функцию:\n f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.hlines(0, -8, 8.3, linestyle = '--', color = 'k')


current_x = np.arange(x_limit[0], change_x[0][0], 0.1)
line1 = plt.plot(current_x, func(current_x, *koef), change_color())
plt.legend(line1, "Убывание")
for i in range(len(change_x)-1):
    current_x = np.arange(change_x[i][0], change_x[i+1][0], 0.1)
    plt.plot(current_x, func(current_x, *koef), change_color())
    
current_x = np.arange(change_x[-1][0], x_limit[1], 0.1)
line2 = plt.plot(current_x, func(current_x, *koef), change_color())


red_line = mlines.Line2D([], [],color='r', label='Убывание')
blue_line = mlines.Line2D([], [],color='b', label='Возрастание')
marker_roots = mlines.Line2D([], [], linestyle = '--', color = 'y', marker='x',
                          markersize=8, label='Корни уравнения')
plt.legend(handles=[red_line,blue_line,marker_roots])

plt.plot(x[0],func(x[0],*koef), 'ro')
plt.text(x[0],func(x[0],*koef) + 30,
         f'Вершина функции {change_x[0][0],round(change_x[0][1],1)}')

plt.plot(roots_x, roots_x , 'yx')
plt.text(x[0], -20000, f'Корни уравнения на промежутке {x_limit}:\n {roots_x}') 

plt.show()










