"""
Solution idea:
Backtrack until finding a solution. Use memoization to prune early, with the following key:
frozenset([(shape_idx, rotation_idx, top_left_x, top_lefy_y) for every shape on the board]).
"""
from tqdm import tqdm


def _read_and_parse_presents(lines):
    presents = []
    curr_present = None
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
        print(''.join(['#' if e == '#' else '.' for e in row]))


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


def _init_grid(tree):
    return [
        ['.' for _ in range(tree['w'])]
        for _ in range(tree['h'])
    ]


def _check_if_can_put(t, i, j, grid):
    for r in range(3):
        for c in range(3):
            if grid[i + r][j + c] == t[r][c] == '#':
                return False

    return True


def _put_in_grid(t, i, j, grid):
    before = [[None] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            before[r][c] = grid[i + r][j + c]
            if t[r][c] == '#':
                grid[i + r][j + c] = t[r][c]
    return before


def _revert_grid(i, j, grid, before):
    for r in range(3):
        for c in range(3):
            grid[i + r][j + c] = before[r][c]


def solve(grid, w, h, amounts, transformed_presents, memo, grid_status, remaining_i_j):
    if grid_status in memo:
        return memo[grid_status]

    if all(a == 0 for a in amounts):
        _print_grid(grid)
        memo[grid_status] = True
        return True

    p_idx = None
    for p_idx in range(len(amounts)):
        if amounts[p_idx] > 0:
            break

    new_amounts = amounts[:]
    new_amounts[p_idx] -= 1

    trans = transformed_presents[p_idx]
    for t_idx, t in enumerate(trans):
        for i, j in remaining_i_j:
            if _check_if_can_put(t, i, j, grid):
                before = _put_in_grid(t, i, j, grid)
                new_grid_status = grid_status | frozenset({(i, j, p_idx, t_idx)})
                new_remaining_i_j = [(r, c) for r, c in remaining_i_j if (r, c) != (i, j)]
                sol = solve(
                    grid=grid,
                    w=w,
                    h=h,
                    amounts=new_amounts,
                    transformed_presents=transformed_presents,
                    memo=memo,
                    grid_status=new_grid_status,
                    remaining_i_j=new_remaining_i_j
                )
                _revert_grid(i, j, grid, before)
                if sol:
                    memo[grid_status] = True
                    return True

    memo[grid_status] = False
    return False


def main(fname):
    presents, trees = _read_and_parse(fname)
    transformed_presents = _transformations(presents)
    num_satisfiable = 0

    for tree in tqdm(trees):
        grid = _init_grid(tree)
        num_satisfiable += solve(
            w=tree['w'],
            h=tree['h'],
            amounts=list(tree['amounts']),
            transformed_presents=transformed_presents,
            grid=grid,
            memo=dict(),
            grid_status=frozenset(),
            remaining_i_j=[(i, j) for i in range(tree['h'] - 2) for j in range(tree['w'] - 2)]
        )

    return num_satisfiable


if __name__ == '__main__':
    assert 2 == main('./test_data.txt')
    print(main('./data.txt'))
