#!/usr/bin/env python3

num_zeros = 0
input_file = './input.txt'


def group_add(a, b):
    c = a + b
    if c > 99:
        return group_add(a, b - 100)
    elif c < 0:
        return group_add(a, b + 100)
    else:
        return c

curr = 50 # We always start at 50
print(f'The dial starts by pointing at {curr}.')
with open(input_file, 'r') as f:
    for line in f:
        # split left or right
        direction = line[0]
        distance = int(line[1:])
        if direction == 'L':
            # curr -= distance
            curr = group_add(curr, -distance)
        else:
            # curr += distance
            curr = group_add(curr, distance)

        print(f"The dial is rotated {line[:-1]} to point at {curr}")

        if curr == 0:
            num_zeros += 1

print(f"FINAL ANSWER: {num_zeros}")
