#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * n
        f[0] = 1
        if (n >= 2): #be careful of the boundary
            f[1] = 2 
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        return f[n-1]

# @lc code=end

