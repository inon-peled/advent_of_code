def _parse(fname):
    return [int(r) for r in open(fname)]


def solve(nums):
    i = 0
    total = 0
    seen = {0}
    while True:
        total += nums[i]
        if total in seen:
            return total
        seen.add(total)
        i = (i + 1) % len(nums)


if __name__ == '__main__':
    assert 0 == solve([1, -1])
    assert 10 == solve([+3, +3, +4, -2, -4])
    assert 5 == solve([-6, +3, +8, +5, -6])
    assert 14 == solve([+7, +7, -2, -7, -4])
    print(solve(_parse('./input.txt')))
