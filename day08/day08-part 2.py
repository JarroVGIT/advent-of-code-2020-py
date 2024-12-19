# Advent of Code 2020 - Day 08 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from copy import deepcopy

content = parse_data_as_lines(8)
result = 0

ops = []
for line in content:
    operation, arg = line.split(" ")
    ops.append((operation, int(arg)))

ptr = 0
acc = 0
ptr_seen = []

for idx, (operation, arg) in enumerate(ops):
    if operation not in ["jmp", "nop"]:
        continue
    new_ops = deepcopy(ops)
    new_ops[idx] = ("jmp", arg) if operation == "nop" else ("nop", arg)

    looped = False

    ptr = 0
    acc = 0
    ptr_seen = []
    while True:
        if ptr in ptr_seen:
            looped = True
            break
        elif ptr == len(new_ops):
            break

        op, ar = new_ops[ptr]
        ptr_seen.append(ptr)
        if op == "nop":
            ptr += 1
            continue
        elif op == "acc":
            acc += ar
            ptr +=1
            continue
        elif op == "jmp":
            ptr += ar
            continue
        else:
            raise ValueError("Shouldn't reach this")

    if not looped:
        result = acc
        break

print(f"Part 2: {result}, {elapsed(start_time)}")