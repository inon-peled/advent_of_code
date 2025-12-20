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


def _find_root(g):
    """Find the node that has no father."""
    for node in g:
        if not any(node in children for children in g.values()):
            return node
    return None


def _sub_tree_weights(node, g, w, w_sub_trees):
    if not g:
        w_sub_trees[node] = w[node]
        return

    w_sub_trees[node] = w[node]
    for c in g[node]:
        _sub_tree_weights(c, g, w, w_sub_trees)
        w_sub_trees[node] += w_sub_trees[c]


def solve(g, w, w_sub_trees):
    for children in g.values():
        b = [w_sub_trees[c] for c in children]
        for i in range(len(b) - 1):
            if b[i] != b[i + 1]:
                lighter_idx = i if b[i] < b[i + 1] else i + 1
                weight_diff = abs(b[i] - b[i + 1])
                heavier_idx = i if lighter_idx == i + 1 else i + 1
                child = children[heavier_idx]
                self_weight = w[child]
                lighter_self_weight = self_weight - weight_diff
                return lighter_self_weight
    return None


def main(fname):
    g, w = _parse(fname)
    root = _find_root(g)
    w_sub_trees = {}
    _sub_tree_weights(node=root, g=g, w=w, w_sub_trees=w_sub_trees)
    answer = solve(g=g, w=w, w_sub_trees=w_sub_trees)
    return answer


if __name__ == '__main__':
    assert 60 == main('./test.txt')
    print(main('./input.txt'))
