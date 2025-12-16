from collections import deque
from hashlib import md5


def _bfs(start, goal_func, neighbors_func):
    q = deque([start])
    dist = {start: 0}
    prev = {}

    while q:
        u = q.popleft()
        if goal_func(u):
            return u

        for v in neighbors_func(u):  # neighbors(u) -> iterable of nodes
            if v not in dist:
                dist[v] = dist[u] + 1
                prev[v] = u
                q.append(v)

    return None


def _valid_neighbors(state):
    i, j, path_so_far = state
    candidates = [
        (i - 1, j),  # Up
        (i + 1, j),  # Down
        (i, j - 1),  # Left
        (i, j + 1)  # Right
    ]
    lock_stat_str = md5(path_so_far.encode()).hexdigest()[:4]
    lock_stat_bool = [l in 'bcdef' for l in lock_stat_str]

    n = []
    directions = 'UDLR'
    for k in range(len(directions)):
        c = candidates[k]
        if (0 <= c[0] <= 3) and (0 <= c[1] <= 3) and lock_stat_bool[k]:
            neighbor_state = (c[0], c[1], path_so_far + directions[k])
            n.append(neighbor_state)

    return n


def _goal(u):
    bottom_right = (u[0] == u[1] == 3)
    return bottom_right


def solve(passcode):
    start = (0, 0, passcode)
    final_state = _bfs(start=start, goal_func=_goal, neighbors_func=_valid_neighbors)
    answer = final_state[-1][len(passcode):]
    return answer


def _test():
    cases = [
        ('ihgpwlah', 'DDRRRD'),
        ('kglvqrro', 'DDUDRLRRUDRD'),
        ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')
    ]
    for pscd, expected in cases:
        actual = solve(pscd)
        assert actual == expected
    print('All test cases passed.')


if __name__ == '__main__':
    _test()
    print('Part 1 solution is:', solve('qljzarfv'))
