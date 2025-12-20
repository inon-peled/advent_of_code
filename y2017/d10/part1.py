def _parse(fname):
    g = {}
    w = {}
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if ' -> ' in line:
                root, children = line.split(' -> ')
            else:
                root = line
                children = None
            r, weight = root.replace('(', '').replace(')', '').split(' ')
            w[r] = int(weight)
            if children is not None:
                g[r] = children.split(', ')
                for child in g[r]:
                    g[child] = g.get(child, [])
    return g, w


def solve(g):
    """Find the node that has no father."""
    for node in g:
        if not any (node in children for children in g.values()):
            return node
    return None


def main(fname):
    g, w = _parse(fname)
    answer = solve(g)
    return answer


if __name__ == '__main__':
    assert 'tknk' == main('./test.txt')
    print(main('./input.txt'))
