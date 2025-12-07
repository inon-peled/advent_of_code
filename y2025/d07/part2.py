"""
Solution idea:
The graph of all particle routes from part 1 is a DAG, rooted at S.
We will calculate for each node the number of routes that lead to it from S.
For this, when calculating layer i, we will assign to every node the sum of numbers from all its fathers in layer i - 1.
The final answer is then the sum of numbers in the bottom-most layer of the DAG.
"""


def solve(filename):
    mat = open(filename).readlines()
    beams = [(mat[0].find('S'), 1)]

    for i in range(1, len(mat)):
        new_beams = []
        for j, r in beams:
            if mat[i][j] == '^':
                new_beams.extend([[j - 1, r], [j + 1, r]])

            else:
                new_beams.append([j, r])

        beams = []
        for b in new_beams:
            if not beams or b[0] != beams[-1][0]:
                beams.append(b)
            else:
                beams[-1][1] += b[1]

    total_worlds = sum(b[1] for b in beams)
    return total_worlds


assert 40 == solve('test.txt')
print()
print(solve('data.txt'))
