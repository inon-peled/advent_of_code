LEFT = 'L'
RIGHT = 'R'
STRAIGHT = 'S'


def _parse(fname):
    board = []
    with open(fname) as f:
        for line in f:
            board.append([c for c in line])

    longest = len(max(board, key=len))
    for i in range(len(board)):
        r = board[i]
        r_padded = r + ([' '] * (longest - len(r)))
        board[i] = r_padded

    assert all(len(r) == longest for r in board)
    return board


def _hide_cart(board, i, j):
    c = board[i][j]
    if c in '<>':
        board[i][j] = '-'
    elif c in 'v^':
        board[i][j] = '|'
    else:
        raise ValueError('No cart found.')


def _init_carts_and_clean_board(board):
    carts = []

    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell = board[i][j]
            if cell in '^<>v':
                carts.append([i, j, board[i][j], LEFT])

    for cart in carts:
        i, j = cart[:2]
        _hide_cart(board, i, j)

    return carts


def _find_collision(sorted_carts):
    for i in range(len(sorted_carts) - 1):
        t1 = sorted_carts[i]
        t2 = sorted_carts[i + 1]
        if (t1[0] == t2[0]) and (t1[1] == t2[1]):
            return t1[:2]
    return None


def _move(cart):
    direction = cart[2]
    if direction == '^':
        cart[0] -= 1
    elif direction == 'v':
        cart[0] += 1
    elif direction == '<':
        cart[1] -= 1
    else:
        cart[1] += 1


def _rotate_on_corner(corner, cart):
    NEXT_SHAPE = {
        '/': {
            'v': '<',
            '^': '>',
            '>': '^',
            '<': 'v'
        },
        '\\': {
            'v': '>',
            '^': '<',
            '>': 'v',
            '<': '^'
        }
    }
    cart[2] = NEXT_SHAPE[corner][cart[2]]


def _rotate_on_junction(cart):
    NEXT_SHAPE = {
        'v': {
            LEFT: '>',
            RIGHT: '<',
            STRAIGHT: 'v'
        },
        '^': {
            LEFT: '<',
            RIGHT: '>',
            STRAIGHT: '^'
        },
        '<': {
            LEFT: 'v',
            RIGHT: '^',
            STRAIGHT: '<'
        },
        '>': {
            LEFT: '^',
            RIGHT: 'v',
            STRAIGHT: '>'
        }
    }
    cart[2] = NEXT_SHAPE[cart[2]][cart[3]]

    NEXT_DIRECTION = {
        RIGHT: LEFT,
        LEFT: STRAIGHT,
        STRAIGHT: RIGHT
    }
    cart[3] = NEXT_DIRECTION[cart[3]]


def _print_state(board, carts):
    b = [r[:] for r in board]
    for cart in carts:
        cell = b[cart[0]][cart[1]]
        b[cart[0]][cart[1]] = cart[2] if cell not in '^<>vx' else 'x'
    print()
    for row in b:
        print(''.join(row))


def _advance_carts(board, carts):
    for cart_idx, cart in enumerate(carts):
        cell = board[cart[0]][cart[1]]

        if cell in ['-', '|']:
            pass
        elif cell in ['/', '\\']:
            _rotate_on_corner(cell, cart)
        elif cell == '+':
            _rotate_on_junction(cart)
        else:
            raise ValueError(f'Unknown cell type "{cell}" for {cart_idx=}')

        _move(cart)
        pass
    # _print_state(board, carts)


def solve(board):
    carts = _init_carts_and_clean_board(board)
    while True:
        carts.sort()
        x = _find_collision(carts)
        if x is not None:
            collision_coordinates = (x[1], x[0])
            return collision_coordinates
        _advance_carts(board, carts)


def main(fname):
    board = _parse(fname)
    answer = solve(board)
    return answer


if __name__ == '__main__':
    assert (7, 3) == main('./test.txt')
    print(main('./input.txt'))
