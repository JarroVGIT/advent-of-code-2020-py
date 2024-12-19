# Advent of Code 2020 - Day 02 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(2)

result = 0

for line in content:
    counts, pol, pwd = line.split(" ")
    min, max = list(map(int, counts.split("-")))
    min, max = min-1, max-1
    pol = pol.replace(":", "")
    if (pwd[min] == pol and pwd[max] != pol) or (pwd[min] != pol and pwd[max] == pol):
        result+=1

print(f"Part 2: {result}, {elapsed(start_time)}")