#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#


# @lc code=start
class Solution:

    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[List[int]]:
        if not len(nums):
            return [[lower, upper]]
        last = nums[0]
        results = []
        if last > lower:
            results.append([lower, last - 1])
        for num in nums[1:]:
            if abs(num - last) != 1:
                results.append([last + 1, num - 1])
            last = num
        if last < upper:
            results.append([last + 1, upper])
        return results


# @lc code=end
