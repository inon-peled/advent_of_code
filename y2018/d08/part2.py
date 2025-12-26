def _parse(fname):
    with open(fname) as f:
        line = f.read()
        nums = [int(e) for e in line.strip().split()]
        return nums


def solve(nums, start):
    total = 0
    num_children = nums[start]
    num_metadata = nums[start + 1]
    start += 2

    if num_children == 0:
        end = start + num_metadata
        for j in range(start, end):
            total += nums[j]
        return total, end

    child_values = [None]
    for k in range(num_children):
        t, e = solve(nums, start)
        child_values.append(t)
        start = e

    end = start + num_metadata
    for j in range(start, end):
        m = nums[j]
        if m < len(child_values):
            t = child_values[m]
            total += t

    return total, end


def main(fname):
    nums = _parse(fname)
    total, _ = solve(nums, 0)
    return total


if __name__ == '__main__':
    assert 66 == main('./test.txt')
    print(main('./input.txt'))
