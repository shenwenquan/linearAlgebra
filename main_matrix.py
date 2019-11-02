from playLA.Matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)

    print(matrix.row_vector(0))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))

    print("zero_2_3: {}".format(Matrix.zero(2, 3)))
