def solve1(fname):
    total = 0
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            total += len(set(line)) == len(line)
    return total


def solve2(fname):
    total = 0
    with open(fname) as f:
        for line in f:
            line = line.strip().split()
            good = True
            for i in range(len(line) - 1):
                for j in range(i + 1, len(line)):
                    w_i = sorted(line[i])
                    w_j = sorted(line[j])
                    if w_i == w_j:
                        good = False
            total += good
    return total


if __name__ == '__main__':
    print(solve1('input.txt'))
    print(solve2('input.txt'))
