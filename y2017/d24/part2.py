'''
Solution idea: backtracking with memoization. Note that no chip repeats.
'''


def _parse(fname):
    chips = set()
    with open(fname) as f:
        for line in f:
            a, b = [int(e) for e in line.strip().split('/')]
            chips.add((a, b))
    return chips


def solve(chips, last_pin, memo):
    memo_key = tuple(sorted(chips))
    if memo_key in memo:
        return memo[memo_key]

    options = []
    for a, b in chips:
        if a == last_pin or b == last_pin:
            options.append((a, b))

    s = []
    l = []
    for opt in options:
        a, b = opt
        strength, length = solve(
            chips=chips - {opt},
            last_pin=(a if b == last_pin else b),
            memo=memo
        )
        curr_strength = a + b + strength
        curr_length = 1 + length
        s.append(curr_strength)
        l.append(curr_length)

    best_length = max(l) if l else 0
    best_strength = 0
    for i in range(len(l)):
        if l[i] == best_length:
            best_strength = max(best_strength, s[i])

    memo[memo_key] = best_strength, best_length
    return memo[memo_key]


def main(fname):
    chips = _parse(fname)
    answer, _ = solve(chips=chips, last_pin=0, memo={})
    return answer


if __name__ == '__main__':
    assert 19 == main('./test.txt')
    print(main('./input.txt'))
