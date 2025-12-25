from collections import defaultdict


def _add_to_board(line, board):
    s = line.split()
    claim_id = s[0].replace('#', '')
    y, x = [int(e) for e in s[2].replace(':', '').split(',')]
    w, h = [int(e) for e in s[3].split('x')]
    for i in range(x, x + h):
        for j in range(y, y + w):
            board[i, j] += 1
    return claim_id, x, y, w, h


def _find_non_overlapping(board, claims):
    for c in claims:
        claim_id, x, y, w, h = c
        found = True
        for i in range(x, x + h):
            for j in range(y, y + w):
                if board[i, j] != 1:
                    found = False
        if found:
            return claim_id


def solve(fname):
    board = defaultdict(int)
    claims = []
    with open(fname) as f:
        for line in f:
            claims.append(_add_to_board(line, board))

    answer = int(_find_non_overlapping(board, claims))
    return answer


if __name__ == '__main__':
    assert 3 == solve('test.txt')
    print(solve('input.txt'))
