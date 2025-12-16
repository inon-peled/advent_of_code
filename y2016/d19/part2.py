'''
Solution idea, thanks to ChatGPT (https://chatgpt.com/share/6941bb97-e8e0-800e-83a1-0e0a13a28f04):
Use 2 double-ended queues (deques), to keep track of the elf across the current elf in O(1) updates.
'''

from collections import deque


def solve(n):
    middle = (n + 1) // 2
    d_left_half = deque([i, 1] for i in range(1, middle))
    d_right_half = deque([i, 1] for i in range(middle, n + 1))

    while len(d_left_half) + len(d_right_half) > 1:
        elf = d_left_half.popleft()
        elf_across = d_right_half.popleft()
        elf[1] += elf_across[1]
        d_right_half.append(elf)
        if len(d_right_half) - len(d_left_half) >= 2:
            balance_elf = d_right_half.popleft()
            d_left_half.append(balance_elf)

    if d_left_half:
        winner = d_left_half.popleft()
    else:
        winner = d_right_half.popleft()

    return winner[0]


if __name__ == '__main__':
    assert 2 == solve(5)
    print('Part 2 solution is:', solve(3018458))
