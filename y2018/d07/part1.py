'''
Solution idea:
Initialize a heap with all the nodes that have in-degree zero.
While the heap is not empty:
1. Pop v from the heap and yield v as the next character.
2. Mark v as closed.
2. For every child u of v, if all the fathers of u are already closed, push u to the heap.
'''
from collections import defaultdict
from heapq import heappush, heappop, heapify


def _parse(fname):
    nodes = set()
    edges_out = defaultdict(set)
    edges_in = defaultdict(set)
    with open(fname) as f:
        for line in f:
            s = line.strip().split()
            src = s[1]
            dst = s[-3]
            nodes.add(src)
            nodes.add(dst)
            edges_out[src].add(dst)
            edges_in[dst].add(src)
    return nodes, edges_out, edges_in


def _dijkstra(nodes, edges_out, edges_in):
    closed = set()
    h = [v for v in nodes if v not in edges_in]
    heapify(h)
    while h:
        v = heappop(h)
        if v not in closed:
            closed.add(v)
            yield v
            neighbors = [u for u in edges_out[v] if not edges_in[u].difference(closed)]
            for n in neighbors:
                heappush(h, n)


def solve(fname):
    nodes, edges_out, edges_in = _parse(fname)
    answer = ''.join(_dijkstra(nodes, edges_out, edges_in))
    return answer


if __name__ == '__main__':
    assert 'CABDFE' == solve('test.txt')
    print(solve('input.txt'))
