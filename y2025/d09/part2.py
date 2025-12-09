"""
Solution from ChatGPT: https://chatgpt.com/share/69386d5d-9a10-800e-a96f-33259617c839
"""
from collections import deque

def read_points():
    pts = []
    with open("./data.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = line.split(",")
                pts.append((int(x), int(y)))
    return pts

def build_compressed_coords(points):
    xs_raw = set()
    ys_raw = set()
    for x, y in points:
        xs_raw.add(x)
        xs_raw.add(x + 1)
        ys_raw.add(y)
        ys_raw.add(y + 1)
    xs_raw = sorted(xs_raw)
    ys_raw = sorted(ys_raw)
    xs = [xs_raw[0] - 1] + xs_raw + [xs_raw[-1] + 1]
    ys = [ys_raw[0] - 1] + ys_raw + [ys_raw[-1] + 1]
    x2i = {x: i for i, x in enumerate(xs)}
    y2i = {y: i for i, y in enumerate(ys)}
    return xs, ys, x2i, y2i

def build_walls(points, xs, ys, x2i, y2i):
    nx = len(xs) - 1
    ny = len(ys) - 1
    h_wall = [[False] * nx for _ in range(ny + 1)]
    v_wall = [[False] * (nx + 1) for _ in range(ny)]
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        if x1 == x2:
            xi = x2i[x1]
            y0, y1_ = sorted((y1, y2))
            j0 = y2i[y0]
            j1 = y2i[y1_]
            for j in range(j0, j1):
                v_wall[j][xi] = True
        else:
            yi = y2i[y1]
            x0, x1_ = sorted((x1, x2))
            i0 = x2i[x0]
            i1 = x2i[x1_]
            for k in range(i0, i1):
                h_wall[yi][k] = True
    return h_wall, v_wall

def flood_fill_outside(xs, ys, h_wall, v_wall):
    nx = len(xs) - 1
    ny = len(ys) - 1
    outside = [[False] * nx for _ in range(ny)]
    dq = deque()
    for j in range(ny):
        for i in range(nx):
            if j == 0 or j == ny - 1 or i == 0 or i == nx - 1:
                outside[j][i] = True
                dq.append((j, i))
    while dq:
        j, i = dq.popleft()
        if j > 0 and not outside[j - 1][i] and not h_wall[j][i]:
            outside[j - 1][i] = True
            dq.append((j - 1, i))
        if j < ny - 1 and not outside[j + 1][i] and not h_wall[j + 1][i]:
            outside[j + 1][i] = True
            dq.append((j + 1, i))
        if i > 0 and not outside[j][i - 1] and not v_wall[j][i]:
            outside[j][i - 1] = True
            dq.append((j, i - 1))
        if i < nx - 1 and not outside[j][i + 1] and not v_wall[j][i + 1]:
            outside[j][i + 1] = True
            dq.append((j, i + 1))
    return outside

def build_prefix(xs, ys, outside):
    nx = len(xs) - 1
    ny = len(ys) - 1
    A = [[0] * nx for _ in range(ny)]
    for j in range(ny):
        h = ys[j + 1] - ys[j]
        for i in range(nx):
            if outside[j][i]:
                w = xs[i + 1] - xs[i]
                A[j][i] = w * h
    PS = [[0] * (nx + 1) for _ in range(ny + 1)]
    for j in range(ny):
        s = 0
        for i in range(nx):
            s += A[j][i]
            PS[j + 1][i + 1] = PS[j][i + 1] + s
    return PS

def rect_outside(PS, j0, j1, i0, i1):
    return PS[j1][i1] - PS[j0][i1] - PS[j1][i0] + PS[j0][i0]

def solve(points):
    xs, ys, x2i, y2i = build_compressed_coords(points)
    h_wall, v_wall = build_walls(points, xs, ys, x2i, y2i)
    outside = flood_fill_outside(xs, ys, h_wall, v_wall)
    PS = build_prefix(xs, ys, outside)
    best = 0
    n = len(points)
    for a in range(n):
        x1, y1 = points[a]
        for b in range(a + 1, n):
            x2, y2 = points[b]
            if x1 == x2 or y1 == y2:
                continue
            x0, x1_ = sorted((x1, x2))
            y0, y1_ = sorted((y1, y2))
            area = (x1_ - x0 + 1) * (y1_ - y0 + 1)
            i0 = x2i[x0]
            i1 = x2i[x1_ + 1]
            j0 = y2i[y0]
            j1 = y2i[y1_ + 1]
            if rect_outside(PS, j0, j1, i0, i1) == 0:
                if area > best:
                    best = area
    return best

def main():
    pts = read_points()
    print(solve(pts))

if __name__ == "__main__":
    main()
