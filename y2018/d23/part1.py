def _parse(fname):
    bots = {}

    with open(fname) as f:
        for line in f:
            line = line.strip()
            pos, r = line.split(', ')

            pos = pos.split('<')[1]
            pos = pos.split('>')[0]
            pos = tuple(int(e) for e in pos.split(','))

            r = r.split('=')
            r = int(r[1])
            bots[pos] = r

    return bots


def _manhattan_distance(pos1, pos2):
    assert len(pos1) == len(pos2)
    return sum(abs(pos1[i] - pos2[i]) for i in range(len(pos1)))


def solve(bots):
    max_r = max(bots.values())
    bots_with_max_r = [pos for pos in bots if bots[pos] == max_r]
    assert len(bots_with_max_r) == 1

    pos_strongest_bot = bots_with_max_r[0]
    r_strongest_bot = bots[pos_strongest_bot]

    total = 0
    for b in bots:
        if _manhattan_distance(b, pos_strongest_bot) <= r_strongest_bot:
            total += 1

    return total


def main(fname):
    bots = _parse(fname)
    return solve(bots)


if __name__ == '__main__':
    assert 7 == main('./test.txt')
    print(main('./input.txt'))