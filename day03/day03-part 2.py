# Advent of Code 2020 - Day 03 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(3)
result = 0

rows = [list(line) for line in content]
max_x = len(rows[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result = 1

for right, down in slopes:
    int_result = 0
    x = 0
    for y in range(down, len(rows), down):
        x += right
        x_corrected = x % max_x
        val = rows[y][x_corrected]
        if val == "#":
            int_result += 1
    result *= int_result

print(f"Part 2: {result}, {elapsed(start_time)}")