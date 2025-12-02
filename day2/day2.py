from typing import List

class Range():

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def is_invalid(self, id: int) -> bool:
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

        for l,r in zip(left, right):
            if l != r:
                return False

        print(f"\tFound invalid ID: {id}")
        return True

    def find_invalid_ids(self) -> List[int]:
        invalid_ids: List[int] = []
        for id in range(self.min, self.max+1):
            if self.is_invalid(id):
                invalid_ids.append(id)
        return invalid_ids

if __name__ == "__main__":
    file = "/Volumes/workplace/advent-of-code-2025/day2/input2.txt"

    ranges: List[str] = []
    with open(file) as f:
        for line in f:
            ranges.extend(line.split(","))

    overall_sum = 0
    for r_str in ranges:
        min, max = r_str.split("-")
        print(f"handling range: {min}-{max}")
        r = Range(int(min), int(max))
        range_sum = sum(r.find_invalid_ids())
        print(f"\t{range_sum=}")
        overall_sum += range_sum


    print(f"OVERALL RESULT: {overall_sum}")