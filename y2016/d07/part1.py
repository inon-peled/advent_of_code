def _split(line):
    in_sq_p = False
    pieces_inside_sq_p = []
    pieces_outside_sq_p = []
    curr_piece = ''

    for c in line:
        if c == '[':
            in_sq_p = True
            if curr_piece:
                pieces_outside_sq_p.append(curr_piece)
                curr_piece = ''
        elif c == ']':
            in_sq_p = False
            if curr_piece:
                pieces_inside_sq_p.append(curr_piece)
                curr_piece = ''
        else:
            curr_piece += c

    if not in_sq_p:
        pieces_outside_sq_p.append(curr_piece)
    else:
        pieces_inside_sq_p.append(curr_piece)

    return {
        'outside': pieces_outside_sq_p,
        'inside': pieces_inside_sq_p
    }


def _check_one_piece(p):
    if len(p) < 4:
        return False
    for i in range(len(p) - 3):
        cond1 = (p[i] == p[i + 3])
        cond2 = (p[i + 1] == p[i + 2])
        cond3 = (p[i] != p[i + 1])
        all_conds = (cond1 and cond2 and cond3)
        if all_conds:
            return True
    return False


def _is_tls(pieces):
    good_outside = False
    for p in pieces['outside']:
        if _check_one_piece(p):
            good_outside = True

    good_inside = True
    for p in pieces['inside']:
        if _check_one_piece(p):
            good_inside = False

    good = good_outside and good_inside
    return good


def _process_one_line(line):
    pieces = _split(line)
    is_tls = _is_tls(pieces)
    return is_tls


def solve(fname):
    total_tls = 0
    with open(fname) as f:
        for line in f:
            total_tls += _process_one_line(line)
    return total_tls


if __name__ == '__main__':
    assert 1 == _process_one_line('abba[mnop]qrst')
    assert 0 == _process_one_line('abcd[bddb]xyyx')
    assert 0 == _process_one_line('aaaa[qwer]tyui')
    assert 1 == _process_one_line('ioxxoj[asdfgh]zxcvbn')
    print(solve('input.txt'))
