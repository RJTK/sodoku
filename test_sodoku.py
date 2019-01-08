from sodoku import (N, M, Sodoku, solve, FeasibilityError)
from unittest import TestCase


class TestSodoku(TestCase):
    easy_board = [[1, None, 7, 8, None, None, 6, None, None],
                  [None, 5, None, None, 1, 3, None, None, 9],
                  [None, 8, None, 6, None, None, 7, None, 5],
                  [3, None, 9, 4, 5, None, None, None, None],
                  [None, 2, None, None, None, None, None, 5, 4],
                  [None, None, 4, None, None, 2, 8, None, 6],
                  [None, 1, 8, None, 9, 7, None, None, None],
                  [None, None, None, 5, None, None, 9, 6, None],
                  [9, None, None, None, 6, None, 2, None, 8]]

    medium_board = [[None, None, 4, 8, None, 7, None, None, None],
                    [None, 3, 2, 5, None, 4, None, 6, 7],
                    [5, None, None, None, None, 3, None, None, None],
                    [None, 5, None, None, 4, None, None, None, None],
                    [4, None, 9, None, None, None, 5, None, 2],
                    [None, None, None, None, 5, None, None, 4, None],
                    [None, None, None, 9, None, None, None, None, 5],
                    [2, 6, None, 4, None, 5, 7, 3, None],
                    [None, None, None, 6, None, 1, 2, None, None]]

    hard_board = [[2, None, None, None, None, None, None, None, None],
                  [None, None, None, 7, None, None, 3, None, 4],
                  [None, 3, None, 1, None, 5, None, 2, None],
                  [None, None, 8, None, 3, 4, None, None, 9],
                  [None, 9, None, None, None, None, None, 6, None],
                  [6, None, None, 8, 9, None, 1, None, None],
                  [None, 5, None, 4, None, 1, None, 8, None],
                  [3, None, 6, None, None, 9, None, None, None],
                  [None, None, None, None, None, None, None, None, 7]]

    extreme_board = [[9, None, 5, None, None, 3, None, 2, None],
                     [2, None, None, None, 7, None, None, None, None],
                     [None, None, None, 2, None, None, 5, 7, None],
                     [None, None, 9, None, None, 5, None, None, None],
                     [None, 6, 8, None, None, None, 7, 4, None],
                     [None, None, None, 6, None, None, 3, None, None],
                     [None, 9, 6, None, None, 4, None, None, None],
                     [None, None, None, None, 1, None, None, None, 6],
                     [None, 4, None, 3, None, None, 8, None, 1]]

    # From wikipedia, apparently this is hard for a brute force algorithm
    # This also contains the minimum possible number of solutions
    min_clues_board = [[None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, 3, None, 8, 5],
                       [None, None, 1, None, 2, None, None, None, None],
                       [None, None, None, 5, None, 7, None, None, None],
                       [None, None, 4, None, None, None, 1, None, None],
                       [None, 9, None, None, None, None, None, None, None],
                       [5, None, None, None, None, None, None, 7, 3],
                       [None, None, 2, None, 1, None, None, None, None],
                       [None, None, None, None, 4, None, None, None, 9]]

    invalid_board = [[1, None, 7, 8, None, None, 6, None, None],
                     [None, 5, None, None, 1, 3, None, None, 9],
                     [None, 8, 8, 6, None, None, 7, None, 5],
                     [3, None, 9, 4, 5, None, None, None, None],
                     [None, 2, None, None, None, None, None, 5, 4],
                     [None, None, 4, None, None, 2, 8, None, 6],
                     [None, 1, 8, None, 9, 7, None, None, None],
                     [None, None, None, 5, None, None, 9, 6, None],
                     [9, None, None, None, 6, None, 2, None, 8]]

    def test000(self):
        board = self.easy_board
        str(Sodoku(board))
        return

    def test_iter_row(self):
        board = self.easy_board
        s = Sodoku(board)
        self.assertTrue({2, 5, 4}, set(s.get_fixed(s.iter_row(4))))
        return

    def test_iter_col(self):
        board = self.easy_board
        s = Sodoku(board)
        self.assertTrue({1, 5, 9, 6}, set(s.get_fixed(s.iter_col(4))))
        return

    def test_iter_box(self):
        board = self.easy_board
        s = Sodoku(board)
        self.assertTrue({4, 5, 2}, set(s.get_fixed(s.iter_box(4, 4))))
        return

    def test_valid_001(self):
        board = self.easy_board
        s = Sodoku(board)
        self.assertTrue(s.is_valid())
        return

    def test_valid_002(self):
        board = self.invalid_board
        s = Sodoku(board)
        self.assertFalse(s.is_valid())
        return

    def test_feasible(self):
        board = self.easy_board
        s = Sodoku(board)
        feasible = set(s.find_feasible(4, 4))
        self.assertEqual(feasible, {3, 7, 8})
        return

    def test_copy(self):
        board = self.easy_board
        s = Sodoku(board)
        s.copy()
        return

    def test_update(self):
        board = self.easy_board
        s = Sodoku(board)
        i, j = s.get_feasible_ordered()[0]
        f = s.find_feasible(i, j)
        s.update(i, j, next(iter(f)))

        self.assertTrue(s.is_valid())
        return

    def test_solve000(self):
        board = self.easy_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        return

    def test_solve001(self):
        board = self.medium_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        return

    def test_solve002(self):
        board = self.hard_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        return

    def test_solve003(self):
        board = self.extreme_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        return

    def test_solve004(self):
        board = self.min_clues_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        return
