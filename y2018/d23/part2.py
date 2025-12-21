"""
Solution from ChatGPT (https://chatgpt.com/share/69480904-2ffc-800e-82b9-8dae3ae0d879):

Each bot covers a region in space defined by an L1 (Manhattan) ball, not a cube.
The goal is to find a single point that lies inside the maximum number of such
regions, and among those points minimize Manhattan distance to the origin.

Instead of intersecting bot regions (which is incorrect, since pairwise
intersection does not imply a common intersection), we search space itself.

Algorithm:

1. Maintain a priority queue of axis-aligned boxes, ordered by:
   (a) number of bots that can reach the box (more is better),
   (b) minimum possible distance from the box to the origin (smaller is better),
   (c) box size (smaller is better),
   (d) a numeric tiebreaker.

2. Initialize the queue with one large box that contains all points that could be in range of any bot.

3. Repeatedly:

   * Remove the highest-priority box from the queue.
   * If the box represents a single point, return its distance to the origin.
   * Otherwise, split the box by halving each coordinate range
     (up to 8 sub-boxes) and insert each sub-box that is reachable
     by at least one bot back into the queue.

This process always refines the most promising region first and
guarantees the first single point reached is optimal.

"""
import heapq


def _parse(fname):
    bots = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            pos, r = line.split(', ')
            pos = pos.split('<')[1].split('>')[0]
            pos = tuple(int(e) for e in pos.split(','))
            r = int(r.split('=')[1])
            bots.append((pos, r))
    return bots


def _initialize(bots):
    xs = [p[0] for p, _ in bots]
    ys = [p[1] for p, _ in bots]
    zs = [p[2] for p, _ in bots]
    rs = [r for _, r in bots]

    minx = min(x - r for x, r in zip(xs, rs))
    maxx = max(x + r for x, r in zip(xs, rs))
    miny = min(y - r for y, r in zip(ys, rs))
    maxy = max(y + r for y, r in zip(ys, rs))
    minz = min(z - r for z, r in zip(zs, rs))
    maxz = max(z + r for z, r in zip(zs, rs))

    span = max(maxx - minx, maxy - miny, maxz - minz) + 1
    size = 1
    while size < span:
        size <<= 1

    root = {'mn': [minx, miny, minz], 'mx': [minx + size - 1, miny + size - 1, minz + size - 1]}
    return root


def _dist_point_to_rc(point, rc):
    # minimal L1 distance from point to any point in axis-aligned box rc
    d = 0
    for dim in range(3):
        v = point[dim]
        lo = rc['mn'][dim]
        hi = rc['mx'][dim]
        if v < lo:
            d += lo - v
        elif v > hi:
            d += v - hi
    return d


def _count_bots_intersect_rc(bots, rc):
    c = 0
    for (pos, r) in bots:
        if _dist_point_to_rc(pos, rc) <= r:
            c += 1
    return c


def _dist_origin_to_rc(rc):
    # minimal L1 distance from origin to any point in box
    d = 0
    for dim in range(3):
        lo = rc['mn'][dim]
        hi = rc['mx'][dim]
        if hi < 0:
            d += -hi
        elif lo > 0:
            d += lo
    return d


def _rc_size(rc):
    return max(rc['mx'][d] - rc['mn'][d] for d in range(3)) + 1  # edge length


def _split_rc(rc):
    mn = rc['mn']
    mx = rc['mx']
    mid = [(mn[d] + mx[d]) // 2 for d in range(3)]

    ranges = []
    for d in range(3):
        ranges.append([(mn[d], mid[d]), (mid[d] + 1, mx[d])])

    out = []
    for x0, x1 in ranges[0]:
        if x0 > x1:
            continue
        for y0, y1 in ranges[1]:
            if y0 > y1:
                continue
            for z0, z1 in ranges[2]:
                if z0 > z1:
                    continue
                out.append({'mn': [x0, y0, z0], 'mx': [x1, y1, z1]})
    return out


def solve(bots):
    root = _initialize(bots)

    heap = []
    counter = 0

    c0 = _count_bots_intersect_rc(bots, root)
    heapq.heappush(heap, (-c0, _dist_origin_to_rc(root), _rc_size(root), counter, root))

    while heap:
        negc, dist0, sz, _, rc = heapq.heappop(heap)
        if sz == 1:
            return dist0  # single point => exact answer

        for child in _split_rc(rc):
            c = _count_bots_intersect_rc(bots, child)
            if c == 0:
                continue
            counter += 1
            heapq.heappush(heap, (-c, _dist_origin_to_rc(child), _rc_size(child), counter, child))

    raise RuntimeError("No solution found")


def main(fname):
    bots = _parse(fname)
    return solve(bots)


if __name__ == '__main__':
    assert 36 == main('./test2.txt')
    print(main('./input.txt'))
