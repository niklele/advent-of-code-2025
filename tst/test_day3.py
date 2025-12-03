import pytest
from typing import List, Tuple
from src.day3 import find_max_battery, find_max_joltage


@pytest.mark.parametrize(
    "batteries,start,end,expected",
    [
        pytest.param([5, 1, 4, 3, 2, 8], 0, 6, (5, 8), id="full"),
        pytest.param([5, 1, 4, 3, 2, 8], 1, 6, (5, 8), id="skip first"),
        pytest.param([5, 1, 4, 3, 2, 8], 0, 5, (0, 5), id="skip last"),
        pytest.param([5, 1, 4, 3, 2, 8], 1, 5, (2, 4), id="skip first and last"),
        pytest.param([5, 1, 4, 3, 2, 8], 1, 3, (2, 4), id="skip first and last half"),
        pytest.param([5, 1, 4, 3, 2, 8], 3, 5, (3, 3), id="skip first half and last"),
    ],
)
def test_find_max_battery(
    batteries: List[int], start: int, end: int, expected: Tuple[int, int]
):
    assert find_max_battery(batteries, start, end) == expected


@pytest.mark.parametrize(
    "bank,expected",
    [
        pytest.param("12", 12, id="simple"),
        pytest.param("213", 23, id="skip middle"),
        pytest.param("119", 19, id="get last"),
        pytest.param("1191", 91, id="get middle"),
        pytest.param("12345", 45, id="increasing"),
        pytest.param("54321", 54, id="decreasing"),
        pytest.param("987654321111111", 98, id="test1"),
        pytest.param("811111111111119", 89, id="test2"),
        pytest.param("234234234234278", 78, id="test3"),
        pytest.param("818181911112111", 92, id="test4"),
    ],
)
def test_find_max_joltage_2(bank: str, expected: int):
    assert find_max_joltage(bank, N=2) == expected

    @pytest.mark.parametrize(
        "bank,expected",
        [
            pytest.param("987654321111111", 987654321111, id="test1"),
            pytest.param("811111111111119", 811111111119, id="test2"),
            pytest.param("234234234234278", 434234234278, id="test3"),
            pytest.param("818181911112111", 888911112111, id="test4"),
        ],
    )
    def test_find_max_joltage_12(bank: str, expected: int):
        assert find_max_joltage(bank, N=12) == expected
