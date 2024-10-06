from numpy import array, zeros, float64, array_equal, round
from mas import adjacency_matrix, floyd


def test_floyd(karate_club_csv: str) -> None:
    expected_closeness = array([0.586207,
                                0.500000,
                                0.576271,
                                0.478873,
                                0.390805,
                                0.395349,
                                0.395349,
                                0.453333,
                                0.531250,
                                0.447368,
                                0.390805,
                                0.377778,
                                0.382022,
                                0.531250,
                                0.382022,
                                0.382022,
                                0.293103,
                                0.386364,
                                0.382022,
                                0.515152,
                                0.382022,
                                0.386364,
                                0.382022,
                                0.404762,
                                0.386364,
                                0.386364,
                                0.373626,
                                0.472222,
                                0.465753,
                                0.395349,
                                0.472222,
                                0.557377,
                                0.531250,
                                0.566667])
    dist = floyd(adjacency_matrix(karate_club_csv))

    n = dist.shape[0]
    closeness = zeros((n,), dtype=float64)

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += dist[i][j]
        closeness[i] = n / sum

    assert array_equal(round(closeness, 6), expected_closeness)
