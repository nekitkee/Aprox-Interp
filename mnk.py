
#TODO: //check if there are 0 on main diagonal and exchange rows in that case

# Заполннение матрицы частными призводными
def fillMatrix(x , y , k):
    k=k+1
    n= len(x)
    matrixA = [[0 for x in range(k)] for y in range(k)]
    matrixB = [0 for x in range(k)]

    for row in range(k):
        for col in range (k):
            sumx = 0
            for i in range(n):
                sumx+=pow(x[i],row+col)
            matrixA[col][row] = sumx

    matrixB[0]=sum(y)

    for row in range(1,k):
        sumxy = 0
        for i in range(n):
            sumxy+=pow(x[i],row) * y[i]
        matrixB[row] = sumxy

    return (matrixA,matrixB)

# Вычисление значения апроксимирующей функции в произвольной точке
def aproximation(polyval , x):
    fx= 0
    for k in range(len(polyval)):
        fx+=pow(x,k)*polyval[k]
    return fx


