from hashlib import md5

def solve(door_id, psswd_len):
    i = 0
    psswd = [None] * psswd_len
    while None in psswd:
        hash_str = md5(f'{door_id}{i}'.encode()).hexdigest()
        if hash_str.startswith('00000'):
            pos = int(hash_str[5], 16)
            if 0 <= pos < len(psswd) and psswd[pos] is None:
                psswd[pos] = hash_str[6]
        i += 1
    psswd_str = ''.join(psswd)
    return psswd_str


if __name__ == '__main__':
    assert '05ace8e3' == solve('abc', 8)
    print(solve('ffykfhsq', 8))
