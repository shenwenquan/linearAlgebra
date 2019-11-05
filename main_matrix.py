from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print(matrix.row_vector(0))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))
    print("zero_2_3: {}".format(Matrix.zero(2, 3)))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("T.dot(p) = {}".format(T.dot(p)))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("T.dot(P) = {}".format(T.dot(P)))

    print("A.dot(B) = {}".format(matrix.dot(matrix2)))
    print("B.dot(A) = {}".format(matrix2.dot(matrix)))

