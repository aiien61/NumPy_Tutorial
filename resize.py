import numpy as np
from pprint import pprint

def resize():
    a = np.arange(12)
    pprint(a)
    pprint(np.reshape(a, (3, 4)))
    pprint(np.resize(a, (3, 4)))  # same as np.reshape
    pprint(np.resize(a, (3, 5)))  # auto duplicate elements to fill in
    pprint(np.resize(a, (3, 2)))  # auto trim elements to fit the target size
    
    try:
        pprint(np.reshape(a, (3, 5)))
    except ValueError as e:
        print(e)

    try:
        pprint(np.reshape(a, (3, 2)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    resize()

