import functools

def parse(lines):
    conns = dict()
    for line in lines.splitlines():
        server, out = line.split(': ')
        conns[server] = out.split()
    conns['out'] = []
    return conns


def count_paths(src, dst, conns):
    @functools.cache
    def _inner(src, dst):
        if src == dst:
            return 1
        else:
            return sum(_inner(nxt, dst) for nxt in conns[src])
    return _inner(src,dst)

def part1(conns):
    return count_paths('you', 'out', conns)


def part2(conns):
    c = lambda s,d: count_paths(s, d, conns)
    return (c('svr', 'dac') * c('dac', 'fft') * c('fft', 'out') +
            c('svr', 'fft') * c('fft', 'dac') * c('dac', 'out'))

