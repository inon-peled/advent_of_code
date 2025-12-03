def count_zero_clicks(lines):
    pos = 50      # starting position
    zeros = 0     # total clicks that land on 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        # Count how many clicks during this rotation land on 0
        if direction == 'R':
            # First i ≥ 1 such that (pos + i) % 100 == 0
            r = (100 - pos) % 100
            if r == 0:
                r = 100
        elif direction == 'L':
            # First i ≥ 1 such that (pos - i) % 100 == 0
            r = pos % 100
            if r == 0:
                r = 100
        else:
            raise ValueError(f"Invalid direction in line: {line}")

        if r <= distance:
            zeros += 1 + (distance - r) // 100

        # Update final position after full rotation
        if direction == 'R':
            pos = (pos + distance) % 100
        else:  # 'L'
            pos = (pos - distance) % 100

    return zeros


def main():
    with open("data_c1.txt", "r") as f:
        lines = f.readlines()

    print(count_zero_clicks(lines))


if __name__ == "__main__":
    main()
