def _process(grp):
    total = 0
    nest = 0
    garbage = False
    ignore = False

    for i in range(len(grp)):
        c = grp[i]

        if ignore:
            ignore = False
            continue

        if c == '<':
            garbage = True
            continue

        if garbage:
            if c == '!':
                ignore = True
            elif c == '>':
                garbage = False
            continue

        if c == '{':
            nest += 1
            continue

        if c == '}':
            total += nest
            nest -= 1
            continue

    return total


def solve(fname):
    with open(fname) as f:
        contents = f.read().strip()
    total = _process(contents)
    return total


def _test():
    assert 1 == _process('{}')
    assert 6 == _process('{{{}}}')
    assert 5 == _process('{{},{}}')
    assert 16 == _process('{{{},{},{{}}}}')
    assert 1 == _process('{<a>,<a>,<a>,<a>}')
    assert 9 == _process('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    assert 9 == _process('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    assert 3 == _process('{{<a!>},{<a!>},{<a!>},{<ab>}}')


if __name__ == '__main__':
    _test()
    print(solve('input.txt'))
