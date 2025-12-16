def _parse(fname):
    inst = []

    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            assert line[0] in ('cpy', 'inc', 'dec', 'jnz')
            if line[0] == 'cpy':
                if line[1] not in ('a', 'b', 'c', 'd'):
                    line[1] = int(line[1])
            elif line[0] == 'jnz':
                line[-1] = int(line[-1])
                if line[1] not in ('a', 'b', 'c', 'd'):
                    line[1] = int(line[1])
            inst.append(line)

    return inst


def solve(fname, regs):
    inst = _parse(fname)
    p = 0

    while p < len(inst):
        s = inst[p]
        # print(p, regs, s)

        if s[0] == 'inc':
            r = s[1]
            regs[r] += 1
            p += 1
        elif s[0] == 'dec':
            r = s[1]
            regs[r] -= 1
            p += 1
        elif s[0] == 'cpy':
            r = s[-1]
            val = s[1] if isinstance(s[1], int) else regs[s[1]]
            regs[r] = val
            p += 1
        elif s[0] == 'jnz':
            val = s[1] if isinstance(s[1], int) else regs[s[1]]
            if val != 0:
                offset = s[-1]
                p += offset
            else:
                p += 1
        else:
            raise ValueError('Unrecognized instruction: ' + s)

    return regs['a']


if __name__ == '__main__':
    assert 42 == solve('test_data.txt', regs={r: 0 for r in 'abcd'})
    print('Answer to part 1 is', solve('input.txt', regs={r: 0 for r in 'abcd'}))
    print('Answer to part 2 is', solve('input.txt', regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}))
