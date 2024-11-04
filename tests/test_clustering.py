import pandas as pd
from mas.clustering import knn

def test_knn(iris_csv: str):
    data = pd.read_csv(iris_csv, delimiter=';').iloc[:, 0:2].replace(',', '.', regex=True).to_numpy(dtype=float)
    knn(data, k=3, sigma=1)
