import numpy as np
import pandas as pd
from numpy.typing import NDArray


def distances(X: NDArray[np.float64]) -> NDArray[np.float64]:
    return np.sqrt(np.sum((X[:, np.newaxis] - X) ** 2, axis=-1))


def gaussian_kernel(X: NDArray[np.float64], sigma: float) -> NDArray[np.float64]:
    dist = distances(X)
    kernel_matrix = np.exp(-dist / (2 * sigma**2))

    return kernel_matrix


def _eradius(
    row: NDArray[np.float64], e: float, index: int, similarities: NDArray[np.float64]
) -> list[tuple[int, int, float]]:
    out = [
        (index, j, similarities[index, j])
        for j, distance in enumerate(row)
        if index != j and distance <= e
    ]
    return out


def _knn(row, index: int, k: int):
    row_enum = [(j, r) for j, r in enumerate(row) if j != index]
    row_enum.sort(key=lambda x: x[1], reverse=True)

    top_k = row_enum[:k]
    return [(index, y, sim) for y, sim in top_k]


def knn(X: NDArray[np.float64], k: int, sigma: float):
    kernel = gaussian_kernel(X, sigma)
    out: list[tuple[int, int, float]] = []

    for i, row in enumerate(kernel):
        out.extend(_knn(row, index=i, k=k))

    return (
        pd.DataFrame(out, columns=["Source", "Target", "Sim"])
        .sort_values(["Source", "Target"])
        .reset_index(drop=True)
    )


def eradius(X: NDArray[np.float64], e: float, sigma: float):
    kernel = gaussian_kernel(X, sigma)
    dist = distances(X)
    out = []

    for i, row in enumerate(dist):
        out.extend(_eradius(row, e=e, index=i, similarities=kernel))

    return (
        pd.DataFrame(out, columns=["Source", "Target", "Sim"])
        .sort_values(["Source", "Target"])
        .reset_index(drop=True)
    )


def hybrid(X: NDArray[np.float64], k: int, e: float, sigma: float):
    kernel = gaussian_kernel(X, sigma)
    dist = distances(X)
    out = []

    for i, row in enumerate(kernel):
        eradius_result = _eradius(dist[i], e=e, index=i, similarities=kernel)
        if len(eradius_result) > k:
            out.extend(eradius_result)
        else:
            out.extend(_knn(row, index=i, k=k))

    return (
        pd.DataFrame(out, columns=["Source", "Target", "Sim"])
        .sort_values(["Source", "Target"])
        .reset_index(drop=True)
    )
