def _read_input(path):
    with open(path, 'r') as f_in:
        lines = f_in.readlines()

    lines_parsed = [tuple(int(d) for d in l.rstrip().split('x')) for l in lines]
    return lines_parsed


def main(input_path):
    gifts = _read_input(input_path)
    total_ribbon = 0

    for g in gifts:
        smallest_face = 2 * min(g[0] + g[1], g[1] + g[2], g[2] + g[0])
        gift_volume = g[0] * g[1] * g[2]
        total_ribbon += smallest_face + gift_volume

    return total_ribbon


if __name__ == '__main__':
    print(main('data_c2.txt'))
