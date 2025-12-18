'''
Solution idea:
For every i = 0, 1, 2, ...:
Record program state upon every execution of the out command, until any of the following happens:
* The program halts -- reject i.
* A cycle of states is detected.
** In this case, if the cycle outputs 0, 1 repeatedly, then accept i and terminate, otherwise reject i.
A state consists only of the program counter and the registers, because the program instructions do not change.
'''


def _parse(fname):
    instructions = []
    for line in open(fname):
        line = line.strip().split()
        if line[1] not in 'abcd':
            line[1] = int(line[1])
        if len(line) > 2 and line[2] not in 'abcd':
            line[2] = int(line[2])
        instructions.append(line)
    return instructions


def _cpy(inst, regs):
    dst = inst[2]
    if isinstance(dst, int):
        return

    src = inst[1]
    src_val = src if isinstance(src, int) else regs[src]
    regs[dst] = src_val


def _inc(inst, regs):
    r = inst[1]
    if isinstance(r, int):
        return
    else:
        regs[r] += 1


def _dec(inst, regs):
    r = inst[1]
    if isinstance(r, int):
        return
    else:
        regs[r] -= 1


def _jnz(inst, regs, p):
    if len(inst) != 3:
        return p + 1

    src = inst[1]
    src_val = src if isinstance(src, int) else regs[src]

    if src_val != 0:
        offset = inst[2]
        offset_val = offset if isinstance(offset, int) else regs[offset]
        new_p = p + offset_val
        return new_p
    else:
        return p + 1


def _out(inst, regs, p, states):
    s = (p, regs['a'], regs['b'], regs['c'], regs['d'])
    if s in states:
        return None
    else:
        states.add(s)
        r = inst[1]
        val = regs[r]
        return val


def _simulate(a_init_val, instructions):
    states = set()
    outputs = []
    regs = {'a': a_init_val, 'b': None, 'c': None, 'd': None}
    p = 0
    n = len(instructions)

    while 0 <= p < n:
        inst = instructions[p]
        cmd = inst[0]
        if cmd == 'cpy':
            _cpy(inst, regs)
            p += 1
        elif cmd == 'inc':
            _inc(inst, regs)
            p += 1
        elif cmd == 'dec':
            _dec(inst, regs)
            p += 1
        elif cmd == 'jnz':
            p = _jnz(inst, regs, p)
            pass
        elif cmd == 'out':
            res = _out(inst, regs, p, states)
            # No cycle yet detected
            if res is not None:
                outputs.append(res)
            # Cycle detected
            else:
                if len(outputs) < 2 or outputs[0] != 0:
                    return False
                for i in range(1, len(outputs)):
                    if outputs[i] != 1 - outputs[i - 1]:
                        return False
                return True
            p += 1
        else:
            raise ValueError(f'unknown command: {inst}')

    return False  # Because the program halted


def main(fname):
    instructions = _parse(fname)
    a_init_val = 0
    while True:
        a_init_val += 1
        sim_result = _simulate(a_init_val, instructions)
        if sim_result:
            return a_init_val
        else:
            print(f'Rejected {a_init_val}')



if __name__ == '__main__':
    print('Part 1 answer:', main('./input.txt'))
