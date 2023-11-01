import numpy as np
from pprint import pprint

def append():
    a = np.arange(12)
    pprint(a)
    pprint(np.append(a, [100, 101]))  # append elements of the list to the end

    b = np.arange(12).reshape(3, 4)
    pprint(b)
    pprint(np.append(b, [1, 2, 3, 4])) # if axis is not being specified, auto convert 2D to fit 1D list


if __name__ == "__main__":
    append()