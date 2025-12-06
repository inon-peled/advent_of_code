def _factorize(num):
    factors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors


def _count_gifts(house_number):
    factors = _factorize(house_number)
    num_gifts = 10 * sum(factors)
    return num_gifts


def _test():
    cases = [[1, 10],
             [2, 30],
             [3, 40],
             [4, 70],
             [5, 60],
             [6, 120],
             [7, 80],
             [8, 150],
             [9, 130]]
    for num, expected in cases:
        got = _count_gifts(num)
        assert got == expected


def main(min_gifts):
    i = 0
    while True:
        i += 1
        if i % (10 ** 5) == 0:
            print(f'Processed {i} numbers so far...')
        gifts = _count_gifts(i)
        if gifts >= min_gifts:
            print(f'\nAnswer: {i}')
            break


if __name__ == '__main__':
    _test()
    main(29000000)
