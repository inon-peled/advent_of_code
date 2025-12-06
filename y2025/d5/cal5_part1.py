def _read_input_file(filename):
    in_ranges = True
    ranges = []
    ingredients = []

    with open(filename) as f_input:
        for line_raw in f_input:
            line = line_raw.strip()

            if line == '':
                in_ranges = False
                continue

            if in_ranges:
                rng = tuple(int(num) for num in line.split('-'))
                ranges.append(rng)
            else:
                grd = int(line)
                ingredients.append(grd)

    return ranges, ingredients


def _count_fresh_ingredients(ranges, ingredients):
    count_fresh = 0

    for grd in ingredients:
        for rng in ranges:
            if rng[0] <= grd <= rng[1]:
                count_fresh += 1
                break

    return count_fresh


def _quick_test():
    ranges, ingredients = _read_input_file('test_data_c5.txt')
    got = _count_fresh_ingredients(ranges=ranges, ingredients=ingredients)
    expected = 3
    assert got == expected, f'Expected {expected} but got {got}'
    print('\n------ Quick test passed successfully ------')


def main(filename):
    ranges, ingredients = _read_input_file(filename)
    solution = _count_fresh_ingredients(ranges=ranges, ingredients=ingredients)
    return solution


if __name__ == '__main__':
    _quick_test()
    solution = main('data_c5.txt')
    print(f'\nSolution is {solution}')
