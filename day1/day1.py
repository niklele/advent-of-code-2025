#!/usr/bin/env python3


class Safe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.zeros = 0
        self.curr = 50

    def __repr__(self):
        return f"<curr:{self.curr} zeros:{self.zeros}>"

    def _check_zero(self, new: int):
        if new == 0:
            self.zeros += 1
        # If we started at 0 then remove the double counted zero
        if self.curr == 0:
            self.zeros -= 1
        print(f"\tcheck_zero -> {self}")

    def rotate_left(self, distance: int):
        print(f"{self} rotate_left:{distance}")
        new = self.curr - distance
        while new < 0:
            self.zeros += 1
            new += 100
            print(f"\tunderflow -> <new:{new} zeros:{self.zeros}>")
        self._check_zero(new)
        self.curr = new

    def rotate_right(self, distance: int):
        print(f"{self} rotate_right:{distance}")
        new = self.curr + distance
        while new > 99:
            # subtract 100 and loop around back to the starting point
            self.zeros += 1
            new -= 100
            print(f"\toverflow -> <new:{new} zeros:{self.zeros}>")
        self._check_zero(self.curr)
        self.curr = new


if __name__ == "__main__":
    input_file = "./day1/input1.txt"
    # input_file = './day1/test1.txt'

    safe = Safe()
    print(f"The dial starts by pointing at {safe.curr}.")

    with open(input_file, "r") as f:
        for line in f:
            print(f"The dial is rotated {line[:-1]}")

            # split left or right
            direction = line[0]
            distance = int(line[1:])
            if direction == "L":
                safe.rotate_left(distance)
            else:
                safe.rotate_right(distance)

            print(f"\tto point at {safe.curr}.")

    print(f"FINAL ANSWER: {safe.zeros}")
