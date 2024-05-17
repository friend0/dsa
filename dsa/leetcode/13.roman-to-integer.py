#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:

    def romanToInt(self, s: str) -> int:
        result = 0
        if not len(s):
            return result

        base = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        base_val = base[s[-1]]
        for char in s[::-1]:
            cur_base_val = base[char]
            if cur_base_val >= base_val:
                result += base[char]
                base_val = cur_base_val
            else:
                result -= base_val
        return result


# @lc code=end
