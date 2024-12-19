# Advent of Code 2020 - Day 03 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(3)

rows = [list(line) for line in content]
max_x = len(rows[0])
x = 0
result = 0

for y in range(1, len(rows)):
    x += 3
    x_corrected = x % max_x
    val = rows[y][x_corrected]
    if val == "#":
        result += 1


print(f"Part 1: {result}, {elapsed(start_time)}")