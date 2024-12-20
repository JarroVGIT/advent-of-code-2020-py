# Advent of Code 2020 - Day 14 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
import sys

content = parse_data_as_lines(14)
result = 0

memory = {}

def get_mask_ints(mask: str) -> tuple[int, int]:
    """
    The mask to be applied is both an OR and AND, so we construct 
    integers for both the OR part and the AND part.
    """
    reversed = list(mask)
    reversed.reverse()
    
    max = sys.maxsize * 2 + 1
    
    or_decimal = 0
    and_decimal = 0

    for idx, bit in enumerate(reversed):
        if bit == "1":
            or_decimal += 2**idx
        elif bit == "0":
            and_decimal += 2**idx

    and_decimal = max-and_decimal
    return or_decimal, and_decimal

for line in content:
    if line.startswith("mask = "):
        mask: tuple[int,int] = get_mask_ints(line.replace("mask = ", ""))
    else:
        mem, val = line.split(" = ")
        mem = int(mem.replace("mem[", "").replace("]",""))
        val = int(val)
        memory[mem] = (mask[0] | val) & mask[1]

result = sum(memory.values())
print(f"Part 1: {result}, {elapsed(start_time)}")