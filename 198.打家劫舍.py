#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        s = [0] * len(nums)
        s[0] = nums[0]
        s[1] = max(nums[0], nums[1])
        for x in range(2, len(nums)):
            s[x] = max(s[x-1], nums[x]+s[x-2])
        return s[len(nums)-1]
        # @lc code=end

