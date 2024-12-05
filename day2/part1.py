"""
--- Day 1: AdventOfCode 2024 ---
"""

DIRECTORY = r"C:\Users\benoit\PycharmProjects\adventOfCode2024\day2"

AT_LEAST = 1
AT_MOST = 3
SAFE_LINES = 0


"""
--- Day 1 PART1: AdventOfCode 2024 ---
"""


def correct_order(inputs):
    """
    Check if the levels are either all increasing or all decreasing.
    :param inputs:
    :return:
    """
    # The levels are either all increasing or all decreasing.
    return all(x < y for x, y in zip(inputs, inputs[1:])) or all(
        x > y for x, y in zip(inputs, inputs[1:])
    )


def at_least_or_at_most(inputs):
    """
    Check if the difference between the levels is at most 3 and at least 1.
    :param inputs:
    :return:
    """

    for i, _ in enumerate(inputs[:-1]):
        cal = abs(inputs[i] - inputs[i + 1])

        if cal > AT_MOST or cal < AT_LEAST:
            return False
    return True


with open(
    DIRECTORY + "/input.txt",
    "r",
    encoding="utf-8",
) as files:
    for line in files:

        fire_levels = [int(level) for level in line.strip().split()]

        ordered = correct_order(fire_levels)
        least_or_most = at_least_or_at_most(fire_levels)
        if ordered and least_or_most:
            SAFE_LINES += 1

print(SAFE_LINES)
