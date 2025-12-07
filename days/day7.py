import collections

def parse(lines):
    lines = lines.splitlines()
    start = lines[0].index('S')
    splitters = [set(p for p,c in enumerate(line) if c == '^')
                 for line in lines[2::2]]

    return start, splitters

def part1(manifold):
    start, splitters = manifold
    beams = [start]

    n_splits = 0
    for split in splitters:
        new_beams = []
        for beam in beams:
            if beam in split:
                new_beams.append((beam+1))
                new_beams.append((beam-1))
                n_splits += 1
            else:
                new_beams.append(beam)
        beams = set(new_beams)
    return n_splits


def part2(manifold):
    start, splitters = manifold
    beams = [start]

    beams = {start: 1}
    for split in splitters:
        new_beams = collections.defaultdict(int)
        for beam, cnt in beams.items():
            if beam in split:
                new_beams[beam-1] += cnt
                new_beams[beam+1] += cnt
            else:
                new_beams[beam] += cnt
        beams = new_beams
    return sum(beams.values())
