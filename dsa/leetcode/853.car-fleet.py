#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start
class Solution:

    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        states = zip(position, speed)
        stack = []
        for position, speed in reversed(sorted(states)):
            stack.append((target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


# @lc code=end
