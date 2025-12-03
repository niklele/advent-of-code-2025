import pytest
from src.day3 import find_max_joltage


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
    assert find_max_joltage(bank) == expected
