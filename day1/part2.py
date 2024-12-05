"""
--- Day 1 PART2: AdventOfCode 2024 ---
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


for number_a in array_a:
    number_of_similarity = array_b.count(number_a)
    RESULT += number_a * number_of_similarity

print(RESULT)
