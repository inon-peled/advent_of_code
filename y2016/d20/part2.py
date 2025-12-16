import sys
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


def _count_allowed(d):
    if not d:
        return 2 ** 32 - 1

    start = d.popleft()
    total_allowed = start[0]
    d.appendleft(start)

    while len(d) > 1:
        t1 = d.popleft()
        t2 = d.popleft()
        if _is_overlapping(t1, t2):
            t_merged = [min(t1[0], t2[0]), max(t1[1], t2[1])]
            d.appendleft(t_merged)
        else:
            total_allowed += t2[0] - t1[1] - 1
            d.appendleft(t2)

    t = d.popleft()
    total_allowed += 4294967295 - t[1]
    return total_allowed


def solve(fname):
    d = _parse(fname)
    answer = _count_allowed(d)
    return answer


if __name__ == '__main__':
    print('Part 2 solution is:', solve('./input.txt'))
