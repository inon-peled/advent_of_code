'''
Solution idea:
Generate the squared frames, one at a time, using the same guidelines as described in the docstring of part 1 solution.
While generating a frame, its values are dictated only bt the previous frame.
'''

def solve(inp):
    if inp <= 0:
        return 1

    f_start = 1
    f_end = 1
    base = 1
    frame_idx = 0
    frame = list(range(f_start, f_end + 1))

    while True:
        f_start = f_end + 1
        base += 2
        f_end = base ** 2
        frame_idx += 1
        edge_len = frame_idx * 2


        next_frame = []

if __name__ == '__main__':
    assert 0 == solve(1)
    assert 3 == solve(12)
    assert 2 == solve(23)
    assert 4 == solve(33)
    assert 6 == solve(71)
    assert 8 == solve(73)
    assert 31 == solve(1024)
    print(f'Part 1 answer:', solve(277678))
