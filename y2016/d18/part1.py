def _find_next(state, i, n):
    j = (i + 1) % n
    while j not in state:
        j = (j + 1) % n
    return j


def solve(n):
    state = {e: 1 for e in range(n)}
    i = 0

    while True:
        if len(state) == 1:
            return 1 + list(state)[0]
        next_i = _find_next(state, i, n)
        state[i] += state[next_i]
        state.pop(next_i)
        i = _find_next(state, next_i, n)


if __name__ == '__main__':
    assert 3 == solve(5)
    print('Part 1 solution is:', solve(3018458))
