from collections import deque
from heapq import heappush, heappop


def _parse(fname):
    lines = open(fname).readlines()
    board = {}
    units = {}
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line):
            loc = j, i
            if char in ['#', '.']:
                board[loc] = char
            elif char in ['G', 'E']:
                units[loc] = (char, 200)
                board[loc] = '.'
            else:
                raise ValueError(f'Unknown character {char}')
    return board, units


def _neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]


def _all_reachable_enemies(board, units, start, enemy_type):
    reachable_enemies = []
    distances = {}
    q = deque([(0, (None, None), start)])

    while q:
        d, f, (x, y) = q.popleft()
        if (x, y) not in distances:
            distances[(x, y)] = (d, f)
            for neigh_x, neigh_y in _neighbors(x, y):
                board_neigh = board[neigh_x, neigh_y]
                if board_neigh == '#':
                    continue
                elif (neigh_x, neigh_y) in units:
                    neigh_type, neigh_hp = units[(neigh_x, neigh_y)]
                    if neigh_type != enemy_type:
                        continue
                    else:
                        enemy = (neigh_hp, neigh_x, neigh_y, x, y, 1 + d)
                        heappush(reachable_enemies, enemy)
                else:
                    q_item = (1 + d, (x, y), (neigh_x, neigh_y))
                    q.append(q_item)

    return reachable_enemies, distances


def _find_nearest_reachable_enemy(board, units, loc):
    enemy_type = 'G' if units[loc][0] == 'E' else 'E'
    reachable_enemies, distances = _all_reachable_enemies(board, units, loc, enemy_type)

    if not reachable_enemies:
        return None, None

    nearest_hp, nearest_x, nearest_y, nearest_f_x, nearest_f_y, nearest_dist = heappop(reachable_enemies)
    father = nearest_f_x, nearest_f_y
    node = nearest_x, nearest_y
    while father != loc:
        node = father
        father = distances[father][1]

    return nearest_dist, node


def _attack(next_loc, units):
    curr_hp = units[next_loc][1]
    new_hp = curr_hp - 3
    if new_hp <= 0:
        units.pop(next_loc)
    else:
        units[next_loc] = (units[next_loc][0], new_hp)


def _move(loc, next_loc, units):
    u = units.pop(loc)
    units[next_loc] = u


def _one_turn(board, units):
    unit_locs = sorted(units, key=lambda p: p[1])
    for loc in unit_locs:
        nearest_dist, next_loc = _find_nearest_reachable_enemy(board, units, loc)
        if nearest_dist is not None:
            if nearest_dist == 1:
                _attack(next_loc, units)
            else:
                _move(loc, next_loc, units)


def _is_last_turn(units):
    unit_types = {u[0] for u in units.values()}
    return len(unit_types) <= 1


def _print_board(turn, board, units):
    print(f'\n==== After {turn} turns ====')
    h = max(b[0] for b in board)
    w = max(b[1] for b in board)
    for i in range(h + 1):
        print()
        for j in range(w + 1):
            u = units.get((j, i))
            if u is None:
                print(board[j, i], end='')
            else:
                print(u[0], end='')
    print()


def _simulate(board, units):
    turn = 0
    _print_board(turn, board, units)

    while True:
        if _is_last_turn(units):
            return turn
        _one_turn(board, units)
        turn += 1
        _print_board(turn, board, units)


def main(fname):
    board, units = _parse(fname)
    total_turns = _simulate(board, units)
    return total_turns


if __name__ == '__main__':
    assert 47 == main('test1.txt')
    # print(main('input.txt'))
