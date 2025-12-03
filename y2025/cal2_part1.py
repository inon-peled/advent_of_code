'''
Solved via ChatGPT, ref. https://chatgpt.com/share/69300f4c-d43c-800e-9e74-82c3c300b1e6
'''


def parse_ranges(text: str):
    text = text.replace("\n", "").strip()
    parts = text.split(",")
    ranges = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        a, b = part.split("-")
        ranges.append((int(a), int(b)))
    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort()
    merged = [list(ranges[0])]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            # Overlapping or touching; merge
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return [(s, e) for s, e in merged]


def sum_doubled_ids_in_ranges(ranges):
    if not ranges:
        return 0

    # Ranges must be merged & sorted
    ranges = merge_ranges(ranges)

    global_min = ranges[0][0]
    global_max = ranges[-1][1]

    total = 0

    # Precompute powers of 10 up to a safe size
    pow10 = [1]
    while pow10[-1] <= global_max * 10:  # generous upper bound
        pow10.append(pow10[-1] * 10)

    # Helper: check membership by walking ranges once
    range_idx = 0
    num_ranges = len(ranges)

    def add_if_in_range(n, nonlocal_range_idx):
        nonlocal total
        i = nonlocal_range_idx
        # Advance range index while current range ends before n
        while i < num_ranges and ranges[i][1] < n:
            i += 1
        if i >= num_ranges:
            return i  # no more ranges

        # If n is before current range, just keep index
        if n < ranges[i][0]:
            return i

        # Now ranges[i][0] <= n <= ranges[i][1]
        total += n
        return i

    # Generate doubled numbers by length
    # A has k digits; N has 2k digits
    # Stop when the smallest 2k-digit number > global_max
    k = 1
    while True:
        # smallest 2k-digit number is 10^(2k-1)
        if pow10[2 * k - 1] > global_max:
            break

        base_min = pow10[k - 1]  # smallest k-digit
        base_max = pow10[k] - 1  # largest k-digit

        for A in range(base_min, base_max + 1):
            N = A * (pow10[k] + 1)  # A * 10^k + A

            if N < global_min:
                continue
            if N > global_max:
                # As A grows, N grows; we can break this A-loop
                break

            range_idx = add_if_in_range(N, range_idx)
            if range_idx >= num_ranges:
                # No more ranges will contain anything
                break

        k += 1

    return total


def main():
    with open("data_c2.txt", "r") as f:
        content = f.read()

    ranges = parse_ranges(content)
    result = sum_doubled_ids_in_ranges(ranges)
    print(result)


if __name__ == "__main__":
    main()
