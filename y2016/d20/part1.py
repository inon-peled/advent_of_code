from collections import deque


def _is_overlapping(t1, t2):
    return (t2[0] <= t1[0] <= t2[1]) or (t1[0] <= t2[0] <= t1[1]) or (t1[0] == t2[1] + 1) or (t2[0] == t1[1] + 1)


def _parse(fname):
    intervals = []
    with open(fname) as f:
        for line in f:
            t = [int(e) for e in line.split('-')]
            intervals.append(t)
    sorted_intervals = sorted(intervals)
    d = deque(sorted_intervals)
    return d

def _find_lowest_allowed_num(d):
    if not d:
        return 0

    while len(d) > 1:
        t1 = d.popleft()
        t2 = d.popleft()
        if _is_overlapping(t1, t2):
            t_merged = [min(t1[0], t2[0]), max(t1[1], t2[1])]
            d.appendleft(t_merged)
        else:
            return t1[1] + 1

    t = d.popleft()
    if t[1] <= 4294967295:
        return t[1] + 1
    else:
        return None


def solve(fname):
    d = _parse(fname)
    original_intervals = list(d)
    lowest_allowed_num = _find_lowest_allowed_num(d)

    # Sanity check
    for t in original_intervals:
        if t[0] <= lowest_allowed_num <= t[1]:
            print('Oops')

    return lowest_allowed_num


if __name__ == '__main__':
    assert 3 == solve('./test_data.txt')
    print('Part 1 solution is:', solve('./input.txt'))
