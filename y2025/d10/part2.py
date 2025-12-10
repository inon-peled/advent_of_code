"""
Solution via Linear Programming.
"""

from scipy.optimize import linprog

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


def _min_presses(buttons, target_voltages):
    """
    Solve an ILP, where decision variables are x = num presses for each button.
    c = 1 for each button, because we want to minimize total presses.
    b_eq = target_voltages
    A_eq[i][j] = 1 if button j affects light i, otherwise 0
    lb = 0
    ub = max voltage of any light, because no button can be pressed beyond this number
    integrality = True for all x
    """
    num_lights = len(target_voltages)
    num_buttons = len(buttons)
    c = [1] * len(buttons)
    b_eq = target_voltages[:]
    A_eq = [
        [int(i in buttons[j]) for j in range(num_buttons)]
        for i in range(num_lights)
    ]
    bounds = (0, max(target_voltages))

    res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=1)
    assert res.success is True

    optimal_presses = res.x
    total_presses = int(sum(optimal_presses))
    return total_presses


def main(fname):
    machines = read_and_parse(fname)
    total_best_presses = 0
    for i, m in enumerate(machines):
        m_presses = _min_presses(
            buttons=m['buttons'],
            target_voltages=m['target_voltages']
        )
        total_best_presses += m_presses
    return total_best_presses


if __name__ == '__main__':
    assert 33 == main('./test_data.txt')
    print('\nSolution to part 2:', main('./data.txt'))
