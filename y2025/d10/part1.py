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
        lights = tuple(0 if e == '.' else 1 for e in line[0][1:-1])
        buttons = tuple([_to_tuple(e) for e in line[1:-1]])
        machines.append({'target_lights': lights, 'buttons': buttons})
    return machines


def _toggle(lights, button):
    result = list(lights)
    for b in button:
        result[b] = 1 - result[b]
    return result


def _min_presses(lights_state, buttons, target_lights, memo):
    memo_key = tuple(tuple(e) for e in (lights_state, buttons, target_lights))
    if memo_key in memo:
        return memo[memo_key]

    if tuple(lights_state) == tuple(target_lights):
        memo[memo_key] = 0
    else:
        best_presses = None

        for i, button in enumerate(buttons):
            curr_lights = _toggle(lights_state, button)
            available_buttons = buttons[:i] + buttons[i + 1:]
            best_presses_available_buttons = _min_presses(
                lights_state=curr_lights,
                buttons=available_buttons,
                target_lights=target_lights,
                memo=memo
            )
            if best_presses_available_buttons is not None:
                best_presses_including_button = 1 + best_presses_available_buttons
                if best_presses is None or best_presses_including_button < best_presses:
                    best_presses = best_presses_including_button

        memo[memo_key] = best_presses

    return memo[memo_key]


def _initial_lights(m):
    init = [0] * len(m['target_lights'])
    return init


def main(fname):
    machines = read_and_parse(fname)
    total_best_presses = 0
    memo = dict()
    for m in machines:
        best_presses = _min_presses(
            lights_state=_initial_lights(m),
            buttons=m['buttons'],
            target_lights=m['target_lights'],
            memo=memo
        )
        total_best_presses += best_presses
    return total_best_presses


if __name__ == '__main__':
    assert 7 == main('./test_data.txt')
    print(main('./data.txt'))
