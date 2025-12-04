from src.day4 import check, ROLL, EMPTY
from typing import List
import pytest


@pytest.fixture
def test_grid() -> List[List[str]]:
    return [[EMPTY, EMPTY, ROLL], [EMPTY, ROLL, ROLL], [ROLL, EMPTY, EMPTY]]


@pytest.mark.parametrize(
    "r,c,expected",
    [pytest.param(0, 0, 0, id="empty"), pytest.param(1, 1, 1, id="roll")],
)
def test_check(test_grid, r: int, c: int, expected: int):
    assert check(test_grid, r, c) == expected
