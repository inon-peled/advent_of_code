'''
Solution idea:
Start from the center of the bounding box of all points.
Do BFS, and consider only neighbors that have total L1 distance less than the given bound.
Complexity: O(RD), where R is the size of the required region, and D is the number of data points.
'''
from collections import deque

DATA = [(162, 168), (86, 253), (288, 359), (290, 219), (145, 343), (41, 301), (91, 214), (166, 260), (349, 353),
        (178, 50), (56, 79), (273, 104), (173, 118), (165, 47), (284, 235), (153, 69), (116, 153), (276, 325),
        (170, 58), (211, 328), (238, 346), (333, 299), (119, 328), (173, 289), (44, 223), (241, 161), (225, 159),
        (266, 209), (293, 95), (89, 86), (281, 289), (50, 253), (75, 347), (298, 241), (88, 158), (40, 338), (291, 156),
        (330, 88), (349, 289), (165, 102), (232, 131), (338, 191), (178, 335), (318, 107), (335, 339), (153, 156),
        (88, 119), (163, 268), (159, 183), (162, 134)]
DATA_BOUND = 10_000

TEST = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
TEST_BOUND = 32


def _center_of_mass(data):
    bb = {
        'min_x': min(d[0] for d in data),
        'max_x': max(d[0] for d in data),
        'min_y': min(d[1] for d in data),
        'max_y': max(d[1] for d in data),
    }
    center_x = (bb['max_x'] - bb['min_x']) // 2
    center_y = (bb['max_y'] - bb['min_y']) // 2
    return center_x, center_y


def _total_l1(p, data):
    return sum(abs(p[0] - d[0]) + abs(p[1] - d[1]) for d in data)


def neighbors(x, y, data, bound):
    candidates = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]
    neigh = []
    for c in candidates:
        c_total_l1 = _total_l1(c, data)
        if c_total_l1 < bound:
            neigh.append(c)
    return neigh


def _bfs(start, bound, data):
    closed = set()
    q = deque([start])
    while q:
        v = q.popleft()
        if v not in closed:
            closed.add(v)
            neigh = neighbors(v[0], v[1], data, bound)
            for n in neigh:
                if n not in closed:
                    q.append(n)

    answer = len(closed)
    return answer


def solve(data, bound):
    start = _center_of_mass(data)
    answer = _bfs(start, bound, data)
    return answer


if __name__ == '__main__':
    assert 16 == solve(TEST, TEST_BOUND)
    print(solve(DATA, DATA_BOUND))
