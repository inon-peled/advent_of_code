'''
Solution idea: the board is a sparse matrix, so store only the infected locations in a set.
'''


def _parse(fname):
    board = set()
    i = -1
    mid = None
    with open(fname) as f:
        for line in f:
            line = line.strip()
            i += 1
            if i == 0:
                mid = len(line) // 2
            for j in range(len(line)):
                if line[j] == '#':
                    board.add((i, j))
    direction = 0
    return board, mid, mid, direction


def _simulate(num_bursts, board, r, c, direction):
    total_infected = 0

    for k in range(num_bursts):
        if (r, c) in board:
            direction = (direction + 1) % 4
            board.remove((r, c))
        else:
            direction = (direction - 1) % 4
            board.add((r, c))
            total_infected += 1

        if direction == 0:
            r -= 1
        elif direction == 1:
            c += 1
        elif direction == 2:
            r += 1
        else:
            c -= 1

    return total_infected


def main(fname, num_bursts):
    board, r, c, direction = _parse(fname)
    total_infected = _simulate(num_bursts, board, r, c, direction)
    return total_infected


if __name__ == '__main__':
    # assert 0 == main('./test.txt', 0)
    # assert 1 == main('./test.txt', 1)
    # assert 5 == main('./test.txt', 7)
    # assert 41 == main('./test.txt', 70)
    # assert 5587 == main('./test.txt', 10000)
    print(main('./input.txt', 10000))
