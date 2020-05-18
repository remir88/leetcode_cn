#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    __times = 0

    def __init__(self):
        self.__times = 0
        
    def traverse(self, root: TreeNode, cur: int):
        if cur-root.val==0:
            self.__times += 1
        if root.left:
            self.traverse(root.left, cur-root.val)
        if root.right:
            self.traverse(root.right, cur-root.val)
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.traverse(root, sum)        
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)           
        return self.__times
        
# @lc code=end

