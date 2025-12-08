PRINT_DEBUG = True


def read_and_parse(fname):
    data = open(fname).readlines()
    parsed = [[int(e) for e in d.split(',')] for d in data]
    return parsed


def _dist_sq(u, v):
    return (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2 + (u[2] - v[2]) ** 2


def _sorted_pairs(points):
    pairs = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            pairs.append((i, j))
    pairs_sorted = sorted(pairs, key=lambda ij: _dist_sq(points[ij[0]], points[ij[1]]))
    return pairs_sorted


def _lengths_sorted(union_find):
    lengths = [len(union_find[k]) for k in union_find]
    lengths_sorted = sorted(lengths, reverse=True)
    if PRINT_DEBUG:
        print(f'\t{union_find=}\n\t{lengths=}\n\t{lengths_sorted=}\n')
    return lengths_sorted


def _prod_longest_lengths(union_find, num_longest):
    sorted_lengths = _lengths_sorted(union_find)
    longest = sorted_lengths[:num_longest]
    prod = 1
    for length in longest:
        prod *= length
    return prod


def _find_rep(union_find, u):
    for v in union_find:
        if u in union_find[v]:
            return v
    return None

def _do_union(u, v, union_find):
    u_rep = _find_rep(union_find, u)
    v_rep = _find_rep(union_find, v)
    if u_rep != v_rep:
        union_find[u_rep].extend(union_find[v_rep])
        union_find.pop(v_rep)


def main(fname, max_connections, num_longest):
    points = read_and_parse(fname)
    union_find = {i: [i] for i in range(len(points))}
    pairs = _sorted_pairs(points)

    for t in range(max_connections):
        pr = pairs[t]
        _do_union(pr[0], pr[1], union_find)
        if PRINT_DEBUG:
            print(f'Turn {t + 1}:\nPair {pr} = {points[pr[0]]} and {points[pr[1]]}')
            _lengths_sorted(union_find)

    if PRINT_DEBUG:
        print('Final state:')

    expected = list(range(len(points)))
    actual = sorted(sum(union_find.values(), []))
    assert expected == actual, f'\nExpected\n\t{expected}\n\tbut got\n\t{actual}'

    solution = _prod_longest_lengths(union_find, num_longest)
    return solution


if __name__ == '__main__':
    assert 40 == main('./test_data.txt', 10, 3)
    sol = main('./data.txt', 1000, 3)
    print('\nSolution is', sol)
