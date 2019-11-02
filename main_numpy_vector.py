import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    lst = [1, 2, 3]
    lst[0] = "Linear Algebra"
    print(lst)

    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = 666
    # print(vec)

    # 模
    print(np.linalg.norm(vec))

    # 求单位向量
    print(vec / np.linalg.norm(vec))
