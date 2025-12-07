TEST_DATA = [
    ("Butterscotch", -1, -2, 6, 3, 8),
    ("Cinnamon", 2, 3, -2, -1, 3),
]

DATA = [
    ("Sprinkles", 2, 0, -2, 0, 3),
    ("Butterscotch", 0, 5, -3, 0, 3),
    ("Chocolate", 0, 0, 5, -1, 8),
    ("Candy", 0, -1, 0, 5, 8),
]


def split(n, k):
    if k == 1:
        yield (n,)
    else:
        for x in range(n + 1):
            for rest in split(n - x, k - 1):
                yield (x,) + rest


def _calc_one_combination(data, amounts):
    num_props = len(data[0]) - 2  # Without name and calories
    totals = [0] * num_props
    ingredients = [d[1:-1] for d in data]

    for i in range(len(ingredients)):
        for k in range(num_props):
            totals[k] += ingredients[i][k] * amounts[i]

    if any(t < 0 for t in totals):
        return 0
    value = 1
    for total in totals:
        value *= total
    return value


def solve(data, teaspoons):
    num_ingredients = len(data)
    best_value = 0
    for s in split(teaspoons, num_ingredients):
        curr_value = _calc_one_combination(data, s)
        if best_value < curr_value:
            best_value = curr_value
    return best_value


if __name__ == '__main__':
    assert 62842880 == solve(TEST_DATA, 100)
    print()
    print(solve(DATA, 100))
