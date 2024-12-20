# Advent of Code 2020 - Day 17 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_grid, start_time
from rich import print

content = parse_data_as_grid(17)
result = 0
grid = {}
for k, v in content.items():
    grid[int(k.real), int(k.imag), 0, 0] = True if v == "#" else False

neighbors = [
    (x, y, z, w) for x in range(-1, 2, 1) for y in range(-1, 2, 1) for z in range(-1, 2, 1) for w in range(-1, 2, 1)
]
neighbors.remove((0, 0, 0, 0))

for i in range(6):
    max_x = max(c[0] for c in grid) + 2
    min_x = min(c[0] for c in grid) - 1
    max_y = max(c[1] for c in grid) + 2
    min_y = min(c[1] for c in grid) - 1
    max_z = max(c[2] for c in grid) + 2
    min_z = min(c[2] for c in grid) - 1
    max_w = max(c[3] for c in grid) + 2
    min_w = min(c[3] for c in grid) - 1
    new_grid = {}
    for w in range(min_w, max_w):
        for z in range(min_z, max_z):
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    is_active = grid.get((x,y,z, w), False)
                    active_n = sum(grid.get((x+dx, y+dy, z+dz, w+dw), False) for dx, dy, dz, dw in neighbors)
                    if not is_active and active_n == 3:
                        new_grid[(x,y,z,w)] = True
                    elif is_active and active_n not in [2,3]:
                        new_grid[(x,y,z,w)] = False
                    else:
                        new_grid[(x,y,z,w)] = is_active
            
    grid = new_grid

result = sum(grid.values())

print(f"Part 2: {result}, {elapsed(start_time)}")
