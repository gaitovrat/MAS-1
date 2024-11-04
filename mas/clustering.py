import numpy as np
from collections import OrderedDict

def gaussian_kernel(X: np.ndarray, sigma: float) -> np.ndarray:
    distances = np.sum((X[:, np.newaxis] - X) ** 2, axis=-1)
    kernel_matrix = np.exp(-distances / (2 * sigma ** 2))
 
    return kernel_matrix

def knn(X: np.ndarray, k: int, sigma: float):
    kernel = gaussian_kernel(X, sigma)
    out = {}

    for i, row in enumerate(kernel):
        row_enum = [(j, r,) for j, r in enumerate(row) if j != i]
        row_enum = sorted(row_enum, key=lambda x: x[1], reverse=True)
        for j in range(k):
            x = i
            y = row_enum[j][0]
            out[tuple(sorted((x,y,)))] = row_enum[j][1]
    out = OrderedDict(sorted(out.items(), key=lambda item: item[0]))
    return out


def eradius(X: np.ndarray, e: float, sigma: float):
    kernel = gaussian_kernel(X, sigma)
