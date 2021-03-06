from copy import deepcopy
from random import shuffle, choice
from threading import Thread, Timer, Event
from itertools import product

N = 9
M = 3

all_ij = list(product(range(N), range(N)))


class FeasibilityError(Exception):
    pass

# Board will store either None if it is empty,
# an int if the value has been fixed, or a set
# or other iterable indicating feasible values


class Sodoku:
    def __init__(self, board):
        self.original_board = board
        self.board = deepcopy(board)
        assert(len(board) == N)
        for row in board:
            assert(len(row) == N)

        self.feasible = None
        self.reset_feasible()
        return

    def get_blank_feasible(self):
        # return [[None] * N for _ in range(N)]
        return deepcopy(self.original_board)

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
        for i, j in product(range(M), range(M)):
            yield (M * box_row + i, M * box_col + j)
        return

    def find_feasible(self, i, j):
        if self.original_board[i][j] is not None:
            feasible = [self.original_board[i][j]]
        elif self.feasible[i][j] is None:
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
                all([self.is_valid_box(M * i, M * j)
                     for i, j in product(range(M), range(M))]))

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
                if it is not None]

    def is_feasible(self, i, j, v):
        return (self.board[i][j] == v or v in self.find_feasible(i, j))

    def update(self, i, j, v):
        if not self.is_feasible(i, j, v):
            raise ValueError("Value {} is not feasible for ({}, {})"
                             "".format(v, i, j))
        self.board[i][j] = v
        self.reset_feasible((i, j))
        self.fill_determined()
        return

    def fill_determined(self):
        for i, j in [(i, j) for i, j in all_ij
                     if self.board[i][j] is None]:
            if self.board[i][j] is None:
                f = self.find_feasible(i, j)
                if len(f) == 1:
                    self.board[i][j] = next(iter(f))
                    self.reset_feasible((i, j))
                    self.fill_determined()
                    break
        return

    def copy(self):
        assert self.is_valid(), "Bug, invalid state!"
        new = Sodoku(self.board)
        return new

    def is_solved(self):
        return (all(self.board[i][j] is not None
                    for i in range(N) for j in range(N)) and
                self.is_valid() and
                self.check_feasible())

    # ------ Below are iterators for solve methods ----------
    def iter_unfilled(self):
        # Iterate brute force from top-left to bottom-right
        for i, j in all_ij:
            if self.board[i][j] is None:
                yield (i, j)

    def get_feasible_ordered(self):
        # Iterate in order of constrained-ness
        all_feasible = []

        for i, j in all_ij:
            if self.board[i][j] is None:
                f = self.find_feasible(i, j)
                all_feasible.append((len(f), (i, j)))
        return [f[1] for f in sorted(all_feasible)]

    def iter_random_unfilled(self):
        # Iterate in a random order
        choices = [(i, j) for i in range(N) for j in range(N)
                   if self.board[i][j] is None]
        shuffle(choices)
        for ch in choices:
            yield ch
        return

    def iter_weighted_random_unfilled(self):
        # Iterate randomly but with the order weighted to benefit
        # more constrained choices
        choices = []
        for i, j in all_ij:
            if self.board[i][j] is None:
                f = self.find_feasible(i, j)
                k = N - len(f)
                choices.extend([(i, j)] * k)

        shuffle(choices)
        for ch in choices:
            yield ch
        return


def solve_brute_force(sodoku):
    if sodoku.is_solved():
        return sodoku

    for i, j in sodoku.iter_unfilled():
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve_brute_force(new_board)
            if solved is not None:
                return solved
    return None


def solve_bfs_brute_force(sodoku):
    if sodoku.is_solved():
        return sodoku

    queue = [sodoku]
    while queue:
        s = queue.pop(0)

        for i, j in s.iter_unfilled():
            for v in s.find_feasible(i, j):
                new_board = s.copy()
                new_board.update(i, j, v)
                if new_board.check_feasible():
                    queue.append(new_board)

                if new_board.is_solved():
                    return new_board

    raise AssertionError("Unsolved!")


def solve_constraint_ordered(sodoku):
    if sodoku.is_solved():
        return sodoku

    feasible_moves = sodoku.get_feasible_ordered()
    for i, j in feasible_moves:
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve_constraint_ordered(new_board)
            if solved is not None:
                return solved
    return None


def solve_stochastic(sodoku):
    if sodoku.is_solved():
        return sodoku

    for i, j in sodoku.iter_random_unfilled():
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve_stochastic(new_board)
            if solved is not None:
                return solved
    return None


def solve_constraint_weighted_stochastic(sodoku):
    if sodoku.is_solved():
        return sodoku

    for i, j in sodoku.iter_weighted_random_unfilled():
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve_constraint_weighted_stochastic(new_board)
            if solved is not None:
                return solved
    return None


def solve_stochastic_interruptable(sodoku, event):
    if event.is_set():
        return None

    if sodoku.is_solved():
        return sodoku

    for i, j in sodoku.iter_weighted_random_unfilled():
        for v in sodoku.find_feasible(i, j):
            new_board = sodoku.copy()
            new_board.update(i, j, v)
            if not new_board.check_feasible():
                continue

            solved = solve_stochastic_interruptable(new_board, event)
            if solved is not None:
                return solved

            if event.is_set():
                return None

    return None


def solve_random_search(sodoku, event):
    if sodoku.is_solved():
        return sodoku

    breadths = list(range(3, 16, 2))
    max_breadth = choice(breadths)
    n = 1

    queue = []

    def _append_queue(s):
        nonlocal queue
        # This is to avoid exploring the same paths more than once.
        queue.append((s, s.iter_weighted_random_unfilled()))
        # queue.append((s, ((i, j) for (i, j) in s.get_feasible_ordered())))
        return

    _append_queue(sodoku)
    while queue:
        s, iterator = queue.pop(0)
        if event.is_set():
            return None

        for i, j in iterator:
            for v in s.find_feasible(i, j):
                n += 1
                new_board = s.copy()
                new_board.update(i, j, v)
                if new_board.check_feasible():
                    _append_queue(new_board)

                if new_board.is_solved():
                    return new_board

                if n >= max_breadth:
                    break

            if n >= max_breadth:
                n = 1
                _append_queue(s)
                break

    raise AssertionError("Not solvable!")


def solve_random_restart(sodoku, initial_timeout=None):
    solved = None
    event = Event()
    if initial_timeout is None:
        initial_timeout = 0.01

    timeout = initial_timeout

    def _solve():
        nonlocal solved
        event.clear()

        t = Timer(timeout, stop)
        t.start()
        solved = solve_random_search(sodoku, event)
        t.cancel()
        return

    def stop():
        event.set()
        return

    while True:
        solve_thread = Thread(target=_solve)
        solve_thread.start()
        solve_thread.join()
        if solved is not None:
            return solved
        if timeout < 5.0:
            timeout *= 1.1


def solve(sodoku):
    return solve_random_restart(sodoku)
