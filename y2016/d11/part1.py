from copy import deepcopy
from heapq import heappop, heappush

TEST_DATA = {
    1: {'hm', 'lm'},
    2: {'hg'},
    3: {'lg'},
    4: set()
}

DATA = {
    1: {'pg', 'pm'},
    2: {'ag', 'bg', 'cg', 'dg'},
    3: {'am', 'bm', 'cm', 'dm'},
    4: set()
}


def _is_valid_floor(flr):
    if len(flr) <= 1:
        return True

    chips = {item[0] for item in flr if item[1] == 'm'}
    gens = {item[0] for item in flr if item[1] == 'g'}

    for chip in chips:
        if gens and (chip not in gens):
            return False

    return True


def _do_move(d, e, f, item1, item2):
    items = {item1, item2} - {None}
    new_d = deepcopy(d)
    new_d[e] -= items
    new_d[f] |= items
    new_e = f
    return new_e, new_d


def _is_valid_data(d):
    for i, flr in d.items():
        if not _is_valid_floor(flr):
            return False

    return True


def _valid_neighbors(state):
    d = state['d']
    e = state['e']

    adj_floors = {
        1: (2,),
        2: (1, 3),
        3: (2, 4),
        4: (1,)
    }[e]
    valid = set()

    for f in adj_floors:
        for item1 in d[e]:
            other_items = (d[e] | {None}) - {item1}
            for item2 in other_items:
                new_e, new_d = _do_move(d=d, e=e, f=f, item1=item1, item2=item2)
                if _is_valid_data(d=new_d):
                    valid.add(_state_to_key({'e': new_e, 'd': new_d}))

    return valid


def _make_goal(start_d):
    goal_data = {k: set() for k in start_d}
    max_floor = max(start_d.keys())
    for floor in start_d.values():
        goal_data[max_floor] |= floor
    goal_state = {'e': max_floor, 'd': goal_data}
    return goal_state


def _state_to_key(state):
    key = (
        state['e'],
        tuple((k, tuple(sorted(v))) for k, v in state['d'].items())
    )
    return key

def _key_to_state(key):
    state = {
        'e': key[0],
        'd': {k: set(v) for (k, v) in key[1]}
    }
    return state


def dijkstra(data):
    i = 0
    start = {'e': 1, 'd': data}
    start_key = _state_to_key(start)

    goal = _make_goal(start['d'])

    pq = [(0, start_key)]
    dist = {start_key: 0}
    prev = {}

    while pq:
        i += 1
        if i % 10000 == 0:
            print(f'{i} Dijkstra iterations so far...')
        d, u = heappop(pq)
        u_state = _key_to_state(u)
        if u_state == goal:
            return d
        if d > dist[u]:
            continue
        neighbors = _valid_neighbors(u_state)
        for v_key in neighbors:
            nd = d + 1
            if nd < dist.get(v_key, float("inf")):
                dist[v_key] = nd
                prev[v_key] = u
                heappush(pq, (nd, v_key))

    return None

if __name__ == '__main__':
    assert 11 == dijkstra(TEST_DATA)
    print('Assert succeeded\n')
    print('\nPart 1 answer is:', dijkstra(DATA))
