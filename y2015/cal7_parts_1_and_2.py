"""
Solution idea: recursively traverse the circuit (graph) backwards from the target wire to all its sources,
using explicit values as base cases.
"""

BINARY_MASK = 0xFFFF

BINARY_OPERATORS = [' AND ', ' OR ', ' LSHIFT ', ' RSHIFT ']

DEBUG_FLAG = False

MEMO = dict()


def _debug_print(msg):
    if DEBUG_FLAG:
        print('DEBUG: ', msg)


def _read_input(filename):
    with open(filename) as f_input:
        lines = [l.rstrip() for l in f_input.readlines()]

    return lines


def _parse(lines):
    parsed = dict()

    for l in lines:
        s, t = l.split(' -> ')
        parsed[t] = s

    return parsed


def _binary_operation(parsed, operator, s):
    op1, op2 = s.split(operator)
    _debug_print('starting _binary_operation({}, {}, {})'.format(op1, op2, operator))
    s1 = _solve(parsed, op1)
    s2 = _solve(parsed, op2)

    if operator == ' AND ':
        res = (s1 & s2) & BINARY_MASK
    elif operator == ' OR ':
        res = (s1 | s2) & BINARY_MASK
    elif operator == ' RSHIFT ':
        res = (s1 >> s2) & BINARY_MASK
    else:  # Must be LSHIFT
        assert operator == ' LSHIFT '
        res = (s1 << s2) & BINARY_MASK

    _debug_print('finished _binary_operation({}, {}, {}) = {}'.format(op1, op2, operator, res))
    return res


def _not_operation(parsed, s):
    op = s[len('NOT '):]
    _debug_print('_not_operation({})'.format(op))
    solution = _solve(parsed, op)
    res = (~solution) & BINARY_MASK
    _debug_print('finished _not_operation({}) = {}'.format(op, res))
    return res


def _solve(parsed, target_wire, memo=MEMO):
    if target_wire in memo:
        return memo[target_wire]


    if target_wire.isnumeric():
        _debug_print(f'returning numeric value {target_wire}')
        memo[target_wire] = int(target_wire)
        return memo[target_wire]

    s = parsed[target_wire]

    if s.isnumeric():
        memo[target_wire] = int(s)
        return memo[target_wire]

    for operator in BINARY_OPERATORS:
        if operator in s:
            memo[target_wire] = _binary_operation(parsed, operator, s)
            return memo[target_wire]

    if 'NOT' in s:
        memo[target_wire] = _not_operation(parsed, s)
        return memo[target_wire]

    _debug_print(f'solving for wire name {s}')
    memo[target_wire] = _solve(parsed, s)
    return memo[target_wire]


def main(filename, target_wire):
    MEMO.clear()
    lines = _read_input(filename)
    parsed = _parse(lines)
    solution = _solve(parsed, target_wire)
    return solution


def _quick_test(test_filename):
    test_cases = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }

    for target_wire, expected in test_cases.items():
        actual = main(test_filename, target_wire)
        if actual == expected:
            print(f'\n====== Test case {target_wire} passed')
        else:
            print(f'\n====== Test case {target_wire} failed:\nexpected {expected} but got {actual}')
            assert actual == expected

    print(f'\n^^^^^^^^^^^^ All test cases passed successfully ^^^^^^^^^^^^')



if __name__ == '__main__':
    _quick_test(test_filename='test_data_c7.txt')

    solution1 = main(filename='data_c7_part1.txt', target_wire='a')
    print(f'\nSolution to part 1: {solution1}')

    solution2 = main(filename='data_c7_part2.txt', target_wire='a')
    print(f'\nSolution to part 2: {solution2}')
