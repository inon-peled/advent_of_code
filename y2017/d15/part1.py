FACTOR1 = 16807
FACTOR2 = 48271


def _gen(val, factor):
    while True:
        val = (val * factor) % 2147483647
        y = bin(val)[-16:]
        yield y


def judge(num_turns, val1, val2):
    g1 = _gen(val1, FACTOR1)
    g2 = _gen(val2, FACTOR2)
    total = 0
    for t in range(num_turns):
        y1 = next(g1)
        y2 = next(g2)
        total += (y1 == y2)
    return total


if __name__ == '__main__':
    assert 588 == judge(40_000_000, 65, 8921)
    print(judge(40_000_000, 699, 124))
