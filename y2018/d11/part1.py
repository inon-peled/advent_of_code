SQ_W = 3
BOARD_W = 300
BOARD_H = 300


class Solver:
    def __init__(self, grid_sn, sq_w=SQ_W, board_w=BOARD_W, board_h=BOARD_H):
        self.grid_sn = grid_sn
        self.sq_w = sq_w
        self.board_w = board_w
        self.board_h = board_h
        self.memo = {}

    def _power(self, x, y):
        if (x, y) in self.memo:
            return self.memo[(x, y)]

        rack_id = x + 10
        p = rack_id * y
        p += self.grid_sn
        p *= rack_id
        p //= 100
        p %= 10
        p -= 5
        self.memo[(x, y)] = p
        return p

    def _square_total_power(self, top_left_x, top_left_y):
        total = 0
        for x in range(top_left_x, top_left_x + self.sq_w):
            for y in range(top_left_y, top_left_y + self.sq_w):
                total += self._power(x, y)
        return total

    def solve(self):
        best_x_y = None
        best_total = None
        for i in range(1, self.board_w + 1 - self.sq_w):
            for j in range(1, self.board_h + 1 - self.sq_w):
                sq_total = self._square_total_power(i, j)
                if best_total is None or sq_total > best_total:
                    best_total = sq_total
                    best_x_y = (i, j)
        return best_x_y


def _test_power():
    assert 4 == Solver(8)._power(3, 5)
    assert -5 == Solver(57)._power(122, 79)
    assert 0 == Solver(39)._power(217, 196)
    assert 4 == Solver(71)._power(101, 153)


def _test_solve():
    assert Solver(18).solve() == (33, 45)
    assert Solver(42).solve() == (21, 61)


def _test():
    _test_power()
    _test_solve()


if __name__ == '__main__':
    _test()
    print(Solver(7400).solve())
