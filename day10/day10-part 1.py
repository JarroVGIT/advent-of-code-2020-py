# Advent of Code 2020 - Day 10 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(10)
result = 0

adapters = [int(line) for line in content]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

one_jolts = sum(b-a == 1 for a,b in zip(adapters, adapters[1:]))
three_jolts = sum(b-a == 3 for a, b in zip(adapters, adapters[1:]))

result = one_jolts * three_jolts

print(f"Part 1: {result}, {elapsed(start_time)}")