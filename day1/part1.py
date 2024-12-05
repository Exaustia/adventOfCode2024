"""
--- Day 1: AdventOfCode 2024 ---
"""

DIRECTORY = r"C:\Users\benoit\PycharmProjects\adventOfCode2024\day1"

array_a = []
array_b = []

RESULT = 0

with open(DIRECTORY + "/input.txt", "r", encoding="utf-8") as files:
    for line in files:
        A, B = line.strip().split()
        array_a.append(int(A))
        array_b.append(int(B))


sorted_array_A = sorted(array_a)
sorted_array_B = sorted(array_b)


for i, (number_a, number_b) in enumerate(zip(sorted_array_A, sorted_array_B)):
    max_number = max(number_a, number_b)
    min_number = min(number_a, number_b)
    RESULT += max_number - min_number

print(RESULT)
