# Advent of Code 2020 - Day 16 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from copy import deepcopy

content = parse_data_as_lines(16, "\n\n")
result = 0

ranges = content[0].split("\n")
my_ticket = list(map(int, content[1].split("\n")[1].split(",")))
nearby_tickets = content[2].split("\n")[1:]

ranges_by_type = {}
all_ranges: list[range] = []

def update_ranges(ranges: list[range], new_range: range) -> None:
    new_start = new_range.start
    new_end = new_range.stop
    merged = []
    for r in ranges:
        curr_start, curr_end = r.start, r.stop
        if curr_end < new_start:
            # Current range ends before the new range starts (no overlap)
            merged.append(r)
        elif new_end < curr_start:
            # Current range starts after the new range ends (no overlap)
            merged.append(range(new_start, new_end))  # Add the new range
            new_start, new_end = curr_start, curr_end
        else:
            # Ranges overlap, merge
            new_start = min(new_start, curr_start)
            new_end = max(new_end, curr_end)
    merged.append(range(new_start, new_end))
    return sorted(merged, key=lambda r: r.start)

for r in ranges:
    t, rs = r.split(": ")
    r1, r2 = rs.split(" or ")
    r1 = range(int(r1.split("-")[0]), int(r1.split("-")[1])+1)
    r2 = range(int(r2.split("-")[0]), int(r2.split("-")[1])+1)
    ranges_by_type[t] = [r1, r2]
    all_ranges.extend([r1, r2])

remaining_tickets = deepcopy(nearby_tickets)
for ticket in nearby_tickets:
    nums = list(map(int, ticket.split(",")))
    for num in nums:
        if not any(num in r for r in all_ranges):
            remaining_tickets.remove(ticket)

remaining_tickets = [list(map(int, ticket.split(","))) for ticket in remaining_tickets]

possible_fields: list[list[str]] = []
for i in range(len(remaining_tickets[0])):
    possible = []
    for field, rs in ranges_by_type.items():
        if (sum([t[i] in rs[0] for t in remaining_tickets]) + sum([t[i] in rs[1] for t in remaining_tickets])) == len(remaining_tickets):
            possible.append(field)
    possible_fields.append(possible)

all_fields = set(ranges_by_type.keys())

# Trim the search field by removing elements that occur in possible locations with length 1:
singles = []
while True:
    found_single = False
    to_remove = ""
    for pos_list in possible_fields:
        if len(pos_list) == 1 and pos_list[0] not in singles:
            to_remove = pos_list[0]
            found_single = True
            singles.append(pos_list[0])
            break
    if found_single:
        for pos_list in possible_fields:
            if len(pos_list) > 1:
                pos_list.remove(to_remove)
        continue
    else:
        break

# Didn't even need to DFS; recursively removing single elements yields correct list.
# def backtrack(idx: int, used_field_names: set[str], curr_list: list[str]) -> list[str]:
#         if idx == len(possible_fields):
#             return curr_list if len(used_field_names) == len(all_fields) else None
#         for name in possible_fields[idx]:
#             if name not in used_field_names:
#                 used_field_names.add(name)
#                 curr_list.append(name)
#                 result = backtrack(idx + 1, used_field_names, curr_list)
#                 if result:
#                     return result
#                 used_field_names.remove(name)
#                 curr_list.pop()
#         return None

fields = [idx for idx, f in enumerate(possible_fields) if f[0].startswith("departure")]
result = 1
for idx in fields:
    result *= my_ticket[idx]

print(f"Part 2: {result}, {elapsed(start_time)}")