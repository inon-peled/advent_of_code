from collections import defaultdict


def _parse_to_graph(fname):
    graph = defaultdict(list)
    for line in open(fname):
        line = line.strip()
        s, ts = line.split(':')
        ts = ts.split()
        graph[s].extend(ts)
    return graph


def _count_paths(graph, start, end, unvisited, path_so_far):
    if start == end:
        return 1
    if not unvisited:
        return 0

    unvisited = unvisited - {start}
    path_so_far = path_so_far + [start]
    remaining_neighbors = set(graph[start]) & unvisited
    total = 0
    for neighbor in remaining_neighbors:
        total += _count_paths(graph, neighbor, end, unvisited - {neighbor}, path_so_far)
    return total


def main(fname, start, end):
    graph = _parse_to_graph(fname)
    solution = _count_paths(graph, start, end, set(graph.keys()) | {end}, [])
    return solution


if __name__ == '__main__':
    assert 5 == main('./test_data_part1.txt', 'you', 'out')
    print('Solution to part 1 is', main('./data.txt', 'you', 'out'))
