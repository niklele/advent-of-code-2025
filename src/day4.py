from typing import List
import os

EMPTY = "."
ROLL = "@"


def check(grid: List[List[str]], r: int, c: int) -> int:
    if grid[r][c] == ROLL:
        return 1
    else:
        return 0


def count_neighbors(grid: List[List[str]], r: int, c: int) -> int:
    row_max = len(grid) - 1
    col_max = len(grid[0]) - 1
    count = 0

    """
    UpLeft      Up      UpRight
    Left        @       Right
    DownLeft    Down    DownRight
    """

    if r > 0 and c > 0:
        # check up left
        count += check(grid, r - 1, c - 1)

    if r > 0:
        # check up
        count += check(grid, r - 1, c)

    if r > 0 and c < col_max:
        # check up right
        count += check(grid, r - 1, c + 1)

    if c < col_max:
        # check right
        count += check(grid, r, c + 1)

    if r < row_max and c < col_max:
        # check down right
        count += check(grid, r + 1, c + 1)

    if r < row_max:
        # check down
        count += check(grid, r + 1, c)

    if r < row_max and c > 0:
        # check down left
        count += check(grid, r + 1, c - 1)

    if c > 0:
        # check left
        count += check(grid, r, c - 1)

    return count


def cell_is_accessible(grid: List[List[str]], r: int, c: int) -> bool:
    if grid[r][c] == ROLL:
        neighbors = count_neighbors(grid, r, c)
        if neighbors < 4:
            # print(f"\t{r},{c} is accessible.")
            return True
        else:
            # print(f"\t{r},{c} is not accessible.")
            return False
    else:
        # print(f"\t{r},{c} is empty.")
        return False


def parse_grid(file: str) -> List[List[str]]:
    grid: List[List[str]] = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip("\n")
            row = [ch for ch in line]
            grid.append(row)
    return grid


def run(file: str) -> int:
    total = 0

    grid = parse_grid(file)

    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            # print(f"Processing {r},{c}: {value}")
            if cell_is_accessible(grid, r, c):
                total += 1

    return total


if __name__ == "__main__":
    # file = "inputs/input4.txt"
    file = "inputs/test4.txt"

    total = run(os.path.join(os.getcwd(), file))
    print(f"OVERALL RESULT: {total}")
