# Advent of Code 2020 - Day 19 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import re

# Below works fine on the example, but not in the input. I get the response that I have
# the response of another user, coincidinky? Tested with some other solutions on Reddit,
# and mine is definitely incorrect.

# The below solution is the same as Part 1, because I thought I had a neat little trick;
# since I am building a regex pattern, the new rule "8: 42 | 42 8" can be rewritten as
# `8: 42 "+"` or `8: "(" 42 ")" "+"`
# rule `11: 42 31 | 42 11 31` can be rewritten as `11: 42 "+" 31 "+"` or as 
# `11: "(" 42 ")" "+" "(" 31 ")" "+"`. I even tested this out in regex101, seemed to work. 
# Thought I was very clever, but turned out this is overreaching (too many matches). 

# Alternatively, I changed rule 8 and 11 to multiple or statements. Took the script 23
# minutes to build the pattern and match everything, but it yielded the correct answer.

# 11: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 31
# 8: 42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 42 42

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

print(f"Part 2: {result}, {elapsed(start_time)}")