def _to_num(s):
    return int(s[:-1])


def _parse(fname):
    files = dict()
    for i, line in enumerate(open(fname)):
        if i < 2:
            continue
        path, size, used, avail, use_percent = line.split()
        path_parsed = tuple(
            int(e) for e in
            path[len('/dev/grid/node-'):].replace('x', '').replace('y', '').split('-')
        )
        files[path_parsed] = {
            'size': _to_num(size),
            'used': _to_num(used),
            'avail': _to_num(avail),
            'use_percent': _to_num(use_percent)
        }
    return files


def solve(files):
    max_x = max(p[0] for p in files)
    payload = files[max_x, 0]['used']
    possible = [kv for kv in files.items() if kv[1]['size'] >= payload]
    assert len(possible) == len(files)

    empty = list(filter(
        (lambda kv: kv[1]['used'] == 0),
        files.items()
    ))
    assert len(empty) == 1
    empty_x, empty_y = empty[0][0]

    max_x = max(p[0] for p in files)
    assert max_x >= 2 and empty_x < max_x

    answer = empty_y  # Move empty up all the way to the top
    answer += (max_x - empty_x)  # Move empty right all the way to the rightmost column
    # Repeatedly half-loop around the goal, until the goal reaches its final position in the top-left corner.
    # The number of repetitions is the remaining distance between the goal and the top-left corner.
    # Each half loop is 5 steps: 4 to loop back up-left + 1 to swap with the goal.
    answer += (max_x - 1) * 5
    return answer


def main(fname):
    files = _parse(fname)
    answer = solve(files)
    return answer


if __name__ == '__main__':
    assert 7 == main('./test_data.txt')
    print(main('./input.txt'))
