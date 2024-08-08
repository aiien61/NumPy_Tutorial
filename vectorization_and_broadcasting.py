import numpy as np
from pprint import pprint

array1: np.ndarray = np.array([10, 100, 1_000])
array2: np.ndarray = np.array([[1., 2., 3.],
                               [4., 5., 6.]])

print(f"array2:")
pprint(array2)

print("array2 + 1:")
pprint(array2 + 1)

print("array2 * array2:")
pprint(array2 * array2)

# matrix multiplication
print("array2 x array2:")
pprint(array2 @ array2.T)