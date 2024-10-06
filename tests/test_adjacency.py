from numpy import array, array_equal
from mas import adjacency_list, adjacency_matrix


def test_adjacency_matrix(links_csv: str) -> None:
    expected = array([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ])

    matrix = adjacency_matrix(links_csv)

    assert array_equal(expected, matrix)


def test_adjacency_list(links_csv: str) -> None:
    expected = array([
        [1, 2],
        [2, 3],
        [3, 1]
    ])
    adj_list = adjacency_list(links_csv)

    assert array_equal(expected, adj_list)
