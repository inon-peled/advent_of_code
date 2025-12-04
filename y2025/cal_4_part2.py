ROLL_SYMBOL = '@'
EMPTY_SYMBOL = '.'


def _read_board(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    board = []
    for line in lines:
        board.append(list(line.strip()))
    return board


def _check_one_square(board, i, j):
    total_neighbor_rolls = 0

    if board[i][j] != ROLL_SYMBOL:
        return False

    for row_idx in [i - 1, i, i + 1]:
        if 0 <= row_idx < len(board):
            for col_idx in [j - 1, j, j + 1]:
                if (0 <= col_idx < len(board[0])) and not (row_idx == i and col_idx == j):
                    is_roll = (board[row_idx][col_idx] == ROLL_SYMBOL)
                    total_neighbor_rolls += is_roll

    is_accessible_to_forklift = (total_neighbor_rolls < 4)
    return is_accessible_to_forklift


def _do_one_round_of_elimination(board):
    eliminated_in_this_round = 0
    board_end_of_round = [r[:] for r in board]

    for i in range(len(board)):
        for j in range(len(board[i])):
            is_accessible = _check_one_square(board, i, j)
            if is_accessible:
                board_end_of_round[i][j] = EMPTY_SYMBOL
                eliminated_in_this_round += 1

    return eliminated_in_this_round, board_end_of_round


def _solve(board):
    total_accessible_squares = 0

    if not board:
        return total_accessible_squares

    assert all(len(row) == len(board[0]) for row in board)

    while True:
        eliminated_in_this_round, board_end_of_round = _do_one_round_of_elimination(board)
        if eliminated_in_this_round == 0:
            break
        board = board_end_of_round
        total_accessible_squares += eliminated_in_this_round

    return total_accessible_squares


def main(filename):
    board = _read_board(filename)
    solution = _solve(board)
    return solution


def _quick_test():
    test_solution = main('test_data_c4.txt')
    assert test_solution == 43


if __name__ == '__main__':
    _quick_test()
    print(main('data_c4.txt'))
