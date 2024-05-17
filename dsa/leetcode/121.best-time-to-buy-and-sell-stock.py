#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from xmlrpc.client import MAXINT


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        lowest, profit = prices[0], 0
        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > profit:
                profit = price - lowest
        return profit


# @lc code=end
