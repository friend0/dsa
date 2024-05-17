#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = 0, 0
        m_seen = [[0] * 9 for _ in range(len(board))]
        n_seen = [[0] * 9 for _ in range(len(board))]
        sub_seen = [[0] * 9 for _ in range(len(board))]

        for m in range(len(board)):
            for n in range(len(board)):
                elem = board[m][n]
                if elem != '.':
                    sub_index = 3 * (m // 3) + (n // 3)
                    m_seen[m][int(elem) - 1] += 1
                    n_seen[n][int(elem) - 1] += 1
                    sub_seen[sub_index][int(elem) - 1] += 1

                    if m_seen[m][int(elem) - 1] > 1:
                        return False
                    elif n_seen[n][int(elem) - 1] > 1:
                        return False
                    elif sub_seen[sub_index][int(elem) - 1] > 1:
                        return False
        return True


# @lc code=end
