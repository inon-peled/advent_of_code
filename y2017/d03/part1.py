'''
Solution idea:
The board is made of co-centric square frames, as follows:
* Frame 0: 1 -> 1^2 (i.e, just 1)
* Frame 1: 1^2 + 1 -> 3^2
* Frame 2: 3^2 +1 -> 5^2
* Frame 3: 5^2 + 1 -> 7^2
* Etc.
Use this to find the frame that contains the input.

Next, note that for frame f > 0, the corners of the frame are:
* c1 = frame_start + f + 1 (top-right)
* c2 = c1 + f + 1
* c3 = c2 + f + 1
* c4 = c3 + f + 1
Using this, find the edge that contains the input.

Finally, the Manhattan distance is f + dist_mid(input), where dist_mid(input) is
the offset of the input from the middle of the edge.
'''


def solve(inp):
    if inp == 1:
        return 0

    f_start = 1
    f_end = 1
    base = 1
    frame = 0

    while not (f_start <= inp <= f_end):
        f_start = f_end + 1
        base += 2
        f_end = base ** 2
        frame += 1

    edge_len = frame * 2
    c = f_start - 1
    while c < f_end:
        next_c = c + edge_len
        if c <= inp <= next_c:
            mid = c + (edge_len // 2)
            dist_mid = abs(inp - mid)
            answer = frame + dist_mid
            return answer
        else:
            c = next_c


if __name__ == '__main__':
    assert 0 == solve(1)
    assert 3 == solve(12)
    assert 2 == solve(23)
    assert 4 == solve(33)
    assert 6 == solve(71)
    assert 8 == solve(73)
    assert 31 == solve(1024)
    print(f'Part 1 answer:', solve(277678))
