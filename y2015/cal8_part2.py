from json import dumps


def _read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines_clean = [l.rstrip() for l in lines]
    return lines_clean


def _process_one_string(s):
    len_string_code = len(s)
    s_encoded = dumps(s)
    len_encoded = len(s_encoded)
    diff = len_encoded - len_string_code
    return diff


def _solve(lines_clean):
    total_diff = 0
    for l in lines_clean:
        total_diff += _process_one_string(l)
    return total_diff


def main(filename):
    lines_clean = _read_input(filename)
    solution = _solve(lines_clean)
    return solution


def _test(test_filename):
    got = main(test_filename)
    assert got == 19
    print('\n----- Test passed -----')


if __name__ == '__main__':
    _test('test_data_c8.txt')
    print(main('data_c8.txt'))
