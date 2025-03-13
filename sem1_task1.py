def summ(array):
    s = 0
    for i in range(len(array)//2):
        s += array[i] + array[len(array)-i-1]
    return s
import numpy as np
a = np.arange(1, 1000001, dtype=np.int64)
print(summ(a))
