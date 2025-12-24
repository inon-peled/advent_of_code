def _one_round(r, elves):
    r1 = r[elves[0]]
    r2 = r[elves[1]]
    s = str(r1 + r2)
    for d in s:
        r.append(int(d))
    elves[0] = (elves[0] + r1 + 1) % len(r)
    elves[1] = (elves[1] + r2 + 1) % len(r)


def solve(min_recipes):
    r = [3, 7]
    elves = [0, 1]
    while len(r) < min_recipes:
        _one_round(r, elves)

    for k in range(10):
        _one_round(r, elves)

    final = r[min_recipes:min_recipes + 10]
    answer = ''.join(map(str, final))
    return answer


if __name__ == '__main__':
    assert '5158916779' == solve(9)
    assert '0124515891' == solve(5)
    assert '9251071085' == solve(18)
    assert '5941429882' == solve(2018)
    print(solve(380621))
