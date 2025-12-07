from itertools import product

CONTAINERS = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
TARGET = 150

TEST_CONTAINERS = [20, 15, 10, 5, 5]
TEST_TARGET = 25


def solve(containers, target):
    total_combinations = 0
    for choice in product([0, 1], repeat=len(containers)):
        chosen_volumes = [containers[i] for i in range(len(choice)) if choice[i]]
        total_chosen_volumes = sum(chosen_volumes)
        if total_chosen_volumes == target:
            total_combinations += 1
    return total_combinations


assert 4 == solve(TEST_CONTAINERS, TEST_TARGET)
print(solve(CONTAINERS, TARGET))
