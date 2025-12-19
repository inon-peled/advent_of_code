TEST = {
    'init': 'a',
    'steps': 6,
    'a': {
        0: [1, 1, 'b'],
        1: [0, -1, 'b']
    },
    'b': {
        0: [1, -1, 'a'],
        1: [1, 1, 'a'],
    }
}

DATA = {
    'init': 'a',
    'steps': 12317297,
    'a': {
        0: [1, 1, 'b'],
        1: [0, -1, 'd'],
    },
    'b': {
        0: [1, 1, 'c'],
        1: [0, 1, 'f'],
    },
    'c': {
        0: [1, -1, 'c'],
        1: [1, -1, 'a'],
    },
    'd': {
        0: [0, -1, 'e'],
        1: [1, 1, 'a'],
    },
    'e': {
        0: [1, -1, 'a'],
        1: [0, 1, 'b'],
    },
    'f': {
        0: [0, 1, 'c'],
        1: [0, 1, 'e'],
    }
}


def simulate(data):
    state = 'a'
    tape = {}
    loc = 0
    n = data['steps']
    for i in range(n):
        symbol = tape.get(loc, 0)
        write, move, next_state = data[state][symbol]
        tape[loc] = write
        loc += move
        state = next_state
    answer = sum(tape.values())
    return answer


if __name__ == '__main__':
    assert 3 == simulate(TEST)
    print(simulate(DATA))
