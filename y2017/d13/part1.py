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


def _simulate(layers):
    mx_layer = max(layers)
    state = [None] * (mx_layer + 1)
    for r in layers:
        state[r] = {'position': 0, 'range': layers[r], 'direction': 1}

    cost = 0
    for t in range(mx_layer + 1):
        s = state[t]
        if s is not None and s['position'] == 0:
            cost += s['range'] * t
        _advance(state)

    return cost


def solve(fname):
    layers = {}
    with open(fname) as f:
        for line in f:
            idx, depth = [int(e) for e in line.strip().split(':')]
            layers[idx] = depth
    answer = _simulate(layers)
    return answer


if __name__ == '__main__':
    assert 24 == solve('test.txt')
    print(solve('./input.txt'))
