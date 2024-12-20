# Advent of Code 2020 - Day 14 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from itertools import product
content = parse_data_as_lines(14)
result = 0

memory = {}

def get_address_spaces(mask: str, mem_loc: int) -> list[int]:
    """
    Given a mem_loc (int) and a mask (containing floating bits), construct
    all possible memory locations. 
    """
    mem_loc = list(bin(mem_loc).replace("0b", ""))
    mem_loc = (["0"] * (len(mask)-len(mem_loc))) + mem_loc
    
    one_positions = [pos for pos, char in enumerate(mask) if char == "1"]
    for pos in one_positions:
        mem_loc[pos] = "1"
    
    x_positions = [pos for pos, char in enumerate(mask) if char == 'X']
    mem_locs = []
    for combination in product('01', repeat=len(x_positions)):
        for pos, bit in zip(x_positions, combination):
            mem_loc[pos] = bit
        mem_locs.append(int("".join(mem_loc), base=2))
    return mem_locs

for line in content:
    if line.startswith("mask = "):
        mask = line.replace("mask = ", "")
    else:
        mem, val = line.split(" = ")
        mem = int(mem.replace("mem[", "").replace("]",""))
        val = int(val)
        for space in get_address_spaces(mask, mem):
            memory[space] = val  

result = sum(memory.values())

print(f"Part 2: {result}, {elapsed(start_time)}")