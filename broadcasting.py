import numpy as np
from pprint import pprint


def extend_axis():
    a = np.array([[1, 2]])
    pprint(a)
    print(a.shape)
    b = np.array([3, 4])
    pprint(b)
    print(b.shape)

    pprint(a + b)
    print((a + b).shape)


def extend_dimension():
    a = np.arange(3).reshape(1, 1, 3)
    b = np.arange(8).reshape(4, 2, 1)
    pprint(a)
    print(a.shape)

    pprint(b)
    print(b.shape)

    pprint(a + b)
    print((a + b).shape)


def extend_axis_and_dimension():
    a = np.array([1, 2])
    b = np.array([[3, 4], [5, 6]])
    pprint(a)
    print(a.shape)
    pprint(b)
    print(b.shape)
    pprint(a + b)
    print((a + b).shape)



if __name__ == "__main__":
    extend_axis_and_dimension()