import os
from pathlib import Path

import pytest

FILEPATH = Path(os.path.dirname(os.path.abspath(__file__)))
TEST_DATA_PATH = FILEPATH / "data"
DATA_PATH = FILEPATH / ".." / "data"


@pytest.fixture(name="links_csv")
def fixture_links_csv() -> Path:
    return TEST_DATA_PATH / "links.csv"


@pytest.fixture(name="karate_club_csv")
def fixture_karate_club_csv() -> Path:
    return DATA_PATH / "KarateClub.csv"


@pytest.fixture(name="iris_csv")
def fixture_iris_csv() -> Path:
    return DATA_PATH / "Iris.csv"

@pytest.fixture(name="knn_csv")
def fixture_knn_csv() -> Path:
    return TEST_DATA_PATH / "knn.csv"
