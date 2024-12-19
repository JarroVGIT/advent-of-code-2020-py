# Advent of Code 2020 - Day 02 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(2)

result = 0

for line in content:
    counts, pol, pwd = line.split(" ")
    min, max = list(map(int, counts.split("-")))
    pol = pol.replace(":", "")
    if min <= pwd.count(pol) <= max:
        result +=1


print(f"Part 1: {result}, {elapsed(start_time)}")