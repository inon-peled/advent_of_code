from hashlib import md5


def _enc(salt, idx):
    s = f'{salt}{idx}'
    m = s
    for i in range(2017):
        m = md5(m.encode()).hexdigest().lower()
    return m


def _check_rep_in_first_element(buffer):
    b = buffer[0]
    found_rep = None

    for i in range(len(b) - 2):
        if b[i] == b[i + 1] == b[i + 2]:
            found_rep = b[i]
            break

    return found_rep


def _check_next_b(buffer, rep):
    for k in range(1, len(buffer)):
        b = buffer[k]
        for i in range(len(b) - 4):
            if rep == b[i] == b[i + 1] == b[i + 2] == b[i + 3] == b[i + 4]:
                return True
    return False


def _check_key(buffer):
    rep = _check_rep_in_first_element(buffer)

    if rep is not None:
        next_b_exists = _check_next_b(buffer, rep)
        return next_b_exists

    return False


def solve(salt):
    buffer = [_enc(salt, j) for j in range(1001)]
    keys = []
    idx = 0

    while len(keys) < 64:
        if _check_key(buffer):
            keys.append(idx)

        idx += 1
        buffer = buffer[1:]
        new_b = _enc(salt, idx + 1000)
        buffer.append(new_b)

    answer = keys[-1]
    return answer


if __name__ == '__main__':
    print('Part 2 solution:', solve('cuanljph'))
