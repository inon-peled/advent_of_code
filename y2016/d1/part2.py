DATA = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'


def solve(inp):
    parsed = inp.split(', ')
    face = 1
    loc = [0, 0]
    visited = [[0, 0]]

    for p in parsed:
        if p[0] == 'R':
            face = (face - 1) % 4
        else:
            face = (face + 1) % 4

        num = int(p[1:])

        if face == 0:
            vs = [[loc[0] + i, loc[1]] for i in range(1, num + 1)]
            loc[0] += num
        elif face == 2:
            vs = [[loc[0] - i, loc[1]] for i in range(1, num + 1)]
            loc[0] -= num
        elif face == 1:
            vs = [[loc[0], loc[1] + i] for i in range(1, num + 1)]
            loc[1] += num
        else:
            vs = [[loc[0], loc[1] - i] for i in range(1, num + 1)]
            loc[1] -= num

        for v in vs:
            if v in visited:
                distance_to_first_visited = abs(v[0]) + abs(v[1])
                return distance_to_first_visited

        visited += vs

    return None


if __name__ == '__main__':
    assert 4 == solve('R8, R4, R4, R8')
    print('Solution to part 2:', solve(DATA))
