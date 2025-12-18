'''
Solution idea: nothing special, just let it run for 24h, by which time it will have reached the answer :-)
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


def _tgl(inst, regs, p, instructions):
    offset = inst[1]
    offset_val = offset if isinstance(offset, int) else regs[offset]
    target_p = p + offset_val
    if not (0 <= target_p < len(instructions)):
        return

    target_inst = instructions[target_p]
    target_cmd = target_inst[0]
    if target_cmd in ['inc', 'dec', 'tgl']:
        target_inst[0] = 'dec' if target_cmd == 'inc' else 'inc'
    else:
        target_inst[0] = 'cpy' if target_cmd == 'jnz' else 'jnz'
    instructions[target_p] = target_inst


def solve(a_init_val, instructions):
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
        elif cmd == 'tgl':
            _tgl(inst, regs, p, instructions)
            p += 1
        else:
            raise ValueError(f'unknown command: {inst}')

    answer = regs['a']
    return answer

def main(fname, a_init_val):
    instructions = _parse(fname)
    answer = solve(a_init_val, instructions)
    return answer

if __name__ == '__main__':
    assert 3 == main('./test_data.txt', 7)
    print('Part 2 answer:', main('./input.txt', 12))
