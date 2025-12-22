"""
Solution idea: dynamic programming with memoization.
"""

TEST_DEPTH = 510
TEST_TARGET = 10, 10

DEPTH = 8103
TARGET = 9, 758


def _geologic_edge(x, y, target_x, target_y):
    if x == y == 0:
        return 0

    if x == target_x and y == target_y:
        return 0

    if y == 0:
        return x * 16807

    if x == 0:
        return y * 48271

    raise ValueError(f'Not an edge case: {x=} {y=}')


def _erosion(x, y, target_x, target_y, depth, memo):
    memo_key = x, y
    if memo_key in memo:
        return memo[memo_key]

    if 0 in (x, y) or (x, y) == (target_x, target_y):
        g = _geologic_edge(x, y, target_x, target_y)
    else:
        a = _erosion(x - 1, y, target_x, target_y, depth, memo)
        b = _erosion(x, y - 1, target_x, target_y, depth, memo)
        g = a * b

    e = (g + depth) % 20183
    memo[memo_key] = e
    return e


def _print_region(risk):
    if risk == 0:
        symbol = '.'
    elif risk == 1:
        symbol = '='
    else:
        symbol = '|'
    print(symbol, end='')


def solve(depth, target_x, target_y):
    memo = {}
    total_risk = 0
    for i in range(target_y + 1):
        # print()
        for j in range(target_x + 1):
            e = _erosion(j, i, target_x, target_y, depth, memo)
            risk = e % 3
            # _print_region(risk)
            total_risk += risk
    # print()
    return total_risk


if __name__ == '__main__':
    assert 114 == solve(TEST_DEPTH, TEST_TARGET[0], TEST_TARGET[1])
    print(solve(DEPTH, TARGET[0], TARGET[1]))
