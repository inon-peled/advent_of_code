def _parse(fname):
    board = []
    with open(fname) as f:
        for line in f:
            board.append([int(e) for e in line.split()])
    return board

def solve(board):
    total = 0
    for row in board:
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                n1 = row[i]
                n2 = row[j]
                mx = max(n1, n2)
                mn = min(n1, n2)
                if mx % mn == 0:
                    total += (mx // mn)
    return total


if __name__ == '__main__':
    assert 9 == solve(_parse('test2.txt'))
    print(solve(_parse('input.txt')))
