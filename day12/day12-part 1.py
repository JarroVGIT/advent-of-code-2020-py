# Advent of Code 2020 - Day 12 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(12)
result = 0

ops = []
for line in content:
    ops.append((line[0], int(line[1:])))

current_dir = "E"
current_loc = complex(0,0)
rotate_r = ["N", "E", "S", "W", "N", "E", "S", "W"]
rotate_l = ["N", "W", "S", "E", "N", "W", "S", "E"]

def do_op(current_loc: complex, current_dir: str, op: tuple[str, int]):
    operation, amount = op
    match operation:
        case "N":
            return current_loc + (amount * complex(0,-1)), current_dir
        case "E":
            return current_loc + (amount * complex(1,0)), current_dir
        case "S":
            return current_loc + (amount * complex(0,1)), current_dir
        case "W":
            return current_loc + (amount * complex(-1,0)), current_dir
        case "F":
            return do_op(current_loc, current_dir, (current_dir, amount))
        case "R":
            idx = rotate_r.index(current_dir)
            next_idx = amount // 90
            return current_loc, rotate_r[idx+next_idx]
        case "L":
            idx = rotate_l.index(current_dir)
            next_idx = amount // 90
            return current_loc, rotate_l[idx+next_idx]
        case _:
            raise ValueError()

for op in ops:
    current_loc, current_dir = do_op(current_loc, current_dir, op)

result = abs(int(current_loc.real)) + abs(int(current_loc.imag))

print(f"Part 1: {result}, {elapsed(start_time)}")