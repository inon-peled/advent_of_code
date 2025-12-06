from hashlib import md5

SECRET = 'bgvyzdsv'


def main(secret, min_zeroes_in_prefix):
    i = 0
    while True:
        # if i % (10 ** 6) == 0:
        #     print(f'Processed {i} strings so far...')
        i += 1
        concat = f'{secret}{i}'
        checksum = md5(concat.encode()).hexdigest()
        if checksum[:min_zeroes_in_prefix] == ('0' * min_zeroes_in_prefix):
            return i


def _quick_test():
    assert 609043 == main('abcdef', 5)
    assert 1048970 == main('pqrstuv', 5)
    print('\n------ Quick test passed ------')


if __name__ == '__main__':
    _quick_test()
    print(f'\nPart 1 solution: {main(SECRET, 5)}')
    print(f'\nPart 2 solution: {main(SECRET, 6)}')
