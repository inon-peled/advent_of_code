"""
Solution idea:
Form a graph, where each point is a node, and two nodes are connected
by an edge if-and-only-if their distance is at most 3.
The constellations are then the connected components in the graph -- use BFS to find them.
"""
from collections import defaultdict, deque

MAX_MANHATTAN_DIST = 3


def _manhattan_distance(p1, p2):
    assert len(p1) == len(p2)
    d_sq = sum(abs(p1[i] - p2[i]) for i in range(len(p1)))
    return d_sq


def _parse(fname):
    nodes = []
    for line in open(fname):
        point = tuple(int(e) for e in line.strip().split(','))
        nodes.append(point)

    edges = defaultdict(list)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist_sq = _manhattan_distance(nodes[i], nodes[j])
            if dist_sq <= MAX_MANHATTAN_DIST:
                edges[nodes[i]].append(nodes[j])
                edges[nodes[j]].append(nodes[i])

    return nodes, edges


def _bfs(nodes, edges):
    visited = set()
    if not nodes:
        return visited

    start = next(iter(nodes))
    d = deque([start])

    while d:
        v = d.popleft()
        visited.add(v)
        neighbors = edges[v]
        for u in neighbors:
            if u not in visited:
                d.append(u)

    return visited


def solve(nodes, edges):
    remaining = {p for p in nodes}
    visited = set()
    num_ccs = 0

    while remaining:
        cc = _bfs(remaining, edges)
        visited.update(cc)
        remaining -= cc
        num_ccs += 1

    return num_ccs


def main(fname):
    nodes, edges = _parse(fname)
    answer = solve(nodes, edges)
    return answer


if __name__ == '__main__':
    assert 2 == main('test1.txt')
    assert 4 == main('test2.txt')
    assert 3 == main('test3.txt')
    assert 8 == main('test4.txt')
    print(main('input.txt'))
