# Advent of Code 2020 - Day 07 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from collections import defaultdict

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

counts = defaultdict(lambda: 0)

def calc_next_bags(color, count) -> dict[str, int]:
    global counts
    counts[color] += count
    result = 0
    if rules.get(color):
        for k, val in rules[color].items():
            result += calc_next_bags(k, count*val) + 1
    return result

calc_next_bags("shiny gold", 1)

result = sum(v for k,v in counts.items() if k != "shiny gold") 

print(f"Part 2: {result}, {elapsed(start_time)}")