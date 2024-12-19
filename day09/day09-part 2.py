# Advent of Code 2020 - Day 09 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time, is_example
from rich import print
from itertools import combinations

content = parse_data_as_lines(9)
result = 0

preamble = 25 if not is_example else 5

numbers = [int(number) for number in content]

for idx, number in enumerate(numbers[preamble:]):
    combis = list(combinations(numbers[idx:idx+preamble], 2))
    sums = [a+b for a,b in combis]
    if number in sums:
        continue
    else:
        faulty_number = number
        faulty_idx = idx+preamble
        break

# idx, faulty_number is where it goes wrong, so backtrack from there.
for i in range(faulty_idx-1, 0, -1):
    sum_so_far = numbers[i]
    j = i
    while sum_so_far < faulty_number:
        j -= 1
        if j == 0:
            break
        sum_so_far = sum(numbers[j:i+1])
        if sum_so_far == faulty_number:
            result = max(numbers[j:i+1]) + min(numbers[j:i+1])
            break

print(f"Part 2: {result}, {elapsed(start_time)}")