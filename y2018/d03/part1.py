from collections import defaultdict


def _add_to_board(line, board):
    s = line.split()
    y, x = [int(e) for e in s[2].replace(':', '').split(',')]
    w, h = [int(e) for e in s[3].split('x')]
    for i in range(x, x + h):
        for j in range(y, y + w):
            board[i, j] += 1


def solve(fname):
    board = defaultdict(int)
    with open(fname) as f:
        for line in f:
            _add_to_board(line, board)

    answer = sum(v > 1 for v in board.values())
    return answer


if __name__ == '__main__':
    assert 4 == solve('test.txt')
    print(solve('input.txt'))
