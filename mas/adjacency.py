import csv

from numpy import array, ndarray, zeros


def adjacency_matrix(filename: str) -> ndarray:
    edges = []

    with open(filename, "r") as fd:
        reader = csv.reader(fd, delimiter=';')
        for e1, e2 in reader:
            edges.append((int(e1), int(e2)))

    max_node = max(max(u, v) for u, v in edges)
    data = zeros((max_node, max_node), dtype=int)

    for u, v in edges:
        data[u-1, v-1] = data[v-1, u-1] = 1

    return data


def adjacency_list(filename: str) -> ndarray:
    data = []

    with open(filename, "r") as fd:
        reader = csv.reader(fd, delimiter=';')
        for line in reader:
            i = int(line[0])
            j = int(line[1])
            data.append((i, j,))

    return array(data, dtype=int)
