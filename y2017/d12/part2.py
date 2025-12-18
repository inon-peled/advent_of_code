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
    nodes = set(g.keys())
    num_groups = 0

    while nodes:
        v = next(iter(nodes))
        s = set()
        q = deque([v])
        num_groups += 1
        while q:
            p = q.popleft()
            if p not in s:
                s.add(p)
                nodes.remove(p)
                q.extend(g[p])

    return num_groups


def main(fname):
    g = _parse(fname)
    answer = solve(g)
    return answer


if __name__ == '__main__':
    assert 2 == main('./test.txt')
    print(main('./input.txt'))
