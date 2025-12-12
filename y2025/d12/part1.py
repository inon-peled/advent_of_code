"""
Solution idea:
Run a Mixed-Integer Linear Programming (MILP) solver on the following formulation:

    min -c * x
    Subject to:
    0 <= x <= 1
    l <= A * x <= u
    All x are integers

where:

# x = decision variables, one per (p_idx, inst_num, rot_idx, i, j), where:
    p_idx runs on present indexes
    inst_num runs on number of instances of the present
    rot_idx runs on all possible transformation of the present
    i, j is the position of top left corner of the transformed present instance, in the tree's region.

# c = vector of 1's, same length as x

# A, l, u represent the following constraints:
## No overlaps:
   For every position  n in the tree's region, define for every x:
        v(n, x) = 1 if x covers p, otherwise 0,
   and require:
        0 <= sum(v(n, x) over all x) <= 1
## Exactly one transformation per present instance:
   For every p_idx and inst_num as defined above, define:
        r(p_idx, inst_num, x) = 1 if x applies to p_idx and inst_num, otherwise 0,
   and require:
        1 <= sum(r(inst_num, x) over all x) <= 1

This formulation has a solution if-and-only-if the tree's region can fit all present instances.
"""


def _read_and_parse_presents(lines):
    presents = []
    for l in lines:
        if ':' in l:
            curr_present = []
        elif l == '':
            presents.append(curr_present)
        else:
            curr_present.append([c for c in l])
    return presents


def _read_and_parse_trees(lines):
    trees = []
    for l in lines:
        size, amounts = l.split(': ')
        w, h = (int(e) for e in size.split('x'))
        amounts = tuple(int(num) for num in amounts.split(' '))
        trees.append((w, h, amounts))
    return trees


def _read_and_parse(fname):
    lines_presents = []
    lines_trees = []
    for line in open(fname):
        if 'x' not in line:
            lines_presents.append(line.strip())
        else:
            lines_trees.append(line.strip())

    presents = _read_and_parse_presents(lines_presents)
    trees = _read_and_parse_trees(lines_trees)
    return presents, trees


def _rotate_90deg_rightwards(present):
    rotated_present = []
    for j in range(len(present[0])):
        rotated_present.append([present[i][j] for i in range(len(present) - 1, -1, -1)])
    return rotated_present


def _print_grid(g):
    print()
    for row in g:
        print(''.join(row))


def _flip(present):
    f1 = [r[::-1] for r in present]
    f2 = [present[i] for i in range(len(present) - 1, -1, -1)]
    return [f1, f2]


def _transformations(presents):
    trasnformed_presents = []
    for present in presents:
        p1 = present[:]
        p2 = _rotate_90deg_rightwards(p1)
        p3 = _rotate_90deg_rightwards(p2)
        p4 = _rotate_90deg_rightwards(p3)
        f1, f2 = _flip(present)
        t = []
        for p in [p1, p2, p3, p4, f1, f2]:
            if p not in t:
                t.append(p)
        trasnformed_presents.append(t)
    return trasnformed_presents


def main(fname):
    presents, trees = _read_and_parse(fname)
    transformed_presents = _transformations(presents)
    for t in transformed_presents[1]:
        _print_grid(t)


if __name__ == '__main__':
    main('./test_data.txt')
