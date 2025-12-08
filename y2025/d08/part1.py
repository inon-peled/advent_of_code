from collections import defaultdict

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


def _lengths_sorted(circuits):
    lengths = defaultdict(int)

    for i in range(len(circuits)):
        c = circuits[i]
        lengths[c] += 1

    lengths_sorted = sorted(lengths.values(), reverse=True)
    if PRINT_DEBUG:
        print(f'There are {len(lengths_sorted)} circuits:\n\t{list(lengths.items())}\n\t{lengths_sorted=}\n')

    return lengths_sorted


def _prod_longest_lengths(circuits, num_longest):
    sorted_lengths = _lengths_sorted(circuits)
    longest = sorted_lengths[:num_longest]
    prod = 1
    for length in longest:
        prod *= length
    return prod


def main(fname, max_connections, num_longest):
    points = read_and_parse(fname)
    circuits = list(range(len(points)))
    pairs = _sorted_pairs(points)

    connections_made = 0
    t = 0
    while connections_made < max_connections:
        pr = pairs[t]
        if circuits[pr[1]] != circuits[pr[0]]:
            circuits[pr[1]] = circuits[pr[0]]
            connections_made += 1

        t += 1
        if PRINT_DEBUG:
            print(f'Turn {t}:\nPair {pr} = {points[pr[0]]} and {points[pr[1]]}')
            print('Connections so far:', connections_made)
            _lengths_sorted(circuits)

    if PRINT_DEBUG:
        print('Final state:')

    solution = _prod_longest_lengths(circuits, num_longest)
    return solution


if __name__ == '__main__':
    assert 40 == main('./test_data.txt', 10, 3)
