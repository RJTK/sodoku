board001 = [[None, None, 4, 8, None, 7, None, None, None],
            [None, 3, 2, 5, None, 4, None, 6, 7],
            [5, None, None, None, None, 3, None, None, None],
            [None, 5, None, None, 4, None, None, None, None],
            [4, None, 9, None, None, None, 5, None, 2],
            [None, None, None, None, 5, None, None, 4, None],
            [None, None, None, 9, None, None, None, None, 5],
            [2, 6, None, 4, None, 5, 7, 3, None],
            [None, None, None, 6, None, 1, 2, None, None]]

board002 = [[2, None, None, None, None, None, None, None, None],
            [None, None, None, 7, None, None, 3, None, 4],
            [None, 3, None, 1, None, 5, None, 2, None],
            [None, None, 8, None, 3, 4, None, None, 9],
            [None, 9, None, None, None, None, None, 6, None],
            [6, None, None, 8, 9, None, 1, None, None],
            [None, 5, None, 4, None, 1, None, 8, None],
            [3, None, 6, None, None, 9, None, None, None],
            [None, None, None, None, None, None, None, None, 7]]

board003 = [[9, None, 5, None, None, 3, None, 2, None],
            [2, None, None, None, 7, None, None, None, None],
            [None, None, None, 2, None, None, 5, 7, None],
            [None, None, 9, None, None, 5, None, None, None],
            [None, 6, 8, None, None, None, 7, 4, None],
            [None, None, None, 6, None, None, 3, None, None],
            [None, 9, 6, None, None, 4, None, None, None],
            [None, None, None, None, 1, None, None, None, 6],
            [None, 4, None, 3, None, None, 8, None, 1]]

board004 = [[3, None, None, None, 7, 5, None, None, None],
            [1, None, None, None, 9, None, None, 3, 7],
            [2, None, None, 4, None, None, None, None, None],
            [6, None, None, None, None, 4, None, 5, None],
            [None, None, 4, None, 2, 1, None, None, 3],
            [None, 7, None, None, 6, None, None, None, None],
            [None, None, None, None, None, None, None, None, 4],
            [None, None, 6, 2, None, None, None, 7, 9],
            [4, 8, None, None, None, None, 3, None, 6]]

board005 = [[None, None, None, None, None, None, 8, 7, None],
            [7, 8, None, 9, 4, None, None, None, None],
            [None, None, None, None, 5, None, None, 2, None],
            [None, None, None, 3, None, None, None, None, None],
            [None, 5, 6, None, None, None, None, None, None],
            [8, None, 9, None, None, 2, None, 1, None],
            [None, None, None, None, 9, None, None, 8, None],
            [None, None, None, None, None, None, 4, None, 7],
            [None, None, 1, 7, None, 6, None, None, None]]

board006 = [[None, None, None, None, None, None, None, 9, 6],
            [None, 7, 5, None, 3, None, None, None, None],
            [9, None, 2, None, None, None, None, None, None],
            [None, None, None, None, None, 8, 3, 7, None],
            [None, None, 3, None, 4, None, None, 5, None],
            [None, None, 6, None, None, 1, None, None, None],
            [None, None, 4, 2, 8, None, None, 1, None],
            [None, None, None, None, None, 4, None, None, 2],
            [None, 1, None, 5, None, None, 9, None, None]]

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

# Claimed by http://aisudoku.com/index_en.html to be the hardest puzzle
# in existence.
ai_escargot_board = [[1, None, None, None, None, 7, None, 9, None],
                     [None, 3, None, None, 2, None, None, None, 8],
                     [None, None, 9, 6, None, None, 5, None, None],
                     [None, None, 5, 3, None, None, 9, None, None],
                     [None, 1, None, None, 8, None, None, None, 2],
                     [6, None, None, None, None, 4, None, None, None],
                     [3, None, None, None, None, None, None, 1, None],
                     [None, 4, 1, None, None, None, None, None, 7],
                     [None, None, 7, None, None, None, 3, None, None]]

# Found on stack exchange https://puzzling.stackexchange.com/questions/252
# Due to same guy as ai_escargot
ai_SE_board = [[8, None, None, None, None, None, None, None, None],
               [None, None, 3, 6, None, None, None, None, None],
               [None, 7, None, None, 9, None, 2, None, None],
               [None, 5, None, None, None, 7, None, None, None],
               [None, None, None, None, 4, 5, 7, None, None],
               [None, None, None, 1, None, None, None, 3, None],
               [None, None, 1, None, None, None, None, 6, 8],
               [None, None, 8, 5, None, None, None, 1, None],
               [None, 9, None, None, None, None, 4, None, None]]
