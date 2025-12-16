DATA = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'


def _next_row(prev):
    n = len(prev)
    curr = ''
    for j in range(n):
        left = prev[j - 1] if j > 0 else '.'
        center = prev[j]
        right = prev[j + 1] if j < n - 1 else '.'
        trap_cond1 = (left == center == '^' and right == '.')
        trap_cond2 = (center == right == '^' and left == '.')
        trap_cond3 = (center == right == '.' and left == '^')
        trap_cond4 = (center == left == '.' and right == '^')
        trap_cond_total = trap_cond1 or trap_cond2 or trap_cond3 or trap_cond4
        tile = '^' if trap_cond_total else '.'
        curr += tile
    return curr


def solve(data, total_rows):
    prev = data[:]
    total_safe = prev.count('.')
    for i in range(1, total_rows):
        curr = _next_row(prev)
        total_safe += curr.count('.')
        prev = curr
    return total_safe


if __name__ == '__main__':
    assert 6 == solve('..^^.', 3)
    assert 38 == solve('.^^.^.^^^^', 10)
    print('Part 1 solution:', solve(DATA, 40))
    print('Part 2 solution:', solve(DATA, 400000))
