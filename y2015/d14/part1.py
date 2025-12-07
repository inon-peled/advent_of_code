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


def solve(deers, total_time):
    final = []
    for deer in deers:
        distance = process_one_deer(deer[1], deer[2], deer[3], total_time)
        final.append(distance)
    best = max(final)
    return best


if __name__ == '__main__':
    test_data = read_and_parse('test.txt')
    assert 16 == solve(test_data, 1)
    assert 160 == solve(test_data, 10)
    assert 176 == solve(test_data, 11)
    assert 176 == solve(test_data, 12)
    assert 1120 == solve(test_data, 1000)
    print()
    print(solve(read_and_parse('data.txt'), 2503))
