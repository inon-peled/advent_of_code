def _decipher_maximal_repetition_code(chars, i):
    j = i + 1
    breaks = [i]

    while True:
        while chars[j] != ')':
            j += 1
        breaks.append(j)
        j += 1
        if (j == len(chars)) or (chars[j] != '('):
            break

    codes = []
    for k in range(len(breaks) - 1):
        c = ''.join(chars[(breaks[k] + 1):breaks[k + 1]]).replace('(', '')
        codes.append(c)

    codes_numeric = [[int(e) for e in c.split('x')] for c in codes]

    len_of_text_piece = codes_numeric[-1][0]
    next_i = j + len_of_text_piece

    total_chars_added = len_of_text_piece
    for chunk, repetition in codes_numeric:
        total_chars_added *= repetition

    return next_i, total_chars_added


def _one_swipe(s):
    chars = [c for c in s if c not in [' ', '\t', '\r', '\n']]
    i = 0
    decompressed_length = 0

    while i < len(chars):
        if chars[i] != '(':
            decompressed_length += 1
            i += 1
        else:
            i, total_chars_added = _decipher_maximal_repetition_code(chars, i)
            decompressed_length += total_chars_added

    return decompressed_length


def solve(fname):
    s = open(fname).read()
    swipe_result = _one_swipe(s)
    answer = len(swipe_result)
    return answer


def _test():
    cases = [
        # ('ADVENT', len('ADVENT')),
        # ('A(1x5)BC', len('ABBBBBC')),
        # ('(3x3)XYZ', len('XYZXYZXYZ')),
        # ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
        ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
    ]
    for inp, expected in cases:
        actual = _one_swipe(inp)
        assert actual == expected


if __name__ == '__main__':
    _test()
    # print('Solution to part 2:', solve('input.txt'))
