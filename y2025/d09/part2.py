from tqdm import tqdm


def _line(c1, c2):
    l = []
    if c1[0] == c2[0]:
        for k in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
            l.append([c1[0], k])
    else:
        for k in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
            l.append([k, c1[1]])
    return l


def _perimeter(corners):
    perimeter = []

    for i in (range(len(corners))):
        c1 = corners[i]
        c2 = corners[(i + 1) % len(corners)]
        perimeter.extend(_line(c1, c2))

    perimeter_sorted = [list(s) for s in sorted(set(tuple(p) for p in perimeter))]
    return perimeter_sorted


def _read_and_parse(fname):
    with open(fname) as f_in:
        corners = [[int(e) for e in line.strip().split(',')] for line in f_in]
    corners_rev_xy = [[c[1], c[0]] for c in corners]
    return corners_rev_xy


def _is_internal(c, perimeter):
    left_wall = any(p[0] == c[0] and p[1] <= c[1] for p in perimeter)
    right_wall = any(p[0] == c[0] and p[1] >= c[1] for p in perimeter)
    up_wall = any(p[1] == c[1] and p[0] <= c[0] for p in perimeter)
    down_wall = any(p[1] == c[1] and p[0] >= c[0] for p in perimeter)
    internal = left_wall and right_wall and up_wall and down_wall
    return internal


def _find_largest_rectangle(corners, perimeter):
    largest_area = 0
    for c1 in tqdm(corners, desc='c1'):
        for c2 in tqdm(corners, desc='c2'):
            min_x = min(c1[0], c2[0])
            min_y = min(c1[1], c2[1])
            max_x = max(c1[0], c2[0])
            max_y = max(c1[1], c2[1])

            cc = [
                [min_x, min_y],
                [max_x, min_y],
                [max_x, max_y],
                [min_x, max_y]
            ]
            internals = [_is_internal(cc[i], perimeter) for i in range(4)]
            if all(internals):
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                largest_area = max(largest_area, area)
    return largest_area


def main(fname):
    corners = _read_and_parse(fname)
    perimeter = _perimeter(corners)
    largest_area = _find_largest_rectangle(corners, perimeter)
    return largest_area


if __name__ == '__main__':
    assert 24 == main('./test_data.txt')
    print(main('./data.txt'))
