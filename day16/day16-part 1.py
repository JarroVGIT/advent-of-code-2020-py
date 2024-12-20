# Advent of Code 2020 - Day 16 - part 1
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from copy import copy
content = parse_data_as_lines(16, "\n\n")
result = 0

ranges = content[0].split("\n")
my_ticket = content[1].split("\n")[1]
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
    all_ranges = update_ranges(all_ranges, r1)
    all_ranges = update_ranges(all_ranges, r2)

remaining_tickets = copy(nearby_tickets)
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
        for r in rs:
            if all(t[i] in r for t in remaining_tickets):
                possible.append(field)
                break
    possible_fields.append(possible)

print(possible_fields)


print(f"Part 1: {result}, {elapsed(start_time)}")