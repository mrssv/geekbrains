#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц: см. в методичке.
#Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, mat_dict):
        self.mat_dict = mat_dict

    def create_mat(self):
        self.mat_dict = numpy.array(self.mat_dict)
        return print(self.mat_dict)

    def __str__(self) -> str:
        result = ''
        for i in self.mat_dict:
            for j in i:
                result += str(j) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        num_str = len(self.mat_dict)
        num_col = len(other.mat_dict[0])
        for i in range(num_str):
            for j in range(num_col):
                self.mat_dict[i][j] = self.mat_dict[i][j] + other.mat_dict[i][j]
        result_sum = self.mat_dict
        return Matrix(result_sum)


my_dict = Matrix([[1, 2, 3], [4, 5, 6]])
my_dict2 = Matrix([[6, 5, 4], [3, 2, 1]])
print(my_dict)
print(my_dict2)
print(my_dict + my_dict2)