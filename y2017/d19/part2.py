def _parse(fname):
    with open(fname) as f:
        mat = [[e for e in l if e not in ('\r', '\n')] for l in f]
    assert all(len(r) == len(mat[0]) for r in mat)

    pad_row = [' '] * (len(mat[0]) + 2)
    padded_mat = [pad_row] + [[' '] + r + [' '] for r in mat] + [pad_row]
    assert all(len(r) == len(padded_mat[0]) for r in padded_mat)
    return padded_mat


def _to_ints(cmplx):
    return int(cmplx.real), int(cmplx.imag)


def _new_direction(mat, direction, i, j):
    d_i, d_j = _to_ints(direction)
    if d_i != 0:
        new_dir = complex(0, 1) if mat[i][j + 1] != ' ' else complex(0, -1)
    else:
        new_dir = complex(1, 0) if mat[i + 1][j] != ' ' else complex(-1, 0)
    return new_dir


def solve(padded_mat):
    start_j = padded_mat[1].index('|')
    pos = complex(1, start_j)
    direction = complex(1, 0)
    letters = ''
    total_moves = 0

    while True:
        i, j = _to_ints(pos)
        m = padded_mat[i][j]
        if m in ('|', '-'):
            pass
        elif m == '+':
            direction = _new_direction(padded_mat, direction, i, j)
        elif m == ' ':
            return total_moves
        else:
            letters += m
        pos += direction
        total_moves += 1


def main(fname):
    mat = _parse(fname)
    letters = solve(mat)
    return letters


if __name__ == '__main__':
    assert 38 == main('./test.txt')
    print(main('./input.txt'))
