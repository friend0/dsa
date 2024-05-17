#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            while j > i and nums[j] == val:
                j -= 1
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

            i += 1
        return j + 1


# @lc code=end
