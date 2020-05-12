#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

import sys

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0

        m = [sys.maxsize] * len(prices)
        m[0] = prices[0]

        for i in range(1, len(prices)):
            if m[i-1]<prices[i]:
                m[i] = m[i-1]
            else:
                m[i] = prices[i]
        
        ans = 0
        for i in range(1, len(prices)):
            x = prices[i] - m[i-1]
            if x>ans:
                ans = x

        return ans

# @lc code=end

