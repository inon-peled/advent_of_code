'''
Solved via ChatGPT, ref. https://chatgpt.com/share/69300f4c-d43c-800e-9e74-82c3c300b1e6
'''


def is_invalid_id(n: int) -> bool:
    s = str(n)
    # Must be an even number of digits
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def parse_ranges(text: str):
    text = text.replace("\n", "").strip()
    parts = text.split(",")
    ranges = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))
    return ranges


def main():
    with open("./data_c2.txt", "r") as f:
        content = f.read()

    ranges = parse_ranges(content)

    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    print(total)


if __name__ == "__main__":
    main()
