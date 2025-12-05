import os
from typing import Tuple, List


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"<{self.start}-{self.end}>"

    def __contains__(self, item) -> bool:
        if not isinstance(item, int):
            raise ValueError("Range can only work with int")

        if self.start <= item <= self.end:
            return True

        return False


def parse_input(file: str) -> Tuple[List[Range], List[int]]:
    ranges = []
    inputs = []
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            if "-" in line:
                start, end = line.split("-")
                ranges.append(Range(int(start), int(end)))
            elif line:
                inputs.append(int(line))

    return ranges, inputs


def count_fresh(ranges: List[Range], inputs: List[int]) -> int:
    """
    Count number of ingredients in inputs that match with the ranges of fresh ingredients.
    """
    num_fresh = 0
    for i in inputs:
        for r in ranges:
            if i in r:
                num_fresh += 1
                break  # Don't double count

    return num_fresh


if __name__ == "__main__":
    file = "inputs/input5.txt"
    # file = "inputs/test5.txt"

    ranges, inputs = parse_input(os.path.join(os.getcwd(), file))
    total = count_fresh(ranges, inputs)
    print(f"OVERALL RESULT: {total}")
