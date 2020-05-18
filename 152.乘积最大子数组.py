#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax = []
        fmin = []
        fmax.append(nums[0])
        fmin.append(nums[0])
        for i in range(1, len(nums)):
            fmax.append(max(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i]))
            fmin.append(min(fmin[i-1]*nums[i], fmax[i-1]*nums[i], nums[i]))
        return max(fmax)

# @lc code=end

