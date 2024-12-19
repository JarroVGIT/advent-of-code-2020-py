# Advent of Code 2020 - Day 10 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from collections import defaultdict

content = parse_data_as_lines(10)
result = 0

adapters = [int(line) for line in content]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

counts = defaultdict(int)
counts[0] = 1

for adapter in adapters[1:]:
    counts[adapter] = counts[adapter-1] + counts[adapter-2] + counts[adapter-3]

result = counts[adapters[-1]]

print(f"Part 2: {result}, {elapsed(start_time)}")