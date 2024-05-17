#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0]
        if len(nums) == 2:
            return [0, 1]

        memo = {target - num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if (j := memo.get(num)) is not None:
                if i != j:
                    return [i, j]
        return []


# @lc code=end
