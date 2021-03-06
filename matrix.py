import random
from datetime import datetime


class Matrix:

    def __init__(self, shape=[0, 0]):
        self.matrix = []
        self.shape = shape
        pass

    def read_matrix2D(self):
        """
        To read matrix from the console input to store in self.matrix
        Reads one row at a time and splits into array of floats
        """
        self.matrix = []
        for x in range(self.shape[0]):
            row = input().split()
            row_integer = [(float(num)) for num in row]
            self.matrix.append(row_integer)

    def read_order2D(self):
        """
        To take shape of matrix as a string and assign to self.shape list
        """
        order = input().split(" ")
        self.shape = [int(order[0]), int(order[1])]

    def print(self, t=0):
        """
            Printing matrix on console.
            Parameter:
            t - type of output
                default t = 0 which prints the matrix as a normal list.
                t = 1 prints the matrix with space and newline like a string
        """
        if t == 0:
            print(self.matrix)
        elif t == 1:
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    print(round(self.matrix[x][y], 4), end=" ")
                print()

    def __add__(self, other):
        """
            Adds two objects of Matrix class and returns the sum matrix object.
            sum_matrix is the addition of matrix1 + matrix2

            Parameter:
                self - the first matrix object to be added
                other -
                    - the other matrix object that has to be added
                    - an integer or float to add component-wise

            returns:
                a matrix object whose self.matrix is the sum_matrix and self.shape is shape of added matrix
        """
        if self.shape[0] == other.shape[0] and self.shape[1] == other.shape[1]:

            sum_matrix = [[self.matrix[x][y] + other.matrix[x][y] for y in range(self.shape[1])]
                          for x in range(self.shape[0])]
            new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
            new_matrix.matrix = sum_matrix
            return new_matrix
        else:
            print("The operation cannot be performed.")

        return self

    def __sub__(self, other):
        """
            Subtracts two objects of Matrix class and returns the difference matrix object.
            diff_matrix is the addition of matrix1 + matrix2

            Parameter:
                self - the first matrix object to be diff
                other -
                    - the other matrix object that has to be added
                    - an integer or float to add component-wise

            returns:
                a matrix object whose self.matrix is the diff_matrix and self.shape is shape of added matrix
        """
        # print(type(other))
        if self.shape[0] == other.shape[0] and self.shape[1] == other.shape[1]:
            diff_matrix = [[self.matrix[x][y] - other.matrix[x][y] for y in range(self.shape[1])]
                           for x in range(self.shape[0])]
            new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
            new_matrix.matrix = diff_matrix
            return new_matrix
        else:
            print("The operation cannot be performed.")

        return self

    def __mul__(self, other, multiplication_type="matrix_multiplication"):
        """
            Supports two types of multiplication.
            Matrix to matrix multiplication using the matrix rules
            Matrix and constant multiplication to multiply a constant component wise.

            Parameters:
                self - the first matrix
                other - Either another matrix or a constant
                    if other is Matrix object, then it does matrix to matrix multiplication
                    if other is a float or an integer, it does matrix to constant multiplication
                multiplication_type -
                    matrix_multiplication - Indicates if the multiplication is using rules of matrix multiplication
                    component_wise - Indicates if the multiplication is done component_wise

            returns:
                the product matrix object after m to m multiplication.
                or
                the product matrix object after m to c multiplication.
        """
        if type(other) == type(self):
            if self.shape[1] == other.shape[0]:
                p_matrix = [[0 for y in range(other.shape[1])] for x in range(self.shape[0])]
                for x in range(self.shape[0]):
                    for y in range(other.shape[1]):
                        for k in range(other.shape[0]):
                            p_matrix[x][y] += self.matrix[x][k] * other.matrix[k][y]
                new_matrix = Matrix(shape=[self.shape[0], other.shape[1]])
                new_matrix.matrix = p_matrix
                return new_matrix
            else:
                print("The operation cannot be performed")
            return None

        else:
            c_matrix = [[round(self.matrix[x][y] * other) for y in range(self.shape[1])]
                        for x in range(self.shape[0])]
            new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
            new_matrix.matrix = c_matrix
            return new_matrix

    def __truediv__(self, other):
        """
            To divide two matrices component wise.

            returns:
                A matrix object whose matrix is the component-wise division of two matrices.
        """
        if self.shape[0] == other.shape[0] and self.shape[1] == other.shape[1]:
            d_matrix = [[round(float(self.matrix[x][y]) / float(other.matrix[x][y]), 4) for y in range(self.shape[1])]
                        for x in range(self.shape[0])]
            new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
            new_matrix.matrix = d_matrix
            return new_matrix
        else:
            print("The operation cannot be performed!")
        return None

    def main_transpose(self):
        """
            To transpose the self.matrix over its main diagonal

            returns:
                A Matrix object that is the transpose about its main diagonal.
        """
        t_matrix = [[self.matrix[y][x] for y in range(self.shape[1])] for x in range(self.shape[0])]
        new_matrix = Matrix(shape=[self.shape[1], self.shape[0]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def side_transpose(self):
        """
            To transpose matrix over its secondary/ side diagonal

            returns:
                A matrix object that is transpose about its side diagonal
        """
        t_matrix = []
        counter_row = 0
        for i in reversed(range(self.shape[0])):
            t_matrix.append([])
            for j in reversed(range(self.shape[1])):
                t_matrix[counter_row].append(self.matrix[j][i])
            counter_row += 1

        new_matrix = Matrix(shape=[self.shape[1], self.shape[0]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def vertical_transpose(self):
        """
            To transpose the matrix over its 'vertical axis'

            returns:
                A matrix object that is reversed about its rows

            Usage:
                Example:
                    If                              After vertical transpose,
                       matrix = [[1, 2, 3],         The matrix = [[3, 2, 1],
                                 [4, 5, 6],                       [6, 5, 4],
                                 [7, 8, 9]]                       [9, 8, 7]]
        """
        t_matrix = []
        for i in range(self.shape[0]):
            t_matrix.append(list(reversed(self.matrix[i])))

        new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def horizontal_transpose(self):
        """
            To transpose the matrix over its 'horizontal axis'

            returns:
                A matrix object that is reversed about its columns

            Usage:
                Example:
                    If                              After Horizontal transpose,
                       matrix = [[1, 2, 3],         The matrix = [[7, 8, 9],
                                 [4, 5, 6],                       [4, 5, 6],
                                 [7, 8, 9]]                       [1, 2, 3]]
        """
        t_matrix = []

        for i in range(self.shape[0]):
            t_matrix.append([])
            for j in range(self.shape[1]):
                t_matrix[i].append(self.matrix[self.shape[0] - 1 - i][j])

        new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def minor(self):
        pass

    def cofactor_matrix(self):
        pass

    def det(self):
        """
            To find the determinant of the matrix.

            returns:
                Numerical value that is the determinant of the matrix

        """
        det = 0
        if self.shape[0] == self.shape[1]:

            pass
        else:
            return "error"

    def fill(self, number=0):
        """
            Fills a matrix with the given number.

            returns:
                A matrix object that is filled with the given number.
        """
        m = []
        for x in range(self.shape[0]):
            m.append([])
            for y in range(self.shape[1]):
                m[x].append(number)

        new_matrix = Matrix(shape=[self.shape[0], self.shape[1]])
        new_matrix.matrix = m
        return new_matrix

    def generate_matrix(self, shape: list, input_string: str):
        """
            To generate a 2D matrix from the space separated input string of numbers

            returns:
                nothing, but its stores the generated matrix in the self.matrix list
        """
        self.shape[0] = shape[0]
        self.shape[1] = shape[1]
        input_list = input_string.split(" ")
        counter = 0
        for x in range(shape[0]):
            self.matrix.append([])
            for y in range(shape[1]):
                self.matrix[x].append(round(float(input_list[counter])))
                counter = counter + 1

    def identity(self, size: int):
        """
            To generate and return an identity matrix of a given size

            Parameters:
                size - an integer to indicate the size of the identity matrix

            returns:
                A Matrix object with an identity matrix of the given size

        """
        i_matrix = []
        for x in range(size):
            i_matrix.append([])
            for y in range(size):
                if x == y:
                    i_matrix[x].append(1)
                else:
                    i_matrix[x].append(0)
        new_matrix = Matrix(shape=[size, size])
        new_matrix.matrix = i_matrix
        return new_matrix

    def generate_random(self, shape: list, val_range: list, dtype="float", seed=datetime.now()):
        """
            To generate a matrix with random integers

            Parameters:
                shape - [x, y] is a list with x indicating rows, y indicating columns
                val_range - [a, b] is a list with a indicating lower end, b indicating upper end of the range
                seed - its an integer seed value for random generator if you want to set a particular random matrix

            returns:
                nothing - It modifies the existing self.matrix and doesnt return it.
        """
        random.seed(seed)
        self.shape[0] = shape[0]
        self.shape[1] = shape[1]

        for x in range(shape[0]):
            self.matrix.append([])
            for y in range(shape[1]):
                # self.matrix[x].append(random.randint(val_range[0], val_range[1]) + random.random() if dtype == "float"
                #                       else random.randint(val_range[0], val_range[1]))
                if dtype == "float":
                    self.matrix[x].append(float(random.randint(val_range[0], val_range[1]) + round(random.random(), 4)))
                elif dtype == "int":
                    self.matrix[x].append(random.randint(val_range[0], val_range[1]))


if __name__ == "__main__":
    print("This module cannot run as main")