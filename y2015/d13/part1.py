from itertools import permutations
from collections import defaultdict


def read_and_parse(filename):
    lines = open(filename).readlines()
    instructions = defaultdict(dict)
    for line in lines:
        s = line.split()
        u = s[0]
        sign = -1 if s[2] == 'lose' else 1
        change = int(s[3])
        v = s[-1][:-1]
        instructions[u][v] = sign * change
    return instructions

def _calc_one_perm(p, instructions):
    total = 0
    n = len(p)
    for i in range(len(p)):
        curr = p[i]
        prev = p[(i - 1) % n]
        next = p[(i + 1) % n]
        total += instructions[curr][next]
        total += instructions[curr][prev]
    return total


def solve(instructions):
    best_total = None
    for p in permutations(instructions.keys()):
        curr = _calc_one_perm(p, instructions)
        if best_total is None or curr > best_total:
            best_total = curr
    return best_total

if __name__ == '__main__':
    assert 330 == solve(read_and_parse('test.txt'))
    print()
    print(solve(read_and_parse('data.txt')))