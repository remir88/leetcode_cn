#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        for x in range(0, zeros):
            nums.remove(0)
        for x in range(0, zeros):
            nums.append(0)
# @lc code=end

