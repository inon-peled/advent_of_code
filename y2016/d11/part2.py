'''
Originally, I used the same code as for part 1, but it was too slow with 7 items.
Claude improved this as follows, using a better state representation, in which generator-chip pairs are interchangeable
if they occupy different floors.
'''

from heapq import heappop, heappush

TEST_DATA = {
    1: {'hm', 'lm'},
    2: {'hg'},
    3: {'lg'},
    4: set()
}

DATA_1 = {
    1: {'pg', 'pm'},
    2: {'ag', 'bg', 'cg', 'dg'},
    3: {'am', 'bm', 'cm', 'dm'},
    4: set()
}

DATA_2 = {
    1: {'pg', 'pm', 'xg', 'xm', 'yg', 'ym'},
    2: {'ag', 'bg', 'cg', 'dg'},
    3: {'am', 'bm', 'cm', 'dm'},
    4: set()
}


def _data_to_pairs(data):
    """Convert floor-based data to pair representation: [(gen_floor, chip_floor), ...]"""
    elements = set()
    for floor, items in data.items():
        for item in items:
            elements.add(item[0])

    pairs = []
    for elem in elements:
        gen_floor = None
        chip_floor = None
        for floor, items in data.items():
            if elem + 'g' in items:
                gen_floor = floor
            if elem + 'm' in items:
                chip_floor = floor
        pairs.append((gen_floor, chip_floor))

    return tuple(sorted(pairs))


def _is_valid_floor_pairs(pairs, floor):
    """Check if a specific floor is valid given the pair configuration"""
    gens_on_floor = sum(1 for g, c in pairs if g == floor)
    chips_on_floor = []

    for g, c in pairs:
        if c == floor:
            # This chip is on the floor
            if g == floor:
                # Protected by its own generator
                continue
            else:
                # Not protected - needs to be checked
                chips_on_floor.append(True)

    # If there are unprotected chips and any generators, it's invalid
    if chips_on_floor and gens_on_floor > 0:
        return False

    return True


def _is_valid_state(elevator, pairs):
    """Check if the entire state is valid"""
    for floor in range(1, 5):
        if not _is_valid_floor_pairs(pairs, floor):
            return False
    return True


def _get_items_on_floor(pairs, floor):
    """Get list of items on a floor: [(pair_idx, 'g'/'m'), ...]"""
    items = []
    for i, (g, c) in enumerate(pairs):
        if g == floor:
            items.append((i, 'g'))
        if c == floor:
            items.append((i, 'm'))
    return items


def _apply_move(elevator, pairs, target_floor, items_to_move):
    """Apply a move and return new state"""
    new_pairs = list(pairs)
    for pair_idx, item_type in items_to_move:
        g, c = new_pairs[pair_idx]
        if item_type == 'g':
            new_pairs[pair_idx] = (target_floor, c)
        else:
            new_pairs[pair_idx] = (g, target_floor)
    return target_floor, tuple(sorted(new_pairs))


def _get_neighbors(elevator, pairs):
    """Get all valid neighboring states with move pruning"""
    neighbors = []
    items = _get_items_on_floor(pairs, elevator)

    # Determine which directions to try
    directions = []
    if elevator < 4:
        directions.append(elevator + 1)
    if elevator > 1:
        directions.append(elevator - 1)

    for target_floor in directions:
        going_up = target_floor > elevator

        # Try moving 2 items
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                new_elev, new_pairs = _apply_move(elevator, pairs, target_floor, [items[i], items[j]])
                if _is_valid_state(new_elev, new_pairs):
                    neighbors.append((new_elev, new_pairs))

        # Try moving 1 item
        for item in items:
            new_elev, new_pairs = _apply_move(elevator, pairs, target_floor, [item])
            if _is_valid_state(new_elev, new_pairs):
                neighbors.append((new_elev, new_pairs))

    return neighbors


def _heuristic(elevator, pairs):
    """A* heuristic: sum of distances from floor 4"""
    score = 0
    for g, c in pairs:
        score += (4 - g) + (4 - c)
    return score


def solve(data):
    """Dijkstra search with pair-based state representation"""
    start_pairs = _data_to_pairs(data)
    start_elevator = 1
    start_state = (start_elevator, start_pairs)

    num_pairs = len(start_pairs)
    goal_pairs = tuple([(4, 4)] * num_pairs)
    goal_state = (4, goal_pairs)

    pq = [(0, start_state)]
    dist = {start_state: 0}

    i = 0
    while pq:
        i += 1
        if i % 10000 == 0:
            print(f'After {i} iterations, queue size: {len(pq)}, visited: {len(dist)}')

        d, state = heappop(pq)
        elevator, pairs = state

        if state == goal_state:
            return d

        if d > dist.get(state, float('inf')):
            continue

        for new_state in _get_neighbors(elevator, pairs):
            new_d = d + 1
            if new_d < dist.get(new_state, float('inf')):
                dist[new_state] = new_d
                heappush(pq, (new_d, new_state))

    return None


if __name__ == '__main__':
    result = solve(TEST_DATA)
    print(f'Test: {result}')
    assert result == 11
    print('Assert succeeded\n')

    print('Part 1 answer is:', solve(DATA_1))
    print('Part 2 answer is:', solve(DATA_2))
