def _parse(fname):
    board = []
    with open(fname) as f:
        for line in f:
            board.append([int(e) for e in line.split()])
    return board

def solve(board):
    total = 0
    for row in board:
        mn = min(row)
        mx = max(row)
        diff = mx - mn
        total += diff
    return total


if __name__ == '__main__':
    assert 18 == solve(_parse('test1.txt'))
    print(solve(_parse('input.txt')))
