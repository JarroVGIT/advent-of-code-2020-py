# Advent of Code 2020 - Day 07 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from collections import deque

content = parse_data_as_lines(7)
result = 0
rules: dict[str, dict[str, int]] = {}
for line in content:
    bag, rule = line.split(" bags contain ")
    if rule == "no other bags.":
        continue
    rules[bag] = {}
    for r in rule.split(", "):
        parts = r.split(" ")
        count = int(parts[0])
        color = f"{parts[1]} {parts[2]}"
        rules[bag][color] = count

q = deque(["shiny gold"])
seen = set()
while q:
    color = q.popleft()
    can_contain = [k for k,v in rules.items() if color in v and k not in seen]
    print(f"{color} directly contained by {can_contain}")
    seen.update(can_contain)
    q.extend(can_contain)
    result += len(can_contain)


print(f"Part 1: {result}, {elapsed(start_time)}")