import operator
import functools

def parse(lines):
    op = {'+': operator.add, '*': operator.mul}
    lines = lines.splitlines()
    *nums, ops = lines
    ops = [op[o] for o in ops.split()]
    return nums, ops

def total(nums, ops):
    t = 0
    for n,o in zip(nums, ops):
        t += functools.reduce(o, n)
    return t


def part1(problems):
    nums, ops = problems
    nums = [[int(n) for n in line.split()] for line in nums]
    nums = zip(*nums)
    return total(nums, ops)


def part2(problems):
    nums, ops = problems

    nums = [''.join(line).strip() for line in zip(*nums)]
    grouped_nums = []
    curr = []
    for num in nums:
        if num == '':
            grouped_nums.append(curr)
            curr = []
        else:
            curr.append(int(num))
    grouped_nums.append(curr)

    return total(grouped_nums, ops)

