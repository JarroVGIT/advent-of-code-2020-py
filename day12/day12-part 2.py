# Advent of Code 2020 - Day 12 - part 2
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
rotate_r = {90: 1j, 180: -1, 270: -1j}
rotate_l = {90: -1j, 180: -1, 270: 1j}

def do_op(current_loc: complex, waypoint: complex, op: tuple[str, int]):
    operation, amount = op
    match operation:
        case "N":
            return current_loc, waypoint + (amount * complex(0,-1))
        case "E":
            return current_loc, waypoint + (amount * complex(1,0))
        case "S":
            return current_loc, waypoint + (amount * complex(0,1))
        case "W":
            return current_loc, waypoint + (amount * complex(-1,0))
        case "F":
            return current_loc + waypoint*amount, waypoint
        case "R":
            return current_loc, waypoint * rotate_r[amount]
        case "L":
            return current_loc, waypoint * rotate_l[amount]
        case _:
            raise ValueError()

waypoint = complex(10,-1)
for op in ops:
    current_loc, waypoint = do_op(current_loc, waypoint, op)

result = abs(int(current_loc.real)) + abs(int(current_loc.imag))

print(f"Part 2: {result}, {elapsed(start_time)}")