#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    __ans = []

    def __init__(self):
        self.__ans = []

    def level(self, root: TreeNode, k: int):
        if root==None:
            return
        if len(self.__ans)==k:
            self.__ans.append([])
        self.__ans[k].append(root.val)
        self.level(root.left, k+1)
        self.level(root.right,k+1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.level(root, 0)
        return self.__ans

# @lc code=end

