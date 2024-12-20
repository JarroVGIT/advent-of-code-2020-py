# Advent of Code 2020 - Day 18 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

problems = parse_data_as_lines(18)
result = 0

def calc(input: str) -> int:
    res = 0
    op = "+"
    for c in input.split(" "):
        if c.isdigit():
            res = eval(f"{res}{op}{c}")
        else:
            op = c
    return res

# remove all parentheses first
for problem in problems:
    while (close:=problem.find(")")) > 0:
        open = problem[:close].rfind("(")
        e = calc(problem[open+1:close])
        problem = problem[:open] + str(e) + problem[close+1:]

    result += calc(problem)

print(f"Part 1: {result}, {elapsed(start_time)}")