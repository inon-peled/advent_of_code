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
    for aunt_num, aunt in aunts.items():
        found = True
        for k, v in aunt.items():
            if k in ['cats', 'trees']:
                if target[k] >= v:
                    found = False
            elif k in ['pomeranians', 'goldfish']:
                if target[k] <= v:
                    found = False
            elif target[k] != v:
                found = False
        if found:
            return aunt_num

    return None


if __name__ == '__main__':
    print(solve(read_and_parse('./data.txt'), TARGET_AUNT))
