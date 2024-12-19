# Advent of Code 2020 - Day 01 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = list(map(int, parse_data_as_lines(1)))

for entry in content:
    if (2020-entry) in content:
        result = entry*(2020-entry)
        break

print(f"Part 1: {result}, {elapsed(start_time)}")