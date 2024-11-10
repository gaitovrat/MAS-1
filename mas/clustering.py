import numpy as np
import pandas as pd
from numpy.typing import NDArray


def gaussian_kernel(X: NDArray[np.float64], sigma: float) -> NDArray[np.float64]:
    distances = np.sum((X[:, np.newaxis] - X) ** 2, axis=-1)
    kernel_matrix = np.exp(-distances / (2 * sigma**2))

    return kernel_matrix


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
    out = []

    for i, row in enumerate(kernel):
        out.extend(_eradius(row, e=e, index=i))

    return (
        pd.DataFrame(out, columns=["Source", "Target", "Sim"])
        .sort_values(["Source", "Target"])
        .reset_index(drop=True)
    )


def _knn(row, index: int, k: int):
    out = []
    row_enum = [
        (
            j,
            r,
        )
        for j, r in enumerate(row)
        if j != index
    ]

    for j in range(k):
        x = index
        y, sim = row_enum[j]
        out.append(
            (
                x,
                y,
                sim,
            )
        )

    return out


def _eradius(row, e: float, index: int):
    out = []

    for j, similarity in enumerate(row):
        if index != j and similarity >= e:
            out.append(
                (
                    index,
                    j,
                    similarity,
                )
            )
    return out


def hybrid(X: NDArray[np.float64], k: int, e: float, sigma: float):
    kernel = gaussian_kernel(X, sigma)
    out = []

    for i, row in enumerate(kernel):
        eradius_result = _eradius(row, e=e, index=i)
        if len(eradius_result) > k:
            out.extend(eradius_result)
        else:
            out.extend(_knn(row, index=i, k=k))

    return (
        pd.DataFrame(out, columns=["Source", "Target", "Sim"])
        .sort_values(["Source", "Target"])
        .reset_index(drop=True)
    )
