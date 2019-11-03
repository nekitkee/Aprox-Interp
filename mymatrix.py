
# Структура, описывающая матрицу
class MyMatrix:

    a = []
    b = []
    x = []

    def __init__(self,a , b):
        self.x = [0]*len(b)
        self.a = a
        self.b = b

    def gaussianElim(self):

        a = self.a
        b = self.b
        x = self.x
        n = len(self.a)

        for k in range(n):
            max = k
            # Поиск наибольшего в столбце
            for j in range(k + 1, n):
                if abs(self.a[max][k]) < abs(self.a[j][k]):
                    max = j

            # Поднимаем строку
            self.a.insert(k, self.a.pop(max))
            self.b.insert(k, self.b.pop(max))

            # Вычитание коэфициента в J строке
            temp1 = self.a[k][k]
            self.a[k][k] = 1
            for j in range(k + 1, n):
                self.a[k][j] = self.a[k][j] / temp1
            self.b[k] = self.b[k] / temp1

            for I in range(k + 1, n):
                temp2 = self.a[I][k]
                self.a[I][k] = 0
                if (temp2 != 0):
                    for j in range(k + 1, n):
                        self.a[I][j] = self.a[I][j] - temp2 * self.a[k][j]
                    self.b[I] = self.b[I] - temp2 * self.b[k]

        # Обратный ход
        self.x[n - 1] = self.b[n - 1] / self.a[n - 1][n - 1]
        for i in reversed(range(n - 1)):
            for k in range(i, n):
                self.b[i] = self.b[i] - self.x[k] * self.a[i][k]
            self.x[i] = self.b[i] / self.a[i][i]

        return self.x


    # Печать матрицы
    def print(self):
        print("MATRIX A")
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print("%.3f" % (self.a[i][j]), end="   ")
            print()
        print("MATRIX B")
        print(self.b)
        print()


    # Печать результата
    def printResult(self):
        print("RESULT: ")
        for i in range(len(self.x)):
            print("x[{}] = {}".format(i+1 , self.x[i]))
        print()








