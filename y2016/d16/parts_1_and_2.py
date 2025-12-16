def _gen(s, max_len):
    while len(s) < max_len:
        rev_flip = ''.join('0' if c == '1' else '1' for c in s[::-1])
        s = s + '0' + rev_flip
    s_prefix = s[:max_len]
    return s_prefix


def _checksum(s):
    while len(s) % 2 == 0:
        new_s = ''
        for i in range(0, len(s), 2):
            chunk = s[i:i + 2]
            c = '1' if chunk[0] == chunk[1] else '0'
            new_s += c
        s = new_s
    return s


def solve(s, max_len):
    g = _gen(s, max_len)
    c = _checksum(g)
    return c


if __name__ == '__main__':
    assert '01100' == solve('10000', 20)
    print('Part 1 solution is:', solve('10001110011110000', 272))
    print('Part 2 solution is:', solve('10001110011110000', 35651584))
