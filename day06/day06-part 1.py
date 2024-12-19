# Advent of Code 2020 - Day 06 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(6, "\n\n")
result = 0

groups = [block.split("\n") for block in content]

for group in groups:
    yesses = set()
    for person in group:
        yesses.update(list(person))
    result += len(yesses)


print(f"Part 1: {result}, {elapsed(start_time)}")