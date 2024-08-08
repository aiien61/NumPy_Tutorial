import numpy as np
from pprint import pprint
from typing import List

# Less understandable representation 
matrix: List[int] = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]

pprint([[i + 1 for i in row ]for row in matrix])

# More readable representation
array1: np.ndarray = np.array([10, 100, 1_000])
array2: np.ndarray = np.array([[1., 2., 3.],
                               [4., 5., 6.]])


print(f"array1 ({array1.dtype})")
pprint(array1)
print(f"array2 ({array2.dtype})")
pprint(array2)
