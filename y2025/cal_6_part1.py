def _read_and_parse_input_file(filename):
    exercises = None
    with open(filename) as f_in:
        for line in f_in.readlines():
            line_items = line.split()
            if exercises is None:
                exercises = [[] for _ in range(len(line_items))]
            for i, item in enumerate(line_items):
                exercises[i].append(item)

    for ex in exercises:
        for i in range(len(ex) - 1):
            ex[i] = int(ex[i])

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
    expected = 4277556
    assert expected == got
    print('\n------- Test passed -------')


if __name__ == '__main__':
    _test('test_data_c6.txt')
    print(main('data_c6.txt'))
