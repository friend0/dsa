#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        results = [1] * nums_len
        p = 1
        for i, num in enumerate(nums):
            results[i] = p
            p *= num
        p = 1
        for i in reversed(range(nums_len)):
            results[i] *= p
            p *= nums[i]
        return results


# @lc code=end
