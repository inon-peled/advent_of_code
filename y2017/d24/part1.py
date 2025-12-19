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

    best = 0
    for opt in options:
        a, b = opt
        sol = solve(
            chips=chips - {opt},
            last_pin=(a if b == last_pin else b),
            memo=memo
        )
        curr = a + b + sol
        if curr > best:
            best = curr

    memo[memo_key] = best
    return best


def main(fname):
    chips = _parse(fname)
    answer = solve(chips=chips, last_pin=0, memo={})
    return answer

if __name__ == '__main__':
    assert 31 == main('./test.txt')
    print(main('./input.txt'))
