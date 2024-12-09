"""
--- Day 1: AdventOfCode 2024 ---
"""

import re

DIRECTORY = r"C:\Users\benoit\PycharmProjects\adventOfCode2024\day3"


"""
--- Day 1 PART1: AdventOfCode 2024 ---
"""

REGEX = r"mul\((\d+),(\d+)\)"
TOTAL = 0

with open(
    DIRECTORY + "/input.txt",
    "r",
    encoding="utf-8",
) as file:
    print(sum(int(x) * int(y) for x, y in re.findall(REGEX, file.read())))
