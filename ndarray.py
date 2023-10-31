import numpy as np
from pprint import pprint

def ndarray_attributes():
    a = np.arange(1, 4)
    print(f"type of the variable: {type(a)}")
    pprint(a)
    print(f"memory location: {a.data}")
    print(f"type of elements of the variable: {a.dtype}")

    b = np.arange(1, 7).reshape(2, 3)
    pprint(b)
    pprint(b.T)


def axis():
    a = np.arange(6).reshape(3, 2)
    pprint(a)
    print(a.shape)

    b = np.array([a, a])  # build an array containing two array a
    pprint(b)
    print(b.shape)

    print('sum by axis=0:')
    print(b.sum(axis=0))

    print('sum by axis=1:')
    print(b.sum(axis=1))

    print('sum by axis=2:')
    print(b.sum(axis=2))

    a = np.array([0, 1, 2])
    print(a.dtype)
    pprint(a)
    b = np.array([0, 1, 2], dtype='int32')
    print(b.dtype)
    pprint(b)
    c = np.array([0, 1, 2], dtype='float')
    print(c.dtype)
    pprint(c)
    d = np.array([3e33, 5e55], dtype='float64')  # type int will be error
    print(d.dtype)
    pprint(d)
    e = np.array([1.2, 3.4, -5.6], dtype='int')
    print(e.dtype)
    pprint(e)
    f = np.array([0, 1, 2, -3], dtype='bool')
    print(f.dtype)
    pprint(f)


if __name__ == "__main__":
    axis()
