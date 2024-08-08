import math
import numpy as np
from pprint import pprint

array1: np.ndarray = np.array([10, 100, 1_000])
array2: np.ndarray = np.array([[1., 2., 3.],
                               [4., 5., 6.]])

# squared root
try:
    pprint(math.sqrt(array2))
except TypeError as e:
    print(e)

pprint(np.array([[math.sqrt(i) for i in row] for row in array2]))

pprint(np.sqrt(array2))

# summation
pprint(array2.sum(axis=0))  # sum up in row direction
pprint(array2.sum(axis=1))  # sum up in column direction
pprint(array2.sum())  # sum up all the numbers into one number