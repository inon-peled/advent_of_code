def solve(fname):
    with open(fname) as f:
        jumps = [int(line.strip()) for line in f]

    i = 0
    steps = 0
    n = len(jumps)
    while i < n:
        j = jumps[i]
        jumps[i] += 1
        i += j
        steps += 1

    return steps


if __name__ == '__main__':
    assert 5 == solve('test.txt')
    print(solve('input.txt'))
