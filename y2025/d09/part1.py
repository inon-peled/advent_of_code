def _read_and_parse(fname):
    with open(fname) as f_in:
        corners = [[int(e) for e in line.strip().split(',')] for line in f_in]
    return corners


def _find_largest_rectangle(corners):
    largest_area = 0
    for c1 in corners:
        for c2 in corners:
            min_x = min(c1[0], c2[0])
            min_y = min(c1[1], c2[1])
            max_x = max(c1[0], c2[0])
            max_y = max(c1[1], c2[1])
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            largest_area = max(largest_area, area)
    return largest_area


def main(fname):
    corners = _read_and_parse(fname)
    largest_area = _find_largest_rectangle(corners)
    return largest_area


if __name__ == '__main__':
    assert 50 == main('./test_data.txt')
    print(main('./data.txt'))
