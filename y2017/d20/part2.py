'''
Solution idea: for every pair of particles, solve a quadratic (or linear) equation of their trajectories
in each of the 3 dimensions. The particles then collide if-and-only-if all 3 equations yield the same integer solution.
The equation is:
(a / 2) * (t ** 2) + v * t + p = 0,
so to work with integer coefficients, solve instead:
a * (t ** 2) + 2 * v * t + 2 * p = 0.

Solution idea proposed by both ChatGPT (https://chatgpt.com/share/69446174-d480-800e-926f-6e99fef6b0ea) and
Gemini (https://gemini.google.com/share/53260be667cd).
Code was originally mine and then rewritten with bug corrections through Gemini.
'''
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
    if delta < 0:
        return None
    root = int(round(delta ** 0.5))
    if root ** 2 == delta:
        return root
    return None


def _solve_quad(a, b, c):
    solutions = set()

    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return solutions

    root = _integer_root(delta)
    if root is None:
        return solutions

    # Solving at^2 + bt + c = 0
    for r in [root, -root]:
        num = -b + r
        den = 2 * a
        if num % den == 0:
            t = num // den
            if t >= 0:
                solutions.add(t)

    return solutions


def _solve_linear(b, c):
    if b == 0:
        return {-1} if c == 0 else set()
    if (-c) % b == 0:
        sol = -c // b
        if sol >= 0:
            return {sol}
    return set()


def _solve_equation(part1, part2, dim):
    p1, v1, a1 = part1['p'][dim], part1['v'][dim], part1['a'][dim]
    p2, v2, a2 = part2['p'][dim], part2['v'][dim], part2['a'][dim]

    # Corrected coefficients for discrete movement:
    # Position at time t: p0 + v0*t + a*(t*(t+1)/2)
    # 2*p(t) = 2*p0 + (2*v0 + a)*t + a*t^2
    a = a1 - a2
    b = (2 * v1 + a1) - (2 * v2 + a2)
    c = 2 * (p1 - p2)

    if a != 0:
        return _solve_quad(a, b, c)
    return _solve_linear(b, c)


def _detect_collision(part1, part2):
    results = []
    for d in range(3):
        sol = _solve_equation(part1, part2, d)
        if sol == {-1}:
            continue
        if not sol:
            return None
        results.append(sol)

    if not results:
        return 0

    # Find common integer t across all dimensions
    sol_all_dims = results[0]
    for next_sol in results[1:]:
        sol_all_dims &= next_sol

    if not sol_all_dims:
        return None

    return min(sol_all_dims)


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
        to_remove = set()
        for i, j in collisions[t]:
            # Particles can only collide if both haven't been destroyed yet
            if remain[i] and remain[j]:
                to_remove.add(i)
                to_remove.add(j)

        for idx in to_remove:
            remain[idx] = False

    return sum(remain)


def main(fname):
    particles = _parse(fname)
    answer = solve(particles)
    return answer


if __name__ == '__main__':
    assert 1 == main('./test2.txt')
    print(main('./input.txt'))
