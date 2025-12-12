import re

def parse(lines):
    chunks = lines.split('\n\n')
    *shapes, raw_regions = chunks

    shapes = [s.splitlines()[1:] for s in shapes]
    regions = []
    for r in raw_regions.splitlines():
        w,h,*s = map(int, re.findall(r'\d+', r))
        regions.append((w,h,s))
    return shapes, regions


def part1(presents):
    shapes, regions = presents

    shapes_size = []
    for shape in shapes:
        size = sum(sum(c=='#' for c in l) for l in shape)
        shapes_size.append(size)

    count = 0
    for w, h, region in regions:
        # Exclude regions where total size of presents is already too large
        size = sum(shapes_size[i]*r for i,r in enumerate(region))
        if size > w*h:
            continue
        count += 1
<<<<<<< HEAD
=======

    # Ehm, it seems this day was a joke. No need to solve some NP-Complete
    # packing problem. Just naively look at the areas is enough.

>>>>>>> 06f88e3 (Add day 12)
    return count
