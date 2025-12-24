def _one_round(r, elves):
    r1 = r[elves[0]]
    r2 = r[elves[1]]
    s = str(r1 + r2)
    for d in s:
        r.append(int(d))
    elves[0] = (elves[0] + r1 + 1) % len(r)
    elves[1] = (elves[1] + r2 + 1) % len(r)


def solve(sub):
    r = [3, 7]
    elves = [0, 1]
    while True:
        suffix = ''.join(map(str, r[-10:]))
        if sub in suffix:
            r_s = ''.join(map(str, r))
            sb_idx = r_s.index(sub)
            return sb_idx
        else:
            _one_round(r, elves)


if __name__ == '__main__':
    assert 9 == solve('51589')
    assert 5 == solve('01245')
    assert 18 == solve('92510')
    assert 2018 == solve('59414')
    print(solve('380621'))
