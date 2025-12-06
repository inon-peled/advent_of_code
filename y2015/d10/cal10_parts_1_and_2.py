def _process_once(num):
    description = ''
    s = str(num)

    if len(s) == 1:
        return f'1{s}'

    i = 0

    for j in range(1, len(s)):
        if s[j] != s[i]:
            sequence_length = j - i
            char = s[i]
            description += f'{sequence_length}{char}'
            i = j

    sequence_length = j - i + 1
    char = s[j]
    description += f'{sequence_length}{char}'

    return description


def _quick_test():
    for num, expected in [
        (1, 11),
        (11, 21),
        (21, 1211),
        (1211, 111221),
        (111221, 312211),
        (333333, 63),
        (11112, 4112)
    ]:
        got = _process_once(num)
        assert str(expected) == got
    print('\n------ Test passed -----')


def main(num, repeat):
    next_num = num
    for _ in range(repeat):
        next_num = _process_once(next_num)
    result = len(next_num)
    return result


if __name__ == '__main__':
    _quick_test()

    solution1 = main(1321131112, 40)
    print('\nSolution to part 1:', solution1)

    solution2 = main(1321131112, 50)
    print('\nSolution to part 2:', solution2)
