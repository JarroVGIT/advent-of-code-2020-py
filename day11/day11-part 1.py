# Advent of Code 2020 - Day 11 - part 1
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


def new_seat_value(grid: dict[complex, str], seat: complex):
    if grid[seat] == "L" and not any(grid.get(seat+dir) == "#" for dir in dirs):
        return "#"
    elif grid[seat] == "#" and sum(grid.get(seat+dir) == "#" for dir in dirs) >= 4:
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
    
print(f"Part 1: {result}, {elapsed(start_time)}")