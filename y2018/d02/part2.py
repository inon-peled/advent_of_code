def _diff(s1, s2):
    return sum(s1[i] != s2[i] for i in range(len(s1)))


def main(fname):
    strings = []
    with open(fname) as f:
        for line in f:
            strings.append(line.strip())

    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            s1 = strings[i]
            s2 = strings[j]
            if _diff(s1, s2) == 1:
                common = ''.join(s1[i] for i in range(len(s1)) if s1[i] == s2[i])
                return common


if __name__ == '__main__':
    print(main('./input.txt'))
