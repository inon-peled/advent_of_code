'''
Solution idea:
This is a Voronoi diagram in L1, not Euclidean distance. So:
1. Form a bounding box.
2. Do multi-source BFS from the data points, namely:
2.1. Initialize the FIFO with all the data points.
2.2. Continue BFS:
2.2.1. Keep track of source root and min. distance from it.
2.2.2. When reaching an already closed point from a different source with the same min. distance,
       change the root of p to '.'.
3. Remove all data points that lie on the edges of the bounding box -- these are the data points with infinitely
   large Voronoi cells.
4. Output the largest number locations that were reached from the same root.
'''
from collections import deque, defaultdict

DATA = [(162, 168), (86, 253), (288, 359), (290, 219), (145, 343), (41, 301), (91, 214), (166, 260), (349, 353),
        (178, 50), (56, 79), (273, 104), (173, 118), (165, 47), (284, 235), (153, 69), (116, 153), (276, 325),
        (170, 58), (211, 328), (238, 346), (333, 299), (119, 328), (173, 289), (44, 223), (241, 161), (225, 159),
        (266, 209), (293, 95), (89, 86), (281, 289), (50, 253), (75, 347), (298, 241), (88, 158), (40, 338), (291, 156),
        (330, 88), (349, 289), (165, 102), (232, 131), (338, 191), (178, 335), (318, 107), (335, 339), (153, 156),
        (88, 119), (163, 268), (159, 183), (162, 134)]
TEST = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
MINI_TEST = [(1, 1), (1, 3)]


def _bounding_box(data):
    bb = {
        'min_x': min(d[0] for d in data),
        'max_x': max(d[0] for d in data),
        'min_y': min(d[1] for d in data),
        'max_y': max(d[1] for d in data),
    }
    return bb


def neighbors(x, y, bb):
    candidates = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]
    neigh = []
    for c in candidates:
        if (bb['min_x'] <= c[0] <= bb['max_x']) and (bb['min_y'] <= c[1] <= bb['max_y']):
            neigh.append(c)
    return neigh


def _l1(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def _multi_source_bfs(data, bb):
    closed = {(x, y): (0, x, y) for x, y in data}
    q = deque([(0, x, y, x, y) for i, (x, y) in enumerate(data)])

    while q:
        d, x, y, root_x, root_y = q.popleft()
        neigh = neighbors(x, y, bb)
        for n in neigh:
            n_dist = _l1(n, (root_x, root_y))
            if n not in closed:
                closed[n] = n_dist, root_x, root_y
                q.append((n_dist, n[0], n[1], root_x, root_y))
                pass
            else:
                prev_dist = closed[n][0]
                prev_root = closed[n][1:]
                if prev_dist is None:
                    continue
                if prev_dist == n_dist and prev_root != (root_x, root_y):
                    closed[n] = None, None, None
                    pass

    return closed


def _areas_in_bbox(closed):
    areas = defaultdict(int)
    for _, root_x, root_y in closed.values():
        areas[root_x, root_y] += 1
    return areas


def _remove_infinite(areas, bb):
    finite = {}
    for x, y in areas:
        if (x == bb['min_x']) or (x == bb['max_x']) or (y == bb['min_y']) or (y == bb['max_y']):
            continue
        finite[x, y] = areas[x, y]
    return finite


def solve(data):
    bb = _bounding_box(data)
    closed = _multi_source_bfs(data, bb)
    areas = _areas_in_bbox(closed)
    finite_areas = _remove_infinite(areas, bb)
    max_finite_area = max(finite_areas.values())
    return max_finite_area


if __name__ == '__main__':
    assert 17 == solve(TEST)
    print(solve(DATA))
