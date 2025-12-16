def _swap_pos(x, y, s):
    i = min(x, y)
    j = max(x, y)
    swapped = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
    return swapped


def _swap_ltr(x, y, s):
    return _swap_pos(s.index(x), s.index(y), s)


def _swap(s, line):
    a = line[2]
    b = line[5]
    if line[1] == 'position':
        a = int(a)
        b = int(b)
        return _swap_pos(a, b, s)
    else:
        return _swap_ltr(a, b, s)


def _rotate_right(x, s):
    for i in range(x):
        s = s[-1] + s[:-1]
    return s


def _rotate_left(x, s):
    for i in range(x):
        s = s[1:] + s[0]
    return s


def _rotate_pos(x, s):
    idx = s.index(x)
    extra = int(idx >= 4)
    num = 1 + idx + extra
    return _rotate_right(num, s)


def _rotate(s, line):
    if line[1] == 'left':
        x = int(line[2])
        return _rotate_left(x, s)
    elif line[1] == 'right':
        x = int(line[2])
        return _rotate_right(x, s)
    else:
        x = line[-1]
        return _rotate_pos(x, s)


def _reverse(s, line):
    x = int(line[2])
    y = int(line[4])
    chunk = s[x:y + 1]
    reversed = s[:x] + chunk[::-1] + s[y + 1:]
    return reversed


def _move(s, line):
    x = int(line[2])
    y = int(line[5])
    letter_to_move = s[x]
    moved = s[:x] + s[x + 1:]
    moved = moved[:y] + letter_to_move + moved[y:]
    return moved


def solve(s, fname):
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            if line[0] == 'swap':
                s = _swap(s, line)
            elif line[0] == 'rotate':
                s = _rotate(s, line)
            elif line[0] == 'reverse':
                s = _reverse(s, line)
            elif line[0] == 'move':
                s = _move(s, line)
            else:
                raise ValueError(f'Unknown command: {line}')
            print(f'Processed line {line} -- now {s=}')
    return s


if __name__ == '__main__':
    assert 'decab' == solve('abcde', 'test_data.txt')
    print()
    print('\nPart 1 solution is:', solve('abcdefgh', 'input.txt'))
