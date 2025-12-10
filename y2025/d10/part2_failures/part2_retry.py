"""
Solution idea:
For each light L, let V_L be its target voltage, let B_L be the buttons that contain L, and consider
all combinations of V presses over the buttons in B_L.
For each such combination, solve recursively on the remaining buttons and lights.
"""

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


def _advance(state, comp, buttons):
    new_state = state[:]
    for i in range(len(comp)):
        v = comp[i]
        b = buttons[i]
        for l in b:
            new_state[l] += v
    return new_state


def _compositions(N, k):
    if k == 1:
        yield (N,)
        return
    for i in range(N + 1):
        for rest in _compositions(N - i, k - 1):
            yield (i,) + rest


def _applicable_buttons(buttons, light_idx):
    applicable_buttons = []
    for btn in buttons:
        if light_idx in btn and all(i not in btn for i in range(light_idx)):
            applicable_buttons.append(btn)
    return applicable_buttons


def _min_presses(light_idx, state, buttons, target_voltages, memo):
    memo_key = tuple(state)
    if memo_key in memo:
        return memo[memo_key]

    if light_idx >= len(target_voltages):
        return 0

    applicable_buttons = _applicable_buttons(buttons=buttons, light_idx=light_idx)
    if not applicable_buttons:
        return 0

    volt = target_voltages[light_idx] - state[light_idx]

    best = None
    for comp in _compositions(volt, len(applicable_buttons)):
        new_state = _advance(state=state, comp=comp, buttons=applicable_buttons)
        comp_best_presses = _min_presses(
            light_idx=light_idx + 1,
            state=new_state,
            buttons=buttons,
            target_voltages=target_voltages,
            memo=memo
        )
        if comp_best_presses is not None:
            curr_best = volt + comp_best_presses
            if best is None or curr_best < best:
                best = curr_best

    memo[memo_key] = best
    return best


def main(fname):
    machines = read_and_parse(fname)
    total_best_presses = 0
    for i, m in enumerate(machines):
        print(i)
        m_presses = _min_presses(
            light_idx=0,
            state=[0] * len(m['target_voltages']),
            buttons=m['buttons'],
            target_voltages=m['target_voltages'],
            memo=dict()
        )
        total_best_presses += m_presses
    return total_best_presses


if __name__ == '__main__':
    assert 33 == main('./test_data.txt')
    print(main('./data.txt'))
