import os

def find_max_joltage(bank: str) -> int:
    """
    Within each bank, you need to turn on exactly two batteries;
    the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on.
    For example, if you have a bank like 12345 and you turn on batteries 2 and 4,
    the bank would produce 24 jolts. (You cannot rearrange batteries.)
    """

    # convert from str to list of ints
    batteries = [int(b) for b in bank]

    # To find the max joltage, we need to put together 2 numbers: AB
    # A: largest number up to (not including) the last digit
    # B: largest number in the remaining digits

    a_index = 0
    a = batteries[a_index]
    for i, battery in enumerate(batteries[:-1]):
        if battery > a:
            a = battery
            a_index = i

    b_index = a_index + 1
    b = batteries[b_index]
    for i, battery in enumerate(batteries[a_index+1:]):
        if battery > b:
            b_index = i
            b = battery

    total = int(f"{a}{b}")

    print(f"\tturn on batteries {a_index} and {b_index} -> {total}")

    return total

def run(file: str) -> int:

    total = 0
    with open(file, "r") as f:
        for bank in f:
            bank = bank.strip("\n")
            print(f"Find max joltage for {bank}")
            total += find_max_joltage(bank)

    return total

if __name__ == "__main__":
    file = "inputs/input3.txt"
    # file = "inputs/test3.txt"

    overall_sum = run(os.path.join(os.getcwd(), file))
    print(f"OVERALL RESULT: {overall_sum}")