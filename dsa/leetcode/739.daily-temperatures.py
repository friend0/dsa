#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) and stack[-1][1] < temp:
                j, tempj = stack.pop()
                results[j] = i - j
            stack.append((i, temp))
        return results


# @lc code=end
