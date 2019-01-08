from copy import deepcopy
from random import shuffle

N = 9
M = 3


class FeasibilityError(Exception):
    pass

# Board will store either None if it is empty,
# an int if the value has been fixed, or a set
# or other iterable indicating feasible values


class Sodoku:
    def __init__(self, board):
        self.board = deepcopy(board)
        assert(len(board) == N)
        for row in board:
            assert(len(row) == N)

        self.feasible = None
        self.reset_feasible()
        return

    def get_blank_feasible(self):
        return [[None] * N for _ in range(N)]

    def reset_feasible(self, i_j=None):
        if i_j is None:
            self.feasible = self.get_blank_feasible()
        else:
            i, j = i_j
            for jx in range(N):
                self.feasible[i][jx] = None
            for ix in range(N):
                self.feasible[ix][j] = None
            for ix, jx in self.iter_box_indices(i, j):
                self.feasible[ix][jx] = None
        return

    def __str__(self):
        thick_row = "||=|=|=||=|=|=||=|=|=||\n"
        s = ""
        for i in range(N):
            if i % M == 0:
                s += thick_row

            for j in range(N):
                if j % M == 0:
                    sep = "||"
                else:
                    sep = "|"

                if self.board[i][j] is None:
                    s += sep + " "
                else:
                    s += sep + str(self.board[i][j])
            s += "||\n"
        s += thick_row
        return s

    def iter_row(self, i):
        for j in range(N):
            yield self.board[i][j]
        return

    def iter_col(self, j):
        for i in range(N):
            yield self.board[i][j]
        return

    def iter_box(self, i, j):
        for (ix, jx) in self.iter_box_indices(i, j):
            yield self.board[ix][jx]
        return

    def iter_box_indices(self, i, j):
        box_row = i // M
        box_col = j // M
        for i in range(M):
            for j in range(M):
                yield (M * box_row + i, M * box_col + j)
        return

    def find_feasible(self, i, j):
        if self.feasible[i][j] is None:
            feasible = set(list(range(1, N + 1)))

            def _filter_feasible(iterable):
                nonlocal feasible
                for v in iterable:
                    if v in feasible and type(v) is int:
                        feasible -= {v}
                return

            _filter_feasible(self.iter_row(i))
            _filter_feasible(self.iter_col(j))
            _filter_feasible(self.iter_box(i, j))
            self.feasible[i][j] = feasible
        else:
            feasible = self.feasible[i][j]
        return feasible

    def is_valid(self):
        return (all([self.is_valid_row(i) for i in range(N)]) and
                all([self.is_valid_col(j) for j in range(N)]) and
                all([self.is_valid_box(M * i, M * j) for i in range(M)
                     for j in range(M)]))

    def check_feasible(self):
        return not any(self.board[i][j] is None and
                       len(self.find_feasible(i, j)) == 0
                       for i in range(N) for j in range(N))

    def is_valid_row(self, i):
        row = list(self.iter_row(i))
        row = self.get_fixed(row)
        return len(row) == len(set(row))

    def is_valid_col(self, j):
        col = list(self.iter_col(j))
        col = self.get_fixed(col)
        return len(col) == len(set(col))

    def is_valid_box(self, i, j):
        box = list(self.iter_box(i, j))
        box = self.get_fixed(box)
        return len(box) == len(set(box))

    def get_fixed(self, iterable):
        return [it for it in iterable
                if type(it) is int]

    def is_feasible(self, i, j, v):
        feasible = self.find_feasible(i, j)
        return v in feasible

    def update(self, i, j, v):
        if not self.is_feasible(i, j, v):
            raise ValueError("Value {} is not feasible for ({}, {})"
                             "".format(v, i, j))
        self.board[i][j] = v
        self.reset_feasible((i, j))
        self.fill_determined()
        return

    def get_feasible_ordered(self):
        all_feasible = []
        for i in range(N):
            for j in range(N):
                if self.board[i][j] is None:
                    f = self.find_feasible(i, j)
                    all_feasible.append((len(f), (i, j)))
        return [f[1] for f in sorted(all_feasible)]

    def iter_unfilled(self):
        for i in range(N):
            for j in range(N):
                if self.board[i][j] is None:
                    yield (i, j)

    def iter_random_unfilled(self):
        choices = [(i, j) for i, j in zip(range(N), range(N))
                   if self.board[i][j] is None]
        shuffle(choices)
        for ch in choices:
            yield ch

    def fill_determined(self):
        recall = False
        for i in range(N):
            for j in range(N):
                if self.board[i][j] is None:
                    f = self.find_feasible(i, j)
                    if len(f) == 1:
                        self.board[i][j] = next(iter(f))
                        self.reset_feasible((i, j))
                        recall = True
                        break
            if recall:
                break
        if recall:
            self.fill_determined()
        return

    def copy(self):
        assert self.is_valid(), "Bug, invalid state!"
        new = Sodoku(self.board)
        return new

    def is_solved(self):
        return (self.is_valid() and
                self.check_feasible() and
                all(type(self.board[i][j]) is int
                    for i, j in zip(range(N), range(N))))


def solve(sodoku):
    if sodoku.is_solved():
        return sodoku

    # for i, j in sodoku.iter_unfilled():

    # feasible_moves = sodoku.get_feasible_ordered()
    # for i, j in feasible_moves:

    for i, j in sodoku.iter_random_unfilled():
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve(new_board)
            if solved is not None:
                return solved
    return None
