INIT_BOARD = '.#./..#/###'


def _tile_size(tile_str):
    return len(tile_str.split('/')[0])


def _parse(fname):
    rules = {2: {}, 3: {}}
    with open(fname) as f:
        for line in f:
            line = line.strip()
            pre, suf = line.split(' => ')
            if _tile_size(pre) == 2:
                rules[2][pre] = suf
            else:
                rules[3][pre] = suf
    return rules


def _encode(mat):
    enc = '/'.join(''.join(row) for row in mat)
    return enc


def _decode(tile):
    tile_mat = []
    for row in tile.split('/'):
        tile_mat.append([e for e in row])
    return tile_mat


def _rot_90(tile):
    tile_mat = _decode(tile)
    h = len(tile_mat)
    w = len(tile_mat[0])
    rot_mat = [
        [tile_mat[h - 1 - i][j] for i in range(h)]
        for j in range(w)
    ]
    rot_enc = _encode(rot_mat)
    return rot_enc


def _rot_180(tile):
    rot = _rot_90(_rot_90(tile))
    return rot


def _rot_270(tile):
    rot = _rot_90(_rot_180(tile))
    return rot


def flip_vrt(tile):
    tile_mat = _decode(tile)
    tile_mat_flip = tile_mat[::-1]
    tile_mat_flip_enc = _encode(tile_mat_flip)
    return tile_mat_flip_enc


def flip_hrz(tile):
    tile_flip = _rot_90(tile)
    tile_flip = flip_vrt(tile_flip)
    tile_flip = _rot_270(tile_flip)
    return tile_flip


def transformations(tile):
    rot = {
        tile,
        _rot_90(tile),
        _rot_180(tile),
        _rot_270(tile)
    }
    flip_h = {flip_hrz(t) for t in rot}
    flip_v = {flip_vrt(t) for t in rot}
    trans = rot | flip_h | flip_v
    return trans


def _convert(tile, rules):
    size = len(tile.split('/')[0])
    trans = transformations(tile)
    for pre, suf in rules[size].items():
        if pre in trans:
            return suf
    return tile


def _extract_tile_mat(board, i, j, tile_size):
    tile_mat = []
    for r in range(tile_size):
        tile_mat.append(board[i + r][j:j + tile_size])
    enc = _encode(tile_mat)
    return enc


def _chunk(board, tile_size):
    tiles = []
    for i in range(0, len(board), tile_size):
        for j in range(0, len(board[0]), tile_size):
            tiles.append(_extract_tile_mat(board, i, j, tile_size))
    return tiles


def _copy(tile, board, i, j):
    tile_mat = _decode(tile)
    tile_size = _tile_size(tile)
    for r in range(tile_size):
        for c in range(tile_size):
            board[i + r][j + c] = tile_mat[r][c]


def _splice(tiles):
    tile_size = _tile_size(tiles[0])
    num_tiles_in_edge = int(len(tiles) ** 0.5)
    size = tile_size * num_tiles_in_edge
    new_board = [[None for _ in range(size)] for _ in range(size)]
    tile_idx = 0
    for i in range(0, size, tile_size):
        for j in range(0, size, tile_size):
            tile = tiles[tile_idx]
            _copy(tile, new_board, i, j)
            tile_idx += 1
    return _encode(new_board)


def _one_iteration(board, rules):
    board_mat = _decode(board)
    size = len(board_mat[0])
    tile_size = 2 if size % 2 == 0 else 3

    tiles = _chunk(board_mat, tile_size)
    tiles_converted = [_convert(t, rules) for t in tiles]

    new_board = _splice(tiles_converted)
    return new_board


def main(fname, initial_board, num_iterations):
    board = initial_board
    rules = _parse(fname)
    for i in range(num_iterations):
        board = _one_iteration(board, rules)
    lights_on = board.count('#')
    return lights_on


if __name__ == '__main__':
    assert 12 == main('./test.txt', INIT_BOARD, 2)
    assert 12 == main('./test.txt', '#..#/..../..../#..#', 1)
    print(main('./input.txt', INIT_BOARD, 5))
