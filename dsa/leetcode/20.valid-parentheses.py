#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    lefts = set(['(', '{', '['])
    rights = set([')', '}', ']'])

    def isValid(self, s: str) -> bool:
        left_stack, right_stack = [], []
        for char in s:
            if char in s:
                if char in self.lefts:
                    left_stack.append(char)
                elif char in self.rights:
                    if not len(left_stack):
                        return False
                    l = left_stack.pop()
                    if char == ')' and l != '(':
                        return False
                    elif char == '}' and l != '{':
                        return False
                    elif char == ']' and l != '[':
                        return False
        if len(right_stack) or len(left_stack):
            return False
        return True


# @lc code=end
