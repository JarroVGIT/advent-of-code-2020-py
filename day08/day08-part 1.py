# Advent of Code 2020 - Day 08 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(8)
result = 0

ops = []
for line in content:
    operation, arg = line.split(" ")
    ops.append((operation, int(arg)))

ptr = 0
acc = 0
ptr_seen = []
while True:
    operation, arg = ops[ptr]
    if ptr in ptr_seen:
        break
    else:
        ptr_seen.append(ptr)

    if operation == "nop":
        ptr += 1
        continue
    elif operation == "acc":
        acc += arg
        ptr +=1
        continue
    elif operation == "jmp":
        ptr += arg
        continue
    else:
        raise ValueError("Shouldn't reach this")

result = acc

print(f"Part 1: {result}, {elapsed(start_time)}")