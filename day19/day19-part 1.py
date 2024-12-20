# Advent of Code 2020 - Day 19 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import re

rules, to_match = parse_data_as_lines(19, "\n\n")
result = 0

rules_dict: dict[int, list[str|int]] = {}
for rule in rules.split("\n"):
    idx, r = rule.split(": ")
    r = r.split(" ")
    r = [int(c) if c.isdigit() else c.replace("\"", "") for c in r]
    rules_dict[int(idx)] = r


while any(isinstance(c, int) for c in rules_dict[0]):
    for idx, item in enumerate(rules_dict[0]):
        if isinstance(item, int):
            if len(rules_dict[item]) == 1 and isinstance(rules_dict[item][0], str):
                to_add = rules_dict[item]
            else:
                to_add = ["("] + rules_dict[item] + [")"]
            base_rule = rules_dict[0][:idx] + to_add + rules_dict[0][idx+1:]
            break
    rules_dict[0] = base_rule

pattern = "^" + "".join(base_rule) + "$"

for line in to_match.split("\n"):
    if re.match(pattern, line):
        result+=1

print(f"Part 1: {result}, {elapsed(start_time)}")