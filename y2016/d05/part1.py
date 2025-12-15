from hashlib import md5

def solve(door_id, psswd_len):
    i = 0
    psswd = ''
    while len(psswd) < psswd_len:
        hash_str = md5(f'{door_id}{i}'.encode()).hexdigest()
        if hash_str.startswith('00000'):
            psswd += hash_str[5]
        i += 1
    return psswd


if __name__ == '__main__':
    assert '18f47a30' == solve('abc', 8)
    print(solve('ffykfhsq', 8))
