import collections
import itertools
from scipy.optimize import linprog


Machine = collections.namedtuple('Machine', ['lights', 'buttons', 'joltage'])


def parse_machine(line):
    tokens = line.split()
    lights = [l == '#' for l in tokens[0][1:-1]]
    buttons = [tuple(int(b) for b in bs[1:-1].split(',')) for
                     bs in tokens[1:-1]]
    joltage = tuple(int(j) for j in tokens[-1][1:-1].split(','))
    return Machine(lights, buttons, joltage)


def parse(lines):
    return [parse_machine(line) for line in lines.splitlines()]


def press_buttons(machine):
    # Tree search was too slow, even with a priority queue
    # Since a button is pressed only once at max (pressing twice does
    # nothing), it is enough to iterate through all button combinations
    for n in range(1, len(machine.buttons)):
        for pressed in itertools.combinations(machine.buttons, n):
            state = [sum(i in p for p in pressed)
                     for i in range(len(machine.lights))]
            state = [bool(i%2) for i in state]
            if state == machine.lights:
                return n


def part1(machines):
    return sum(map(press_buttons, machines))

def find_min_joltage(machine):
    c = [1 for _ in machine.buttons]
    A = [[i in b for b in machine.buttons]
         for i in range(len(machine.joltage))]
    total = linprog(c, A_eq=A, b_eq=machine.joltage, integrality=1,
                    options={'disp': False}).fun
    return int(total)


def part2(machines):
    return sum(map(find_min_joltage, machines))
