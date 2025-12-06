def _next_pswd(p):
    next_p = list(p)

    for i in range(-1, -len(next_p) - 1, -1):
        if next_p[i] == 'z':
            next_p[i] = 'a'
        else:
            curr_ord = ord(p[i])
            next_ord = curr_ord + 1
            next_chr = chr(next_ord)
            next_p[i] = next_chr
            break

    next_p_str = ''.join(next_p)
    return next_p_str


def _rule1(p):
    for i in range(len(p) - 2):
        if ord(p[i]) == ord(p[i + 1]) - 1 == ord(p[i + 2]) - 2:
            return True
    return False


def _rule2(p):
    good = not ('i' in p or 'o' in p or 'l' in p)
    return good


def _rule3(p):
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    num_pairs = 0
    for l in letters:
        num_pairs += f'{l}{l}' in p
        if num_pairs >= 2:
            return True
    return False


def _good_pswd(p):
    r1 = _rule1(p)
    r2 = _rule2(p)
    r3 = _rule3(p)
    good = r1 and r2 and r3
    return good


def main(pswd):
    original_pswd = pswd
    while not _good_pswd(pswd):
        pswd = _next_pswd(pswd)
        if pswd == original_pswd:
            print('No good password exists :-(')
            return
    return pswd


def _quick_test_next_pswd():
    for p, expected in [
        ('abcdefgh', 'abcdefgi'),
        ('abcdefgz', 'abcdefha'),
        ('qzzz', 'raaa'),
        ('zzzz', 'aaaa')
    ]:
        got = _next_pswd(p)
        assert got == expected

    print('----- next_pswd test passed -----')


def _quick_test_good_pswd():
    assert not _good_pswd('hijklmmn')
    assert not _good_pswd('abbceffg')
    assert not _good_pswd('abbcegjk')
    assert _good_pswd('abcdffaa')
    assert _good_pswd('ghjaabcc')
    print('----- test_good_pswd passed -----')


def _quick_test_main():
    assert main('abcdefgh') == 'abcdffaa'
    assert main('ghijklmn') == 'ghjaabcc'
    print('----- main test passed -----')


def _quick_tests():
    _quick_test_next_pswd()
    _quick_test_good_pswd()
    _quick_test_main()


if __name__ == '__main__':
    # _quick_tests()
    print('\nSolution to part 1 is', main('hxbxwxba'))
    print('\nSolution to part 2 is', main(_next_pswd('hxbxxyzz')))
