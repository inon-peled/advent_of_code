"""
Solved via ChatGPT, ref. https://chatgpt.com/share/69300f4c-d43c-800e-9e74-82c3c300b1e6
"""


def _parse_ranges(text: str):
    text = text.replace("\n", "").strip()
    parts = text.split(",")
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        a, b = p.split("-")
        out.append((int(a), int(b)))
    return out


def _merge_ranges(ranges):
    if not ranges:
        return []
    ranges.sort()
    merged = [list(ranges[0])]
    for s, e in ranges[1:]:
        ms, me = merged[-1]
        if s <= me + 1:
            merged[-1][1] = max(me, e)
        else:
            merged.append([s, e])
    return [(s, e) for s, e in merged]


def _generate_repeated_numbers(global_min, global_max):
    """
    Generate all numbers N such that:
        N = concat(A repeated m times), m >= 2
    and global_min <= N <= global_max.
    Yields numbers in ascending order, deduplicated.
    """
    results = []

    max_len = len(str(global_max))

    for total_len in range(2, max_len + 1):  # length of N
        for m in range(2, total_len + 1):  # number of repeats
            if total_len % m != 0:
                continue
            k = total_len // m  # block length

            start = 10 ** (k - 1)
            end = 10 ** k - 1

            for A in range(start, end + 1):
                s = str(A) * m
                N = int(s)

                if N > global_max:
                    break
                if N >= global_min:
                    results.append(N)

    return sorted(set(results))


def _sum_invalid_ids(ranges):
    ranges = _merge_ranges(ranges)
    global_min = ranges[0][0]
    global_max = ranges[-1][1]

    rep_nums = _generate_repeated_numbers(global_min, global_max)

    total = 0
    r_index = 0
    r_len = len(ranges)

    for n in rep_nums:
        # Skip ranges until one could contain n
        while r_index < r_len and ranges[r_index][1] < n:
            r_index += 1
        if r_index == r_len:
            break
        if ranges[r_index][0] <= n <= ranges[r_index][1]:
            total += n

    return total


def main():
    with open("data_c2.txt", "r") as f:
        content = f.read()

    ranges = _parse_ranges(content)
    result = _sum_invalid_ids(ranges)
    print(result)


if __name__ == "__main__":
    main()
