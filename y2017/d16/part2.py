"""
Wrong solution idea: treat the dance as a permutation, because the "partner" command looks for particular
letters, not positions.

Correct solution idea:
Repeatedly dance until returning to the original order, after T dances, where hopefully T is much smaller than 10^9.
This indicates a cycle of length T, so do just B % T additional dances and output the result.
"""
def _spin(state, x):
    new_state = state[-x:] + state[:-x]
    return new_state


def _exchange(state, i1, i2):
    state[i1], state[i2] = state[i2], state[i1]


def _dance(state, parsed_instructions):
    for t in parsed_instructions:
        if t[0] == 'spin':
            x = t[1]
            state = _spin(state, x)
        elif t[0] == 'exchange':
            _exchange(state, t[1], t[2])
        else:
            i1 = state.index(t[1])
            i2 = state.index(t[2])
            _exchange(state, i1, i2)
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

def _find_cycle(state, instructions):
    n = 0
    initial_state = state[:]
    while True:
        state = _dance(state, instructions)
        n += 1
        if state == initial_state:
            print(f'Back to initial state after {n} dances')
            return n


def main(repetitions, letters, fname):
    parsed_instructions = _parse(fname)

    state = list(letters)
    cycle_length = _find_cycle(state, parsed_instructions)
    remaining = repetitions % cycle_length

    state = list(letters)
    for r in range(remaining):
        state = _dance(state, parsed_instructions)
    answer = ''.join(state)
    return answer


if __name__ == '__main__':
    print(main(1000000000, 'abcdefghijklmnop', 'input.txt'))
