import numpy as np
from pprint import pprint


def reshape():
    c = np.arange(1, 7).reshape(2, 3)
    d = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]],
                  [[13,14,15], [16,17,18], [19,20,21], [22,23,24]]])
    
    pprint(c)
    print(c.shape)

    c = c.reshape(3, 2)
    pprint(c)
    print(c.shape)

    c = c.reshape(6, 1)
    pprint(c)
    print(c.shape)

    pprint(d)
    print(d.shape)

    d = d.reshape(2, 6, 2)
    pprint(d)
    print(d.shape)

    d = d.reshape(8, 3)
    pprint(d)
    print(d.shape)

    # np.reshape(x, newshape, order)
    a = np.arange(12) # 1D array
    pprint(a)

    b = np.reshape(a, (3, 4)) # reshaped to be 2D array
    pprint(b)


if __name__ == "__main__":
    reshape()