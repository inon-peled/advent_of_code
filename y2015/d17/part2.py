from itertools import combinations

CONTAINERS = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
TARGET = 150

TEST_CONTAINERS = [20, 15, 10, 5, 5]
TEST_TARGET = 25


def _count_under_constaint(containers, target, exact_num_to_choose):
    total_combinations = 0
    for chosen_volumes in combinations(containers, exact_num_to_choose):
        total_chosen_volumes = sum(chosen_volumes)
        if total_chosen_volumes == target:
            total_combinations += 1
    return total_combinations


def solve(containers, target):
    for i in range(1, len(containers)):
        count = _count_under_constaint(containers, target, i)
        if count > 0:
            return count


assert 3 == solve(TEST_CONTAINERS, TEST_TARGET)
print(solve(CONTAINERS, TARGET))
