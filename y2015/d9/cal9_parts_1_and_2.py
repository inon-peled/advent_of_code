from collections import defaultdict
from itertools import permutations


def _read_and_convert_to_graph(filename):
    g = defaultdict(dict)
    with open(filename) as f_in:
        for line in f_in:
            e, w = line.strip().split(' = ')
            u, v = e.split(' to ')
            g[u][v] = int(w)
            g[v][u] = int(w)
    return g


def _total_one_route(r, g):
    total = 0
    for i in range(len(r) - 1):
        u = r[i]
        v = r[i + 1]
        w = g[u][v]
        total += w
    return total


def _solve(g, part_num):
    best_total = None
    for perm in permutations(g.keys()):
        perm_total = _total_one_route(r=perm, g=g)
        found_better = ((best_total is None) or
                        ((perm_total < best_total) if part_num == 1 else (perm_total > best_total)))
        if found_better:
            best_total = perm_total
    return best_total


def _quick_test(test_filename):
    got1 = main(test_filename, 1)
    expected1 = 605
    assert got1 == expected1

    got2 = main(test_filename, 2)
    expected2 = 982
    assert got2 == expected2

    print('\n------ Test passed -----')


def main(filename, part_num):
    g = _read_and_convert_to_graph(filename)
    solution = _solve(g, part_num)
    return solution


if __name__ == '__main__':
    _quick_test('test_data_c9.txt')
    print('\nPart 1 solution:', main('data_c9.txt', 1))
    print('\nPart 2 solution:', main('data_c9.txt', 2))
