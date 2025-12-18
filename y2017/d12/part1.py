from collections import deque


def _parse(fname):
    g = {}
    with open(fname) as f:
        for line in f:
            left, right = line.strip().split('<->')
            right_split = right.split(', ')
            g[int(left)] = [int(r) for r in right_split]
    return g


def solve(g):
    s = {0}
    q = deque(g[0])
    while q:
        p = q.popleft()
        if p not in s:
            s.add(p)
            q.extend(g[p])
    answer = len(s)
    return answer


def main(fname):
    g = _parse(fname)
    answer = solve(g)
    return answer


if __name__ == '__main__':
    assert 6 == main('./test.txt')
    print(main('./input.txt'))
