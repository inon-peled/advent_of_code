def _light_corners(board):
    n = len(board[0]) - 2
    board[1][n] = board[n][1] = board[1][1] = board[n][n] = '#'


def _num_neighbors_on(board_with_margins, i, j):
    neigh = []
    for i_diff in [-1, 0, 1]:
        for j_diff in [-1, 0, 1]:
            if not (i_diff == 0 and j_diff == 0):
                neigh.append(board_with_margins[i + i_diff][j + j_diff])

    num_on = neigh.count('#')
    return num_on


def _one_turn(board_with_margins):
    new_board_with_margins = [board_with_margins[i][:] for i in range(len(board_with_margins))]
    for i in range(1, len(board_with_margins) - 1):
        for j in range(1, len(board_with_margins[0]) - 1):
            num_on = _num_neighbors_on(board_with_margins, i, j)
            if board_with_margins[i][j] == '#':
                if num_on not in (2, 3):
                    new_board_with_margins[i][j] = '.'
            elif num_on == 3:
                new_board_with_margins[i][j] = '#'

    _light_corners(new_board_with_margins)
    return new_board_with_margins


def read_and_add_margins(fname):
    board = []

    with open(fname) as f:
        for line in f.readlines():
            board.append(['.'] + list(line.strip()) + ['.'])

    dummy_row = ['.'] * len(board[0])
    board = [dummy_row[:]] + board + [dummy_row[:]]
    return board


def print_board(board_with_margins):
    for row in board_with_margins:
        print(''.join(row))
    print()


def main(fname, num_turns, do_prints):
    board = read_and_add_margins(fname)
    _light_corners(board)
    if do_prints:
        print('\nInitially:\n')
        print_board(board)
    for i in range(num_turns):
        board = _one_turn(board)
        if do_prints:
            print(f'\nAfter {i + 1} steps:\n')
            print_board(board)

    final_on = sum(board[i][j] == '#' for i in range(len(board)) for j in range(len(board[0])))
    return final_on


if __name__ == '__main__':
    assert 17 == main('./test_data.txt', 5, True)
    print('\nSolution:\n')
    print(main('./data.txt', 100, False))
