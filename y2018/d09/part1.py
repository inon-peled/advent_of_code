from collections import deque


def _simulate(num_players, max_marble):
    q = deque([0])
    scores = [0] * num_players
    m = 1
    while True:
        for p in range(num_players):
            if m > max_marble:
                return scores
            if m % 23 == 0:
                scores[p] += m
                q.rotate(7)
                other_m = q.popleft()
                scores[p] += other_m
            else:
                q.append(q.popleft())
                q.append(q.popleft())
                q.appendleft(m)
            m += 1


def solve(num_players, max_marble):
    scores = _simulate(num_players, max_marble)
    winner_score = max(scores)
    return winner_score


if __name__ == '__main__':
    assert 32 == solve(9, 25)
    assert 8317 == solve(10, 1618)
    assert 146373 == solve(13, 7999)
    assert 2764 == solve(17, 1104)
    assert 54718 == solve(21, 6111)
    assert 37305 == solve(30, 5807)
    print('Part 1 answer is:', solve(452, 71250))
    print('Part 2 answer is:', solve(452, 7125000))
