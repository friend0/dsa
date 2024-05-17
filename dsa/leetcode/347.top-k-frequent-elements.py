#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for _ in nums]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, count in counts.items():
            frequencies[count - 1].append(num)

        results = []
        for f in frequencies[::-1]:
            for num in f:
                results.append(num)
                if len(results) == k:
                    return results

        return results


# @lc code=end
