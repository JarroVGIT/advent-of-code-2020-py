# Advent of Code 2020 - Day 01 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from itertools import combinations

content = list(map(int, parse_data_as_lines(1)))

combis = combinations(content, 3)
for a,b,c in combis:
    if a+b+c == 2020:
        result = a*b*c

print(f"Part 2: {result}, {elapsed(start_time)}")