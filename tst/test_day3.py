import pytest
from typing import List, Tuple
from src.day3 import find_max_battery, find_max_joltage


@pytest.mark.parametrize(
    "batteries,start,end,expected",
    [
        ([5, 1, 4, 3, 2, 8], 0, 6, (5, 8)),
        ([5, 1, 4, 3, 2, 8], 1, 6, (5, 8)),
        ([5, 1, 4, 3, 2, 8], 0, 5, (0, 5)),
        ([5, 1, 4, 3, 2, 8], 1, 5, (2, 4)),
        ([5, 1, 4, 3, 2, 8], 1, 3, (2, 4)),
        ([5, 1, 4, 3, 2, 8], 3, 5, (3, 3)),
    ],
)
def test_find_max_battery(
    batteries: List[int], start: int, end: int, expected: Tuple[int, int]
):
    assert find_max_battery(batteries, start, end) == expected


@pytest.mark.parametrize(
    "bank,expected",
    [
        ("12", 12),
        ("213", 23),
        ("119", 19),
        ("1191", 91),
        ("12345", 45),
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_find_max_joltage(bank: str, expected: int):
    assert find_max_joltage(bank, N=2) == expected
