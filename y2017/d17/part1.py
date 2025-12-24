from collections import deque


def solve(insertions, forward):
    q = deque([0])
    for i in range(1, insertions + 1):
        q.rotate(-forward)
        head = q.popleft()
        q.appendleft(i)
        q.append(head)
        pass
    q.popleft()
    answer = q.popleft()
    return answer


if __name__ == '__main__':
    assert 638 == solve(2017, 3)
    print(solve(2017, 366))
