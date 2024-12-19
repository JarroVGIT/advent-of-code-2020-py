# Advent of Code 2020 - Day 09 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from itertools import combinations

content = parse_data_as_lines(9)
result = 0
preamble = 25

numbers = [int(number) for number in content]
for idx, number in enumerate(numbers[preamble:]):
    combis = list(combinations(numbers[idx:idx+preamble], 2))
    sums = [a+b for a,b in combis]
    if number in sums:
        continue
    else:
        result = number
        break

print(f"Part 1: {result}, {elapsed(start_time)}")