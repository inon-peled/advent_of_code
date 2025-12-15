def solve(fname, min_or_max):
    columns = None
    with open(fname) as f:
        for line in f:
            stripped = line.strip()
            if columns is None:
                num_cols = len(stripped)
                columns = [[] for _ in range(num_cols)]
            for i, c in enumerate(stripped):
                columns[i].append(c)

    message = ''
    for col in columns:
        selected_char = min_or_max(set(col), key=col.count)
        message += selected_char
    return message


if __name__ == '__main__':
    assert 'easter' == solve('test_data.txt', max)
    print('Solution to part 1:', solve('input.txt', max))

    assert 'advent' == solve('test_data.txt', min)
    print('Solution to part 2:', solve('input.txt', min))
