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


def _collect_all_aba(pieces):
    abas = {'inside': set(), 'outside': set()}
    for which in abas:
        pcs = pieces[which]
        for p in pcs:
            for i in range(len(p) - 2):
                if p[i] == p[i + 2] and p[i] != p[i + 1]:
                    abas[which].add(p[i:i + 3])
    return abas


def _invert(set_of_abas):
    return {p[1] + p[0] + p[1] for p in set_of_abas}


def _is_ssl(abas):
    abas_inverted = {k: _invert(v) for k, v in abas.items()}
    for which in abas_inverted:
        other = 'inside' if which == 'outside' else 'outside'
        if abas[which].intersection(abas_inverted[other]):
            return True
    return False


def _process_one_line(line):
    pieces = _split(line)
    abas = _collect_all_aba(pieces)
    is_ssl = _is_ssl(abas)
    return is_ssl


def solve(fname):
    total_tls = 0
    with open(fname) as f:
        for line in f:
            total_tls += _process_one_line(line)
    return total_tls


if __name__ == '__main__':
    assert 1 == _process_one_line('aba[bab]xyz')
    assert 0 == _process_one_line('xyx[xyx]xyx')
    assert 1 == _process_one_line('aaa[kek]eke')
    assert 1 == _process_one_line('zazbz[bzb]cdb')
    print(solve('input.txt'))
