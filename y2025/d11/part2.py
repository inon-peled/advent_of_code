from collections import defaultdict


def _parse_to_graph(fname):
    graph = defaultdict(list)
    for line in open(fname):
        line = line.strip()
        s, ts = line.split(':')
        ts = ts.split()
        graph[s].extend(ts)
    return graph


def _count_paths(graph, start, end, unvisited, constraints, path_so_far):
    if start == end:
        path_contains_all_constraints = all(c in path_so_far for c in constraints)
        return int(path_contains_all_constraints)
    if not unvisited:
        return 0

    unvisited = unvisited - {start}
    path_so_far = path_so_far + [start]
    remaining_neighbors = set(graph[start]) & unvisited
    total = 0
    for neighbor in remaining_neighbors:
        count = _count_paths(graph, neighbor, end, unvisited, constraints, path_so_far)
        total += count

    return total


def main(fname, start, end, constraints):
    graph = _parse_to_graph(fname)
    solution = _count_paths(graph, start, end, set(graph.keys() | {end}), constraints, [])
    return solution


if __name__ == '__main__':
    assert 2 == main('./test_data_part2.txt', 'svr', 'out', ['dac', 'fft'])
    print('Solution to part 2 is', main('./data.txt', 'svr', 'out', ['dac', 'fft']))
