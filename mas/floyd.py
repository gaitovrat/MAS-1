from numpy import fill_diagonal, float64, inf, ndarray, zeros


def floyd(matrix: ndarray) -> ndarray:
    n = matrix.shape[0]
    dist = zeros((n, n), dtype=float64)

    for i in range(n):
        for j in range(n):
            dist[i, j] = matrix[i, j] if matrix[i, j] != 0 else inf

    fill_diagonal(dist, 0)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, j] > (dist[i, k] + dist[k, j]):
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist.astype(int)
