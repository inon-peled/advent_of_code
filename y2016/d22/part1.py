def _to_num(s):
    return int(s[:-1])


def _parse(fname):
    files = dict()
    for i, line in enumerate(open(fname)):
        if i < 2:
            continue
        path, size, used, avail, use_percent = line.split()
        files[path] = {
            'size': _to_num(size),
            'used': _to_num(used),
            'avail': _to_num(avail),
            'use_percent': _to_num(use_percent)
        }
    return files


def _viable_pairs(files):
    total = 0
    for f1 in files:
        for f2 in files:
            if f1 != f2 and files[f2]['avail'] >= files[f1]['used'] > 0:
                total += 1
    return total


def main(fname):
    files = _parse('./input.txt')
    total = _viable_pairs(files)
    return total


if __name__ == '__main__':
    print(main('./input.txt'))
