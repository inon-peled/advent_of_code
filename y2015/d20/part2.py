from collections import defaultdict


def _factorize(num):
    factors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors


def _count_gifts(elf_visits, house_number):
    factors = _factorize(house_number)
    num_gifts = 0
    for f in factors:
        if elf_visits[f] <= 50:
            num_gifts += 11 * f
            elf_visits[f] += 1
    return num_gifts


def main(min_gifts):
    i = 0
    elf_visits = defaultdict(int)
    while True:
        i += 1
        if i % (10 ** 5) == 0:
            print(f'Processed {i:,} numbers so far...')
        gifts = _count_gifts(elf_visits, i)
        if gifts >= min_gifts:
            print(f'\nAnswer: {i}')
            break


if __name__ == '__main__':
    main(29000000)
