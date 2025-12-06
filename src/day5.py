import os
from typing import Tuple, List, Dict, Optional
import uuid
from enum import Enum
from dataclasses import dataclass

"""
we need to solve 2 problems:
1. build datastructure for problem 2 from input

Given a list of non-overlapping ranges, add a new range.

- represent as a single numberline with points that are the start or end of a range.
- when we add a new range, add new start and end marker
- then fix up any markers within that range:
  - if theres a start, then remove it because the new start will be earlier so it will have more inclusion
  - if theres an end, then also remove it because the new end will be later so it will have more inclusion
  
then the datastructure should be a linked list so that we can easily find next markers

2. query datastructure to get all non-overlapping ranges. the values we want are then enumerated from [start,end] inclusive
"""

class MarkerType(Enum):
    START = "start"
    END = "end"

@dataclass
class Marker:
    type: MarkerType
    pos: int
    prev: Optional["Marker"] = None
    next: Optional["Marker"] = None

class NumberLine:
    def __init__(self, start: int, end: int):
        self.head = Marker(type=MarkerType.START, pos=start)
        self.tail = Marker(type=MarkerType.END, pos=end)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, marker: Marker):
        curr = self.head
        while curr.next:
            if marker.pos > curr.pos:
                # insert after curr, first update curr.next and then update curr
                if curr.next:
                    marker.next = curr.next
                    curr.next.prev = marker
                curr.next = marker
                marker.prev = curr
                break
            curr = curr.next

        if not marker.prev:
            # Add to the very end
            self.tail.next = marker
            marker.prev = self.tail
            self.tail = marker
    def _coallesce(self, start: Marker, end: Marker):
        curr = start
        while curr.next and curr != end:
            # remove curr
            saved_prev = curr.prev
            saved_next = curr.next

            saved_prev.next = saved_next
            saved_next.prev = saved_prev

            curr = curr.next

    def add_range(self, start: int, end: int):
        start_mark = Marker(type=MarkerType.START, pos=start)
        end_mark = Marker(type=MarkerType.END, pos=end)

        # Place the start_mark and end_mark
        self._insert(start_mark)
        self._insert(end_mark)

        # Remove any markers in between start and end
        self._coallesce(start_mark, end_mark)

    def get_ranges(self) -> List[Tuple[int]]:
        ret = []
        curr = self.head

        curr_start = self.head.pos
        while curr.next:
            if curr.type == MarkerType.START:
                curr_start = curr.pos
            else:
                # Complete the range and ship it
                ret.append((curr_start, curr.pos))
            curr = curr.next

        # Close off the final range using the tail
        ret.append((curr_start, self.tail.pos))

        return ret


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"<{self.start}-{self.end}>"

    def __contains__(self, item) -> bool:
        if not isinstance(item, int):
            raise ValueError("Range can only work with int")

        if self.start <= item <= self.end:
            return True

        return False

    def __eq__(self, other):
        if not isinstance(other, Range):
            raise ValueError("Range can only be compared to another Range")

        return self.id == other.id

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

def parse_input_numberline(file: str) -> NumberLine:
    numberline = None
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            if "-" in line:
                start, end = line.split('-')
                if not numberline:
                    numberline = NumberLine(int(start), int(end))
                else:
                    numberline.add_range(int(start), int(end))

    return numberline

def count_fresh_numberline(numberline: NumberLine) -> int:
    total = 0
    for start, end in numberline.get_ranges():
        diff = end - start
        total += diff
    return total

def count_fresh_inputs(ranges: List[Range], inputs: List[int]) -> int:
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

def count_all_fresh(ranges: List[Range]) -> int:
    """
    Count number of unique ingredients that are fresh according to the ranges of fresh ingredients.
    """
    fresh = set()
    for r in ranges:
        for i in range(r.start, r.end + 1):
            fresh.add(i)

    return len(fresh)


if __name__ == "__main__":
    # file = "inputs/input5.txt"
    file = "inputs/test5.txt"

    file_path = os.path.join(os.getcwd(), file)

    # ranges, inputs = parse_input(file_path)
    # total = count_fresh_inputs(ranges, inputs)
    # total = count_all_fresh(ranges)

    numberline = parse_input_numberline(file_path)
    total = count_fresh_numberline(numberline)

    print(f"OVERALL RESULT: {total}")
