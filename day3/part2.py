"""
--- Day 1: AdventOfCode 2024 ---
"""

import re

DIRECTORY = r"C:\Users\benoit\PycharmProjects\adventOfCode2024\day3"


"""
--- Day 1 PART1: AdventOfCode 2024 ---
"""

REGEX_MUL = r"mul\((\d+),(\d+)\)"
REGEX_ALL_DO = r"do\(\)(.*?)(?=don't\(\)|$)"

with open(
    DIRECTORY + "/input.txt",
    "r",
    encoding="utf-8",
) as file:
    contents = re.findall(
        REGEX_ALL_DO, "do()" + file.read().replace("\n", "") + "don't()"
    )
    print(sum(int(x) * int(y) for x, y in re.findall(REGEX_MUL, "".join(contents))))
