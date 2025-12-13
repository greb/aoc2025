import collections
import itertools
import functools


Machine = collections.namedtuple('Machine', ['lights', 'buttons', 'joltage'])


def parse_machine(line):
    tokens = line.split()
    lights = tuple(l == '#' for l in tokens[0][1:-1])
    buttons = [tuple(int(b) for b in bs[1:-1].split(',')) for
                     bs in tokens[1:-1]]
    joltage = tuple(int(j) for j in tokens[-1][1:-1].split(','))

    # Turn buttons into an adjacency matrix for easier handling
    buttons = [tuple(int(i in bs) for i in range(len(joltage)))
               for bs in buttons]
    return Machine(lights, buttons, joltage)


def parse(lines):
    return [parse_machine(line) for line in lines.splitlines()]


def check_lights(machine):
    # Tree search was too slow, even with a priority queue
    # Since a button is pressed only once at max (pressing twice does
    # nothing), it is enough to iterate through all button combinations
    for n in range(1, len(machine.buttons)+1):
        for pressed in itertools.combinations(machine.buttons, n):
            state = tuple(sum(bs) for bs in zip(*pressed))
            parity = tuple(bool(s%2) for s in state)
            if parity == machine.lights:
                return n

def part1(machines):
    return sum(check_lights(m) for m in machines)


def check_joltage(machine):
    costs = dict()
    # Null cost needed when all parities are even
    costs[(0,)*len(machine.joltage)] = 0
    for n in range(1, len(machine.buttons)+1):
        for pressed in itertools.combinations(machine.buttons, n):
            state = tuple(sum(bs) for bs in zip(*pressed))
            if state in costs:
                continue
            costs[state] = n

    @functools.cache
    def solve(joltage):
        if all(j == 0 for j in joltage):
            return 0
        result = sum(joltage)
        for state, cost in costs.items():
            if not all(s <= j and s%2 == j%2 for s,j in zip(state, joltage)):
                continue
            new_joltage = tuple((j-s)//2 for s,j in zip(state, joltage))
            result = min(result, cost + 2*solve(new_joltage))
        return result

    return solve(machine.joltage)


def part2(machines):
    return sum(check_joltage(m) for m in machines)
