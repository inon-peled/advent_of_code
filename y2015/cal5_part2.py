def _check_rule_1(s):
    for i in range(len(s) - 1):
        pair1 = s[i:i + 2]
        for j in range(i + 2, len(s) - 1):
            pair2 = s[j:j + 2]
            if pair1 == pair2:
                return True

    return False


def _check_rule_2(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True

    return False


def _is_nice(s):
    is_valid = _check_rule_1(s) and _check_rule_2(s)
    return is_valid


def _read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines_clean = [l.rstrip() for l in lines]
    return lines_clean


def main(filename):
    lines_clean = _read_input(filename)
    total_nice = sum(_is_nice(s) for s in lines_clean)
    return total_nice


def _quick_test():
    assert _is_nice('qjhvhtzxzqqjkmpb')
    assert _is_nice('xxyxx')
    assert not _is_nice('uurcxstgmygtbstg')
    assert not _is_nice('ieodomkazucvgmuy')
    print('\n------ Quick test passed -----')


if __name__ == '__main__':
    _quick_test()
    print(main('data_c5.txt'))
