#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        isExisit = [False] * (len(nums)+1)
        for i in range(0, len(nums)):
            isExisit[nums[i]] = True
        ans = []
        for j in range(1, len(nums)+1):
            if not isExisit[j]:
                ans.append(j)
        return ans

# @lc code=end

