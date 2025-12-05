def _read_input(path):
    with open(path, 'r') as f_in:
        directions = f_in.read().rstrip()
    return directions


def _solve(directions):
    loc = [0, 0]
    visited_locations = set(tuple(loc))

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

    num_visited = len(visited_locations)
    return num_visited


def main(input_path):
    directions = _read_input(input_path)
    num_visited = _solve(directions)
    return num_visited


if __name__ == '__main__':
    print(main('data_c3.txt'))
