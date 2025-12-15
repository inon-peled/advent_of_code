def _decipher_parentheses(chars):
    if not chars:
        return 0

    if chars[0] != '(':
        return 1 + _decipher_parentheses(chars[1:])

    j = 0
    while chars[j] != ')':
        j += 1

    rep = ''.join(chars[:j + 1])
    chunk_len, num_repeat = [int(e) for e in rep[1:-1].split('x')]

    rec_start = len(rep)
    rec_end = rec_start + chunk_len
    rec_chars = chars[rec_start:rec_end]
    rec_sol = _decipher_parentheses(rec_chars)

    return (num_repeat * rec_sol) + _decipher_parentheses(chars[rec_end:])


def solve(fname):
    s = open(fname).read()
    answer = _decipher_parentheses(s)
    return answer


def _test():
    cases = [
        ('ADVENT', len('ADVENT')),
        ('A(1x5)BC', len('ABBBBBC')),
        ('(3x3)XYZ', len('XYZXYZXYZ')),
        ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
        ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
    ]
    for inp, expected in cases:
        actual = _decipher_parentheses(inp)
        assert actual == expected


if __name__ == '__main__':
    _test()
    print('Solution to part 2:', solve('input.txt'))
