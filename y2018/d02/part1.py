from collections import defaultdict


def _process(s):
    d = defaultdict(int)
    for letter in s:
        d[letter] += 1
    exactly_2 = any(v == 2 for v in d.values())
    exactly_3 = any(v == 3 for v in d.values())
    return exactly_2, exactly_3


def main(fname):
    with open(fname) as f:
        exactly_2 = 0
        exactly_3 = 0
        for line in f:
            p2, p3 = _process(line)
            exactly_2 += p2
            exactly_3 += p3
    mul = exactly_2 * exactly_3
    return mul


if __name__ == '__main__':
   print(main('./input.txt'))
