#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
from operator import index


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if not len(needle):
            return -1
        if not len(haystack):
            return -1

        window = len(needle) - 1
        index, first, last = 0, 0, len(needle) - 1

        while index + window < len(haystack):
            first, last = 0, window
            if needle[first] == haystack[
                    index + first] and needle[last] == haystack[index + last]:
                while first <= last:
                    if needle[first] == haystack[
                            first + index] and needle[last] == haystack[last +
                                                                        index]:
                        first += 1
                        last -= 1
                        if first > last:
                            return index
                    else:
                        break
            index += 1
        return -1


# @lc code=end
