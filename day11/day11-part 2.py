# Advent of Code 2020 - Day 11 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_grid, start_time
from rich import print

grid = parse_data_as_grid(11)
seats = [k for k,v in grid.items() if v == "L"]
floors = {k: v for k,v in grid.items() if v == "."}

dirs = [complex(-1,0), complex(-1, -1), 
        complex(0,-1), complex(1, -1), 
        complex(1, 0), complex(1,1), 
        complex(0, 1), complex(-1, 1)
]

adjecent: dict[complex, list[complex]] = {}
for seat in seats:
    adjecent[seat] = []
    for dir in dirs:
        n = seat+dir
        while grid.get(n) != "L" and n in grid:
            n = n+dir
        if grid.get(n) == "L":
            adjecent[seat].append(n)

def new_seat_value(grid: dict[complex, str], seat: complex):
    if grid[seat] == "L" and not any(grid.get(n) == "#" for n in adjecent[seat]):
        return "#"
    elif grid[seat] == "#" and sum(grid.get(n) == "#" for n in adjecent[seat]) >= 5:
        return "L"
    else:
        return grid[seat]

while True:
    updated_grid = {}
    for seat in seats:
        updated_grid[seat] = new_seat_value(grid, seat)
    updated_grid.update(floors)
    if grid == updated_grid:
        result = sum(v == "#" for v in updated_grid.values())
        break
    grid = updated_grid

print(f"Part 2: {result}, {elapsed(start_time)}")