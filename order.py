import numpy as np
from pprint import pprint

c = np.arange(12)
pprint(c)


def order_by_C():
    d = np.reshape(c, (3, 4), order='C')
    pprint(d)


def order_by_Fortran():
    d = np.reshape(c, (3, 4), order='F')
    pprint(d)


if __name__ == "__main__":
    order_by_Fortran()