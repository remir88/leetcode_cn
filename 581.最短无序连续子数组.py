#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums==sorted(nums):
            return 0
        while nums[-1]==max(nums):
            nums.pop(-1)
        while nums[0]==min(nums):
            nums.pop(0)
        return len(nums)
# @lc code=end

