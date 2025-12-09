from tqdm import tqdm


def _print_board(board):
    for row in board:
        print(''.join(row))


def _build_board(corners, print_progress):
    max_x = max(c[0] for c in corners)
    max_y = max(c[1] for c in corners)
    pad_row = ['.'] * (max_y + 2)
    board = [pad_row[:] for i in range(max_x + 2)]

    for i in tqdm(range(len(corners))):
        c1 = corners[i]
        c2 = corners[(i + 1) % len(corners)]
        if c1[0] == c2[0]:
            for k in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
                board[c1[0]][k] = '#'
        else:
            for k in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
                board[k][c1[1]] = '#'
        if print_progress:
            print(f'\nIteration {i + 1}:')
            _print_board(board)

    for i in tqdm(range(len(board))):
        start = next((i for i, x in enumerate(board[i]) if x == '#'), None)
        end = next((i for i, x in reversed(list(enumerate(board[i]))) if x == '#'), None)
        if start is not None and end is not None:
            for j in range(start, end + 1):
                board[i][j] = '#'

    if print_progress:
        print(f'\nAfter filling:')
        _print_board(board)

    return board


def _read_and_parse(fname):
    with open(fname) as f_in:
        corners = [[int(e) for e in line.strip().split(',')] for line in f_in]
    corners_rev_xy = [[c[1], c[0]] for c in corners]
    return corners_rev_xy


def _find_largest_rectangle(corners, board):
    largest_area = 0
    for c1 in corners:
        for c2 in corners:
            min_x = min(c1[0], c2[0])
            min_y = min(c1[1], c2[1])
            max_x = max(c1[0], c2[0])
            max_y = max(c1[1], c2[1])
            if all(board[r][c] == '#' for c in range(min_y, max_y + 1) for r in range(min_x, max_x + 1)):
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                largest_area = max(largest_area, area)
    return largest_area


def main(fname, print_progress):
    corners = _read_and_parse(fname)
    board = _build_board(corners, print_progress)
    print('\nBoard created, now calculating largest rectangle...')
    largest_area = _find_largest_rectangle(corners, board)
    return largest_area


if __name__ == '__main__':
    # assert 24 == main('./test_data.txt', True)
    print(main('./data.txt', False))
