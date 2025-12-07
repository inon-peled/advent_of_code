def process_one_deer(speed, fly, rest, total_time):
    lag_duration = fly + rest
    lag_distance = speed * fly
    num_full_lags = total_time // lag_duration
    distance_full_lags = lag_distance * num_full_lags

    remainder = total_time % lag_duration
    remainder_fly_time = min(remainder, fly)
    remainder_distance = speed * remainder_fly_time

    total_distance = distance_full_lags + remainder_distance
    return total_distance


def read_and_parse(filename):
    deers = []
    for line in open(filename).readlines():
        s = line.split()
        name = s[0]
        speed = int(s[3])
        fly = int(s[6])
        rest = int(s[-2])
        deers.append((name, speed, fly, rest))

    return deers


def _calc_state(deers, total_time):
    state = []
    for deer in deers:
        distance = process_one_deer(deer[1], deer[2], deer[3], total_time)
        state.append(distance)
    return state

def solve(deers, total_time):
    scores = [0] * len(deers)
    for i in range(total_time):
        state = _calc_state(deers, i + 1)
        best_distance = max(state)
        for j in range(len(state)):
            if state[j] == best_distance:
                scores[j] += 1
    best_score = max(scores)
    return best_score


if __name__ == '__main__':
    test_data = read_and_parse('test.txt')
    assert 1 == solve(test_data, 1)
    assert 139 == solve(test_data, 140)
    assert 689 == solve(test_data, 1000)
    print()
    print(solve(read_and_parse('data.txt'), 2503))
