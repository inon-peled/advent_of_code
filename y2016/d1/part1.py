DATA = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'


def solve(inp):
    parsed = inp.split(', ')

    face = 1
    loc = [0, 0]

    for p in parsed:
        if p[0] == 'R':
            face = (face - 1) % 4
        else:
            face = (face + 1) % 4

        num = int(p[1:])
        if face == 0:
            loc[0] += num
        elif face == 2:
            loc[0] -= num
        elif face == 1:
            loc[1] += num
        else:
            loc[1] -= num

    path_length = abs(loc[0]) + abs(loc[1])
    return path_length


if __name__ == '__main__':
   assert 5 == solve('R2, L3')
   assert 2 == solve('R2, R2, R2')
   assert 12 == solve('R5, L5, R5, R3')
   print('Solution to part 1:', solve(DATA))
