def _process(grp):
    garbage = False
    ignore = False
    count_grbg = 0

    for i in range(len(grp)):
        c = grp[i]

        if ignore:
            ignore = False
            continue

        if c == '<' and not garbage:
            garbage = True
            continue

        if garbage:
            if c == '>':
                garbage = False
                continue
            if c == '!':
                ignore = True
                continue
            count_grbg += 1


    return count_grbg


def solve(fname):
    with open(fname) as f:
        contents = f.read().strip()
    total = _process(contents)
    return total


def _test():
    assert 0 == _process('<>')
    assert 17 == _process('<random characters>')
    assert 3 == _process('<<<<>')
    assert 2 == _process('<{!>}>')
    assert 0 == _process('<!!>')
    assert 0 == _process('<!!!>>')
    assert 10 == _process('<{o"i!a,<{i<a>')


if __name__ == '__main__':
    _test()
    print(solve('input.txt'))
