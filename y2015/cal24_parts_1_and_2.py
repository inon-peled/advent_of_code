from math import prod


def _read_input(filename):
    with open(filename) as f_in:
        lines = f_in.readlines()
    lines_parsed = [int(l) for l in lines]
    return lines_parsed


def _rec_candidates(weights, target_size, target_weight):
    if target_size == 1:
        if target_weight in weights:
            yield [target_weight]
    else:
        for i in range(len(weights)):
            for sol in _rec_candidates(weights[i + 1:], target_size - 1, target_weight  - weights[i]):
                yield sol + [weights[i]]


def _solve(weights, num_packages):
    """
    The below presumes that for every candidate, the remaining weights can be split as required.
    """

    target_weight = sum(weights) / num_packages
    best_entag = None

    for target_size in range(1, len(weights)):
        print(f'Now trying {target_size=}...')
        for candidate in _rec_candidates(weights, target_size, target_weight):
            entag = int(prod(candidate))
            if best_entag is None or entag < best_entag:
                best_entag = entag
        if best_entag is not None:
            return best_entag
        else:
            print(f'Did not find a candidate for {target_size=}.')


def main(filename, num_packages):
    weights = _read_input(filename)
    solution = _solve(weights, num_packages)
    return solution


def _quick_test():
    test_weights = list(range(1, 6)) + list(range(7, 12))
    solution = _solve(test_weights, 3)
    assert 99 == solution
    print("\n------- Quick test passed -----")


if __name__ == '__main__':
    _quick_test()
    print('\nPart 1 solution:', main("data_c24.txt", 3))
    print('\nPart 2 solution:', main("data_c24.txt", 4))
