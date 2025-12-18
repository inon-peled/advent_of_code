'''
Solution idea:
There are just 8 numbered locations in the board, so a brute force solution is possible,
when done efficiently as follows:
1. Calculate distance between every pair of numbered locations, by running BFS from each of them.
2. Find the minimum value over all permutations of the numbered locations, where for each permutation
   n_0 -> n_1 -> ... n_7, the value is the sum of n_i -> n_{i + 1} distances.
'''

from collections import deque
from itertools import permutations


def _bfs(start, neighbors_func, board):
    q = deque([start])
    dist = {start: 0}
    prev = {}

    while q:
        u = q.popleft()
        for v in neighbors_func(u, board):
            if v not in dist:
                dist[v] = dist[u] + 1
                prev[v] = u
                q.append(v)

    return dist


def _extract(start, numbers, dist):
    extracted = dict()

    for num in numbers:
        i, j = numbers[num]
        extracted[num] = dist[i, j]

    return extracted


def _valid_neighbors(state, board):
    i, j = state
    w = len(board[0])
    h = len(board)

    candidates = [
        (i - 1, j),  # Up
        (i + 1, j),  # Down
        (i, j - 1),  # Left
        (i, j + 1)  # Right
    ]

    n = []
    for c in candidates:
        if (0 <= c[0] < h) and (0 <= c[1] < w) and (board[c[0]][c[1]] != '#'):
            n.append(c)
    return n


def _find_numbers(board):
    numbers = dict()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][0] in '1234567890':
                num = int(board[i][j])
                numbers[num] = i, j
    return numbers


def _pairwise_distances(numbers, board):
    pairs = dict()
    for num in numbers:
        start = numbers[num]
        dist = _bfs(start, _valid_neighbors, board)
        extracted = _extract(start, numbers, dist)
        pairs[num] = extracted
    return pairs


def _find_minimum_path(numbers, pairs, is_circular):
    min_path_len = None
    non_zero_nums = [num for num in numbers if num != 0]
    for perm in permutations(non_zero_nums):
        path_len = 0
        path = [0] + list(perm)
        if is_circular:
            path += [0]
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            edge_len = pairs[u][v]
            path_len += edge_len
        if min_path_len is None or path_len < min_path_len:
            min_path_len = path_len
    return min_path_len


def solve(board, is_circular):
    numbers = _find_numbers(board)
    pairs = _pairwise_distances(numbers, board)
    min_path_len = _find_minimum_path(numbers, pairs, is_circular)
    return min_path_len


def _parse(fname):
    board = []
    for line in open(fname):
        board.append([e for e in line.strip()])
    return board


def main(fname, is_circular):
    board = _parse(fname)
    solution = solve(board, is_circular)
    return solution


if __name__ == '__main__':
    assert 14 == main('./test_data.txt', False)
    print('Part 1 solution is:', main('./input.txt', False))
    print('Part 2 solution is:', main('./input.txt', True))
