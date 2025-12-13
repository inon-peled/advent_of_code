"""
Solution outline:
As it turns out (ref. https://aoc.winslowjosiah.com/solutions/2025/day/12/), the given data is amenable to a solution
via a simple heuristic (unlike the general packing problem), whereby each tree is satisfiable if-and-only-if the
total number of presents that it requires is at most (tree height // 3) * (tree width // 3).
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


def _solve_special_case(tree):
    total_presents = sum(tree['amounts'])
    num_tiles = (tree['w'] // 3) * (tree['h'] // 3)
    is_satisfiable = (total_presents <= num_tiles)
    return is_satisfiable


def main(fname):
    presents, trees = _read_and_parse(fname)

    total_satisfiable = 0
    for tree in tqdm(trees):
        is_satisfiable = _solve_special_case(tree)
        total_satisfiable += is_satisfiable

    return total_satisfiable


if __name__ == '__main__':
    print(main('./data.txt'))
