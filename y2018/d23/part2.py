"""
Solution idea:

Each bot in the given data is a 3d cube with a given center and radius.
We need to find a maximal set of cubes, where each pair of cubes overlap, namely, their intersection is
a non-empty rectangular cuboid.

For this, we will o as follows:

1. For each cube, initialize a dict S with the following elements:
1.1. D_S = a rectangular cuboid that equals this cube.
1.2. P_S = 1

2. For each cube C:
2.1. For each dict S:
2.2 Let T(C, D_S) be the cuboid intersection of C and D_S.
2.3. If T(C, D_S) is non-empty, then increment P_S and assign T(C, D_S) to D_S.

3. Calculate M = max{P_S | all dicts S}.
4. Let K = {S | S is a dict with P_S = M}.
5. Return min {x_S + y_S + z_S | (x_S, y_S, z_S) is a corner of D_S, for S in K}.

Worst Case Complexity:
Let N be the number of given cubes.

There are O(N) dicts, each containing O(N) cubes, so the dicts take altogether O(N^2) space.
There are a few other variables, each taking O(N) space.
So the total space complexity is O(N^2).

For time complexity:
Step 1 takes O(N) time for initializations.
Step 2 consists of O(N^2) iterations, eac incurring O(1) calculations (assuming set operations are O(1)).
Each of the remaining three steps incurs O(N) operations.
So the total time complexity is O(N^2).
"""


def _parse(fname):
    bots = []

    with open(fname) as f:
        for line in f:
            line = line.strip()
            pos, r = line.split(', ')

            pos = pos.split('<')[1]
            pos = pos.split('>')[0]
            pos = tuple(int(e) for e in pos.split(','))

            r = r.split('=')
            r = int(r[1])

            bots.append((pos, r))

    return bots


def _manhattan_distance(pos1, pos2):
    assert len(pos1) == len(pos2)
    return sum(abs(pos1[i] - pos2[i]) for i in range(len(pos1)))


def _initialize(bots):
    dicts = []
    for i, b in enumerate(bots):
        pos, r = b
        mn = (pos[0] - r, pos[1] - r, pos[2] - r)
        mx = (pos[0] + r, pos[1] + r, pos[2] + r)
        ranges = {'mn': mn, 'mx': mx}
        s_b = {
            'p': 1,
            'd': ranges
        }
        dicts.append(s_b)
    return dicts


def _is_inside(point, rc):
    for dim in range(3):
        if not (rc['mn'][dim] <= point[dim] <= rc['mx'][dim]):
            return False
    return True


def _corners(rc):
    mn = rc['mn']
    mx = rc['mx']
    for x in [mn[0], mx[0]]:
        for y in [mn[1], mx[1]]:
            for z in [mn[2], mx[2]]:
                yield x, y, z


def _is_non_empty_intersection(rc1, rc2):
    for corner in _corners(rc2):
        if _is_inside(point=corner, rc=rc1):
            return True
    return False


def _intersection(rc1, rc2):
    mn1 = rc1['mn']
    mn2 = rc2['mn']
    mx1 = rc1['mx']
    mx2 = rc2['mx']
    rc_intersect = {'mn': [], 'mx': []}
    for dim in range(3):
        rc_intersect['mn'].append(max(mn1[dim], mn2[dim]))
        rc_intersect['mx'].append(min(mx1[dim], mx2[dim]))
    return rc_intersect


def _one_round(i, dicts):
    bot_dict = dicts[i]
    bot_rc = bot_dict['d']
    for j, s in enumerate(dicts):
        if i == j:
            continue
        s_rc = s['d']
        if _is_non_empty_intersection(rc1=s_rc, rc2=bot_rc):
            rc_intersect = _intersection(rc1=s_rc, rc2=bot_rc)
            s['d'] = rc_intersect
            s['p'] += 1

def solve(bots):
    # Step 1
    dicts = _initialize(bots)

    # Step 2
    for i in range(len(dicts)):
        _one_round(i, dicts)

    # Step 3
    m = max(s['p'] for s in dicts)

    # Step 4
    k = [s for s in dicts if m == s['p']]

    # Step 5
    min_dist = None
    for s in k:
        closest = sum(s['d']['mn'])
        if min_dist is None or min_dist < closest:
            min_dist = closest
    return min_dist


def main(fname):
    bots = _parse(fname)
    return solve(bots)


if __name__ == '__main__':
    assert 36 == main('./test2.txt')
    print(main('./input.txt'))
