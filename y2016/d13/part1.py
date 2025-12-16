import heapq
from functools import partial

FAV_NUM = 1352
START = (1, 1)


def _dijkstra(start, goal, neighbors_func):
    pq = [(0, start)]
    dist = {start: 0}
    prev = {}

    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            return d
        if d > dist[u]:
            continue
        for v in neighbors_func(u):
            nd = d + 1
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return None


def _is_open_space(x, y, num):
    k = num + ((x * x) + (3 * x) + (2 * x * y) + y + (y * y))
    k_bin = bin(k)
    one_bits = k_bin.count('1')
    even = (one_bits % 2 == 0)
    return even


def _test():
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
            actual = _is_open_space(x=j, y=i, num=10)
            assert actual == expected


def _valid_neighbors(location, num):
    n = []
    x, y = location
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for c in candidates:
        if c[0] >= 0 and c[1] >= 0 and _is_open_space(x=c[0], y=c[1], num=num):
            n.append(c)
    return n


def solve(num, start, goal):
    assert _is_open_space(start[0], start[1], num)
    assert _is_open_space(goal[0], goal[1], num)

    neighbors_func = partial(_valid_neighbors, num=num)
    answer = _dijkstra(start=start, goal=goal, neighbors_func=neighbors_func)
    return answer


if __name__ == '__main__':
    _test()
    assert 11 == solve(num=10, start=START, goal=(7, 4))
    print('Part 1 solution is', solve(num=FAV_NUM, start=START, goal=(31, 39)))
