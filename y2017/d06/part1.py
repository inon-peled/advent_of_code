DATA = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
TEST = [0, 2, 7, 0]

def solve(data):
    visited = set()
    state = data[:]
    n = len(state)
    i = 0
    while True:
        if tuple(state) in visited:
            return i

        visited.add(tuple(state))
        i += 1

        mx = max(state)
        mx_idx = state.index(mx)
        state[mx_idx] = 0

        j = (mx_idx + 1) % n
        while mx > 0:
            state[j] += 1
            j = (j + 1) % n
            mx -= 1


if __name__ == '__main__':
    assert 5 == solve(TEST)
    print(solve(DATA))
