'''
Solution idea:
Simulate for each delay d=0, 1, 2, ..., until the first time that there are no collisions at all.
For faster execution, keep the delayed state and advance it one time step before each simulation.
'''


def _advance(state):
    for j in range(len(state)):
        s = state[j]
        if s is None:
            continue
        if s['position'] == 0 and s['direction'] == -1:
            s['direction'] = 1
        if s['position'] == s['range'] - 1 and s['direction'] == 1:
            s['direction'] = -1
        s['position'] += s['direction']


def _simulate(initial_state):
    state = [None if d is None else d.copy() for d in initial_state]
    for t in range(len(initial_state)):
        s = state[t]
        if s is not None and s['position'] == 0:
            return False
        _advance(state)

    return True


def solve(fname):
    layers = {}
    with open(fname) as f:
        for line in f:
            idx, depth = [int(e) for e in line.strip().split(':')]
            layers[idx] = depth

    mx_layer = max(layers)
    state = [None] * (mx_layer + 1)
    for r in layers:
        state[r] = {'position': 0, 'range': layers[r], 'direction': 1}

    delay = 0
    while True:
        res = _simulate(state)
        if res:
            return delay
        delay += 1
        _advance(state)
        if delay % 10000 == 0:
            print(f'Tried {delay} delays so far.')


if __name__ == '__main__':
    assert 10 == solve('test.txt')
    print(solve('./input.txt'))
