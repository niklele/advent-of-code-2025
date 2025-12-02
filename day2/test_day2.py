import pytest
from day2.day2 import *

def test_is_invalid_pt1():
    assert is_invalid_pt1(11)
    assert is_invalid_pt1(22)

    for i in range(12,22):
        assert is_invalid_pt1(i) == False

@pytest.mark.parametrize("input_str,expected_combinations",
 [
     ( "A", [ (1,1) ] ),
     ( "AA", [ (1,2) ] ),
     ( "AAA", [ (1,3) ] ),
     ( "AAAA", [ (1,4), (2,2) ] ),
     ( "AAAAA", [(1,5)] ),
     ( "AAAAAA", [(1,6), (2,3)] ),
     ( "AAAAAAAAAAAA", [(1, 12), (2, 6), (3, 4)] )
 ])
def test_get_combinations(input_str: str, expected_combinations: List[Tuple[int,int]]):
    combinations = get_combinations(input_str)
    assert len(combinations) == len(expected_combinations)
    for exp in expected_combinations:
        assert exp in combinations


@pytest.mark.parametrize("input_str,sequence_length,repeats,expected",
[
    ("A", 1, 1, False), # AT LEAST 1 repeat, so 1x1 is out
    ("AB", 1, 2, False),
    ("AA", 1, 2, True),
    ("ABC", 1, 3, False),
    ("ABCABC", 3, 2, True),
    ("ABABAB", 2, 3, True),
    ("ABABCD", 2, 3, False),
])
def test_check_combination(input_str: str, sequence_length: int, repeats: int, expected: bool):
    assert check_combination(input_str, sequence_length, repeats) == expected

@pytest.mark.parametrize("num,expected",
 [
     (1, False), # 1 one time: AT LEAST 1 repeat, so 1x1 is out
     (12, False), # 12 one time
     (123, False), # 123 one time
     (1234, False), # 1234 one time
     (12321, False), # 12321 palindrome is not invalid
     (12341234, True), # 1234 two times
     (123123123, True), # 123 three times
     (12121212, True), # 12 four times
     (1212121212, True), # 12 five times
     (1111111, True) # 1 seven times
 ])
def test_is_invalid_pt2(num: int, expected: bool):
    assert is_invalid_pt2(num) == expected

def test_find_invalid_ids_pt1():
    # Zero invalid IDs
    assert len(find_invalid_ids(min=15, max=17, version="1")) == 0

    # Two invalid IDs
    invalid_ids = find_invalid_ids(min=11, max=22, version="1")

    assert len(invalid_ids) == 2
    assert 11 in invalid_ids
    assert 22 in invalid_ids

@pytest.mark.parametrize("min,max,expected_invalid_ids",
[
    (15,17,[]), # Zero invalid IDs
    (11,22,[11,22]), # Two invalid IDs
    (95,115,[99,111]),
    (998,1012,[999,1010]),
    (1188511880,1188511890,[1188511885]),
    (222220,222224,[222222]),
    (1698522,1698528,[]),
    (446443,446449,[446446]),
    (38593856,38593862,[38593859]),
    # (565653,824824827,[824824824]), # SLOW
    # (2121212118,2121212124,[2121212121]), # SLOW
]
)
def test_find_invalid_ids_pt2(min: int, max: int, expected_invalid_ids: List[int]):

    invalid_ids = find_invalid_ids(min=min, max=max, version="2")
    assert len(invalid_ids) == len(expected_invalid_ids)
    for id in expected_invalid_ids:
        assert id in invalid_ids
