def parse(lines):
    fresh, ingredients = lines.split('\n\n')
    fresh_ranges = []
    for f in fresh.splitlines():
        r = map(int, f.split('-'))
        fresh_ranges.append(tuple(r))
    ingredients = list(map(int, ingredients.splitlines()))

    return fresh_ranges, ingredients


def part1(inventory):
    fresh_ranges, ingredients = inventory

    cnt = 0
    for ing in ingredients:
        for a, b in fresh_ranges:
            if a <= ing <= b:
                cnt += 1
                break
    return cnt

def part2(inventory):
    fresh_ranges, ingredients = inventory

    # Algo only works if ranges are sorted
    fresh_ranges.sort()
    checked_ranges = []
    curr = fresh_ranges[0]
    for a,b in fresh_ranges[1:]:
        ca, cb = curr
        if ca <= a <= cb:
            # Merge ranges
            curr = ca, max(b, cb)
        else:
            checked_ranges.append(curr)
            curr = a,b
    checked_ranges.append(curr)

    cnt = 0
    for a,b in checked_ranges:
        cnt += b-a+1
    return cnt
