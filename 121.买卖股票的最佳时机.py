#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv = 0
        for i in range(1, len(prices)):
            x = prices[i] - min(prices[:i])
            if x>maxv:
                maxv = x
        return maxv

# @lc code=end

