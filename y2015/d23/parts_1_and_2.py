def _read_and_parse_input(fname):
    instructions = []
    with open(fname) as f:
        for l in f.readlines():
            l_stripped = l.strip()
            l_split = [l_stripped[:3], l_stripped[4:]]
            if ',' in l:
                scnd = l_split[-1].split(',')
                scnd[-1] = int(scnd[-1])
                l_split = [l_split[0]] + scnd
            if l_split[0] == 'jmp':
                l_split[1] = int(l_split[1])
            instructions.append(l_split)
    return instructions


def _simulate(prog, target_reg, initial_regs):
    i = 0
    regs = list(initial_regs)
    while i < len(prog):
        inst = prog[i]
        cmd = inst[0]
        if cmd == 'hlf':
            j = 0 if inst[1] == 'a' else 1
            regs[j] //= 2
            i += 1
        elif cmd == 'tpl':
            j = 0 if inst[1] == 'a' else 1
            regs[j] *= 3
            i += 1
        elif cmd == 'inc':
            j = 0 if inst[1] == 'a' else 1
            regs[j] += 1
            i += 1
        elif cmd == 'jmp':
            i += inst[1]
        elif cmd == 'jie':
            j = 0 if inst[1] == 'a' else 1
            if regs[j] % 2 == 0:
                i += inst[2]
            else:
                i += 1
        elif cmd == 'jio':
            j = 0 if inst[1] == 'a' else 1
            if regs[j] == 1:
                i += inst[2]
            else:
                i += 1
        else:
            raise ValueError(f'Unknown command in instruction {i}: {inst}')

    return regs[target_reg]


def main(fname, target_reg, initial_regs):
    prog = _read_and_parse_input(fname)
    answer = _simulate(prog, target_reg, initial_regs)
    return answer


if __name__ == '__main__':
    assert 2 == main('./test_data.txt',  0, (0, 0))
    print('Solution to part 1:', main('./data.txt', 1, (0, 0)))
    print('Solution to part 1:', main('./data.txt', 1, (1, 0)))
