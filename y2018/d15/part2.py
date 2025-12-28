"""
Fixed the solution using Claude: https://claude.ai/share/827f86f9-00d1-4672-91c4-e1bc0eac836e
"""
from collections import deque

_PRINT_BOARD = False


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
        (x, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x, y + 1)
    ]


def _bfs_distances(board, units, start):
    """BFS to find distances from start to all reachable squares"""
    distances = {start: 0}
    q = deque([start])

    while q:
        x, y = q.popleft()
        for nx, ny in _neighbors(x, y):
            if (nx, ny) in distances:
                continue
            if board.get((nx, ny)) != '.':
                continue
            if (nx, ny) in units:
                continue
            distances[(nx, ny)] = distances[(x, y)] + 1
            q.append((nx, ny))

    return distances


def _find_move_target(board, units, loc):
    """Find the best square to move toward (or None if no valid targets)"""
    my_type = units[loc][0]
    enemy_type = 'E' if my_type == 'G' else 'G'

    # Find all enemies
    enemies = [pos for pos, (utype, hp) in units.items() if utype == enemy_type]
    if not enemies:
        return None

    # Find all squares in range of enemies (empty squares adjacent to enemies)
    in_range = []
    for ex, ey in enemies:
        for nx, ny in _neighbors(ex, ey):
            if board.get((nx, ny)) == '.' and (nx, ny) not in units:
                in_range.append((nx, ny))

    if not in_range:
        return None

    # BFS from current location
    distances = _bfs_distances(board, units, loc)

    # Find reachable targets with their distances
    reachable = []
    for target in in_range:
        if target in distances:
            reachable.append((distances[target], target[1], target[0], target))

    if not reachable:
        return None

    # Choose nearest target (by distance, then reading order)
    reachable.sort()
    chosen_target = reachable[0][3]

    # Now find which first step to take toward chosen_target
    # BFS from chosen_target back to find all paths
    if chosen_target == loc:
        return loc  # Already there

    # BFS from target backwards to find best first step
    reverse_dist = _bfs_distances(board, units, chosen_target)

    # Check all neighbors of start position
    possible_first_steps = []
    for nx, ny in _neighbors(loc[0], loc[1]):
        if (nx, ny) in reverse_dist:
            possible_first_steps.append((reverse_dist[(nx, ny)], ny, nx, (nx, ny)))

    if not possible_first_steps:
        return None

    possible_first_steps.sort()
    return possible_first_steps[0][3]


def _find_attack_target(units, loc):
    """Find adjacent enemy to attack (lowest HP, then reading order)"""
    my_type = units[loc][0]
    enemy_type = 'E' if my_type == 'G' else 'G'

    x, y = loc
    targets = []
    for nx, ny in _neighbors(x, y):
        if (nx, ny) in units:
            utype, hp = units[(nx, ny)]
            if utype == enemy_type:
                targets.append((hp, ny, nx, (nx, ny)))

    if not targets:
        return None

    targets.sort()
    return targets[0][3]


def _attack(target_loc, units, attack_power):
    curr_hp = units[target_loc][1]
    new_hp = curr_hp - attack_power
    if new_hp <= 0:
        units.pop(target_loc)
    else:
        units[target_loc] = (units[target_loc][0], new_hp)


def _move(loc, next_loc, units):
    u = units.pop(loc)
    units[next_loc] = u


def _one_turn(board, units, elf_attack_power):
    unit_locs = sorted(units.keys(), key=lambda p: (p[1], p[0]))

    for loc in unit_locs:
        if loc not in units:  # Unit was killed earlier this turn
            continue

        # Check if combat should end (no targets at start of this unit's turn)
        my_type = units[loc][0]
        enemy_type = 'E' if my_type == 'G' else 'G'
        if not any(u[0] == enemy_type for u in units.values()):
            return False  # Round incomplete

        attack_power = 3 if units[loc][0] == 'G' else elf_attack_power

        # Try to attack
        target = _find_attack_target(units, loc)
        if target:
            _attack(target, units, attack_power)
            continue

        # Try to move
        move_target = _find_move_target(board, units, loc)
        if move_target and move_target != loc:
            _move(loc, move_target, units)
            loc = move_target

        # Try to attack after moving
        target = _find_attack_target(units, loc)
        if target:
            _attack(target, units, attack_power)

    return True  # Round completed


def _is_last_turn(units):
    unit_types = {u[0] for u in units.values()}
    return len(unit_types) <= 1


def _print_board(turn, board, units):
    if not _PRINT_BOARD:
        return
    print(f'\n==== After {turn} turns ====')
    h = max(b[1] for b in board)
    w = max(b[0] for b in board)
    for i in range(h + 1):
        print()
        for j in range(w + 1):
            u = units.get((j, i))
            if u is None:
                print(board[j, i], end='')
            else:
                print(u[0], end='')
    print()


def _simulate(board, units, elf_attack_power):
    turn = 0
    _print_board(turn, board, units)

    while True:
        if _is_last_turn(units):
            return turn
        completed = _one_turn(board, units, elf_attack_power)
        if not completed:
            return turn  # Don't increment turn for incomplete round
        turn += 1
        _print_board(turn, board, units)


def _num_elves(units):
    return sum(u[0] == 'E' for u in units.values())


def main(fname):
    elf_attack_power = 0
    while True:
        elf_attack_power += 1
        board, units = _parse(fname)
        initial_num_elves = _num_elves(units)
        total_turns = _simulate(board, units, elf_attack_power)
        num_elves_left = _num_elves(units)
        if num_elves_left != initial_num_elves:
            continue
        remaining_hp = sum(u[1] for u in units.values())
        answer = total_turns * remaining_hp
        return answer


if __name__ == '__main__':
    assert 1140 == main('test1.txt')
    assert 6474 == main('test2.txt')
    assert 3478 == main('test3.txt')
    assert 31284 == main('test4.txt')
    print('\nPart 2 answer:', main('input.txt'))
