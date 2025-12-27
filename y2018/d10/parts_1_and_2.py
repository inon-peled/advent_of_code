"""
Solution idea:
When the message appears, the points are relatively grouped together, namely, their bounding box is
small in comparison to other steps.
So simulate each step, and print the points at the end of a step whenever all the following hold:
* The current bounding box has an area smaller than the area in all previous steps.
* Each edge of the current bounding box is at most (num_points * 2 / 3) long.
"""


def _parse(fname):
    points = []
    with open(fname) as f:
        for line in f:
            s = (line
                 .strip()
                 .replace('position=<', '')
                 .replace('velocity=<', '')
                 .replace('>', '')
                 .split()
                 )
            pv = [int(e.replace(',', '')) for e in s]
            points.append(pv)
    return points


def _bbox_x_y(points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    return min_x, max_x, min_y, max_y


def _bounding_box_area(points):
    min_x, max_x, min_y, max_y = _bbox_x_y(points)
    area = (max_x - min_x) * (max_y - min_y)
    max_edge_length = max(
        max_x - min_x + 1,
        max_y - min_y + 1
    )
    return area, max_edge_length


def _advance(points):
    for p in points:
        p[0] += p[2]
        p[1] += p[3]


def _print_points(i, points):
    print(f'\n\n====================== After {i} Seconds ======================')
    points_set = set((p[0], p[1]) for p in points)
    min_x, max_x, min_y, max_y = _bbox_x_y(points)

    for y in range(min_y - 1, max_y + 2):
        print()
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in points_set:
                print('#', end='')
            else:
                print('.', end='')


def solve(points, max_iterations):
    n = len(points)
    min_bbox_area = None
    for i in range(max_iterations):
        bbox_area, max_edge_length = _bounding_box_area(points)
        if (min_bbox_area is None or bbox_area < min_bbox_area) and (max_edge_length <= 2 * n / 3):
            _print_points(i, points)
            min_bbox_area = bbox_area
        _advance(points)


def main(fname, max_iterations):
    points = _parse(fname)
    solve(points, max_iterations)


if __name__ == '__main__':
    main('./test.txt', 10 ** 3)
    main('./input.txt', 10 ** 5)
