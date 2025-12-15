with open('./data.txt') as f_in:
    data1 = [
        [int(e) for e in line.strip().split()]
        for line in f_in
    ]

num_valid1 = sum(
    ((d[0] < d[1] + d[2]) and (d[1] < d[0] + d[2]) and (d[2] < d[0] + d[1]))
    for d in data1
)
print(num_valid1)

num_valid2 = 0
for j in range(3):
    for i in range(0, len(data1), 3):
        d = [data1[i][j], data1[i + 1][j], data1[i + 2][j]]
        num_valid2 += ((d[0] < d[1] + d[2]) and (d[1] < d[0] + d[2]) and (d[2] < d[0] + d[1]))

print(num_valid2)

