from collections import Counter


def solve(data):
    sum_of_valid_room_numbers = 0
    for line in data:
        line = line.strip()
        line = line.split('[')
        given_checksum = line[1][:-1]
        h = line[0].split('-')
        room_number = int(h[-1])
        letters = ''.join(h[:-1])
        counts = Counter(letters)
        letters_ordered = list(counts.items())
        letters_ordered.sort(key=lambda t: t[0])  # secondary: ascending
        letters_ordered.sort(key=lambda t: t[1], reverse=True)  # primary: descending
        expected_checksum = ''.join(e[0] for e in letters_ordered[:5])
        if (given_checksum == expected_checksum):
            sum_of_valid_room_numbers += room_number

    return sum_of_valid_room_numbers

assert 123 == solve(['aaaaa-bbb-z-y-x-123[abxyz]'])
assert 987 == solve(['a-b-c-d-e-f-g-h-987[abcde]'])
assert 404 == solve(['not-a-real-room-404[oarel]'])
assert 0 == solve(['totally-real-room-200[decoy]'])

data = open('./input.txt').readlines()
print('Solution to part 1:', solve(data))
