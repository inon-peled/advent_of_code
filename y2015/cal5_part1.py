def _check_rule_1(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_s = [c for c in s if c in vowels]
    num_vowels_in_s = len(vowels_in_s)
    is_valid = (num_vowels_in_s >= 3)
    return is_valid


def _check_rule_2(s):
    if len(s) < 2:
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True

    return False


def _check_rule_3(s):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    is_valid = all(s.find(f) == -1 for f in forbidden)
    return is_valid


def _is_nice(s):
    is_valid = _check_rule_1(s) and _check_rule_2(s) and _check_rule_3(s)
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
    assert _is_nice('ugknbfddgicrmopn')
    assert _is_nice('aaa')
    assert not _is_nice('jchzalrnumimnmhp')
    assert not _is_nice('haegwjzuvuyypxyu')
    assert not _is_nice('dvszwmarrgswjxmb')
    print('\n------ Quick test passed -----')


if __name__ == '__main__':
    _quick_test()
    print(main('data_c5.txt'))
