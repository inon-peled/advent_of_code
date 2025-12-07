def solve(filename):
    mat = open(filename).readlines()
    beams = [mat[0].find('S')]
    num_splits = 0

    for i in range(1, len(mat)):
        new_beams = []
        for j in beams:
            if mat[i][j] == '^':
                new_beams.extend([j - 1, j + 1])
                num_splits += 1
            else:
                new_beams.append(j)
        beams = sorted(set(new_beams))

    return num_splits


assert 21 == solve('test.txt')
print(solve('data.txt'))
