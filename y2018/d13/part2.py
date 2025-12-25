"""
Again, solved by simulation, then had a bug that Claude removed (same conversation link as in part1.py).
The bug was that I handled at most one collision every turn, whereas some turns had multiple collisions.
"""
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
    collided = set()  # Track indices of carts that have collided

    for cart_idx, cart in enumerate(carts):
        if cart_idx in collided:  # Skip carts that already collided
            continue

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

        # Check for collision immediately after this cart moves
        for other_idx, other_cart in enumerate(carts):
            if cart_idx != other_idx and other_idx not in collided:
                if cart[0] == other_cart[0] and cart[1] == other_cart[1]:
                    collided.add(cart_idx)
                    collided.add(other_idx)
                    break

    return collided


def solve(board):
    carts = _init_carts_and_clean_board(board)
    while True:
        carts.sort()
        collided = _advance_carts(board, carts)

        # Remove collided carts (in reverse order to maintain indices)
        for idx in sorted(collided, reverse=True):
            carts.pop(idx)

        if len(carts) == 1:
            c = carts[0]
            return c[1], c[0]


def main(fname):
    board = _parse(fname)
    answer = solve(board)
    return answer


if __name__ == '__main__':
    print(main('./input.txt'))
