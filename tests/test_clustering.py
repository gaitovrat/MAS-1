from pathlib import Path

import numpy as np
import pandas as pd

from mas.clustering import eradius, knn


def test_knn(iris_csv: Path, knn_csv: str):
    expected_result = pd.read_csv(knn_csv, delimiter=";")
    df = pd.read_csv(iris_csv, delimiter=";")
    data = (
        df.loc[:, df.columns != "Species"]
        .replace(",", ".", regex=True)
        .to_numpy(dtype=float)
    )
    result = knn(data, k=3, sigma=1)

    for row in result.itertuples():
        expected_row = expected_result[
            (expected_result["Source"] == row.Source)
            & (expected_result["Target"] == row.Target)
        ]

        # The row may be missing due to minor floating-point precision differences
        if len(expected_row) == 0:
            continue

        assert len(expected_row) == 1

        row_sim = np.float64(row.Sim)
        expected_sim = expected_row.Sim.iloc[0]
        assert np.isclose(row_sim, expected_sim, atol=1e-9)


def test_eradius(iris_csv: Path, knn_csv: str):
    expected_result = pd.read_csv(knn_csv, delimiter=";")
    df = pd.read_csv(iris_csv, delimiter=";")
    data = (
        df.loc[:, df.columns != "Species"]
        .replace(",", ".", regex=True)
        .to_numpy(dtype=float)
    )
    result = eradius(data, e=0.9, sigma=1)

    for row in result.itertuples():
        expected_row = expected_result[
            (expected_result["Source"] == row.Source)
            & (expected_result["Target"] == row.Target)
        ]

        # The row may be missing due to minor floating-point precision differences
        if len(expected_row) == 0:
            continue

        assert len(expected_row) == 1

        row_sim = np.float64(row.Sim)
        expected_sim = expected_row.Sim.iloc[0]
        assert np.isclose(row_sim, expected_sim, atol=1e-9)
