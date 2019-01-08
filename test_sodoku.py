from sodoku import (N, Sodoku, solve)
from example_boards import (board001, board002, board003, board004,
                            board005, board006,
                            min_clues_board, ai_escargot_board,
                            ai_SE_board)
from unittest import TestCase


def verify_solves(sodoku, init_board):
    for i in range(N):
        for j in range(N):
            s = sodoku.board[i][j]
            b = init_board[i][j]
            if b is not None and b != s:
                return False
    return True


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
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve001(self):
        board = board001
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve002(self):
        board = board002
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve003(self):
        board = board003
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve004(self):
        board = board004
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve005(self):
        board = board005
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve006(self):
        board = board006
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve_min_clues(self):
        board = min_clues_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve_ai_escargot(self):
        board = ai_escargot_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return

    def test_solve_ai_se(self):
        board = ai_SE_board
        s = solve(Sodoku(board))
        self.assertTrue(s.is_solved())
        self.assertTrue(verify_solves(s, board))
        return
