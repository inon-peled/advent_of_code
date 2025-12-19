def _parse(fname):
    board = dict()
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
                    board[i, j] = '#'
    direction = 0
    return board, mid, mid, direction


def _affect_cell(board, r, c, total_infected):
    cell = board.get((r, c), '.')
    if cell == '.':
        board[r, c] = 'w'
    elif cell == 'w':
        board[r, c] = '#'
        total_infected += 1
    elif cell == '#':
        board[r, c] = 'f'
    else:
        board[r, c] = '.'
    return total_infected


def _next_direction(board, r, c, direction):
    cell = board.get((r, c), '.')

    if cell == '.':
        new_direction = (direction - 1) % 4
    elif cell == 'w':
        new_direction = direction
    elif cell == '#':
        new_direction = (direction + 1) % 4
    else:
        new_direction = (direction + 2) % 4

    return new_direction


def _simulate(num_bursts, board, r, c, direction):
    total_infected = 0

    for k in range(num_bursts):
        direction = _next_direction(board, r, c, direction)
        total_infected = _affect_cell(board, r, c, total_infected)

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

    if direction == 0:
        r -= 1
    elif direction == 1:
        c += 1
    elif direction == 2:
        r += 1
    else:
        c -= 1

    return total_infected


if __name__ == '__main__':
    assert 26 == main('./test.txt', 100)
    assert 2511944 == main('./test.txt', 10_000_000)
    print(main('./input.txt', 10_000_000))
