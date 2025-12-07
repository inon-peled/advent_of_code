TARGET_AUNT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def read_and_parse(fname):
    aunts = dict()
    with open(fname) as f:
        for line in f.readlines():
            first_colon_idx = line.find(':')
            p1 = line[:first_colon_idx]
            num = int(p1[3:])
            aunts[num] = dict()

            p2 = line[first_colon_idx + 1:].split(',')
            for kv in p2:
                k, v = kv.split(':')
                aunts[num][k.strip()] = int(v)

    return aunts


def solve(aunts, target):
    s_target = set(target.items())

    for aunt_num in aunts:
        s_a = set(aunts[aunt_num].items())
        is_sub = s_a.issubset(s_target)
        if is_sub:
            return aunt_num

    return None


if __name__ == '__main__':
    print(solve(read_and_parse('./data.txt'), TARGET_AUNT))
