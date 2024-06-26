#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            print(i, j, s[i], s[j])
            c1, c2 = s[i].lower(), s[j].lower()
            if c1 != c2:
                return False
            i += 1
            j -= 1
        return True


# @lc code=end
