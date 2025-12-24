from collections import deque


def solve(insertions, forward):
    q = deque([0])

    for i in range(1, insertions + 1):
        q.rotate(-forward)
        head = q.popleft()
        q.appendleft(i)
        q.append(head)
        if i % 100_000 == 0:
            print(f'Finished {format(i, ',')} iterations')

    while True:
        head = q.popleft()
        if head == 0:
            answer = q.popleft()
            return answer
        else:
            q.append(head)


if __name__ == '__main__':
    print(solve(50_000_000, 366))
