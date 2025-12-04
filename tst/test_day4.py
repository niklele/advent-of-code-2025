from src.day4 import parse_grid, check
from typing import List
import pytest
import os


@pytest.fixture
def test_grid() -> List[List[str]]:
    base = os.path.dirname(os.path.realpath(__file__))
    return parse_grid(os.path.join(base, "../inputs/input4.txt"))


@pytest.mark.parametrize(
    "r,c,expected",
    [pytest.param(0, 0, 0, id="empty"), pytest.param(1, 1, 1, id="roll")],
)
def test_check(test_grid, r: int, c: int, expected: int):
    assert check(test_grid, r, c) == expected
