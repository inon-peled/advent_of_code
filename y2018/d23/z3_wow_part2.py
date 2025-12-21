"""
A much shorter solution using Z3, also from https://chatgpt.com/share/69480904-2ffc-800e-82b9-8dae3ae0d879.
However, this takes much longer to find the answer than the custom, best-first search solver in part2.py.
"""

from z3.z3 import Ints, If, Abs, Optimize, Sum


def solve(bots):
    x, y, z = Ints("x y z")
    in_range = []

    for bx, by, bz, r in bots:
        in_range.append(
            If(Abs(x - bx) + Abs(y - by) + Abs(z - bz) <= r, 1, 0)
        )

    s = Optimize()
    total = Sum(in_range)
    dist = Abs(x) + Abs(y) + Abs(z)

    s.maximize(total)  # primary objective
    s.minimize(dist)  # tie-breaker

    s.check()
    m = s.model()
    return m.eval(dist).as_long()


def parse(fname):
    bots = []
    for line in open(fname):
        p, r = line.strip().split(", ")
        x, y, z = map(int, p[p.index("<") + 1:p.index(">")].split(","))
        bots.append((x, y, z, int(r[2:])))
    return bots


if __name__ == '__main__':
    assert solve(parse("test2.txt")) == 36
    print(solve(parse("input.txt")))
