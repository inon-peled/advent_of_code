import heapq
from functools import partial

FAV_NUM = 1352
START = (1, 1)
MAX_STEPS = 50


def _dijkstra_constrained(start, neighbors_func, max_dist):
    pq = [(0, start)]
    dist = {start: 0}
    prev = {}

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in neighbors_func(u):
            nd = d + 1
            if nd <= max_dist and nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    num_nodes_visited = len(dist)
    return num_nodes_visited


def _is_open_space(x, y, num):
    k = num + ((x * x) + (3 * x) + (2 * x * y) + y + (y * y))
    k_bin = bin(k)
    one_bits = k_bin.count('1')
    even = (one_bits % 2 == 0)
    return even


def _test():
    num = 10

    board = [
        ['.', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['.', '.', '#', '.', '.', '#', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
        ['#', '#', '#', '.', '#', '.', '#', '#', '#', '.'],
        ['.', '#', '#', '.', '.', '#', '.', '.', '#', '.'],
        ['.', '.', '#', '#', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '#', '#', '.', '#', '#', '#'],
    ]
    for i in range(len(board)):
        for j in range(len(board[0])):
            expected = (board[i][j] == '.')
            actual = _is_open_space(x=j, y=i, num=num)
            assert actual == expected

    cases = [
        (0, 1),
        (1, 3),
        (2, 5),
        (3, 6),
        (4, 9)
    ]
    neighbors_func = partial(_valid_neighbors, num=num)
    for case in cases:
        max_steps, expected = case
        actual = _dijkstra_constrained(start=START, neighbors_func=neighbors_func, max_dist=max_steps)
        assert actual == expected


def _valid_neighbors(location, num):
    n = []
    x, y = location
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for c in candidates:
        if c[0] >= 0 and c[1] >= 0 and _is_open_space(x=c[0], y=c[1], num=num):
            n.append(c)
    return n


def solve(num, start, max_steps):
    assert _is_open_space(start[0], start[1], num)

    neighbors_func = partial(_valid_neighbors, num=num)

    answer = _dijkstra_constrained(start=start, neighbors_func=neighbors_func, max_dist=max_steps)
    return answer


if __name__ == '__main__':
    _test()
    print('Part 2 solution is', solve(num=FAV_NUM, start=START, max_steps=MAX_STEPS))
