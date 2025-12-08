import math

# For testing purposes since example uses fewer connections
N = 1000

def parse(lines):
    junctions = [tuple(map(int, line.split(',')))
                 for line in lines.splitlines()]

    dists = []
    for idx, j0 in enumerate(junctions):
        for j1 in junctions[idx+1:]:
            dists.append((dist(j0, j1),j0,j1))
    dists.sort()

    return junctions, dists


def dist(j0, j1):
    d = 0
    for a,b in zip(j0, j1):
        c = a-b
        d += c*c
    return d

def part1(junctions):
    junctions, dists = junctions

    circuits = [set([j]) for j in junctions]
    for _, j0, j1 in dists[:N]:
        for i,c in enumerate(circuits):
            if j0 in c:
                i0 = i
            if j1 in c:
                i1 = i
        if i0 == i1:
            continue
        circuits[i0] |= circuits[i1]
        del circuits[i1]

    lengths = sorted(map(len, circuits), reverse=True)
    return math.prod(lengths[:3])


def part2(junctions):
    junctions, dists = junctions
    circuits = [set([j]) for j in junctions]

    for _, j0, j1 in dists:
        for i,c in enumerate(circuits):
            if j0 in c:
                i0 = i
            if j1 in c:
                i1 = i
        if i0 == i1:
            continue
        circuits[i0] |= circuits[i1]
        del circuits[i1]

        if len(circuits) == 1:
            break

    return j0[0] * j1[0]
