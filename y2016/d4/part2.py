from collections import Counter

def _decrypt(line, room_number):
    decrypted = ''
    for char in line:
        if char.isalpha():
            dec_char = ord(char) - ord('a')
            dec_char = (dec_char + room_number) % 26
            dec_char += ord('a')
            dec_char = chr(dec_char)
            decrypted += dec_char
        elif char == '-':
            decrypted += ' '
        else:
            raise ValueError(f'Invalid char {char}')
    return decrypted



def print_all_decrypted(data):
    for original_line in data:
        line = original_line.strip()
        line = line.split('[')

        h = line[0].split('-')
        room_number = int(h[-1])
        letters = ''.join(h[:-1])
        counts = Counter(letters)

        letters_ordered = list(counts.items())
        letters_ordered.sort(key=lambda t: t[0])  # secondary: ascending
        letters_ordered.sort(key=lambda t: t[1], reverse=True)  # primary: descending

        given_checksum = line[1][:-1]
        expected_checksum = ''.join(e[0] for e in letters_ordered[:5])

        if (given_checksum == expected_checksum):
            decrypted = _decrypt('-'.join(h[:-1]), room_number)
            print(decrypted, room_number)


data = open('./input.txt').readlines()
print_all_decrypted(data)
