FIRST_CODE = 20151125
FINAL_ROW = 2978
FINAL_COL = 3083


def _simulate_one_diagonal(diag_num, last_code):
    diag = []
    for i in range(diag_num):
        last_code = (last_code * 252533) % 33554393
        diag.append(last_code)
    return diag


def solve(first_code, final_row, final_col):
    if final_row == final_col == 1:
        return first_code

    last_code = first_code
    final_diag = final_row + final_col - 1

    for i in range(2, final_diag + 1):
        diag = _simulate_one_diagonal(i, last_code)
        last_code = diag[-1]

    solution = diag[final_col - 1]
    return solution


def _quick_test():
    expected_diagonals = [
        [20151125],
        [31916031, 18749137],
        [16080970, 21629792, 17289845],
        [24592653, 8057251, 16929656, 30943339],
        [77061, 32451966, 1601130, 7726640, 10071777],
        [33071741, 17552253, 21345942, 7981243, 15514188, 33511524]
    ]

    for i in range(1, len(expected_diagonals)):
        expected = expected_diagonals[i]
        got = _simulate_one_diagonal(i + 1, expected_diagonals[i - 1][-1])
        assert got == expected, f'Expected {expected} but got {got}'

    expected_mat = [
        [20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
        [31916031, 21629792, 16929656, 7726640, 15514188, 4041754],
        [16080970, 8057251, 1601130, 7981243, 11661866, 16474243],
        [24592653, 32451966, 21345942, 9380097, 10600672, 31527494],
        [77061, 17552253, 28094349, 6899651, 9250759, 31663883],
        [33071741, 6796745, 25397450, 24659492, 1534922, 27995004],
    ]

    for i in range(len(expected_diagonals)):
        for j in range(len(expected_diagonals[0])):
            expected = expected_mat[i][j]
            got = solve(FIRST_CODE, i + 1, j + 1)
            assert expected == got, f'Expected {expected} but got {got}'

    print('\n------ Quick test passed successfully ------')


if __name__ == '__main__':
    _quick_test()
    main_solution = solve(FIRST_CODE, FINAL_ROW, FINAL_COL)
    print(f'\nSolution: {main_solution}')
