import networkx as nx
import numpy as np


def random_generate(n: int, p: float) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            r = np.random.uniform()
            if r <= p:
                graph.add_edge(i, j)

    return graph


def ba_generate(n: int, m: int) -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(m))

    for i in range(m):
        for j in range(i + 1, m):
            G.add_edge(i, j)

    degrees = np.array([degree for node, degree in G.degree()])

    for new_node in range(m, n):
        prob = degrees / degrees.sum()

        chosen_nodes = np.random.choice(range(new_node), size=m, replace=False, p=prob)

        for node in chosen_nodes:
            G.add_edge(new_node, node)
        degrees = np.array([degree for _, degree in G.degree()])

    return G
