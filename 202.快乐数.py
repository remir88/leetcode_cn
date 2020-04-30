#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def val(self, n:int) -> int:
        ret = 0
        while n > 0:
            ret += (n%10)**2
            n //= 10
        return ret

    def isHappy(self, n: int) -> bool:
        dict = {}
        while n not in dict:
            dict[n] = True
            n = self.val(n)
            if n==1:
                return True
        return False

        
# @lc code=end

