import matplotlib.pyplot as plt
import numpy

import input
from mymatrix import MyMatrix
from mnk import fillMatrix , aproximation
from spline import BuildSpline , interpolate

# Считывание таблицы с входными данными
x = input.x
y = input.y

# Порядок апроксимации
k = input.k

# Заполнение матрицы частными производными
a , b = fillMatrix(x,y,k)
matrix = MyMatrix(a , b )

# Решение матрицы методом Гаусса возвращает значения апроксимирующего полинома к-той степени
polyval = matrix.gaussianElim()

# Вычисление вектора сплайнов методом прогонки
spline = BuildSpline(x, y)

# Новый шаг на сетке
new_x =  numpy.arange(1,8.2 , 0.2)

# Вывод на график точек из входной таблицы
plt.scatter(x, y)

# Вычисления значений Y для нового шага
intr = []
aprox = []
for newx in new_x:
    intr.append(interpolate(spline, newx))
    aprox.append(aproximation(polyval, newx))

# График с апроксимирующей и интерполирующей функциями
plt.plot(new_x , intr)
plt.plot(new_x, aprox)
plt.show()


