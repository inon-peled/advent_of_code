def _read_input_file(filename):
    ranges = []

    with open(filename) as f_input:
        for line_raw in f_input:
            line = line_raw.strip()
            if line != '':
                rng = tuple(int(num) for num in line.split('-'))
                ranges.append(rng)
            else:
                break

    return ranges

def _unify_two_overlapping_ranges(r1, r2):
    unified_start = min(r1[0], r2[0])
    unified_end = max(r1[1], r2[1])
    unified_range = unified_start, unified_end
    return unified_range


def _is_overlapping(u, v):
    is_overlap = (v[0] <= u[0] <= v[1]) or (v[0] <= u[1] <= v[1]) or (u[0] <= v[0] <= u[1]) or (u[0] <= v[1] <= u[1])
    return is_overlap


def _unify(sorted_ranges):
    unified = []
    if not sorted_ranges:
        return unified

    i = 0
    overlap = sorted_ranges[i]

    while True:
        i += 1
        if i >= len(sorted_ranges):
            unified.append(overlap)
            break

        next = sorted_ranges[i]
        if _is_overlapping(overlap, next):
            overlap = _unify_two_overlapping_ranges(overlap, next)
        else:
            unified.append(overlap)
            overlap = next

    return unified


def _count_total_ingredients(unified_distinct_ranges):
    total = 0

    for rng in unified_distinct_ranges:
        rng_size = rng[1] - rng[0] + 1
        total += rng_size

    return total


def main(filename):
    ranges = _read_input_file(filename)
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    unified_distinct_ranges = _unify(sorted_ranges)
    total_ingredients = _count_total_ingredients(unified_distinct_ranges)
    return total_ingredients


def _quick_test():
    got = main('test_data_c5.txt')
    expected = 14
    assert got == expected, f'Expected {expected} but got {got}'
    print('\n------ Quick test passed successfully ------')


if __name__ == '__main__':
    _quick_test()
    solution = main('data_c5.txt')
    print(f'\nSolution is {solution}')
