def _init_screen(w, h):
    return [['.' for _ in range(w)] for _ in range(h)]


def _rect(screen, top_left_x, top_left_y, rect_w, rect_h):
    for i in range(top_left_y, top_left_y + rect_h):
        for j in range(top_left_x, top_left_x + rect_w):
            screen[i][j] = '#'
    pass


def _rotate(lst, by):
    rotated = lst[-by:] + lst[:-by]
    return rotated


def _rotate_row(screen, y, by):
    screen[y] = _rotate(screen[y], by)
    pass


def _rotate_column(screen, x, by):
    original = [screen[i][x] for i in range(len(screen))]
    rotated = _rotate(original, by)
    for i in range(len(screen)):
        screen[i][x] = rotated[i]
    pass


def _follow_instructions(instructions, screen, top_left_x, top_left_y):
    for inst in instructions:
        if inst.startswith('rect'):
            rect_w, rect_h = [int(e) for e in inst.split()[-1].split('x')]
            _rect(screen, top_left_x, top_left_y, rect_w, rect_h)
        else:
            inst_split = inst.split()
            by = int(inst_split[-1])
            is_column = (inst_split[1] == 'column')
            idx = int(inst_split[2].split('=')[1])
            if is_column:
                _rotate_column(screen, idx, by)
            else:
                _rotate_row(screen, idx, by)


def solve(fname, w, h, rect_top_left):
    top_left_x, top_left_y = rect_top_left
    screen = _init_screen(w=w, h=h)
    instructions = open(fname).readlines()
    _follow_instructions(instructions, screen, top_left_x, top_left_y)
    total_pixels_on = sum(sum(c == '#' for c in row) for row in screen)
    return total_pixels_on, screen


def _print_screen(screen):
    for row in screen:
        for i in range(0, len(row), 5):
            print(''.join((c if c == '#' else ' ') for c in row[i:i + 5]), end='  ')
        print()


if __name__ == '__main__':
    test_sol = solve('test_data.txt', w=7, h=3, rect_top_left=(0, 0))
    assert test_sol[0] == 6
    assert test_sol[1] == [
        ['.', '#', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '.'],
    ]

    sol = solve('input.txt', w=50, h=6, rect_top_left=(0, 0))
    print('Solution to part 1 =', sol[0])

    print('For part 2 solution, see below:')
    _print_screen(sol[1])
