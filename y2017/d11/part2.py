def _walk(route_str):
    route = route_str.split(',')
    pos = [0, 0, 0]
    max_abs_coord = 0
    directions = {
        'n': [0, -1, 1],
        'ne': [1, -1, 0],
        'se': [1, 0, -1],
        's': [0, 1, -1],
        'sw': [-1, 1, 0],
        'nw': [-1, 0, 1],
    }

    for r in route:
        d = directions[r]
        pos = [pos[0] + d[0], pos[1] + d[1], pos[2] + d[2]]
        max_abs_coord = max(max_abs_coord, max(abs(c) for c in pos))

    return max_abs_coord


def solve(fname):
    with open(fname) as f:
        route_str = f.read()
        answer = _walk(route_str)
        return answer


if __name__ == '__main__':
    assert 3 == _walk('ne,ne,ne')
    assert 2 == _walk('ne,ne,sw,sw')
    assert 2 == _walk('ne,ne,s,s')
    assert 3 == _walk('se,sw,se,sw,sw')
    print(solve('./input.txt'))
