"""
Solution idea: as seen in hexgrid.png, the position of every hexagonal tile can be described as a 3-dim tuple,
relative to the start tile.
These 3-dim tuple corresponds to a system of 3 axes that partition the space into six regions,
corresponding to the six edges of the start tile.
To simulate the walk, start from (0, 0, 0), and in each step, change each coordinate per the tiles in
the first ring in the png.
When reaching the final tile (x, y, z), the largest among {|x|, |y|, |z|} if the number of steps required to reach it.
"""


def _walk(route_str):
    route = route_str.split(',')
    pos = [0, 0, 0]
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

    answer = max(abs(c) for c in pos)
    return answer


def solve(fname):
    with open(fname) as f:
        route_str = f.read()
        answer = _walk(route_str)
        return answer


if __name__ == '__main__':
    assert 3 == _walk('ne,ne,ne')
    assert 0 == _walk('ne,ne,sw,sw')
    assert 2 == _walk('ne,ne,s,s')
    assert 3 == _walk('se,sw,se,sw,sw')
    print(solve('./input.txt'))
