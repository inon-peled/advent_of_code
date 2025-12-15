def _one_swipe(s):
    chars = [c for c in s if c not in [' ', '\t', '\r', '\n']]
    i = 0
    result = []

    while i < len(chars):
        if chars[i] != '(':
            result.append(chars[i])
            i += 1
        else:
            j = i + 1
            while chars[j] != ')':
                j += 1
            instruction = ''.join(chars[i + 1:j])
            offset, repetition = [int(e) for e in instruction.split('x')]
            chunk = chars[j + 1:j + 1 + offset]
            result.extend(chunk * repetition)
            i += 2 + len(instruction) + offset

    result_joined = ''.join(result)
    return result_joined


def solve(fname):
    s = open(fname).read()
    swipe_result = _one_swipe(s)
    answer = len(swipe_result)
    return answer


def _test():
    cases = [
        ('ADVENT', 'ADVENT'),
        ('A(1x5)BC', 'ABBBBBC'),
        ('(3x3)XYZ', 'XYZXYZXYZ'),
        ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
        ('(6x1)(1x3)A', '(1x3)A'),
        ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY')
    ]
    for inp, expected in cases:
        actual = _one_swipe(inp)
        assert actual == expected


if __name__ == '__main__':
    _test()
    print('Solution to part 1:', solve('input.txt'))
