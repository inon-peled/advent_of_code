'''
Solution idea: for every pair of particles, solve a quadratic (or linear) equation of their trajectories
in each of the 3 dimensions. The particles then collide if-and-only-if all 3 equations yield the same integer solution.
The equation is:
(a / 2) * (t ** 2) + v * t + p = 0,
so to work with integer coefficients, solve instead:
a * (t ** 2) + 2 * v * t + 2 * p = 0.
'''
import math
from collections import defaultdict


def _to_list(s):
    t = s.replace('a=<', '').replace('v=<', '').replace('p=<', '').replace('>', '')
    lst = [int(e) for e in t.split(',')]
    return lst


def _parse(fname):
    particles = []
    with open(fname) as f:
        for i, line in enumerate(f):
            p, v, a = line.split(', ')
            part = {'p': _to_list(p), 'v': _to_list(v), 'a': _to_list(a)}
            particles.append(part)
    return particles


def _minus(vec1, vec2):
    return [vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2]]


def _integer_root(delta):
    low = int(math.floor(delta ** 0.5))
    high = int(math.ceil(delta ** 0.5))
    if delta == low ** 2:
        return low
    if delta == high ** 2:
        return high
    return None


def _solve_quad(a, b, c):
    solutions = set()

    delta = -4 * a * c + (b ** 2)
    if delta < 0:
        return solutions

    root = _integer_root(delta)
    if root is None:
        return solutions

    t1 = -b + root
    if t1 >= 0 and t1 % (2 * a) == 0:
        solutions.add(t1 // (2 * a))

    t2 = -b - root
    if t2 >= 0 and t2 % (2 * a) == 0:
        solutions.add(t2 // (2 * a))

    return solutions


def _solve_linear(b, c):
    if c % b != 0:
        return set()
    sol = -c // b
    return {sol}


def _solve_equation(part1, part2, dim):
    vec1 = [2 * part1['p'][dim], 2 * part1['v'][dim], part1['a'][dim]]
    vec2 = [2 * part2['p'][dim], 2 * part2['v'][dim], part2['a'][dim]]
    d = _minus(vec1, vec2)
    c, b, a = d

    if a != 0:
        return _solve_quad(a, b, c)
    if b != 0:
        return _solve_linear(b, c)
    if c == 0:
        return {-1}
    return set()


def _detect_collision(part1, part2):
    sol_x = _solve_equation(part1, part2, 0)
    sol_y = _solve_equation(part1, part2, 1)
    sol_z = _solve_equation(part1, part2, 2)

    sol_all_dims = {-1}
    for sol in [sol_x, sol_y, sol_z]:
        if sol != {-1}:
            sol_all_dims = sol

    if sol_all_dims == {-1}:
        return 0

    if sol_x != {-1}:
        sol_all_dims &= sol_x
    if sol_y != {-1}:
        sol_all_dims &= sol_y
    if sol_z != {-1}:
        sol_all_dims &= sol_z

    if not sol_all_dims:
        return None
    min_time = min(sol_all_dims)
    return min_time


def solve(particles):
    collisions = defaultdict(list)
    for i in range(len(particles) - 1):
        for j in range(i + 1, len(particles)):
            t = _detect_collision(particles[i], particles[j])
            if t is not None:
                collisions[t].append((i, j))

    remain = [True] * len(particles)
    times_ascending = sorted(collisions.keys())
    for t in times_ascending:
        for i, j in collisions[t]:
            remain[i] = False
            remain[j] = False

    total_remaining = sum(remain)
    return total_remaining


def main(fname):
    particles = _parse(fname)
    answer = solve(particles)
    return answer


if __name__ == '__main__':
    assert 1 == main('./test2.txt')
    print(main('./input.txt'))
