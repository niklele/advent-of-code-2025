from typing import List, Tuple, Dict
import sympy


def is_invalid_pt1(id: int) -> bool:
    """
    Return true for an ID which is made only of some sequence of digits repeated twice.
    So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
    """

    id_str = str(id)

    # Repeated twice means there are an even number of digits
    if len(id_str) % 2 != 0:
        return False

    # Split into halves and compare characters
    mid = len(id_str) // 2
    left = id_str[:mid]
    right = id_str[mid:]

    for l, r in zip(left, right):
        if l != r:
            return False

    print(f"\tFound invalid ID: {id}")
    return True


divisors_memo: Dict[int, List[int]] = {
    1: [1],
    2: [1, 2],
    3: [1, 3],
    4: [1, 2, 4],
    5: [1, 5],
    6: [1, 2, 3],
    7: [1, 7],
    8: [1, 2, 4, 8],
    9: [1, 3, 9],
    10: [1, 2, 5, 10],
    11: [1, 11],
    12: [1, 2, 3, 4, 6, 12],
}


def get_combinations(id_str: str) -> List[Tuple[int, int]]:
    length = len(id_str)
    combinations: List[Tuple[int, int]] = []
    seen_factors = set()

    if length in divisors_memo:
        divisors = divisors_memo[length]
    else:
        divisors = sympy.ntheory.divisors(length)
        divisors_memo[length] = divisors

    for d in divisors:
        if d not in seen_factors:
            combinations.append((d, length // d))
            seen_factors.add(d)
            seen_factors.add(length // d)
    return combinations


def check_combination(id_str: str, sequence_length: int, repeats: int) -> bool:
    """
    Check that the given ID matches the pattern in the combination
    eg. 1x6 requires that the char sequence of length 1 is repeated 6 times
    3x2 requires that the char sequence of length 3 is repeated 2 times
    """
    if sequence_length == 1 and repeats == 1:
        return False

    substr = id_str[:sequence_length]
    if substr * repeats == id_str:
        print(f"\tFound invalid ID: {id_str} using {sequence_length}x{repeats}")
        return True

    return False


def is_invalid_pt2(id: int) -> bool:
    """
    Return true for an ID if it is made only of some sequence of digits repeated at least twice.
    So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
    """

    id_str = str(id)
    # store every possible repeat run -- all possible divisors of the string
    # eg. A -> A (1x1) always true
    # eg. AB -> AA (1x2)
    # eg. ABC -> AAA (1x3)
    # eg. ABCD -> AAAA (1x4), ABAB (2x2)
    # eg. ABCDE -> AAAAA (1x5)
    # eg. ABCDEF -> AAAAAA (1x6), ABCABC (3x2), ABABAB (2x3)
    # Then check each option

    for sequence_length, repeats in get_combinations(id_str):
        if check_combination(id_str, sequence_length, repeats):
            return True
        if sequence_length != 1:
            # If length is not 1 then flip for the other combination
            # We can't use the Nx1 combination because that would always be true
            if check_combination(id_str, repeats, sequence_length):
                return True
    return False


def find_invalid_ids(min: int, max: int, version: str = "2") -> List[int]:
    invalid_ids: List[int] = []
    for id in range(min, max + 1):
        if version == "1" and is_invalid_pt1(id):
            invalid_ids.append(id)
        elif is_invalid_pt2(id):
            invalid_ids.append(id)
    return invalid_ids


def run(file: str) -> int:
    ranges: List[str] = []
    with open(file) as f:
        for line in f:
            ranges.extend(line.split(","))

    overall_sum = 0
    for r_str in ranges:
        min, max = r_str.split("-")
        print(f"handling range: {min}-{max}")
        range_sum = sum(find_invalid_ids(int(min), int(max)))
        print(f"\t{range_sum=}")
        overall_sum += range_sum

    return overall_sum


if __name__ == "__main__":
    file = "/Volumes/workplace/advent-of-code-2025/day2/input2.txt"
    # file = "/Volumes/workplace/advent-of-code-2025/day2/test.txt"
    overall_sum = run(file)
    print(f"OVERALL RESULT: {overall_sum}")
