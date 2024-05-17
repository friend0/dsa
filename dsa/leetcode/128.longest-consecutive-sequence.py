#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        nmap = {num: True for num in nums}

        longest_sequence = 0
        for num in nums:
            # check left neighbor

            if nmap.get(num - 1) is None:
                # sequence
                slength = 0
                while nmap.get(num + slength):
                    slength += 1
                longest_sequence = max(longest_sequence, slength)
        return longest_sequence


# @lc code=end
