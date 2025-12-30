"""
Solution idea:
Hopefully, there is a cycle of states that the forest goes through from some minute onwards,
and the length of this cycle is quite small.
So detect such a cycle and use its length to skip tons of repeated calculations.
"""


def _parse(fname):
    with open(fname) as f:
        forest = [list(l.strip()) for l in f]
        assert all(len(l) == len(forest[0]) for l in forest)
    return forest


def _count_neighbors(forest, i, j):
    totals = {'#': 0, '|': 0, '.': 0}
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            if (x == i and y == j) or (x < 0) or (y < 0) or (x >= len(forest[0])) or (y >= len(forest)):
                continue
            char = forest[x][y]
            totals[char] += 1
    return totals


def _one_turn(forest):
    new_forest = [l[:] for l in forest]
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            n = _count_neighbors(forest, i, j)
            if forest[i][j] == '.' and n['|'] >= 3:
                new_forest[i][j] = '|'
            elif forest[i][j] == '|' and n['#'] >= 3:
                new_forest[i][j] = '#'
            elif forest[i][j] == '#' and not (n['|'] >= 1 and n['#'] >= 1):
                new_forest[i][j] = '.'
    return new_forest


def _find_cycle(forest):
    t = 0
    states = {t: forest}
    while True:
        forest = _one_turn(forest)
        t += 1
        for prev_t in states:
            if states[prev_t] == forest:
                cycle_length = t - prev_t
                print(f'A cycle of length {cycle_length} begins at minute {prev_t}')
                return prev_t, cycle_length, forest
        states[t] = forest


def solve(forest, turns):
    initial_t, cycle_length, forest = _find_cycle(forest)
    n = (turns - initial_t) // cycle_length
    remaining_turns = turns - (initial_t + cycle_length * n)

    for _ in range(remaining_turns):
        forest = _one_turn(forest)

    counts = {'#': 0, '|': 0, '.': 0}
    for i in range(len(forest[0])):
        for j in range(len(forest)):
            char = forest[i][j]
            counts[char] += 1

    answer = counts['#'] * counts['|']
    return answer


def main(fname, turns):
    forest = _parse(fname)
    answer = solve(forest, turns)
    return answer


if __name__ == '__main__':
    print(main('input.txt', 1_000_000_000))
