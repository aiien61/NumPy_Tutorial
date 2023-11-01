import time
import numpy as np
from pprint import pprint


def three_dimensional_array():
    d = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]],
                  [[13,14,15], [16,17,18], [19,20,21], [22,23,24]]])
    
    pprint(d)
    print(d.shape)


def calculate_time():
    a = np.random.randn(100000)
    b = list(a)
    start_time = time.time()
    for _ in range(1000):
        sum_1 = np.sum(a)
    print(f"Using NumPy: {time.time() - start_time} sec")

    start_time = time.time()
    for _ in range(1000):
        sum_2 = sum(b)
    print(f"Basic Python: {time.time() - start_time} sec")


if __name__ == "__main__":
    calculate_time()
