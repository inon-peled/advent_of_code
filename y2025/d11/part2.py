"""
Solution idea: the directed graphs are acyclic, so do a topological sort, go over the nodes in this order and count.
First, run from src to dac, then from dac to fft, then from fft to out.
Then also run from src to fft, then from fft to dac, then from dac to out.
"""

from collections import defaultdict


def _parse_to_graph(fname):
    graph = defaultdict(list)
    for line in open(fname):
        line = line.strip()
        s, ts = line.split(':')
        ts = ts.split()
        graph[s].extend(ts)
    return graph


def _detect_cycles(graph):
    graph = graph.copy()
    while graph:
        in_degrees = {v: 0 for v in graph}
        for lst in graph.values():
            for n in lst:
                in_degrees[n] = 0

        for v in graph:
            for u in graph[v]:
                in_degrees[u] += 1

        in_deg_zero = [v for v in graph if in_degrees[v] == 0]
        if not in_deg_zero:
            return True

        for v in in_deg_zero:
            graph.pop(v)

    return False


def _topological_sort(graph):
    graph = graph.copy()
    topological_order = []

    while graph:
        in_degrees = {v: 0 for v in graph}
        for lst in graph.values():
            for n in lst:
                in_degrees[n] = 0

        for v in graph:
            for u in graph[v]:
                in_degrees[u] += 1

        in_deg_zero = [v for v in graph if in_degrees[v] == 0]
        if not in_deg_zero:
            return None

        for v in in_deg_zero:
            topological_order.append(v)
            graph.pop(v)

    topological_order.append('out')
    return topological_order

def _fathers(node, graph):
    fs = []
    for v in graph:
        if node in graph[v]:
            fs.append(v)
    fs = set(fs)
    return fs

def _count_paths(graph, src, dst, counts, order):
    start_idx = order.index(src)
    end_idx = order.index(dst)
    nodes_to_visit = order[start_idx + 1:end_idx + 1]
    for node in nodes_to_visit:
        fathers = _fathers(node, graph)
        for f in fathers:
            counts[node] += counts[f]
        pass
    pass


def _count_sub_graph(graph, order, start, end, start_value):
    counts = {n: 0 for n in order}
    counts[start] = start_value
    _count_paths(graph, start, end, counts, order)
    return counts[end]


def _count_paths_with_constraints(order, mid1, mid2, graph):
    c1 = _count_sub_graph(graph, order, 'svr', mid1, 1)
    c2 = _count_sub_graph(graph, order, mid1, mid2, c1)
    c3 = _count_sub_graph(graph, order, mid2, 'out', c2)
    return c3


def main(fname):
    graph = _parse_to_graph(fname)
    order = _topological_sort(graph)
    c2 = _count_paths_with_constraints(order, 'fft', 'dac', graph)
    c1 = _count_paths_with_constraints(order, 'dac', 'fft', graph)
    solution = c1 + c2
    return solution


if __name__ == '__main__':
    assert not _detect_cycles(_parse_to_graph('./data.txt'))
    assert not _detect_cycles(_parse_to_graph('./test_data_part2.txt'))
    # print(_topological_sort(_parse_to_graph('./data.txt')))
    assert 2 == main('./test_data_part2.txt')
    print('Solution to part 2 is', main('./data.txt'))
