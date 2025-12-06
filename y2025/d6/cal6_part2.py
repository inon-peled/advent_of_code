def _parse_one_column(exercises, j):
    col = []
    for i in range(len(exercises)):
        col.append(exercises[i][j])
    return col


def _parse_one_exercise(exercises, j):
    ex = []
    operator = ''
    while j < len(exercises[0]):
        col = _parse_one_column(exercises, j)
        if col[-1] != ' ':
            operator = col[-1]

        j += 1
        if all(c == ' ' for c in col):
            break

        ex.append(int(''.join(col[:-1])))

    ex.append(operator)
    return ex, j


def _read_and_parse_input_file(filename):
    with open(filename) as f_in:
        exercises_raw = [list(line) for line in f_in.readlines()]

    for i in range(len(exercises_raw)):
        while exercises_raw[i][-1]  in ['\r', '\n']:
            exercises_raw[i] = exercises_raw[i][:len(exercises_raw[i]) - 1]

    possible_len_diff_in_last_row = len(exercises_raw[0]) - len(exercises_raw[-1])
    if possible_len_diff_in_last_row > 0:
        exercises_raw[-1] = exercises_raw[-1] + ([' '] * possible_len_diff_in_last_row)

    j = 0
    exercises = []
    while j < len(exercises_raw[0]):
        ex, j = _parse_one_exercise(exercises_raw, j)
        exercises.append(ex)

    return exercises


def _solve(exercises):
    total = 0

    for ex in exercises:
        op = ex[-1]
        ex_total = ex[0]
        for i in range(1, len(ex) - 1):
            if op == '+':
                ex_total += ex[i]
            else:
                ex_total *= ex[i]
        total += ex_total

    return total


def main(filename):
    exercises = _read_and_parse_input_file(filename)
    solution = _solve(exercises)
    return solution


def _test(test_filename):
    got = main(test_filename)
    expected = 3263827
    assert expected == got
    print('\n------- Test passed -------')


if __name__ == '__main__':
    _test('test_data_c6.txt')
    print(main('data_c6.txt'))
