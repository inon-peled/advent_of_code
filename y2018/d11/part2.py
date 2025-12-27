"""
Solution idea -- use a Summed Area Table (SAT), as suggested by ChatGPT:
https://chatgpt.com/share/695052d1-518c-800e-83cf-d2c679b482ef

Actually, that's a pretty classic scheme in dynamic programming, whereby a matrix is calculated dynamically by
first calculating its top row, then calculating its left-most column, then every cell is calculated from previous cells.
"""

BOARD_W = 300
BOARD_H = 300


class Solver:
    def __init__(self, grid_sn, board_w=BOARD_W, board_h=BOARD_H):
        self.grid_sn = grid_sn
        self.board_w = board_w
        self.board_h = board_h
        self.memo_sq1 = {}

    def _build_sat(self):
        sat = {(1, 1): self._power(1, 1)}

        for x in range(2, self.board_w + 1):
            sat[(x, 1)] = self._power(x, 1) + sat[x - 1, 1]

        for y in range(2, self.board_h + 1):
            sat[(1, y)] = self._power(1, y) + sat[1, y - 1]

        for x in range(2, self.board_w + 1):
            for y in range(2, self.board_h + 1):
                sat[(x, y)] = (
                        self._power(x, y) +
                        sat[x, y - 1] +
                        sat[x - 1, y] -
                        sat[x - 1, y - 1]
                )
        return sat

    def _power(self, x, y):
        if (x, y) not in self.memo_sq1:
            rack_id = x + 10
            p = rack_id * y
            p += self.grid_sn
            p *= rack_id
            p //= 100
            p %= 10
            p -= 5
            self.memo_sq1[(x, y)] = p
        return self.memo_sq1[(x, y)]

    def _square_total_power(self, top_left_x, top_left_y, k, sat):
        bottom_right_x = top_left_x + k - 1
        bottom_right_y = top_left_y + k - 1
        rect1 = sat[bottom_right_x, bottom_right_y]
        rect2 = sat[bottom_right_x, top_left_y - 1] if top_left_y > 1 else 0
        rect3 = sat[top_left_x - 1, bottom_right_y] if top_left_x > 1 else 0
        rect4 = sat[top_left_x - 1, top_left_y - 1] if top_left_x > 1 and top_left_y > 1 else 0
        total = rect1 - rect2 - rect3 + rect4
        return total

    def solve(self):
        sat = self._build_sat()
        best_x_y_k = None
        best_total = None

        for k in range(1, self.board_w + 1):
            for i in range(1, self.board_w + 1 - k):
                for j in range(1, self.board_h + 1 - k):
                    sq_total = self._square_total_power(i, j, k, sat)
                    if best_total is None or sq_total > best_total:
                        best_total = sq_total
                        best_x_y_k = (i, j, k)
        return best_x_y_k


def _test():
    assert Solver(18).solve() == (90, 269, 16)
    assert Solver(42).solve() == (232, 251, 12)


if __name__ == '__main__':
    _test()
    print(Solver(7400).solve())
