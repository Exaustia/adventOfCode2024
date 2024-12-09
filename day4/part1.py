"""
--- Day 1: AdventOfCode 2024 ---
"""

import numpy as np
import re

DIRECTORY = r"C:\Users\benoit\PycharmProjects\adventOfCode2024\day4"


"""
--- Day 1 PART1: AdventOfCode 2024 ---
"""

MATCH = "XMAS"
REVERSED_MATCH = MATCH[::-1]  # Inverser le mot
REGEX = rf"{MATCH}|{REVERSED_MATCH}"  # Créer une regex pour correspondre au mot dans les deux sens

TOTAL = 0


def match_str(lines: np.ndarray) -> int:
    print(lines)
    for line in lines:
        if re.search(REGEX, line):
            return 1
    return 1


def vertical_match(lines: list) -> list:
    # Transposer les lignes pour obtenir les colonnes
    transposed = ["".join(row) for row in zip(*lines)]
    return match_str(transposed)


def diagonal_match(array: np.ndarray) -> int:
    diagonals = []
    # Obtenir les diagonales principales
    for offset in range(-array.shape[0] + 1, array.shape[1]):
        diagonals.append("".join(array.diagonal(offset)))
    # Obtenir les diagonales secondaires
    flipped_array = np.fliplr(array)
    for offset in range(-flipped_array.shape[0] + 1, flipped_array.shape[1]):
        diagonals.append("".join(flipped_array.diagonal(offset)))
    return match_str(diagonals)


with open(DIRECTORY + "/input.txt", "r", encoding="utf-8") as file:
    array = np.array([list(line) for line in [line.strip() for line in file]])

    TOTAL += match_str(array)

    print(TOTAL)
