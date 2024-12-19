# Advent of Code 2020 - Day 13 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(13)
result = 0

timestamp = int(content[0])
busses = []
for bus in content[1].split(","):
    if bus == "x":
        continue
    busses.append(int(bus))

i = 0
while True:
    t = timestamp+i
    found = False
    for bus in busses:
        if t % bus == 0:
            result = i*bus
            found = True
            break
    if found:
        break
    i += 1

print(f"Part 1: {result}, {elapsed(start_time)}")