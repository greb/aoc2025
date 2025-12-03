import functools


def parse(lines):
    return [[int(n) for n in line] for line in lines.splitlines()]

def find_max_joltage(bank, n):
    # Greedy algo with O(n) works here
    digits = []
    for i in range(n):
        head = len(bank) - (n-i-1)
        m = max(bank[:head])
        digits.append(m)
        p = bank.index(m)
        bank = bank[p+1:]
    return functools.reduce(lambda x,y: x*10+y, digits)

def part1(banks):
    return sum(find_max_joltage(bank, 2) for bank in banks)

def part2(banks):
    return sum(find_max_joltage(bank, 12) for bank in banks)
