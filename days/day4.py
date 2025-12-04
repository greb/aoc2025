def parse(lines):
    rolls = set()
    for y, line in enumerate(lines.splitlines()):
        for x, c in enumerate(line):
            if c == '@':
                rolls.add((x,y))
    return rolls

def neighbors(pos):
    deltas = [(1,0), (1,1), (0,1),(-1,1),
             (-1,0), (-1,-1), (0,-1), (1,-1)]

    for delta in deltas:
        x, y = zip(pos, delta)
        yield (sum(x), sum(y))


def part1(rolls):
    cnt = 0
    for roll in rolls:
        adj_rolls = rolls & set(neighbors(roll))
        if len(adj_rolls) < 4:
            cnt += 1
    return cnt


def part2(rolls):
    cnt = 0
    while True:
        removed = set()
        for roll in rolls:
            adj_rolls = rolls & set(neighbors(roll))
            if len(adj_rolls) < 4:
                removed.add(roll)
        if len(removed) == 0:
            break
        print(len(removed))
        rolls -= removed
        cnt += len(removed)
    return cnt
