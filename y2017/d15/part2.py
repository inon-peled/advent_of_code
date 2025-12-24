FACTOR1 = 16807
MODULO1 = 4
FACTOR2 = 48271
MODULO2 = 8

def _gen(val, factor, m):
    while True:
        val = (val * factor) % 2147483647
        if val % m == 0:
            y = bin(val)[-16:]
            yield y


def judge(num_turns, val1, val2):
    g1 = _gen(val1, FACTOR1, MODULO1)
    g2 = _gen(val2, FACTOR2, MODULO2)
    total = 0
    for t in range(num_turns):
        y1 = next(g1)
        y2 = next(g2)
        total += (y1 == y2)
    return total


if __name__ == '__main__':
    assert 309 == judge(5_000_000, 65, 8921)
    print('Assertion passed')
    print(judge(5_000_000, 699, 124))
