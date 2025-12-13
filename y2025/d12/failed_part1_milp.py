### DOES NOT WORK: MILP INSTANCES TAKE TOO MUCH TIME AND MEMORY TO BUILD.


"""
Solution idea:
Run a Mixed-Integer Linear Programming (MILP) solver on the following problem form:

    min c * x
    Subject to:
    0 <= x <= 1
    l <= A * x <= u
    All x are integers

where:

# x = decision variables, one per (p_idx, inst_num, rot_idx, i, j), where:
## p_idx runs on present indexes.
## inst_num runs on number of instances of the present.
## rot_idx runs on all possible transformation of the present.
## (i, j) is the position, in the tree's region, of the top left corner of the transformed present instance.
   Because every present is 3x3, i ranges on (0, tree height - 2) and j ranges on (0, tree width - 2).

# c = vector of minus ones, same length as x.

# A, l, u represent the following constraints:

## Exactly one transformation per present instance:
   For every p_idx and inst_num as defined above, define for every x:
        r(p_idx, inst_num, x) = 1 if x applies to p_idx and inst_num, otherwise 0,
   and require:
        1 <= sum(r(inst_num, x) over all x) <= 1

## No overlaps:
   For every position n in the tree's region, define for every x:
        v(n, x) = 1 if x covers p, otherwise 0,
   and require:
        0 <= sum(v(n, x) over all x) <= 1

This formulation has a solution if-and-only-if the tree's region can fit all present instances.
"""
from tqdm import tqdm


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
        trees.append({'w': w, 'h': h, 'amounts': amounts})
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


def _is_covering(t, tree):
    for r in len(t):
        for c in len(t[0]):
            pass


def _is_satisfiable(tree, transformed_presents):
    total_instances = sum(tree['amounts'])
    num_transformations_per_instance = len(transformed_presents[0])
    num_variables = tree['w'] * tree['h'] * total_instances * num_transformations_per_instance
    print('total instances:', total_instances)
    print('number of transformations:', num_transformations_per_instance)
    print('number of variables:', num_variables)

    # c = [-1] * num_variables
    # A = []
    # l = []
    # u = []
    #
    # # Constraint: exactly one instance
    # for amount in tree['amounts']:
    #     k = 0
    #     # For every present instance
    #     for _ in range(amount):
    #         # For every position in the tree where the top left corner of the instance can be placed:
    #         for i in range(tree['h'] - 2):
    #             for j in range(tree['w'] - 2):
    #                 l.append(1)
    #                 u.append(1)
    #                 A.append(
    #                     [0] * k +
    #                     [1] * num_transformations_per_instance +
    #                     [0] * (num_variables - k - num_transformations_per_instance)
    #                 )
    #                 k += num_transformations_per_instance

    return False
    # # Constraint: no overlapping instances
    # for i in range(tree['h'] - 2):
    #     for j in range(tree['w'] - 2):
    #         for present_idx, amount in enumerate(tree['amounts']):
    #             trans = transformed_presents[present_idx]
    #             for _ in amount:
    #                 for t in trans:
    #                     l.append(0)
    #                     u.append(1)
    #                     A.append(_is_covering(t, i, j, tree)


def main(fname):
    presents, trees = _read_and_parse(fname)
    transformed_presents = _transformations(presents)

    num_satisfiable = 0
    for tree in tqdm(trees):
        num_satisfiable += _is_satisfiable(tree, transformed_presents)

    return num_satisfiable


if __name__ == '__main__':
    main('./test_data.txt')
    main('./data.txt')
