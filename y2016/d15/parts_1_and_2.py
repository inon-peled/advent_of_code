TEST_DISCS = [
    [5, 4],
    [2, 1]
]

DISCS = [
    [7, 0],
    [13, 0],
    [3, 2],
    [5, 2],
    [17, 0],
    [19, 7]
]


def solve(start_state):
    discs = [d[:] for d in start_state]
    t = 0
    goal = [d[0] - i for i, d in enumerate(discs, start=1)]
    while True:
        curr = [d[1] for d in discs]
        if curr == goal:
            return t
        t += 1
        for d in discs:
            d[1] = (d[1] + 1) % d[0]


if __name__ == '__main__':
    assert 5 == solve(TEST_DISCS)
    print('Part 1 solution is', solve(DISCS))
    print('Part 2 solution is', solve(DISCS + [[11, 0]]))
