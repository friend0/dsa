#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            data = [0] * 26
            for c in s:
                data[ord(c) - ord('a')] += 1

            res[tuple(data)].append(s)
        return res.values()


# @lc code=end
