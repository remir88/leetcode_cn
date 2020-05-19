#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    __max = 0

    def __init__(self):
        self.__max = 0

    def deep(self, root: TreeNode) -> int:
        if not root:
            return -1
        left = self.deep(root.left)+1
        right = self.deep(root.right)+1

        if self.__max < left+right:
            self.__max = left+right
        
        return max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.deep(root)
        return self.__max
        
# @lc code=end

