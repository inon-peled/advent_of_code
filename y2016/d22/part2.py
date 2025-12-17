'''
Solution was close but wrong, then I corrected it via ChatGPT.
ChatGPT noticed that the empty spot cannot be moved directly up, because there are walls
(cells marked as '#' in the problem text).
'''

from collections import deque


def _to_num(s: str) -> int:
    return int(s[:-1])


def _parse(fname: str):
    files = {}
    for i, line in enumerate(open(fname, "r", encoding="utf-8")):
        if i < 2:
            continue
        path, size, used, avail, use_percent = line.split()
        x, y = (
            int(e)
            for e in path[len("/dev/grid/node-"):]
        .replace("x", "")
        .replace("y", "")
        .split("-")
        )
        files[(x, y)] = {
            "size": _to_num(size),
            "used": _to_num(used),
            "avail": _to_num(avail),
            "use_percent": _to_num(use_percent),
        }
    return files


def _bfs_empty_to_target(files, start, target, walls):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        (x, y), d = q.popleft()
        if (x, y) == target:
            return d
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            np = (nx, ny)
            if np not in files:
                continue
            if np in walls:
                continue
            if np in seen:
                continue
            seen.add(np)
            q.append((np, d + 1))
    raise ValueError(f"target {target} unreachable from {start}")


def solve(files):
    max_x = max(x for x, _ in files)
    # find empty
    empties = [p for p, v in files.items() if v["used"] == 0]
    assert len(empties) == 1
    empty = empties[0]
    empty_size = files[empty]["size"]  # since used==0, avail==size

    # walls: nodes whose data can never be moved into the empty
    walls = {p for p, v in files.items() if v["used"] > empty_size}

    # move empty next to goal (left of it)
    target_empty = (max_x - 1, 0)
    dist = _bfs_empty_to_target(files, empty, target_empty, walls)

    # then: 1 swap to move goal left once, then 5 steps per further left shift
    return dist + 1 + 5 * (max_x - 1)


def main(fname):
    files = _parse(fname)
    return solve(files)


if __name__ == "__main__":
    assert 7 == main("./test_data.txt")
    print(main("./input.txt"))
