# Advent of Code 2020 - Day 15 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(15)
result = 0

numbers = list(map(int, content[0].split(",")))

i = 0
prev = None
last_heard: dict[int, int] = {}
for idx, num in enumerate(numbers):
    if prev is not None:
        last_heard[prev] = i
    prev = num
    i = idx + 1

while i < 2020:
    if last_heard.get(prev) is None:
        last_heard[prev] = i
        prev = 0
    else:
        tmp = i - last_heard[prev]
        last_heard[prev] = i
        prev = tmp
    i += 1

result = prev

print(f"Part 1: {result}, {elapsed(start_time)}")