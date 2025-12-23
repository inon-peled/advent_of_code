"""
Solution idea: Dijkstra's algorithm on the graph of possible moves,
with a neighbors function that relies on the implementation of part 1.
"""
from heapq import heappop, heappush

TEST_DEPTH = 510
TEST_TARGET = 10, 10

DEPTH = 8103
TARGET = 9, 758

ROCKY = 0
WET = 1
NARROW = 2

GEAR = 'G'
TORCH = 'T'
NEITHER = 'O'

POSSIBLE_TOOLS = {
    ROCKY: {GEAR, TORCH},
    WET: {GEAR, NEITHER},
    NARROW: {TORCH, NEITHER}
}


class Solver:
    def __init__(self, depth, target_x, target_y):
        self.depth = depth
        self.target_x = target_x
        self.target_y = target_y
        self.memo = {}

    def _geologic_edge(self, x, y):
        if x == y == 0:
            return 0

        if x == self.target_x and y == self.target_y:
            return 0

        if y == 0:
            return x * 16807

        if x == 0:
            return y * 48271

        raise ValueError(f'Not an edge case: {x=} {y=}')

    def _erosion(self, x, y):
        memo_key = x, y
        if memo_key in self.memo:
            return self.memo[memo_key]

        if 0 in (x, y) or (x, y) == (self.target_x, self.target_y):
            g = self._geologic_edge(x, y)
        else:
            a = self._erosion(x - 1, y)
            b = self._erosion(x, y - 1)
            g = a * b

        e = (g + self.depth) % 20183
        self.memo[memo_key] = e
        return e

    @staticmethod
    def _print_region(risk):
        if risk == 0:
            symbol = '.'
        elif risk == 1:
            symbol = '='
        else:
            symbol = '|'
        print(symbol, end='')

    def _region_type(self, x, y):
        e = self._erosion(x, y)
        reg_type = e % 3
        return reg_type

    def _neighbors(self, state):
        x, y, current_tool = state
        current_region_type = self._region_type(x, y)
        currently_possible_tools = POSSIBLE_TOOLS[current_region_type]

        n = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]
        n_possible = [xy for xy in n if min(xy) >= 0]

        moves = []
        for neigh in n_possible:
            neigh_reg_type = self._region_type(neigh[0], neigh[1])
            next_tools = POSSIBLE_TOOLS[neigh_reg_type]
            possible_next_tools = next_tools.intersection(currently_possible_tools)
            for t in possible_next_tools:
                edge_cost = 1 if t == current_tool else 8
                moves.append((neigh[0], neigh[1], t, edge_cost))

        return moves

    def _is_goal(self, state):
        x, y, tool = state
        reached = (x == self.target_x and y == self.target_y and tool == TORCH)
        return reached

    @staticmethod
    def _dijkstra(start, func_is_goal, func_neighbors):
        pq = [(0, start)]
        settled = set()

        while pq:
            d, u = heappop(pq)

            if u not in settled:
                settled.add(u)

                if func_is_goal(u):
                    return d

                moves = func_neighbors(u)
                for m in moves:
                    v = m[:-1]
                    w = m[-1]
                    if v not in settled:
                        heappush(pq, (d + w, v))

        return None

    def solve(self):
        start = (0, 0, TORCH)
        answer = self._dijkstra(start, self._is_goal, self._neighbors)
        return answer


if __name__ == '__main__':
    assert 45 == Solver(depth=TEST_DEPTH, target_x=TEST_TARGET[0], target_y=TEST_TARGET[1]).solve()
    print(Solver(depth=DEPTH, target_x=TARGET[0], target_y=TARGET[1]).solve())
