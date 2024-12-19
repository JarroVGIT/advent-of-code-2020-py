# Advent of Code 2020 - Day 13 - part 2
# Author: Jarro van Ginkel
from aoc_utils import elapsed, parse_data_as_lines, start_time
from rich import print
from math import prod

content = parse_data_as_lines(13)
result = 0

busses = []
for idx, bus in enumerate(content[1].split(",")):
    if bus == "x":
        continue
    else:
        busses.append((idx, int(bus)))

def is_prime(n: int) -> bool:
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

assert all(is_prime(bus) for idx, bus in busses)

# Chinese Remainder Theorem
# t ≡ bus1idx (mod bus1) -> t % bus1 = 0
# t ≡ bus2-bus2idx (mod bus2) -> t % bus2 = bus2-bus2idx
# t ≡ bus3-bus3idx (mod bus3) -> t % bus3 = bus3-bus3idx
# etc.

# The implementation is straight from ChatGPT and I won't be taking 
# any questions at this time, thank you.

remainders = [] 
for idx, bus in busses:
    remainders.append(bus-idx)

moduli = [bus for idx,bus in busses]

def modular_inverse(remainder, modulus):
    m0, x0, x1 = modulus, 0, 1
    while remainder > 1:
        q = remainder // modulus
        remainder, modulus = modulus, remainder % modulus
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chinese_remainder(remainders, moduli):
    M = prod(moduli)  # Compute the product of all moduli
    t = 0
    for ai, mi in zip(remainders, moduli):
        Mi = M // mi
        inv = modular_inverse(Mi, mi)
        t += ai * Mi * inv
    return t % M


result = chinese_remainder(remainders, moduli)

print(f"Part 2: {result}, {elapsed(start_time)}")