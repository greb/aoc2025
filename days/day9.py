import itertools

def sort_coords(pair):
    (x0,y0), (x1,y1) = pair
    return min(x0,x1), min(y0,y1), max(x0,x1), max(y0,y1)

def area(pair):
    (x0, y0), (x1, y1) = pair
    return (abs(x1-x0)+1) * (abs(y1-y0)+1)

def parse(lines):
    return [tuple(map(int,line.split(','))) for line in lines.splitlines()]

def part1(tiles):
    areas = []
    for pair in itertools.combinations(tiles,2):
        areas.append(area(pair))
    return max(areas)


def part2(tiles):
    perimeter = [sort_coords(pair) for pair
                 in itertools.pairwise(tiles + [tiles[0]])]

    areas = []
    for pair in itertools.combinations(tiles, 2):
        x0, y0, x1, y1 = sort_coords(pair)
        for px0, py0, px1, py1 in perimeter:
            if x0 < px1 and y0 < py1 and x1 > px0 and y1 > py0:
                break
        else:
            areas.append(area(pair))
    return max(areas)
