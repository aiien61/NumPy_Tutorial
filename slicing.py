import numpy as np
from pprint import pprint


def one_dimension_slicing():
    a = np.arange(10)
    pprint(a)
    pprint(a[1: 5])
    pprint(a[2: 8: 2])
    pprint(a[::-1])
    pprint(a[:3])
    pprint(a[4:])
    print(a[:3], a[3:])
    pprint(a[::2])
    pprint(a[:])


def two_dimension_slicing():
    b = np.arange(20).reshape(4, 5)
    pprint(b)
    pprint(b[1:3, 2:4])
    pprint(b[:2, 1:])
    pprint(b[::2, :])
    pprint(b[:, ::2])
    pprint(b[:, ::-1])
    pprint(b[::-1, ::-1])


if __name__ == "__main__":
    two_dimension_slicing()
