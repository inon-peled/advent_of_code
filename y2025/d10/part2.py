from tqdm import tqdm

from ast import literal_eval


def _to_tuple(s):
    ev = literal_eval(s)
    if not isinstance(ev, tuple):
        ev = (ev,)
    return ev


def read_and_parse(fname):
    machines = []
    for line in open(fname):
        line = line.strip().split()
        buttons = tuple([_to_tuple(e) for e in line[1:-1]])
        target_voltages = tuple(literal_eval(line[-1].replace('{', '[').replace('}', ']')))
        machines.append({'target_voltages': target_voltages, 'buttons': buttons})
    return machines


def _increment(lights_state, button):
    result = list(lights_state)
    for b in button:
        result[b] += 1
    return result


def _min_presses(voltage_state, buttons, target_voltages, memo):
    memo_key = tuple(tuple(e) for e in (voltage_state, buttons, target_voltages))
    if memo_key in memo:
        return memo[memo_key]

    if tuple(voltage_state) == tuple(target_voltages):
        memo[memo_key] = 0
    elif any(v > t for v, t in zip(voltage_state, target_voltages)):
        memo[memo_key] = None
    else:
        best_presses = None

        for i, button in enumerate(buttons):
            curr_voltages = _increment(voltage_state, button)
            best_presses_remaining = _min_presses(
                voltage_state=curr_voltages,
                buttons=buttons,
                target_voltages=target_voltages,
                memo=memo
            )
            if best_presses_remaining is not None:
                best_presses_including_button = 1 + best_presses_remaining
                if best_presses is None or best_presses_including_button < best_presses:
                    best_presses = best_presses_including_button

        memo[memo_key] = best_presses

    return memo[memo_key]


def _initial_voltages(m):
    init = [0] * len(m['target_voltages'])
    return init


def main(fname):
    machines = read_and_parse(fname)
    total_best_presses = 0
    memo = dict()
    for m in tqdm(machines, desc='Machines'):
        best_presses = _min_presses(
            voltage_state=_initial_voltages(m),
            buttons=m['buttons'],
            target_voltages=m['target_voltages'],
            memo=memo
        )
        total_best_presses += best_presses
    return total_best_presses


if __name__ == '__main__':
    assert 33 == main('./test_data.txt')
    print(main('./data.txt'))
