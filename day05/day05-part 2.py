# Advent of Code 2020 - Day 05 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print

content = parse_data_as_lines(5)
result = set()

seats = []

tickets = [list(row) for row in content]

def calculate(min: int, max: int, ticket: list[str]):
    if min == max:
        return min
    if ticket[0] in ["B", "R"]:
        new_min = min + (max - min +1)//2
        return calculate(min=new_min, max=max, ticket=ticket[1:])
    else:
        new_max = max - ((max - min) // 2) -1
        return calculate(min=min, max=new_max, ticket=ticket[1:])


for ticket in tickets:
    row = calculate(0, 127, ticket[:7])
    col = calculate(0, 7, ticket[7:])
    seats.append(row*8+col)

max = max(seats)
min = min(seats)
for id in seats:
    if id+1 not in seats and id != max:
        result.add(id+1)
    if id-1 not in seats and id != min:
        result.add(id-1)

print(f"Part 2: {result}, {elapsed(start_time)}")