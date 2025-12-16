'''
Solution idea: Simulate the game using a double-ended queue (deque).
In this manner, every update of the game takes place at the end of the deque in just O(1) time.
'''

from collections import deque


def solve(n):
    d = deque([i, 1] for i in range(1, n + 1))

    while len(d) > 1:
        elf = d.popleft()
        next_elf = d.popleft()
        elf[1] += next_elf[1]
        d.append(elf)

    winner = d.popleft()
    return winner[0]


if __name__ == '__main__':
    assert 3 == solve(5)
    print('Part 1 solution is:', solve(3018458))
