# Advent of Code 2020 - Day 04 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import re

content = parse_data_as_lines(4, "\n\n")

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

result = 0

def validate(field: str, val:str) -> bool:
    match field:
        case "byr":
            return 1920 <= int(val) <= 2002
        case "iyr":
            return 2010 <= int(val) <= 2020
        case "eyr":
            return 2020 <= int(val) <= 2030
        case "hgt":
            if val.endswith("cm"):
                return 150 <= int(val[:-2]) <= 193
            elif val.endswith("in"):
                return 59 <= int(val[:-2]) <= 76
            else:
                return False
        case "hcl":
            return bool(re.match(r"^#[0-9a-f]{6}$", val))
        case "ecl":
            return val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        case "pid":
            return bool(re.match(r"^\d{9}$", val))
        case _:
            return False

for passport in content:
    p = passport.replace("\n", " ")
    p = p.split(" ")
    present = set()
    for fieldval in p:
        field, val = fieldval.split(":")
        if validate(field, val):
            present.add(field)
    if present.issuperset(req_fields):
        result += 1

print(f"Part 2: {result}, {elapsed(start_time)}")