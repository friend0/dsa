#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    tokens = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if not len(tokens):
            return 0

        for token in tokens:
            # if the token is a digit, pop it onto the stack
            if token in self.tokens:
                op1, op2 = int(stack.pop()), int(stack.pop())
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op2 - op1)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(int(op2 / op1))
            else:
                stack.append(int(token))
        return stack[-1]


# # @lc code=end
