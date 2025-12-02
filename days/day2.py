import itertools

def parse(txt):
    ids = []
    chunks = txt.split(',')
    for c in chunks:
        ids.append(tuple(int(i) for i in c.split('-')))
    return ids

def invalid_id1(n):
    s = str(n)
    m = len(s) // 2
    return s[:m] == s[m:]


def invalid_id2(n):
    s = str(n)
    for l in range(1, len(s)//2+1):
        xs = list(itertools.batched(s, l))
        if all(map(lambda x: x == xs[0], xs)):
            return True
    return False


def solve(ids, func_id):
    s = 0
    for a, b in ids:
        for n in range(a,b+1):
            if func_id(n):
                s += n
    return s


def part1(ids):
    return solve(ids, invalid_id1)

def part2(ids):
    return solve(ids, invalid_id2)

