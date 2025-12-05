def _read_input(path):
    with open(path, 'r') as f_in:
        directions = f_in.read().rstrip()
    return directions


def _split_directions(directions):
    d_santa = directions[0:len(directions):2]
    d_robot = directions[1:len(directions):2]
    return d_santa, d_robot


def _simulate(directions):
    loc = [0, 0]
    visited_locations = {tuple(loc)}

    for d in directions:
        if d == '<':
            loc[0] -= 1
        elif d == '>':
            loc[0] += 1
        elif d == '^':
            loc[1] += 1
        else:
            loc[1] -= 1
        visited_locations.add(tuple(loc))

    return visited_locations


def _solve(directions):
    d_santa, d_robot = _split_directions(directions)
    visited_santa = _simulate(d_santa)
    visited_robot = _simulate(d_robot)
    all_visited = visited_santa | visited_robot
    num_all_visited = len(all_visited)
    return num_all_visited


def main(input_path):
    directions = _read_input(input_path)
    num_visited = _solve(directions)
    return num_visited


def _quick_test():
    assert 3 == _solve('^v')
    assert 3 == _solve('^>v<')
    assert 11 == _solve('^v^v^v^v^v')
    print('\n------ Quick test passed successfully ------')


if __name__ == '__main__':
    _quick_test()
    print(main('data_c3.txt'))
