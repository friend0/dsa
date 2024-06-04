#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(n_open, n_closed):
            if n_open == n_closed == n:
                return res.append("".join(stack))
            if n > n_open:
                stack.append('(')
                backtrack(n_open + 1, n_closed)
                stack.pop()
            if n_open > n_closed:
                stack.append(')')
                backtrack(n_open, n_closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# @lc code=end
