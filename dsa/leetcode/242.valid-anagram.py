#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sm = {k: 0 for k in s}
        tm = {k: 0 for k in t}

        if sm.keys() != tm.keys():
            return False

        for char in s:
            sm[char] += 1

        for char in t:
            tm[char] += 1

        if sm.items() != tm.items():
            return False
        return True


# @lc code=end
