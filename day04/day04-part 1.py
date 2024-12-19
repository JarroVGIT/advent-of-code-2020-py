# Advent of Code 2020 - Day 04 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import re

content = parse_data_as_lines(4, "\n\n")
result = 0

req_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
}

for passport in content:
    p = passport.replace("\n", " ")
    p = p.split(" ")
    present = set()
    for fieldval in p:
        field, val = fieldval.split(":")
        present.add(field)
    if present.issuperset(req_fields):
        result += 1

print(f"Part 1: {result}, {elapsed(start_time)}")
