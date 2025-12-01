M = 100

def parse(lines):
    return [ (s[0], int(s[1:])) for s in lines.splitlines()]

def part1(rots):
    pos = 50
    cnt = 0
    for d, n in rots:
        if d == 'R':
            pos = (pos+n) % M
        else:
            pos = (pos-n) % M
        if pos == 0:
            cnt += 1
    return cnt


def part2(rots):
    pos = 50
    cnt = 0
    for d, n in rots:
        r, n = divmod(n, M)
        cnt += r

        if d == 'R':
            if pos+n >= M:
                cnt += 1
            pos = (pos+n) % M
        else:
            if pos > 0 and (pos-n) <= 0:
                cnt += 1
            pos = (pos-n) % M

    return cnt
