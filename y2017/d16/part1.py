def _spin(state, x):
    new_state = state[-x:] + state[:-x]
    return new_state


def _exchange(state, i1, i2):
    l = list(state)
    l[i1], l[i2] = l[i2], l[i1]
    new_state = ''.join(l)
    return new_state


def _dance(state, parsed_instructions):
    for t in parsed_instructions:
        if t[0] == 'spin':
            x = t[1]
            state = _spin(state, x)
        elif t[0] == 'exchange':
            state = _exchange(state, t[1], t[2])
        else:
            i1 = state.index(t[1])
            i2 = state.index(t[2])
            state = _exchange(state, i1, i2)
    return state


def _parse(fname):
    with open(fname) as f:
        contents = f.read().strip()
        instructions = contents.split(',')

    parsed_instructions = []
    for i in range(len(instructions)):
        t = instructions[i]
        cmd = t[0]
        if cmd == 's':
            t_parsed = ('spin', int(t[1:]))
        elif cmd == 'x':
            a, b = [int(e) for e in t[1:].split('/')]
            t_parsed = ('exchange', a, b)
        elif cmd == 'p':
            a, b = [e for e in t[1:].split('/')]
            t_parsed = ('partner', a, b)
        else:
            raise ValueError(t)
        parsed_instructions.append(t_parsed)

    return parsed_instructions


def main(letters, fname):
    parsed_instructions = _parse(fname)
    state = _dance(letters, parsed_instructions)
    return state


if __name__ == '__main__':
    assert 'baedc' == main('abcde', 'test.txt')
    print(main('abcdefghijklmnop', 'input.txt'))
