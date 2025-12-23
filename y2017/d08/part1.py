from collections import defaultdict


class Solver:
    def __init__(self):
        self.regs = defaultdict(int)

    def _check_cond(self, cond):
        cond = cond.split()
        lhs = self.regs[cond[0]]
        expression = f'{lhs} {cond[1]} {cond[2]}'
        res = eval(expression)
        return res

    def _do(self, op):
        op = op.split()
        if op[1] == 'inc':
            self.regs[op[0]] += int(op[-1])
        else:
            self.regs[op[0]] -= int(op[-1])

    def solve(self, fname):
        with open(fname) as f:
            for line in f:
                op, cond = line.strip().split(' if ')
                if self._check_cond(cond):
                    self._do(op)

        answer = max(self.regs.values())
        return answer


if __name__ == '__main__':
    assert 1 == Solver().solve('./test_data.txt')
    print(Solver().solve('./input.txt'))