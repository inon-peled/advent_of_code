'''
Solution idea: the particle with the smallest magnitude of acceleration will eventually be closest to <0, 0, 0>.
If there are several such particles, then the one with the lowest velocity wins.
And if there are several such particles, then the one that starts closest to <0, 0, 0> wins.
'''


def _to_list(s):
    t = s.replace('a=<', '').replace('v=<', '').replace('p=<', '').replace('>', '')
    lst = [int(e) for e in t.split(',')]
    return lst


def _parse(fname):
    particles = []
    with open(fname) as f:
        for i, line in enumerate(f):
            p, v, a = line.split(', ')
            part = {'p': _to_list(p), 'v': _to_list(v), 'a': _to_list(a)}
            particles.append(part)
    return particles


def _sq(component):
    return sum(c ** 2 for c in component)


def solve(particles):
    sq = [{c: _sq(part[c]) for c in part} for part in particles]

    min_a = min(s['a'] for s in sq)
    min_v = min(s['v'] for s in sq)
    min_p = min(s['p'] for s in sq)
    mins = {'a': min_a, 'v': min_v, 'p': min_p}

    filtered = list(enumerate(sq))
    for c in ['a', 'v', 'p']:
        filtered = [s for s in filtered if s[1][c] == mins[c]]
        if len(filtered) == 1:
            winner = filtered[0]
            winner_idx = winner[0]
            return winner_idx


def main(fname):
    particles = _parse(fname)
    answer = solve(particles)
    return answer


if __name__ == '__main__':
    assert 0 == main('./test.txt')
    print(main('./input.txt'))